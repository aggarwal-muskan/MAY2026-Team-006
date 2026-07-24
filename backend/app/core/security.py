from functools import wraps

from flask_jwt_extended import get_jwt, verify_jwt_in_request

from app.core.responses import fail


ROLE_ADMIN = "admin"
ROLE_OWNER = "owner"
ROLE_TENANT = "tenant"
ROLE_SERVICE_PROVIDER = "service_provider"
ROLE_SECURITY = "security"


def roles_required(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            role = claims.get("role")
            if role not in roles:
                return fail("You do not have permission for this resource", "FORBIDDEN", 403)
            return fn(*args, **kwargs)

        return wrapper

    return decorator
