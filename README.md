# Flask OpenAI Chat Application

A real-time chat application using Flask and OpenAI's API with streaming responses.

## Features
- Real-time streaming responses from OpenAI
- Markdown support for responses
- Conversation history context
- Responsive chat interface
- API key management

## Prerequisites
- Docker
- OpenAI API key

## Installation

1. Pull the Docker image:
    ```sh
    docker pull khhamid/my-chatbot
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 5001:5001 --name flask-openai-chat khhamid/chatbot
    ```

3. Open your browser and navigate to `http://localhost:5001` to access the application.
## Usage

- Obtain an OpenAI API key from the [OpenAI website](https://beta.openai.com/signup/)
- Enter your OpenAI API key on the homepage
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