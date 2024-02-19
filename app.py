import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import pyttsx3

#from io import BytesIO

st.set_page_config(
    page_title="AI Audiobook Reader App",
    page_icon="🔊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# AI Audiobook Reader App"
    }
)
def main():
    st.title("File Upload and Page Selection")
    speaker = pyttsx3.init()
    # File upload
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        #file_data = BytesIO(uploaded_file.getvalue())

        if file_extension == "pdf":
            pdf = PdfReader(uploaded_file)
            num_pages = len(pdf.pages)
            selected_pages = st.multiselect("Select page (Once at a time)", range(1, num_pages + 1))
            selected_pages = [int(page) for page in selected_pages]

            for page in selected_pages:
                 st.write(f"Page {page}")
                 st.text(pdf.pages[page - 1].extract_text())
                 text = pdf.pages[page - 1].extract_text()

            #start_audio = st.button("Start Audio")
            #stop_audio = st.button("Stop Audio")
            
            if st.button("Start Audio"):
                speaker.say(text)        
                speaker.runAndWait()
                st.success("Audio generated successfully!")


        elif file_extension == "docx":
            doc = Document(uploaded_file)
            num_pages = len(doc.sections)
            selected_pages = st.multiselect("Select pages", range(1, num_pages + 1))
            selected_pages = [int(page) for page in selected_pages]

            for page in selected_pages:
                st.write(f"Page {page}")
                st.write(doc.sections[page - 1].text)
    elif uploaded_file is None:
        st.error("Please upload a file")





if __name__ == "__main__":
    main()