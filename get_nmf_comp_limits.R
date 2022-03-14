#!/usr/bin/env Rscript

# Description: Calculates min and max value of vertex-wise scores for each component in an NMF solution.
# Module requirements: R/3.5.1

left_scores <- read.table("results/left_k8.txt", header = F, sep = " ") # MODIFY
right_scores <- read.table("results/right_k8.txt", header = F, sep = " ") # MODIFY

leftmin <- apply(left_scores,2,min)
leftmax <- apply(left_scores,2,max)
left_limits <- rbind(leftmin, leftmax)

rightmin <- apply(right_scores,2,min)
rightmax <- apply(right_scores,2,max)
right_limits <- rbind(rightmin, rightmax)

# write results to text file
write.table(left_limits, file="nmf_k8_left_minmax.csv", sep=",", row.names=F, col.names=F) # MODIFY
write.table(right_limits, file="nmf_k8_right_minmax.csv", sep=",", row.names=F, col.names=F) # MODIFY
