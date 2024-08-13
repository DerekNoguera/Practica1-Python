import pytest
from unittest.mock import Mock, patch
from mock import QueryJob

@pytest.fixture
def client_mock():
    with patch('google.cloud.bigquery.Client', Mock()) as client: # Reemplazar la clase Client por un Mock
        return client
    
def test_query_job_run(client_mock):
    query = "SElECT * FROM 'project.dataset.table'"
    client_mock.return_value.query.return_value.result.return_value = "Success" #result retorna "Success"
    client_mock.return_value.query.return_value.result.side_effect = Exception() #result levanta una Excepción
    query_job = QueryJob(query, client_mock("project"))
    # query_job.run()
    with pytest.raises(Exception):
        query_job.run()
    
    client_mock.assert_called_once_with("project")
    client_mock.return_value.query.assert_called_once_with(query)
    client_mock.return_value.query.return_value.result.assert_called()