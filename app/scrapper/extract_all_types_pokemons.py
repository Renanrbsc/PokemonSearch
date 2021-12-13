import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

'''
# A biblioteca BeatifulSoup permite a construção de uma árvore
a partir de vários elementos de uma página HTML e fornece
uma simples interface para acessar estes elementos.
# A biblioteca requests é para realizar pedidos HTTP.
'''


class DataPokemons:
    """Extração de dados pagina Pokedex Pokemon
    https://www.pokemon.com/br/pokedex
    -- Script criado para obter dados dos pokemons e
    -- montar um banco de dados atraves do mesmo"""

    def __init__(self):
        self.pag_html = ''
        self.soup = None

    def request(self, j):
        self.pag_html = requests.get(f"https://www.pokemon.com/br/pokedex/{j}").text

        self.soup = BeautifulSoup(self.pag_html, 'html.parser')

        # return f"{self.soup.prettify()}"
        return self.soup

    # -- defs utilizadas para se obter dados especificos das tags
    # -- Utilizado metodo de extração por tags que continham class=""

    def type_pokemon(self):
        """Obtendo Tipo do Pokemon atraves da tag type do html"""
        list_types = list()

        type_st = self.soup.find_all("div", "dtm-type")
        types = str(type_st).split('>')

        list_types.append(types[6].strip('</a'))

        if len(types) > 11:
            if types[10] != ', <div class="dtm-type"':
                list_types.append(types[10].strip('</a'))
            else:
                list_types.append('')
        else:
            list_types.append('')

        return list_types

    def save_data(self, dados_pokemon):
        # -- salvando dados obtidos para Database
        with open('data_save/types_pokemons.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(';'.join(dados_pokemon) + '\n')

    def main(self):
        """Atraves dos dados obtidos podemos mostra-los na tela por ordem,
        Assim refazemos o processo em todas as paginas que contem dados e
        salvamos em um txt"""

        # -- Loop de requests para obter dados das paginas necessarias
        for j in range(1, 810):
            self.request(j)

            types = self.type_pokemon()

            self.save_data(types)

            # -- Exibindo na tela valores obtidos
            print(f'-----Pokemon Code: {j}-----')
            for i in types:
                print(i)
            print(f'----------------------------')


if __name__ == "__main__":
    pokedex = DataPokemons()
    pokedex.main()
