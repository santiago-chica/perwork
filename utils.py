from base64 import b64encode

def base_64_encode(txt:str):
    return b64encode(bytes(txt, 'UTF-8')).decode()