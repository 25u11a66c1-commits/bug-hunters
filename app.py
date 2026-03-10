import streamlit as st
import os
from groq import Groq

# ----------------------------
# GROQ SETUP
# ----------------------------

# Option 1: Put your API key here
# api_key = "YOUR_GROQ_API_KEY"

# Option 2: Use environment variable
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# ----------------------------
# AI FUNCTION
# ----------------------------

def generate_ai(prompt):

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content


# ----------------------------
# STREAMLIT UI
# ----------------------------

st.set_page_config(
    page_title="BrandCraft AI",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 BrandCraft AI")
st.subheader("Generative AI Powered Branding Automation System")

st.markdown("---")

# Sidebar Inputs
st.sidebar.header("Business Details")

business_idea = st.sidebar.text_input("Business Idea")
target_audience = st.sidebar.text_input("Target Audience")
brand_style = st.sidebar.selectbox(
    "Brand Style",
    ["Modern", "Luxury", "Minimal", "Playful", "Tech"]
)

generate_button = st.sidebar.button("Generate Branding")

# ----------------------------
# MAIN LOGIC
# ----------------------------

if generate_button:

    if business_idea == "":
        st.warning("Please enter a business idea")
    else:

        with st.spinner("Generating branding assets..."):

            # Brand Name Prompt
            brand_prompt = f"""
            Generate 5 creative brand names.

            Business Idea: {business_idea}
            Target Audience: {target_audience}
            Brand Style: {brand_style}

            Return only brand names in a list.
            """

            brand_names = generate_ai(brand_prompt)

            st.header("✨ Brand Name Suggestions")
            st.write(brand_names)

            brand_name = st.text_input("Select or Enter Brand Name")

            if brand_name:

                # Tagline
                tagline_prompt = f"""
                Generate 5 catchy taglines.

                Brand Name: {brand_name}
                Business Idea: {business_idea}
                Style: {brand_style}
                """

                taglines = generate_ai(tagline_prompt)

                st.header("🏷 Taglines")
                st.write(taglines)

                # Brand Story
                story_prompt = f"""
                Write a compelling brand story.

                Brand Name: {brand_name}
                Business Idea: {business_idea}
                Target Audience: {target_audience}

                Make it emotional and inspiring.
                """

                story = generate_ai(story_prompt)

                st.header("📖 Brand Story")
                st.write(story)

                # Logo Idea
                logo_prompt = f"""
                Suggest creative logo design ideas.

                Brand Name: {brand_name}
                Business Idea: {business_idea}

                Include:
                - colors
                - symbols
                - design style
                """

                logo = generate_ai(logo_prompt)

                st.header("🎨 Logo Concept")
                st.write(logo)

                # Marketing Copy
                marketing_prompt = f"""
                Create marketing copy.

                Brand Name: {brand_name}
                Business Idea: {business_idea}

                Include:
                - Instagram caption
                - Twitter post
                - Advertisement slogan
                """

                marketing = generate_ai(marketing_prompt)

                st.header("📢 Marketing Copy")
                st.write(marketing)

st.markdown("---")
st.caption("Built with Streamlit + Groq LLM")