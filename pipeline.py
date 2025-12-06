# pipeline.py
from kfp import dsl, compiler
from src.pipelinecomponents import data_extraction, data_preprocessing, model_training, model_evaluation

@dsl.pipeline(name='Boston Housing MLOps Pipeline', description='End-to-end pipeline')
def ml_pipeline():
    extract = data_extraction()
    preprocess = data_preprocessing(input_data=extract.outputs['output_data'])
    train = model_training(train_data=preprocess.outputs['train_data'])
    eval_task = model_evaluation(test_data=preprocess.outputs['test_data'], model=train.outputs['model'])

if __name__ == '__main__':
    compiler.Compiler().compile(ml_pipeline, 'pipeline.yaml')
    print("Compiled pipeline to pipeline.yaml")
