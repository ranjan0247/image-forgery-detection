import os
import base64
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

# Import your existing detection logic here
# import prediction 
# import ela 

app = Flask(__name__)
CORS(app)

# Serve the HTML file
@app.route('/')
def home():
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    temp_path = os.path.join("temp", file.filename)
    
    # Ensure temp directory exists
    os.makedirs("temp", exist_ok=True)
    file.save(temp_path)

    try:
        # ---------------------------------------------------------
        # REPLACE THIS BLOCK WITH YOUR ACTUAL PREDICTION LOGIC
        # Example: 
        # verdict, confidence, heatmap_img_path = prediction.analyze_image(temp_path)
        # ---------------------------------------------------------
        
        # Mock data (replace with actual ML results)
        verdict = "Tampered"
        confidence = 94.5
        heatmap_img_path = temp_path # Replace with actual generated ELA heatmap path
        
        # Convert the generated heatmap image to base64 so the frontend can display it
        with open(heatmap_img_path, "rb") as img_file:
            heatmap_base64 = base64.b64encode(img_file.read()).decode('utf-8')
            heatmap_data_url = f"data:image/jpeg;base64,{heatmap_base64}"

        return jsonify({
            "verdict": verdict,
            "confidence": str(confidence),
            "heatmap": heatmap_data_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up the temporary uploaded file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    app.run(port=5000, debug=True)