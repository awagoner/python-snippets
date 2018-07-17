import numpy as np

def float_to_zip(zip_code):
    if np.isnan(zip_code):
        return np.nan
        
    # np.isnan infers missing data/information
    # 0 makes sure to left-pad with zero
    # zip codes have 5 digits
    # .0 means, we don't want anything after the decimal
    # f is for float
    zip_code = "{:05.0f}".format(zip_code)
    return zip_code
