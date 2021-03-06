# nmf_viz
Scripts for visualizing outputs of 1) NMF and 2) bPLS runs using NMF component weights as the brain input. Works with outputs from [cobra-nmf](https://github.com/CoBrALab/cobra-nmf) and [pyls](https://github.com/rmarkello/pyls). Usage instructions found in script comment headers; detailed instructions for using nmf_viz scripts within the cobra-nmf pipeline also documented [here](https://github.com/CoBrALab/documentation/wiki/opNMF-for-vertex-data#1-set-up-your-input-spreadsheet).

### Plot vertex-wise NMF component weights on a cortical surface
1) get_nmf_comp_limits.R
2) make_nmf_brain_maps.sh

### Plot metric-wise bootstrap ratios for each NMF component in a bPLS brain pattern as a heatmap 
* create_NMF_BSR_heatmaps.py
