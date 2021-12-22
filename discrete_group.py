# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:54:41 2021

@author: sayori
"""

def list_pr(l):
    for i in l:
        print(i)
def id_pr(i,pos=0):
    ps=["左","右"]
    if i[0]==0 and i[1]==0:
        print("无{}幺元".format(ps[pos]))
    else:
        print("有{}幺元:".format(ps[pos]),end="")
        for k in range(2):
            if i[k]==1:
                print(k,end=" ")
        print()
        


class Group:
    project=[0,0,0,0]
    def __init__(self,num):
        self.num=num
    def __add__(self,a):
        if self.num==0 and a.num==0:
            return Group(Group.project[0])
        if self.num==0 and a.num==1:
            return Group(Group.project[1])
        if self.num==1 and a.num==0:
            return Group(Group.project[2])
        if self.num==1 and a.num==1:
            return Group(Group.project[3])

def evalute_project():
    all_project=[[a,b,c,d] for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
    semi_group=[]
    not_semi_group=[]
    for single_project in all_project:
        Group.project=single_project
        flag=True
        for k1 in range(2):
            for k2 in range(2):
                for k3 in range(2):
                        a=Group(k1)
                        b=Group(k2)
                        c=Group(k3)                   
                        if (a+b+c).num!=(c+b+a).num:                      
                            flag=False
        if flag:
            semi_group.append(single_project)
        else:
            not_semi_group.append(single_project)
                        
            
    print("not_semigroup({}):".format(len(not_semi_group)))
    list_pr(not_semi_group)
    print("semigroup({}):".format(len(semi_group)))
    list_pr(semi_group)
    
    monoid=[]
    group=[]
    for i in semi_group:
        Group.project=i
        left=[1,1]
        right=[1,1]
        for alpha in range(2):
            for beta in range(2):
                a=Group(alpha)
                b=Group(beta)
                if (a+b).num!=b.num:
                    left[a.num]=0
                if (a+b).num!=a.num:
                    right[b.num]=0
        if (left[0]==1 or left[1]==1) and (right[0]==1 or right[1]==1):
            monoid.append(i)
            flag=True
            if left[0]==1:
                lid=0
            else:
                lid=1
            flag=True
            for k1 in range(2):#抽象代数定理1.1.15
                if (Group(0)+Group(k1)).num!=lid and (Group(1)+Group(k1)).num!=lid:
                    flag=False
            if flag:
                group.append(i)
           
        #print("\n",i)
        #id_pr(left)
        #id_pr(right,pos=1)
    print("monoid({}):".format(len(monoid)))
    list_pr(monoid)
    print("group({}):".format(len(group)))
    list_pr(group)
    
    
        
evalute_project()