#set term postscript eps color
set term png size 600, 300
set title ''
set key left
set xlabel 'h'
set ylabel 'seconds'

filename(quantity)=sprintf('result_orig/dat2/%s.dat', quantity)

plot filename('time') u 1:2 w l t 'CR', \
	filename('time') u 1:3 w l t 'TH', \
	filename('time') u 1:4 w l t 'CD'

pause -1