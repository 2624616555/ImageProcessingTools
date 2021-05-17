import rasterio
import numpy as np

def read_tif(path:str)->np.ndarray:
    dataset = rasterio.open(path)
    data = dataset.read()
    dataset.close()
    return data

def write_tif(data:np.ndarray, path:str):
    if data.ndim == 2:
        data = np.array([data])
    elif data.ndim == 3:
        pass
    else:
        print("wrong data dim!")
    new_dataset = rasterio.open(path, 'w', driver='GTiff', height=data.shape[1], width=data.shape[2], count=data.shape[0], dtype=data.dtype)
    new_dataset.write(data)
    new_dataset.close()
