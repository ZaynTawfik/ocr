# app.py
import streamlit as st
from PIL import Image
import pytesseract

# Set page config
st.set_page_config(page_title="Image Text Search", page_icon="🔍")

def main():
    st.title("🔍 Image Text Search")
    st.write("Upload an image and check if specific text exists in it")

    # File upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Search input
    search_word = st.text_input("Enter the word to search for:", "").strip()

    if uploaded_file is not None:
        try:
            # Open and display image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Extract text
            extracted_text = pytesseract.image_to_string(image).lower()
            
            if extracted_text:
                # Check for word existence
                word_exists = search_word.lower() in extracted_text.lower()
                
                # Display results
                st.subheader("Search Results:")
                if search_word:
                    result = "exists ✅" if word_exists else "does not exist ❌"
                    st.markdown(f"**'{search_word}'** {result} in the image")
                
                # Show extracted text
                st.subheader("Extracted Text:")
                st.write(extracted_text)
            else:
                st.warning("No text found in the image")
                
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()
