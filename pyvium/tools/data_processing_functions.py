import os
import csv
from typing import Dict, List, Union
from tqdm import tqdm

from ..util import get_file_list


class DataProcessing:
    @staticmethod
    def export_to_csv(data, file_path) -> None:
        """Saves data on a .csv file."""
        path = os.path.normpath(file_path)
        with open(path, "w", encoding="UTF-8") as f:
            write = csv.writer(f)
            write.writerows(data)

    @staticmethod
    def get_idf_data(
        idf_path: str, include: List[str] = []
    ) -> Union[List[List[int]], Dict[str, List[List[int]]]]:
        data = {"primary_data": []}

        # open and read idf file
        with open(idf_path, "r", encoding="ISO-8859-2") as idf:
            raw_data = idf.read()

        # split the file into a list of lines
        lines = raw_data.splitlines()

        def extract_data_section(start_index: int) -> List[List[int]]:
            section_data = []
            num_points = int(lines[start_index + 2])
            start = start_index + 3
            end = start + num_points
            for line_index in range(start, end):
                row = lines[line_index].split()
                datapoint = [eval(value) for value in row]
                section_data.append(datapoint)
            return section_data, end

        def extract_osc_data(start_index: int) -> List[List[int]]:
            section_data = []
            num_sections = int(lines[start_index + 1])
            start = start_index + 1
            for _ in range(num_sections):
                section, end = extract_data_section(int(start))
                section_data.append(section)
                start = end - 1
            return section_data

        for index, line in enumerate(lines):
            if "primary_data" in line:
                data["primary_data"].extend(extract_data_section(index))
            elif "ocp" in include and "ocpdata" in line:
                data["ocpdata"] = extract_data_section(index)
            elif "pretreatment" in include and "pretreatmentdata" in line:
                data["pretreatmentdata"] = extract_data_section(index)
            elif "rc" in include and "RsCs_data" in line:
                data["RsCs_data"] = extract_data_section(index)
            elif "osc" in include and "osc_data" in line:
                data["osc_data"] = extract_osc_data(index)

        if len(include) == 0:
            return data["primary_data"]

        return data

    @staticmethod
    def convert_idf_to_csv(idf_path) -> None:
        """Extracts the data from a ivium .idf file and saves the data to a .csv file"""
        path = os.path.normpath(rf"{idf_path}")
        data = DataProcessing.get_idf_data(path)
        DataProcessing.export_to_csv(data, path + ".csv")

    @staticmethod
    def convert_idf_dir_to_csv(idf_dir_path=".") -> Dict[str, Union[int, List[str]]]:
        """Extracts the data of all .idf files on a directory and saves the data .csv files"""
        path = os.path.normpath(idf_dir_path)
        files = get_file_list(path)
        idf_files = list(filter(lambda file: (file[-4:] == ".idf"), files))
        converted_count = 0
        errors = []
        for idf_filename in tqdm(idf_files):
            try:
                DataProcessing.convert_idf_to_csv(path + "\\" + idf_filename)
                converted_count += 1
            except Exception:
                errors.append(idf_filename)

        return {
            "converted_count": converted_count,
            "error_count": len(errors),
            "errors": errors,
        }
