# This demonstrates the basic principle of lazy loading: loading data only when it's needed #

class LazyLoader:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = "Loaded data"
            print("Data loaded")
        return self._data

loader = LazyLoader()

# Data isn't loaded yet
print("Before loading")

# Data is loaded when accessed
print(loader.data)

# Data is already loaded, no reload occurs
print(loader.data)
