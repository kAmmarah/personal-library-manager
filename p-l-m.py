import streamlit as st
import pandas as pd

# App configuration
st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="wide")

# Header
st.title("📚 Personal Library Manager")
st.markdown("### This app created by Ammara 🎨✨")

# Initialize library data
if "library_data" not in st.session_state:
    st.session_state.library_data = pd.DataFrame(columns=["📖 Title", "✍️ Author", "⭐ Rating", "📅 Year"])

# Section to add new books
with st.expander("➕ Add a New Book"):
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author Name")
    rating = st.slider("⭐ Rating", 1, 5, 3)
    year = st.number_input("📅 Publication Year", min_value=1900, max_value=2025, step=1)
    
    if st.button("📚 Add Book"):
        new_data = pd.DataFrame([[title, author, rating, year]], columns=["📖 Title", "✍️ Author", "⭐ Rating", "📅 Year"])
        st.session_state.library_data = pd.concat([st.session_state.library_data, new_data], ignore_index=True)
        st.success("✅ Book added successfully!")

# Display the library collection
st.subheader("📜 My Library Collection")
st.dataframe(st.session_state.library_data, use_container_width=True)

# Footer
st.markdown("🎨 **Designed by Ammara** 💖")
