from openai import OpenAI
from config import OPEN_API_KEY

client = OpenAI(api_key=OPEN_API_KEY)

conversation_memory = {}

def summarize_text(text: str, history: list = None):
    messages = []

    messages.append({
        "role": "system", 
        "content": "You are a helpful assistant. Summarize the text in 3-4 concise sentences. Focus only on key points. Avoid repetition."

    })

    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": text
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=messages
    )

    return response.choices[0].message.content

def improve_grammar(text: str, history: list = None):
    messages = []

    messages.append({
        "role": "system", 
        "content": "You are an expert English editor. Correct grammar, improve clarity, and make the text professional while preserving original meaning."

    })

    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": text
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=messages
    )

    return response.choices[0].message.content

def answer_question(question: str, context: str = None, history: list = None):
    messages = []
   
    #System instruction
    if context:
        messages.append({
            "role": "system",
            "content": "Answer ONLY from the provided context. If the answer is not in the context, say: 'Answer not found in the provided context.'"
        })

    else:
        messages.append({
            "role": "system",
            "content": "Answer the question clearly and concisely."
        })

    #Add conversation history
    if history:
        messages.extend(history)

    #Add context if provided
    if context:
        messages.append({
            "role": "user",
            "content": f"context:\n{context}"
        })

    #Add actual question
    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages= messages
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

def process_input(user_input: str, session_id: str, context: str=None):
    
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    history = conversation_memory[session_id]

    intent = classify_intent(user_input)

    if intent == "summarize":
        result =  summarize_text(text = user_input, history = history)
    elif intent == "grammar":
        result =  improve_grammar(text = user_input, history=history)
    elif intent == "question":
        result =  answer_question(question = user_input, context=context, history=history)
    else:
        result = {"type": "unknown", "result": "Couldn't determine intent"}

    #Add assistant response
    history.append({"role": "assistant", "content": result})

    return result