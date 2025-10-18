import base64

def xor_decrypt(ciphertext_b64, key):
    ciphertext = base64.b64decode(ciphertext_b64)
    key_bytes = key.encode()
    decrypted = bytearray()
    for i in range(len(ciphertext)):
        decrypted.append(ciphertext[i] ^ key_bytes[i % len(key_bytes)])
    return decrypted.decode('utf-8', errors='ignore')

ciphertext_b64 = "Jw0KB1IMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
candidates = ['becoom', 'ceruse', 'rescue', 'recuse', 'cereus', 'secure']

for key in candidates:
    result = xor_decrypt(ciphertext_b64, key)
    print(f"\n🔑 Key: {key}")
    print(f"📤 Decrypted: {result}")
