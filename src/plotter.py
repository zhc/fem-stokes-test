from dolfin import * 
import os
import main
from solver import create_mesh

color = True

square_time_collector = []
square_err_collector = []

psi_collector = []

def init_result():
    #delete all "result_*" files
    filelist = [ f for f in os.listdir(".") if f.startswith("result_") ]
    for f in filelist:
        os.remove(f)  
        
             
#def collect_u_p_result(element, h, u, p, time, mesh, task_name):
#    coords = mesh.coordinates() 
#    fu_name =  "result_%s_u_%d_%s" % (task_name, h, element)
#    fp_name = "result_%s_p_%d_%s" % (task_name, h, element)
#    
#    fff = File(fu_name+".pvd")
#    fff << u
#    fff = File(fp_name+".pvd")
#    fff << p
#
#    return
#    
#    fu = open(fu_name+".dat", "w")
#    fp = open(fp_name+".dat", "w")
#    fu.write("# x y ux uy\n")
#    fp.write("# x y p\n")
#    last_y = coords[0][1]
#    for i in coords:
#        y = u(i)
#        if last_y != i[1]:
#            fp.write("\n")
#            fu.write("\n")
#        fu.write("%.9f %.9f %.9f %.9f\n" % (i[0], i[1], y[0], y[1] ))
#        fp.write("%.9f %.9f %.9f\n" % (i[0], i[1], p(i) ))
#        last_y = i[1]        
#    fu.close()
#    fp.close()
#    
#    fu = open(fu_name+".plt", "w")
#    fu.write("""set xrange[0:1] 
#set yrange[0:1]
#set isosamples 50
#set pm3d
#set pal defined (-3 "blue", 0 "white", 1 "red")
#set pal gray
#unset surface
#set view map
#set contour
#set cntrparam levels 10
#set clabel 
#set key outside
#set term postscript eps color
#set title 'Velocity X-component, %s element, %dx%d cells'
#set xlabel 'X'
#set ylabel 'Y'
#set key title 'Levels'
#set key noautotitle
#set key lmargin
#set output '%s_X.eps'
#set key off
#splot '%s.dat' using 1:2:3 with lines
#set title 'Velocity Y-component, %s element, %dx%d cells'
#set output '%s_Y.eps'
#splot '%s.dat' using 1:2:4 with lines
#""" % (element, h, h, fu_name, fu_name, element, h, h, fu_name, fu_name))
#    fu.close()
#    
#    fp = open(fp_name+".plt", "w")
#    fp.write("""set xrange[0:1] 
#set yrange[0:1]
#set isosamples 50
#set pm3d
#set pal defined (-3 "blue", 0 "white", 1 "red")
#unset surface
#set view map
#set contour
#set cntrparam levels auto 10
#set key outside
#set term postscript eps color
#set title 'Pressure, %s element, %dx%d cells'
#set xlabel 'X'
#set ylabel 'Y'
#set key title 'Levels'
#set key noautotitle
#set key lmargin
#set output '%s.eps'
#set key off
#splot '%s.dat' w lines""" % (element, h, h, fp_name, fp_name))
#    fp.close()
#    
#    os.system("gnuplot %s" % (fp_name+".plt"))
#    os.system("gnuplot %s" % (fu_name+".plt"))
#        
#def collect_cavity_result(element, h, u, p, psi, time, mesh):
#    collect_u_p_result(element, h, u, p, time, mesh, "cavity")
#    square_time_collector.append( {"h":h, "e":element, "t":time} )
#    
#    #saving psi
#    fu_name =  "result_%s_psi_%d_%s" % ("cavity", h, element)
#    fff = File(fu_name+".pvd")
#    fff << psi
#    
#    mesh = create_mesh(150)
#    coords = mesh.coordinates()
#    for i in coords:
#        if i[0] == 0.1 or i[0] == 0.3 or i[0] == 0.5:
#            psi_collector.append({"e":element, "x":i[0], "y":i[1], "v":psi(i)})
##    psi_collector.append()
#    
#def save_result():
#    # saving time
#    square_time_collector.sort(key=lambda x: x["e"])
#    square_time_collector.sort(key=lambda x: x["h"])
#    fname = "result_square_time"
#    f = open(fname+".dat", "w")
#    if len(square_time_collector) >= len(main.elements_table):
#        f.write("h %s %s %s\n" % (square_time_collector[0]["e"], square_time_collector[1]["e"], square_time_collector[2]["e"]))
#        i = 0
#        while (i < len(square_time_collector)):
#            f.write("%d %.9f %.9f %.9f\n" % (square_time_collector[i]["h"], square_time_collector[i]["t"], square_time_collector[i+1]["t"], square_time_collector[i+2]["t"]) )
#            i += len(main.elements_table)
#        f.close()        
#        
#        f = open(fname+".plt", "w")
#        f.write("""#set xrange[0:1] 
##set yrange[0:1]
##set term postscript eps color
#set term png size 640, 480
#set title 'Solution time dependence from cell count'
#set xlabel 'cell count'
#set ylabel 'time'
#set output '%s.png'
#set key inside
#set key autotitle columnheader
#plot '%s.dat' using 1:2 with lines, '%s.dat' using 1:3 with lines, '%s.dat' using 1:4 with lines
#""" % (fname, fname, fname, fname))
#        f.close()
#        
#        os.system("gnuplot %s" % (fname+".plt"))
#
#    # saving errors
#    square_err_collector.sort(key=lambda x: x["e"])
#    square_err_collector.sort(key=lambda x: x["h"])
#    fname1 = "result_square_err_u"
#    fname2 = "result_square_err_p"
#    f1 = open(fname1+".dat", "w")
#    f2 = open(fname2+".dat", "w")
#    if len(square_err_collector) >= len(main.elements_table):
#        f1.write("h %s %s %s\n" % (square_err_collector[0]["e"], square_err_collector[1]["e"], square_err_collector[2]["e"]))
#        f2.write("h %s %s %s\n" % (square_err_collector[0]["e"], square_err_collector[1]["e"], square_err_collector[2]["e"]))
#        i = 0
#        while (i < len(square_time_collector)):
#            f1.write("%d %.9f %.9f %.9f\n" % (square_err_collector[i]["h"], square_err_collector[i]["u_err"], square_err_collector[i+1]["u_err"], square_err_collector[i+2]["u_err"]) )
#            f2.write("%d %.9f %.9f %.9f\n" % (square_err_collector[i]["h"], square_err_collector[i]["p_err"], square_err_collector[i+1]["p_err"], square_err_collector[i+2]["p_err"]) )
#            i += len(main.elements_table)
#        f1.close()
#        f2.close()        
#        
#        f = open("result_square_err.plt", "w")
#        f.write("""#set term postscript eps color
#set term png size 640, 480
#set title 'Velocity error dependence from cell count'
#set xlabel 'cell count'
#set ylabel 'velocity error'
#set output '%s.png'
#set key inside
#set key autotitle columnheader
#plot '%s.dat' using 1:2 with lines, '%s.dat' using 1:3 with lines, '%s.dat' using 1:4 with lines
#
#set title 'Pressure error dependence from cell count'
#set ylabel 'pressure error'
#set output '%s.png'
#plot '%s.dat' using 1:2 with lines, '%s.dat' using 1:3 with lines, '%s.dat' using 1:4 with lines
#""" % (fname1, fname1, fname1, fname1, fname2, fname2, fname2, fname2 ))
#        f.close()
#        
#        os.system("gnuplot result_square_err.plt")
#    if (len(psi_collector) > 0):
#        psi_collector.sort(key=lambda x: x["e"])
#        psi_collector.sort(key=lambda x: x["x"])
#        psi_collector.sort(key=lambda x: x["y"])
#        fname = "result_cavity_psi"
#        f = open(fname+".dat", "w")
#        i = 0
#        f.write("y %s %s %s %s %s %s %s %s %s\n" %
#                (psi_collector[i]["e"], 
##                 psi_collector[i]["x"],
#                 psi_collector[i+1]["e"], 
##                 psi_collector[i+1]["x"],
#                 psi_collector[i+2]["e"], 
##                 psi_collector[i+2]["x"],
#                 psi_collector[i+3]["e"], 
##                 psi_collector[i+3]["x"],
#                 psi_collector[i+4]["e"], 
##                 psi_collector[i+4]["x"],
#                 psi_collector[i+5]["e"],
##                 psi_collector[i+5]["x"],
#                 psi_collector[i+6]["e"], 
##                 psi_collector[i+6]["x"],
#                 psi_collector[i+7]["e"], 
##                 psi_collector[i+7]["x"],
#                 psi_collector[i+8]["e"],
##                 psi_collector[i+8]["x"]
#                 ))        
#        while i < len(psi_collector):
#            f.write("%.9f %.9f %.9f %.9f %.9f %.9f %.9f %.9f %.9f %.9f\n" % 
#                    (psi_collector[i]["y"], 
#                     psi_collector[i]["v"], 
#                     psi_collector[i+1]["v"], 
#                     psi_collector[i+2]["v"], 
#                     psi_collector[i+3]["v"], 
#                     psi_collector[i+4]["v"], 
#                     psi_collector[i+5]["v"],
#                     psi_collector[i+6]["v"], 
#                     psi_collector[i+7]["v"], 
#                     psi_collector[i+8]["v"]))
#            i += 9
#        f.close()
#        
#        f = open(fname+".plt", "w")
#        f.write("""#set term postscript eps color
#set term png size 640, 480
#set title 'Stream functions at x=0.1'
#set xlabel 'y'
#set ylabel 'psi'
#set output '%s_x0.1.png'
#set key inside
#set key autotitle columnheader
#plot '%s.dat' using 1:2 with lines, '%s.dat' using 1:3 with lines, '%s.dat' using 1:4 with lines
#
#set title 'Stream functions at x=0.3'
#set output '%s_x0.3.png'
#plot '%s.dat' using 1:5 with lines, '%s.dat' using 1:6 with lines, '%s.dat' using 1:7 with lines
#
#set title 'Stream functions at x=0.5'
#set output '%s_x0.5.png'
#plot '%s.dat' using 1:8 with lines, '%s.dat' using 1:9 with lines, '%s.dat' using 1:10 with lines
#""" % (fname, fname, fname, fname,
#       fname, fname, fname, fname, 
#       fname, fname, fname, fname))
#        f.close()
#        
#        os.system("gnuplot "+fname+".plt")        