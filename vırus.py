from rand_string.rand_string import RandString 
import os 




while True:
    try: 

        os.mkdir(RandString("lowercase",6))
    except FileExistsError:
        pass