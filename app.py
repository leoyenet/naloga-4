import os
from flask import Flask, render_template, request, url_for
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def make_meme(image_path, top_text, bottom_text):
    img = Image.open(image_path)

    base_width = 600
    w_percent = base_width / float(img.size[0])
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(img)

    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, 40)
    except IOError:
        font = ImageFont.load_default()

    width, height = img.size

    def draw_text(text, position):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2

        outline_range = 2
        for adj_x in range(-outline_range, outline_range + 1):
            for adj_y in range(-outline_range, outline_range + 1):
                draw.text((x + adj_x, position + adj_y), text, font=font, fill="black")

        draw.text((x, position), text, font=font, fill="white")

    if top_text:
        draw_text(top_text.upper(), 10)
    if bottom_text:
        draw_text(bottom_text.upper(), height - 60)

    meme_filename = "meme_" + os.path.basename(image_path)
    meme_path = os.path.join(app.config["UPLOAD_FOLDER"], meme_filename)
    img.save(meme_path)
    return meme_filename


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "Ni slike!"
        file = request.files["image"]
        if file.filename == "":
            return "Prazno ime datoteke!"

        top_text = request.form.get("top_text", "")
        bottom_text = request.form.get("bottom_text", "")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        meme_name = make_meme(filepath, top_text, bottom_text)
        return render_template("result.html", meme_name=meme_name)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
