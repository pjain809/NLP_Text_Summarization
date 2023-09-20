
import os
import zipfile
from pathlib import Path
import urllib.request as request
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Downloads the specified file as in `config.yaml` and saves at the `local_data_file` path.
        """

        if not os.path.exists(self.config.local_data_file):
            _, _ = request.urlretrieve(url=self.config.source_URL,
                                       filename=self.config.local_data_file)
            logger.info(f"Input data has been downloaded and saved at \n"
                        f"Path: {self.config.local_data_file} \n"
                        f"Size: {get_size(Path(self.config.local_data_file))}")
        else:
            logger.info(f"Input data is already available at \n"
                        f"Path: {self.config.local_data_file} \n"
                        f"Size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the zip file contents onto the `unzip_dir` path.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Input data has been extracted at \n"
                    f"Path: {self.config.unzip_dir} \n")

