# GirlfriendGPT - Streamlit Cloud Version

This is a simplified version of GirlfriendGPT optimized for deployment via Docker.

## Features

* Customizable AI companion with different personalities
* Interactive chat interface
* Predefined personality templates

## How to Use

1. Select a personality template or customize your own
2. Enter the attributes for your AI companion
3. Click "Spin up your companion" to create your AI girlfriend
4. Start chatting with your personalized AI companion

## Docker Deployment

To deploy this application using Docker:

1. Make sure you have Docker installed on your system
2. Clone this repository
3. Build the Docker image:
   ```bash
   docker build -t girlfriendgpt .
   ```
4. Run the container:
   ```bash
   docker run -p 8501:8501 girlfriendgpt
   ```
5. Access the application at http://localhost:8501

## Notes

This is a simplified version without the full Steamship backend. It uses simulated responses for demonstration purposes.