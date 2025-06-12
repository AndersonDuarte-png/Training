
resultados = []
velocidadeFinalGrupo = 0

def LesmaVeloz(velocidade):
    if int(velocidade) < 10:
        return 1
    elif int(velocidade) >= 10 and int(velocidade) < 20 :
        return 2
    else:
        return 3

while True:
    try:
        QuantLesmaGrupo = input()
        entrada = input()
        VelocidadeQuantLesmaGrupo = entrada.split()



        for x in VelocidadeQuantLesmaGrupo:
            Velocidade = LesmaVeloz(x)


            if Velocidade > velocidadeFinalGrupo:
                velocidadeFinalGrupo = Velocidade


        resultados.append(velocidadeFinalGrupo)
        VelocidadeQuantLesmaGrupo = 0
        velocidadeFinalGrupo = 0

    except EOFError:
        for x in resultados:
            print(x)
        break