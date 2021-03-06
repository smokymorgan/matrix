from mat import Mat
import math
import matutil
## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return matutil.identity(labels, 1)
    #return Mat({labels, labels}, {(l,l):1 for l in labels})


## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    translator= identity()
    translator[('x','u')]= x
    translator[('y','u')]= y
    return translator

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    scaler= identity()
    scaler[('x', 'x')]= a
    scaler[('y', 'y')]= b
    return scaler

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    rotator= identity()
    rotator[('x','x')]= math.cos(angle)
    rotator[('x','y')]= -math.sin(angle)
    rotator[('y','x')]= math.sin(angle)
    rotator[('y','y')]= math.cos(angle)
    return rotator

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y)* rotation(angle)* translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    reflect= identity()
    reflect[('x', 'x')]= -1
    return reflect

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    reflect= identity()
    reflect[('y', 'y')]= -1
    return reflect
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    scolor= identity({'r', 'g', 'b'})
    scolor[('r','r')]= scale_r
    scolor[('g','g')]= scale_g
    scolor[('b','b')]= scale_b
    return scolor


## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    gray_matrix= scale_color(77/256, 151/256, 28/256)
    gray_matrix[('b','r')]= gray_matrix[('g','r')]= gray_matrix['r','r']
    gray_matrix[('b','g')]= gray_matrix[('r','g')]= gray_matrix['g','g']
    gray_matrix[('r','b')]= gray_matrix[('g','b')]= gray_matrix['b','b']


    return gray_matrix


## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


