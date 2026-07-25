from flask import request


def paginate_query(query):
    page = max(1, request.args.get("page", default=1, type=int))
    limit = max(1, min(100, request.args.get("limit", default=20, type=int)))
    pagination = query.paginate(page=page, per_page=limit, error_out=False)
    return pagination.items, {
        "page": page,
        "limit": limit,
        "total": pagination.total,
        "pages": pagination.pages,
    }
