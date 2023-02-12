#Chamada do arquivo de entrada (dados)
file=input('Digite o nome do arquivo: ')
#Abertura do arquivo de entrada em formato de leitura
fin=open(file,'r')
#Leitura das linhas do arquivo
dados=fin.readlines()
#Criação de listas para: pontos, valor de cota e distância entra cada ponto
ptcotas=[]
vlcotas=[]
dtcotas=[]
#Definindo colunas
for i in range(1,12):
    pt=dados[i].split(',')[0]
    ptcotas.append(pt)
    vl=dados[i].split(',')[1]
    vlcotas.append(float(vl))
    dt=dados[i].split(',')[2]
    dtcotas.append(float(dt))
#Importando bibliotecas
import matplotlib.pyplot as plt
import math
#Definindo a distância horizontal padrão entre os pontos
x=100
#Definindo ângulos entre os pontos
a=(int(vlcotas[1])-int(vlcotas[0]))/x
ab=math.degrees(math.atan(a)) #ângulo do ponto 1 ao 2
b=(int(vlcotas[2])-int(vlcotas[1]))/x
bc=math.degrees(math.atan(b)) #ângulo do ponto 2 ao 3
c=(int(vlcotas[3])-int(vlcotas[2]))/x
cd=math.degrees(math.atan(c)) #ângulo do ponto 3 ao 4
d=(int(vlcotas[4])-int(vlcotas[3]))/x
de=math.degrees(math.atan(d)) #ângulo do ponto 4 ao 5
e=(int(vlcotas[5])-int(vlcotas[4]))/x
ef=math.degrees(math.atan(e)) #ângulo do ponto 5 ao 6
f=(int(vlcotas[6])-int(vlcotas[5]))/x
fg=math.degrees(math.atan(f)) #ângulo do ponto 6 ao 7
g=(int(vlcotas[7])-int(vlcotas[6]))/x
gh=math.degrees(math.atan(g)) #ângulo do ponto 7 ao 8
h=(int(vlcotas[8])-int(vlcotas[7]))/x
hi=math.degrees(math.atan(h)) #ângulo do ponto 8 ao 9
i=(int(vlcotas[9])-int(vlcotas[8]))/x
ij=math.degrees(math.atan(i)) #ângulo do ponto 9 ao 10
j=(int(vlcotas[10])-int(vlcotas[9]))/x
jk=math.degrees(math.atan(j)) #ângulo do ponto 10 ao 11
#Criando lista com os valores dos ângulos 
angulos=[ab, bc, cd, de, ef, fg, gh, hi, ij, jk]

#Criando gráfico para os valores iniciais das cotas
plt.figure(1)
plt.subplot(1,1,1)
plt.plot(dtcotas, vlcotas, 'ko-')
plt.xlabel('Distância (m)')
plt.ylabel('Valor de cota (m)')
plt.show()

#Tomada de decisão
DES=int(input(' Para obter os valores das cotas com a distância entres os pontos referenciada ao eixo horizontal, digite 1; \n Para obter os valores das cota com a distância entre os pontos referenciada a superfície topográfica, digite 2; \n Digite qualquer outro valor para encerrar o programa: ' ))
#Valores de cotas com a distância entres os pontos referenciada na horizontal
if (DES==1):
    rd=int(input(' Para obter os valores das cotas com uma distância de 20 metros, digite 1; \n Para obter os valores das cotas com uma distância de 25 metros, digite 2; \n Para obter os valores das cotas com uma distância de 50 metros, digite 3: '))
   #Criando valores de cotas para a distância de 20 metros
    if (rd==1):
        anv=(math.tan(math.radians(ab)))*(20)+int(vlcotas[0])
        bnv=(math.tan(math.radians(ab)))*(20)+int(anv)
        cnv=(math.tan(math.radians(ab)))*(20)+int(bnv)
        dnv=(math.tan(math.radians(ab)))*(20)+int(cnv)
        fnv=(math.tan(math.radians(bc)))*(20)+int(vlcotas[1])
        gnv=(math.tan(math.radians(bc)))*(20)+int(fnv)
        hnv=(math.tan(math.radians(bc)))*(20)+int(gnv)
        inv=(math.tan(math.radians(bc)))*(20)+int(hnv)
        knv=(math.tan(math.radians(cd)))*((-20)*(-1))+int(vlcotas[2])
        lnv=(math.tan(math.radians(cd)))*((-20)*(-1))+int(knv)
        mnv=(math.tan(math.radians(cd)))*((-20)*(-1))+int(lnv)
        nnv=(math.tan(math.radians(cd)))*((-20)*(-1))+int(mnv)
        pnv=(math.tan(math.radians(de)))*(20)+int(vlcotas[3])
        qnv=(math.tan(math.radians(de)))*(20)+int(pnv)
        rnv=(math.tan(math.radians(de)))*(20)+int(qnv)
        snv=(math.tan(math.radians(de)))*(20)+int(rnv)
        unv=(math.tan(math.radians(ef)))*((-20)*(-1))+int(vlcotas[4])
        vnv=(math.tan(math.radians(ef)))*((-20)*(-1))+int(unv)
        wnv=(math.tan(math.radians(ef)))*((-20)*(-1))+int(vnv)
        xnv=(math.tan(math.radians(ef)))*((-20)*(-1))+int(wnv)
        znv=(math.tan(math.radians(fg)))*(20)+int(vlcotas[5])
        aan=(math.tan(math.radians(fg)))*(20)+int(znv)
        bbn=(math.tan(math.radians(fg)))*(20)+int(aan)
        ccn=(math.tan(math.radians(fg)))*(20)+int(bbn)
        een=(math.tan(math.radians(gh)))*(20)+int(vlcotas[6])
        ffn=(math.tan(math.radians(gh)))*(20)+int(een)
        ggn=(math.tan(math.radians(gh)))*(20)+int(ffn)
        hhn=(math.tan(math.radians(gh)))*(20)+int(ggn)
        jjn=(math.tan(math.radians(hi)))*(20)+int(vlcotas[7])
        kkn=(math.tan(math.radians(hi)))*(20)+int(jjn)
        lln=(math.tan(math.radians(hi)))*(20)+int(kkn)
        mmn=(math.tan(math.radians(hi)))*(20)+int(lln)
        oon=(math.tan(math.radians(ij)))*((-20)*(-1))+int(vlcotas[8])
        ppn=(math.tan(math.radians(ij)))*((-20)*(-1))+int(oon)
        qqn=(math.tan(math.radians(ij)))*((-20)*(-1))+int(ppn)
        rrn=(math.tan(math.radians(ij)))*((-20)*(-1))+int(qqn)
        ttn=(math.tan(math.radians(jk)))*(20)+int(vlcotas[9])
        uun=(math.tan(math.radians(jk)))*(20)+int(ttn)
        vvn=(math.tan(math.radians(jk)))*(20)+int(uun)
        wwn=(math.tan(math.radians(jk)))*(20)+int(vvn)
        #Criando lista para os novos valores das cotas
        nvcotas=[ anv, bnv, cnv, dnv, fnv, gnv, hnv, inv, knv, lnv, mnv, nnv, pnv, qnv, rnv, snv, unv, vnv, wnv, xnv, znv, aan, bbn, ccn, een, ffn, ggn, hhn, jjn, kkn, lln, mmn, oon, ppn, qqn, rrn, ttn, uun, vvn, wwn]
        #Novos valores de distância (20)
        #Criando lista para as novas distâncias
        nvdist=[20, 40, 60, 80, 120, 140, 160, 180, 220, 240, 260, 280, 320, 340, 360, 380, 420, 440, 460, 480, 520, 540, 560, 580, 620, 640, 660, 680, 720, 740, 760, 780, 820, 840, 860, 880, 920, 940, 960, 980]
        #Recria o primeiro gráfico com as novas cotas em cima
        plt.subplot(1,1,1)
        plt.plot(dtcotas, vlcotas, 'ko-')
        plt.plot(nvdist, nvcotas, 'ro')
        plt.xlabel('Distância (m)')
        plt.ylabel('Valor de cota (m)')
        plt.show()
   #Criando valores de cotas para a distância de 25 metros
    if(rd==2):
        anv=(math.tan(math.radians(ab)))*(25)+int(vlcotas[0])
        bnv=(math.tan(math.radians(ab)))*(25)+int(anv)
        cnv=(math.tan(math.radians(ab)))*(25)+int(bnv)
        env=(math.tan(math.radians(bc)))*(25)+int((vlcotas[1]))
        fnv=(math.tan(math.radians(bc)))*(25)+int(env)
        gnv=(math.tan(math.radians(bc)))*(25)+int(fnv)
        inv=(math.tan(math.radians(cd)))*((-25)*(-1))+int(vlcotas[2])
        jnv=(math.tan(math.radians(cd)))*((-25)*(-1))+int(inv)
        knv=(math.tan(math.radians(cd)))*((-25)*(-1))+int(jnv)
        mnv=(math.tan(math.radians(de)))*(25)+int(vlcotas[3])
        nnv=(math.tan(math.radians(de)))*(25)+int(mnv)
        onv=(math.tan(math.radians(de)))*(25)+int(nnv)
        qnv=(math.tan(math.radians(ef)))*((-25)*(-1))+int(vlcotas[4])
        rnv=(math.tan(math.radians(ef)))*((-25)*(-1))+int(qnv)
        snv=(math.tan(math.radians(ef)))*((-25)*(-1))+int(rnv)
        unv=(math.tan(math.radians(fg)))*(25)+int(vlcotas[5])
        vnv=(math.tan(math.radians(fg)))*(25)+int(unv)
        wnv=(math.tan(math.radians(fg)))*(25)+int(vnv)
        ynv=(math.tan(math.radians(gh)))*(25)+int(vlcotas[6])
        znv=(math.tan(math.radians(gh)))*(25)+int(ynv)
        aan=(math.tan(math.radians(gh)))*(25)+int(znv)
        ccn=(math.tan(math.radians(hi)))*(25)+int(vlcotas[7])
        ddn=(math.tan(math.radians(hi)))*(25)+int(ccn)
        een=(math.tan(math.radians(hi)))*(25)+int(ddn)
        ggn=(math.tan(math.radians(ij)))*((-25)*(-1))+int(vlcotas[8])
        hhn=(math.tan(math.radians(ij)))*((-25)*(-1))+int(ggn)
        iin=(math.tan(math.radians(ij)))*((-25)*(-1))+int(hhn)
        kkn=(math.tan(math.radians(jk)))*(25)+int(vlcotas[9])
        lln=(math.tan(math.radians(jk)))*(25)+int(kkn)
        mmn=(math.tan(math.radians(jk)))*(25)+int(lln)
        #Criando lista para os novos valores de cotas
        nvcotas=[ anv, bnv, cnv, env, fnv, gnv, inv, jnv, knv, mnv, nnv, onv, qnv, rnv, snv, unv, vnv, wnv, ynv, znv, aan, ccn, ddn, een, ggn, hhn, iin, kkn, lln, mmn]
        #Novos valores de distância (25)
        #Criando lista para novas distâncias
        nvdist=[25, 50, 75, 125, 150, 175, 225, 250, 275, 325, 350, 375, 425, 450, 475, 525, 550, 575, 625, 650, 675, 725, 750, 775, 825, 850, 875, 925, 950, 975]
        #Recria o primeiro gráfico com as novas cotas em cima
        plt.subplot(1,1,1)
        plt.plot(dtcotas, vlcotas, 'ko-')
        plt.plot(nvdist, nvcotas, 'ro')
        plt.xlabel('Distância (m)')
        plt.ylabel('Valor de cota (m)')
        plt.show()
    #Criando valores de cotas para distância de 50 metros
    if(rd==3):
        anv=(math.tan(math.radians(ab)))*(50)+int(vlcotas[0])
        bnv=(math.tan(math.radians(bc)))*(50)+int((vlcotas[1]))
        cnv=(math.tan(math.radians(cd)))*((-50)*(-1))+int(vlcotas[2])
        dnv=(math.tan(math.radians(de)))*(50)+int(vlcotas[3])
        env=(math.tan(math.radians(ef)))*((-50)*(-1))+int(vlcotas[4])
        fnv=(math.tan(math.radians(fg)))*(50)+int(vlcotas[5])
        gnv=(math.tan(math.radians(gh)))*(50)+int(vlcotas[6])
        hnv=(math.tan(math.radians(hi)))*(50)+int(vlcotas[7])
        inv=(math.tan(math.radians(ij)))*((-50)*(-1))+int(vlcotas[8])
        jnv=(math.tan(math.radians(jk)))*(50)+int(vlcotas[9])
        #Criando lista para os novos valores de cotas
        nvcotas=[anv, bnv, cnv, dnv, env, fnv, gnv, hnv, inv, jnv]
        #Novos valores de distância
        #Criando lista para novas distâncias
        nvdist= [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
        #Recria o primeiro gráfico com as novas cotas em cima
        plt.subplot(1,1,1)
        plt.plot(dtcotas, vlcotas, 'ko-')
        plt.plot(nvdist, nvcotas, 'ro')
        plt.xlabel('Distância (m)')
        plt.ylabel('Valor de cota (m)')
        plt.show()
#Valores de cotas com a distância entre os pontos referenciada com a superfície topográfica
if(DES==2):
    print(' \n Não é possível realizar esse cálculo.')
#Para encerrar o programa
if(DES!=1 and DES!=2):
    print(' \n Programa encerrado.')