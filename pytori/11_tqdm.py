from tqdm import tqdm
import time

with tqdm(total=100, desc="処理中") as pbar:
    for count in map(str, range(100)):
        if int(count) % 2 or int(count) % 3 == 0:   
            tqdm.write(count.upper())
            time.sleep(0.01)
        else:
            tqdm.write(count.upper())
            time.sleep(0.3)
        pbar.update(1)
    tqdm.write("完了！")