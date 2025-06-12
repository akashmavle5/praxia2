import ollama

# Choose the Meditron model (e.g., 'meditron:7b')
model_name = 'meditron'

# Define the user prompt
prompt = "What are the symptoms of a common cold?"

# Use the generate function for a single prompt/response
result = ollama.generate(model=model_name, prompt=prompt)

# Print the model's response
print(result['response'])

# Alternatively, use the chat function for conversational interactions
messages = [
    {'role': 'user', 'content': 'What are the symptoms of a common cold?'},
]

chat_response = ollama.chat(model=model_name, messages=messages)

# Print the chat response
print(chat_response['message']['content'])
