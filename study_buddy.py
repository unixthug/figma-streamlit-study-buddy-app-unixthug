import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCDJlwVJ7YrGEmI6a-DvhNq9eFU0rO8oYw")
model = genai.GenerativeModel('gemini-pro')

col1, col2, col3 = st.columns([0.2, 0.7, 0.1])
with col1:
    st.image("img/Group 9.png")
with col2:
    st.title("Welcome to :violet[Studium]!")
    st.write("Your personalized AI study buddy")
    with st.expander("About Studium"):
        st.write("Welcome to Studium - your AI-powered homework assistant! Effortlessly organize notes, tackle homework, and boost productivity. Say goodbye to study stress!")
    with st.expander("How To"):
        st.write("With Studium, accessing AI-powered assistance is just a prompt away.  \n  \nSimply upload a .txt file containing your notes or homework questions. Then ask the AI your questions.  \n  \nStudium's intelligent algorithms analyze your materials and provide tailored responses to help you understand concepts, clarify doubts, and solve problems. Say hello to seamless study sessions and efficient learning with Studium!")
    st.subheader("Upload Notes or Homework to Start!")
    st.divider()
    study_type = st.selectbox("Select the type of study help", ["Notes", "Homework"])
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write("Upload Successful!")
    st.image("img/noun-gladiator-2147528 1.png")

    # prompt logic
    def get_response(study_type, prompt):
        if prompt == "":
            return "***Greetings, I am :violet[Caesar]! Your AI-powered assistant! Please enter a prompt to begin.***"
        if study_type == "Notes":
            if uploaded_file is None:
                return "Please upload a file to begin."
            response = model.generate_content([prompt, uploaded_file.read().decode("utf-8")])
            response.resolve()
            return response.text
        elif study_type == "Homework":
            if uploaded_file is None:
                return "Please upload a file to begin."
            response = model.generate_content([prompt, uploaded_file.read().decode("utf-8")])
            response.resolve()
            return response.text

    if 'caesar' not in st.session_state:
        st.session_state['caesar'] = get_response(study_type,"")
    def update():
        st.session_state['caesar'] = get_response(study_type, prompt)
    st.write(st.session_state['caesar'])
    prompt = st.text_input("Prompt", placeholder="Type something...", help="Keep prompts short to improve accuracy of results.")
    st.button("Submit", on_click=update)

with col3:
    st.write("")


