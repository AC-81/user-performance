#!/usr/bin/python

import sklearn #importing the basic library required 

from sklearn.preprocessing import MinMaxScaler

import sys

sys.path.append("../tools/")
from data_process import get_data


user_data1 , user_id1 , problem_data1 , train_submission1 = get_data()


'''
		we have the following things with us now
		
		user_data1 : the performance of a particular user is given and some features like his/her level , problems solved etc are 			present
		submission_count , problem_solved , contribution  , follower_count  , max_rating , rating ,rank 
		
		user_id1 : it has only user id's in it and the data related to its corresponding columns in user_data
		
		problem_data : it has the description of a particular problem , i.e its id(int) and the difficulty.
		
		train_submission1 : it has 4 columns which are (all are ints)
					1) user_id 
					2) problem_id
					3) attempts_range
					4) difficulty on a scale of 1 to 14 (both included)

		

'''
user_data = (MinMaxScaler()).fit_transform(user_data1)

user_id = user_id1

train_submission[: , 3] = (MinMaxScaler()).fit_transform(train_submission1[: , 3])

'''
user_data has submission_count , problem_solved , contribution  , follower_count  , max_rating , rating ,rank (all are integers)

user_id has only user id's in it and the data related to its corresponding columns in user_data

train_submissions  has 4 columns which are (all are ints) 
					1) user_id 
					2) problem_id
					3) attempts_range
					4) difficulty on a scale of 1 to 14 (both included) (before scaling)
					in train_submission,the third column has been scaled usin the min max scaler


			
'''

print(user_data[0:5])
print(user_id[0:5])
print(train_submission[0:5])




	




