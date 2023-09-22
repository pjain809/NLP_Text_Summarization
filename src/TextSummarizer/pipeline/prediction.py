
from TextSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = pipeline("summarization", model=str(self.config.model_path), tokenizer=tokenizer)
        print(f"Dialogue: \n{text}\n")

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print(f"\nModel Summary: \n{output}")

        return output
