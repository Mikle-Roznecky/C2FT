import msvcrt
import os
import sys
import time
from itertools import chain
from decorators import WindowsOnly
from tool import getByteKey, stdout, savedata, cleardata

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
    print(char)
    
    if char == b'\x08':
        if len(bufferl) > 0:
            bufferl.pop()
            stdout("\b \b")
    elif char == b'\r' or char == b'\x03': break
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

@WindowsOnly
def inputPath(start_up_text = None, key_stop_byte = b'\r', key_stop = "enter"):
    if start_up_text != None:
        print(start_up_text, end="", flush=True)
    cleardata()
    buffer = [[], []]
    cursor = 0
        
    while True:
        text = ""
        char = msvcrt.getch()
        STOP_SIGNALS = (getByteKey(key_stop), key_stop_byte, b'\x03')
        if char in STOP_SIGNALS:
            text += ", BREAK!"
            return "".join(chain(buffer[0], "|", buffer[1]))
        
        elif char == b'\x08':
            if len(buffer[0]) > 0:
                buffer[0].pop()
                stdout("\b \b")
                text += ", delete!"
                if len(buffer[1]) > 0:
                    stdout("".join(buffer[1]) + " ")
                    stdout("\b" * (len(buffer[1]) + 1))
                       
        elif char in (b'\xe0', b'\x00'):
            arrows_keys = {
                b'H': [0, 1],
                b'P': [0, -1],
                b'K': [-1, 0],
                b'M': [1, 0]
            }
            next_char = msvcrt.getch()
            text += f", Special Symbol, next char: {next_char}"
            if next_char in arrows_keys:
                if (arrows_keys[next_char])[0] == -1:
                    if len(buffer[0]) > 0:
                        buffer[1].insert(0, buffer[0][-1])
                        buffer[0].pop()
                        stdout("\b")
                        text += "  <==="
                if (arrows_keys[next_char])[0] == 1:
                    if len(buffer[1]) > 0:
                        buffer[0].append(buffer[1][0])
                        del buffer[1][0]
                        text += "  ===>"
                        stdout(buffer[0][-1])
            
        else:   
            try:
                symbol = char.decode("cp866")
                if ord(symbol) > 32:
                    buffer[0].append(symbol)
                    cursor += 1
                    if len(buffer[1]) == 0:
                        sys.stdout.write(symbol)
                        text += "Append symbol"
                    else:
                        stdout(symbol)
                        stdout("".join(buffer[1]))
                        stdout("\b" * len(buffer[1]))
                        text += f", rewrite symbols, New: {"".join(buffer[1])}"
                    sys.stdout.flush()
                    
            except UnicodeDecodeError:
                pass
                            
x = inputPath("Input Your Path: ")
