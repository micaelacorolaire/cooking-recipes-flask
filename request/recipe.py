from pydantic import BaseModel,UUID4

class recipe(BaseModel):
    id_recipe=UUID4
    recipe_name=str
    ingredients=str
    instructions=str