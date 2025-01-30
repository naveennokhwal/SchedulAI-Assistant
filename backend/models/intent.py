import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class IntentClassifier:
    def __init__(self, text):
        self.text = text
        # Load the saved model and tokenizer
        self.MODEL_NAME = r"backend\models\intent_model"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL_NAME)
        self.intent_to_label = {'add_task': 0,
         'add_remainder': 1,
         'update_remainder': 2,
         'delete_remainder': 3,
         'delete_task': 4,
         'update_task': 5}
        self.label_to_intent  = {v: k for k, v in self.intent_to_label.items()}
        

    def predict_intent(self):
        inputs = self.tokenizer(
            self.text,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=128,
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=-1).item()
        return predicted_class

    def result(self):
        predicted_class = self.predict_intent()
        return self.label_to_intent[predicted_class]
