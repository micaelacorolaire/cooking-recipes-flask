from pydantic import BaseModel,Field

class recipe_ingredients(BaseModel):
    id_recipe_ingredients:str=Field(min_length=1,nullable=False)
    ingredients:str=Field(min_length=1,max_length=1000,nullable=False)
    quantity:int=Field(ge=1,le=1000,nullable=False)
    
    