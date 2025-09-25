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
base_model = ChatOpenAI(model="gpt-4.1-mini-2025-04-14", temperature=0.7)
ft_model = ChatOpenAI(
    model="ft:gpt-4.1-mini-2025-04-14:daivajnaads:maheshvs-linkedinposts:CJZ5hLYj",
    temperature=0.7  # optional, ensures variability
)


# Function to generate posts using both models
def generate_linkedin_post(topic, base_model=base_model, ft_model=ft_model):
    prompt_for_base = f"Generate a LinkedIn post about {topic}"

    try:
        # Call base model
        base_response = base_model([HumanMessage(content=prompt_for_base)])
        base_content = base_response.content
    except Exception as e:
        base_content = f"Error with base model: {str(e)}"

    try:
        # Call fine-tuned model
        ft_response = ft_model([HumanMessage(content=topic)])  # Use just the topic for fine-tuned model
        ft_content = ft_response.content
    except Exception as e:
        ft_content = f"Error with fine-tuned model: {str(e)}"

    # Always access .content
    return base_content, ft_content

# Button to generate posts
if st.button("Generate LinkedIn Post"):
    if topic:
        with st.spinner("Generating posts..."):
            base_content, ft_content = generate_linkedin_post(topic)
            # Optional small delay for UX
            time.sleep(5)

        # Display responses in two columns
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Base Model (gpt-4.1-mini) 🔗")
            st.markdown(
                f'<div class="output-text">{base_content}</div>',
                unsafe_allow_html=True
            )
        with col2:
            st.subheader("MaheshVShet\'s-FineTuned-LinkedIn-GPT")
            st.markdown(
                f'<div class="output-text">{ft_content}</div>',
                unsafe_allow_html=True
            )
    else:
        st.warning("Please enter a topic before generating posts.")
