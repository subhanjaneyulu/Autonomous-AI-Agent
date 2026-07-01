import streamlit as st

from planner import create_execution_plan
from executor import execute_plan
from reflection import review_document
from doc_generator import generate_docx


st.set_page_config(
    page_title="Autonomous AI Agent",
    layout="wide"
)

st.title("Autonomous AI Document Generator")

st.markdown(
    """
Generate professional business documents using an autonomous AI workflow.

Workflow:

Planning

Execution

Reflection

DOCX Generation
"""
)

user_request = st.text_area(
    "Enter your request",
    height=150,
    placeholder="Example: Create a business proposal for an AI based Hospital Management System."
)

if st.button("Run Agent", use_container_width=True):

    if not user_request.strip():
        st.warning("Please enter a request.")
        st.stop()

    with st.spinner("Planning..."):

        plan = create_execution_plan(user_request)

    st.success("Planning Completed")

    st.subheader("Execution Plan")

    st.json(plan)

    with st.spinner("Generating Document..."):

        document = execute_plan(
            user_request,
            plan
        )

    st.success("Document Generated")

    st.subheader("Generated Document")

    st.markdown(document)

    with st.spinner("Reviewing Document..."):

        review = review_document(document)

    st.subheader("Reflection")

    if review.strip() == "APPROVED":

        st.success(review)

    else:

        st.warning(review)

    with st.spinner("Generating Word Document..."):

        file_path = generate_docx(
            document,
            plan.document_type
        )

    st.success("Word Document Generated Successfully")

    st.write(file_path)

    with open(file_path, "rb") as file:
        st.download_button(
            label="Download Word Document",
            data=file,
            file_name=file_path.split("\\")[-1],
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )