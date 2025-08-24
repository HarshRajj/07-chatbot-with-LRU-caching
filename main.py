
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from chatbot.prompt_utils import get_prompt_template
from chatbot.rate_limiter import TokenBucket
from chatbot.chat_cli import run_chatbot

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("GOOGLE_API_KEY not found in .env file.")
        return

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
    memory = ConversationBufferMemory(k=4, return_messages=True)
    prompt = get_prompt_template()
    chain = ConversationChain(llm=llm, memory=memory, prompt=prompt)
    bucket = TokenBucket(rate=10, per=60)
    run_chatbot(chain, bucket)

if __name__ == "__main__":
    main()