import os
import csv
from typing import Dict, List, Union
from tqdm import tqdm

from ..util import get_file_list

class DataProcessing():
    @staticmethod
    def export_to_csv(data,file_path) -> None:
        '''Saves data on a .csv file.'''
        path = os.path.normpath(file_path)
        with open(path, 'w', encoding='UTF-8') as f:
            write = csv.writer(f)
            write.writerows(data)

    @staticmethod
    def get_idf_data(idf_path) -> List[List[int]]:
        '''Extracts the data from a ivium .idf file and returns a lits of points (data matrix)'''
        data = []

        # open and read idf file
        #with open(idf_path, 'r', encoding='cp1252') as idf:
        with open(idf_path, 'r', encoding='ISO-8859-2') as idf:
            raw_data = idf.read()
    
        # split the file into a list of lines
        lines = raw_data.splitlines()
    
        for index,line in enumerate(lines):
            if 'primary_data' in line:
                datapoints = int(lines[index+2])
                start = index+3
                end = start + datapoints
                for line_index in range(start, end):
                    row = lines[line_index].split()
                    datapoint = [eval(value) for value in row]            
                    data.append(datapoint)
        return data

    @staticmethod
    def convert_idf_to_csv(idf_path) -> None:
        '''Extracts the data from a ivium .idf file and saves the data to a .csv file'''
        print(idf_path)
        path = os.path.normpath(rf'{idf_path}')
        print(path)
        data = DataProcessing.get_idf_data(path)
        DataProcessing.export_to_csv(data,path+'.csv')
    
    @staticmethod
    def convert_idf_dir_to_csv(idf_dir_path='.') -> Dict[str,Union[int,List[str]]]:
        '''Extracts the data of all .idf files on a directory and saves the data .csv files'''
        path = os.path.normpath(idf_dir_path)
        files = get_file_list(path)
        idf_files = list(filter(lambda file: (file[-4:] == '.idf'), files))
        converted_count = 0
        errors = []
        for idf_filename in tqdm(idf_files):
            try:
                DataProcessing.convert_idf_to_csv(path+'\\'+idf_filename)
                converted_count += 1
            except Exception:
                errors.append(idf_filename)

        return {"converted_count":converted_count, "error_count": len(errors),"errors":errors}

