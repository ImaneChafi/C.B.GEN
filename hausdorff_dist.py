
import numpy as np
import pymeshlab as ml

"""
Simple Hausdorff Distance function between two shapes (cb_gen and cb_gt) using Pymeshlab
Parameters:
    path: path of die file to create crown bottom from
    cb_gen: file name for crown bottom generated 
    cb_gt: file name for ground truth crown bottom
"""

def hausdff(cb_gen, cb_gt):
    #Create an array to store hd mean values
    hd_arr = []

    #Print hausdorff distance using Pymeshlab
    ms = ml.MeshSet()
    ms.load_new_mesh(cb_gt) #ground truth cb
    ms.load_new_mesh(cb_gen) #generated cb

    res_dict = ms.apply_filter('hausdorff_distance', targetmesh=1, sampledmesh=0, savesample = True)
    print(res_dict)

    #Adding all hausdorff distance in txt file for analysis. 
    with open("/die24/HD.txt", 'a') as f:
        f.write('HD for ' + f"cb_merged{self.die_name}.stl and GT is" + " " + str(res_dict) + "\n")
    ms.save_current_mesh(self.path + f'cb_merged{self.die_name}.stl')

    #Each hausdorff distance mean is appended to the array. It can then be used to compute the average mean distance. 
    hd_arr.append(str(res_dict.get("mean")))
    print(hd_arr)

def main():
    ##Smoothing - Change folder and filename by user input
    path = "/data/"
    cb_gen =  "cb_merged.stl"
    cb_gt = "crownb.stl"
    hausdff(path + cb_gen, path + cb_gt)

##Main function
if __name__ == "__main__":
    main()
