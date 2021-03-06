from solver import *
import shutil
import os

elements_table = {
    "CR": ("Crouzeix-Raviart", 1, "Discontinuous Lagrange", 0),    
    "CD": ("Lagrange", 2, "Discontinuous Lagrange", 0),    
    "TH": ("Lagrange", 2, "Lagrange", 1),
    

#    "TH1": ("Lagrange", 1, "Lagrange", 1), # doesnt work
#    "TH2": ("Lagrange", 2, "Lagrange", 2), # strange solution, form like eight
#    "TH3": ("Lagrange", 3, "Lagrange", 2), # like a normal solution 
#    "TH4": ("Lagrange", 3, "Lagrange", 3), # like a normal solution, not sure
#    "TH5": ("Lagrange", 3, "Lagrange", 1), # like a normal solution, not sure
#    
#    "CR1": ("Crouzeix-Raviart", 2, "Discontinuous Lagrange", 1), # invalid degree
#    
#    "CD1": ("Lagrange", 3, "Discontinuous Lagrange", 1), # like a normal solution
#    "CD2": ("Lagrange", 1, "Discontinuous Lagrange", 0), # doesnt work    
#    "CD3": ("Lagrange", 1, "Discontinuous Lagrange", 1), # doesnt work     
#    "CD4": ("Lagrange", 3, "Discontinuous Lagrange", 0), # like a normal solution, not sure     
    }
n_min = 25
n_max = 150
hstep = 5
n_ex = 200

times = {}
u_errs = {}
p_errs = {}
psi_errs = {}
 
def save_pvd(name, data):
    f = File(name+".pvd")
    f << data    
    
def save_pvd_list(u, p, psi, name, h):    
    save_pvd("result/pvd/velocity_%s_%d" % (name, h), u)
    save_pvd("result/pvd/pressure_%s_%d" % (name, h), p)
    save_pvd("result/pvd/psi_%s_%d" % (name, h), psi)

def save_time(name, h, time):    
    if h not in times:
        times[h] = {}
    times[h][name] = time
    
def save_u_err(name, h, u_err):    
    if h not in u_errs:
        u_errs[h] = {}
    u_errs[h][name] = u_err

def save_p_err(name, h, p_err):    
    if h not in p_errs:
        p_errs[h] = {}
    p_errs[h][name] = p_err
    
def save_psi_err(name, h, psi_err):    
    if h not in psi_errs:
        psi_errs[h] = {}
    psi_errs[h][name] = psi_err
    

def save_dat_aggr(fname, times):    
    ft = open("result/dat2/%s.dat" % fname, "w")
    
    arr_h = range(n_min, n_max+1, hstep)
    arr_n = []
    for name in times[n_min]:
        arr_n.append(name)
        
    ft.write("# h ")
    for name in arr_n:
        ft.write("%s " % name)
    ft.write("\n")
    for h in arr_h:
        ft.write("%.9f " % h)
        for name in arr_n:
            ft.write("%.9f " % (times[h][name]))
        ft.write("\n")
    ft.close()

def init_result():
    if os.path.exists("result"):
        shutil.rmtree("result")
    os.mkdir("result")
    os.mkdir("result/dat")
    os.mkdir("result/dat2")
    os.mkdir("result/pvd")
    os.mkdir("result/slice")
    
def save_result():    
    save_dat_aggr("time", times)
    save_dat_aggr("u_err", u_errs)
    save_dat_aggr("psi_err", psi_errs)
    save_dat_aggr("p_err", p_errs)
    
def save_dat(u, p, psi, name, h, mesh):
    coords = mesh.coordinates()    
    fu = open("result/dat/velocity_%s_%d.dat" % (name, h), "w")
    fp = open("result/dat/pressure_%s_%d.dat" % (name, h), "w")
    fps = open("result/dat/psi_%s_%d.dat" % (name, h), "w")
    fu.write("# x y ux uy\n")
    fp.write("# x y p\n")
    fps.write("# x y psi\n")
    last_y = coords[0][1]    
    for i in coords:
        yu = u(i)
        yp = p(i)
        yps = psi(i)
        if last_y != i[1]:            
            fu.write("\n")
            fp.write("\n")
            fps.write("\n")
        fu.write("%.9f %.9f %.9f %.9f\n" % (i[0], i[1], yu[0], yu[1] ))
        fp.write("%.9f %.9f %.9f\n" % (i[0], i[1], yp ))
        fps.write("%.9f %.9f %.9f\n" % (i[0], i[1], yps ))
        last_y = i[1]        
    fu.close()
    fp.close()
    fps.close()
    
def save_dat_slice_x(u, p, psi, name, h, mesh, x=0.5):
    coords = mesh.coordinates()    
    fu = open("result/slice/velocity_%s_%d_x%.1f.dat" % (name, h, x), "w")
    fp = open("result/slice/pressure_%s_%d_x%.1f.dat" % (name, h, x), "w")
    fps = open("result/slice/psi_%s_%d_x%.1f.dat" % (name, h,x ), "w")
    fu.write("# y ux uy\n")
    fp.write("# y p\n")
    fps.write("# y psi\n")   
    for i in coords:
        if i[0] == x:                
            yu = u(i)
            yp = p(i)
            yps = psi(i)
            fu.write("%.9f %.9f %.9f\n" % (i[1], yu[0], yu[1] ))
            fp.write("%.9f %.9f\n" % (i[1], yp ))
            fps.write("%.9f %.9f\n" % (i[1], yps ))       
    fu.close()
    fp.close()
    fps.close()
def save_dat_slice_y(u, p, psi, name, h, mesh, y=0.5):
    coords = mesh.coordinates()    
    fu = open("result/slice/velocity_%s_%d_y%.1f.dat" % (name, h, y), "w")
    fp = open("result/slice/pressure_%s_%d_y%.1f.dat" % (name, h, y), "w")
    fps = open("result/slice/psi_%s_%d_y%.1f.dat" % (name, h, y), "w")
    fu.write("# x ux uy\n")
    fp.write("# x p\n")
    fps.write("# x psi\n")   
    for i in coords:
        if i[1] == y:                
            yu = u(i)
            yp = p(i)
            yps = psi(i)
            fu.write("%.9f %.9f %.9f\n" % (i[0], yu[0], yu[1] ))
            fp.write("%.9f %.9f\n" % (i[0], yp ))
            fps.write("%.9f %.9f\n" % (i[0], yps ))       
    fu.close()
    fp.close()
    fps.close()

if __name__ == "__main__":
    init_result()
    mesh_ex = create_mesh(n_ex)
    space_ex = create_space("TH", mesh_ex)
    (u_ex, p_ex, t_ex) = solve_cavity(mesh_ex, space_ex)
    (psi_ex) = solve_cavity_psi(mesh_ex, space_ex, u_ex)
    save_pvd_list(u_ex, p_ex, psi_ex, "TH", n_ex)
    save_dat(u_ex, p_ex, psi_ex, "TH", n_ex, mesh_ex)
    save_dat_slice_x(u_ex, p_ex, psi_ex, "TH", n_ex, mesh_ex, 0.5)
    h = n_min
    while(h<=n_max):
        mesh = create_mesh(h)            
        for element in elements_table:        
            space = create_space(element, mesh)            
            (u, p, time) = solve_cavity(mesh, space)
            (psi) = solve_cavity_psi(mesh, space, u)
            (u_err, p_err, psi_err) = solve_cavity_error(u, p, psi, u_ex, p_ex, psi_ex, mesh_ex)
            save_pvd_list(u, p, psi, element, h)
            save_time(element, h, time)
            save_u_err(element, h, u_err)
            save_p_err(element, h, p_err)
            save_psi_err(element, h, psi_err)
            save_dat(u, p, psi, element, h, mesh_ex)
            save_dat_slice_x(u, p, psi, element, h, mesh_ex, 0.5)
        h+=hstep
    save_result()
