# Llama OCR - Easy Text Extraction from Images

A Streamlit web application that uses Llama 3.2 Vision to extract and structure text from images with OCR capabilities.

## Features

- 🦙 Powered by Llama 3.2 Vision model
- 📸 Upload images (PNG, JPG, JPEG)
- 🔍 Extract structured text from images
- 📝 Output in clean Markdown format
- 🎨 Modern, user-friendly interface

## Prerequisites

Before running this application, you need to have Ollama installed and running on your system.

### Installing Ollama

1. **Download Ollama** from [https://ollama.ai](https://ollama.ai)
2. **Install Ollama** following the instructions for your operating system
3. **Pull the Llama 3.2 Vision model**:
   ```bash
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

1. **Upload an image** using the file uploader in the sidebar
2. **Click "Extract Text 🔍"** to process the image
3. **View the extracted text** in the main area, formatted as Markdown

## Requirements

- Python 3.8+
- Ollama installed and running
- Llama 3.2 Vision model pulled in Ollama
- Internet connection (for initial model download)

## Troubleshooting

- **"Model not found" error**: Make sure you've pulled the `llama3.2-vision` model with `ollama pull llama3.2-vision`
- **Connection errors**: Ensure Ollama is running with `ollama serve`
- **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

## File Structure

```
├── app.py              # Main Streamlit application
├── my_ollama.py        # Ollama integration module
├── requirements.txt    # Python dependencies
└── README.md          # This file
```
