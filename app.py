import streamlit as st

# Step 3: Define FAQ Data
faq_data = {
    "What is the name of the university?": "The name of the university is Federal Urdu University of Arts, Science and Technology (FUUAST), Islamabad.",
    "What faculty does the university have?": "The faculty is very cooperative and good.",
    "Who is the HOD of the CS department?": "The HOD of the CS department is Dr. M. Shiraz.",
    "What departments are available at FUUAST?": "The available departments include CS, AI, Software Engineering, Computer Engineering, Economics, Economics and Finance, Economics with Data Science, Electrical Engineering, Islamiyat, International Relations, Urdu, English, Mathematics, and much more.",
    "What is the fee structure for the programs?": "For specific fee structures, please visit the university's official website or contact the admissions office.",
}

# Step 4: Create Chatbot Function
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def faq_chatbot(user_input):
    questions = list(faq_data.keys())
    result = classifier(user_input, questions)
    best_question = result['labels'][0]
    return faq_data.get(best_question, "I'm sorry, I don't have an answer for that.")

# Step 5: Streamlit UI
st.title("University FAQ Chatbot")
st.write("Ask your questions related to Federal Urdu University of Arts, Science and Technology (FUUAST).")

user_input = st.text_input("Your Question:")

if user_input:
    response = faq_chatbot(user_input)
    st.write("**Response:**", response)
