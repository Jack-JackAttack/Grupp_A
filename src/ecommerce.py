import pandas as pd
from .io_utiles import load_file
from .metrics import (rev_unit_count,rev_unit_count, rev_per_category)
from .viz import (revenue_per_month, revenue_per_city_viz)


class EcommerceAnalyzer:
    def __init__(self, csv_path: str):
        self.df = load_file(csv_path)

    def rev_unit_count(self):
        return rev_unit_count(self.df)
    
    def rev_per_month_viz(self):
        return revenue_per_month(self.df)
    
    def rev_per_category(self):
        return rev_per_category(self.df)
    
    def rev_per_city_viz(self):
        return revenue_per_city_viz(self.df)
    
    
    
