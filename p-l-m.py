# import streamlit as st
# import pandas as pd
# import base64
# import time

# # App config
# st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="wide")

# # Background image function
# def add_bg_image():
#     with open("A_high-resolution_digital_photograph_captures_the_.png", "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{encoded_string}");
#             background-size: cover;
#             background-position: center;
#             font-family: 'Trebuchet MS', sans-serif;
#         }}
#         .stButton>button:hover {{
#             background-color: #ffcc70 !important;
#             color: black !important;
#             transform: scale(1.05);
#         }}
#         .glassbox {{
#             background: rgba(255, 255, 255, 0.75);
#             border-radius: 16px;
#             padding: 20px;
#             box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
#             backdrop-filter: blur(8.2px);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_image()

# # Welcome sound
# st.audio("https://www.soundjay.com/human/sounds/applause-8.mp3", format="audio/mp3", start_time=0)

# # Title and header
# st.title("📚 Personal Library Manager")
# st.markdown("### This app created by Ammara 🎨✨")

# # Initialize or load data
# if "library_data" not in st.session_state:
#     try:
#         st.session_state.library_data = pd.read_csv("sample_books.csv")
#     except:
#         st.session_state.library_data = pd.DataFrame(columns=["📖 Title", "✍️ Author", "⭐ Rating", "📅 Year", "📚 Genre", "💖 Favorite", "📝 Notes", "📍 Location"])

# # --- 🚀 Navigation Bar ---
# menu = st.sidebar.radio("🔍 Go to", [
#     "📖 View Library", "➕ Add Book", "🔎 Search Books",
#     "📊 Library Statistics", "📥 Import CSV", "📤 Download CSV",
#     "📅 Reading Goals"
# ])

# # --- 📖 View Library ---
# if menu == "📖 View Library":
#     st.subheader("📚 My Library Collection")
#     edited_df = st.data_editor(st.session_state.library_data, use_container_width=True, num_rows="dynamic")
#     st.session_state.library_data = edited_df
#     if st.button("🗑️ Delete All Books"):
#         st.session_state.library_data = pd.DataFrame(columns=st.session_state.library_data.columns)
#         st.success("🧹 Library cleared!")

# # --- ➕ Add Book ---
# elif menu == "➕ Add Book":
#     with st.container():
#         st.markdown("<div class='glassbox'>", unsafe_allow_html=True)
#         st.subheader("📘 Add a New Book to Your Library")
#         title = st.text_input("📖 Book Title")
#         author = st.text_input("✍️ Author Name")
#         rating = st.slider("⭐ Rating", 1, 5, 3)
#         year = st.number_input("📅 Publication Year", min_value=0, max_value=2025, step=1)
#         genre = st.selectbox("📚 Genre", ["Fiction", "Non-Fiction", "Self-Help", "Science", "History", "Fantasy", "Business", "Philosophy", "Classic", "Programming"])
#         favorite = st.checkbox("💖 Mark as Favorite")
#         notes = st.text_area("📝 Notes")
#         location = st.text_input("📍 Book Location (shelf, room etc.)")
#         if st.button("📚 Add Book"):
#             new_book = pd.DataFrame([[title, author, rating, year, genre, favorite, notes, location]],
#                 columns=["📖 Title", "✍️ Author", "⭐ Rating", "📅 Year", "📚 Genre", "💖 Favorite", "📝 Notes", "📍 Location"])
#             st.session_state.library_data = pd.concat([st.session_state.library_data, new_book], ignore_index=True)
#             st.success("✅ Book added successfully!")
#             st.audio("https://www.soundjay.com/buttons/sounds/button-16.mp3")
#         st.markdown("</div>", unsafe_allow_html=True)

# # --- 🔍 Search Books ---
# elif menu == "🔎 Search Books":
#     st.subheader("🔍 Search Books in Library")
#     search_term = st.text_input("🔎 Enter book title or author")
#     if search_term:
#         results = st.session_state.library_data[
#             st.session_state.library_data["📖 Title"].str.contains(search_term, case=False, na=False) |
#             st.session_state.library_data["✍️ Author"].str.contains(search_term, case=False, na=False)
#         ]
#         st.dataframe(results, use_container_width=True)

# # --- 📊 Library Statistics ---
# elif menu == "📊 Library Statistics":
#     st.subheader("📈 Library Statistics")
#     if not st.session_state.library_data.empty:
#         genre_count = st.session_state.library_data["📚 Genre"].value_counts()
#         st.bar_chart(genre_count)

#         avg_rating = st.session_state.library_data["⭐ Rating"].mean()
#         st.markdown(f"**📊 Average Rating:** {avg_rating:.2f} ⭐")

#         most_recent = st.session_state.library_data.sort_values(by="📅 Year", ascending=False).head(5)
#         st.markdown("### 🕑 Most Recent Books")
#         st.table(most_recent)
#     else:
#         st.warning("📭 No data available to show statistics.")

# # --- 📥 Import CSV ---
# elif menu == "📥 Import CSV":
#     uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         st.session_state.library_data = pd.concat([st.session_state.library_data, df], ignore_index=True)
#         st.success("✅ Books imported successfully!")

# # --- 📤 Download CSV ---
# elif menu == "📤 Download CSV":
#     st.subheader("📥 Download Your Library")
#     csv = st.session_state.library_data.to_csv(index=False).encode("utf-8")
#     st.download_button(
#         label="📥 Download Library CSV",
#         data=csv,
#         file_name="my_library.csv",
#         mime="text/csv"
#     )

# # --- 📅 Reading Goals ---
# elif menu == "📅 Reading Goals":
#     st.subheader("🎯 Set Your Reading Goals")
#     goal = st.number_input("📚 Books to Read This Year", min_value=1, step=1)
#     read = st.number_input("📘 Books Already Read", min_value=0, step=1)
#     progress = int((read / goal) * 100) if goal > 0 else 0
#     st.progress(progress)
#     st.markdown(f"**📈 Progress:** {progress}%")

# # --- Footer ---
# st.markdown("---")
# st.markdown("🎨 **Designed by Ammara** 💖")








import streamlit as st
import pandas as pd
import base64

# App config
st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="wide")

# Background image function
def add_bg_image():
    with open("image.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image()

# Title and header
st.title("📚 Personal Library Manager")
st.markdown("### This app created by Ammara 🎨✨")

# Initialize or load data
if "library_data" not in st.session_state:
    try:
        st.session_state.library_data = pd.read_csv("sample_books.csv")
    except:
        st.session_state.library_data = pd.DataFrame(columns=["📖 Title", "✍️ Author", "⭐ Rating", "📅 Year", "📚 Genre"])

# --- 🚀 Navigation Bar ---
menu = st.sidebar.radio("🔍 Go to", ["📖 View Library", "➕ Add Book", "🔎 Search Books", "📊 Library Statistics"])

# --- 📖 View Library ---
if menu == "📖 View Library":
    st.subheader("📚 My Library Collection")
    st.dataframe(st.session_state.library_data, use_container_width=True)

# --- ➕ Add Book ---
elif menu == "➕ Add Book":
    st.subheader("📘 Add a New Book to Your Library")
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author Name")
    rating = st.slider("⭐ Rating", 1, 5, 3)
    year = st.number_input("📅 Publication Year", min_value=0, max_value=2025, step=1)
    genre = st.selectbox("📚 Genre", ["Fiction", "Non-Fiction", "Self-Help", "Science", "History", "Fantasy", "Business", "Philosophy", "Classic", "Programming"])

    if st.button("📚 Add Book"):
        new_book = pd.DataFrame([[title, author, rating, year, genre]],
                                columns=["📖 Title", "✍️ Author", "⭐ Rating", "📅 Year", "📚 Genre"])
        st.session_state.library_data = pd.concat([st.session_state.library_data, new_book], ignore_index=True)
        st.success("✅ Book added successfully!")

# --- 🔍 Search Books ---
elif menu == "🔎 Search Books":
    st.subheader("🔍 Search Books in Library")
    search_term = st.text_input("🔎 Enter book title or author")
    if search_term:
        results = st.session_state.library_data[
            st.session_state.library_data["📖 Title"].str.contains(search_term, case=False, na=False) |
            st.session_state.library_data["✍️ Author"].str.contains(search_term, case=False, na=False)
        ]
        st.dataframe(results, use_container_width=True)

# --- 📊 Library Statistics ---
elif menu == "📊 Library Statistics":
    st.subheader("📈 Library Statistics")

    if not st.session_state.library_data.empty:
        genre_count = st.session_state.library_data["📚 Genre"].value_counts()
        st.bar_chart(genre_count)

        avg_rating = st.session_state.library_data["⭐ Rating"].mean()
        st.markdown(f"**📊 Average Rating:** {avg_rating:.2f} ⭐")

        most_recent = st.session_state.library_data.sort_values(by="📅 Year", ascending=False).head(5)
        st.markdown("### 🕑 Most Recent Books")
        st.table(most_recent)
    else:
        st.warning("📭 No data available to show statistics.")

# --- Footer ---
st.markdown("---")
st.markdown("🎨 **Designed by Ammara** 💖")
