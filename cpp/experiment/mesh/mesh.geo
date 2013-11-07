l = 1.0;
p = l/200;
Point(1) = {0, 0, 0, p};
Point(2) = {0, l, 0, p};
Point(3) = {l, l, 0, p};
Point(4) = {l, 0, 0, p};
Line(1) = {2, 3};
Line(2) = {3, 4};
Line(3) = {4, 1};
Line(4) = {1, 2};
Line Loop(5) = {4, 1, 2, 3};
Plane Surface(6) = {5};
Transfinite Surface {6} Left;

Physical Line(1) = {1};
Physical Line(2) = {4, 3, 2};
Physical Surface(1) = {6};


