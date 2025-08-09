import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model & tokenizer from the local directory
model = AutoModelForSequenceClassification.from_pretrained("ticket_classifier_model")
tokenizer = AutoTokenizer.from_pretrained("ticket_classifier_model")
model = AutoModelForSequenceClassification.from_pretrained("samreenss2414/ticket-classifier-model")
tokenizer = AutoTokenizer.from_pretrained("samreenss2414/ticket-classifier-model")


# Your id2label mapping from training
id2label = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

def classify_ticket(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    return id2label[predicted_class_id]

# Gradio UI
demo = gr.Interface(
    fn=classify_ticket,
    inputs=gr.Textbox(lines=4, label="Enter Support Ticket"),
    outputs=gr.Label(label="Predicted Category"),
    title="Customer Support Ticket Classifier (DistilBERT)"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
