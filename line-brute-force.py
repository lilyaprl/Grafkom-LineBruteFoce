import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.suptitle('Membentuk Garis Dengan Algoritma Brute Force')
plt.subplots_adjust(bottom=0.2)
x = np.array([3,9])
y = np.array([1,5])

m=0
x = np.array([3,9])
y = np.array([1,5])
xline,yline = [],[]
if x[0]==x[1]:
        p = y[0]
        if y[0]>y[1]:
            p = y[1]
        xline = np.append(x,x[0])
        yline = np.append(y,p+1)
elif y[0]==y[1]:
    m = np.Infinity
    p = x[0]
    if x[0]>x[1]:
        p = y[1]
    xline = np.append(x,(x[0])+1)
    yline = np.append(y,y[1])
else:
    if m<1:
        m = (y[1]-y[0])/(x[1]-x[0])
        n = abs(x[1]-x[0])
        x2 = x[0]
        i = 1
        while i <= n+1:
            y2 = y[0]+m*(x2-x[0])
            xline.append(x2)
            yline.append(round(y2))
            x2+=1
            i+=1
        else:
            m = (x[1]-x[0])/(y[1]-y[0])
            n = abs(y[1]-y[0])
            y2 = y[0]
            i = 1
            while i <= n+1:
                x2 = x[0]+m*(y2-y[0])
                yline.append(y2)
                xline.append(round(x2))
                y2+=1
                i+=1
np.array(xline)
np.array(yline)
print('Titik Koordinat: (', x[0], ',',y[0],') (',x[1],',',y[1],')')
print('Titik Penghubung: ',end=' ')
for i in range (len(xline)):
    if i < len(xline)-1:
        print('(',xline[i],',', yline[i],end='),')
    else:
        print('(',xline[i],',',yline[i],end=')')
print()

l0, = ax.plot(xline, yline ,'o')
l1, = ax.plot(x, y)

l0.set_label('Titik Penghubung')
l1.set_label('Garis Penghubung')
ax.legend()
plt.grid()
plt.show()
