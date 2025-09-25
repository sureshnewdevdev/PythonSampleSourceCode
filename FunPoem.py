# Fun Poem Generator Using GPT-2

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
theme = input("Enter a theme for your poem: ")
result = generator(f"Write a short poem about {theme}:", max_length=50)
print("\nAI-generated poem:\n", result[0]['generated_text'])
