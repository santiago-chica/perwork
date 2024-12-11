from base64 import b64encode, b64decode
def base64Encode(txt:str):
    return b64encode(bytes(txt, 'UTF-8')).decode()

if __name__ == '__main__':
    encod = base64Encode('Holaaa')
    decod = b64decode(encod).decode()
    print(decod)