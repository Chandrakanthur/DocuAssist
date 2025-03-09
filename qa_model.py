from langchain.llms import OpenAI

def answer_query(question, relevant_passages):
    llm = OpenAI()
    context = "\n".join(relevant_passages)
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    answer = llm.predict(prompt)
    return answer, context
