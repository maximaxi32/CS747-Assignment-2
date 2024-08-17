import argparse

parser = argparse.ArgumentParser()

def main():
    p1=(0,0)
    p2=(2,2)
    o1=(3,3)
    parser.add_argument("--opponent", type=str)
    parser.add_argument("--p", type=float)
    parser.add_argument("--q", type=float)
    args = parser.parse_args()
    Encoder(args.opponent,args.p,args.q)

         
    
class Encoder():
    def __init__(self,opponent_file,p,q):    
        self.p=p
        self.q=q
        with open(opponent_file) as file:
            for line in file:
                line2 = line.rstrip()
                words = line2.split()
                if words[0]=="state":
                    continue
                state=words[0]
                print(state,end=" ")
                print(return_point(state[0:2]),end=" ") 
                print(return_point(state[2:4]),end=" ")
                print(return_point(state[4:6]),end=" ")
                print(colinearity(return_point(state[0:2]),return_point(state[2:4]),return_point(state[4:6])))                  
        


#Helper functions
def colinearity(p1,p2,o1):
    x1=p1[0]
    x2=p2[0]
    y1=p1[1]
    y2=p2[1]
    x=o1[0]
    y=o1[1]
    
    if x1==x2:
        if x!=x2:
            return False
        k=(y-y1)/(y2-y1)
        if k>=0 and k<=1:
            return True
        return False
    if y1==y2:
        if y!=y2:
            return False
        k=(x-x1)/(x2-x1)
        if k>=0 and k<=1:
            return True
        return False
    
    m=(y2-y1)/(x2-x1)
    if m!=1 and m!=-1:
        return False

    m1=(x-x1)/(x2-x1)
    m2=(y-y1)/(y2-y1)
    if m1!=m2:
        return False
    if m1>=0 and m2>=0 and m1<=1 and m2<=1:
        return True
    return False
    
            
def return_point(p1):
    p1=int(p1)
    p1-=1
    row=p1//4
    column=p1%4
    return (row,column)
    



if __name__ == "__main__":
    main()