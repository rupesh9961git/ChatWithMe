# Chat with Me

An AI chat application with a FastAPI backend and React frontend, powered by Ollama LLMs.

---

## Project Structure

```text
ChatWithMe/
├── Backend/
│   ├── api/
│   │   └── main.py        # FastAPI app & endpoints
│   ├── model/
│   │   └── model.py       # LLM model wrapper
│   └── constant/
│       └── constant.py    # Model name constants
├── UI/                    # React (Vite) frontend
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Prerequisites

| Tool    | Version | Install                                    |
| ------- | ------- | ------------------------------------------ |
| Python  | 3.11+   | [python.org](https://python.org)           |
| Node.js | 18+     | [nodejs.org](https://nodejs.org)           |
| npm     | 9+      | Included with Node.js                      |

---

## Backend Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

Key packages installed:

| Package            | Purpose                                  |
| ------------------ | ---------------------------------------- |
| `fastapi`          | Web framework for the API                |
| `uvicorn`          | ASGI server to run FastAPI               |
| `langchain-ollama` | LangChain integration for Ollama models  |
| `ollama`           | Ollama Python client                     |
| `pydantic`         | Request/response data validation         |
| `python-dotenv`    | Load environment variables from `.env`   |

To install individually:

```bash
pip install fastapi uvicorn langchain-ollama ollama pydantic python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OLLAMA_API_KEY=your_api_key_here
OLLAMA_BASE_URL=https://api.ollama.com
```

### 4. Run the backend

```bash
# From project root
.venv/bin/uvicorn Backend.api.main:app --reload
```

The API will be available at `http://localhost:8000`.

Endpoints:

| Method | Path     | Description                        |
| ------ | -------- | ---------------------------------- |
| GET    | `/`      | Health check                       |
| GET    | `/chat`  | Quick test chat                    |
| POST   | `/askMe` | Send a message, get a response     |

---

## Frontend Setup

### 1. Install Node dependencies

```bash
npm install --prefix UI
```

Key packages installed:

| Package                | Purpose                      |
| ---------------------- | ---------------------------- |
| `react` + `react-dom`  | UI framework                 |
| `vite`                 | Dev server and bundler       |
| `@vitejs/plugin-react` | React support for Vite       |

### 2. Run the frontend

```bash
# From project root
npm run dev --prefix UI
```

The UI will be available at `http://localhost:5173`.

> The Vite dev server proxies `/askMe` requests to `http://localhost:8000` automatically — no CORS configuration needed.

---

## Running Locally (Full Stack)

Open **two terminals** from the project root:

### Terminal 1 — Backend

```bash
source .venv/bin/activate
uvicorn Backend.api.main:app --reload
```

### Terminal 2 — Frontend

```bash
npm run dev --prefix UI
```

Then open [http://localhost:5173](http://localhost:5173) in your browser.

---

## Build for Production

```bash
npm run build --prefix UI
```

Output is in `UI/dist/`. Serve it with any static file host or configure FastAPI to serve it directly.

---

## Reference Documents

| Resource | Description |
| -------- | ----------- |
| [LangGraph](https://www.langchain.com/langgraph) | LangChain's framework for building stateful, multi-agent LLM applications |
| [FastAPI](https://fastapi.tiangolo.com/) | Official FastAPI documentation — routing, request models, async, and more |
| [Ollama Cloud](https://docs.ollama.com/cloud) | Ollama Cloud API docs — authentication, endpoints, and model usage |
