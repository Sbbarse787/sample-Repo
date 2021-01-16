max(5, 6, 7, 8, 9)
min(5, 6, 7, 8, 9)
sqrt(121212121)
abs(-5.6)

ceiling(5.6)
floor(5.6)



str <- "Hello  World"
str

10 >= 9
10 < 8
10 == 9

a <- 12
b <- 12

if (b < a) {
   print("b is smaller than a")
} else if (b == a) {
   print("b is equal to a")
} else {
   print("a is smaller than b")
}

x <- 30
if (x > 10) {
   print("Above 10")
   if (x > 5) {
      print("Above 5")
   }
} else if (x < 30) {
   print("smaller than 30")
}

a <- 200
b <- 7
c <- 100

if (a > b & b < c & c > a) {
   print("You are right")
} else {
   print("You are wrong")
}

i <- 6

while (i < 100) {
   if (i == 61) {
      break
   }
   i <- i + 5
   if (i == 11) {
      next
   }
   print(i)
}

for (x in 1:10) {
   print(x)
}


fruits <- list("apple", "fruits", "cherry")
for (x in fruits) {
   if (x == "fruits") {
      next
   } else {
      print(x)
   }
}

dice <- 1:10

for (x in dice) {
   if (x == 6) {
      print("Hit ")
   } else {
      print("mis")
   }
}

func <- function(country, state) {
   cat("I am from", country, "state ,", state)
}
func("India", "maharashtra")

funcs <- function(x) {
   return(5 * x)
}
print(funcs(3))


# !This is Vectors

fruits <- c("banana", "Grapes", "Apple", "mango", "lemon")
print(fruits)
sort(fruits)
fruits[c(-1)]

fruits[1] <- "pears"
print(fruits)
print(length(fruits))

repeat_time <- rep(c(1, 2, 3), times = c(5, 2, 1))
print(repeat_time)

numbers <- seq(from = 0, to = 100, by = 10)
print(numbers)

thelist <- list("apple", "banana", "grapes")
print(thelist[1])

thelist[1] <- "blackberry"
print(thelist)

print(length(thelist))


"banana" %in% thelist
"grapes" %in% thelist

append(thelist, "Orange", after = 4)
print(thelist)

(thelist)[1:3]

list1 <- list("a", "b", "c")
list2 <- list(1, 2, 3)
list3 <- c(list1, list2)
print(list3)


# ? Matrix

Matrix <- matrix(data = c(1, 2, 3, 4, 5, 6, 7, 8), nrow = 4, ncol = 2, byrow = TRUE)
print(Matrix)


outMatrix <- matrix(data = list("Apple", "Grapes", "banana", "cherry"), nrow = 2, ncol = 2)
print(outMatrix)
print(outMatrix[, 1])

newmatrix <- cbind(outMatrix, c("strawberry", "blueberry"))
print(newmatrix)


newmatrix1 <- rbind(newmatrix, c("Mutton", "chicken"))
print(newmatrix1)

"Mutton" %in% newmatrix1

newmatrix2 <- newmatrix1[-c(1), -c(1)]
print(newmatrix2)

dim(newmatrix2)

Matrix1 <- matrix(c("apple", "banana", "cherry", "grape"), nrow = 2, ncol = 2)
Matrix2 <- matrix(c("orange", "mango", "pineapple", "watermelon"), nrow = 2, ncol = 2)
Matrix_Combined <- rbind(Matrix1, Matrix2)
Matrix_Combined

Matrix_Combined <- rbind(Matrix1, Matrix2)
Matrix_Combined


thisarray <- c(1:24)
multiarray <- array(thisarray, dim = c(4, 3, 4))
multiarray

for (x in multiarray) {
   print(x)
}

2 %in% multiarray
dim(multiarray)
length(multiarray)

Data_Frame <- data.frame(
   Training = c("Strength", "Stamina", "Other"),
   Pulse = c(100, 150, 120),
   Duration = c(60, 30, 45)
)

Data_Frame
summary(Data_Frame)

music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))
music_genre