'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def tamanho_setor_busca(areamaior,areamenor):
  x = (areamaior-areamenor)/8
  return str(int(x)) if x - int(x) <= 1e-6 else str(x)