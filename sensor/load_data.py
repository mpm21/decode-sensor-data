import os
import glob
import csv
# to parse data
def load_sensor_data():
        sensor_data=[]
        sensor_files=glob.glob(os.path.join(os.getcwd(),"datasets","*.csv")) # sensor data file management
        for sensor_file in sensor_files:
            with open(sensor_file) as data_file:
                data_reader = csv.DictReader(data_file,delimiter=',') # read the data files
                for row in data_reader:
                    sensor_data.append(row)         # load data records
        return sensor_data