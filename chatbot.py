from openai import OpenAI

# Create an instance of the API library
# OpenAI() will automatically pull the key from the system variable
client = OpenAI()

# ask user to input text. This script is run via the command line 
# for now so the input() function is required
user_input = input("\nAsk me something...\n\n")

model = "gpt-3.5-turbo",

messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]

# Chat Completions API, formatted as an object where model and
# messages are required
response = client.chat.completions.create(
    
)