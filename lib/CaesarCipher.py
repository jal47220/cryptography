alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = "SECRET MESSAGE"
key = 3

def generate_alpha_map(key):
    alpha_map = {}
    
    i = 0
    for char in alphabet:
        # Modulus facilitates wrapping when iterating over a list with a shift (i.e. the key)
        alpha_map[char] = alphabet[(i + key) % len(alphabet)] 
        
        i += 1
    return alpha_map

def encrypt(message, alpha_map):
    cipher = ""
    for char in message:
        if char in alpha_map:
            cipher += alpha_map[char]
        else:
            cipher += char
    return cipher 

def decrypt_with_key(message, key):
    mirrored_alpha_map = generate_alpha_map(-key)
    return encrypt(message, mirrored_alpha_map)

def decrypt_with_alpha_map(message, alpha_map):
    inverted_alpha_map = {value: key for key, value in alpha_map.items()}
    return encrypt(message, inverted_alpha_map)
    
alpha_map = generate_alpha_map(key)
cipher = encrypt(message, alpha_map)
key_translated_msg = decrypt_with_key(cipher, key)
map_translated_msg = decrypt_with_alpha_map(cipher, alpha_map)
print(message == key_translated_msg == map_translated_msg)
