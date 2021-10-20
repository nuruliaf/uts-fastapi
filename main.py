import json

from fastapi import FastAPI, Body, Depends, Request
from app.model import UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer


with open("menu.json", "r") as read_file: 
    data = json.load(read_file)


##################### U S E R #########################
users = [
    {
        "fullname": "Nurul Izza A",
        "username": "asdf",
        "password": "asdf"
    }
]

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome to UTS TST 18219011 Nurul Izza Afkharinah!."}

#signup user
@app.post("/user/signup", tags=["User"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.username)

def check_user(data: UserLoginSchema):
    for user in users:
        if user["username"] == data.username and user["password"] == data.password:
            return True
    return False

#login user
@app.post("/user/login", tags=["User"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.username)
    return {
        "error": "Wrong username or password!"
    }


##################### C R U D #########################
#read all item
@app.get('/menu', dependencies=[Depends(JWTBearer())], tags=["CRUD Menu"])
async def read_all_menu():
    return data

#read an item
@app.get('/menu/{item_id}', dependencies=[Depends(JWTBearer())], tags=["CRUD Menu"]) 
async def read_menu(item_id: int) -> dict: 
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

#add item
@app.post('/menu', dependencies=[Depends(JWTBearer())], tags=["CRUD Menu"])
async def add_menu(name:str) -> dict:
    id = 1
    if(len(data['menu']) > 0):
        id = data['menu'][len(data['menu']) - 1]['id'] + 1
    new_data = {'id':id, 'name' :name}
    data['menu'].append(dict(new_data))
    read_file.close()
    with open("menu.json", "w") as write_file: 
        json.dump(data, write_file, indent=4)
    write_file.close()
    
    return (new_data)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error'
        )

#update item
@app.patch('/menu/{item_id}', dependencies=[Depends(JWTBearer())], tags=["CRUD Menu"]) 
async def update_menu(item_id: int, name:str) -> dict: 
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['name'] = name
            read_file.close()
            with open("menu.json", "w") as write_file: 
                json.dump(data, write_file, indent=4)
            write_file.close()

            return {'Data Updated Successfully'}
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

#delete item
@app.delete('/menu/{item_id}', dependencies=[Depends(JWTBearer())], tags=["CRUD Menu"]) 
async def delete_menu(item_id: int) -> dict: 
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            data['menu'].remove(menu_item)
            read_file.close()
            with open("menu.json", "w") as write_file: 
                json.dump(data, write_file, indent=4)
            write_file.close()

            return {'Data Deleted Successfully'}
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )