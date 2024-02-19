from flask import Blueprint, request
from app.db import pokemons
import uuid

blp = Blueprint("pokemon_endpoint", __name__)

@blp.route("/", methods=["GET"])
def get_all_pokemons():
    return {"pokemon": list(pokemons.values())}

@blp.route("/pokemon/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    return pokemons[pokemon_id]

@blp.route("/", methods=["POST"])
def create_pokemon():
    request_data = request.get_json()
    pokemons_id = uuid.uuid4().hex
    new_pokemon = {**request_data, "attack": [], "id":pokemons_id}
    pokemons[pokemons_id] = new_pokemon
    return new_pokemon, 201

# @blp.route("/", methods=["DELETE"])
# def get_all_pokemons():
#     return "get pokemon"