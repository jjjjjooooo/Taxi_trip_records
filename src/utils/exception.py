"""
An exception.py file is typically used to define custom exception classes in Python.
In Python, exceptions are used to handle errors and exceptional situations that may occur during program execution.
Python provides a set of built-in exception classes, but sometimes it is useful to define custom exception classes tailored to specific needs in your code.
"""

import sys


def error_message_detail(
    error, error_detail: sys
):  # error_detail is expected to be an instance of the sys module.
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self) -> str:
        return self.error_message
