# Flask OpenAI Chat Application

A real-time chat application using Flask and OpenAI's API with streaming responses.

## Features
- Real-time streaming responses from OpenAI
- Markdown support for responses
- Conversation history context
- Responsive chat interface
- API key management

## Prerequisites
- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd flask-openai-chat
```
2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install flask python-dotenv openai markdown2
```
## Configuration
1. Get your (OpenAI API)[https://platform.openai.com/api-keys] key from OpenAI Platform
2. Run the application:
```bash
python app.py
``` 
3. Open the application in your browser:
```bash
http://127.0.0.1:5001/
``` 
4. Enter your OpenAI API key in the application settings
## Project Structure
```
flask-openai-chat/
├── static/
├── templates/
│   ├── chat.html
│   └── setup.html
├── modules/
│   └── openai_handler.py
├── app.py
└── README.md
```
## Usage

- Visit the setup page to enter your OpenAI API key
- Start chatting in the main interface
- Use Shift+Enter for new lines in messages
- Press Enter to send messages
## Features
- Streaming responses
- Markdown rendering
- Conversation context
- Mobile-responsive design
- Real-time updates
## Development
- The application uses Flask for the backend
- AlpineJS for reactive frontend
- TailwindCSS for styling
- Server-Sent Events for streaming
## Notes
- Default model: gpt-4o-mini
- Default temperature: 0.7
- Responses support markdown formatting