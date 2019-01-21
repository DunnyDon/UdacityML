def featureScaling(arr):
    min_val = min(arr)
    denom =float(max(arr) - min_val)
    if denom == 0:
        return [0.5] * len(arr)
        
    rescale_arr = []
    for i in arr:
        rescale_arr.append((i - min_val)/denom)
    return rescale_arr

data = [115, 140, 175]
print featureScaling(data)
