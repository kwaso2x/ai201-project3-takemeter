from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model + tokenizer from the folder you downloaded from Google Drive
MODEL_PATH = "takemeter-model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Label mapping (make sure this matches your training notebook)
id2label = {
    0: "pro_lebron",
    1: "pro_jordan",
    2: "neutral"
}

def classify_comment(text):
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Run through model
    outputs = model(**inputs)

    # Get predicted class index
    predicted_class_id = torch.argmax(outputs.logits, dim=1).item()

    # Convert index to label
    return id2label[predicted_class_id]

if __name__ == "__main__":
    print("Welcome to the TakeMeter! Type a comment to classify it.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter a comment: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        prediction = classify_comment(user_input)
        print("Prediction:", prediction)
        print()
