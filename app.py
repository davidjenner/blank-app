import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Streamlit App Title
st.title("💻 IT Meme Generator")

# Sidebar with options
st.sidebar.header("Meme Settings")

# Option to upload an image
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "png"])

# Default meme templates
meme_templates = {
    "Distracted Boyfriend": "https://i.imgflip.com/1ur9b0.jpg",
        "Two Buttons": "https://i.imgflip.com/1g8my4.jpg",
            "Change My Mind": "https://i.imgflip.com/24y43o.jpg",
            }

            # Option to select a template
            selected_template = st.sidebar.selectbox("Or choose a template", ["None"] + list(meme_templates.keys()))

            # Input for meme captions
            top_text = st.sidebar.text_input("Top Text", "When you fix a bug")
            bottom_text = st.sidebar.text_input("Bottom Text", "But break everything else")

            # Load the selected image
            if uploaded_file:
                image = Image.open(uploaded_file)
                elif selected_template != "None":
                    response = requests.get(meme_templates[selected_template])
                        image = Image.open(BytesIO(response.content))
                        else:
                            st.sidebar.warning("Upload an image or select a template.")
                                image = None

                                # Meme Generation
                                def generate_meme(image, top_text, bottom_text):
                                    """Adds text to the image to create a meme."""
                                        draw = ImageDraw.Draw(image)
                                            font = ImageFont.load_default()

                                                # Get image size
                                                    width, height = image.size

                                                        # Define text position
                                                            top_position = (width // 10, 10)
                                                                bottom_position = (width // 10, height - 50)

                                                                    # Add text
                                                                        draw.text(top_position, top_text.upper(), font=font, fill="white")
                                                                            draw.text(bottom_position, bottom_text.upper(), font=font, fill="white")

                                                                                return image

                                                                                # Show and Download Meme
                                                                                if image:
                                                                                    meme_image = generate_meme(image, top_text, bottom_text)

                                                                                        st.image(meme_image, caption="Generated Meme", use_column_width=True)

                                                                                            # Save the image for download
                                                                                                meme_bytes = BytesIO()
                                                                                                    meme_image.save(meme_bytes, format="PNG")
                                                                                                        meme_bytes.seek(0)

                                                                                                            st.download_button("Download Meme", meme_bytes, file_name="it_meme.png", mime="image/png")