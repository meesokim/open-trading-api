import pandas as pd
import urllib.request
import ssl
import zipfile
import os



def get_theme_master_dataframe(base_dir):



ssl._create_default_https_context = ssl._create_unverified_context

urllib.request.urlretrieve("https://new.real.download.dws.co.kr/common/master/theme_code.mst.zip", base_dir + "\\theme_code.zip")

os.chdir(base_dir)



kospi_zip = zipfile.ZipFile('theme_code.zip')
kospi_zip.extractall()

kospi_zip.close()

file_name = base_dir + "\\theme_code.mst"
df = pd.DataFrame(columns = ['테마코드', '테마명', '종목코드'])

ridx = 1
with open(file_name, mode="r", encoding="cp949") as f:
for row in f:
tcode = row[0:3]
jcode = row[-10:].rstrip()
tname = row[3:-10].rstrip()
df.loc[ridx] = [tcode, tname, jcode]
ridx += 1

return df



df1 = get_theme_master_dataframe("d:\\pysam")