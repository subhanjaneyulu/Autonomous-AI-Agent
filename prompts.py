from langchain_core.prompts import ChatPromptTemplate


#Planner Prompt
planner_prompt = ChatPromptTemplate.from_template("""
    You are the Planning Module of an Autonomous AI Agent.

    Your job is to create an internal execution plan.

    User Request:

    {request}

    Rules:

    - Do NOT generate the final document.
    - Create only executable AI tasks.
    - Generate assumptions if information is missing.
    - Keep the plan concise and logical.
""")

    
#Executor Prompt#

executor_prompt = ChatPromptTemplate.from_template("""
    You are an AI Document Generation Agent.

    You have already received an execution plan from the planning module.

    User Request:
    {request}

    Execution Plan:
    {plan}

    Your task is to execute the plan and generate a professional business document.

    Instructions:

    - Follow the execution plan.
    - Make reasonable assumptions when required.
    - Use professional business language.
    - Include appropriate headings.
    - Keep the document well structured.
    - Do NOT explain your reasoning.
    - Return only the final document.
""")



#Reflection Prompt#

reflection_prompt = ChatPromptTemplate.from_template("""
    You are an AI Quality Assurance Agent.

    Your responsibility is to review the generated business document.

    Document:

    {document}

    Review the document using the following checklist:

    - Does it have a clear title?
    - Does it contain an Executive Summary?
    - Is the Introduction present?
    - Are all sections logically organized?
    - Is the language professional?
    - Is there a Conclusion?
    - Is the document complete?

    If the document satisfies all checks, reply only with:

    APPROVED

    Otherwise reply in the following format:

    NOT APPROVED

    Reason:
    - ...
    - ...
""")