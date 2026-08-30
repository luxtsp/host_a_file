from flask import Flask, send_file

class FileUploader():
    def __init__(self, fpath: str) -> None:
        self.app = Flask("FileUploader")
        self.fpath = fpath
        @self.app.route("/")
        def download():
            return send_file(self.fpath, as_attachment=True, download_name="upload.zip")

    def run(self) -> None:
        print("starting host...")
        self.app.run(host="0.0.0.0", port=5000)
