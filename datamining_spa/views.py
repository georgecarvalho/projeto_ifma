from django.shortcuts import render
from fastapi import FastAPI, Request

app = FastAPI()

def index(request):
    if request.GET.get('media'):
        media = request.GET.get('media')
        percFaltas = request.GET.get('percFaltas') + '%'
        percDiscConc = request.GET.get('percDiscConc') + '%'
        dados = [media, percFaltas, percDiscConc]

        return render(request, 'index.html',{
        'dados': dados
    })
    
    return render(request, 'index.html')

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}
