#!/bin/bash

# Description: Generates a brain map for each component in a given NMF solution using create_civet_image.sh
# Module requirements: minc-toolkit, minc-toolkit-extras

# MODIFY -----------------------------------
out_dir=figures # does not need to exist
ncomps=8
leftlim=nmf_k${ncomps}_left_minmax.csv # must match output of get_nmf_comp_limits.R
rightlim=nmf_k${ncomps}_right_minmax.csv # must match output of get_nmf_comp_limits.R
lh_surface=PS_N266_lh_average.obj # average gray matter surface
rh_surface=PS_N266_rh_average.obj
nmf_res_lh=results/left_k${ncomps}.txt # left component scores
nmf_res_rh=results/right_k${ncomps}.txt # right component scores
# ------------------------------------------

mkdir -p ${out_dir}

for (( comp=1; comp<=$ncomps; comp++ )); do
  ./create_civet_image_nmf.sh $lh_surface $nmf_res_lh $(head -1 $leftlim | cut -d"," -f $comp),$(tail -1 $leftlim | cut -d"," -f $comp) $rh_surface $nmf_res_rh $(head -1 $rightlim | cut -d"," -f $comp),$(tail -1 $rightlim | cut -d"," -f $comp) $comp ${out_dir}/k${ncomps}_comp_${comp}.png
done
