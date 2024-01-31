# CAESAR'S CIPHER
def encrypt_caesar(string, key):
    enc=""
    string = string.upper()
    for i in range(len(string)):
        char = string[i]
        enc += chr((ord(char)+key-65)%26 + 65)            
    return enc

def decrypt_caesar(enc, key):
    string=""
    for i in range(len(enc)):
        char = enc[i]
        string += chr((ord(char)-key-65)%26 + 65)
    return string
# For rot 13 give key = 13

# VIGNERE'S CIPHER
def generateKey(string, key):
    key = key.upper()
    key = list(key)
    if len(string)==len(key):
        return key
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return("".join(key))

def encrypt_vignere(string, key):
    key = generateKey(string, key)
    string = string.upper()
    cipher=[]
    for i in range(len(string)):
        x = (ord(string[i])+ord(key[i]))%26
        x += 65
        cipher.append(chr(x))
    return ("".join(cipher))

def decrypt_vignere(cipher, key):
    key = generateKey(cipher, key)
    string = []
    for i in range(len(cipher)):
        x = (ord(cipher[i])-ord(key[i]) + 26)%26
        x += 65
        string.append(chr(x))
    return ("".join(cipher))

# RAILWAY FENCE TRANSPOSITION CIPHER
def encrypt_railfence(string, key):
    rail = [['\n' for i in range(len(string))] for j in range (key)]
    go_down = False
    row, col = 0, 0
    
    for i in range(len(string)):
        if (row==0) or (row==key-1):
            go_down = not go_down
            
        rail[row][col] = string[i]
        col += 1
        
        if go_down:
            row += 1
        else:
            row -= 1
        
    result = []
    for i in range(key):
        for j in range(len(string)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
                
    return("".join(result))
    
def decrypt_railfence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range (key)]
    go_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            go_down = True
        if row == key-1:
            go_down = False
        
        rail[row][col] = "*"
        col +=1 
        
        if go_down:
            row += 1
        else:
            row -= 1
        
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j]=='*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
                
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        
        if row == 0:
            go_down = True
        if row == key-1:
            go_down = False
            
        if (rail[row][col] != "*"):
            result.append(rail[row][col])
            col+=1
            
        if go_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))

# COLUMNAR TRANSPOSITION CIPHER
import math

def encrypt_columnar(string, key):
    cipher = ""
    k_index = 0
    
    str_len = float(len(string))
    str_list = list(string)
    key_list = sorted(list(key))
    
    col = len(key)
    
    row = int(math.ceil(str_len/col))
    
    fill_null = int((row*col)-str_len)
    str_list.extend('_'*fill_null)
    
    matrix = [str_list[i: i+col]
             for i in range(0, len(str_list), col)]
    
    for _ in range(col):
        current_index = key.index(key_list[k_index])
        cipher += ''.join([row[current_index]
                         for row in matrix])
        k_index += 1
    
    return cipher

def decrypt_columnar(cipher, key):
    string = ''
    k_index = 0
    
    str_index = 0
    str_len = float(len(cipher))
    str_list = list(cipher)
    
    col = len(key)
    row = int(math.ceil(str_len/col))
    
    key_list = sorted(list(key))
    
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None]*col]
        
    for _ in range(col):
        current_index = key.index(key_list[k_index])
        
        for j in range(row):
            dec_cipher[j][current_index] = str_list[str_index]
            str_index += 1
        k_index += 1
        
    
    string = ''.join(sum(dec_cipher, []))
     
    null_count = string.count('_')
 
    if null_count > 0:
        return string[: -null_count]
 
    return string

