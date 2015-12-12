# Libao Jin
# December 11, 2015

rm(list = ls())

# import data from .xlsx file
# install.packages("gdata")
library("gdata")
library("cluster")
library("fpc")
file <- "data/daisy.xlsx"
data <- read.xls(file)
std.data <- scale(data, center = TRUE, scale = TRUE)
# print(std.data)

d <- dist(std.data, method = "euclidean", diag = TRUE, upper = FALSE)
hcs <- hclust(d, method = "complete")

k <- kmeans(std.data, 2, iter.max = 10, nstart = 1, algorithm = "MacQueen", trace=FALSE)
print(k)
cluster <- k$cluster
dev.new()
pdf("result/kmeans_clustering_1.pdf")
clusplot(std.data, cluster, color = TRUE, shade = TRUE, labels = 2, lines = 0)
dev.off()
dev.new()
pdf("result/kmeans_clustering_2.pdf")
plotcluster(std.data, cluster)
dev.off()

output_cluster <- "result/kmeans_cluster.csv"
write.csv(cluster, output_cluster)
