aluno = ("Vinicius" ,23, 10)

print("Nome ",aluno[0])
print("Idade ",aluno[1])
print("Nota ",aluno[2])


print("Digite a nota", aluno[2])

notaespec = 10
if notaespec in aluno:
    print(f"A nota {notaespec} estar presente na tupla")
else: print(f"A nota {notaespec} nao esta presente")