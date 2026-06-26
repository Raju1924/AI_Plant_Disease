from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model="gpt2"
)

result = generator(
    "Tomato Early Blight disease symptoms and treatment:",
    max_length=100,
    num_return_sequences=1
)

print(result[0]["generated_text"])
