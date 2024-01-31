import pyvista as pv
from pyvista import examples
import numpy as np
import pymeshlab as ml
import trimesh

"""
Performs crown bottom generation using geometric manipulation
Parameters:
    path: path of die file to create crown bottom from
    die_name: file name (stl, TODO: Add more file types )
    marginline_name: margin line name with file extention (.ply, the line reconstruction is completed here)
    offset: cement gap 
    n_iter: degree of the polynomial used to approximate the windowed sync function. (see docs.pyvista.org)
    pass_band: windowed sinc filter, between 0 and 2, where lower values cause more smoothing.
    dist_margin_undercut: Distance where undercuts should be blocked from the marginline
    dist_margin_smooth: Distance where smoothing should stop from the marginline
"""
class CrownBottom:
  def __init__(self, path, die_name, marginline_name, offset, n_iter, pass_band, dist_margin_undercut, dist_margin_smooth):
    self.path = path
    self.die_name = die_name
    self.marginline_name = marginline_name
    self.offset = offset
    self.n_iter = n_iter
    self.pass_band = pass_band # The passband value for the windowed sinc filter. This should be between 0 and 2, where lower values cause more smoothing.
    self.dist_margin_undercut = dist_margin_undercut
    self.dist_margin_smooth = dist_margin_smooth

  def smoothing(self):

    die_mesh = pv.read(self.path + self.die_name)
    magrin_mesh = pv.read(self.path + self.marginline_name)

    ########## 1. Margin line reconstruction and Bounding Box creation ##########
    # Get margin-line as set of points and reconstruct as line
    points_3d = magrin_mesh.points
    polygon = pv.lines_from_points(points_3d, close=True)

    # Extract die mesh bounds
    xmin, xmax, ymin, ymax, zmin, zmax = die_mesh.bounds

    # Extrude along z axis bounding box with form as mesh and plot
    body = polygon.extrude((3, 2, 10), capping=True, inplace=True) #change numbers with direction for margin line extrusion for the crown bottom cases
    body.plot(color='white', specular=1, screenshot='extruded.png')
    body.save(f"extruded_line_margin_{self.marginline_name}.stl")

    # Create mesh of extruded box into a closed shell (using trimesh)
    extruded_complete = trimesh.load_mesh(f"extruded_line_margin_{self.marginline_name}.stl")
    extruded_complete = extruded_complete.convex_hull
    extruded_complete.export(f'mesh_extruded_{self.marginline_name}.stl')

    ########## 2. Smoothing based on distance from margin line ###################

    # Start by removing the crown bottom from the die
    extruded_pv = pv.read(f'mesh_extruded_{self.marginline_name}.stl')
    select_cb = die_mesh.select_enclosed_points(extruded_pv)
    inside_cb = select_cb.threshold(0.5) 
    outside_cb = select_cb.threshold(0.5, invert=True) 

    cb_inside = inside_cb.extract_geometry()
    cb_outside = outside_cb.extract_geometry() # No need for the outside mesh

    cb_inside.save(f"separated_cb_{self.die_name}.stl")

    # Translate bounding box up by the distance from the margin to smooth
    print(extruded_pv.center)
    extruded_pv_translated = extruded_pv.translate([0, 0, self.dist_margin_smooth], inplace=True)
    print(extruded_pv_translated.center)

    # Smooth the inside of the bounding box only
    select_blur = cb_inside.select_enclosed_points(extruded_pv_translated)
    inside_blur = select_blur.threshold(0.5) 
    outside_blur = select_blur.threshold(0.5, invert=True)

    # Visualization of the smoothed section of the crown bottom
    p = pv.Plotter()
    p.add_mesh(inside_blur, color="Crimson") 

    surf_inside_b = inside_blur.extract_geometry()
    surf_outside_b = outside_blur.extract_geometry()
    smooth_blur = surf_inside_b.smooth_taubin(self.n_iter, pass_band=0.05)
    smooth_blur.save(f"smoothed_cb_{self.die_name}.stl")

    # Combine two meshes (smoothed part and the not smoothed part)
    complete_smoothing = smooth_blur.merge(surf_outside_b)
    complete_smoothing.save(f"crown_bottom_smoothed_{self.die_name}.stl")
    return complete_smoothing

  def marginline_extention(self, complete_smoothing):
    die_mesh = pv.read(self.path + self.die_name)
    magrin_mesh = pv.read(self.path + self.marginline_name)

    # Recreating the marginline
    mgl = magrin_mesh.points
    mgl = pv.lines_from_points(mgl, close=True)

    # Extruding the margin-line but in the x-y axis only
    mgl = mgl.extrude((0.2, 0.2, 0), inplace=True)
    mgl.plot(color='white', specular=1, screenshot='extruded.png')
    
    merged_cb = complete_smoothing.merge(mgl) #change line for mgl instead of complete smoothing
    
    #This is the ouput crown bottom 
    merged_cb.save("cb_merged.stl")

def main():
    ##Smoothing - Change folder and filename by user input
    path = "data/"
    die_name =  input("Enter die file name:")
    marginline_name = input("Enter margin line file name:")
    crown_bottom_example = CrownBottom(path, die_name, marginline_name, 0.035, 1000, 0.5, 0.1, 1.5)
    smoothed_cb = crown_bottom_example.smoothing()
    crown_bottom_example.marginline_extention(smoothed_cb)
##Main function
if __name__ == "__main__":
    main()
