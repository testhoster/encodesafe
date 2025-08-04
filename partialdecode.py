def strip_wrappers(data):
    data = data.replace('<', '').replace('>', '')
    return base64.b64decode(data).decode()