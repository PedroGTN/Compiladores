class Scope_Dict():

    def change_scope(self, num):
        self.scope += num
        if num>0:
            self.dict.append(dict())
        else:
            self.dict.pop(-1)

    def add(self, name, type):
        if '[' in name:
            if '.' in name:
                ind = name.index('[')
                nt = name[:ind]
                ind = name.index(']')
                name = nt + name[ind+1:]
            else:
                ind = name.index('[')
                name = name[:ind]
        self.dict[self.scope][name] = type


    def search(self, token):
        if '[' in token:
            if '.' in token:
                ind = token.index('[')
                nt = token[:ind]
                ind = token.index(']')
                token = nt + token[ind+1:]
            else:
                ind = token.index('[')
                token = token[:ind]
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
        if '[' in token:
            if '.' in token:
                ind = token.index('[')
                nt = token[:ind]
                ind = token.index(']')
                token = nt + token[ind+1:]
            else:
                ind = token.index('[')
                token = token[:ind]
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