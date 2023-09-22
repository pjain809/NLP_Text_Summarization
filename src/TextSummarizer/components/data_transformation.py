
import os
from transformers import AutoTokenizer
from TextSummarizer.logging import logger
from datasets import load_dataset, load_from_disk
from TextSummarizer.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch["dialogue"], max_length = 1024, truncation = True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch["summary"], max_length = 128, truncation = True)

        return {"input_ids": input_encodings["input_ids"],
                "attention_mask": input_encodings["attention_mask"],
                "labels": target_encodings["input_ids"]}

    def convert(self):
        if os.path.exists(os.path.join("artifacts", "data_transformation", "samsum_dataset")):
            logger.info(f"Transformed data already available at \n"
                        f"Path: {os.path.join('artifacts', 'data_transformation', 'samsum_dataset')}")
            return
        else:
            dataset_samsum = load_from_disk(str(self.config.data_path))
            dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
            dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))
