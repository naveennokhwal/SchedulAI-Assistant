import torch
from transformers import BertForTokenClassification, BertTokenizerFast

class EntityExtractor:
    def __init__(self, text):
        self.text = text.split()
        self.label_list = ['O', 'B-TITLE', 'I-TITLE', 'B-DATE', 'I-DATE', 'B-TIME', 'I-TIME']

        # Load the trained model and tokenizer
        self.model = BertForTokenClassification.from_pretrained(r'backend\models\ner_model')
        self.tokenizer = BertTokenizerFast.from_pretrained(r'backend\models\ner_model')
    
    # Function for inference
    def predict_ner(self):
        # Tokenize the input text
        inputs = self.tokenizer(self.text, return_tensors="pt", padding=True, truncation=True, is_split_into_words=True, max_length=128)
    
        # Get predictions
        with torch.no_grad():
            outputs = self.model(**inputs)
    
        # Get predicted labels
        predictions = torch.argmax(outputs.logits, dim=2)
    
        # Decode the predictions (convert label indices back to label names)
        predicted_labels = predictions[0].cpu().numpy()  # Assuming batch size is 1
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    
        # Map predictions back to label names
        label_map = {i: label for i, label in enumerate(self.label_list)}  # Use the same label list from earlier
        predicted_labels = [label_map[label] for label in predicted_labels]
    
        # Filter out special tokens [CLS], [SEP], and padding
        filtered_tokens = []
        filtered_labels = []
        for token, label in zip(tokens, predicted_labels):
            if token not in ['[CLS]', '[SEP]'] :  # Ignore special tokens and labels that are "O"
                filtered_tokens.append(token)
                filtered_labels.append(label)
    
        # Return the tokens and their predicted labels
        return list(zip(filtered_tokens, filtered_labels))
    
    def extract_entities(self, a):
        title, date, time = [], [], []

        entity_dict = {"B-TITLE": title, "I-TITLE": title, 
                       "B-DATE": date, "I-DATE": date, 
                       "B-TIME": time, "I-TIME": time}

        for word, tag in a:
            if tag in entity_dict:
                if word.startswith("##"):
                    entity_dict[tag][-1] += word[2:]  # Merge with previous word
                else:
                    entity_dict[tag].append(word)  # Add new word

        # Join words to form meaningful phrases
        title = " ".join(title) if title else None
        date = " ".join(date) if date else None
        time = " ".join(time) if time else None

        return [title, date, time]
    
    def result(self):
        output = self.predict_ner()
        entities  = self.extract_entities(output)
        return entities