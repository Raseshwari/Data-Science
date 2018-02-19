# Data-Science
Instructions:
1.	Download the python code file – Discretization_Test.py and place the dataset file – “software-defects-cml.csv” in the same folder.
2. Link to download the sample dataset http://promise.site.uottawa.ca/SERepository/
3.	Execute the program in Pycharm.
Part 1:
Used Pandas python library for reading data from csv file. Reason for using this library is that it has various in-built functions for traversing data, calculating mean, min, max. It has the concept of dataframes in which the data is read and represented in tabular format. Also, because it has the option of creating dataframes from dictionaries and lists.
1.	The first step performed was of reading data from csv file using dataframes in pandas.
Calculated mean of each column using pandas in-built ‘mean()’ function and stored the mean of each column in a variable.
2.	Traversed the dataframe created in step 1 row wise and for each value in the columns of that row checked if the value is greater than or equal to the mean of that column. If the value is greater or equal assigned it ‘0’ value else assigned it ‘1’ value. Appended all these values of 0 and 1 to separate list created for each column.
3.	The 0,1 lists created for each column in step 2 where read using from_items() function of dataframe and a new dataframe was created representing a matrix of 0’s and 1’s.
4.	Data was completely discretized as either 0 or 1 depending on whether its greater or equal to its column’s mean.
The technique used for discretization is the simplest one because the dataset is not too huge and the values aren’t huge either. Also, the classifier column ‘defects’ is having values either 0 or 1 so decided to use the simplest discretization method. 
Part 2:
1.	Created training and target dataset into 10 equal intervals i.e., 10-fold validation for cross validation.
2.	The folds created such that training data in each fold consists of 9/10th (approximately) observations from both positive and negative classes.
3.	Calculated probabilities for each data in all the training dataset (i.e., prior probabilities)
4.	Calculated the posterior probabilities using the Naïve Bayesian formula.
5.	Compared the results of step 4 with values in target dataset and computed precision, recall, f1 and accuracy.
