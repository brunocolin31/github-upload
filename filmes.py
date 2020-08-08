ListaDeDesejosDeFilmes = []
for filmeAtual  in range(6):
    ListaDeDesejosDeFilmes.append(input("Quais os filmes que você quer assistir?"))

for filmeAtual in range(len(ListaDeDesejosDeFilmes)):
    print(ListaDeDesejosDeFilmes[filmeAtual],'',filmeAtual)