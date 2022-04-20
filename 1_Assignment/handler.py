# import libs
import xml.etree.ElementTree as ET
import pandas as pd
import altair as alt

# load and check xml
# export_xml = file.read()
# file.close()
# export_xml

# create etree
tree = ET.parse('Export.xml')
# make dictionar
root = tree.getroot()
record_list = [x.attrib for x in root.iter('Record')]
# create pandas dataframe from record_list
data = pd.DataFrame(record_list)
# make dates from xml readable
for col in ['creationDate', 'startDate', 'endDate']:
    data[col] = pd.to_datetime(data[col])
# convert "value" in xml to numeric
data['value'] = pd.to_numeric(data['value'], errors='ignore')

# check DataFrame
data
# show all "type" fields for selection
data.type.unique()

# filter data for step count and value of it
steps = data.loc[data['type'] == 'HKQuantityTypeIdentifierStepCount']

datevalue = steps[['creationDate', 'value']]
# show stepcount with value 
datevalue

# dataframe from datevalue? 
