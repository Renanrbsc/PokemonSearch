import motor.motor_asyncio

# String mongo connection
MONGO_DETAILS = "mongodb://localhost:27017"

# Connection
engine = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Database
database = engine.PokemonSearch

# Collections
pokemon_collection = database.get_collection("pokemon_collection")
