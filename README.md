# Llama AI Assistant - Chat & OCR

A Streamlit web application that combines chat functionality with Llama 3.2 and OCR capabilities using Llama 3.2 Vision for text extraction from images.

## Features

- 💬 **Chat Interface** - Interactive conversation with Llama 3.2
- 🦙 Powered by Llama 3.2 and Llama 3.2 Vision models
- 📸 **OCR Functionality** - Upload images (PNG, JPG, JPEG)
- 🔍 Extract structured text from images
- 📝 Output in clean Markdown format
- 🎨 Modern, tabbed interface
- 💾 Chat history persistence during session

## Prerequisites

Before running this application, you need to have Ollama installed and running on your system.

### Installing Ollama

1. **Download Ollama** from [https://ollama.ai](https://ollama.ai)
2. **Install Ollama** following the instructions for your operating system
3. **Pull the required models**:
   ```bash
   ollama pull llama3.2:latest
   ollama pull llama3.2-vision
   ```

## Installation

1. **Clone or download this repository**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Make sure Ollama is running**:
   ```bash
   ollama serve
   ```

2. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## Usage

### Chat Tab
1. **Switch to the "💬 Chat" tab**
2. **Type your message** in the chat input at the bottom
3. **Press Enter** to send and receive Llama's response
4. **Continue the conversation** - chat history is maintained during the session

### OCR Tab
1. **Switch to the "📸 OCR" tab**
2. **Upload an image** using the file uploader in the sidebar
3. **Click "Extract Text 🔍"** to process the image
4. **View the extracted text** in the main area, formatted as Markdown

## Requirements

- Python 3.8+
- Ollama installed and running
- Llama 3.2 and Llama 3.2 Vision models pulled in Ollama
- Internet connection (for initial model download)

## Troubleshooting

- **"Model not found" error**: Make sure you've pulled both models:
  - `ollama pull llama3.2:latest` (for chat)
  - `ollama pull llama3.2-vision` (for OCR)
- **Connection errors**: Ensure Ollama is running with `ollama serve`
- **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
- **Chat not working**: Verify the `llama3.2:latest` model is available
- **OCR not working**: Verify the `llama3.2-vision` model is available

## File Structure

```
├── app.py              # Main Streamlit application
├── my_ollama.py        # Ollama integration module
├── requirements.txt    # Python dependencies
└── README.md          # This file
```
