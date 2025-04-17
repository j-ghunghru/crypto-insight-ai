import sys
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

from model import process_user_query


app = Flask(__name__)
CORS(app)


# POST: Submit question
@app.route('/api/data', methods=['POST'])
def post_data():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    question = data.get("question", "").strip()
    #answer = data.get("answer", "").strip().lower()

    # Validation
    if not all([question]):
        return jsonify({"error": "Missing question"}), 400
        
    user_query=  {
        "question": question
    }
    results = process_user_query(user_query)

    return jsonify({
        "message": "Submission successful!",
        "top_results": results
    }), 200
   

if __name__ == '__main__':
    app.run(debug=True)
