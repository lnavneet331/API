from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to extract user information (Modify with actual user data)
def get_user_info():
    return {
        "user_id": "john_doe_17091999",  # Replace with actual user data
        "email": "john@xyz.com",  # Replace with actual user data
        "roll_number": "ABCD123"  # Replace with actual user data
    }

# POST /bfhl
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get("data", [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid input format"}), 400
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = sorted([item for item in alphabets if item.islower()], reverse=True)
        highest_lowercase_alphabet = lowercase_alphabets[0] if lowercase_alphabets else None

        user_info = get_user_info()
        response = {
            "is_success": True,
            "user_id": user_info["user_id"],
            "email": user_info["email"],
            "roll_number": user_info["roll_number"],
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

# GET /bfhl
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
