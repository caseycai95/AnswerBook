from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Answerbook!"}


@app.get("/answer")
def get_answer(question: str = Query(None, description="The question you want to ask")):
    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty. Please provide a valid question."
        )

    gpt_answer = get_answer_from_chatgpt(question)
    return {"question": f"hello, your question is {question}",
            "gpt_answer": {gpt_answer}}


def get_answer_from_chatgpt(question: str):
    # Use OpenAI's ChatCompletion API to generate a response using GPT-4
    response = openai.chat.completions.create(model="gpt-4",  # Use GPT-4
    messages=[
        {"role": "system", "content": "You are a sage."},
        {"role": "user", "content": "provide a complete wisdom random sentence with zen spirit: " + question}
    ],
    max_tokens=50,  # Limit the length of the response
    temperature=1  # Controls randomness
    )

    # Extract and return the generated text
    return response.choices[0].message.content.strip()