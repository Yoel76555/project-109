import statistics
import pandas as pd
import csv

df= pd.read_csv("StudentsPerformance.csv")
writingScore_list = df["writingScore"].to_list()

#mean for writingScore

writingScore_mean= statistics.mean(writingScore_list)

#median for writingScore

writingScore_median= statistics.median(writingScore_list)

#mode for writingScore

writingScore_mode= statistics.mode(writingScore_list)

#printing mean, median, and mode to validate

print("Mean, Median and Mode of writingScore is {}, {} and {} respectively".format(writingScore_mean, writingScore_median, writingScore_mode))

#std deviation for writingScore

writingScore_std_deviation= statistics.stdev(writingScore_list)


#1,2,3 std deviation for writingScore

writingScore_first_std_deviation_start, writingScore_first_std_deviation_end = writingScore_mean-writingScore_std_deviation, writingScore_mean+writingScore_std_deviation
writingScore_second_std_deviation_start, writingScore_second_std_deviation_end = writingScore_mean-(2*writingScore_std_deviation), writingScore_mean+(2*writingScore_std_deviation)
writingScore_third_std_deviation_start, writingScore_third_std_deviation_end = writingScore_mean-(3*writingScore_std_deviation), writingScore_mean+(3*writingScore_std_deviation)

#Percentage of data within 1, 2 and 3 Standard Deviations for writingScore
writingScore_list_of_data_within_1_std_deviation = [result for result in writingScore_list if result > writingScore_first_std_deviation_start and result < writingScore_first_std_deviation_end]
writingScore_list_of_data_within_2_std_deviation = [result for result in writingScore_list if result > writingScore_second_std_deviation_start and result < writingScore_second_std_deviation_end]
writingScore_list_of_data_within_3_std_deviation = [result for result in writingScore_list if result > writingScore_third_std_deviation_start and result < writingScore_third_std_deviation_end]

#Printing data for writingScore (Standard Deviation)

print("{}% of data for writingScore lies within 1 standard deviation".format(len(writingScore_list_of_data_within_1_std_deviation)*100.0/len(writingScore_list)))
print("{}% of data for writingScore lies within 2 standard deviation".format(len(writingScore_list_of_data_within_2_std_deviation)*100.0/len(writingScore_list)))
print("{}% of data for writingScore lies within 3 standard deviation".format(len(writingScore_list_of_data_within_3_std_deviation)*100.0/len(writingScore_list)))





