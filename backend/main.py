from fastapi import FastAPI
from backend.agents.tech_ai.main import router as tech_ai_router

app = FastAPI(title="AURA Platform")

app.include_router(tech_ai_router)
