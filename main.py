from src.unicode_invisible_cleaner.run_from_file import run_from_file
from config import BASE_DIR
import os
from src.backend.app import app as flask_app

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py run_from_file <input_file>")
        print("Usage: python main.py flask_app")
    elif len(sys.argv) == 3 and sys.argv[1] == "run_from_file":
        run_from_file(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "flask_app":
        flask_app.run(debug=True, host="0.0.0.0", port=5000)
