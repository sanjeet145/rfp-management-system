from flask import jsonify
from config.logger import logging
class ExceptionHandler(Exception):
    def __init__(self, error_message, error_details):
        self.error_message= error_message
        _,_,exc_tb = error_details.exc_info()
        self.line_no =exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        log = f"{self.file_name}, line number {self.line_no}, error_message {str(self.error_message)}"
        logging.exception(log)
    def to_response(self):
        return jsonify({"message": "Something went wrong"}), 500
    def __str__(self):
        return f"{self.file_name}, line {self.line_no}: {self.error_message}"
    
