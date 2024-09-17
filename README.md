# Flask Image Tagging API

This project is a Flask-based backend API for uploading images, tagging them using Object Detection (via ImageAI or another vision API), and generating meme-like text captions based on detected objects.

## Features

- **Image Upload**: Upload images to be processed.
- **Image Tagging**: Detect objects in images using object detection models.
- **Meme Text Generation**: Automatically generate meme-like captions for uploaded images based on detected objects.
- **Error Handling**: Detailed error responses for failed operations.

## Tech Stack

- **Flask**: Backend framework to handle API requests.
- **Python**: Backend language.
- **ImageAI**: For object detection (or another object detection API like Azure's Vision API).
- **Waitress**: Production server for running Flask.

---

## Installation

### Prerequisites

- Python 3.7+
- Virtual Environment (recommended)
- API keys for ImageAI (or another object detection API) and OpenAI.

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/flask-image-api.git
   cd flask-image-api
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   pip install -r requirement_gpu.txt
   pip install imageai --upgrade
   pip install waitress
   ```

4. **Download the object detection model** (for ImageAI users):

   Download the YOLOv3 model or another model compatible with ImageAI:

   ```bash
   # Example for ImageAI YOLOv3
   wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt
   ```

5. **Run the application**:

   ```bash
   waitress-serve --listen=127.0.0.1:5000 main:app
   ```

   This will run the app locally at `http://127.0.0.1:5000/`.

---

## Usage

### Upload and Tag an Image

You can upload an image and get the detected tags using the `/images/` endpoint.

#### Request

```http
POST /images/
```
