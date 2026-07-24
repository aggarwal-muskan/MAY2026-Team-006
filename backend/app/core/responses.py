from flask import jsonify


def ok(data=None, message="Success", status=200):
    payload = {"success": True, "message": message}
    if data is not None:
        payload["data"] = data
    return jsonify(payload), status


def fail(message="Request failed", code="BAD_REQUEST", status=400):
    return (
        jsonify(
            {
                "success": False,
                "error": {"code": code, "message": message},
            }
        ),
        status,
    )
