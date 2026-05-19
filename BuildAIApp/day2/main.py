from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI
from dotenv import load_dotenv
from database import engine, SessionLocal
from models import Base, ChatHistory
import os

load_dotenv()

Base.metadata.create_all(bind=engine)

client = OpenAI(
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():

    return '''
    <html>

    <head>

        <title>Enterprise AI Chat</title>

    </head>

    <body style="font-family: Arial; padding: 30px;">

        <h2>Enterprise AI Chat Application</h2>

        <form action="/chat" method="post">

            <textarea
                name="message"
                rows="8"
                cols="80"
                placeholder="Enter your prompt here..."
            ></textarea>

            <br><br>

            <button type="submit">
                Send
            </button>

        </form>

    </body>

    </html>
    '''

@app.post("/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):

    completion = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    ai_response = completion.choices[0].message.content

    db = SessionLocal()

    chat_record = ChatHistory(
        user_message=message,
        ai_response=ai_response
    )

    db.add(chat_record)

    db.commit()

    db.close()

    return f'''
    <html>

    <head>

        <title>AI Response</title>

    </head>

    <body style="font-family: Arial; padding: 30px;">

        <h2>AI Response</h2>

        <hr>

        <pre style="
            white-space: pre-wrap;
            font-size: 16px;
            line-height: 1.6;
        ">
{ai_response}
        </pre>

        <br>

        <a href="/">
            Go Back
        </a>

    </body>

    </html>
    '''
