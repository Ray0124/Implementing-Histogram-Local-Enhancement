Implementing histogram statistics method and local enhancement method to extract low contrast pattern hidding in the pic.  
The sample picture is as bellow:  

![image](https://github.com/Ray0124/Implementing-Histogram-Local-Enhancement/blob/main/hidden%20object.jpg)  

First,we can check probability density function about the picture.  
You will notice that some gray scale probability are high. 

![image](https://github.com/Ray0124/Find-Hidden-Patterns-by-Histogram-Local-Enhancement-/blob/main/pdf.PNG)  

We can use histogram equalization to enhance the contour of the whole picture, but the hidding pattern is low contrast ,so the effect is not good.  
It seems that we should take the picture part by part to judge whether to enhance (Local enhancement).  
According to condition:

![image](https://github.com/Ray0124/Find-Hidden-Patterns-by-Histogram-Local-Enhancement-/blob/main/condition.PNG)  

I made a sliding window to compute some parameter(mean and standard deviation) and comparing the parameter of ROI with the parameter of the whole picture to choose setting like k0、k1 to separate dark from white part, k2、k3 to enhance its low contrast part, and the enhance degree C.    
Then, we can extract the hidding pattern as below:

![image](https://github.com/Ray0124/Find-Hidden-Patterns-by-Histogram-Local-Enhancement-/blob/main/contrast.png)  
