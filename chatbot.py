from openai import OpenAI

# Create an instance of the API library
# OpenAI() will automatically pull the key from the system variable
client = OpenAI()

def set_user_input_category (user_input) :
    #check if any text in input indicates there is a question
    question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
    return "statement"

def q_and_a (model, messages):

    # Chat Completions API, formatted as an object where model and
    # messages are required
    response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # Extract tje message content
    response_content = response.choices[0].message.content

    return response_content

# ask user to input text. This script is run via the command line 
# for now so the input() function is required
user_input = input("\nAsk me something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {"role": "system", "content": "You are an assistant that answers as if you’re a detective solving a mystery."},
    {"role": "user", "content": user_input}
]

response_for_user = q_and_a(model, messages)

if set_user_input_category(user_input) == "question":
    response_for_user = "Good question! " + response_for_user

print("\n" + response_for_user + "\n")
