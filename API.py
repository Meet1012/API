from fastapi import FastAPI,Path
from pydantic import BaseModel

app = FastAPI()

class Items(BaseModel):
    item : str
    quantity : int
    price : float
    
class UpdateItem(BaseModel):
    item : str|None
    quantity : int|None
    price : int|None
    
result = {}
    
@app.get("/items/{item_no}")
def display(*,item_no : int = Path(description = "Enter the Item No")):
    if item_no in result:
        return result[item_no]
    return "Error Not Found"

@app.post("/Create_data/{item_no}")
def create_data(item:Items,item_no:int):
    if item_no in result:
        return "Item already exists"
    result[item_no] = {"item":item.item , "quantity":item.quantity ,"price": item.price}
    return result

@app.put("/Update_Item/{item_no}")
def update_item(item_no:int , items:UpdateItem):
    if item_no not in result:
        return "NO item Found"
    if items.item != None:
        result[item_no]["item"] = items.item
    if items.quantity != None:
        result[item_no]["quantity"] = items.quantity
    if items.price  != None:
        result[item_no]["price"] = items.price 
    return result[item_no]

@app.delete("/Delete_data/{item_no}")
def delete_data(item_no:int = Path(...,description="What u wanna delete")):
    if item_no not in result:
        return {"Error":"Element not found"}
    del result[item_no]
    
    