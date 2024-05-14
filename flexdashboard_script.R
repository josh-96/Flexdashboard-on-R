system("python set_path/Surf.py")

rmarkdown::run("set_path/add_theme_scraping_project.Rmd")

library(flexdashboard)
library(readxl)
library(DT)
library(ggplot2)
library(scales)
library(plotly)
library(tidyverse)

