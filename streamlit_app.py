import streamlit as st
import pandas as pd


def load_data():
    """Loads the Excel file with similarity results."""
    file_path = 'extreme_similarities_examples.xlsx'  # Update with actual file path
    xl = pd.ExcelFile(file_path)
    max_similarity_df = xl.parse('Max Similarity')
    min_similarity_df = xl.parse('Min Similarity')
    return max_similarity_df, min_similarity_df


# Streamlit UI
def main():
    st.set_page_config(layout="wide")

    # Apply RTL styling
    st.markdown("""
        <style>
        body, .stTextArea, .stTextInput, .stDataFrame, .stMarkdown {
            direction: rtl;
            text-align: right;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 style='text-align: center;'>Similarity Analysis Dashboard</h1>
    """, unsafe_allow_html=True)

    # Load data
    max_similarity_df, min_similarity_df = load_data()

    # Display Extreme Max Similarity Section
    st.markdown("""
        <h2 style='text-align: center;'>Extreme Max Similarity</h2>
    """, unsafe_allow_html=True)
    for i, row in max_similarity_df.iterrows():
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**{row['file_name_1']}** (Similarity: {row['similarity']:.2f})")
            st.text_area("", row['chunk_file_1'], height=150, key=f"max_1_{i}")
        with col2:
            st.write(f"**{row['file_name_2']}**")
            st.text_area("", row['chunk_file_2'], height=150, key=f"max_2_{i}")

    # Display Extreme Min Similarity Section
    st.markdown("""
        <h2 style='text-align: center;'>Extreme Min Similarity</h2>
    """, unsafe_allow_html=True)
    for i, row in min_similarity_df.iterrows():
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**{row['file_name_1']}** (Similarity: {row['similarity']:.2f})")
            st.text_area("", row['chunk_file_1'], height=150, key=f"min_1_{i}")
        with col2:
            st.write(f"**{row['file_name_2']}**")
            st.text_area("", row['chunk_file_2'], height=150, key=f"min_2_{i}")


if __name__ == "__main__":
    main()
