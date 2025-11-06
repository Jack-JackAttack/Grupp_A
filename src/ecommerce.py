import pandas as pd
from .io_utiles import load_file
from .metrics import (rev_unit_count, rev_count, rev_summery_per_catagory, rev_category_per_unit, rev_summery, rev_per_category, rev_outliers)
from .viz import (revenue_per_month, revenue_per_city_viz)


class EcommerceAnalyzer:
    def __init__(self, csv_path: str):
        """
        Loading the .csv file into a dataframe, while also cleaning it from missing values.
        """
        self.df = load_file(csv_path)

    def rev_unit_count(self):
        """
        Calculates and returns total revenue and units sold per city.
        """
        return rev_unit_count(self.df)
    
    def rev_count(self):
        return rev_count(self.df)
    
    def rev_summery_per_catagory(self):
        """
        Calculates and returns mean, median, std, min and max for revenue per category.
        """
        return rev_summery_per_catagory(self.df)
    
    def rev_category_per_unit(self):
        return rev_category_per_unit(self.df)
    
    def rev_summery(self):
        return rev_summery(self.df)

    def rev_per_month_viz(self):
        """
        Calculates and plots total revenue per month.
        """
        return revenue_per_month(self.df)
    
    def rev_per_category(self):
        """
        Calculates and returns total revenue per category.
        """
        return rev_per_category(self.df)
    
    def rev_per_city_viz(self):
        """
        Visualizes revenue per city.
        """
        return revenue_per_city_viz(self.df)
    
    
    def rev_outliers(self, x:str = "units"):
        """
        Calculates and returns possible outliers through IQR-method. X-value sets column, units by default.
        """
        return rev_outliers(self.df, x)
