from langchain_core.output_parsers import StrOutputParser

from config import llm
from prompts import executor_prompt


parser = StrOutputParser()

executor_chain = executor_prompt | llm | parser


def execute_plan(request: str, plan: str) -> str:
    """
    Executes the AI generated execution plan
    and returns the final business document.
    """

    response = executor_chain.invoke(
        {
            "request": request,
            "plan": plan
        }
    )

    return response