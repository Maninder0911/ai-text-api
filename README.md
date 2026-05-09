# AI Job Assistant

AI Job Assistant is a Python-based AI-powered backend application designed to assist users with resume improvement, interview preparation, grammar correction, text summarization, and career guidance using OpenAI APIs.

The project demonstrates practical AI integration with backend development using FastAPI, REST APIs, and Streamlit.

---

## Features

- AI-powered resume analysis
- Resume improvement suggestions
- Interview question answering
- Grammar correction and text improvement
- Text summarization
- Skill recommendation system
- Session-based conversational memory
- REST API architecture using FastAPI
- Streamlit frontend integration
- Logging and centralized exception handling

---

## Tech Stack

### Backend
- Python 3
- FastAPI
- OpenAI API

### Frontend
- Streamlit

### Database
- MySQL

### Other Libraries
- Uvicorn
- Pydantic
- python-dotenv

---

## Project Structure

```text
ai-job-assistant/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── config.py
├── models.py
│   
├── services/
│   ├── ai_service.py


```

---

## Features Implemented

### Resume Analyzer
Analyzes resume content and provides improvement suggestions based on clarity, structure, and technical skills.

### Interview Assistant
Answers interview-related questions using AI-generated responses.

### Grammar Improvement
Improves grammar, sentence structure, and readability of user-provided text.

### Text Summarization
Generates concise summaries from large text input.

### Skill Suggestions
Suggests relevant technical skills and learning paths based on user profile and experience.

### Conversational Memory
Maintains session-based memory for contextual conversations.

---

## API Endpoint

### Process Request

```http
POST /process
```

### Sample Requests

```json
{
  "session_id": "user1",
  "input": "Summarize the use of AI in Healthcare Sector",
  "context": ""
}

{
  "session_id": "user1",
  "input": "How does machine learning work?",
  "context": "Machine learning is a branch of artificial intelligence that enables systems to learn from data. It uses algorithms to identify patterns and make decisions without explicit programming.",
}
```

### Supported Tasks

- summarize
- improve_grammar
- answer_question
- suggest_skills
- analyze_resume
- improve_resume

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Maninder0911/ai-job-assistant.git
cd ai-job-assistant
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root directory.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Running the FastAPI Server

```bash
uvicorn app:app --reload
```

API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## Future Enhancements

- Resume upload support (PDF/DOCX)
- Export improved resumes
- Authentication and user management
- Job recommendation integration
- Vector database memory
- Cloud deployment support

---

## Learning Outcomes

This project helped in gaining hands-on experience with:
- FastAPI development
- REST API design
- OpenAI API integration
- AI-powered backend applications
- Prompt engineering
- Streamlit integration
- Exception handling and logging
- Session-based conversational workflows

---

## Author

Maninder Singh