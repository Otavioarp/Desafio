'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def retorna_tempo_minimo_em_minutos(p,s,n):
    import math
    return  math.ceil(math.ceil(p / n) * s /60)