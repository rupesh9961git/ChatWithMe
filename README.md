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
│   ├── constant/
│   │   └── constant.py    # Model name constants
│   ├── tools/
│   │   └── tool.py        # LangChain tool definitions (e.g. weather)
│   └── langGraph/
│       ├── customerOrder.py   # Customer order flow graph
│       └── learnLangGraph.py  # LangGraph learning examples
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

| Package              | Purpose                                        |
| -------------------- | ---------------------------------------------- |
| `fastapi`            | Web framework for the API                      |
| `uvicorn`            | ASGI server to run FastAPI                     |
| `langchain-ollama`   | LangChain integration for Ollama models        |
| `langchain-core`     | Core LangChain primitives (messages, tools)    |
| `langgraph`          | Build stateful multi-node LLM graphs           |
| `langsmith`          | Tracing and observability for LLM calls        |
| `ollama`             | Ollama Python client                           |
| `pydantic`           | Request/response data validation               |
| `python-dotenv`      | Load environment variables from `.env`         |

To install individually:

```bash
pip install fastapi uvicorn langchain-ollama langchain-core langgraph ollama pydantic python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OLLAMA_API_KEY=your_api_key_here
OLLAMA_BASE_URL=https://api.ollama.com

# LangSmith tracing (optional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=ChatWithMe
```

### 4. Run the backend

```bash
# From project root
.venv/bin/uvicorn Backend.api.main:app --reload
```

The API will be available at `http://localhost:8000`.

Endpoints:

| Method | Path      | Description                                  |
| ------ | --------- | -------------------------------------------- |
| GET    | `/`       | Health check                                 |
| GET    | `/chat`   | Quick test chat (hardcoded question)         |
| POST   | `/askMe`  | Send a message, get a response               |
| POST   | `/stream` | Stream a response                            |
| POST   | `/batch`  | Run a batch of predefined questions          |
| POST   | `/tool`   | Call model with tool use (weather lookup)    |

---

## Frontend Setup

### 1. Install Node dependencies

```bash
npm install --prefix UI
```

Key packages installed:

| Package                | Purpose                              |
| ---------------------- | ------------------------------------ |
| `react` + `react-dom`  | UI framework                         |
| `vite`                 | Dev server and bundler               |
| `@vitejs/plugin-react` | React support for Vite               |
| `react-markdown`       | Render markdown in chat responses    |

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

## LangGraph Examples

Run the customer order flow graph:

```bash
.venv/bin/python -m Backend.langGraph.customerOrder
```

Outputs a step-by-step order flow (customer → search shop → place order → confirm → payment → delivery → feedback) and saves `customer_order_graph.png` to the project root.

---

## Build for Production

```bash
npm run build --prefix UI
```

Output is in `UI/dist/`. Serve it with any static file host or configure FastAPI to serve it directly.

---

## LangSmith Tracing

LangSmith provides observability for all LLM calls. The `/askMe` endpoint is instrumented with `@traceable`.

### Setup

1. Sign up at [smith.langchain.com](https://smith.langchain.com)
2. Go to **Settings → API Keys** and create a new key
3. Add the following to your `.env` (already shown above in environment variables)

### Viewing Traces

Open [https://smith.langchain.com](https://smith.langchain.com) and navigate to your **ChatWithMe** project.

Each POST to `/askMe` will appear as a trace named `askMe` with the underlying LLM call nested as a child span. You can inspect:

- Input message and LLM response
- Token usage and latency
- Full conversation context passed to the model

---

## Reference Documents

| Resource | Description |
| -------- | ----------- |
| [LangGraph](https://www.langchain.com/langgraph) | LangChain's framework for building stateful, multi-agent LLM applications |
| [LangSmith](https://smith.langchain.com) | Observability and tracing platform for LLM applications |
| [FastAPI](https://fastapi.tiangolo.com/) | Official FastAPI documentation — routing, request models, async, and more |
| [Ollama Cloud](https://docs.ollama.com/cloud) | Ollama Cloud API docs — authentication, endpoints, and model usage |
