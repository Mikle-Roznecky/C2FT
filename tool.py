def getByteKey(key: str):
    KeyByte = {
        "enter": b'\r',
        "esc": b'\x1b',
        "escape": b'\x1b'
    }
    return KeyByte[key]
    
def rprint(text: str): print(f"\r{text}", end="")