import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

pulsar_params = []
tau = 0.3


def make_float(string_list):
    return [float(i) for i in string_list]


def fourier(x, *a):
    ret = a[0] * np.cos(np.pi / tau * x)
    for deg in range(1, len(a)):
        ret += a[deg] * np.cos((deg + 1) * np.pi / tau * x)
    return ret


with open('gl98_1408.csv', 'r') as csvfile:
    int = csv.reader(csvfile, delimiter=',')
    for row in int:
        if float(row[3]) < 0: row[3] = 0
        pulsar_params.append(make_float(row))
pulsar_params = np.array(pulsar_params)

a = 0.33/len(pulsar_params[:,2])
pulsar_period = np.multiply(pulsar_params[:,2],a)
normalised_profile = pulsar_params[:,3]/max(pulsar_params[:,3])

normalised_profile = np.array(normalised_profile)
#
# curve1 = normalised_profile[59:73]
# z1 = np.polyfit(pulsar_period[59:73], curve1, 8)
# p1 = np.poly1d(z1)
# curve2 = normalised_profile[140:150]
# z2 = np.polyfit(pulsar_period[140:150], curve2, 8)
# p2 = np.poly1d(z2)

#
plt.figure(1)


popt, pcov = curve_fit(fourier, pulsar_period, normalised_profile, [1.0] * 100)
plt.plot(pulsar_period, fourier(pulsar_period, *popt))
plt.plot(pulsar_period, normalised_profile)
#
# plt.plot(pulsar_period[0:59], np.zeros(59))
# plt.plot(pulsar_period[150:], np.zeros(len(pulsar_period[150:])))
# plt.plot(pulsar_period[59:73], p1(pulsar_period[59:73]))
# plt.plot(pulsar_period[73:140], np.zeros(len(pulsar_period[73:140])))
# plt.plot(pulsar_period[140:150], p2(pulsar_period[140:150]))
# plt.plot(pulsar_period[59:70],z1)

# noisy = np.zeros(len(normalised_profile))
# for j in range(0,10000):
#     for i in range(0, len(normalised_profile)):
#         noisy[i] += normalised_profile[i] + np.random.normal(0, 10)
# plt.plot(pulsar_period, noisy/max(noisy))

pulsar_polyfit = np.array([-9.012249604196335278638585464250e-08,
                           1.338561695894840870998764416691e-02,
                           -1.095685607944423408440484570946e-04,
                           -1.202392452344584893108276175669e-08,
                           -2.030664224439728071138335652111e-11,
                           -1.539710868628319921285379842781e-14,
                           1.569318060778122604813653623029e-17,
                           6.392753000822702218711102623017e-21,
                           2.952071911715859777941308278600e-23,
                           1.922862083262306431005007489297e-25,
                           -4.155531187952212765301328004287e-28,
                           -4.689897041107014931125158852454e-30])



plt.show()
