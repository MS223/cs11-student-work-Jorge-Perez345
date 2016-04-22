def de_vowel(some_string):
    for n in some_string:
        if n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != "u":
            return n
print de_vowel()
