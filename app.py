from flask import Flask, render_template, request
from google.cloud import translate

app = Flask(__name__)

def translate_text(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)

    return result["input"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text-to-translate"]
    target_language = request.form["target-language"]

    translated_text = translate_text(text, target_language)

    return translated_text

if __name__ == "__main__":
    app.run()

