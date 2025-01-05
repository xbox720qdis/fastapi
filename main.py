from uuid import UUID
from typing import List
from models import User, Gender, Role, Product
from fastapi import FastAPI, HTTPException

app = FastAPI()

db_products: List[Product]= [
    Product(
        id= 1,
        name= "cocanbcvedsg",
        price= 10.99,
        description= "hhjueiw",
        quantity= 1
    ),
     Product(
        id= 2,
        name= "mAnGo",
        price= 11.99,
        description= "gaswdyu",
        quantity= 3
    )
]




db: List[User] = [
   User(
       id=UUID("99914afc-d48a-4b1b-8e1e-492d32d2cf03"),
       first_name="beni",
        last_name="ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
       id=UUID("37db47f8-6abf-4c1e-aff7-44d8a4e84c16"),
       first_name="sikh",
        last_name="Nigga Balls",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

#create product list

@app.get("/")
async def root():
    return {"hello": "mundo"}  


@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

# create CRUD operation to product

@app.get("/api/v1/products")
async def fetch_products():
    return db_products

@app.post("/api/v1/products")
async def create_product(product: Product):
    db_products.append(product)

    print("ryueu")

@app.delete("/api/v1/products/{product_id}")
async def delete_product(product_id: int ):
        for p in db_products:
            print("elemento", p)
            print(product_id)
            if p.id == product_id:
                db_products.remove(p)
                return 
        raise HTTPException(
            status_code=404,
            detail=f"product with id: {product_id} does not exist"
        )

    
