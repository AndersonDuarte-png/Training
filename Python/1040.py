N1,N2,N3,N4= map(float, input().split())
media = (N1*2)/10 + (N2*3)/10 + (N3*4)/10 + (N4*1)/10
Majuste = str(media)
media= float(Majuste[0:3])

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media <5:
    print("Aluno reprovado.")
elif media>5 and media<6.9:
    print("Aluno em exame.")

    NExame = float(input())
    print(f"Nota do exame: {NExame:.1f}")

    media = (media + NExame)/2

    if media >5.0:
        print("Aluno aprovado.")
    elif media <4.9:
        print("Aluno reprovado.")
    
    print(f"Media final: {media:.1f}")