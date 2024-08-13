from google.cloud import bigquery

class QueryJob:
    def __init__(self, query:str, client: bigquery.Client):
        self.__query = query
        self.__client = client
    
    def run(self) -> bool:
        #query y result son métodos vacíos que Mock simula
        query_job = self.__client.query(self.__query) #mock por defecto retorna otro mock, entonces query_job es un mock
        print(query_job.result())
        print("Query ejecutada con éxito")
        return True

def __main__():
    newInstance = QueryJob("SELECT * FROM 'project.dataset.table'", bigquery.Client("project"))