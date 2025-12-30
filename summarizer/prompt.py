# Alternative v1.2+ import (core package)
from langchain_core.prompts import PromptTemplate


summary_prompt = PromptTemplate(
    input_variables=["document_text"],
    template="""
You are an AI assistant that summarizes documents.

Summarize the following document in **5–10 clear sentences**.
Focus on the main topic, key points, and any important data patterns.
Avoid unnecessary details.

Document:
{document_text}
"""
)
