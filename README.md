# Email Bot: Your Professional Email Assistant

This repository contains a Streamlit-based web application that leverages the Groq API and the Llama-3.1-8b-instant model to transform raw notes or brief instructions into polished, professional emails.

---

## Features

* **Professional Formatting**: Automatically generates subject lines, structured bodies, and appropriate sign-offs.
* **Context-Aware Drafting**: Uses a specialized system prompt to ensure clarity and eliminate corporate filler.
* **Web Interface**: Built with Streamlit for a clean, user-friendly experience.
* **High-Speed Generation**: Utilizes the Groq Llama-3.1-8b model for near-instant text completion.

---

## Prerequisites

Before running the application, ensure you have Python installed on your system. You will also need a valid Groq API key.

### Required Libraries

You must install the following dependencies:
* `groq`
* `streamlit`
* `load_dotenv`
* `os`

---

## Installation and Setup

1.  **Clone the Repository**
    Clone this project to your local machine.

2.  **Install Dependencies**
    Run the following command in your terminal:
    ```bash
    pip install groq streamlit python-dotenv
    ```

3.  **Environment Configuration**
    Create a `.env` file in the root directory and add your Groq API key:
    ```text
    GROQ_API_KEY=your_api_key_here
    ```
    *Note: While the script contains a hardcoded key for demonstration, using an environment variable is recommended for security.*

---

## Running the Application

To launch the Email Bot, navigate to the project directory in your terminal and execute the following command:

```bash
streamlit run main.py
```

Once executed, the application will be hosted locally, typically at `http://localhost:8501`.

### Usage Procedure

1.  Enter your raw notes or specific email instructions into the provided text area.
2.  Click the **Compose** button.
3.  The model will process the input and display the generated email, including a subject line and professional body, in the output section.

---

## Technical Details

The application uses the following configuration for the LLM:
* **Model**: llama-3.1-8b-instant
* **Max Tokens**: 300
* **Temperature**: 0.7 (balancing creativity and professional consistency)

---

## Author
**Muhammad Abdullah Khan**