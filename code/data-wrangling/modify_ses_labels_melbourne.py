import os
import pandas as pd

# Load, add sub-labels, set sub as index
tsv = pd.read_csv("participants.tsv", sep="\t")
tsv.set_index('participant_id', inplace=True)

for sub in tsv.index:
    first_ses = tsv.loc[sub]['first_session']

    if first_ses == "NN":
        ses_labs = {"ses-nn" : "ses-bl", "ses-sd" : "ses-sd"}
    else:
        ses_labs = {"ses-sd" : "ses-sd", "ses-nn" : "ses-bl"}
    
    for ses in ["ses-nn", "ses-sd"]:
        old_scan = f"{sub}/{ses}/anat/{sub}_{ses}_T1w.nii.gz"
        new_scan = f"{sub}/{ses}/anat/{sub}_{ses_labs[ses]}_T1w.nii.gz"
        
        if os.path.exists(old_scan) and not os.path.exists(new_scan):
            print(f"{old_scan} >>> {new_scan}")
            os.rename(old_scan, new_scan)
        else:
            print(f"{new_scan} exists. Skipping...")
        
        old_dir = f"{sub}/{ses}"
        new_dir = f"{sub}/{ses_labs[ses]}"

        if os.path.exists(old_dir) and not os.path.exists(new_dir):
            print(f"{old_dir} >>> {new_dir}")
            os.rename(old_dir, new_dir)
        else:
            print(f"{new_dir} exists. Skipping...")

