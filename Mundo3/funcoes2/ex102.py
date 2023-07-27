def fatorial(num, show=False):
  """
  --> Calculo de Fatorial:
  :param num: Número que se deseja calcular o fatorial
  :param show: Multiplicações para obtenção do fatorial
  :return: Retorna o fatorial
  """
  f = 1
  for c in range(num, 0, -1):
    if show:
      print(c, end='')
      if c > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f
print(fatorial(5, show=True))
help(fatorial)
