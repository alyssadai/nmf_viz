#!/bin/bash

# Description: Generates a brain map for each component in a given NMF solution using create_civet_image.sh
# Module requirements: minc-toolkit, minc-toolkit-extras

# MODIFY -----------------------------------
ncomps=8
leftlim=nmf_k${ncomps}_left_minmax.csv # must match output of get_nmf_comp_limits.R
rightlim=nmf_k${ncomps}_right_minmax.csv # must match output of get_nmf_comp_limits.R
lh_surface=../../derivatives/PS_N265_lh_average.obj
rh_surface=../../derivatives/PS_N265_rh_average.obj
nmf_res_lh=results/left_k${ncomps}.txt
nmf_res_rh=results/right_k${ncomps}.txt
# ------------------------------------------

for (( comp=1; comp<=$ncomps; comp++ )); do
  # MODIFY version of create_civet_image.sh if desired
  ./create_civet_image_nmf_1.1.sh $lh_surface $nmf_res_lh $(head -1 $leftlim | cut -d"," -f $comp),$(tail -1 $leftlim | cut -d"," -f $comp) $rh_surface $nmf_res_rh $(head -1 $rightlim | cut -d"," -f $comp),$(tail -1 $rightlim | cut -d"," -f $comp) $comp k${ncomps}_comp_${comp}.png
done
