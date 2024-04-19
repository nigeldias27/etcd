from fastapi import FastAPI
import etcd3
from pydantic import BaseModel
app = FastAPI()
try:
    etcd = etcd3.client(host = "Etcd-server",port = 2379)
    connection = 1
except Exception as e:
    print(e)
    connection = 0
class KeyVal(BaseModel):
    key : str
    val: str
@app.get("/listKeys")
def listKeys():
    keyList = etcd.get_all()
    return [m.key for (_, m) in keyList]

@app.get("/getVal")
def getVal(key):
    value,metadata = etcd.get(key)
    if value == None:
        return "Key does not exist" 
    else:
        return value
@app.post("/putKeyVal")
def putKeyVal(keyVal: KeyVal):
    print(keyVal,keyVal.key,keyVal.val)
    etcd.put(keyVal.key,keyVal.val)
    return "Successfully Added"
@app.get("/deleteVal")
def getVal(key):
    isDeleted = etcd.delete(key)
    if isDeleted:
        return "Key Deleted"
    else:
        return "Error occured while deleting"
@app.get("/getConnStatus")
def getVal():
    return connection