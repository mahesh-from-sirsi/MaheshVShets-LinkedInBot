import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import time

# Title and description
st.title("🤴🤴🤴 MaheshVShet's-FineTuned-LinkedIn-GPT 🤴🤴🤴")
st.markdown(
    "📚📚📚 LinkedIn post generator by Gen-AI like "
    "[Mahesh Venkatesh Shet](https://www.linkedin.com/in/mahesh-venkatesh-shet/) 📚📚📚"
)
st.markdown(
    "🔥🔥🔥 Powered by GPT-4.1 (gpt-4.1-mini-2025-04-14) fine-tuned model. 🔥🔥🔥"
)

# Text input for topic
topic = st.text_input("Please enter the topic")
st.code(
    """Example: Explain Transformers Architecture
How does RAG work?""",
    language=None
)

# Initialize the models
base_model = ChatOpenAI(model="gpt-4.1-mini-2025-04-14")
ft_model = ChatOpenAI(
    model="ft:gpt-4.1-mini-2025-04-14:daivajnaads:maheshvs-linkedinposts:CJZ5hLYj"
)

# Function to generate posts using both models
def generate_linkedin_post(prompt, base_model=base_model, ft_model=ft_model):
    # Wrap prompt in HumanMessage
    response1 = base_model([HumanMessage(content=prompt)])
    response2 = ft_model([HumanMessage(content=prompt)])
    return response1.content, response2.content

# Button to generate posts
if st.button("Generate LinkedIn Post"):
    if topic:
        with st.spinner("Generating posts..."):
            base_response, ft_response = generate_linkedin_post(
                f"Generate a LinkedIn post about {topic}"
            )
            # Optional small delay for UX
            time.sleep(1)

        # Display responses in two columns
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Base Model (gpt-4.1-mini) 🔗")
            st.markdown(
                f'<div class="output-text">{base_response}</div>',
                unsafe_allow_html=True
            )
        with col2:
            st.subheader("MaheshVShet\'s-FineTuned-LinkedIn-GPT")
            st.markdown(
                f'<div class="output-text">{ft_response}</div>',
                unsafe_allow_html=True
            )
    else:
        st.warning("Please enter a topic before generating posts.")
