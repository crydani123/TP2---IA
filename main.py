import copy
from operator import attrgetter

global objeto
objeto = [[1,2,3],[4,5,6],[7,8,0]]

class grafo:
  def __init__(self, infraiz):
    self.raiz = aresta(infraiz)
    global ultimos
    ultimos = []
  def geraultimos(self):
    ultimos = []
    self.raiz.percorre()

class aresta:
  def __init__(self,inf):
    self.estado = inf
    self.prox = []

  def novoprox (self,inf):
    self.prox.append(aresta(inf))

  def imprime(self):
    print(self.estado)
    for x in self.prox:
      x.imprime()

  def percorre(self):
    for x in self.prox:
      x.percorre()
    if self.prox == []:
      ultimos.append(self)
    return

class fila:
  lista = []
  global objeto
  def __init__(self, item, prioridade, caminho):
    self.item = item
    self.prioridade = prioridade
    if caminho:
      self.caminho = copy.deepcopy(caminho)
    else:
      self.caminho = []
    self.caminho.append(item.estado)
    fila.lista.append(self)
    fila.lista.sort(key=attrgetter('prioridade') ,reverse=True)

  def prox(self):
    try:
      return fila.lista.pop()
    except:
      return False

def popula():
  mat = [[9,9,9],[9,9,9],[9,9,9]]
  for x in range(3):
    for y in range(3):
      mat[x][y] = int(input("Digite os números do jogo de 0 a 8 sem repetir "))
  
  return(mat)

def geraprox(matriz):
  
  matlist = []
  varx = -1
  vary = -1
  for x in range(3):
    for y in range(3):
      if (matriz[x][y] == 0):
        varx = x
        vary = y

  x = varx
  y = vary


  if x != 0:
    mattemp = copy.deepcopy(matriz) 
    valor = matriz[x-1][y]
    mattemp[x][y] = valor
    mattemp[x-1][y] =0
    matlist.append(mattemp)

  if y != 0:
    mattemp = copy.deepcopy(matriz) 
    valor = matriz[x][y-1]
    mattemp[x][y] = valor
    mattemp[x][y-1] = 0
    matlist.append(mattemp)

  if x != 2:
    mattemp = copy.deepcopy(matriz) 
    valor = matriz[x+1][y]
    mattemp[x][y] = valor
    mattemp[x+1][y] =0
    matlist.append(mattemp)

  if y != 2:
    mattemp = copy.deepcopy(matriz) 
    valor = matriz[x][y+1]
    mattemp[x][y] = valor
    mattemp[x][y+1] =0
    matlist.append(mattemp)
  
  return(matlist)

def adiciona (opcoes, nodo, arv):
  
  def buscalocal(item, nodo):
    res = False
    if nodo.estado == item:
      return True
    if nodo.prox != []:
      for x in nodo.prox:
        res = buscalocal(item,x)
      return res

  for x in opcoes:
    if not buscalocal(x,arv.raiz):
      nodo.novoprox(x)
  return

def buscaL(pilha):
  global contagem
  global objeto
  contagem += 1
  pilhab = []
  try:
    for x in pilha:
      if x.estado == objeto:
        return True
      pilhab.extend(x.prox)
  except:
    pilhab = pilha.prox

  if pilhab != []:
    return buscaL(pilhab)
  return False

def buscaP(nodo):
  global caminho
  global contagem
  global objeto
  contagem += 1
  res = False
  if nodo.estado == objeto:
    caminho.append(nodo.estado)
    return True
  if nodo.prox != []:
    for x in nodo.prox:
      res = buscaP(x)
      if res:
        caminho.append(nodo.estado)
        return res
  if res:
    caminho.append(nodo.estado)
  return res

def buscaG(raiz):
  global objeto
  global contagem
  global caminho
  res =False

  def prioridade (estado):
    global objeto
    a = 0
    for i in range(3):
      for j in range (3):
        if estado[i][j] != objeto [i][j]:
          a +=1
    return a

  def recursivo(f):
    global caminho
    global objeto
    global contagem
    contagem +=1
    obj = f.prox()
    if obj:
      if obj.item.estado == objeto:
        caminho = obj.caminho
        return True

      for x in obj.item.prox:
        fila(x,prioridade(x.estado),obj.caminho)
      
      return recursivo(f)
    return(False)

  
  obj = fila(raiz,prioridade(raiz.estado),False)

  res = recursivo(obj)
  
  return res

def buscaA(raiz):
  global objeto
  global contagem
  global caminho
  res =False

  def prioridade (estado):
    objet = [1,2,3,4,5,6,7,8,0]
    pontuação = 0
    vval=0
    hval=0

    for x in objet:
      if x>6 or x==0:
        vval=2
      elif x>3:
        vval=1
      else:
        vval=0
      if x==1 or x==4 or x==0:
        hval=0
      elif x==2 or x==5 or x==7:
        hval=1
      else:
        hval=2

      for y in range(3):
        for z in range(3):
          if estado[y][z] == x:
            pontuação =+abs(y-hval)
            pontuação =+abs(z-vval)


    return pontuação
      
  def recursivo(f):
    global caminho
    global objeto
    global contagem
    contagem +=1
    obj = f.prox()
    if obj:
      if obj.item.estado == objeto:
        caminho = obj.caminho
        return True

      for x in obj.item.prox:
        fila(x,prioridade(x.estado),obj.caminho)
    
      return recursivo(f)
    
    return False

  
  obj = fila(raiz,prioridade(raiz.estado),False)

  res = recursivo(obj)
  
  return res

def imprimebonito (caminho):
  global objeto
  obj = []
  for x in objeto:
    obj.extend(x)
  for x in caminho:
    lugar = 0
    
    for i in range(3):
      for j in range(3):
        if x[i][j] == objeto [i][j]:
          lugar +=1

    for y in x:
      print(y)
    print("-----------",9-lugar," nós fora do lugar")
  
#main 
global caminho
global contagem
resultado = False
contagem = 0
caminho =[]

#mat = popula()
mat = [[1,0,3],[5,2,6],[4,7,8]]

matlist = geraprox(mat)
tree = grafo(mat)
adiciona(geraprox(tree.raiz.estado),tree.raiz,tree)

while not resultado:
  tree.geraultimos()
  for x in ultimos:
    adiciona(geraprox(x.estado),x,tree)
  #if buscaP(tree.raiz):
  #if buscaL(tree.raiz):
  #if buscaG(tree.raiz):
  #if buscaA(tree.raiz):
    resultado = True


if resultado:
  print("achei procurando em ", contagem, " nodos")
else:
  print("não encontrado")

reversed(caminho)
imprimebonito(caminho)