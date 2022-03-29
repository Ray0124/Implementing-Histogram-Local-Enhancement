import cv2
import numpy as np
import matplotlib.pyplot as plt

def getmean(r_pdf):
    m= 0.0
    for i in range(256):
        m=m+i*r_pdf[i]
    return m

def getvar(r_pdf,m):
    var= 0.0
    for i in range(256):
        if r_pdf[i]!=0:
            var=var+(pow(i-m,2)*r_pdf[i])
    return var



img = cv2.imread('hidden object.jpg',0)

dst=np.zeros_like(img)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
h, w = img.shape
hist_nom=hist/(h*w)            #PDF
plt.title("PDF")
plt.plot(hist_nom)


#整體
mean=getmean(hist_nom)
var=getvar(hist_nom,mean)
var_squrt=np.sqrt(var)
print(mean)
print(var_squrt)


#參數設定
mxy=0.0
varxy=0.0
dim=6
ROI=dim*dim
k0=0
k1=0.3
k2=0
k3=0.3
C= 22.8
shift=int(dim/2)

#每點周邊ROI進行判斷
for i in range(shift,h-shift):
    for j in range(shift, w-shift):
        img_ROI=img[(j-shift) : (j+shift+1) , (i-shift) : (i+shift+1)]
        hist_ROI = cv2.calcHist([img_ROI], [0], None, [256], [0, 255])
        hist_ROI_nom = hist_ROI / ROI
        mxy=getmean(hist_ROI_nom)
        varxy=getvar(hist_ROI_nom,mxy)
        varxy_squrt = np.sqrt(varxy)

        # print(mxy)
        # print(varxy_squrt)

        if (k0*mean <= mxy <= k1*mean) and (k2*var_squrt <= varxy_squrt <= k3*var_squrt):
            dst[i, j] = C * img[i, j]
            # print('增強')
        else:
            dst[i, j] = img[i, j]
            #print('pass')


cv2.imshow('en_img',dst)
cv2.imshow('img_ori',img)

plt.show()
# cv2.waitKey(0)






