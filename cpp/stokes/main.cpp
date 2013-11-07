#include <iostream>
#include "stokesthProblem.h"

using namespace std;

int main(int argc, char** argv)
{
    string filename = "parameters.xml";
    if (argc > 1){
        filename = argv[1];
    }
    if (argc > 2){

    }
    if (File::exists(filename)){
        File f_param(filename);
        f_param >> parameters;
    } else {
        Parameters problem("problem");
        problem.add("domain", "mesh/mesh_20.xml");
        problem.add("subdomains", "mesh/mesh_20_physical_region.xml");
        problem.add("boundaries", "mesh/mesh_20_facet_region.xml");
        problem.add("method", "default");
        problem.add("pc", "default");
        problem.add("result", "result/");
        parameters.add(problem);

        File f_param(filename);
        f_param << parameters;
    }
    Mesh mesh(parameters("problem")["domain"]);
    stokesthProblem sp(mesh);
    Constant top(1, 0);
    Constant zero(0, 0);
    sp.addDirichletBC(0, top, 1);
    sp.addDirichletBC(0, zero, 2);
    Timer timer("Calculation Solver");
    timer.start();
    sp.solve();
    timer.stop();
    std::cout << timer.value() << std::endl;
    string path = parameters("problem")["result"];
    if (argc > 2){
        path = argv[2];
    }
    Function u(sp.w()[0]);
    Function p(sp.w()[1]);
    File fu(path + "u.bin");
    fu << *u.vector();
    File fp(path + "p.bin");
    fp << *p.vector();
    return 0;
}

