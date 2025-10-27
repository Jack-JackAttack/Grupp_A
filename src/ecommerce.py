import pandas as pd
from .io_utiles import load_file
from .metrics import (rev_unit_count)

class EcommerceAnalyzer:
    def __init__(self, csv_path: str):
        self.df = load_file(csv_path)

    def rev_unit_count(self):
        return rev_unit_count(self.df)
    
    def rev_per_category(self):
        return NotImplemented
    
