from pathlib import Path
from flask import Flask, send_from_directory, abort

# Keep the existing website files unchanged and use Flask only as the web server.
BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__, static_folder=None)


def serve_file(relative_path: str):
    """Serve an existing file from the website directory."""
    file_path = BASE_DIR / relative_path

    if not file_path.is_file():
        abort(404)

    return send_from_directory(
        file_path.parent,
        file_path.name,
    )


@app.get("/")
def home():
    return serve_file("index.html")


@app.get("/pages/<path:filename>")
def pages(filename):
    return serve_file(f"pages/{filename}")


@app.get("/css/<path:filename>")
def css(filename):
    return serve_file(f"css/{filename}")


@app.get("/js/<path:filename>")
def javascript(filename):
    return serve_file(f"js/{filename}")


@app.get("/images/<path:filename>")
def images(filename):
    return serve_file(f"images/{filename}")


if __name__ == "__main__":
    # PORT is supplied by most hosting platforms; 5000 is used locally.
    import os

    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 5000))
    app.run(host=host, port=port)
