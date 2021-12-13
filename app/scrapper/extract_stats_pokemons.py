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

    def status_pokemon(self):
        """Obtendo status de HP, Attack, Defense, Special_Attack, Special_Defense, Speed
     do Pokemon atraves da tag type do html"""
        list_status = list()
        list_num = list()
        status_soup = self.soup.find_all('ul', {"class", "gauge"})

        status_soup = str(status_soup).split('data-value="')
        for i in status_soup:
            stats = i.split('"></l')
            list_status.append(stats)

        for i in range(0, 7):
            list_num.append(list_status[i][0])

        list_num.pop(0)

        return list_num

    def save_data(self, dados_pokemon):
        # -- salvando dados obtidos para Database
        with open('data_save/status_pokemons.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(';'.join(dados_pokemon) + '\n')

    def main(self):
        """Atraves dos dados obtidos podemos mostra-los na tela por ordem,
        Assim refazemos o processo em todas as paginas que contem dados e
        salvamos em um txt"""

        # -- Loop de requests para obter dados das paginas necessarias
        for j in range(1, 810):
            self.request(j)

            status = self.status_pokemon()

            self.save_data(status)

            # -- Exibindo na tela valores obtidos
            print(f'-----Pokemon Code: {j}-----')
            print('Status:', status)
            print(f'----------------------------')


if __name__ == "__main__":
    pokedex = DataPokemons()
    pokedex.main()
