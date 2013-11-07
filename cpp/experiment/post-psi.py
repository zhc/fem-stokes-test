from dolfin import *

scheme = "th"
n = "20"

def read(scheme, n):
	mesh = Mesh("mesh/mesh_%s.xml" % (n))
	U = VectorFunctionSpace(mesh, "Lagrange", 2)
	P = FunctionSpace(mesh, "Lagrange", 1)
	if (scheme == "cr"):
		U = VectorFunctionSpace(mesh, "CR", 1)
		P = FunctionSpace(mesh, "DG", 0)
	elif scheme == "cd":
		U = VectorFunctionSpace(mesh, "CG", 2)
		P = FunctionSpace(mesh, "DG", 0)
	u = Function(U)
	p = Function(P)
	f = File("result-%s-%s/u.bin" % (scheme, n))
	f >> u.vector()
	return u

def l2(u, u_ex, mesh):
	M = inner((u - u_ex),(u - u_ex))*dx
	return sqrt(assemble(M, mesh=mesh))

def domain_walls(x, on_boundary):
        return on_boundary

def psi(scheme, n):
	mesh = Mesh("mesh/mesh_%s.xml" % (n))
	U = VectorFunctionSpace(mesh, "Lagrange", 2)
	if (scheme == "cr"):
		U = VectorFunctionSpace(mesh, "CR", 1)
	elif scheme == "cd":
		U = VectorFunctionSpace(mesh, "CG", 2)
	u = Function(U)
	f = File("result-%s-%s/u.bin" % (scheme, n))
	f >> u.vector()

	V = FunctionSpace(mesh, "Lagrange", 2)
	psi = TrialFunction(V)
	v = TestFunction(V)
	a = inner(grad(psi), grad(v))*dx
	L = inner(-rot(u), v)*dx
	pp = Function(V)
	bc1 = DirichletBC(V, Constant(0), domain_walls)
	bcs = [bc1]
	solve(a == L, pp, bcs=bcs)
	return pp

psi_ex = psi("th", "200")
mesh = Mesh("mesh/mesh_200.xml")

for scheme in ["th", "cr", "cd"]:
	for n in ["20", "40", "80", "160"]:
		pp = psi(scheme, n)
		print scheme, n, l2(pp, psi_ex, mesh)