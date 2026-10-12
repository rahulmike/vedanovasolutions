"""FastAPI Application for VedaNova AI."""
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.models import ChatRequest, ChatResponse, BrandInfoResponse, PromptChip
from backend.orchestrator import orchestrator
from rag.engine import knowledge_base

app = FastAPI(
    title="VedaNova AI API",
    description="Dual-Mode Conversational API (General LLM & Company PDF RAG)",
    version="1.0.0"
)

# Enable CORS for external embeddable website widget support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    """Health check and readiness probe."""
    return {
        "status": "online",
        "app": "VedaNova AI",
        "indexed_documents": len(knowledge_base.indexed_files),
        "total_chunks": len(knowledge_base.chunks)
    }

@app.get("/api/info", response_model=BrandInfoResponse)
def get_brand_info():
    """Returns VedaNova branding metadata and starter prompts."""
    return BrandInfoResponse(
        company_name="VedaNova AI",
        tagline="Holistic Wellness for a Better Tomorrow",
        subtitle="Integrating Ayurveda, Technology and Research for Modern Living",
        prompt_chips=[
            PromptChip(label="What is VedaNova?", prompt="What is VedaNova and what are its core pillars?"),
            PromptChip(label="Tell me about your services", prompt="What are the available wellness services and pricing?"),
            PromptChip(label="How does it work?", prompt="How does the 3-step consultation process work?"),
            PromptChip(label="Refund policy", prompt="What is the cancellation and refund policy?")
        ],
        indexed_documents=knowledge_base.indexed_files,
        total_document_chunks=len(knowledge_base.chunks)
    )

@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """
    Dual-mode chat endpoint:
    - mode="company": Queries VedaNova PDF knowledge base via RAG.
    - mode="general": Open conversational AI.
    """
    try:
        response = orchestrator.process_message(
            message=request.message.strip(),
            mode=request.mode
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
