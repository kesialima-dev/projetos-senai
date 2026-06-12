def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_aluno(media):
    if media >= 7: return "Aprovado"
    elif media >= 5: return "Recuperação"
    else:            return "Reprovado"

def relatorio_aluno(nome, notas):
    media = calcular_media(notas)   #chama a 1 função
    status = situacao_aluno(media)   #chama a 2 função)
    print(f"{nome}: media {media:.1f} → {status} ")

    #usuando as funçoes juntas:
    relatorio_aluno("Lucas", [8, 7, 9])  # Lucas: média 8.0 → Aprovado
    relatorio_aluno("Beatriz", [5, 6, 4])  # Beatriz: média 5.0 → Recuperação
    relatorio_aluno("Carlos", [3, 2, 4]) # Carlos: média 3.0 → Reprovado
    
                    




