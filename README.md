
# Gemini CLI Chatbot with LRU Caching (Modular)

## Description
A professional, modular CLI chatbot using Google Gemini 2.0 Flash via LangChain.

**Features:**
- Conversation memory (last 4 turns)
- Token-bucket rate limiting (10 requests/minute)
- In-memory LRU cache (50 entries, 5 min TTL)
- Professional prompt template
- Modular codebase (`chatbot/` package)
- Inactivity timeout (5 min)
- CLI commands: `exit`/`quit`, `cache`, `clear`, `demo`

## Folder Structure

```
intern-2025-q7/
├── main.py
├── requirements.txt
├── .env
├── README.md
├── chatbot/
│   ├── __init__.py
│   ├── cache_utils.py
│   ├── rate_limiter.py
│   ├── prompt_utils.py
│   └── chat_cli.py
```

## Setup

1. **Clone the repository:**
	```bash
	git clone https://github.com/HarshRajj/intern-2025-q7.git
	cd intern-2025-q7
	```
2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
3. **Create a `.env` file** and add your Google API key:
	```
	GOOGLE_API_KEY=your_actual_gemini_api_key_here
	```

## Usage

Run the chatbot:
```bash
python main.py
```

### Supported Commands

| Command      | Description                                 |
| ------------ | ------------------------------------------- |
| exit, quit   | End the conversation                        |
| cache        | Show detailed cache statistics              |
| clear        | Clear all cached entries                    |
| demo         | Demonstrate cache behavior with duplicates  |

## Features

- **Memory:** Remembers last 4 turns for context
- **Rate Limiting:** 10 requests per minute (token bucket)
- **Caching:** LRU cache (50 entries, 5 min TTL) for prompt-response pairs
- **Prompt Template:** Uses a concise, professional prompt for Gemini
- **Timeout:** Exits after 5 minutes of inactivity
- **Modular:** All logic in `chatbot/` package

## Sample Output

```
🤖 Gemini Chatbot with Memory, Rate Limiting, and Caching (type 'exit' or 'quit' to quit)
[Cache: 0/50] You: What is Python?
🔄 [FRESH in 1247.3ms] 
🤖 AI: Python is a high-level programming language...

[Cache: 1/50] You: What is Python?
⚡ [CACHED in 2.1ms] 
🤖 AI: Python is a high-level programming language...

[Cache: 1/50] You: cache
📊 Cache Statistics:
  • Cache hits: 1
  • Cache misses: 1
  • Hit rate: 50.0%
  • Cache size: 1/50
  • Time saved: 1.2s total
  • Avg time saved per hit: 1247.3ms
```

---

## Demo
 
[Run the Google Colab](https://colab.research.google.com/drive/1K116N_6GBlogTjkWmt7_wZKq2Wyw39rq?usp=sharing)
