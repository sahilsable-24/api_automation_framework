USER_SCHEMA = {
    "type" : "object",
    "properties":{
        "id" : {"type":"integer"},
        "email" : {"type":"string"},
        "first_name" : {"type":"string"},
        "last_name" : {"type":"string"},
        "avatar" : {"type":"string"},
    },
    "required":["id","email","first_name","last_name", "avatar"]
}

USER_LIST_SCHEMA = {
    "type": "object",
    "properties":{
        "page": {"type":"integer"},
        "per_page": {"type":"integer"},
        "total": {"type":"integer"},
        "total_pages": {"type":"integer"},
        "data": {"type":"array", "items":USER_SCHEMA},
    },
    "required":["page", "per_page","total", "data"]
}