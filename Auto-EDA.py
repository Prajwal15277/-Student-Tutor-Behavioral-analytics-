# Load the Data
import pandas as pd

df = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\DA_Project\Data\ba_table.csv")

# Auto EDA
# ---------
# Sweetviz
# Autoviz
# Dtale
# Pandas Profiling
# Dataprep


# Sweetviz
###########
#pip install sweetviz
import sweetviz as sv

s = sv.analyze(df)
s.show_html()


# Autoviz
###########
#pip install autoviz
from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
#a = av.AutoViz(r"C:\Users\User\OneDrive\Desktop\DA_Project\Data\ba_table.csv", chart_format = 'html')

import matplotlib.pyplot as plt
%matplotlib inline
filename = (r"C:\Users\User\OneDrive\Desktop\DA_Project\Data\ba_table.csv")
dft = av.AutoViz(r"C:\Users\User\OneDrive\Desktop\DA_Project\Data\ba_table.csv", sep = ",")
            
import os
os.getcwd()



# D-Tale
########

 # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
#pip install dtale
import dtale
import pandas as pd

df = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\DA_Project\Data\ba_table.csv")

d = dtale.show(df)
d.open_browser()


# Pandas Profiling
###################

#pip install pandas_profiling
from pandas_profiling import ProfileReport 

p = ProfileReport(df)
p
p.to_file("output.html")

import os
os.getcwd()

# Dataprep
##########

#pip install dataprep
from dataprep.eda import create_report

report = create_report(df, title = 'My Report')

report.show_browser()


