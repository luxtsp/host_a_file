from src import FileUploader
import os

if __name__ == "__main__":
    try:
        file = os.listdir('data')[0]
        server = FileUploader(f"data/{file}")
        server.run()
    except Exception as e:
        print(f"Error: {e}")
