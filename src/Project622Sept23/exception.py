import sys
from src.Project622Sept23.logger import logging


def error_message_detail(error, error_detail:sys):
    _._exc_tb= error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in file: {filename} at line number: {exc_tb.tb_lineno} with error message: {error}"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(self.error_message)
        self.error_message = error_message_detail(error, error_detail)

def __str__(self):
    return self.error_message
        
