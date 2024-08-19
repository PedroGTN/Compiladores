class Scope_Dict():

    def change_scope(self, num):
        self.scope += num
        if num>0:
            self.dict.append(dict())
        else:
            self.dict.pop(-1)

    def add(self, type, name):
        self.dict[self.scope][type] = name


    def search(self, token):
        i = self.scope
        flag = False
        while(i>=0):
            if token in self.dict[i].keys():
                flag = True
            i-=1
        return flag
    
    def print(self):
        print(self.dict)


    def search_text(self, token):
        i = self.scope
        ret = "NULL"
        while(i>=0):
            if token in self.dict[i].keys():
                ret = self.dict[i][token]
                return ret
            i-=1
        return ret


    def __init__(self) -> None:
        self.dict = [dict()]
        self.scope = 0
        pass