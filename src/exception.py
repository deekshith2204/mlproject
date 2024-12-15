import sys
import logging
def error_messege_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exe_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_messege="error is occured in python script[{0}] line number[{1}] error messege[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
        
    return error_messege

    

class CustomException(Exception):
    def __init__(self,error_messege,error_detial:sys):
        super().__init__(error_messege)
        self.error_messege=error_messege_detail(error_messege,error_detial=error_detial)

    def __str__(self):
        return self.error_messege
    

    