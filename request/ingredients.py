from pydantic import BaseModel,UUID4

class ingredients(BaseModel):
    id_ingredients=UUID4
    ingredients_name=str