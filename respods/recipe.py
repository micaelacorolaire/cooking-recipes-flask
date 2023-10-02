from pydantic import BaseModel ,Field

class recipe(BaseModel):
    id_recipe:str=Field(min_length=1,nullable=False)
    recipe_name:str=Field(min_length=1,max_length=60,nullable=False)
    ingredients:str=Field(min_length=1,max_length=200,nullable=False)
    instructions:str=Field(min_length=1,max_length=1000,nullable=False)