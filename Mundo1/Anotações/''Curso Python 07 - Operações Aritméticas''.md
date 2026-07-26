Operadores Aritméticos:
> +  Adição
> -   Subtração
> *   Multiplicação
> ** Potência
> /   Divisão
> //  Divisão Inteira
> %  Resto da Divisão

```python
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2,5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1
```

Ordem de precedência
1. Parêntesis
2. Potência
3. Multiplicação, Divisão, Divisão Inteira, Resto da Divisão
4. Mais e Menos

##### 1. Parâmetro `end` na função `print`
O parâmetro `end` controla o que acontece no final da linha. Por padrão, o `print` pula para a próxima linha `(\n)`

pra manter dois print na mesma linha:
```Python
print('Olá', end=' >>> ') # Pode por qualquer coisa no end
print('Mundo')
# saída: olá >>> Mundo
```

##### 2. Formatação com chaves `{}` (26:59 - 28:10)
No Python 3, a forma mais moderna de formatar strings é usando o método `.format()` com as chaves `{}` como marcadores de posição.

```python
print("A soma é {} e o produto é {}".format(s, m))
```
Você pode controlar casas decimais:
:.3f significa: formatar como float com 3 casas decimais
```python
print("A divisão é {:.3f}".format(divisao))
```
print("A divisão é {:.3f}".format(divisao))