# 3D generation of dental crown bottoms using context learning - Geometric method
> A pythonic VTK and 3D mesh libraries as an automatic script for crown bottom generation using a preparation shape and its corresponding margin line as inputs.
By Imane Chafi, Farida Cheriet, Julia Keren, Ying Zhang, and François Guibault

Accepted to SPIE Medical Imaging 2024

If this research or our data has been of help, please cite our paper as such:

```
@inproceedings{10.1117/12.3006955,
author = {Imane Chafi and Farida Cheriet and Julia Keren and Ying Zhang and Fran{\c{c}}ois Guibault},
title = {{3D generation of dental crown bottoms using context learning}},
volume = {12931},
booktitle = {Medical Imaging 2024: Imaging Informatics for Healthcare, Research, and Applications},
editor = {Hiroyuki Yoshida and Shandong Wu},
organization = {International Society for Optics and Photonics},
publisher = {SPIE},
pages = {129310I},
keywords = {Dentistry, Generative Adversarial Network, Shape generation, Dental Crown Bottom Generation, Geometric deformation     , 3D models, Machine learning, Computer-aided design},
year = {2024},
doi = {10.1117/12.3006955},
URL = {https://doi.org/10.1117/12.3006955}
}
``` 

## Software Implementation 
The code is separated into two sections: Geometric method and ML method
The ML method can be found [here](https://github.com/ImaneChafi/SP-Prep-GAN). This code builds onto code from the [SP-GAN]([https://liruihui.github.io/publication/SP-GAN/) paper by Li et al. 

Due to privacy laws concerning dentistry shape material, we cannot share the original data here. Please email imane.chafi@polymtl.ca for data. 

## Installation

You can download the code from this github page for the geometric method. Refer [here](https://github.com/ImaneChafi/SP-Prep-GAN) for the GAN-Based method.

```
git clone https://github.com/ImaneChafi/C.B.GEN.git
```

## Dependencies

The code for the geometric method needs a couple pythonic function as dependencies. The main ones used are:

> [Pyvista](https://pypi.org/project/pyvista/)
> [Trimesh](https://pypi.org/project/trimesh/)
> [Pymeshlab](https://pypi.org/project/pymeshlab/)
> Numpy

## Running the code
Once these dependencies are installed, you can simply run the `cb_generation.py` file. All files will be saved under your `path` chosen. `python3.9` was used for this code. 

```
python cb_generation.py
```

The command line will prompt you for the file names.

## Evaluation

The code `hausdorff_dist` is available for you to use, to calculate the hausdorff distance between two meshes or pointclouds. 
And example output for the hausdorff distance code evaluation is:
```
{'RMS': 0.05054453760385513, 'diag_mesh_0': 11.399076461791992, 'diag_mesh_1': 11.315515084423572, 'max': 0.1677803099155426, 'mean': 0.039864495396614075, 'min': 6.468382451885191e-08, 'n_samples': 7619}
```
More information about this function [here](https://pymeshlab.readthedocs.io/en/latest/filter_list.html) 

## Licence
The code is available under `MIT` licence. Please list authors if this code has been of help to you!


