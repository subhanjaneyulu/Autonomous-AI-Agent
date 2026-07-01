from fastapi import FastAPI

from models import RequestModel
from planner import create_execution_plan
from executor import execute_plan
from reflection import review_document
from doc_generator import generate_docx

app = FastAPI(
    title="Autonomous AI Agent",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Autonomous AI Agent API is Running"
    }


@app.post("/agent")
def run_agent(request: RequestModel):

    print("🔥 API HIT")

    print("Planner Started")
    plan = create_execution_plan(request.request)
    print("Planner Completed")

    print("Executor Started")
    document = execute_plan(request.request, plan)
    print("Executor Completed")

    print("Reflection Started")
    review = review_document(document)
    print("Reflection Completed")

    print("DOCX Generation Started")
    file_path = generate_docx(
        document_content=document,
        document_type="Business Proposal"
    )
    print("DOCX Generated")

    return {
        "status": "success",
        "review": review,
        "execution_plan": plan,
        "document": document,
        "document_path": file_path
    }