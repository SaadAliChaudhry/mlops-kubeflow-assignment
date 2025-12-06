# src/pipelinecomponents.py
import kfp
from kfp.dsl import component, Input, Output, Dataset, Model, Metrics

@component(packages_to_install=['pandas', 'dvc', 'scikit-learn', 'joblib'])
def data_extraction(output_data: Output[Dataset]):
    import pandas as pd
    df = pd.read_csv('data/raw/boston_housing.csv')
    df.to_csv(output_data.path, index=False)
    print("Data extracted:", df.shape)

@component(packages_to_install=['pandas', 'scikit-learn', 'joblib'])
def data_preprocessing(
    input_data: Input[Dataset],
    train_data: Output[Dataset],
    test_data: Output[Dataset],
    scaler_model: Output[Model]
):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    import joblib

    df = pd.read_csv(input_data.path)
    X = df.drop('PRICE', axis=1)
    y = df['PRICE']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    train_df = pd.DataFrame(X_train_scaled, columns=X.columns)
    train_df['PRICE'] = y_train.values
    train_df.to_csv(train_data.path, index=False)

    test_df = pd.DataFrame(X_test_scaled, columns=X.columns)
    test_df['PRICE'] = y_test.values
    test_df.to_csv(test_data.path, index=False)

    joblib.dump(scaler, scaler_model.path)
    print("Preprocessing done")

@component(packages_to_install=['pandas', 'scikit-learn', 'joblib'])
def model_training(train_data: Input[Dataset], model: Output[Model]):
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    import joblib

    df = pd.read_csv(train_data.path)
    X_train = df.drop('PRICE', axis=1)
    y_train = df['PRICE']

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    joblib.dump(rf, model.path)
    print("Model trained")

@component(packages_to_install=['pandas', 'scikit-learn', 'joblib'])
def model_evaluation(test_data: Input[Dataset], model: Input[Model], metrics: Output[Metrics]):
    import pandas as pd
    import joblib
    from sklearn.metrics import mean_squared_error, r2_score

    df = pd.read_csv(test_data.path)
    X_test = df.drop('PRICE', axis=1)
    y_test = df['PRICE']

    rf = joblib.load(model.path)
    y_pred = rf.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    metrics.log_metric("mse", mse)
    metrics.log_metric("r2", r2)
    print(f"MSE: {mse}, R2: {r2}")
