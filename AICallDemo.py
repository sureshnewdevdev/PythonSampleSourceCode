# Sentiment Analysis Demo with Hugging Face Transformers

from transformers import pipeline

# Create the sentiment analysis pipeline with a specific model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

print("Welcome to the AI Sentiment Analyzer!")
print("Type a sentence to analyze its sentiment (type 'exit' to quit).")

while True:
    user_input = input("\nEnter a sentence: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    result = sentiment_pipeline(user_input)
    label = result[0]['label']
    score = result[0]['score']
    print(f"Sentiment: {label} (confidence: {score:.2f})")
