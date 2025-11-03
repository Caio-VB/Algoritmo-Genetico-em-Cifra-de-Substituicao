# Algoritmo Genético para Cifra de Substituição

Este projeto implementa um **Algoritmo Genético (AG)** para decifrar uma
**cifra de substituição monoalfabética** (apenas letras maiúsculas A–Z e espaço).

Há duas variantes principais:

- `decifrar_menor.py` — script configurado para um **texto menor**  
- `decifrar_maior.py` — script configurado para um **texto maior**

Cada script lê um arquivo com o texto cifrado em bits (0/1) e tenta encontrar
uma chave (permutações do alfabeto) que produza um texto legível em inglês.

---

## Arquivos

- `decifrar_menor.py`
- `decifrar_maior.py`
- `cifrado_menor.txt`
- `cifrado_maior.txt`
- `requirements.txt`

---

## Requisitos

- Python 3.8 ou superior  
- Nenhuma biblioteca externa (só biblioteca padrão)

---

## Artigo Relacionado

Este código foi utilizado e discutido no artigo:

> **“Algoritmo Genético para Decifragem de Cifra de Substituição: Efeitos de Tamanho do Texto, Dicionário e Operadores de Crossover”**  
> Caio Vilor Brandão, Mateus Coelho Silva

O artigo descreve a modelagem do problema, os operadores genéticos utilizados
(OX e PMX) e discute empiricamente por que o OX é recomendado como operador
padrão de *crossover* nessa tarefa.
