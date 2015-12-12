# Libao Jin
# December 12, 2015

rm(list = ls())

# import data from .xlsx file
# install.packages("gdata")
library("gdata")
library("cluster")
library("fpc")
library("MASS")
sink("result/result_regression.txt")
file <- "data/daisy.xlsx"
data <- read.xls(file)
print(dim(data))
std.data <- scale(data[, c(4:10, 12)], center = TRUE, scale = TRUE)
# std.data <- data[,c(4:10, 12)]
print(std.data)

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

group1 <- NULL
group2 <- NULL
for (i in seq(50))
{
	if (cluster[i] == 1)
	{
		if (is.null(group1))
		{
			group1 <- data[i,]
		}
		else
		{	
			group1 <- rbind(group1, data[i,])
		}
	}
	else
	{
		if (is.null(group2))
		{
			group2 <- data[i,]
		}
		else
		{	
			group2 <- rbind(group2, data[i,])
		}
	}
}

names <- c("Y1", "Y2", "Y3", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9")
colnames(group1) <- names
colnames(group2) <- names
print("Group 1")
print(group1)
print("Group 2")
print(group2)

lm.1 <- lm(log(Y1, base = exp(1)) ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 + X9, data = group1)
print(summary(lm.1))
step.1 <- stepAIC(lm.1, direction = "both")
step.1$anova
print(summary(step.1))

lm.2 <- lm(log(Y1, base = exp(1)) ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 + X9, data = group2)
print(summary(lm.2))
step.2 <- stepAIC(lm.2, direction = "both")
step.2$anova
print(summary(step.2))
sink()
