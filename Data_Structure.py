# Custom Array Data Structure using OOP


class Array:
    def __init__(self,*items):
        self.items = items
        
    def __str__(self):
        num = len(str(len(self.items)))
        temp = "="*(num+11)
        count = 0
        num2 = len(str(count))
        final = f"{temp}\n Index|Items\n"
        for i in self:  
            space = " "*(num-num2+3)
            temp2 = f"{space} {count} | {i}"
            final+=f"{temp}\n{temp2}\n"
            count+=1
        return final+temp
    
    
    
    def __iter__(self):                     # For iteration in for loop
        self.index = 0
        return self

    def __next__(self):
        if self.index!=len(self.items):
            temp = self.items[self.index]
            self.index+=1
            return temp
        else:
            raise StopIteration
            
    
    def insert(self,item=None,ind=None):        # To append and insert in the array
        temp =list((None,)*(len(self.items)+1))
        count = 0
        for i in range(len(temp)):
            if i==ind or i==(len(self.items)):
                temp[i]=item
            else:
                temp[i]=self.items[count]
                count+=1
        self.items = tuple(temp)
        
    def __getitem__(self,index):                # Making the object subscriptable
        return self.items[index]                # square bracket will work
    
    
    
