import classes

batman = classes.Movies('Batman, Cavaleiro das trevas' , 'cristopher nolan' ,'2008', 'acão, suspence')

print(batman.listar(), sep='\n')

batman.assistir()
batman.favoritar()

print(batman.jsonificar(), sep='\n')
print(batman.assistido)