import pandas as pd

c=["START_TIME","ELAPTIME_MINUTES","ACTIVITY","SESSION_NUMBER","ENTITY","MB","SUCCESSFUL"]
c1=["START_TIME","END_TIME","ACTIVITY","ACTIVITY_DETAILS","ACTIVITY_TYPE","NUMBER","ENTITY","AS_ENTITY","SUB_ENTITY","COMMMETH","ADDRESS","SCHEDULE_NAME","EXAMINED","AFFECTED","FAILED","BYTES","BYTES_PROTECTED","BYTES_WRITTEN","DEDUP_SAVINGS","COMP_SAVINGS","IDLE","MEDIAW","PROCESSES","COMPLETION_CODE","SUCCESSFUL","VOLUME_NAME","DRIVE_NAME","LIBRARY_NAME","LAST_USE","COMM_WAIT","NUM_OFFSITE_VOLS","INCIDENT_TYPE","ACKNOWLEDGE","CONTACT"]


b=pd.read_csv(r"C:\Users\AngelineD\Desktop\actlog VM&NON VM (2)\actlog VM&NON VM\sp_lxln2ptsm0001_Non-VMActlog_20012021_LN2_TSM_SRV01.csv",index_col=False)
b1=pd.read_csv(r"C:\Users\AngelineD\Desktop\actlog VM&NON VM (2)\actlog VM&NON VM\sp_lxln2ptsm0001_VMActlog_20012021_LN2_TSM_SRV01.csv",index_col=False)

b.columns=c
b1.columns=c1
b1