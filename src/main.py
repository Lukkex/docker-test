from fastapi import FastAPI

app = FastAPI()

#r = redis.Redis(host="redis", port=6379)

# Test debugpy 
# import debugpy
# debugpy.listen(("0.0.0.0", 5678))

# Test torch
import torch


@app.get("/")
def read_root():
    return torch.cuda.is_available()

#@app.get("/hits")
#def read_root():
#    r.incr("hits")
#    return {"Number of Hits": r.get("hits")}