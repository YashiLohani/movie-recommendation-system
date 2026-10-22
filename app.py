
import streamlit as st
from main import movies_df, recommend

# -----------------------------
# 1. Page configuration
# -----------------------------
st.set_page_config(
    page_title="CineMatch | Movie Recommendations",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# 2. Custom responsive styling
# -----------------------------
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        text-align: center;
        color: #808495;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    div.stButton > button {
        width: 100%;
        min-height: 3rem;
        border-radius: 10px;
        font-weight: 600;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 12px;
    }

    @media (max-width: 600px) {
        .block-container {
            padding: 1rem 0.8rem 2rem 0.8rem;
        }

        .subtitle {
            font-size: 0.95rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 3. App heading
# -----------------------------
st.markdown(
    '<div class="main-title">🎬 CineMatch</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies similar to the ones you love.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# 4. Movie selection
# -----------------------------
movie_titles = sorted(movies_df["title"].dropna().unique().tolist())

selected_movie = st.selectbox(
    "Choose a movie",
    options=movie_titles,
    index=None,
    placeholder="Search for a movie...",
)

number_of_recommendations = st.slider(
    "Number of recommendations",
    min_value=3,
    max_value=10,
    value=5
)

# -----------------------------
# 5. Find recommendations
# -----------------------------
if st.button("✨ Find Similar Movies"):
    if selected_movie is None:
        st.warning("Please select a movie first.")

    else:
        # Ask the recommendation engine for results.
        # The function in main.py currently prints results,
        # so capture those results in a string.
        import contextlib
        from io import StringIO

        output = StringIO()

        with contextlib.redirect_stdout(output):
            recommend(
                selected_movie,
                number=number_of_recommendations
            )

        result_text = output.getvalue()

        st.subheader("Your Recommendations")
        st.caption(f"Movies similar to {selected_movie}")

        # Display each recommendation as a movie card.
        recommendation_lines = result_text.splitlines()

        found_recommendations = False

        for line in recommendation_lines:
            if " — " in line and "% similarity" in line:
                title, score_text = line.rsplit(" — ", 1)
                score = score_text.replace("% similarity", "")

                with st.container(border=True):
                    st.markdown(f"### 🎥 {title}")
                    st.progress(
                        min(max(float(score) / 100, 0.0), 1.0)
                    )
                    st.caption(f"Content similarity: {score}%")

                found_recommendations = True

        if not found_recommendations:
            st.info(
                "No recommendations could be displayed. "
                "Check the movie title and dataset."
            )

# -----------------------------
# 6. Footer
# -----------------------------
st.divider()

st.caption(
    "Built with Python, Streamlit, Pandas and Scikit-learn | "
    "Recommendations use TF-IDF and cosine similarity."
)
