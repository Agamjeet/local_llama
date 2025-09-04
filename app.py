import streamlit as st
import my_ollama
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Llama AI Assistant",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description in main area
st.title("🦙 Llama AI Assistant")

# Add clear button to top right
col1, col2 = st.columns([6,1])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        if 'chat_history' in st.session_state:
            del st.session_state['chat_history']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Chat with Llama or extract text from images using Llama 3.2 Vision!</p>', unsafe_allow_html=True)
st.markdown("---")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["💬 Chat", "📸 OCR"])

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Chat Tab
with tab1:
    st.header("💬 Chat with Llama")
    
    # Display chat history
    for message in st.session_state['chat_history']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask Llama anything..."):
        # Add user message to chat history
        st.session_state['chat_history'].append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = my_ollama.chat(
                        model='llama3.2:latest',
                        messages=[{
                            'role': 'user',
                            'content': prompt
                        }]
                    )
                    assistant_response = response.message.content
                    st.markdown(assistant_response)
                    
                    # Add assistant response to chat history
                    st.session_state['chat_history'].append({"role": "assistant", "content": assistant_response})
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# OCR Tab
with tab2:
    st.header("📸 Extract Text from Images")
    
    # Move upload controls to sidebar for OCR
    with st.sidebar:
        st.header("Upload Image")
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image")
            
            if st.button("Extract Text 🔍", type="primary"):
                with st.spinner("Processing image..."):
                    try:
                        response = my_ollama.chat(
                            model='llama3.2-vision',
                            messages=[{
                                'role': 'user',
                                'content': """Analyze the text in the provided image. Extract all readable content
                                            and present it in a structured Markdown format that is clear, concise, 
                                            and well-organized. Ensure proper formatting (e.g., headings, lists, or
                                            code blocks) as necessary to represent the content effectively.""",
                                'images': [uploaded_file.getvalue()]
                            }]
                        )
                        st.session_state['ocr_result'] = response.message.content
                    except Exception as e:
                        st.error(f"Error processing image: {str(e)}")
    
    # Main content area for OCR results
    if 'ocr_result' in st.session_state:
        st.markdown(st.session_state['ocr_result'])
    else:
        st.info("Upload an image and click 'Extract Text' to see the results here.")

# Footer
st.markdown("---")
st.markdown("")
