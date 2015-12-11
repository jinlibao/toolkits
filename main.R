# Libao Jin
# December 11, 2015

# import data from .xlsx file
install.packages("xlsx")
library("xlsx")
file <- "daisy.xlsx"
data <- read.xlsx(file)

rownames(data) <- x[,1]
fact <- factanal(x[1:9], 2, scores = "Bartlett", rotation = "varimax")
disp(fact)
disp(fact$score)
