import os
from openai import AsyncOpenAI
from chainlit.playground.providers.openai import ChatOpenAI
from dotenv import load_dotenv

print("all_ok!")

load_dotenv() 

OEPNAI_API_KEY=os.getenv("OPENAI_API_KEY")

client=AsyncOpenAI(api_key=OEPNAI_API_KEY)

print("client has created")