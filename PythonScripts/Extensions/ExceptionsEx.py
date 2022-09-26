# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class HTTPAccessDeniedException(Error):
    """Website returned an error when retrieving html data. Error received for ${response}""" 
    pass

class HTTPFaultException(Error):
    """Website returned an error when retrieving html data. Error received for ${response}""" 
    pass

class FilePathNotCorrectException(str):
    "Check that the file path is correct. Error received for path: ${str}."
    pass

class DirectoryNotFoundException(str):
    "Check that the file path is correct. Error received for path: ${str}."
    pass

class ModuleNotLocatedError(str):
    "Check that the file path is correct and module name is correct. Error received for path: ${str}."
    pass