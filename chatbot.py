from openai import OpenAI

# Create an instance of the API library
# OpenAI() will automatically pull the key from the system variable
client = OpenAI()

# ask user to input text. This script is run via the command line 
# for now so the input() function is required
user_input = input("\nAsk me something...\n\n")

# Chat Completions API, formatted as an object where model and
# messages are required
response = client.chat.completions.create(

)