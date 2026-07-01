from config import llm
from prompts import planner_prompt
from models import PlannerModel


structured_llm = llm.with_structured_output(PlannerModel)

planner_chain = planner_prompt | structured_llm


def create_execution_plan(request: str):

    response = planner_chain.invoke(
        {
            "request": request
        }
    )

    return response