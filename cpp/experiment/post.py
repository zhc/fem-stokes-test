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

mesh = Mesh("mesh/mesh_200.xml")
u_ex = read("th", "200")

for scheme in ["th", "cr", "cd"]:
	for n in ["20", "40", "80", "160"]:
		u = read(scheme, n)
		print scheme, n, l2(u, u_ex, mesh)