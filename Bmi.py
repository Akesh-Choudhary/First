#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""BMI_calculator
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1_wkg9iV5TbSoNkDygc0SVVhsYnrRH2KB
"""

# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator developed by  Ratan dev yadav ')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input(" dekh kya rha hai Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
	# take height input in centimeters
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height kitna lamba hai daal idhar")

elif(status == 'meters'):
	# take height input in meters
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	# take height input in feet
	height = st.number_input('Feet')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

	# print the BMI INDEX
	st.text("yeh raha aap ka  BMI Index  {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("You are Extremely Underweight bsdk kuch kha le jake")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight khaya pia ker sala humesha acha thodi na hai")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy kitna khata hai")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight kam khaya piya ker ")
	elif(bmi >= 30):
		st.error("Extremely Overweight   kha kha ke marega kya ")

