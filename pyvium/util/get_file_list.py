def get_file_list(dir_path='.'):
    '''Obtains a list of files in a directory'''
    file_list= []
    normalized_path = os.path.normpath(dir_path)
    for path in os.listdir(normalized_path):
        if os.path.isfile(os.path.join(normalized_path, path)):
            file_list.append(path)
    
    return file_list