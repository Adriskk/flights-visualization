

class ModelCannotSaveException(Exception):
    """ Model is not save-able in a file set in config file """

    def __init__(self, filename):
        self.filename = filename
        self.message = f"Cannot save a model in {self.filename} file"
        super().__init__(self.message)


