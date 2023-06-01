def result(txt):
    print('--' * len(txt))
    print('PLACAR'.center(16))
    print('--' * len(txt))

import time
from random import choice
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool

def timeout(seconds):
    def decorator(function):
        def wrapper(*args, **kwargs):
            pool = ThreadPool(processes=1)
            result = pool.apply_async(function, args=args, kwds=kwargs)
            try:
                return result.get(timeout=seconds)
            except TimeoutError as e:
                return e
        return wrapper
    return decorator

def timer(temp_seg):
    while temp_seg:
        mins, secs = divmod(temp_seg, 60)
        tempformat = '\033[1;31m{:02d}:{:02d}\033[m'.format(mins, secs)
        print(tempformat, end='\r')
        time.sleep(1)
        temp_seg -= 1
    print('Seu tempo acabou!!!')

questoes = ('Em que ano vocês se conheceram ?',
            'Juntos há quanto tempo ?',
            'Qual a cor preferida do seu parceiro(a) ?',
            'O que vocês mais gostam de fazer juntos, segundo seu parceiro(a) ? ',
            'O que mais chamou a atenção do seu parceiro(a) quando se conheceram?',
            'O que é mais importante no relacionamento de vocês pro seu parceiro(a) ?',
            'Qual o signo do seu parceiro(a) ?',
            'Qual culinária seu parceiro(a) prefere ?',
            'Qual o nome do melhor amigo(a) do seu parceiro(a) ?',
            'Aniversário de namoro ?')
alt1 = ('(A) 2009', '(B) 2013', '(C) 2010', '(D) 2011')
alt2 = ('(A) 11 anos e 2 meses', '(B) 9 anos e 11 meses', '(C) 10 anos e 3 meses', '(D) 10 anos e 4 meses')
alt3 = ('(A) Azul', '(B) Roxo', '(C) Amarelo', '(D) Verde')
alt4 = ('(A) Cozinhar', '(B) Viajar', '(C) Assistir série', '(D) Ir ao cinema')
alt5 = ('(A) Cabelo', '(B) Nariz', '(C) Boca', '(D) Olhos')
alt6 = ('(A) Companherismo', '(B) Amizade', '(C) Lealdade', '(D) Franqueza')
alt7 = ('(A) Capricórnio', '(B) Touro', '(C) Escorpião', '(D) Gêmeos')
alt8 = ('(A) Japonesa', '(B) Mexicana', '(C) Brasileira', '(D) Italiana')
alt9 = ('(A) Thais', '(B) Wagner', '(C) Erick', '(D) Amanda')
alt10 = ('(A) 24/02', '(B) 24/01', '(C) 24/05', '(D) 15/10')

random1 = choice(alt1)
random2 = choice(alt2)
random3 = choice(alt3)
random4 = choice(alt4)
random5 = choice(alt5)
random6 = choice(alt6)
random7 = choice(alt7)
random8 = choice(alt8)
random9 = choice(alt9)
random10 = choice(alt10)


'''respostas_certas = ('C', 'D', 'D', 'B', 'C', 'A', 'C', 'A', 'B', 'A')
respostas = []
respostas1 = []
pontuacao = 0
num_questoes = 0

for q in questoes:
    print('-' * (len(q)))
    print(f'{num_questoes + 1}) {q}')
    time.sleep(1)
    for a in alternativas[num_questoes]:
        print(a)
        time.sleep(0.5)
    print('Você tem 2 tentativas para acertar e terá 30 segundos para dar a sua resposta.')
    print('Cada pergunta vale 10 pontos.')
    time.sleep(0.2)
    @timeout(30)
    def read_resp():
        return input('Digite sua resposta: ').upper()
        timer(30)
    resp = read_resp()
    
    if isinstance(resp, TimeoutError):
        print('Seu tempo acabou!!!')
    else:
        continue   
    if resp == respostas_certas[num_questoes]:
        respostas.append(resp)
        pontuacao += 1
        print('Resposta \033[1;32mCORRETA!\033[m')
    else:
        print('Resposta \033[1;31mINCORRETA.\033[m Você tem mais uma tentativa.')
        resp = str(input('Digite sua resposta: ')).upper()
        respostas1.append(resp)
        if resp == respostas_certas[num_questoes]:
            pontuacao += 1
            print('Resposta \033[1;32mCORRETA!\033[m')
        else:
            print(f'Resposta \033[1;31mINCORRETA NOVAMENTE.\033[m A resposta certa seria a alternativa \033[1;34m{respostas_certas[num_questoes]}\033[m')
 
    num_questoes += 1

result('resultado')
print('Respostas Certas: ', end='')
for r in respostas_certas:
    print(r, end=' ')
print()
print('Respostas Dadas 1ª tentativa: ', end='')
for r in respostas:
    print(r, end=' ')
print()
print('Respostas Dadas 2ª tentativa: ', end='')
for r in respostas1:
    print(r, end=' ')

print()
pontuacao = pontuacao/len(questoes) * 100
print('Sua pontuação final foi de \033[4;33m{:.1f}\033[m pontos e você levou \033[4;33m{:.1f}\033[m segundos para terminar o quiz de namoro.'.format(pontuacao,temp))

'''