import json
from app import create_app

app = create_app()
client = app.test_client()

def print_test_case(title, endpoint, inputs, expected, response):
    print("\n" + "=" * 70)
    print(f"TEST CASE: {title}")
    print("=" * 70)
    print(f"API Endpoint: POST {endpoint}")
    print("Inputs: " + json.dumps(inputs, indent=4))
    print("Expected: " + json.dumps(expected, indent=4))
    print("-" * 70)
    print(f"ACTUAL STATUS: {response.status_code}")
    try:
        data = response.get_json()
        print("ACTUAL RESPONSE (json): " + json.dumps(data, indent=4))
    except Exception:
        print("ACTUAL RESPONSE: " + response.get_data(as_text=True))
    print("=" * 70 + "\n")

if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("      SOCIONEED API TEST EVIDENCE REPORT (LOGIN & AUTH VALIDATION)")
    print("#" * 70)

    # 1. Successful Login (200 OK)
    login_inputs = {
        "email": "admin@socioneed.com",
        "password": "123456",
        "role": "admin"
    }
    expected_200 = {
        "status_code": 200,
        "message": "Login successful",
        "token_present": True
    }
    resp_200 = client.post("/api/auth/login", json=login_inputs)
    print_test_case("1. Successful Login", "/api/auth/login", login_inputs, expected_200, resp_200)

    # 2. Invalid Login (401 Unauthorized)
    invalid_login_inputs = {
        "email": "admin@socioneed.com",
        "password": "WrongPassword123",
        "role": "admin"
    }
    expected_401 = {
        "status_code": 401,
        "message": "Invalid email or password"
    }
    resp_401 = client.post("/api/auth/login", json=invalid_login_inputs)
    print_test_case("2. Invalid Login (Wrong Password)", "/api/auth/login", invalid_login_inputs, expected_401, resp_401)

    # 3. Validation Error (400 Bad Request)
    missing_fields_inputs = {
        "email": "incomplete@socioneed.com"
    }
    expected_400 = {
        "status_code": 400,
        "error_code": "VALIDATION_ERROR"
    }
    resp_400 = client.post("/api/auth/register", json=missing_fields_inputs)
    print_test_case("3. Validation Error (Missing Required Fields)", "/api/auth/register", missing_fields_inputs, expected_400, resp_400)
