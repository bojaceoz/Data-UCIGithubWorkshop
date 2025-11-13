import streamlit as st
import os



st.set_page_config(page_title="Submission Text Viewer", layout="wide")
st.title("📂 Submission Text Viewer")

# Folder path
folder_path = "submission_text"

# Check if folder exists
if not os.path.exists(folder_path):
    st.warning(f"Folder '{folder_path}' not found. Please create it and add .txt files.")
else:
    # Get all .txt files sorted alphabetically
    txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])

    if not txt_files:
        st.info("No .txt files found in the folder.")
    else:
        # Display each file in its own section
        for file_name in txt_files:
            file_path = os.path.join(folder_path, file_name)

            # Create a container for each file
            with st.container():
                st.subheader(f"📄 {file_name}")

                # Read file
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                # Display each line separately
                for i, line in enumerate(lines, start=1):
                    st.text(f"{i:02d}: {line.strip()}")

                st.markdown("---")  # Divider between files
