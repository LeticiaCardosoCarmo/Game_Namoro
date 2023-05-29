def result(txt):
    print('--' * len(txt))
    print('PLACAR'.center(16))
    print('--' * len(txt))


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
alternativas = (('(A) 2009', '(B) 2013', '(C) 2010', '(D) 2011'),
                ('(A) 11 anos e 2 meses', '(B) 9 anos e 11 meses', '(C) 10 anos e 3 meses', '(D) 10 anos e 4 meses'),
                ('(A) Azul', '(B) Roxo', '(C) Amarelo', '(D) Verde'),
                ('(A) Cozinhar', '(B) Viajar', '(C) Assistir série', '(D) Ir ao cinema'),
                ('(A) Cabelo', '(B) Nariz', '(C) Boca', '(D) Olhos'),
                ('(A) Companherismo', '(B) Amizade', '(C) Lealdade', '(D) Franqueza'),
                ('(A) Capricórnio', '(B) Touro', '(C) Escorpião', '(D) Gêmeos'),
                ('(A) Japonesa', '(B) Mexicana', '(C) Brasileira', '(D) Italiana'),
                ('(A) Thais', '(B) Wagner', '(C) Erick', '(D) Amanda'),
                ('(A) 24/02', '(B) 24/01', '(C) 24/05', '(D) 15/10'))

respostas_certas = ('C', 'D', 'D', 'B', 'C', 'A', 'C', 'A', 'B', 'A')
respostas = []
respostas1 = []
pontuacao = 0
num_questoes = 0

for q in questoes:
    print('-' * (len(q)))
    print(q)
    for a in alternativas[num_questoes]:
        print(a)
    resp = str(input('Digite a resposta correta: ')).upper()
    print('Você tem 2 tentativas para acertar!')
    respostas.append(resp)
    if resp == respostas_certas[num_questoes]:
        pontuacao += 1
        print('Resposta CORRETA!')
    else:
        print('Resposta INCORRETA. Você tem mais uma tentativa.')
        resp = str(input('Digite a resposta correta: ')).upper()
        respostas1.append(resp)
        if resp == respostas_certas[num_questoes]:
            pontuacao += 1
            print('Resposta CORRETA!')
        else:
            print(f'Resposta INCORRETA NOVAMENTE. A resposta certa seria {respostas_certas[num_questoes]}')

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
print(f'Sua pontuação final foi de {pontuacao}%')


    
