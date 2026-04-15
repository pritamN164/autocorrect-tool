import streamlit as st
from autocorrect import correct_sentence, grammar_correct, candidates

st.set_page_config(page_title="AI Autocorrect Tool", layout="centered")

st.title("🧠 AI Autocorrect Tool")
st.write("Improve your text accuracy and fluency using AI-powered correction")

input_text = st.text_area("Enter your text:", height=150)

if st.button("Correct Text"):
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        spell_corrected = correct_sentence(input_text)
        final_corrected = grammar_correct(spell_corrected)

        st.subheader("🔍 Spell Corrected:")
        st.success(spell_corrected)

        st.subheader("✨ Final AI Corrected Output:")
        st.success(final_corrected)

# Suggestions feature
if st.checkbox("Show Word Suggestions"):
    word = st.text_input("Enter a word:")
    if word:
        st.write("Suggestions:", list(candidates(word))[:10])

st.markdown("---")
st.write("THANK YOU")