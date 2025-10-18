from itertools import permutations
from nltk.corpus import words
import nltk

# ✅ ეს ხაზი საჭიროა მხოლოდ ერთხელ — ჩამოტვირთავს ლექსიკონს
nltk.download('words')

# ლექსიკონის მომზადება
english_words = set(word.lower() for word in words.words())

# Caesar Cipher-ის დეკრიფცია
def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted.lower()

ciphertext = "mznxpz"

# ყველა shift-ის ცდა
for shift in range(1, 26):
    decrypted = caesar_decrypt(ciphertext, shift)
    perms = set(''.join(p) for p in permutations(decrypted))
    matches = [word for word in perms if word in english_words]
    if matches:
        print(f"\n🔁 Shift {shift} → Caesar result: {decrypted}")
        print(f"✅ Valid English word(s): {matches}")
