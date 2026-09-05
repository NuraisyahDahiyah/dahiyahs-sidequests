Iris Dataset Mini Data Analysis Project
================
Dahiyah Hashim
2026-09-05

# Introduction

As part of my journey in learning how to use R for statistical analysis
and machine learning, I decided to start off with a mini data analysis
project using the classic **Iris dataset** to explore variations in
petal measurements across three species: setosa, versicolor, and
virginica.

The main objective of this project is to mainly familiarise myself with
R and how to use it!

## Data Exploration and Summary

First, we load the dataset and view its basic structure and summary
statistics.

``` r
data(iris)
head(iris)
```

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

``` r
summary(iris)
```

    ##   Sepal.Length    Sepal.Width     Petal.Length    Petal.Width   
    ##  Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100  
    ##  1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300  
    ##  Median :5.800   Median :3.000   Median :4.350   Median :1.300  
    ##  Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199  
    ##  3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800  
    ##  Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500  
    ##        Species  
    ##  setosa    :50  
    ##  versicolor:50  
    ##  virginica :50  
    ##                 
    ##                 
    ## 

## Key Visualisations

### Petal Length vs. Petal Width

We can visualise how petal dimensions relate across different species
using a scatter plot with custom colours:

``` r
ggplot(
  iris, 
  aes(
    x = Petal.Length,
    y = Petal.Width,
    colour = Species
  )
) + 
  geom_point(size = 2, alpha = 0.7) + 
  scale_colour_manual(
    values = c(
      'setosa' = 'blue',
      'versicolor' = 'orange',
      'virginica' = 'purple'
    )
  )
```

![](iris_dataset_data_analysis_files/figure-gfm/scatterplot-data-1.png)<!-- -->

**Observation:** Setosa petals are significantly smaller in both length
and width compared to Versicolor and Virginica.

### Distribution of Petal Length

Next, we examine the distribution of petal lengths across each species
using a box plot overlaid with individual data points:

``` r
ggplot(
  iris,
  aes(
    x = Species,
    y = Petal.Length,
    fill = Species
  )
) +
  geom_boxplot() +
  geom_jitter(width = 0.1, alpha = 0.5) +
  scale_fill_manual(
    values = c(
      'setosa' = 'blue',
      'versicolor' = 'orange',
      'virginica' = 'purple'
    )
  )
```

![](iris_dataset_data_analysis_files/figure-gfm/boxplot-data-1.png)<!-- -->

**Observation:** Setosa has significantly shorter and tightly clustered
petal lengths (~1–2 cm), while versicolor and virginica show higher
median petal lengths with slightly more variability.
