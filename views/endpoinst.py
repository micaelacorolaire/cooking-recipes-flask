from flask import Flask

app=Flask(__name__)

@app.route('/ingredients',methods=['get'])
def get_ingredients():
    ingredients=db.session.query.filter(id_ingredients=id).first()
    if id_ingredients==id:
        db.session.get(ingredients)
        db.commit()
        print(r'the ingredient is into the app')
    else: 
        print(r'the ingredient {ingredient }dont exists')
        
@app.route('/ingredients/{id}',methods=['delete'])
def deleted_ingredients():
    ingredients=db.session.query.filter(id_ingredients=id).first()
    if id_ingredients==id:
        db.session.delete(ingredients) 
        db.commit()
        print(r'the ingredient was deleted')
    else:
        print(r'the ingredient with {id}could not deleted')
        
@app.route('/ingredients/{id}',methods=['post'])
def post_ingredients(id_ingredients:str):
    ingredients=db.session.query.filter(id_ingredients=id).first()
    if id_ingredients==id:
        db.session.post(ingredients)
        db.commit()
        print(r'the ingredient was added to the app')
    else:
        print(r'an error has ocurred and i can not updated what you are trying to do')
@app.route('/recipe,methods=[get]') 
def get_recipe():
    recipe=db.session.query.filter(recipe_name=recipe.name).first()
    if recipe.name==recipe.name:
        db.session.get(recipe)
        db.commit()
    else:
        print(r'the recipe could not be displayed')
@app.route('/recipe/{id},methods=[post]')
def post_recipe(id:str):
    recipe=db.session.query.filter(recipe_name=recipe.name).first()
    if recipe.id==id:
        db.session.post(recipe)
        db.commit()
    else:
        print(r'this recipe could not updated')
@app.route('/recipe/{id},methods=[deleted]')
def deleted_recipe(id:str):
     recipe=db.session.query.filter(recipe_id=recipe.id).first()
     if recipe.id==id:
        db.session.post(recipe)
        db.commit()
     else:
        print(r'this recipe could not be deleted')
        
@app.route('/recipe_ingredients,methods=[get]')
def ingredients_get():
    recipe=db.session.query.filter(recipe_ingredients_id=recipe_ingredients.id).first()
    if recipe_ingredients==recipe_ingredients:
        db.session.get(recipe)
        db.commit()
    else:
        print('the recipe is not here.')
        
@app.route('/recipe_ingredients/{id_recipe_ingredients},methods=[deleted]')
def deleted(id_recipe_ingredients:str):
     recipe=db.session.query.filter(recipe_ingredients_id=recipe_ingredients.id).first()
     if id_recipe_ingredients=id_recipe_ingredients:
         db.session.deleted(id_recipe_ingredients)
         db.commit()
    else:
        print('the recipe ingredients could not be deleted')
        
@app.route('/recipe_ingredients/{id_recipe_ingredients},methods=[post]')
def post_recipe_ingredients():
     recipe=db.session.query.filter(id_recipe_ingredients=id_recipe_ingredients).first()
     if id_recipe_ingredients==id_recipe_ingredients:
         db.session.updated(id_recipe_ingredients)
         db.commit()
     else:
        print(r'the ingredient recipe was updated')
        
        
         
    
    
    
              

        




if __name__=='__main__':
    app.run(debug=True)