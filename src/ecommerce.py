import pandas as pd
from .io_utiles import (load_file,check_revenue_correct) 
from .metrics import (rev_unit_count,rev_order_id_count,per_category_revenue,rev_summery_per_catagory,rev_category_per_unit)


class EcommerceAnalyzer:
    def __init__(self, csv_path: str):
        self.df = load_file(csv_path)

    def rev_unit_count(self):
        return rev_unit_count(self.df)
    
    def rev_order_id_count(self):
        return rev_order_id_count(self.df)
    
    def per_category_revenue(self):
        return per_category_revenue(self.df)
    
    def rev_summery_per_catagory(self):
        return rev_summery_per_catagory(self.df)
    
    def rev_category_per_unit(self):
        return rev_category_per_unit(self.df)