import msvcrt
import os
import sys
import time
from decorators import WindowsOnly
from tool import rprint, getByteKey

d = False
if "-d" in sys.argv: d = True

@WindowsOnly
def findDisk():
    drives = [d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{d}:\\")]
    return drives

print(findDisk())
bufferl = []

# DEBUG 
while d:
    char = msvcrt.getch()
    
    if char == b'\x08':
        if len(bufferl) > 0:
            bufferl.pop()
            sys.stdout.write("\b \b")
            sys.stdout.flush()
    elif char == b'\r': break
    elif char == b'\xe0' or char == b'\x00':
        msvcrt.getch()
        continue
    else:
        try:
            symbol = char.decode("cp866")
            if ord(symbol) >= 32:
                bufferl.append(symbol)
                sys.stdout.write(symbol)
                sys.stdout.flush()
        except: pass
print("".join(bufferl)) 
    
def inputWithC2FT(start_up_text = None, key_stop_byte = b'\r', key_stop = "enter"):
    if start_up_text != None:
        print(start_up_text)
    buffer = []
    while True:
        char = msvcrt.getch()
        
        if char == getByteKey(key_stop) or char == key_stop_byte:
            return "".join(buffer)
        
        if char == b'\x08':
            if len(buffer) > 0:
                buffer.pop()
                sys.stdout.write("\b \b")
                sys.stdout.flush()

        if char == b'\xe0' or char == b'\x00':
            arrows_keys = {
                b'H': [0, 1],
                b'P': [0, -1],
                b'K': [-1, 0],
                b'M': [1, 0]
            }
            next_char = msvcrt.getch()
            continue
        
        try:
            symbol = char.decode("cp866")
            if ord(symbol) > 32:
                buffer.append(symbol)
                sys.stdout.write(symbol)
                sys.stdout.flush()
                
        except UnicodeDecodeError:
            pass
        time.sleep(0.001)
                    
        
x = inputWithC2FT()
