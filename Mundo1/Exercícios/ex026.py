frase = str(input('Digite uma frase: ')).lower().strip()

print(f"""
    Frase Usada: '{frase.title()}'
    Quantas vezes aparece a letra A: {frase.count('a')}
    Posição que aparece a primeira vez: {frase.find('a')+1}
    Posição que aparece a última vez: {frase.rfind('a')+1}
""")