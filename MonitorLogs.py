import random
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print('Monitor LogPy')
        print('1 - Gerar logs')
        print('2 - Analisar Logs')
        print('3 - Gerar e Analisar logs')
        print('4 - Sair')
        opcao = input('Escolha um opção: ')
        if opcao == '1':
            try:
                qtd = int(input('Quantidade de logs'))
                gerarArquivo(nome_arq, qtd)
            except:
                print('Qtd incorreta')
        elif opcao == '2':
            analisarLog(nome_arq)
        elif opcao == '3':
            try:
                qtd = int(input('Quantidade de logs'))
                gerarArquivo(nome_arq, qtd)
                analisarLog(nome_arq)
            except:
                print('Qtd incorreta')
        elif opcao == '4':
            print('Ate Mais')
            break
        else:
            print('Opção errada')

def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + '\n')
        print('Logs gerados')
        
def montarLog(i):
    data = gerarDataHora (i)
    ip = gerarIP(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status =  gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 500mb - HTTP/2.0 - {agente} - /home'

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22,8 ,0)
    data = datetime.timedelta(seconds=i * random.randint(5,20))
    return (base + data).strftime('%d/%m/%Y %H:%M:%S')

def gerarIP(i):
    r = random.randint(1, 6)
    
    if i >= 20 and i <= 30:
        return '400.2.892.200'
    
    if r == 1:
        return '192.168.5.6'
    #return f'{random.radint(1, 255), random.radint(8, 255), random.radint(6, 255)}'
    elif r== 2:
        return '192.168.1.2'
    elif r== 3:
        return '192.168.7.9'
    elif r== 4:
        return '192.168.8.5'
    elif r== 5:
        return '192.168.8.4'
    else:
        return '192.168.3.1'

def gerarRecurso(i):
    if i % 6 == 0:
        return '/login'
    elif i % 8 == 0:
        return '/admin'
    elif i % 9 == 0:
        return '/produtos'
    elif i % 11 == 0:
        return '/dashboard'
    else:
        return '/home'


def gerarMetodo(i):
    if i % 6 == 0 or i % 8 == 0:   
        return 'POST'
    else:
        return 'GET'


def gerarStatus(i):
    if i % 3 == 0 and i % 6 == 0:      
        return '403'
    elif i % 8 == 0:                   
        return '403'
    elif i % 7 == 0:
        return '404'
    elif i % 15 == 0:
        return '500'
    else:
        return '200'


def gerarTempo(i):
    if 25 <= i <= 35:                  
        return 150 + (i - 25) * 70
    elif i % 5 == 0:
        return 850
    else:
        return random.randint(90, 650)


def gerarAgente(i):
    if i % 10 == 0:
        return 'Mozilla Bot Crawler'
    elif i % 17 == 0:
        return 'Python-urllib'
    else:
        return 'Chrome'

def analisarLog(nome_arq):
    print('\n🔄 Iniciando análise do arquivo...')
    print('⚠️  Função de análise ainda em desenvolvimento.')
    print('Quer que eu faça a análise completa agora (sem split, sem listas, estilo pílulas)?')



if __name__ == "__main__":
    menu()
