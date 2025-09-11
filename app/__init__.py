from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    app.json.ensure_ascii = False   #dodaje polskie znaki
    app.config["JSON_AS_ASCII"] = False


    @app.route("/")
    def index():
        return jsonify({"Wiadomość":"Witaj"})
    
    from .routes import bp
    app.register_blueprint(bp)


    return app


app = create_app()

