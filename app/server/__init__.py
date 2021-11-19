from typing import Optional, Dict

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from server.domains.pokemon.routes import router as PokemonRouter
from server.domains.pokemon.actions import retrieve_pokemons, delete_pokemon
from server.domains.services.actions import login_admin


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(PokemonRouter, tags=["Pokemon"], prefix="/pokemon")





# CONSTANT
LOGIN: Dict = {"username": None,
               "password": None,
               "is_valid": None}


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("menu_escolha.html",
                                      {"request": request, "login": None})


@app.route('/login')
async def login(request: Request):
    if LOGIN.get("is_valid"):
        return templates.TemplateResponse("menu_admin.html", 
                                        {"request": request})
    else:
        return templates.TemplateResponse("login.html", 
                                        {"request": request})


@app.get('/login/credentials/')
async def login_credentials(username: Optional[str] = None, password: Optional[str] = None):
    LOGIN["username"] = username
    LOGIN["password"] = password
    LOGIN["is_valid"] = login_admin(LOGIN)

    return RedirectResponse('/login')
    

@app.route('/menuadminpokemon')
async def menu_admin_pokemon(request: Request):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/login')
    lista_dados = await retrieve_pokemons()
    lista = []
    for dados in lista_dados:
        lista.append(list(dados.values()))

    return templates.TemplateResponse('menu_admin_pokemon.html', 
                                      {"request": request, "lista": lista})


@app.get('/menuadminpokemon/excluirpokemon')
async def excluir_pokemon(id: Optional[str] = None):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/login')
    pokemon = await delete_pokemon(id)
    print(pokemon)

    return RedirectResponse('/menuadminpokemon')


@app.route('/menuadmin/adicionarpokemon')
def adicionar_pokemon(request: Request):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/menuadminpokemon')
    return templates.TemplateResponse('pokemon_admin_dados.html', 
                                      {"request": request})


@app.route('/menuadminpokemon/editarpokemon')
def editar_pokemon(request: Request):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/menuadminpokemon')
    return templates.TemplateResponse('pokemon_admin_dados.html', 
                                      {"request": request})


@app.get('/sair')
def sair_admin():
    # busca a variavel global para modificar
    LOGIN["username"] = None
    LOGIN["password"] = None
    LOGIN["is_valid"] = None
    return RedirectResponse('/')


@app.route('/menupokemon')
async def listar_todos_pokemon(request: Request):
    lista_dados = await retrieve_pokemons()
    lista = []
    for dados in lista_dados:
        lista.append(list(dados.values()))
    return templates.TemplateResponse('Listar_todos_pokemons.html', 
                                      {"request": request, "lista": lista})


