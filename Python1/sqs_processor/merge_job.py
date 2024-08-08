class MergeJob:
    def __init__(self,message) -> None:
        self.message = message
        self.__validate_message()
    def __validate_message(self):
        if 'destination' not in self.message:
            raise ValueError(f"Missing required field 'destination' in message.")
    def __create_temporary_table():
        True
    def __merge_temp_table():
        True
    def process(self) -> bool:
        self.__create_temporary_table()
        self.__merge_temp_table()