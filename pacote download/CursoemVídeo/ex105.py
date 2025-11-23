def notas(*nota, situacao=False):
    ficha=dict()
    ficha['total']=len(nota)
    ficha['maior']=max(nota)
    ficha['menor']=min(nota)
    ficha['media']=sum(nota)/len(nota)
    if situacao:
        if ficha['media']>=7:
            ficha['situacao']='BOA'
        elif ficha['media']>=5:
            ficha['situacao']='Razoável'
        else:
            ficha['situacao']='RUIM'
    return ficha


resposta_de_notas=notas(5.5,2.5,1.5,9, situacao=True)
print(resposta_de_notas)