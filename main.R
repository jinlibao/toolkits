# Libao Jin
# December 11, 2015

rm(list = ls())

# import data from .xlsx file
# install.packages("gdata")
library("gdata")
file <- "daisy.xlsx"
data <- read.xls(file)
std.data <- scale(data)
# print(std.data)

# Factor Analysis
# fact <- factanal(std.data, 2, scores = "Bartlett", rotation = "varimax")
# print(fact)
# print(fact$score)

# Principla Analysis
prin <- princomp(std.data, cor = TRUE)
pre <- predict(prin)
print(summary(prin))
print(loadings(prin))

# Step by step
c.data <- cov(std.data)
e.data <- eigen(c.data)
values <- e.data$values
vectors <- e.data$vectores
print("Covariance")
print(c.data)
print("Eigen Values")
print(values)
print("Eigen Vectore")
print(e.data$vectors)

for(N in seq(12))
{
	print(N)
	score <- 0
	for(i in seq(N))
	{
		score <- values[i] * pre[, i]	
	}
	score <- score / sum(values[1:N])
	# print(score)
	if (N == 1)
	{
		scores <- score
	}
	scores <- cbind(scores, score)
}

print(scores)
output_cov <- "covariance.csv"
output_evalues <- "eigen.values.csv"
output_evectors <- "eigen.vectors.csv"
output_scores <- "scores.csv"
write.csv(c.data, output_cov)
write.csv(values, output_evalues)
write.csv(vectors, output_evectors)
write.csv(scores, output_scores)
