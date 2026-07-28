frase = input('Digite uma frase: ')

print(f"""
    Quantas vezes aparece a letra A: {frase.lower().count('a').r}
    Posição que aparece a primeira vez: {frase.lower().find('a')}
    Posição que aparece a última vez: {frase.lower().rfind('a')}
""")