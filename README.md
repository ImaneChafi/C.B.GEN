# 3D generation of dental crown bottoms using context learning - Geometric method
> A pythonic VTK and 3D mesh libraries as an automatic script for crown bottom generation using a preparation shape and its corresponding margin line as inputs.
By Imane Chafi, Farida Cheriet, Julia Keren, Ying Zhang, and François Guibault

Accepted to SPIE Medical Imaging 2024

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
Once these dependencies are installed, you can simply run the `crown_bottom_v4.py` file. All files will be saved under your `path` chosen. `python3.9` was used for this code. 

```
python crown_bottom_v4.py
```

The command line will prompt you for the file names.

## Evaluation

The code `hausdorff_dist` is available for you to use, to calculate the hausdorff distance between two meshes or pointclouds. 

## Licence
The code is available for all to use with contributions provided under `MIT` licence. 


