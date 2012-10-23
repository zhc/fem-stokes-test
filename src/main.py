from plotter import *
from solver import *

ff = ("28*pi*pi*sin(4*pi*x[0])*cos(4*pi*x[1])", "-36*pi*pi*cos(4*pi*x[0])*sin(4*pi*x[1])")
uu = ("sin(4*pi*x[0])*cos(4*pi*x[1])", "-cos(4*pi*x[0])*sin(4*pi*x[1])")
pp = ("pi*cos(4*pi*x[0])*cos(4*pi*x[1])")
elements_table = {
    "CR": ("Crouzeix-Raviart", 1, "Discontinuous Lagrange", 0),    
    "CD": ("Lagrange", 2, "Discontinuous Lagrange", 0),    
    "TH": ("Lagrange", 2, "Lagrange", 1)
    }
h = 20
hmax = 100
hstep = 20

if __name__ == "__main__":
    init_result()
    mesh_ex = create_mesh(150)
    space_ex = create_space("TH", mesh_ex)
    (u_ex, p_ex, ttt) = solve_cavity(mesh_ex, space_ex)
    while(h<=hmax):
        mesh = create_mesh(h)            
        for element in elements_table:        
            space = create_space(element, mesh)
#            (u, p, time) = solve_square(mesh, space)
#            collect_square_result(element, h, u, p, time, mesh)
            
#            (u_err, p_err) = compare_square(u, p, u_ex, p_ex, mesh)
#            collect_square_error(element, h, u_err, p_err)
            
            (u, p, time) = solve_cavity(mesh, space)
            (psi) = solve_cavity_psi(mesh, space, u)
            
            collect_cavity_result(element, h, u, p, psi, time, mesh)
            (u_err, p_err) = compare_square(u, p, u_ex, p_ex, mesh)
            collect_square_error(element, h, u_err, p_err)
            
            
        h+=hstep
    save_result()