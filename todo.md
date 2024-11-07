To do list:

1. Data loading

- figure out if what files to use for the initial data (ct,text,...)

- open the file and read in the data

- add tests to see if any error is encountered 

2. Data formatting

- Make sure the data is formatted in a structured manner

- identify what is household genes and what are the analyzed genes (user input?)

3. Analysis

- check if the number of data is correct, aka same number for repeats, controls, etc..

- perform the calculations to see gene expression level

4. Stats

- add variance checks and report to user if variation is too high

- perform a statistical test

5. Vizualisation

- create graphs (plotly) of the expression levels 

- provide a formatted stat sheet that contains the results of the tests

6. User experience

- how are files send to be analyzed? Is it an online running piece of software through something like Flask?

- bug testing and error cases + documentation