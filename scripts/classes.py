
class Movies: 

      def __init__(self, titulo, autor, ano, genero):
          self.titulo = titulo
          self_autor = autor
          self.ano = ano
          self.genero = genero

      assistido = 'Pendente'     
      favorito = False

      def assistir(self):  #Setter
          self.assistido = 'Assistindo'

      def favoritar(self): #Setter
          self.favotito = True    

      def listar(self):     #Getter
          return[
          self.titulo,
          self._autor,
          self.ano,
          self.assistido,
          self.favorito       
          ]

       #def jsonificar(self):
           return {
               'titulo':self.titulo,
               'autor':self.autor,
               'ano':self.ano,
               'genero':self.genero,
               'assistido':self.assistir.upper()
               'favorito':self.favorito
                  }   
        @property #Decorador
        def status(self):   #Getter
            return self.__assistido      