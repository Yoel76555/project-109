import statistics
import pandas as pd
import csv

df= pd.read_csv("StudentsPerformance.csv")
readingScore_list = df["readingScore"].to_list()

#mean for readingScore

readingScore_mean= statistics.mean(readingScore_list)

#median for readingScore

readingScore_median= statistics.median(readingScore_list)

#mode for readingScore

readingScore_mode= statistics.mode(readingScore_list)

#printing mean, median, and mode to validate

print("Mean, Median and Mode of readingScore is {}, {} and {} respectively".format(readingScore_mean, readingScore_median, readingScore_mode))

#std deviation for readingScore

readingScore_std_deviation= statistics.stdev(readingScore_list)


#1,2,3 std deviation for readingScore

readingScore_first_std_deviation_start, readingScore_first_std_deviation_end = readingScore_mean-readingScore_std_deviation, readingScore_mean+readingScore_std_deviation
readingScore_second_std_deviation_start, readingScore_second_std_deviation_end = readingScore_mean-(2*readingScore_std_deviation), readingScore_mean+(2*readingScore_std_deviation)
readingScore_third_std_deviation_start, readingScore_third_std_deviation_end = readingScore_mean-(3*readingScore_std_deviation), readingScore_mean+(3*readingScore_std_deviation)

#Percentage of data within 1, 2 and 3 Standard Deviations for readingScore
readingScore_list_of_data_within_1_std_deviation = [result for result in readingScore_list if result > readingScore_first_std_deviation_start and result < readingScore_first_std_deviation_end]
readingScore_list_of_data_within_2_std_deviation = [result for result in readingScore_list if result > readingScore_second_std_deviation_start and result < readingScore_second_std_deviation_end]
readingScore_list_of_data_within_3_std_deviation = [result for result in readingScore_list if result > readingScore_third_std_deviation_start and result < readingScore_third_std_deviation_end]

#Printing data for readingScore (Standard Deviation)

print("{}% of data for readingScore lies within 1 standard deviation".format(len(readingScore_list_of_data_within_1_std_deviation)*100.0/len(readingScore_list)))
print("{}% of data for readingScore lies within 2 standard deviation".format(len(readingScore_list_of_data_within_2_std_deviation)*100.0/len(readingScore_list)))
print("{}% of data for readingScore lies within 3 standard deviation".format(len(readingScore_list_of_data_within_3_std_deviation)*100.0/len(readingScore_list)))





