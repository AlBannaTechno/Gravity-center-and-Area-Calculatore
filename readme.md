### Cg-Area-Calculator
##### This program designed to calculate the surface area of any 3d shape
##### With get it's cg(center of gravity) in 3d model 
##### and draw it using open-gl as isometric shape in 2d-grid

### required
    Pyqt4 , opengl , glfw2[included with project]
### Notes 
    1- we modify glfw2.py to work correctly with opengl core-mode
    2- to support 3d view just use prespective instead of gl.glOrtho
### Usage : 
    run as python 
    just pass the points of shape like 
        (12,15),(17,36),(14,50),(60,0) : for 2d
        $(10,20,12),(40,60,13),(78,6,3),(14,96,30) : for 3d
    use mouse-wheel to zoom in and out
    use left clive as a pan : to move the prespective
    use right click to toggle between filling shape and lined shape
    
### ScreenShots 
    Look At : Screenshot.png
    
AreaCollector