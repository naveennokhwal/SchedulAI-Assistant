import json

def transform_json(input_file, output_file, intent_value):
    """
    Transforms the input JSON file to the desired structure with 'intent' added.
    
    Parameters:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to save the transformed JSON file.
        intent_value (str): The intent value to be added to each entry.
    """
    try:
        # Load the input JSON file
        with open(input_file, 'r') as infile:
            data = json.load(infile)
        
        # List to store transformed data
        transformed_data = []

        # Process each entry
        for entry in data:
            transformed_entry = {
                "text": entry["text"],
                "intent": intent_value,
                "entities": [
                    {"entity": label["labels"][0], "value": label["text"]}
                    for label in entry["label"]
                ]
            }
            transformed_data.append(transformed_entry)
        
        # Save the transformed data to the output file
        with open(output_file, 'w') as outfile:
            json.dump(transformed_data, outfile, indent=4)
        
        print(f"Transformation successful! Updated JSON saved to: {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = r"C:\Learning\Machine-Learning\Deep_Learning_WorkSpace\projects\Scheduler\data collection\data\update_task.json"  # Path to the input JSON file
output_file = r"C:\Learning\Machine-Learning\Deep_Learning_WorkSpace\projects\Scheduler\data collection\data\new_update_task.json"  # Path to save the transformed JSON
intent_value = "update_task"  # Intent value to add to each entry

transform_json(input_file, output_file, intent_value)
