def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")
