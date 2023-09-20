import vtk
import re

def adder(s):
    print("function called")
    print(s)
    re.sub(r"\\","/",s)
    print(s)
    # return s
    reader = vtk.vtkSTLReader()
    # reader.SetFileName(r"C:\Users\HP\Downloads\Cube.stl")
    reader.SetFileName(s)

    # Create a mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # A renderer and render window
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # An interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1) # Background color

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()
    print("Visuals generated")
    
if __name__ == "__main__":
    adder()