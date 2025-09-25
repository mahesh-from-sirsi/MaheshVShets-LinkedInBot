import streamlit as st
import time
from langchain_openai import ChatOpenAI

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

# Initialize the models
base_model = ChatOpenAI(model="gpt-4.1-mini-2025-04-14")
ft_model = ChatOpenAI(model="ft:gpt-4.1-mini-2025-04-14:daivajnaads:maheshvs-linkedinposts:CJZ5hLYj")

if st.button("Generate LinkedIn Post"):
    if topic:
        # Step 1: Generate Base Model Response
        with st.spinner("Generating LinkedIn post based on the base model..."):
            base_response = base_model.invoke(f"Generate a LinkedIn post about {topic}").content
            time.sleep(1)  # optional, just to simulate loading
            st.subheader("Base Model (gpt-4.1-mini) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)

        # Step 2: Generate Fine-Tuned Model Response
        with st.spinner("Generating LinkedIn post based on the fine-tuned model post..."):
            ft_response = ft_model.invoke(f"Generate a LinkedIn post about {topic}").content
            time.sleep(1)  # optional
            st.subheader("MaheshVShet's-FineTuned-LinkedIn-GPT")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating the post.")

