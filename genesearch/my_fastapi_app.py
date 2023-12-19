from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from fastapi import FastAPI

app = FastAPI()

class GeneFilterParams(BaseModel):
    gene_name: str = Query(None, title="Gene Name", description="Filter by gene name")
    chr_value: str = Query(None, title="Chromosome", description="Filter by chromosome")
    position_value: str = Query(None, title="Position", description="Filter by position")

@app.get("/genesearch/exceldatas/")
def search_genes(gene_params: GeneFilterParams):
    # Get the filter parameters from the query string
    gene_name = gene_params.gene_name
    chr_value = gene_params.chr_value
    position_value = gene_params.position_value

    # Make an API request to fetch data
    url = 'http://127.0.0.1:8000/genesearch/exceldatas/'
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch data")

    data = response.json()

    # Filter the data based on the provided parameters
    filtered_data = []
    for variant in data:
        if (not gene_name or variant['genes'] == gene_name) and \
           (not chr_value or variant['chr'] == chr_value) and \
           (not position_value or variant['position'] == position_value):
            filtered_data.append(variant)

    return filtered_data
