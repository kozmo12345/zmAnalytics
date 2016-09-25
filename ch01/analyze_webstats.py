import os
from utils import DATA_DIR, CHART_DIR
import scipy as sp
import matplotlib.pyplot as plt

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

date = "2016-09-23"
filePath = os.path.join("C:\\", "Data\\2016-09-23.txt");
# dtype = sp.dtype([('time','|S20'),('grade','i8'),('name','O'),('rate','f8'),('quality','i8'),('mesu','i8'),('medo','i8'),('code','|S20'),('value','i8')])
data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')

# # 예제는 3갸지 범주이다
colors = ['g', 'k', 'b', 'm', 'r']
linestyles = ['-', '-.', '--', ':', '-']

t = data[:, 0]
g = data[:, 1].astype('i8')
n = data[:, 2].astype('i8')
r = data[:, 3].astype('f8')
q = data[:, 4].astype('i8')
ms = data[:, 5].astype('i8')
md = data[:, 6].astype('i8')
c = data[:, 7]
v = data[:, 8].astype('i8')
# # print("Number of invalid entries:", sp.sum(sp.isnan(r)))
# t = t[~sp.isnan(r)]
g = g[~sp.isnan(g)]
# n = n[~sp.isnan(r)]
# r = r[~sp.isnan(r)]
# q = q[~sp.isnan(r)]
# ms = ms[~sp.isnan(r)]
# md = md[~sp.isnan(r)]
# c = c[~sp.isnan(r)]
# v = v[~sp.isnan(r)]

# r = r[~sp.isnan(r)]
# q = q[~sp.isnan(r)]
# ms = ms[~sp.isnan(r)]
# md = md[~sp.isnan(r)]

# # 입력 데이터 그리기
# def plot_models(x, y, models, fname, mx=None, ymax=None, xmin=None):
#     plt.figure(num=None, figsize=(8, 6))
#     plt.clf()
#     plt.scatter(x, y, s=10)
#     plt.title("Web traffic over the last month")
#     plt.xlabel("Time")
#     plt.ylabel("Hits/hour")
#     plt.xticks(
#         [w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])

#     if models:
#         if mx is None:
#             mx = sp.linspace(0, x[-1], 1000)
#         for model, style, color in zip(models, linestyles, colors):
#             # print "Model:",model
#             # print "Coeffs:",model.coeffs
#             plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

#         plt.legend(["d=%i" % m.order for m in models], loc="upper left")

#     plt.autoscale(tight=True)
#     plt.ylim(ymin=0)
#     if ymax:
#         plt.ylim(ymax=ymax)
#     if xmin:
#         plt.xlim(xmin=xmin)
#     plt.grid(True, linestyle='-', color='0.75')
#     plt.savefig(fname)

# # # 데이터 얼핏 보기
# plot_models(x, y, None, os.path.join(CHART_DIR, "1400_01_01.png"))

# # 모델 생성과 그리기
# fp1, res1, rank1, sv1, rcond1 = sp.polyfit(x, y, 1, full=True)
# print("Model parameters of fp1: %s" % fp1)
# print("Error of the model of fp1:", res1)
# f1 = sp.poly1d(fp1)

# fp2, res2, rank2, sv2, rcond2 = sp.polyfit(x, y, 2, full=True)
# print("Model parameters of fp2: %s" % fp2)
# print("Error of the model of fp2:", res2)
# f2 = sp.poly1d(fp2)
# f3 = sp.poly1d(sp.polyfit(x, y, 3))
# f10 = sp.poly1d(sp.polyfit(x, y, 10))
# f100 = sp.poly1d(sp.polyfit(x, y, 100))

# plot_models(x, y, [f1], os.path.join(CHART_DIR, "1400_01_02.png"))
# plot_models(x, y, [f1, f2], os.path.join(CHART_DIR, "1400_01_03.png"))
# plot_models(
#     x, y, [f1, f2, f3, f10, f100], os.path.join(CHART_DIR, "1400_01_04.png"))

# # 변곡점에 대한 정보를 사용하여 모델 생성과 그리기
# inflection = 3.5 * 7 * 24
# xa = x[:inflection]
# ya = y[:inflection]
# xb = x[inflection:]
# yb = y[inflection:]

# fa = sp.poly1d(sp.polyfit(xa, ya, 1))
# fb = sp.poly1d(sp.polyfit(xb, yb, 1))

# plot_models(x, y, [fa, fb], os.path.join(CHART_DIR, "1400_01_05.png"))


# def error(f, x, y):
#     return sp.sum((f(x) - y) ** 2)

# print("Errors for the complete data set:")
# for f in [f1, f2, f3, f10, f100]:
#     print("Error d=%i: %f" % (f.order, error(f, x, y)))

# print("Errors for only the time after inflection point")
# for f in [f1, f2, f3, f10, f100]:
#     print("Error d=%i: %f" % (f.order, error(f, xb, yb)))

# print("Error inflection=%f" % (error(fa, xa, ya) + error(fb, xb, yb)))


# # 미래 추정하기
# plot_models(
#     x, y, [f1, f2, f3, f10, f100],
#     os.path.join(CHART_DIR, "1400_01_06.png"),
#     mx=sp.linspace(0 * 7 * 24, 6 * 7 * 24, 100),
#     ymax=10000, xmin=0 * 7 * 24)

# print("Trained only on data after inflection point")
# fb1 = fb
# fb2 = sp.poly1d(sp.polyfit(xb, yb, 2))
# fb3 = sp.poly1d(sp.polyfit(xb, yb, 3))
# fb10 = sp.poly1d(sp.polyfit(xb, yb, 10))
# fb100 = sp.poly1d(sp.polyfit(xb, yb, 100))

# print("Errors for only the time after inflection point")
# for f in [fb1, fb2, fb3, fb10, fb100]:
#     print("Error d=%i: %f" % (f.order, error(f, xb, yb)))

# plot_models(
#     x, y, [fb1, fb2, fb3, fb10, fb100],
#     os.path.join(CHART_DIR, "1400_01_07.png"),
#     mx=sp.linspace(0 * 7 * 24, 6 * 7 * 24, 100),
#     ymax=10000, xmin=0 * 7 * 24)

# # 테스트 데이터와 훈련 데이터 분리
# frac = 0.3
# split_idx = int(frac * len(xb))
# shuffled = sp.random.permutation(list(range(len(xb))))
# test = sorted(shuffled[:split_idx])
# train = sorted(shuffled[split_idx:])
# fbt1 = sp.poly1d(sp.polyfit(xb[train], yb[train], 1))
# fbt2 = sp.poly1d(sp.polyfit(xb[train], yb[train], 2))
# print("fbt2(x)= \n%s"%fbt2)
# print("fbt2(x)-100,000= \n%s"%(fbt2-100000))
# fbt3 = sp.poly1d(sp.polyfit(xb[train], yb[train], 3))
# fbt10 = sp.poly1d(sp.polyfit(xb[train], yb[train], 10))
# fbt100 = sp.poly1d(sp.polyfit(xb[train], yb[train], 100))

# print("Test errors for only the time after inflection point")
# for f in [fbt1, fbt2, fbt3, fbt10, fbt100]:
#     print("Error d=%i: %f" % (f.order, error(f, xb[test], yb[test])))

# plot_models(
#     x, y, [fbt1, fbt2, fbt3, fbt10, fbt100],
#     os.path.join(CHART_DIR, "1400_01_08.png"),
#     mx=sp.linspace(0 * 7 * 24, 6 * 7 * 24, 100),
#     ymax=10000, xmin=0 * 7 * 24)

# from scipy.optimize import fsolve
# print(fbt2)
# print(fbt2 - 100000)
# reached_max = fsolve(fbt2 - 100000, x0=800) / (7 * 24)
# print("100,000 hits/hour expected at week %f" % reached_max[0])
