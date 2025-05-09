import sys
from src.logger import logger  # Import your custom logger

def error_message_detail(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script name [{0}] at line number [{1}] with error message: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call base class constructor
        super().__init__(error_message)
        # Generate detailed message
        self.error_message = error_message_detail(error_message, error_detail)
        # Log the error message to your log file
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise ZeroDivisionError
    except Exception as e:
        raise CustomException(e, sys)
