"""
2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do
nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três
funções de remoção de espaços: lstrip(), rstrip() e strip().
"""


name = " Francisco "
name_left = name.lstrip()
name_right = name.rstrip()
name_both = name.strip()
print(f"Esse é o nome original: {name}\nEsse nome está sem o espaço inicial: {name_left}.\nEsse nome está sem o espaço final: {name_right}.\nE esse nome está sem os espaços iniciais e sem o espaços finais: {name_both}.")
