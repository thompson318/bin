#! /bin/python3

import vtk
import numpy
from sksurgeryeval.algorithms.algorithms import np2vtk

reader = vtk.vtkSTLReader()
reader.SetFileName("phantom_patch_00.stl")
reader.Update()
source=reader.GetOutput()
trans=numpy.loadtxt("../configuration/model_to_world.txt")
transformer=vtk.vtkTransformPolyDataFilter()

transform=vtk.vtkTransform()
transform.SetMatrix(np2vtk(trans))
transformer.SetTransform(transform)
transformer.SetInputData(source)
target=vtk.vtkPolyData()
transformer.SetOutput(target)
transformer.Update()
