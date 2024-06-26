#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Complete the function below
    def diagonalSum(self, root):
        #:param root: root of the given tree.

        #code here
        rows = []
        wr = [[root]]
        nx_wr = []
        r_count = 1

        while True :

            #loop break condition, when last branch of binary tree reached, when all the elment of workign row (wr) are None
            not_none = False
            for i in range(len(wr)):
                for j in wr[i]:
                    if j != None:
                        not_none = True
                        break
                if not_none:
                    break
            
            if not not_none:
                break
            

            rows.append(wr)
            
            #now collection row of the tree in desired format
            nx_wr = [[] for _ in range(r_count+1)]
            for i in range(len(wr)):
                for j in range(len(wr[i])):
                    if wr[i][j] is not None:
                        nx_wr[i].append(wr[i][j].left)
                        nx_wr[i+1].append(wr[i][j].right)
            
            r_count += 1
            wr = nx_wr

        #now finally finding the sum of diagonal elements
        r_count = r_count-1 #removing last none row count
        ans = []
        for i in range(1, r_count+1):
            sum = 0
            for j in range(i-1,r_count):
                for node in rows[j][-i]:
                    if node is not None:
                        sum += node.data   
            
            if sum != 0:
                ans.append(sum)
        
        return ans
        
        



    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    # t = 1
    for _ in range(0,t):
        s=input()
        # s = '4 1 3 N N 3'
        root=buildTree(s)
        ob = Solution()
        res = ob.diagonalSum(root)
        # print(res)
        for i in res:
            print (i, end = " ")
        print()

# } Driver Code Ends