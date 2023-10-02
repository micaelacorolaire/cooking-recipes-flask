from sqlalchemy import String,Integer,Column,ForeignKey,UUID4
from models.base import BaseModel
from sqlalchemy import relationship

class recipe_ingredients(BaseModel):
    __tablename__='recipe ingredients'
    __args__={'schema':'public'}
    id_recipe_ingredients=Column(String,primary_key=True,nullable=False)
    ingredient=Column(String,nullable=False)
    quantity=Column(int,nullable=False)
    