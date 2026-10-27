import numpy as np


x_A = np.array([500, 300])
p_A = np.array([0.6, 0.4])

x_B = np.array([440, 120])
p_B = np.array([0.9, 0.1])


def calculate_risk_metrics(x, p):
    m = np.sum(x * p)

    var = np.sum(p * (x - m) ** 2)
    sigma = np.sqrt(var)

    unfavorable_mask = x < m
    sv = np.sum(p[unfavorable_mask] * (x[unfavorable_mask] - m) ** 2)
    ssv = np.sqrt(sv)

    cv = (sigma / m) * 100
    csv = (ssv / m) * 100

    return m, sigma, ssv, cv, csv


m_A, sig_A, ssv_A, cv_A, csv_A = calculate_risk_metrics(x_A, p_A)
m_B, sig_B, ssv_B, cv_B, csv_B = calculate_risk_metrics(x_B, p_B)

print(f"--- АКТИВ: АКЦІЇ ---")
print(f"Сподіваний прибуток (M): {m_A:.2f} тис. $")
print(f"СКО (sigma): {sig_A:.2f} тис. $")
print(f"Семіквадратичне відхилення (SSV): {ssv_A:.2f} тис. $")
print(f"Коефіцієнт варіації (CV): {cv_A:.2f}%")
print(f"Коефіцієнт семіваріації (CSV): {csv_A:.2f}%\n")

print(f"--- АКТИВ: ОБЛІГАЦІЇ ---")
print(f"Сподіваний прибуток (M): {m_B:.2f} тис. $")
print(f"СКО (sigma): {sig_B:.2f} тис. $")
print(f"Семіквадратичне відхилення (SSV): {ssv_B:.2f} тис. $")
print(f"Коефіцієнт варіації (CV): {cv_B:.2f}%")
print(f"Коефіцієнт семіваріації (CSV): {csv_B:.2f}%")