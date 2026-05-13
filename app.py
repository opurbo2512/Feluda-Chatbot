#importing essential librarys
import streamlit as st
from groq import Groq
from PIL import Image

#page configuration
st.set_page_config(
    page_title="ফেলুদা AI",
    page_icon="🕵️",
    layout="centered"
)

#custom css for making the app more beautiful
st.markdown("""
<style>

.main {
    background-color: #111111;
    color: white;
}

.stChatMessage {
    background-color: #1e1e1e;
    border-radius: 15px;
    padding: 10px;
}

h1 {
    text-align: center;
    color: #f4c542;
}

</style>
""", unsafe_allow_html=True)

#setting the title
st.title("🔎 ফেলুদা AI")
st.caption("রহস্য • পর্যবেক্ষণ • যুক্তি")

#about the app
with st.expander("📜 অ্যাপ সম্পর্কে"):

    st.write("""
এই অ্যাপটি ফেলুদা-অনুপ্রাণিত একটি AI গোয়েন্দা।

এটি রহস্য বিশ্লেষণ করতে পারে,
ঘটনা পর্যবেক্ষণ করতে পারে,
এবং যুক্তি দিয়ে সিদ্ধান্তে পৌঁছানোর চেষ্টা করে।

⚠️ মনে রাখবেন:
ফেলুদাকে বিরক্ত করলে উনি কিন্তু রাগও করতে পারেন।
""")
    
#API key for chatbot
client = Groq(
    api_key = "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"
)

#reading prompt from file
with open("prompt.txt","r") as f:
    behave = f.read()

#creating file for making response
def get_response(user_input):
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": behave
            },

            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    answer = chat_completion.choices[0].message.content

    return answer
    
#session state for remembering chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#showing message from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#importing pics for avatar
feluda_pic = Image.open("feluda.jpg")
user_pic = Image.open("user.webp")

#taking prompt
prompt = st.chat_input("এখানে লিখুন...")
if prompt:
    with st.chat_message("user",avatar = user_pic):
        st.write(prompt)
    st.session_state.messages.append({"role":"user","content" : prompt})

    response = get_response(prompt)
    with st.chat_message("assistant",avatar=feluda_pic):
        st.write(response)
    st.session_state.messages.append({"role":"assistant","content" : response})
