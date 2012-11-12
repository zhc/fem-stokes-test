#set term postscript eps color
set term png size 600, 300
set key right
set xlabel 'h'
set ylabel 'pressure error'
set title ''

filename(quantity)=sprintf('result_orig/dat2/%s.dat', quantity)

plot filename('p_err') u 1:2 w l t 'CR', \
	filename('p_err') u 1:3 w l t 'TH', \
	filename('p_err') u 1:4 w l t 'CD'

pause -1