# Automated Detection of Missing Links in Developed Bicycle Networks 
This is the source code for the scientific article [Automated Detection of Missing Links in Developed Bicycle Networks](https://arxiv.org/abs/2201.03402) by A. Vybornova, T. Cunha, A. Gühnemann and [M. Szell](http://michael.szell.net/). The code runs the IPDC procedure (Identify, Prioritize, Decluster, Classify), as presented in the article, for the use case of Copenhagen, but can easily be modified for application to any other city. It pre-processes data from OpenStreetMap and executes the first 3 steps (Identify, Prioritize, Decluster) on the bicycle network; results are generated and saved for the last, manual step of the IPDC procedure (Classify).

**Preprint**: [https://arxiv.org/abs/2201.03402](https://arxiv.org/abs/2201.03402)  
**Visualization**: [FixBike.Net](http://fixbike.net) 

## Folder structure
The main folder/repo is `bikenwgaps`, containing Jupyter notebooks with code (`00_import`, `01_IP`, `02_D`);  the imported packages (`packages`) and the plot parameters (`parameters_plot`) and a subfolder with OSM data (`data/`). All output from the code is saved to the subfolders `./data/pickle/` and `./analysis/`. The folder `_compare` contains the output as generated if all 3 notebooks are run successfully. Once all output is generated, the notebooks can be re-run independently from each other (in any order). 

## Setting up code environment 

The required python version is 3.8.8. `pip` must be installed and updated before setting up the environment. `requirements.txt` must be placed in the working directory. 

```
conda create --override-channels -c conda-forge -n bnwenv shapely
conda activate bnwenv
pip install -r requirements.txt 
conda install -c conda-forge ipywidgets
pip install --user ipykernel 
python -m ipykernel install --user --name=bnwker
```

## Running the jupyter notebooks
Run jupyter notebook with bnwker (Kernel > Change Kernel > bnwker) and make it trusted (Not Trusted > Trust). Run the notebooks in the indicated order:
* `00_import`
* `01_IP`
* `02_D`)
