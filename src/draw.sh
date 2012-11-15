#!/bin/sh

gnuplot vis_time.plt > time.png
gnuplot vis_psi_err.plt > psi_err.png
gnuplot vis_p_err.plt > p_err.png
gnuplot vis_u_err.plt > u_err.png
gnuplot vis_slice.plt

