import pandas as pd
df = pd.read_csv("log.log")
reads = df["dram__bytes_read.sum"].apply(lambda x: int(x.replace(',', '')) if x!="byte" else 0)
#writes = df["dram__bytes_write.sum"].apply(lambda x: int(x.replace(',', '')))
print(reads.sum())
