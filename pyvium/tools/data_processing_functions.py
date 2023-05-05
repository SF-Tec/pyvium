import os
import csv

def get_file_list(dir_path='.'):
    '''Obtains a list of files in a directory'''
    file_list= []
    normalized_path = os.path.normpath(dir_path)
    for path in os.listdir(normalized_path):
        if os.path.isfile(os.path.join(normalized_path, path)):
            file_list.append(path)
    
    return file_list
    

class DataProcessing():
    @staticmethod
    def export_to_csv(data,file_path):
        '''Saves data on a .csv'''
        path = os.path.normpath(file_path)
        with open(path, 'w') as f:
            write = csv.writer(f)
            write.writerows(data)

    @staticmethod
    def get_idf_data(idf_path) -> list:
        '''Extracts the data from a ivium .ids and returns a lits of points (data matrix)'''
        data = []

        with open(idf_path, 'r', encoding='cp1252') as idf:
            raw_data = idf.read()
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
    def convert_idf_to_csv(self, idf_path='.'):
        '''Extracts the data from a ivium .ids and saves the data to a .csv'''
        path = os.path.normpath(idf_path)
        data = self.get_idf_data(path)
        self.export_to_csv(data,path+'.csv')
    
    @staticmethod
    def convert_idf_dir_to_csv(self, idf_dir_path='.'):
        '''Extracts the data of all .idf files on a directory and saves the data .csv files'''
        path = os.path.normpath(idf_dir_path)
        files = get_file_list(path)
        idf_files = list(filter(lambda file: (file[-4:] == '.idf'), files))
        for idf_filename in idf_files:
            self.convert_idf_to_csv(path+'\\'+idf_filename)