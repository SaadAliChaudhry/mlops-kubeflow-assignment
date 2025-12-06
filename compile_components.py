# compile_components.py
from src.pipelinecomponents import data_extraction, data_preprocessing, model_training, model_evaluation
from kfp import compiler
import os

os.makedirs('components', exist_ok=True)
compiler.Compiler().compile(data_extraction, 'components/data_extraction.yaml')
compiler.Compiler().compile(data_preprocessing, 'components/data_preprocessing.yaml')
compiler.Compiler().compile(model_training, 'components/model_training.yaml')
compiler.Compiler().compile(model_evaluation, 'components/model_evaluation.yaml')
print("Components compiled")
