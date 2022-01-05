# Automated Detection of Missing Links in Developed Bicycle Networks 
This is the source code for the scientific article [*Automated Detection of Missing Links in Developed Bicycle Networks*](ADD LINK) by A. Vybornova, T. Cunha, A. Gühnemann and [M. Szell](http://michael.szell.net/). The code runs the IPCC procedure (Identify, Prioritize, Cluster, Classify), as presented in the article, for the use case of Copenhagen, but can easily be modified for application to any other city. It pre-processes data from OpenStreetMap and executes the first 3 steps (Identify, Prioritize, Cluster) on the bicycle network; results are generated and saved for the last, manual step of the IPCC procedure (Classify).

**Preprint**: [](ADD LINK)  
**Visualization**: [FixBike.Net](https://fixbike.net) 

## Folder structure
The main folder/repo is `bikenwgaps`, containing Jupyter notebooks with code (`00_import`, `01_IP`, `02_C`);  the imported packages (`packages`) and the plot parameters (`parameters_plot`) and a subfolder with OSM data (`data/`). Output from the code is saved to the subfolders `./data/pickle/` and `./analysis/`. 

## Setting up code environment
```
conda create --override-channels -c conda-forge -n OSMNX python=3 osmnx=0.16.2 python-igraph watermark haversine rasterio tqdm geojson
conda activate OSMNX
conda install -c conda-forge ipywidgets
pip install opencv-python
conda install -c anaconda gdal
pip install --user ipykernel
python -m ipykernel install --user --name=OSMNX
```
Run Jupyter Notebook with kernel OSMNX (Kernel > Change Kernel > OSMNX)
