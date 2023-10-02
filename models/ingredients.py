from sqlalchemy import Column,String,Integer,ForeignKey,UUID4
from models.base import BaseModel
from sqlalchemy import relationship

class ingredients(BaseModel):
    __tablename__='ingredients'
    __args__={'schema':'public'}
    id_ingredients=Column(String,primary_key=True,nullable=False)
    ingredients_name=Column(String,nullable=False)
    

