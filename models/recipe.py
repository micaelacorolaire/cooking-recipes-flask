from sqlalchemy import String,Integer,Column,ForeignKey,UUID4
from models.base import BaseModel
from sqlalchemy import relationship 


class recipe(BaseModel):
    __tablename__='recipe'
    __args__={'schema':'public'}
    id_recipe=Column(String,primary_key=True,nullable=False)
    recipe_name=Column(String,nullable=False)
    ingredients=Column(String,nullable=False)
    instructions=Column(String,nullable=False)
    
    