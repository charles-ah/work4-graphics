from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, edge, transform, screen, color ):
 #   edge = new_matrix
#    transform = new_matrix()
    s = open(fname,'r').read().split("\n")
    #print str(s)
    i = 0 
    while i < len(s):
        print s[i]
        if s[i] == "line":
            val = s[i+1].split(" ")
            #print str(val)
            add_edge(edge ,int(val[0]), int(val[1]), int(val[2]), int(val[3]), int(val[4]), int(val[5]))
            i += 2
        if s[i] == "ident":
            transform = ident(new_matrix())
            i += 1
        if s[i] == "scale":
            val = s[i+1].split(" ")
            m = make_scale( int(val[0]), int(val[1]), int(val[2]))
            matrix_mult(m,transform)
            i += 2
        if s[i] == "move":
            val = s[i+1].split(" ")
            matrix_mult(make_translate( int(val[0]), int(val[1]), int(val[2])),transform)
            i += 2
        if s[i] == "rotate":
            val = s[i+1].split(" ")
            if val[0] == "x":
                matrix_mult(make_rotX( int(val[1])),transform)
            if val[0] == "y":
                matrix_mult(make_rotY( int(val[1])),transform)
            if val[0] == "z":
                matrix_mult(make_rotZ( int(val[1])),transform)
            i += 2
        if s[i] == "apply":
            edge = matrix_mult(transform,edge)
            i += 1
        if s[i] == "display":
            for x in range(len(edge)):
                for j in range(len(edge[0])):
                    edge[x][j] = int(edge[x][j])
                
            draw_lines(edge,screen,color)
            display(screen)
            i += 1
        if s[i] == "save":
            val = s[i+1]
            draw_lines(edge,screen,color)
            save_ppm(screen,val)
            i += 2
        
#        print str(transform)
#        print s[i]
#        print str(edge)
        
