from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import logging

app = Flask(__name__)


@app.route("/ocr", methods=["POST"])
def ocr():
    if "image" not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    image_file = request.files["image"]
    try:
        image = Image.open(image_file.stream)
        config = "--psm 13 -c tessedit_char_whitelist=0123456789./,"
        text = pytesseract.image_to_string(image, config=config)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# suppress /health endpoint logs
class HealthCheckFilter(logging.Filter):
    def filter(self, record):
        return "/health" not in record.getMessage()


if __name__ == "__main__":
    werkzeug_logger = logging.getLogger("werkzeug")
    werkzeug_logger.addFilter(HealthCheckFilter())

    app.run(host="0.0.0.0", port=5000)
