import sys

def getByteKey(key: str):
    KeyByte = {
        "enter": b'\r',
        "esc": b'\x1b',
        "escape": b'\x1b'
    }
    return KeyByte[key]
    
def rprint(text: str): print(f"\r{text}", end="")
def stdout(text: str): sys.stdout.write(text); sys.stdout.flush()

def savedata(data: str, file="./outdata.txt", mode='a'):
    with open(file=file, mode=mode, encoding='utf-8') as file:
        file.write(data + "\n")
        
def cleardata(file="./outdata.txt"):
    with open(file=file, mode="w", encoding='utf-8') as file:
        file.write("")