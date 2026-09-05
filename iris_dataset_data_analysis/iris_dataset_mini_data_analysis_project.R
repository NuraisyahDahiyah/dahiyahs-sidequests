
# ------------------------------------------------------
# IRIS DATA ANALYSIS PROJECT
# ------------------------------------------------------

# 1. SETUP
library(tidyverse)

# 2. LOAD DATA
data(iris)

# 3. UNDERSTAND DATA
head(iris)
str(iris)
summary(iris)

# 4. SELECT DATA 
iris |>
  select(Species, Petal.Length, Petal.Width) # three types: setosa, versicolor, virginica

# 5. FILTER DATA
iris |>
  filter(Species == "setosa")

# 6. CREATE VARIABLES
iris |>
  mutate(
    Petal.Ratio = Petal.Length / Petal.Width
  )

# 7. SUMMARISE DATA
iris |>
  summarise(
    average_petal_length = mean(Petal.Length)
  )

# 8. GROUP DATA 
iris |>
  group_by(Species) |>
  summarise(
    average_petal_length = mean(Petal.Length),
    average_petal_width = mean(Petal.Width)
  )

# 9. VISUALISE
ggplot(iris, aes(x = Petal.Length, y = Petal.Width)) + 
  geom_point() #ggplot(DATA, aes(MAPPING))


# scatter plot - color by species
ggplot(
  iris, 
  aes(
    x = Petal.Length,
    y = Petal.Width,
    colour = Species
  )
) + 
  geom_point() # indicates the type of graph 

# choose your own color 
ggplot(
  iris, 
  aes( # which variable detrmines the color?
    x = Petal.Length,
    y = Petal.Width,
    colour = Species
  )
) + 
  geom_point(size = 2, alpha = 0.7) + # alpha controls transparency
  scale_colour_manual( # what colors to use?
    values = c(
      'setosa' = 'blue',
      'versicolor' = 'orange',
      'virginica' = 'purple'
    )
  )


# bar chart
ggplot(
  iris, 
  aes(
    x = Species,
    fill = Species # fill is inside of the shape while color is outline/edge
    )
  ) +
  geom_bar()


# bar chart (horizontal)
ggplot(
  iris, 
  aes(
    x = Species,
    fill = Species # fill is inside of the shape while color is outline/edge
  )
) +
  geom_bar() +
  coord_flip() # switches the axes

# box and whisker plot
ggplot(
  iris, 
  aes(
    x = Species, 
    y = Petal.Length,
    fill = Species
  )
) + 
  geom_boxplot() +
  scale_fill_manual(
    values = c(
      'setosa' = 'blue',
      'versicolor' = 'orange',
      'virginica' = 'purple'
    )
  )

## include actual observations on top of box plot

ggplot(
  iris,
  aes(
    x = Species,
    y = Petal.Length,
    fill = Species
  )
) +
  geom_boxplot() +
  geom_jitter(
    width = 0.1,
    alpha = 0.5
  )


# histograms

ggplot(
  iris, 
  aes(x = Petal.Length, fill = Species)
) +
  geom_histogram(
    bins = 20,
    alpha = 0.5
  )

ggplot(
  iris,
  aes(
    x = Petal.Length,
    y = Petal.Width
  )
) + 
  geom_point() +
  facet_wrap(~ Species) # creates seperate plot for each Species


## ggplot pattern
## DATA,
## aes (
##  x = VARIABLE,
##  y = VARIABLE,
##  colour = VARIABLE,
##  fill = VARIABLE
## )
##) +
## GEOMETRY()


# color = color of line / point outlines
# fill = inside color of shapes
# shape = shape of points
