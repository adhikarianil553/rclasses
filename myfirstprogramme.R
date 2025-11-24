############################################
#        BASIC R PROGRAMMING CONCEPTS      #
############################################

# 1. VARIABLES & DATA TYPES
x <- 10              # numeric
y <- 3.14            # numeric
name <- "R"          # character
is_true <- TRUE      # logical

print(x)
print(name)
print(is_true)

# 2. VECTORS
nums <- c(1, 2, 3, 4, 5)
chars <- c("apple", "banana", "cherry")

print(nums)
print(chars)

# Accessing elements
print(nums[1])
print(chars[2:3])

# 3. SEQUENCES
seq1 <- 1:10
seq2 <- seq(0, 1, by = 0.2)

print(seq1)
print(seq2)

# 4. MATRICES
m <- matrix(1:9, nrow = 3, ncol = 3)
print(m)

# Access element (row 2, col 3)
print(m[2, 3])

# 5. DATA FRAMES
df <- data.frame(
  name = c("A", "B", "C"),
  age = c(20, 25, 30),
  score = c(89, 92, 88)
)

print(df)
print(df$age)      # access column
print(df[1, ])     # first row

# 6. BASIC FUNCTIONS
square <- function(n) {
  return(n * n)
}

print(square(5))

# 7. IF-ELSE CONDITION
x <- 10

if (x > 0) {
  print("Positive number")
} else {
  print("Zero or negative")
}

# 8. LOOPS

# For loop
for (i in 1:5) {
  print(i)
}

# While loop
count <- 1
while (count <= 5) {
  print(count)
  count <- count + 1
}

# 9. READING DATA (commented because file may not exist)
# data <- read.csv("myfile.csv")
# print(head(data))

# 10. SIMPLE PLOT
x <- 1:10
y <- x^2

plot(x, y, type = "b", col = "blue", main = "Simple Plot")

