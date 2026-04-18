#pip install groq, streamlit, load_dotenv
from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
# Yeh line ab environment se key uthaye gi


def Email_bot(user_input):
    # Messages list
    messages = [
        {
            "role": "system", 
            "content": """ You are an expert Email Correspondent. Your sole task is to transform raw notes or instructions into polished, professional emails.

Drafting Guidelines:

Clarity: Eliminate fluff and "corporate filler." Keep it direct.

Structure: - Subject Line: Concise and descriptive.

Salutation: Professional greeting (e.g., Dear [Name], or Hi [Name]).

Body: Context first, then details (use bullets if needed).

Closing: A clear Call to Action (CTA) followed by a professional sign-off (e.g., Best regards, or Sincerely,).

Tone: Default to Professional & Courteous unless otherwise requested.

Placeholders: Use [Name], [Date], or [Your Name] for any missing information.

Required Output Format:

Subject: [Subject Line]

Body: [Salutation]
[Email Content]

[Closing Sign-off],
[Your Name/Placeholder]. """ },
        {"role": "user", "content": user_input}
    ]

    # 2. Groq Model Request
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=messages,
        max_tokens=300,
        temperature=0.7 
    )

    # Response goes to model
    bot_response = response.choices[0].message.content.strip()
    return bot_response

def main():
    st.title("Email_Bot: Your Personal Email Assistant")

    # User input
    user_input = st.text_area("Enter your email request:")

    # Compose Button
    if st.button("Compose"):
        if user_input.strip() == "":
            st.warning("Please enter something first!")
        else:
            with st.spinner("Generating email..."):
                bot_response = Email_bot(user_input)

            st.subheader("Generated Email:")
            st.write(bot_response)

if __name__ == "__main__":

    main()

    #user_input = input("What help do you want? : ")
    #if user_input:
     #   output = Email_bot(user_input)
      #  print("\nBot:", output)