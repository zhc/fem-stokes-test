from dolfin import *
import main

def create_mesh(h):
    print "create mesh", h
    mesh = UnitSquare(h, h)
    return mesh

def create_space(element, mesh):
    print "create space", element
    (u_element, u_order, p_element, p_order) = main.elements_table[element]
    U = VectorFunctionSpace(mesh, u_element, u_order)
    P = FunctionSpace(mesh, p_element, p_order)
    W = U*P
    return W
    
def solve_cavity(mesh, space):
    print "solve cavity"
    def domain_top(x, on_boundary):
        return on_boundary and x[1] > 1 - DOLFIN_EPS  
    def domain_walls(x, on_boundary):
        return on_boundary and x[1] < 1 - DOLFIN_EPS    
    bc0 = DirichletBC(space.sub(0), Constant((0,0)), domain_walls)
    bc1 = DirichletBC(space.sub(0), Constant((1,0)), domain_top)
    bcs = [bc0, bc1]    
    (u, p) = TrialFunctions(space)
    (v, q) = TestFunctions(space)
    f = Constant((0, 0))       
    a = inner(grad(u), grad(v))*dx - p*div(v)*dx + div(u)*q*dx
    L = inner(f, v)*dx    
    t = Timer("Solve timing");
    t.start()            
    U = Function(space)
    problem = LinearVariationalProblem(a, L, U, bcs=bcs)
    solver = LinearVariationalSolver(problem)
    solver.solve()    
    t.stop()    
    (u, p) = U.split(True)    
    
    # correct pressure
    c = assemble(p*dx)
    vec = p.vector()
    for i in range(vec.size()):
        vec[i] -= c
                
    
    return u, p, t.value()


def solve_cavity_psi(mesh, space, u):
    V = FunctionSpace(mesh, "Lagrange", 2)
    def domain_walls(x, on_boundary):
        return on_boundary
    bc1 = DirichletBC(V, Constant(0), domain_walls)    
    bcs = [bc1]

    psi = TrialFunction(V)
    v = TestFunction(V)
    
    a = inner(grad(psi), grad(v))*dx
    L = inner(-rot(u), v)*dx
    
    PSI = Function(V)
    problem = LinearVariationalProblem(a, L, PSI, bcs=bcs)
    solver = LinearVariationalSolver(problem)
    solver.solve()
    return PSI

def solve_cavity_error(u, p, psi, u_ex, p_ex, psi_ex, mesh_ex):
    M = inner((u_ex - u),(u_ex - u))*dx
    v_err = assemble(M, mesh=mesh_ex)    
    Mp = (p_ex - p)*(p_ex - p)*dx
    p_err = assemble(Mp, mesh=mesh_ex)
    Mps = (psi_ex - psi)*(psi_ex - psi)*dx
    psi_err = assemble(Mps, mesh=mesh_ex)
    return (sqrt(v_err), sqrt(p_err), sqrt(psi_err))
