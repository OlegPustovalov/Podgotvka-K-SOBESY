class Stack:
    def __init__(self):
        self.stack_ = []

    def isEmpty(self):
        if self.stack_ == []:
            return True
        else:
            return False
    
    def push_(self,item_):
        self.stack_.append(item_)

    def pop_(self):
        self.stack_.pop()
        if (len(self.stack_)-1) >= 0:
            return self.stack_[len(self.stack_)-1]
        else:
            return 0
    
    def peek_(self):
        if (len(self.stack_)-1) >= 0:
            return self.stack_[len(self.stack_)-1]
        else:
            return 0

    def size(self):
        return len(self.stack_)

def balance_str(str_):
    f = Stack()
    s = Stack()      
    smb_s = ''
    for sym_ in str_:
        f.push_(sym_)
    smb_f = f.peek_()
    if (f.size() % 2) == 1 or (smb_f == '(') or (smb_f == '[') or (smb_f == '{'):
        res = "Несбалансированно"
        return res
    else:
        s.push_(smb_f)
        smb_s = smb_f
        while (f.size() > 0):
            if (smb_f == ')') or (smb_f == ']') or (smb_f == '}'):
                s.push_(smb_f)
                smb_s = smb_f
                smb_f = f.pop_()
            elif (smb_f == '(' and smb_s ==')') or (smb_f == '[' and smb_s ==']') or (smb_f == '{' and smb_s =='}'):
                smb_s = s.pop_()
                smb_f = f.pop_() 
            else:
                res = 'Несбалансированно'
                return res                                        
    res = 'Cбалансированно'
    return res


