import os
from dotenv import load_dotenv
from app import create_app

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=os.getenv("FLASK_DEBUG") == "1")
