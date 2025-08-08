# customer_ticket_classifier_llm
This repository is about the customer ticket classifer using LLM model distilBIERT from hugging face. It is deployed to Gradio

Project Overview:-
This project is a machine learning application that classifies customer support tickets into predefined categories using a DistilBERT-based text classification model.
It is built with Hugging Face Transformers, trained on a public dataset, and deployed with an interactive Gradio web interface.

The application can help customer support teams automatically route incoming tickets to the right department, reducing manual effort and improving response times.

Features
Pretrained LLM (DistilBERT) fine-tuned for ticket classification.

End-to-end pipeline:

Data loading & preprocessing with Hugging Face datasets

Model fine-tuning using Trainer

Evaluation with accuracy metrics

Saving & loading trained model

Gradio web interface for real-time predictions.


Project structure

.
├── ticket_classifier_model/   # Saved model & tokenizer

├── app.py                     # Main Gradio app

├── requirements.txt           # Project dependencies

├── Dockerfile                 # Containerization file
└── README.md                  # Project documentation


Dockerized deployment for portability and scalability.


