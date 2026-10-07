## Team Members:

* **Ranjan Ravindra Mamadapur** - R25EF212
* **Pranav Ethapay** - R25EQ058
* **Mohammed Bilal Ahmed** - R25EF147
* **Nayab Nehal Haque** - R25EF160

Image Forgery Detection using ELA and CNN
A simple image forgery detection system that uses Error Level Analysis (ELA) and a Convolutional Neural Network (CNN) to classify images as Authentic or Forged.
How It Works
The project works in two main stages:
1. Error Level Analysis (ELA)
   The uploaded image is resaved as a JPEG and compared with the original image. Differences in compression levels are highlighted to create an ELA image.
2. CNN Classification
   The ELA image is resized to 128 × 128, normalized, and passed to a trained CNN model. The model predicts whether the image is Forged or Authentic and provides a confidence score.
Overall Flow
Input Image
     ↓
Error Level Analysis (ELA)
     ↓
ELA Image / Heatmap
     ↓
128 × 128 Preprocessing
     ↓
Trained CNN Model
     ↓
Forged / Authentic
     ↓
Confidence Score

Dataset
The model was trained using the CASIA image dataset, which contains:
- 11,129 total images
- 8,144 authentic images
- 2,985 forged images
The dataset is used during the training stage so that the CNN can learn patterns associated with authentic and forged images.
The CASIA dataset is not required for every prediction. Once training is complete, the learned model is stored as trained_model.h5 and is used to classify new images.
Technologies Used
- Python
- TensorFlow / Keras — CNN model
- Pillow (PIL) — Image processing and ELA
- NumPy — Image preprocessing
- PyQt5 — Current desktop interface
- Flask — Web backend
- HTML, CSS, JavaScript — Web frontend
Project Structure
image-forgery-detection/
│
├── ela.py
├── prediction.py
├── ui.py
├── trained_model.h5
├── gui.ui
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/

Running the Project
1. Open the project in VS Code
Open the project folder and start a terminal.
2. Activate the virtual environment
From the project directory:
..\venv\Scripts\activate

You should see:
(venv)

at the beginning of the terminal.
3. Run the current desktop application
python ui.py

Upload an image using Browse and click Test to get the prediction.
Web Version
For the website version, Flask will connect the frontend to the existing ELA and CNN backend:
Website
   ↓
Flask
   ↓
ELA + CNN
   ↓
Prediction

The web application can then be started using:
python app.py

