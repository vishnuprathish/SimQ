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
        'A':list([x for x in range(100)]),
        'B':list([random.randint(0,x) for x in range(0,100)]),
        'C':list([random.randint(0,x) for x in range(0,100)])
    }

    
    def __init__(self, tableName,columns,pKey=None):
        self.tableName=tableName
        self.pKey=pKey
        self.columns=columns
        self.runs=[0 for x in range(len(self.columns))]
        pass
    
    def __str__(self):
        
        return str("Size: " + str(self.size) + "  Runs: "+ str(self.runs)) #+ str(self.TableData))
        
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
        self.size=int(size)
    
    def getRuns(self):
        return self.runs
        
    def getColRuns(self,colName):  #get the number of runs of a specified columns
        print self.getColIdx(colName)
        return self.runs[self.getColIdx(colName)]
    
    def getSize(self):
        return self.size
        
    def getMaxT(self,columnName):
        return max(self.TableData[columnName])
        
    def getMinT(self,columnName):
        return min(self.TableData[columnName])
        
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
        
    def getSelFactor(self,args):
        if(args[1]=='='):
            selFactor=float(1/float(self.ukeys[self.getColIdx(args[0])]))
        elif(args[1]=='>'):      #Coulmn > Value
            selfFactor = float(((self.getMaxT(args[0])) - int(args[2]))) / float(( self.getMaxT(args[0]) - self.getMinT(args[0]) ))
        elif(args[1]=='<'):      #Coulmn > Value
            selfFactor = float(((self.getMaxT(args[0])) - int(args[2]))) / float(( self.getMaxT(args[0]) - self.getMinT(args[0]) ))
        elif(args[1]=='IN'):
            factors=[self.getSelFactor([args[0],'=',value]) for value in args[2]]
            final=factors[0]
            del factors[0]

            for smrit in factors:
                final=float(float(final) * float(smrit))
            selFactor=final
        return selFactor
        
    def select(self,args):
        x=Relation("result",self.columns,None)
        #x.setStats(self,None,None,self.size*S.getSize())
        if(args[1]=='='):
            if(args[2] in self.getColumnNames()):
                x.setStats()
                pass    
            else:
                sFactor=self.getSelFactor(args)
                x.setSize(self.size * sFactor)  #Column = value 
                
                #finding the number of runs for Column = value predicate. 
                chRuns = [self.getColRuns(args[0])*sFactor,self.getColRuns(args[0])*sFactor , self.getColRuns(args[0])*sFactor]
                chRuns[self.getColIdx(args[0])]=1
                print chRuns
                x.setRuns(chRuns)
                pass 
        
        if(args[1]=='>'):      #Coulmn > Value
            selfFactor = float(((self.getMaxT(args[0])) - int(args[2]))) / float(( self.getMaxT(args[0]) - self.getMinT(args[0]) ))
            x.setSize(selfFactor * self.size) 
            
        elif(args[1]=='<'):      #Coulmn > Value
            selfFactor = float(((self.getMaxT(args[0])) - int(args[2]))) / float(( self.getMaxT(args[0]) - self.getMinT(args[0]) ))
            x.setSize((1-selfFactor) * self.size)  
        elif(args[1]=='IN'):
            selfFactor=self.getSelFactor(args)
            x.setSize(selfFactor * self.size)
            
            
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
R.setStats([100],[100,100,300],100)
print R.getColumnNames()
S = Relation("R",{'A':'int','B':'int','D':'int'})
S.setStats([100],[100,2,300],100)
print S.getColumnNames()

print S.select(['A','>','25'])
print S.select(['B','>','25'])
print S.select(['C','>','25'])

print S.select(['A','<','25'])
print S.select(['A','<','75'])
print S.select(['B','<','25'])

print S.select(['B','=','25'])

print S.select(['B','IN',[10,20,30]])



