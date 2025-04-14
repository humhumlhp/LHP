import pandas as pd
from scipy.signal import find_peaks

# Đọc file
df = pd.read_excel("Solieu.xlsx", sheet_name="Amplitudes")
df_clean = df.dropna()

# Tìm các đỉnh
spl = df_clean['Sound pressure level (dB)'].values
peaks, _ = find_peaks(spl)
peaks_df = df_clean.iloc[peaks][['Time (s)', 'Sound pressure level (dB)']]

# Xuất ra file Excel
peaks_df.to_excel("Dinh_am_thanh.xlsx", index=False)