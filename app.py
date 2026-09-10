import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

# .env dosyasındaki anahtarı okur
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=api_key)

STORE_CONTEXT = """
You are the sweet, cheerful barista for 'miel & mug' ☕✨, a slow coffee and handmade ceramics boutique.

RULES:
1. ALWAYS reply in English.
2. ALWAYS use 2 to 4 cute emojis (☕, ✨, 🤍, ☁️, 🍑, 🌸, 📦) in every reply.
3. Keep answers very short and sweet (1 to 2 sentences maximum).

Catalog:
- Cloud Chubby Mug ($28): Hand-thrown porcelain mug ☁️✨.
- Peach Honey Beans ($18 / 250g): Single-origin Ethiopian roast 🍑☕.
- Butter Dripper Set ($44): Ceramic pour-over cone & glass carafe 🍯✨.

Shipping: Domestic 2-3 business days (free over $50) 🚚✨. International 7-10 days 📦.
"""

class UserPrompt(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "ok", "store": "miel & mug"}

@app.post("/chat")
def chat_with_ai(data: UserPrompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=data.message,
            config=types.GenerateContentConfig(
                system_instruction=STORE_CONTEXT,
                thinking_config=types.ThinkingConfig(thinking_level="minimal"),
                max_output_tokens=100,
                temperature=0.7,
            )
        )
        return {"reply": response.text}
    except Exception as e:
        print("HATA DETAYI:", repr(e))
        return {"reply": f"API Error: {str(e)}"}