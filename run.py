from app.factory import create_app
# import app.config import 

if __name__ == "__main__":
    app = create_app()
    app.config["DEBUG"] = True
    app.config["MONGO_URI"] = '<redacted>'
    app.run()