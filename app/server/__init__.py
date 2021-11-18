from inspect import Arguments
from typing import Tuple, Any
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from server.domains.pokemon.routes import router as PokemonRouter

from server.domains.pokemon.actions import retrieve_pokemons


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(PokemonRouter, tags=["Pokemon"], prefix="/pokemon")





# CONSTANT
LOGIN = []


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("menu_escolha.html",
                                      {"request": request, "login": None})


@app.route('/login')
def login(request: Request):
    print('Sem validação de Admin')
    if LOGIN:
        return templates.TemplateResponse('menu_admin.html', 
                                          {"request": request})
    else:
        return templates.TemplateResponse('login.html', 
                                          {"request": request})


@app.get('/login/{username}')
async def login(request: Request, username: str) -> Tuple[Any, int]:
    print(username)

    # user_login: Dict = {"username": username, "password": password}
    # print(user_login)
    # bool_login = login_admin(user_login)
    # print(bool_login)
    # if LOGIN:
    return templates.TemplateResponse('menu_admin.html', 
                                      {"request": request})
    # else:
    #     return templates.TemplateResponse('login.html', 
    #                                       {"request": request})


@app.route('/menuadminpokemon')
def menu_admin_pokemon(request: Request):
    if not LOGIN:
        return RedirectResponse('/menuadmin')
    lista_dados = retrieve_pokemons()
    lista = []
    for dados in lista_dados:
        lista.append(dados.list())

    return templates.TemplateResponse('menu_admin_pokemon.html', 
                                      {"request": request, "lista": lista})


@app.route('/menuadmin/adicionarpokemon')
def adicionar_pokemon(request: Request):
    if not LOGIN:
        return RedirectResponse('/menuadminpokemon')
    return templates.TemplateResponse('pokemon_admin_dados.html', 
                                      {"request": request})


@app.route('/menuadminpokemon/editarpokemon')
def editar_pokemon(request: Request):
    if not LOGIN:
        return RedirectResponse('/menuadminpokemon')
    id = request.args['id']
    print(id)
    return templates.TemplateResponse('pokemon_admin_dados.html', 
                                      {"request": request})


@app.route('/sair')
def sair_admin():
    # busca a variavel global para modificar
    global LOGIN
    LOGIN = []
    return RedirectResponse('/')


@app.route('/menupokemon')
async def listar_todos_pokemon(request: Request):
    lista_dados = await retrieve_pokemons()
    lista = []
    for dados in lista_dados:
        lista.append(list(dados.values()))
    return templates.TemplateResponse('Listar_todos_pokemons.html', 
                                      {"request": request, "lista": lista})


