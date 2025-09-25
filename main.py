import streamlit as st
import time
from langchain_openai import ChatOpenAI
from concurrent.futures import ThreadPoolExecutor
from langchain_core.messages import HumanMessage

# Title and description
st.title("🤴🤴🤴 MaheshVShet's-FineTuned-LinkedIn-GPT 🤴🤴🤴")
st.markdown("📚📚📚 LinkedIn post generator by Gen-AI like [Mahesh Venkatesh Shet](https://www.linkedin.com/in/mahesh-venkatesh-shet/) 📚📚📚") 
st.markdown("🔥🔥🔥 Powered by GPT-4.1 (gpt-4.1-mini-2025-04-14) fine-tuned model. 🔥🔥🔥")

# Text input for topic
topic = st.text_input("Please enter the topic")

st.code("""
    Example:
    Explain Transformers Architecture
    How does RAG work?
    """, language=None)

# Initialize models
base_model = ChatOpenAI(model="gpt-4.1-mini-2025-04-14")
ft_model = ChatOpenAI(model="ft:gpt-4.1-mini-2025-04-14:daivajnaads:maheshvs-linkedinposts:CJZ5hLYj")

# Function to generate responses concurrently
def generate_linkedin_post(prompt):
    human_prompt = [HumanMessage(content=prompt)]
    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(base_model.invoke, human_prompt)
        f2 = executor.submit(ft_model.invoke, human_prompt)
        response1 = f1.result()
        response2 = f2.result()
    return response1.content, response2.content

if st.button("Generate LinkedIn Post"):
    if topic:
        with st.spinner("Generating posts..."):
            base_response, ft_response = generate_linkedin_post(f"Generate a LinkedIn post about {topic}")
            time.sleep(1)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Base Model (gpt-4.1-mini) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)

        with col2:
            st.subheader("MaheshVShet's-FineTuned-LinkedIn-GPT")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating posts.")
