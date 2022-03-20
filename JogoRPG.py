from asyncio.windows_events import NULL
import random
from turtle import clear
from drag import drag
from itens import itens
from ogro import ogro
from MonstroPlanta import MonstroPlanta
from heroi import heroi
import os
import time
import funcoes
import math

opcao = 0

os.system('clear')

string = '''

Bem-vindo aventureiro!, 
escolha seu herói para lhe 
representar em suas batalhas

Escolha a classe do seu herói:

[1]guerreiro
[2]mago
[3]arqueiro

'''
funcoes.digitar_historia(string)

raca = NULL
classe = NULL
potion = 0
weapon = "nenhuma"
vest = "nenhuma"
hero = heroi(raca,classe,1,20,200)
inventario = itens(potion,weapon,vest)

opcao = int(input())

if opcao == 1:
    hero.classe = "guerreiro"
elif opcao == 2:
    hero.classe = "mago"
elif opcao == 3:
    hero.classe = "arqueiro"


os.system('clear')

string = f"\n você escolheu a classe {hero.classe}"

funcoes.digitar_historia(string)

string = '''

Escolha agora qual a raça
de seu herói dentre as opções a seguir:

[1]humano
[2]elfo
[3]anão
[4]orc

'''
funcoes.digitar_historia(string)


opcao_raca = int(input())

os.system('clear')

if opcao_raca == 1:
    hero.raca = "humano"
elif opcao_raca == 2:
    hero.raca = "elfo"
elif opcao_raca == 3:
    hero.raca = "anão"
elif opcao_raca == 4:
    hero.raca = "orc"

string = f"\n você escolheu a classe {hero.classe} de raça {hero.raca},\n vamos iniciar sua aventura!"

funcoes.digitar_historia(string)

time.sleep(3)

os.system('clear')

string = '''
Sua aventura começa entrando na floresta maldita aos arredores de midgard,
sua terra foi devastada por monstros do submundo com afinidades elementais,
diversos monstros de elementos diferentes estão causando destruição na Terra,
e você é o herói escolhido para derrotar o Dragão de fogo demoníaco, pois ele 
comanda a horda de monstros, se você derrotá-lo aventureiro, você irá salvar
a Terra e receber glória eterna.
'''

funcoes.digitar_historia(string)

time.sleep(5)

os.system('clear')

matou_monstro = False

string = '''

Andando tranquilamente pela floresta você encontra um monstro planta!,
ele tem uma aparência meio fraca e você com certeza pode derrotá-lo

'''

funcoes.digitar_historia(string)

while matou_monstro == False:
    string = '''

o que você decide fazer?

[1]batalhar com ele
[2]ignorá-lo

    '''

    funcoes.digitar_historia(string)

    opcao_batalha = int(input())

    monstroPlanta1 = MonstroPlanta("pequeno","verde","comum","elemental de planta","1","5",5)

    os.system('clear')

    if opcao_batalha == 1:
        dano = funcoes.ataque(hero.forca)
        monstroPlanta1.vida = round(float(monstroPlanta1.vida)) - dano
        string = f'''

você decidiu atacar o monstro planta!
e causou um total de {round(dano)} de dano
        
        '''

        funcoes.digitar_historia(string)

        if monstroPlanta1.vida <= 0:
            string = "\n você matou o monstro planta!"
            funcoes.digitar_historia(string)
            hero.level = hero.level+1
            matou_monstro = True
        else:
            string = f"\n a vida atual do monstor planda é {round(monstroPlanta1.vida)}"
            funcoes.digitar_historia(string)
            ataque = round(funcoes.ataque(monstroPlanta1.forca))
            hero.vida = hero.vida -  ataque
            string = f"o monstro planta lança um ataque em você causando {ataque} de dano!\n e sua vida atual agora é {hero.vida}"
            funcoes.digitar_historia(string)

    elif opcao_batalha == 2:
        fuga = funcoes.fuga()
        if fuga == True:
            print("você meteu o pé")
            matou_monstro = True
        else:
            print("você tropeçou e não conseguiu fugir!")
            time.sleep(1)
            ataque = round(funcoes.ataque(monstroPlanta1.forca))
            hero.vida = hero.vida -  ataque
            string = f"o monstro planta lança um ataque em você causando {ataque} de dano!\n e sua vida atual agora é {hero.vida}"
            funcoes.digitar_historia(string)
            
    
string = '''

continuando sua viagem aventureiro, gostaria de saber seus status?

[1]sim
[2]não

'''

funcoes.digitar_historia(string)

opcao = int(input())

time.sleep(3)

os.system('clear')


if opcao == 1:
    print(f'''
seu herói possui:
{hero.forca} de força
{hero.level} de level
{hero.vida} de vida

atualmente
    ''')

time.sleep(5)

os.system('clear')

string = '''
Dando continuação à sua aventura, você encontra um baú em seu caminho, deseja abrí-lo ?

[1]sim
[2]não

'''
funcoes.digitar_historia(string)

opcao = int(input())

if opcao == 1:
    chance = random.random()*10
    if chance < 3:
        chance_pocao = random.random()*10
        print("você encontrou uma poção!, ela lhe garantiu um aumento aleatório em algum status")
        if chance_pocao < 5:
            hero.forca = hero.forca + 5
        elif chance_pocao >= 5:
            hero.vida = hero.vida + 5
    elif chance >= 3 and chance <=6 and hero.classe == "guerreiro":
        print("você encontrou um machado grande!, que lhe garantiu um aumento significativo de poder")
        inventario.arma = "machado grande"
        hero.forca = hero.forca + 5
    elif chance >= 3 and chance <=6 and hero.classe == "arqueiro":
        print("você encontrou um arco grande!, que lhe garantiu um aumento significativo de poder")
        inventario.arma = "arco grande"
        hero.forca = hero.forca + 5
    elif chance >= 3 and chance <=6 and hero.classe == "mago":
        print("você encontrou um cetro grande!, que lhe garantiu um aumento significativo de poder")
        inventario.arma = "cetro grande"
        hero.forca = hero.forca + 5
    elif chance > 6:
        print("você encontrou uma couraça demoniaca, que lhe garantiu um aumento significativo de vida")
        inventario.vestimenta = "couraça demoníaca"
        hero.vida = hero.vida + 50

time.sleep(3)

print(f'''
Agora seu herói possui:
{hero.forca} de força
{hero.level} de level
{hero.vida} de vida

atualmente
    ''')

time.sleep(3)

os.system('clear')

string = '''

ao longo de sua jornada você acaba entrando em um pequeno vilarejo, onde nele a pobreza já se tornou 
característica, andando pelas ruas de terra deste vilare você encontra um garotinho cabisbaixo sentado na calçada
ao ver aquela cena o que você faz ?

[1]Se aproxima do garotinho para perguntar qual o problema
[2]Ignora o garotinho e continua sua viagem

'''

funcoes.digitar_historia(string)

opcao = int(input())

os.system('clear')

if opcao == 1:
    string = '''

Ao se aproximar do garotinho ele te dá uma facada e rouba seus pertences!,
Não confie em garotinhos pobres!
    
    ''' 
    funcoes.digitar_historia(string)

    time.sleep(3)

    os.system('clear')

    hero.vida = hero.vida - 50

    if inventario.arma != "nenhuma":
        inventario.arma = "nenhuma"
        hero.forca = hero.forca - 5
    if inventario.vestimenta != "nenhuma":
        inventario.vestimenta = "nenhuma"
        hero.vida = hero.vida - 50
    string = f'''

Agora seu herói possui:
{hero.forca} de força
{hero.level} de level
{hero.vida} de vida

atualmente
    '''
    funcoes.digitar_historia(string)

    time.sleep(3)

    os.system('clear')

elif opcao == 2:
    string = '''
    
Você ignorou o garotinho famindo e triste, provavelmente ele morrerá,
mas acho que isso não importa muito pra você nobre aventureiro!
    
    '''
    funcoes.digitar_historia(string)

    time.sleep(3)

    os.system('clear')

if opcao == 1:

    string = '''

Após sua frustração com o garotinho pobre e perdendo suas esperanças nas pessoas, você
continua sua jornada, ao sentar-se em uma raíz de arvore bem espessa você avista criaturinhas 
andando em sua frente, são gnomos plantadores e eles percebem sua tristeza e se aproximam de você
perguntando-lhe o que está acontecendo, o que você faz ? 

[1]Conversa com os pequeninos
[2]Ignora achando q a facada está te fazendo ter alucinações

    '''

    funcoes.digitar_historia(string)

    opcao2 = int(input())

    os.system('clear')

    if opcao2 == 1:

        string = '''

Dando um voto de confiança aos pequeninos você conta sobre sua jornada, sobre derrotar matar
o lendário Dragão de fogo demoníaco e também sobre sua frustração recente ao tentar ajudar um
pequenino cabisbaixo.

        '''

        funcoes.digitar_historia(string)

        time.sleep(3)

        os.system('clear')

        string = '''
Por dar seu voto de confiança, e também pelos gnomos acharem que você é maluco por estar em
uma jornada tão perigosa e inconsequente, os pequeninos lhe concedem a bênção da floresta
aumentando todos os seus status em 50%, e também dobrando seu level!

        '''
        
        funcoes.digitar_historia(string)

        hero.vida = round(hero.vida + hero.vida/2)
        hero.forca = round(hero.forca + hero.forca/2)
        hero.level = round(hero.level*2)

        string = f'''

Seus status agora são:

{hero.forca} de forca
{hero.level} de level
{hero.vida} de vida

        '''

        funcoes.digitar_historia(string)

        time.sleep(4)

        os.system('clear')
    

    elif opcao2 == 2:

        string = '''

Você decide ignorar os gnomos e seguir viagem.

'''
        funcoes.digitar_historia(string)

        time.sleep(3)

elif opcao == 2:

    string = '''

Sentindo-se culpado por ver o pobre garoto pobre morrendo e nao fazer absolutamente nada,
você segue sua jornada com essa contradição de herói martelando sua cabeça, caminhando próximo
a um riacho para abastecer seu cantil, você encontra uma criatura meio humana meio peixe e ao
se aproximar você nota que ela é uma sereia, e acaba sendo atraído por sua beleza e seu canto
cuja voz beira o angelical, a sereia nota sua presença juntamente ao fato de que você está
enfrentando um decisivo dilema e decide lhe ajudar a sanar suas preocupações, e garantiu que 
isso iria incrementar sua experiência de vida e apaziguar suas contradições, diante de tal
proposta você se sente um pouco receioso, o que decide fazer ?

[1]Decide deixá-la ajudar
[2]Não confiar na suposta sereia

    '''
    funcoes.digitar_historia(string)

    opcao2 = int(input())

    if opcao2 == 1:

        string = '''

Você decide deixar a sereia ajudá-lo, ela demonstra gratidão pelo voto de confiança, com isso
ela clareia sua mente avisando-o sobre o possível futuro caso você ajudasse o garoto, o qual 
você receberia um ataque furtivo e teria seus pertences roubados, além disso ela lhe concede 
a bênção dos mares, aumentando sua força e sabedoria em 100%, e ela decide lhe seguir sempre 
que estiveres próximo a um rio ou ao mar lhe concedendo sua vida em adição à sua jornada.

        '''
        time.sleep(5)

        os.system('clear')
        
        funcoes.digitar_historia(string)


        hero.forca = round(hero.forca*2)
        hero.level = round(hero.level*2)
        hero.vida = round(hero.vida*2)

        string = f'''
        
Seus status agora são:

{hero.forca} de forca
{hero.level} de level
{hero.vida} de vida

        '''

        funcoes.digitar_historia(string)

        time.sleep(3)

        os.system('clear')

    elif opcao2 == 2:

        string = '''
"você decidiu ignorar a sereia,sentindo-se ofendida por sua escolha ela lança uma maldição
em você, diminuindo sua vida parcialmente.
        
        '''

        funcoes.digitar_historia(string)

        hero.vida = round(hero.vida - hero.vida/4)

        string = f'''
        
Seus status agora são:

{hero.forca} de forca
{hero.level} de level
{hero.vida} de vida

        '''

        funcoes.digitar_historia(string)

        time.sleep(4)

        os.system('clear')


string = '''
Após andar por mais alguns dias, você finalmente sai da floresta, e se depara com um enorme deserto cheio de grandiosas
dunas de areia, ali você percebe que chegou no deserto de Mauruler, um antigo deserto cheio de mistérios em sua história.
Muitas lendas dizem que antigamente esse deserto era um oásis, e era uma terra governada por uma poderosa família 
durante gerações, até que um de seus reis decidiu mexer com a magia da vida, com a ganância de se tornar imortal,
isso irritou a entidade divina da terra, cuja mesma lançou uma maldição de infertilidade, transformando aquela terra
rica e fértil em um deserto que apenas florecem memórias.
'''

funcoes.digitar_historia(string)

time.sleep(4)

os.system('clear')

string = '''

Você avista uma estrutura estranha, cheia de escrituras e com uma entrada com a seguinte mensagem : 
"Aqui jás o grandioso rei Beonath, que viveu toda a vida de sua terra, apenas os que em vida não
desejam nada podem entrar, pois quem deseja mais do que a vida acaba por perdê-la".
O que você decide fazer ?

[1]Entrar na possível tumba
[2]Seguir viagem e não assumir o risco


'''

funcoes.digitar_historia(string)

opcao = int(input())

os.system('clear')

if opcao == 1:
    string = '''
Você entrou na tumba do rei Beonath, tome cuidado aventureiro, pois em vida esse rei desprezou a tudo e
a todos em prol de sua ganância, ele não terá piedade de quem tentar tirar algo dele, mesmo após sua morte.

Andando dentro daquela grandiosa estrutura, você encontra uma bifurcação, e deve escolher entre seguir pela
esquerda ou direita, porém na parede você encontra a seguinte mensagem:

"aos corajosos e fortes o braço direito não lhe falha, aos bondosos e benevolentes a mão esquerda
da cura os protege"

Qual caminho você decide seguir?

[1]Esquerda
[2]Direita

'''
    funcoes.digitar_historia(string)

    opcao2 = int(input())
    
    if opcao2 == 1:

        string = '''
Você pegou o caminho da bondade, nele você chega ao final de um corredor e encontra o segredo da vida
o qual o rei Beonath guardou consigo até mesmo após sua morte, e você é concedido com 200 a mais de vida
'''
        funcoes.digitar_historia(string)

        time.sleep(3)

        os.system('clear')

        hero.vida = hero.vida + 200

        string = f'''
        
Seus status agora são:

{hero.forca} de forca
{hero.level} de level
{hero.vida} de vida

        '''

        funcoes.digitar_historia(string)

        time.sleep(3)

        os.system('clear')

    elif opcao2 == 2:

        string = '''
Você pegou o caminho da coragem e força, chegando ao final de um corredor você se depara com uma belíssima
espada, tão linda que deixaria um mortal com pouca força de vontade cair pelo desejo insano em possuí-la.
Abaixo do suporte onde se encontra a espada, você lê a seguinte mensagem:

"a espada de Beonath, o encontro entre a vida e a morte, aqueles que conseguem possuí-la terão o maior poder
já visto em seu reino, mas aqueles que não são dignos de empunhá-la não sairão daqui.

Diante desta situação, o que você decide fazer ?

[1]Arriscar e pegar a espada, confiando em ser digno
[2]Ignorar a espada e não assiscar

'''
        funcoes.digitar_historia(string)

        opcao3 = int(input())

        if opcao3 == 1:

            chance = random.random()*10

            if chance >= 5:

                string = '''
Você foi testado digno nobre aventureiro, e foi capaz de empunhar a espada de Beonath, 
garantindo-lhe o grandioso poder uma vez empunhado pelo Rei das areias.                
'''
                funcoes.digitar_historia(string)

                hero.forca = hero.forca + 100

                string = f'''
        
Seus status agora são:

{hero.forca} de forca
{hero.level} de level
{hero.vida} de vida

        '''

                funcoes.digitar_historia(string)

                time.sleep(4)

                os.system('clear')

            else:

                string = '''
Você não foi digno de empunhar a espada nobre aventureiro, e como punição você perdeu metade
da sua quantidade atual de vida.
                '''

                funcoes.digitar_historia(string)

                time.sleep(3)

                os.system('clear')

                hero.vida = hero.vida/2

                string = f'''
        
Seus status agora são:

{hero.forca} de forca
{hero.level} de level
{hero.vida} de vida

        '''

                funcoes.digitar_historia(string)

                time.sleep(4)

                os.system('clear')




















