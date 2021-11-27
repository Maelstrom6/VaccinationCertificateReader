import base64
import json
import base45
import uuid
import hashlib
from io import BytesIO

def get_hcert(base64str):
    result: bytes = base64.b64decode(base64str)
    return json.loads(result.decode("utf-8"))


if __name__ == '__main__':
    s = "eyJpZFR5cGUiOiJSU0FJRCIsImlkVmFsdWUiOiI5OTA2MDc1NjEwMDg4IiwiZmlyc3ROYW1lIjoiQ2hyaXN0b3BoZXIgSm9uIiwic3VybmFtZSI6IkR1IFBsZXNzaXMiLCJkYXRlT2ZCaXJ0aCI6IjA3LUp1bi0xOTk5IiwiaW1tdW5pemF0aW9uRXZlbnRzIjpbeyJ2YWNjaW5lUmVjZWl2ZWQiOiJDb21pcm5hdHkiLCJ2YWNjaW5lRGF0ZSI6IjMwLUF1Zy0yMDIxIiwicHJvb2ZPZlZhY2NpbmVDb2RlIjoiVjRYVk45TDRGRlJFIn0seyJ2YWNjaW5lUmVjZWl2ZWQiOiJDb21pcm5hdHkiLCJ2YWNjaW5lRGF0ZSI6IjExLU9jdC0yMDIxIiwicHJvb2ZPZlZhY2NpbmVDb2RlIjoiVkhGRlBDRVZDM1lBIn1dLCJleHBpcnlEYXRlIjoiMTItSmFuLTIwMjIifQ=="
    # print(str(s))
    # print(type(s))
    # s = "21b7cea9-a2b7-485c-85b7-9ac7768f1b55"
    # print(uuid.UUID(s))
    # print(base64.b64decode("WyFCevnATatCiPW"))
    digest = hashlib.sha256(bytes(s, encoding="utf-8")).digest()
    print(base64.b64encode(digest))