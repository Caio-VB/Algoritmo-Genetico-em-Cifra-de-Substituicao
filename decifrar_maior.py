import random
from pathlib import Path

palavras_ingles = {'A', 'AN', 'THE', 'I', 'YOU', 'HE', 'SHE', 'IT', 'WE', 'THEY', 'ME', 'HIM', 'HER', 'US', 'THEM', 'MY', 'YOUR', 'HIS', 'ITS', 'OUR', 'THEIR', 'MINE', 'YOURS', 'HERS', 'OURS', 'THEIRS', 'THIS', 'THAT', 'THESE', 'THOSE', 'EACH', 'EVERY', 'SOME', 'ANY', 'NO', 'NONE', 'ALL', 'BOTH', 'EITHER', 'NEITHER', 'AM', 'ARE', 'IS', 'WAS', 'WERE', 'BE', 'BEEN', 'BEING', 'HAVE', 'HAS', 'HAD', 'DO', 'DOES', 'DID', 'CAN', 'COULD', 'MAY', 'MIGHT', 'SHALL', 'SHOULD', 'WILL', 'WOULD', 'MUST', 'OF', 'TO', 'IN', 'FOR', 'ON', 'WITH', 'AT', 'BY', 'FROM', 'ABOUT', 'INTO', 'OVER', 'AFTER', 'BEFORE', 'BETWEEN', 'UNDER', 'THROUGH', 'DURING', 'WITHOUT', 'WITHIN', 'AGAINST', 'AMONG', 'AROUND', 'ACROSS', 'BEHIND', 'ABOVE', 'BELOW', 'NEAR', 'AND', 'OR', 'BUT', 'SO', 'BECAUSE', 'THOUGH', 'ALTHOUGH', 'WHILE', 'IF', 'THEN', 'THAN', 'AS', 'WHEN', 'WHERE', 'UNTIL', 'NOT', 'NO', 'YES', 'VERY', 'REALLY', 'JUST', 'ONLY', 'ALSO', 'EVEN', 'STILL', 'ALWAYS', 'OFTEN', 'USUALLY', 'SOMETIMES', 'NEVER', 'ALREADY', 'AGAIN', 'TOGETHER', 'HOWEVER', 'MAYBE', 'PROBABLY', 'BE', 'HAVE', 'DO', 'SAY', 'TELL', 'GO', 'COME', 'GET', 'MAKE', 'TAKE', 'GIVE', 'KNOW', 'THINK', 'SEE', 'LOOK', 'WANT', 'NEED', 'USE', 'WORK', 'TRY', 'CALL', 'ASK', 'FEEL', 'BECOME', 'LEAVE', 'PUT', 'MEAN', 'KEEP', 'LET', 'BEGIN', 'SEEM', 'HELP', 'TALK', 'TURN', 'START', 'PLAY', 'MOVE', 'LIVE', 'BELIEVE', 'BRING', 'HAPPEN', 'WRITE', 'PROVIDE', 'SIT', 'STAND', 'LOSE', 'PAY', 'MEET', 'INCLUDE', 'CONTINUE', 'SET', 'LEARN', 'CHANGE', 'LEAD', 'UNDERSTAND', 'WATCH', 'FOLLOW', 'STOP', 'CREATE', 'SPEAK', 'READ', 'SPEND', 'GROW', 'OPEN', 'WALK', 'WIN', 'OFFER', 'REMEMBER', 'LOVE', 'CONSIDER', 'APPEAR', 'BUY', 'WAIT', 'SERVE', 'SEND', 'EXPECT', 'BUILD', 'STAY', 'FALL', 'CUT', 'REACH', 'REMAIN', 'RETURN', 'EXPLAIN', 'SHOW', 'AGREE', 'DECIDE', 'TIME', 'YEAR', 'WAY', 'DAY', 'THING', 'MAN', 'WOMAN', 'CHILD', 'WORLD', 'LIFE', 'HAND', 'PART', 'EYE', 'PLACE', 'WORK', 'WEEK', 'CASE', 'POINT', 'GOVERNMENT', 'COMPANY', 'NUMBER', 'GROUP', 'PROBLEM', 'FACT', 'HOME', 'SCHOOL', 'STATE', 'FAMILY', 'STUDENT', 'COUNTRY', 'CITY', 'SERVICE', 'AREA', 'MONEY', 'STORY', 'ISSUE', 'SIDE', 'KIND', 'HEAD', 'HOUSE', 'FRIEND', 'FATHER', 'MOTHER', 'POWER', 'HOUR', 'GAME', 'LINE', 'END', 'MEMBER', 'LAW', 'CAR', 'COMMUNITY', 'NAME', 'TEAM', 'MINUTE', 'IDEA', 'KID', 'BODY', 'INFORMATION', 'BACK', 'PARENT', 'FACE', 'DOOR', 'WATER', 'FOOD', 'AIR', 'ROOM', 'WORD', 'LETTER', 'PHONE', 'MESSAGE', 'GOOD', 'NEW', 'FIRST', 'LAST', 'LONG', 'GREAT', 'LITTLE', 'OWN', 'OTHER', 'OLD', 'RIGHT', 'BIG', 'HIGH', 'DIFFERENT', 'SMALL', 'LARGE', 'NEXT', 'EARLY', 'YOUNG', 'IMPORTANT', 'FEW', 'PUBLIC', 'BAD', 'SAME', 'ABLE', 'BEST', 'BETTER', 'CLEAR', 'FULL', 'REAL', 'TRUE', 'FREE', 'HARD', 'EASY', 'LATE', 'SHORT', 'STRONG', 'SURE', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'HUNDRED', 'THOUSAND', 'MILLION', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER', 'TODAY', 'YESTERDAY', 'TOMORROW', 'MORNING', 'AFTERNOON', 'EVENING', 'NIGHT'}

ascii32 = [chr(32 + i) for i in range(95)]
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

bytes = Path("cifrado_maior.txt").read_text(encoding="utf-8")
cifrada = []
fitness = []
melhor_fitness = 0
melhor_individuo = []

for byte in bytes.split():
    codigo = 0
    while len(byte) < 8: 
        byte = f"0{byte}"
    for i, bit in enumerate(byte):
        if i == 0 and bit == "1": 
            codigo += 128
        if i == 1 and bit == "1": 
            codigo += 64
        if i == 2 and bit == "1": 
            codigo += 32
        if i == 3 and bit == "1": 
            codigo += 16
        if i == 4 and bit == "1": 
            codigo += 8
        if i == 5 and bit == "1": 
            codigo += 4
        if i == 6 and bit == "1": 
            codigo += 2
        if i == 7 and bit == "1": 
            codigo += 1
    caracter = ascii32[codigo-32]
    cifrada.append(caracter)

def pupulacao_inicial(individuos=10):
    return [random.sample(alfabeto, len(alfabeto)) for _ in range(individuos)]

tamanho_populacao = 10
populacao = pupulacao_inicial(tamanho_populacao)

def busca_posicao(letra):
    for i in range(len(alfabeto)):
        if alfabeto[i] == letra:
            return i
    return -1

def busca_letra(individuo, posicao):
    if posicao < 0:
        return " "
    return individuo[posicao]

def crossover_ox(p1, p2):
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    filho = [None] * n
    filho[a:b] = p1[a:b]
    pos = b
    for x in p2[b:] + p2[:b]:
        if x not in filho:
            if pos >= n:
                pos = 0
            filho[pos] = x
            pos += 1
    return filho

import random

def crossover_pmx(p1, p2):
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    filho = [None] * n

    filho[a:b] = p1[a:b]
    seg_set = set(p1[a:b])

    map_p2 = {p1[i]: p2[i] for i in range(a, b)}

    for i in list(range(0, a)) + list(range(b, n)):
        x = p2[i]
        while x in seg_set:
            x = map_p2.get(x, x)
        filho[i] = x

    return filho

def mutacao_swap(individuo, taxa_mutacao=0.35):
    if len(individuo) >= 2 and random.random() < taxa_mutacao:
        a, b = random.sample(range(len(individuo)), 2)
        individuo[a], individuo[b] = individuo[b], individuo[a]
    return individuo


def roleta(pesos, total):
    r, acum = random.uniform(0, total), 0
    for idx, peso in enumerate(pesos):
        acum += peso
        if r <= acum:
            return idx
    return len(pesos) - 1

geracao = 0
while geracao < 5000:
    decifradas = []
    
    for i, individuo in enumerate(populacao):
        linha = []
        for j, letra in enumerate(cifrada):
            linha.append(busca_letra(individuo, busca_posicao(letra)))
        decifradas.append(linha)

    palavras_decifradas = []
    for linha in decifradas:
        s = ''.join(map(str, linha)) 
        palavras = s.split(' ')
        palavras_decifradas.append(palavras)
        
    fitness = []
    for i, linha in enumerate(palavras_decifradas):
        count = 0
        vistos = set()
        for palavra in linha:
            if palavra in palavras_ingles and palavra not in vistos:
                count += 1
                vistos.add(palavra)
        fitness.append(count)
        if count >= melhor_fitness:
            melhor_fitness = count
            melhor_decifrado = linha
            melhor_cifra = populacao[i]
    print(fitness)

    numero_de_pares = tamanho_populacao // 2
    nova_populacao = []

    for _ in range(numero_de_pares):
        pesos = [max(0, p)**9 for p in fitness]
        total = sum(pesos)
        if total == 0:
            i = random.randrange(len(populacao))
            j = random.randrange(len(populacao))
            while j == i and len(populacao) > 1:
                j = random.randrange(len(populacao))
        else:
            i = roleta(pesos, total)
            
            r = random.uniform(0, total)
            acum = 0
            i = 0
            for idx, peso in enumerate(pesos):
                acum += peso
                if r <= acum:
                    i = idx
                    break
            
            tentativas = 0
            j = i
            while j == i and tentativas < 5:
                j = roleta(pesos, total)
                tentativas += 1
            if j == i:
                j = random.randrange(len(populacao))
                while j == i and len(populacao) > 1:
                    j = random.randrange(len(populacao))

        pai1 = populacao[i]
        pai2 = populacao[j]
        meio = len(pai1) // 2

        filho1 = crossover_ox(pai1, pai2)
        filho2 = crossover_ox(pai2, pai1)
        
        taxa_mutacao = 0.35
        filho1 = mutacao_swap(filho1, taxa_mutacao)
        filho2 = mutacao_swap(filho2, taxa_mutacao)

        nova_populacao.append(filho1)
        nova_populacao.append(filho2)
    
    populacao = nova_populacao
    geracao += 1


print(melhor_fitness)
print(melhor_individuo)
        


