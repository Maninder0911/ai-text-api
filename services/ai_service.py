from openai import OpenAI
from config import OPEN_API_KEY

client = OpenAI(api_key=OPEN_API_KEY)

def summarize_text(text: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {"role":"system", "content": "You are a helpful assistant. Summarize the text in 3-4 concise sentences. Focus only on key points. Avoid repetition."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content

def improve_grammar(text: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": "You are an expert English editor. Correct grammar, improve clarity, and make the text professional while preserving original meaning."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content

def answer_question(context: str, question: str):
    prompt = f"context:\n{context}\n\nQuestion: {question}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": "Answer ONLY from the provided context. If the answer is not in the context, say: 'Answer not found in the provided context.'"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def classify_intent(user_input: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": """Classify the user request into one of these:
                - summarize
                - grammar
                - question

                Respond with ONLY the category name."""
            },
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip().lower()

def process_input(user_input: str):
    intent = classify_intent(user_input)

    if intent == "summarize":
        return {"type": "summary", "result": summarize_text(user_input)}
    elif intent == "grammar":
        return {"type": "grammar", "result": improve_grammar(user_input)}
    elif intent == "question":
        return {"type": "question", "result": answer_question(user_input, user_input)}
    else:
        return {"type": "unknown", "result": "Couldn't determine intent"}