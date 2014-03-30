import random
def compute(table1,table2,operator,args):
    
    pass
class Relation:
    'well, a table. '
    columns={}
    pKey=None
    runs=[]
    ukeys=[]
    size=0
    
    TableData={
        'A':[x for x in range(1000)]
        'B':random.shuffle([x/3 for x in range(1000)])
        'C':random.shuffle([x/6 for x in range(1000)])
    }

    
    def __init__(self, tableName,columns=None,pKey=None):
        self.tableName=tableName
        self.pKey=pKey
        self.columns=columns
        pass
    
    def __str__(self):
        return str(self.size)
        
    def setPkey(self,pKey):
        self.pKey=pKey
        pass
    
    def getPkey(self):
        return self.pKey
        pass
        
    def setColumns(self,columns):
        self.columns=columns
        
    def getName(self):
        return self.tableName
        
    def getColumns(self):
        return self.columns
        
    def getColumnNames(self):
        return [x for x in self.columns.keys()]

    def setStats(self,runs=None,ukeys=None,size=None):
        self.runs=runs
        self.ukeys=ukeys
        self.size=size
    def setRuns(self,runs):
        self.runs=runs
    
    def setuKeys(self,uKeys):
        self.uKeys=uKeys
    
    def setSize(self,size):
        self.size=size
    
    def getRuns(self):
        return self.runs
    
    def getSize(self):
        return self.size
        
    def getColIdx(self,columnName):
        i=0
        for x in self.getColumnNames():       
            if columnName==x:
                return i
            i+=1
        return -1
        
    def union(self,S):
        x=Relation("result",self.columns,self.pKey)
        x.setStats(self.runs+S.getRuns(),None,self.size+S.getSize())
        return x
        pass

    def intersect(self,S):
        x=Relation("result",self.columns,self.pKey)
        x.setStats(self,None,None,self.size-S.getSize())
        return x
        pass
        
    def cartProd(self,S):
        
        x=Relation("result",self.columns+S.getColumns(),None)
        x.setStats(self,None,None,self.size*S.getSize())
        return x
        pass
        
    def select(self,args):
        x=Relation("result",self.columns+s.getColumns(),None)
        x.setStats(self,None,None,self.size*S.getSize())
        if(args[1]=='='):
            if(args[2] in self.getcolumnNames()):
                x.setStats()
                pass
            else:
                x.setSize(self.size/self.uKeys[getColIdx[args[2]]])  #Column = value 
                pass 
        
        if(args[1]=='>'):      #Coulmn > Value
            
            
        return x
        pass
    
    def project(self,args):
        x=Relation("result",self.columns,None)
        x.setStats(self,None,None,self.size)
        return x
        pass
        
    def natJoin(self,S,args):
        x=Relation("result",self.columns+S.getColumns(),None)
        x.setStats(self,None,None,self.size*S.getSize())
        return x
        pass
        
    def generateData(seed):
	pass 


R = Relation("R",{'A':'int','B':'int','C':'int'})
R.setStats([100],100,1000)
print R.getColumnNames()
S = Relation("R")
S = Relation("R",{'A':'int','B':'int','D':'int'})
S.setStats([100],100,1000)
print S.getColumnNames()

print R.union(S)

