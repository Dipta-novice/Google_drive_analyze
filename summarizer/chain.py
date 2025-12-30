from summarizer.llm import get_llm
from summarizer.prompt import summary_prompt

def summarize_text(text: str) -> str:
    llm = get_llm()

    # Create runnable chain
    chain = summary_prompt | llm

    response = chain.invoke({
        "document_text": text[:8000]  # safety truncation
    })

    return response.content
