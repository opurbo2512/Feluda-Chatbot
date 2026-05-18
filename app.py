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
    color: white;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

h1 {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

#setting the title
st.title("🔎 ফেলুদা AI")
st.caption("রহস্য • পর্যবেক্ষণ • যুক্তি")

#about the app
with st.expander("📜 অ্যাপ সম্পর্কে"):

    st.write("""
🤖 এটি ফেলুদা AI — সত্যজিৎ রায়ের বিখ্যাত গোয়েন্দা চরিত্র প্রদোষচন্দ্র মিত্র (ফেলুদা)-এর উপর ভিত্তি করে তৈরি একটি AI chatbot।
-কী কী করতে পারবেন:
🔎 রহস্য সমাধান করুন — যেকোনো ঘটনা বা সমস্যা ফেলুদার কাছে পেশ করুন। সে মগজাস্ত্র দিয়ে বিশ্লেষণ করবে।
💬 বাংলায় কথা বলুন — সহজ, সাহিত্যিক বাংলায় উত্তর পাবেন। ইংরেজিতে প্রশ্ন করলেও বাংলায় উত্তর দেবে।

⚠️ এটি একটি AI চরিত্র — বাস্তব ফেলুদা নয়। বিনোদনের উদ্দেশ্যে তৈরি।
""")
    
#API key for chatbot
client = Groq(
    api_key = st.secrets["GROQ_API_KEY"]
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
    
#importing pics for avatar
feluda_pic = Image.open("feluda.jpg")
user_pic = Image.open("user.webp")

#session state for remembering chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#showing message from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar = message["pic"]):
        st.write(message["content"])

#taking prompt
prompt = st.chat_input("এখানে লিখুন...")
if prompt:
    with st.chat_message("user",avatar = user_pic):
        st.write(prompt)
    st.session_state.messages.append({"role":"user","content" : prompt,"pic" : user_pic})

    response = get_response(prompt)
    with st.chat_message("assistant",avatar=feluda_pic):
        st.write(response)
    st.session_state.messages.append({"role":"assistant","content" : response,"pic" : feluda_pic})
