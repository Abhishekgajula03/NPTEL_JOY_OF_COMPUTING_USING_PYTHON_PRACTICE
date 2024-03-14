# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:07:53 2024

@author: Abhishek
"""
import turtle
turtle.bgcolor("black")
seurat=turtle.Turtle()

width=5
height=7
dot_distance=25
seurat.setpos(-250,250)

def spiral(m,n):#m-row,n-col,a-list through which i represent matrix
    k=0#k= index of starting row  l=index of starting col'''
    l=0
    f=0
    seurat.color("white")
    while(k<m and l<n):
        if f==1:
            seurat.right(90)
        #printing thr first row 
        for i in range(l,n):
            seurat.forward(dot_distance)
            #print(a[k][i],end=" ")
        k=k+1
        f=1
        seurat.right(90)
        #printing the last col from remaining col
        for i in range(k,m):
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
        n=n-1
        seurat.right(90)
        #printing the last row from remaining row
        if k<m:
            for i in range(n-1,l-1,-1):
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m=m-1
        seurat.right(90)    
        if l<n:
            #printing the first col from remaining col
            for i in range(m-1,k-1,-1):
                seurat.forward(dot_distance)
                #print(a[i][l],end="")
            l+=1
"""a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
    """
spiral(20, 20)
turtle.done()