entrada = input()
HoraInicial , HoraFim =  entrada.split()

if int(HoraInicial) > int(HoraFim):
    tempo = 24 - int(HoraInicial)
    tempo = tempo + int(HoraFim)
    print("O JOGO DUROU {} HORA(S)" .format(tempo) )
elif(int(HoraInicial) == int(HoraFim)):
    print("O JOGO DUROU 24 HORA(S)")
else:
    tempo  = int(HoraFim) - int(HoraInicial)
    print("O JOGO DUROU {} HORA(S)" .format(tempo) )