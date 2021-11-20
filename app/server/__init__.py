from typing import Optional, Dict

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from server.domains.pokemon.routes import router as PokemonRouter
from server.domains.pokemon.actions import retrieve_pokemons, delete_pokemon, update_pokemon
from server.domains.pokemon.routes import add_all_pokemon_data
from server.domains.services.actions import login_admin


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(PokemonRouter, tags=["Pokemon"], prefix="/pokemon")





# CONSTANT
LOGIN: Dict = {"username": None,
               "password": None,
               "is_valid": None}

ID_POKEMON: Dict = {"id": None}

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
    all_data = await retrieve_pokemons()
    list_data = []
    for data in all_data:
        list_data.append(list(data.values()))

    return templates.TemplateResponse('menu_admin_pokemon.html', 
                                      {"request": request, "list_data": list_data})






@app.get('/menuadminpokemon/deletepokemon')
async def admin_delete_pokemon(id: Optional[str] = None):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/login')
    pokemon = await delete_pokemon(id)
    print(pokemon)

    return RedirectResponse('/menuadminpokemon')



@app.get('/menuadminpokemon/updatepokemon/id/data/')
async def get_data_for_update_pokemon(name: Optional[str] = None, type: Optional[str] = None, 
height: Optional[str] = None, weight: Optional[str] = None, category: Optional[str] = None, 
fisrt_skill: Optional[str] = None, second_skill: Optional[str] = None, first_weakness: Optional[str] = None, 
second_weakness: Optional[str] = None, description: Optional[str] = None):
    data = {"name": name, "type": type, "height": height, "weight": weight, 
            "category": category, "fisrt_skill": fisrt_skill, 
            "second_skill": second_skill, "first_weakness": first_weakness, 
            "second_weakness": second_weakness, "description": description}
    pokemon = await update_pokemon(ID_POKEMON['id'], data)
    print(pokemon)
    return RedirectResponse('/menuadminpokemon')


@app.route('/menuadminpokemon/updatepokemon/id')
async def route_screen_update_pokemon(request: Request):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/login')
    if ID_POKEMON:
        return templates.TemplateResponse("pokemon_admin_dados_update.html", 
                                          {"request": request})


@app.get('/menuadminpokemon/updatepokemon')
async def get_id_for_update_pokemon(id: Optional[str] = None):
    ID_POKEMON['id'] = id
    return RedirectResponse('/menuadminpokemon/updatepokemon/id')





@app.route('/menuadmin/addpokemon')
def add_pokemon(request: Request):
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/login')
    return templates.TemplateResponse('pokemon_admin_dados_add.html', 
                                      {"request": request})


@app.get('/menuadmin/addallpokemon')
async def admin_add_all_pokemon():
    if not LOGIN.get("is_valid"):
        return RedirectResponse('/login')
    if len(await retrieve_pokemons()) == 0:
        await add_all_pokemon_data()
    return RedirectResponse('/menuadminpokemon')
    



@app.get('/exit')
def exit_login():
    # busca a variavel global para modificar
    LOGIN["username"] = None
    LOGIN["password"] = None
    LOGIN["is_valid"] = None
    return RedirectResponse('/')





@app.route('/menupokemon')
async def listar_todos_pokemon(request: Request):
    all_data = await retrieve_pokemons()
    list_data = []
    for data in all_data:
        list_data.append(list(data.values()))
    return templates.TemplateResponse('Listar_todos_pokemons.html', 
                                      {"request": request, "list_data": list_data})


