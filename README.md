---
title: Simple Chatbot
emoji: 🌖
colorFrom: red
colorTo: pink
sdk: docker
pinned: false
license: mit
---

# simple_chatbot

Simple chatbot with the openai API and Gradio

## Demo

[Live Demo](https://huggingface.co/spaces/JanfNavf/simple_chatbot)

## Setup and Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/jorge-armando-navarro-flores/simple_chatbot.git

   cd simple_chatbot
   ```

2. **Create a Virtual Environment**

   ```sh
   python -m venv venv

   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your email and OpenAI credentials:

   ```env
   OPENAI_API_KEY=Your_OpenAI_API_key
   ```

5. **Run the Chatbot**

   ```sh
   python app.py
   ```
