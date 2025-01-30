import spacy
import joblib
import numpy as np
import os

class GreetClassifier:
    def __init__(self, text, model_path=r"backend\models\greeting\greeting_classifier.pkl"):
        self.text = text
        self.model_path = model_path
        self.nlp = spacy.load("en_core_web_md")  # Load medium-sized model with word vectors
        self.model = None
        self._load_model()  # Load model if exists

    def _get_embedding(self):
        """Convert text to word embedding using spaCy."""
        return self.nlp(self.text).vector

    def _load_model(self):
        """Load trained model if available."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print("Loaded trained model.")
        else:
            print("No trained model found. Train the model first.")

    def is_greeting(self):
        """Predict if the given text is a greeting (1) or not (0)."""
        if self.model is None:
            raise ValueError("Model not trained. Train the model first using train() method.")

        text_vector = np.array([self._get_embedding()])
        return self.model.predict(text_vector)[0]



