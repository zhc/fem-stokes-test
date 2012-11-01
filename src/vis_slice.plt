#set term postscript eps color
#set term png size 640, 480
set title ''


filename(quantity, element, h, slice)=sprintf('result/slice/%s_%s_%d_%s.dat', quantity, element, h, slice)

set multiplot layout 2, 2

slice = 'y0.5'
quantity= 'psi'

plot \
	filename(quantity, 'CR', 25, slice) w l t 'CR', \
	filename(quantity, 'CD', 25, slice) w l t 'CD', \
	filename(quantity, 'TH', 25, slice) w l t 'TH', \
	filename(quantity, 'TH', 200, slice) w l t 'EX'

plot \
	filename(quantity, 'CR', 50, slice) w l t 'CR', \
	filename(quantity, 'CD', 50, slice) w l t 'CD', \
	filename(quantity, 'TH', 50, slice) w l t 'TH', \
	filename(quantity, 'TH', 200, slice) w l t 'EX'

plot \
	filename(quantity, 'CR', 100, slice) w l t 'CR', \
	filename(quantity, 'CD', 100, slice) w l t 'CD', \
	filename(quantity, 'TH', 100, slice) w l t 'TH', \
	filename(quantity, 'TH', 200, slice) w l t 'EX'

plot \
	filename(quantity, 'CR', 150, slice) w l t 'CR', \
	filename(quantity, 'CD', 150, slice) w l t 'CD', \
	filename(quantity, 'TH', 150, slice) w l t 'TH', \
	filename(quantity, 'TH', 200, slice) w l t 'EX'

	
unset multiplot	
 
pause -1