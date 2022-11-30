# Vertical Force Test Record (FP_QA_VerticalForceTestRecord.py)

Before each data collection involving force plates in our gait lab, we perform a quick and simple ‘spot check’ in which an individual stands still on each plate to verify the X.Y,Z force outputs  are as expected. The individual’s mass is measured on calibrated scales. 

|![image](https://user-images.githubusercontent.com/50867224/204856084-ddea73a0-1236-4a65-82c1-a2b1a9ab0436.png)|
|:--:|
| <b>Daily Vertical Force ‘spot check’: Subject stands still on each plate</b>|



This Python program produces graphical representation of the long term results of the daily spot check to enable visualisation of any drift of force output accuracy over time. We have been using 4 piezoelectric BTS plates since 2013.
The program reads the test record data from a .csv  file, with each plate’s mean x, y and z force outputs over the duration of static standing period recorded for a known subject mass on a particular day. A limited data set is  given here as an example and the .csv file is provided in the repository.

 |![image](https://user-images.githubusercontent.com/50867224/204856160-377ed5f5-dc70-496f-8c5e-eb4176dd4788.png)|
 |:--:|
| <b>Raw csv file containing force plate outputs for each test date. We have 4 force plates in our lab so x, y,z force data is included for plates FP1 – FP4</b>|




‘Pandas’ is used to read the existing .csv  file to a dataframe and carry out some manipulation such as converting known load in Kg to Newtons and then calculate output forces as percentage of the known vertical load.

|![image](https://user-images.githubusercontent.com/50867224/204856230-d23449d0-88fa-4c92-ac8a-52585be9fadd.png) |
|:--:|
| <b>csv file converted to dataframe format</b>|




The graphical output is produced using ‘Matplotlib’. It displays output as percentage of known vertical load, so should equal the subject’s weight for Fy and be close to zero for Fz and Fx.

|![image](https://user-images.githubusercontent.com/50867224/204856362-26c12af1-a53c-4984-b348-cf9830519335.png)|
|:--:|
| <b>Final Graphical Output</b>|

 

 


