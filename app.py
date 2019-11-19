from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route("/mock", methods=['GET'])
def mock_route():
    latitude = request.args.get("lat", default = None)
    longitude = request.args.get("long", default = None)

    if latitude is None or longitude is None:
        return jsonify(
            {
                "error": "parameters cannot be null"
            }), 400
    return jsonify({ "location": "Not available" })

if __name__ == "__main__":
    app.run(debug=True)