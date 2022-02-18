# Automated Detection of Missing Links in Bicycle Networks 
This is the source code for the scientific article [Automated Detection of Missing Links in Bicycle Networks](https://arxiv.org/abs/2201.03402) by A. Vybornova, T. Cunha, A. Gühnemann and [M. Szell](http://michael.szell.net/). The code runs the IPDC procedure (Identify, Prioritize, Decluster, Classify), as presented in the article, for the use case of Copenhagen. 

## Workflow demonstration: Copenhagen
The code presented here pre-processes Copenhagen data from OpenStreetMap (see below) and executes all four steps of the IPDC procedure (Identify, Prioritize, Decluster, Classify). The final output is a list of 105 top prirority gaps on the Copenhagen network, as visualized on [FixBike.Net](http://fixbike.net). The last step (Classify) requires a manual classification of automatically identified gaps. We provide our classification results for Copenhagen in order to make the entire workflow reproducible. 

## Using the workflow: Application to other cities
The code is applied to the use case of Copenhagen to demonstrate the workflow, but can be easily modified for application to any other city. 
[Input data: 1 csv file each for all nodes and edges for car network and protected bicycle infrastructure network; finally, in the table "..." that is the output of `02_D` must be used to conduct a manual classification of identified gaps; table "..." is then used as input for `03_plot`]

**Preprint**: [https://arxiv.org/abs/2201.03402](https://arxiv.org/abs/2201.03402)  
**Visualization (map)**: [FixBike.Net](http://fixbike.net) 
**Visualization (table)**: [FixBike.Net](http://fixbike.net/table) 

## Folder structure

The main folder/repo is `bikenwgaps`. It contains:
* Jupyter notebooks with code: `00_import`, `01_IP`, `02_DC`, `03_plot`
*  `requirements.txt`: required packages for setting up the code environment
* `packages.py`: list of packages imported within each notebook
* `parameters_plot.py`: list of plot parameters imported for plotting 
*  `/data/`: subfolder with OSM data (in csv file format) as imported in `00_import`
*  `_compare`: subfolder with code output as generated if all 3 notebooks are run successfully

All output from the code is saved to the subfolders `./data/pickle/` and `./analysis/`. Once all output is generated, the notebooks can be re-run independently from each other (in any order). 

## Running binder
[Binder: Live repository](https://mybinder.org/v2/gh/anastassiavybornova/bikenwgaps/HEAD)

## Running on your local machine

### Setting up code environment 

The required python version is 3.8.8. `pip` must be installed and updated before setting up the environment. `requirements.txt` must be placed in the working directory. For issues that may arise with geopandas dependencies on windows, we refer to this [blogpost by Geoff Boeing](https://geoffboeing.com/2014/09/using-geopandas-windows/). 

```
conda create --override-channels -c conda-forge -n bnwenv shapely
conda activate bnwenv
pip install -r requirements.txt 
conda install -c conda-forge ipywidgets
pip install --user ipykernel 
python -m ipykernel install --user --name=bnwker
```

### Using the jupyter notebooks
Run jupyter notebook with bnwker (Kernel > Change Kernel > bnwker) and make it trusted (Not Trusted > Trust). Run the notebooks in the indicated order:
* `00_import`
* `01_IP`
* `02_DC`
* `03_plot`

## Results
The final output of the code consists of 2 files, saved to `./analysis/`, which give an overview of identified gaps (a html file with a map, as shown below, and a csv file containing the gap list) and are to be used for the last, manual step of the IPDC procedure - Classify.

![kbh_gh](https://user-images.githubusercontent.com/73348979/154326998-5b3609e9-b858-4fb1-ae30-fef281f840ec.png)
