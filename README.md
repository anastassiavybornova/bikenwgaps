# Automated Detection of Missing Links in Bicycle Networks 
This is the source code for the scientific article [Automated Detection of Missing Links in Bicycle Networks](https://arxiv.org/abs/2201.03402) by A. Vybornova, T. Cunha, A. Gühnemann and [M. Szell](http://michael.szell.net/). The code runs the IPDC procedure (Identify, Prioritize, Decluster, Classify), as presented in the article, for the use case of Copenhagen. 

**Preprint**: [https://arxiv.org/abs/2201.03402](https://arxiv.org/abs/2201.03402) 

**Visualization (map)**: [FixBike.Net](http://fixbike.net) 

**Visualization (table)**: [FixBike.Net/table](http://fixbike.net/table) 

<img src="https://user-images.githubusercontent.com/73348979/154666572-0d797b4b-f208-4103-851b-dc03cdca2af5.png"/>

## Workflow demonstration: Copenhagen
The code presented here pre-processes Copenhagen data from OpenStreetMap (see below) and executes the all four steps of the IPDC procedure (Identify, Prioritize, Decluster, Classify). The last step (Classify) requires a manual classification of automatically identified gaps.
The code is applied to the use case of Copenhagen to demonstrate the workflow, but can be easily modified for application to any other city - see instructions in the last part of the readme.

## Folder structure

The main folder/repo is `bikenwgaps`. It contains:
* Jupyter notebooks with code: `00_import`, `01_IP`, `02_DC`, `03_PLOT`
*  `_compare`: subfolder with code output as generated if all 3 notebooks are run successfully
* `/analysis/`: subfolder with gap classification data for Copenhagen (to reproduce plots)
*  `/data/`: subfolder with OSM data (in csv file format) as imported in `00_import`
*  `/fixbikenet/`: subfolder with all html and image sources for [FixBike.Net](http://fixbike.net) and [FixBike.Net/table](http://fixbike.net/table)
* `packages.py`: list of packages imported within each notebook
* `parameters_plot.py`: list of plot parameters imported for plotting 
*  `requirements.txt`: required packages for setting up the code environment

All output from the code is saved to the subfolders `./data/pickle/`, `./analysis/`, and `./results/`. Once all output is generated, the notebooks can be re-run independently from each other (in any order). 

## Running binder
[![badge](https://img.shields.io/badge/run%20code-on%20binder-F5A252.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/anastassiavybornova/bikenwgaps/HEAD)

## Running on your local machine

### Setting up code environment 

The required python version is 3.8.8. `pip` must be installed and updated before setting up the environment. `requirements.txt` must be placed in the working directory. For issues that may arise with geopandas dependencies on windows, we refer our fellow sufferers to this [blogpost by Geoff Boeing](https://geoffboeing.com/2014/09/using-geopandas-windows/). 

```
conda create --override-channels -c conda-forge -n bnwenv shapely
conda activate bnwenv
pip install -r requirements.txt 
conda install -c conda-forge ipywidgets
pip install --user ipykernel 
python -m ipykernel install --user --name=bnwker
```

### Running the jupyter notebooks
Run jupyter notebook with bnwker (Kernel > Change Kernel > bnwker) and make it trusted (Not Trusted > Trust). Run the notebooks in the indicated order:
* `00_import`
* `01_IP`
* `02_DC`
* `03_PLOT`

## Using the workflow: Application to other cities
The code can be easily modified for application to any other city. Steps to take: 
* Before running `00_import` - change the input data (csv files generated from [https://www.openstreetmap.org/](OpenStreetMap))
* Run `00_import`, adjusting file names for import, and verify if largest connected component is accurately represented
* Run `01_IP`, adjusting D_min (detour factor) if needed (default: D_min = 1.5)
* Run `02_DC`, adjusting B_cutoff (benefit cutoff) if needed (default: B_cutoff = 15300) and the coordinates for map centering (default is mycity_coord = [55.6761, 12.5683] for Copenhagen)
* Manually classify the gaps 
    * use "./analysis/gaps_declustered_table.csv" and "./analysis/gaps_declustered_plot.html" generated for your city* column "class": enter gap class (e.g. "BR" for bridge, "ST" for street, etc.)
    * if gap is not confirmed (data issue/error): leave "class" cell for that row empty
    * columns "address" and "comments": optional
    * save edited csv table as "./analysis/gaps_classified_table.csv" (replacing the existing file of Copenhagen data)
    * table is imported in the next step (notebook 03_PLOT) for visualization of results
* Run `03_PLOT`, adjusting coordinates for map centering and (if needed) adjusting gap colours and classes

<img src="https://user-images.githubusercontent.com/73348979/154647305-264f33ab-5136-4576-a5b8-8a8db495a042.png">
