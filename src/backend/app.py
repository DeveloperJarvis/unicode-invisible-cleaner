import os
import json
from flask import Flask, render_template, request, jsonify
from unicode_invisible_cleaner.detector import InvisibleTextDetector
from unicode_invisible_cleaner.cleaner import InvisibleTextRemover
from config import BASE_DIR

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "src", "frontend"),
    static_folder=os.path.join(BASE_DIR, "src", "frontend", "static")
)

@app.route("/", methods=["GET", "POST"])
def process_text():
    if request.method == "POST":
        text = request.form.get("text", "")
        # print(text)

        if not text:
            return jsonify({"error": "No text provided"}), 400 # Return 400 error
        detector = InvisibleTextDetector()
        detected = detector.detect(text)
        print("Detected Invisible Characters:", detected)
        highlighted_text = text
        # print(highlighted_text)
        for char in detected:
            highlighted_text = highlighted_text.replace(
                char,
                f'<span class="highlight">{char}></span'
            )
        remover = InvisibleTextRemover()
        cleaned = remover.clean(text)
        print({
            "highlighted": highlighted_text,
            "cleaned": cleaned
        })
        return json.dumps({
            "highlighted": highlighted_text,
            "cleaned": cleaned
        })
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
