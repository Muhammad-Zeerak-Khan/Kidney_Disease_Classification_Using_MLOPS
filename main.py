from Kidney_Tumor_Classification import logger
from Kidney_Tumor_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Kidney_Tumor_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Kidney_Tumor_Classification.pipeline.stage_03_model_training import ModelTrainingPipeline
from Kidney_Tumor_Classification.pipeline.stage_04_model_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<") 
    data_ingestion_train_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_train_pipeline.main()       
    logger.info(f">>>>> {STAGE_NAME} completed!<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e    
    
STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"*"*20)
    logger.info(f">>>>> {STAGE_NAME} started <<<<<") 
    prepare_base_model_train_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_base_model_train_pipeline.main()
    logger.info(f">>>>> {STAGE_NAME} completed!<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME = "Training Stage"     
try:
    logger.info(f"*"*20)
    logger.info(f">>>>> stage")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> {STAGE_NAME} completed!<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)    
    raise e


STAGE_NAME = "Evaluation Stage"     
try:
    logger.info(f"*"*20)
    logger.info(f">>>>> stage")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> {STAGE_NAME} completed!<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)    
    raise e    