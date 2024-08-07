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

def get_api_chat_response_message (model, messages):

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
# user_input = input("\nAsk me something...\n\n")

model = "gpt-3.5-turbo"

book_title = "The Forgotten House"

plot_description = """In the heart of the bustling metropolis of Astoria, the old Henderson House stands as a
silent sentinel, its imposing facade a stark contrast to the modern skyscrapers that
surround it. Once a grand mansion, it now sits abandoned, its windows broken, its
once-luxurious gardens now a tangle of weeds and ivy. The house is said to be haunted, its
halls echoing with the whispers of a tragic past.

When seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately
drawn to the mystery of the old house. Despite the warnings of her new friends, Mia
becomes determined to uncover the truth behind the rumors that surround it.
As Mia delves deeper into the history of the Henderson House, she discovers a dark and
twisted tale. The house was once the home of the wealthy and influential Henderson
family, until one fateful night when a series of mysterious disappearances rocked the city.
The family was never seen again, and the house was left abandoned, a grim reminder of
the tragedy that had befallen it.

Determined to unravel the mystery, Mia enlists the help of her friends, including the
charming and enigmatic Alex. Together, they embark on a dangerous journey into the heart
of the city's dark underbelly, where they must confront not only the malevolent spirits that
haunt the Henderson House but also the sinister forces that seek to keep its secrets buried.

As they dig deeper, Mia and her friends uncover a web of lies and deceit that stretches
back decades, and they realize that the key to solving the mystery may lie closer to home
than they ever imagined. But with each step closer to the truth, they also draw closer to
danger, and Mia must confront her own fears if she is to uncover the secrets of the
Henderson House and escape its haunting legacy."""

book_reviews = {
    "I read The Forgotten House and found it to be average. The writing was decent, and the plot was somewhat engaging, but it didn't leave a lasting impression on me.",
    "I found The Forgotten House to be predictable and lacking in originality. The plot felt formulaic, and the characters were one-dimensional. Overall, a disappointing read.",
    "A thrilling tale that kept me on the edge of my seat! The author expertly weaves together mystery, suspense, and a touch of the supernatural. A must-read for fans of young adult fiction!",
    "The writing style of this book didn't resonate with me. I found it to be overly descriptive, which slowed down the pacing of the story. The characters also felt clichéd and uninteresting.",
    "I struggled to connect with the characters in this book. They felt flat and underdeveloped, which made it difficult to care about their fates. The plot, while intriguing, was ultimately let down by the lack of depth in the characters.",
    "I couldn't put this book down! The characters are relatable, the plot is engaging, and the setting is beautifully described. A captivating read from start to finish!", 
    "The Forgotten House was an okay read. The story was interesting enough to keep me turning the pages, but I didn't feel particularly invested in the characters or the outcome.",
    "The Forgotten House is a hauntingly beautiful story that lingers long after the final page. The author's descriptive prose brings the city to life, while the mystery keeps you guessing until the end. Highly recommend!",
    "An atmospheric masterpiece! The author's vivid descriptions make you feel like you're right there in the city, exploring its secrets alongside the characters. A captivating and immersive read!",
    "While the premise of The Forgotten House was intriguing, I felt that the execution fell short. The story lacked depth and complexity, and the ending left me feeling unsatisfied. Overall, not a book I would recommend.",
    "The Forgotten House was an alright book. The premise was intriguing, but the execution fell a bit flat for me. I think it could have been more engaging with stronger character development.",
    "A gripping mystery with a supernatural twist! The characters are well-developed, the plot is fast-paced, and the setting is richly detailed. A definite must-read for fans of the genre!",
    "The Forgotten House started off strong, but I found the middle portion of the book to be slow and repetitive. The resolution felt rushed and unsatisfying, leaving me wanting more.",
    "I finished The Forgotten House and felt indifferent about it. The story was fine, but it didn't leave a lasting impression on me. It's a decent read if you're looking for something light."
}

book_reviews_with_sentiments = []

for sentiment in book_reviews:
    reviews_prompt = f"""
    Determine the sentiment of the current book review in the dictionary blow, in between < and >, as a single word, positive or negative.

    <{book_reviews}>
    """

plot_prompt = f"""

Summarize the text below, in between < and >, in no more than 100 words.

<{plot_description}>
Refer to the book title {book_title} within the summary. Write this as one paragraph and make the summarization exciting. This text will be used to promote the launch of a new book."
"""

messages = [
    {"role": "system", "content": "You are an assistant that answers as if you’re a detective solving a mystery."},
    {"role": "user", "content": plot_prompt}
]

book_summary = get_api_chat_response_message(model, messages)

#if set_user_input_category(user_input) == "question":
    #response_for_user = "Good question! " + response_for_user

print("\n" + book_summary + "\n")
