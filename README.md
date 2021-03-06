# surfs_up

## Overview of the analysis:
------
For this project we analyzed weather data for the island of Oahu in Hawaii to determine if it would be a good investmet to open a surf gear and icecream store in that location. 

### Tools used:

* Jupyter Notebook
* SQLite database - hawaii.sqlite database file

## Results:
------
In the following tables you can see the results from the statistical analysis for the month of June and December. 
Three takeaway points from this analysis:

* The weather in the island of Oahu is consisten year round, with an average Temperature of 75° for the monht of june and 71° for the month of december. 
* The minimum Temperature for June is 64° and 56° for december which are pleasant temperatures for outdoors activities.  
* The value of the standard deviation is 3.25° for june and 3.74° for december, therefore we can say with certainty that the weather does not vary too much. Making the Island of Oahu a safe option to open the surf and icecream shop. 

| June Stats      |           |
|-----------------|-----------|
| count           | 1700      |
| mean            | 74.944118 |
| std             | 3.257417  |
| min             | 64        |
| 25%             | 73        |
| 50%             | 75        |
| 75%             | 77        |
| max             | 85        |

| December Stats |           |
|----------------|-----------|
| count          | 1517      |
| mean           | 71.041529 |
| std            | 3.74592   |
| min            | 56        |
| 25%            | 69        |
| 50%            | 71        |
| 75%            | 74        |
| max            | 83        |

## Summary:
------
In summary we can determine that opening a surf and icecream store in Oahu is a safe investment considering the weather. Of course there is other variables that we need to consider like the demand for this type of products, turist seasons and cost/rent of the store.  
 
### Additional queries that we could add to expand this analysis are:

* We could add a query to obtain the data for precipitation for each month.
* Add graphs to observe the behavior of the temperature through the days of the month. 
* A query that returns the statistical data for each year in the data base in order to get the temperature through out the year.
* A query that returns the seasonal statistical data to compare the weather for each season. 
