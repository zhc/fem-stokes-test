#set term postscript eps color
#set term png size 640, 480
set title ''

filename(quantity)=sprintf('result/dat2/%s.dat', quantity)

plot filename('u_err') u 1:2 w l t 'CR', \
	filename('u_err') u 1:3 w l t 'TH', \
	filename('u_err') u 1:4 w l t 'CD'

pause -1