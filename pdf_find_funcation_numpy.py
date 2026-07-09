import numpy as np
import math

# user define funcation that find the pdf(probability density funcation)
def find_pdf(mean,std,x):
      a=x-mean    # step 1 
      b=a/std   # step 2
      c=b **2    # step 4
      d=-0.5 * c  # step 5 
      e=np.exp(d)   # step 6
      f=std * np.sqrt(2 * np.pi)  # step 7
      g=1/f    # step 8
      pdf= g  *e # step 9
      return pdf

mean=int(input("Enter the mean==>"))         # mean==avg
std=int(input("Enter the standard deviation==>"))  # std
x=int(input ("Enter the value "))   # any vlaue 
result=find_pdf(mean,std,x)
print("answer fdf==>",result)