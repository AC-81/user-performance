#!/usr/bin/python

import csv
import numpy as np
from sklearn.preprocessing import StandardScaler
def usernum_to_num(user_id):
	for i in range(0,len(user_id)):
		user_id[i] = (user_id[i])[5:]

	return user_id

def probid_to_id(problem_data):
	for i in range(0,len(problem_data)):
		problem_data[i , 0 ] = float((problem_data[i , 0 ])[5:])

	return problem_data


def prid_to_id(problem_data):
	for i in range(0,len(problem_data)):
		problem_data[i , 1 ] = float((problem_data[i , 1 ])[5:])

	return problem_data


def get_data(user_data = "../tools/user_data.csv" , problem_data = "../tools/problem_data.csv" , train_submission = "../tools/train_submissions.csv"):
	'''
	user_data has 11 columns in the following order
	user_id , submission_count , problem_solved , contribution , country , follower_count , last_online_time_seconds , max_rating , rating ,
	rank , registration_time_seconds

	problem_data has 4 columns in the following order
 	problem_id , level_type(between A TO N) , points , tags

		
	train_submission has 3 columns in the following order
	user_id , problem_id , attempts_range 
	
	
	'''
	
	
	user_data = (np.array(list(csv.reader(open( user_data ,'r'))) ))[1:100 , : ]
	
	problem_data = (np.array(list(csv.reader(open( problem_data ,'r')))))[1:100 , : ]
	
	train_submission = (np.array(list(csv.reader(open( train_submission ,'r')))))[1:100 , : ]

	#print(user_data[0:5])
	
	#print(problem_data[0:5])

	#print(train_submission[0:5])
	
	user_id = user_data[: , 0] #user_(a number)
	user_id = usernum_to_num(user_id) # a list of ints
	
	
		
	user_data1 = user_data[ : , [1,2,3,5,7,8,9]] # removed some irrelevant features
	
	problem_data1 = problem_data[: , [0,1]] # there is not much use of points and tags as points and level_type are nearly similar.
						# thers is only problem_id and level_type in problem_data1 
	
	problem_diff = np.zeros( (len(train_submission),1) , dtype=int )
	
	train_submission1 = np.append(train_submission , problem_diff , axis=1) 

	'''
	now train_submission1 has the following structure 
		user_id , problem_id, attempts_range , (a column with zeros)	
	'''

	for i in range(0,len(user_data1)):
		if user_data1[i , 6]  == 'beginner':
			user_data1[i , 6] = 1
		elif user_data1[i , 6]  == 'intermediate':
			user_data1[i , 6] = 2
		elif user_data1[i , 6]  == 'advanced':
			user_data1[i , 6] = 3
		elif user_data1[i , 6]  == 'expert':
			user_data1[i , 6] = 4
		
	user_data1 = user_data1.astype(np.float)
	print("prob data",problem_data1[0:10 , 0] )
	print("trainsub",train_submission[0:10 , 1] )
	print("user_data",user_data1[0:10 , 6] )
	print(len(problem_data1))
	print(len(train_submission))
	for i in range(0,len(problem_data1)):
		for j in range(0,len(train_submission)):
			if train_submission[j , 1] == problem_data1[i , 0]:
				if problem_data1[i , 1] == 'A':
					train_submission1[j , 3] = 1
				elif problem_data1[i , 1] == 'B':
					train_submission1[j , 3] = 2
				elif problem_data1[i , 1] == 'C':
					train_submission1[j , 3] = 3
				elif problem_data1[i , 1] == 'D':
					train_submission1[j , 3] = 4
				elif problem_data1[i , 1] == 'E':
					train_submission1[j , 3] = 5
				elif problem_data1[i , 1] == 'F':
					train_submission1[j , 3] = 6
				elif problem_data1[i , 1] == 'G':
					train_submission1[j , 3] = 7
				elif problem_data1[i , 1] == 'H':
					train_submission1[j , 3] = 8
				elif problem_data1[i , 1] == 'I':
					train_submission1[j , 3] = 9
				elif problem_data1[i , 1] == 'J':
					train_submission1[j , 3] = 10
				elif problem_data1[i , 1] == 'K':
					train_submission1[j , 3] = 11
				elif problem_data1[i , 1] == 'L':
					train_submission1[j , 3] = 12
				elif problem_data1[i , 1] == 'M':
					train_submission1[j , 3] = 13
				elif problem_data1[i , 1] == 'N':
					train_submission1[j , 3] = 14



	
	problem_data1 = probid_to_id(problem_data1)
	train_submission1 = probid_to_id(train_submission1)
	train_submission1 = prid_to_id(train_submission1)
	train_submission1 = train_submission1.astype(np.float)

	print("the third row", train_submission1[0:20 , 3 ])


	'''
		AFTER completion of this code snippet 
		we have the following things with us 
		
		user_data : the data of a particular user that how well he has been doing till now. 
		
		user_id : it has only user id's in it and the data related to its corresponding columns in user_data
		
			
		problem_data1 : it has the description of a particular problem , i.e its id and the difficulty.
		
		train_submission1 : it has 4 columns which are 
					1) user_id (float)
					2) problem_id(float)
					3) attempts_range(float)
					4) difficulty on a scale of 1 to 14 (both included)(float)

		

	'''
	
				
	return user_data1 , user_id , problem_data1 , train_submission1	

	
