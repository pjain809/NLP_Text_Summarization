
import os
from TextSummarizer.logging import logger
from TextSummarizer.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file == "dataset_dict.json":
                    continue
                if file not in self.config.ALL_REQUIRED_FILES or \
                        len(os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset", file))) == 0:
                    validation_status = False

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation Status: {validation_status}")

            logger.info(f"Data Validation has been Completed.\n"
                        f"Validation Status : {validation_status}")
            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e
