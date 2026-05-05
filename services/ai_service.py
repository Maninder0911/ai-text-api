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

def get_suggestions(intent):
    if intent == "resume_improve":
        return [
            "Generate a cover letter",
            "Analyze this resume"
        ]
    elif intent == "job_analysis":
        return [
            "Suggest skills for this role",
            "Prepare interview questions"
        ]
    return []

def improve_resume(text: str, intent: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role":"system",
                "content": "Improve this resume text to be professional, concise, and impactful"
            },
            {
                "role":"user",
                "content": text
            }
        ]
    )

    return {
  "response": response.choices[0].message.content,
  "suggestions": get_suggestions(intent)
    }
    #return response.choices[0].message.content

def generate_cover_letter(details: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role":"system",
                "content": "Write a professional cover letter based on the provided details"
            },
            {
                "role":"user",
                "content": details
            }
        ]
    )
    return response.choices[0].message.content

def suggest_skills(role: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role":"system",
                "content": "Suggest key skills required for this role"
            },
            {
                "role":"user",
                "content": role
            }
        ]
    )
    return response.choices[0].message.content

def interview_help(question: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role":"system",
                "content": "Provide a strong, professional answer to this interview question"
            },
            {
                "role":"user",
                "content": question
            }
        ]
    )
    return response.choices[0].message.content

def analyze_job(description: str, intent: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role":"system",
                "content": "Analyze this job description and list key requirements and skills"
            },
            {
                "role":"user",
                "content": description
            }
        ]
    )

    return {
  "response": response.choices[0].message.content,
  "suggestions": get_suggestions(intent)
    }
    #return response.choices[0].message.content

def analyze_resume(text: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role":"system",
                "content": """Analyze the resume and provide:
                1. Strengths
                2. Weaknesses
                3. Missing skills
                4. Suggestions for improvement

                Keep it structured and concise."""
            },
            {
                "role":"user",
                "content": text
            }
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
                "content": """Classify the user request into one of the following categories:
                - summarize: if the user asks to shorten or summarize text
                - grammar: if the user wants grammar correction or sentence improvement
                - question: if the user is asking a general question
                - resume_improve: if the user provides resume-like text or professional background and wants it improved or refined
                - cover_letter: if the user asks to write a cover letter
                - skill_suggestion: if the user asks what skills are needed for a role
                - interview_help: if the user asks for interview answers
                - job_analysis: if the user provides a job description for analysis
                - resume_analysis: if the user asks to analyze a resume

                IMPORTANT RULES:
                - If the input is a paragraph describing experience or background → classify as resume_improve
                - If the user explicitly asks 'what skills are needed' → skill_suggestion
                - If unsure between grammar and resume_improve → choose resume_improve

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
    
    elif intent == "resume_improve":
        result =  improve_resume(user_input,intent)
    
    elif intent == "cover_letter":
        result =  generate_cover_letter(user_input)
    
    elif intent == "skill_suggestion":
        result =  suggest_skills(user_input)
    
    elif intent == "interview_help":
        result =  interview_help(user_input)
    
    elif intent == "job_analysis":
        result =  analyze_job(user_input,intent)

    elif intent == "resume_analysis":
        result =  analyze_resume(user_input)
    
    else:
        result = {"type": "unknown", "result": "Couldn't determine intent"}

    #Add assistant response
    history.append({"role": "assistant", "content": result})

    return result