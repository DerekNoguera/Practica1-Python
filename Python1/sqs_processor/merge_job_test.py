import pytest
from merge_job import MergeJob

def test_merge_job_initialization_with_valid_message():
    message = {
        "type": "merge",
        "sources": ["dataset.table", "dataset.table2"],
        "destination": "dataset.dest_table"
    }
    merge_job = MergeJob(message)
    assert merge_job is not None
    
def test_merge_job_intialization_with_invalid_message():
    message = {
        "type":"merge", 
        "sources": ["dataset.table", "dataset2.table"]}
    
    with pytest.raises(ValueError) as e:
        MergeJob(message)
        
    assert str(e.value) == "Missing required field 'destination' in message."
    
def  test_process_dataset_mismatch():
    True
def  test_process_destination_table_not_exists():
    True
def  test_process_success():
    
    True