# Author: Alyssa Dai
# Last updated: 2021/06/22
# Description: Automatically generates a 2x2 labelled heatmap for each NMF component in the brain pattern of a behaviour PLS latent variable,
# denoting the changes in metrics significantly correlated with the latent variable per component. Colorbar also generated as separate image.
# Edit all lines commented with "MODIFY"!

# Module requirements: anaconda/5.1.0-python3 on CIC (has seaborn package)
# Usage: python create_NMF_BSR_heatmaps.py
# Outputs: 1) bsr_colorbar_vertical.png  2) k*(number of significant LVs) .png files named as follows: lv{lv_num}_k{k}_comp{comp_num}.png

# ----------

# Import modules
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.patheffects as PathEffects
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedFormatter, FixedLocator
import numpy as np
import pandas as pd
import seaborn as sns
import math
import os

# Read in required pyls outputs
input_dir = "outputs/N266_ScanAge/15-AgeIncl_Resid_RaceHotEnc_out" # MODIFY - directory in which your PLS outputs have been saved
output_dir = "plots/15-AgeIncl_Resid_RaceHotEnc_out" # MODIFY - directory in which to save your BSR plots, doesn't have to exist

if not os.path.exists(output_dir):
    os.mkdir(f"{output_dir}")

# If another implementation of PLS was used (i.e. not Ross Markello's pyls), modify below filenames as necessary
permres_pvals= pd.read_csv(f"{input_dir}/permres_pvals.csv", header=None)
bsr_weights = np.loadtxt(f"{input_dir}/bootres_x_weights_normed.csv", delimiter=",")


# Set figure aesthetics
sns.set_style("ticks")

# MODIFY - upper BSR limit for colorbar (~ x-axis limit in BSR bar plot), lower limit will automatically set to be symmetric about 0 for readability
cb_max = 8
cb_min = -cb_max

# Generate colorbar (will correspond to colors used to populate metric plots below)
fig, ax = plt.subplots(figsize=(0.3, 6), dpi=300)
cmap = mpl.cm.RdBu_r
norm = mpl.colors.Normalize(vmin=cb_min, vmax=cb_max)
cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm,
                                orientation='vertical') # Can switch to horizontal if desired
cb1.outline.set_visible(False)
cb1.set_ticks(ticks=MultipleLocator(2)) # MODIFY - interval between colorbar ticks
cb1.ax.tick_params(labelsize=16)
# fig.tight_layout()

# Save colorbar
plt.savefig(f"{output_dir}/bsr_colorbar_vertical.png", transparent=True, bbox_inches='tight',dpi=300)


k = 8 # MODIFY - number of components in your NMF solution
metric_labels = np.array([['CT', 'SA'], ['MC', 'GI']]) # MODIFY - ensure that order of metrics matches that in your actual data

# Generate metric plot for each NMF component for each significant LV (p < .05).
# Note that any resulting plot with all squares grayed out indicate that no metrics contributed significantly to the LV within that component.
for lv_num in range(permres_pvals.shape[0]):
    if (permres_pvals.loc[lv_num][0] <= 0.05):
        bsr_weights_lv = bsr_weights[:,lv_num]
        bsr_weights_lv_splits = np.array_split(bsr_weights_lv,k)
        for c in range(k):
            fig, ax = plt.subplots(figsize=(4, 4))

            lv_comp = bsr_weights_lv_splits[c].reshape(2,2)

            im = sns.heatmap(lv_comp, cmap='RdBu_r',
                             vmin = cb_min, vmax = cb_max,
                             cbar = False, linewidths=2, xticklabels=False, yticklabels=False, # linecolor = 'black',
                             mask = abs(lv_comp) < 1.96, # OPTIONAL: MODIFY - by default, only shows colors of metrics with p < .05; can change value to 2.58 (p < .01), or comment out this line to show color position of all metrics
                             square = True)
            ax.patch.set_facecolor('#717272') # Color of non-significant metrics - gray by default
            fig.patch.set_alpha(0)

            # Add metric labels
            for y in range(lv_comp.shape[0]):
                for x in range(lv_comp.shape[1]):
                    txt = plt.text(x + 0.5, y + 0.54, metric_labels[y, x],
                             horizontalalignment='center',
                             verticalalignment='center',
                             fontsize = 50, fontweight="semibold")
                    # OPTIONAL: Add white text stroke for contrast against color of square (may be useful if you have both BSRs close to extrema and values close to 0)
                    # txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='w')])

            # Save image
            plt.savefig(f"{output_dir}/lv{lv_num+1}_k{k}_comp{c+1}.png", dpi=300)
