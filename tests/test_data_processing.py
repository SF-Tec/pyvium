import os
import pytest
from pyvium.tools.data_processing_functions import DataProcessing

def test_get_all_idf_data():
    # Arrange
    test_file = os.path.join(os.path.dirname(__file__), "data", "test_open.idf")
    
    # Act
    result = DataProcessing.get_all_idf_data(test_file)
    
    # Assert
    assert isinstance(result, dict)
    assert "primary_data" in result
    assert "ocpdata" in result
    assert "osc_data" in result
    
    # Check primary_data structure
    assert len(result["primary_data"]) == 34  # From the actual file
    assert len(result["primary_data"][0]) == 3
    
    # Check ocpdata structure
    assert len(result["ocpdata"]) == 121  # From the actual file
    assert len(result["ocpdata"][0]) == 3
    
    # Check osc_data structure
    assert len(result["osc_data"]) == 34  # From the actual file
    assert isinstance(result["osc_data"][0], list)
    assert isinstance(result["osc_data"][0][0], list)

def test_get_all_idf_data_eis():
    # Arrange
    test_file = os.path.join(os.path.dirname(__file__), "data", "eis_test.idf")
    
    # Act
    result = DataProcessing.get_all_idf_data(test_file)
    
    # Assert
    assert isinstance(result, dict)
    assert "primary_data" in result
    assert len(result["primary_data"]) > 0
    
    if "osc_data" in result:
        assert isinstance(result["osc_data"], list)
        for section in result["osc_data"]:
            assert isinstance(section, list)
            for measurement in section:
                assert isinstance(measurement, list)

def test_get_idf_data():
    # Arrange
    test_file = os.path.join(os.path.dirname(__file__), "data", "test_open.idf")
    
    # Act
    result = DataProcessing.get_idf_data(test_file)
    
    # Assert
    assert isinstance(result, list)
    assert len(result) == 34  # From the actual file
    assert all(isinstance(row, list) for row in result)
    assert all(isinstance(val, float) for row in result for val in row)

def test_get_all_idf_data_file_not_found():
    # Act & Assert
    with pytest.raises(FileNotFoundError):
        DataProcessing.get_all_idf_data("nonexistent_file.idf")

def test_get_all_idf_data_with_corrupted_file(tmp_path):
    # Arrange
    corrupted_content = """
primary_data
invalid_data_format
some garbage data
"""
    corrupted_file = tmp_path / "corrupted.idf"
    corrupted_file.write_text(corrupted_content, encoding="ISO-8859-2")
    
    # Act
    result = DataProcessing.get_all_idf_data(str(corrupted_file))
    
    # Assert
    assert isinstance(result, dict)
    assert "primary_data" in result
    assert result["primary_data"] == []  # Should return empty list for corrupted data


@pytest.fixture
def data_dir():
    return os.path.join(os.path.dirname(__file__), "data")

def test_get_all_idf_data_eis_file(data_dir):
    """Test parsing of real EIS (Electrochemical Impedance Spectroscopy) data file"""
    # Arrange
    eis_file = os.path.join(data_dir, "eis_test.idf")
    
    # Act
    result = DataProcessing.get_all_idf_data(eis_file)
    
    # Assert
    assert isinstance(result, dict)
    assert "primary_data" in result
    assert "osc_data" in result
    
    # EIS files should have oscillation data
    assert len(result["osc_data"]) > 0
    
    # Each oscillation section should be properly structured
    for section in result["osc_data"]:
        assert isinstance(section, list)
        assert len(section) > 0
        for measurement in section:
            assert isinstance(measurement, list)
            assert all(isinstance(value, float) for value in measurement)

def test_get_all_idf_data_open_file(data_dir):
    """Test parsing of general test data file"""
    # Arrange
    test_file = os.path.join(data_dir, "test_open.idf")
    
    # Act
    result = DataProcessing.get_all_idf_data(test_file)
    
    # Assert
    assert isinstance(result, dict)
    assert "primary_data" in result
    
    # Verify primary data structure
    assert len(result["primary_data"]) > 0
    for measurement in result["primary_data"]:
        assert isinstance(measurement, list)
        assert all(isinstance(value, float) for value in measurement)
    
    # Check data consistency
    first_measurement = result["primary_data"][0]
    assert len(first_measurement) > 0  # Should have at least one value
    
    # If present, check other data sections
    for section in ["ocpdata", "RsCs_data", "pretreatmentdata"]:
        if section in result:
            assert isinstance(result[section], list)
            if result[section]:  # If section is not empty
                assert all(isinstance(measurement, list) for measurement in result[section])
                assert all(isinstance(value, float) 
                         for measurement in result[section] 
                         for value in measurement)

def test_get_all_idf_data_performance(data_dir):
    """Test performance with real data files"""
    import time
    
    # Arrange
    eis_file = os.path.join(data_dir, "eis_test.idf")
    test_file = os.path.join(data_dir, "test_open.idf")
    
    # Act & Assert
    start_time = time.time()
    
    # Process both files
    result_eis = DataProcessing.get_all_idf_data(eis_file)
    result_test = DataProcessing.get_all_idf_data(test_file)
    
    end_time = time.time()
    processing_time = end_time - start_time
    
    # Performance assertions
    assert processing_time < 2.0  # Should process both files in under 2 seconds
    
    # Verify both results are properly structured
    assert isinstance(result_eis, dict)
    assert isinstance(result_test, dict)
    assert "primary_data" in result_eis
    assert "primary_data" in result_test

def test_get_all_idf_data_memory_usage(data_dir):
    """Test memory efficiency with real data files"""
    import psutil
    import os as os_lib
    
    # Arrange
    process = psutil.Process(os_lib.getpid())
    initial_memory = process.memory_info().rss
    test_file = os.path.join(data_dir, "test_open.idf")
    
    # Act
    result = DataProcessing.get_all_idf_data(test_file)
    
    # Assert
    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory
    
    # Memory usage should be reasonable (less than 100MB increase)
    assert memory_increase < 100 * 1024 * 1024  # 100MB in bytes
    
    # Verify data was actually loaded
    assert len(result["primary_data"]) > 0 