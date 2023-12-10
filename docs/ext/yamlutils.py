def ensure_dict(o) -> dict:
    if o is None:
        return {}
    elif isinstance(o, dict):
        return o
    raise ValueError("Expected dictionary")

def set_default_values(o: dict, default) -> dict:
    return { key: value if value is not None else default for (key,value) in o.items() }
