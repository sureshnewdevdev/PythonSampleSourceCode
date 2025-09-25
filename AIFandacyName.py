from transformers import pipeline

name_gen = pipeline("text-generation", model="gpt2")
character_type = input("Enter a type (wizard, dragon, robot, etc.): ")
result = name_gen(f"Suggest a unique {character_type} name:", max_length=15)
print("\nAI-generated name:\n", result[0]['generated_text'])
