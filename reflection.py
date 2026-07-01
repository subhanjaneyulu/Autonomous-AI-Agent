from langchain_core.output_parsers import StrOutputParser

from config import llm
from prompts import reflection_prompt


parser = StrOutputParser()

reflection_chain = reflection_prompt | llm | parser


def review_document(document: str) -> str:
    """
    Reviews the generated document and
    returns APPROVED or improvement suggestions.
    """

    response = reflection_chain.invoke(
        {
            "document": document
        }
    )

    return response