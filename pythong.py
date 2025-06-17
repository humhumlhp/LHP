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

# Tính bước thời gian trung bình giữa các đỉnh để tính chu kỳ trung bình
times = peaks_df['Time (s)'].values
if len(times) > 1:
    period = (times[-1] - times[0]) / (len(times) - 1)
    frequency = 1 / period  # Tần số
    speed_of_sound = 343  # Tốc độ âm thanh (m/s)
    wavelength = speed_of_sound / frequency
    print("Wavelength of the sound: {:.2f} m".format(wavelength))
else:
    print("Not enough peaks to calculate wavelength")