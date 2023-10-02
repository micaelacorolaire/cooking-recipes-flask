from pydantic import BaseModel,Field

class ingredients(BaseModel):
    id_ingredients:str=Field(min_length=1,nullable=False)
    ingredients_name:str=Field(min_length=1,max_length=2000,nullable=False)