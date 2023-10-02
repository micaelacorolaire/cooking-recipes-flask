from pydantic import BaseModel,UUID4

class recipe_ingredients(BaseModel):
    id_recipe_ingredients=UUID4
    ingredients=str
    quantity=int
