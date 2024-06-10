import os
import pandas as pd
import numpy as np
#Change participants.tsv for the Melbourne dataset

# Load two behavioral excel files
demo = pd.read_excel("sourcedata/BehaviouralData.xlsx", sheet_name="Demographics")
demo['Code'] = "sub-" + demo['Code'].apply(str)
demo.set_index('Code', inplace=True)

sleep = pd.read_excel("sourcedata/Behaviour.xlsx")
sleep.drop(range(19,26), axis=0, inplace=True) # Remove empty rows
sleep['Subject'] = "sub-" + sleep['Subject'].apply(int).apply(str)
sleep.set_index('Subject', inplace=True)

task = pd.read_excel("sourcedata/BehaviouralData.xlsx", sheet_name="ResponseinSetTask")
task['Subject number'] = "sub-" + task['Subject number'].apply(str)
task.set_index('Subject number', inplace=True)

# Load, set sub as index
tsv = pd.DataFrame()
tsv['participant_id'] = sleep.index
tsv.set_index('participant_id', inplace=True)

# Demographics
tsv['age'] = demo['Age']
tsv['sex'] = demo['Sex']
tsv['group'] = 3
tsv['site'] = "Melbourne"

# Sleep data
tsv['psqi_score'] = sleep['Global PSI']
tsv['kss_score_baseline'] = sleep['KSS NSD']
tsv['kss_score_sd'] = sleep['KSS SD']

# Task data
tsv['pvt_meanrt_baseline'] = task['NSD Total reaction time']
tsv['pvt_meanrt_sd'] = task['SD Total reaction time']

# First session
tsv['first_session'] = task['1st Session']
tsv.loc[tsv["first_session"] == "NSD", "first_session"] = "NN"

# Chronotype
tsv['chronotype'] = sleep['MEQ']
tsv.loc[tsv["chronotype"].between(16,41), "chronotype"] = 2 # Evening
tsv.loc[tsv["chronotype"].between(42,58), "chronotype"] = 3 # Intermediate
tsv.loc[tsv["chronotype"].between(59,86), "chronotype"] = 1 # Morning

# Save in dataset folder
tsv.to_csv("participants.tsv", sep="\t", na_rep="n/a")