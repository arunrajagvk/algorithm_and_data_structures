
def secondMax():
    n = int(input())
    arr = map(int, input().split())
    if n >= 2:
        print(set(arr))
        l = list(set(arr))
        new_l = max(l)
        print(new_l)
        l.remove(new_l)
        return max(l)
    else:
        return n

def solve(meal_cost, tip_percent, tax_percent):
    if meal_cost > 0 :
        tip_cost = meal_cost * (tip_percent / 100)
        tax_cost = meal_cost * (tax_percent / 100)
        total_cost = meal_cost + tip_cost + tax_cost
        return round(total_cost)
    else:
        return round(meal_cost)

###########################################################
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1



###########################################################



def stringParser(str_ip):
    for s in str_ip:
        e_str = []
        o_str = []
        [ e_str.append(s[i]) if i%2 == 0 else o_str.append(s[i]) for i in range(0,len(s)) ]
        print('{} {}'.format(''.join(e_str),''.join(o_str)))

###########################################################

def reverse_str(arr):
    str_list = [str(i) for i in arr[::-1]]
    print (' '.join(str_list))

###########################################################
def phone_book(nm,pb):
    f_result=[]
    for n in nm:
        if pb.get(n):
            f_result.append( n+"="+pb.get(n))
        else:
            f_result.append("Not found")
    return f_result

###########################################################
def get_binary(n):
    if n>1:
        result.append(n%2)
        get_binary(n//2)
        result
    elif n == 1:
        result.append(1)
    return result[::-1]

def consecutive_sum(binary_result):
    consecutive = 0
    max_consecutive =0

    for i in range(0,len(b_result)):
        if b_result[i] != 0:
            consecutive +=1
        elif b_result[i] == 0:
            if max_consecutive <= consecutive:
                max_consecutive = consecutive
            consecutive = 0
    print(max(max_consecutive,consecutive))

###########################################################

## Example for Abstract class

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price = price 

    def display(self):
        print("Title: {}\nAuthor: {}\nPrice: {}".format(self.title,self.author,self.price))


# title=input()
# author=input()
# price=int(input())
# new_novel=MyBook(title,author,price)
# new_novel.display()

###########################################################

if __name__ == '__main__':


    ## -- Solution second max --#
    # secondMax()

    ## -- Solution total cost with tax  --#
    # meal_cost = float(input())
    # tip_percent = int(input())
    # tax_percent = int(input())
    # print(solve(meal_cost, tip_percent, tax_percent))

    ## -- Solution class and instance for Age --#
    # t = int(input())
    # for i in range(0, t):
    #     age = int(input())
    #     p = Person(age)
    #     p.amIOld()
    #     for j in range(0, 3):
    #         p.yearPasses()
    #     p.amIOld()
    #     print("")

    ## -- Solution split string --#
    # 2
    # Hacker
    # Rank
    #
    # Hce akr
    # Rn ak
    # input_str = int(input())
    #     # str_inp = []
    #     # for i in range(0, input_str):
    #     #     ip_st = str(input())
    #     #     str_inp.append(ip_st)
    #     # stringParser(str_inp)

    ## -- Solution reverse string --#
    # 1 2 3 4 => 4 3 2 1
    # n = int(input())
    #
    # arr = list(map(int, input().rstrip().split()))
    # reverse_str(arr)

    ## -- Solution dictionary  --#
    # n = int(input())
    # phone_b = {}
    # for i in range(0,n):
    #     str_inp1,str_inp2 = input().split()
    #     phone_b[str_inp1] = str_inp2
    #
    # result_arr = []
    # res_ip=[]
    # while True:
    #     ip = str(input())
    #     res_ip.append(ip)
    #     if not ip:
    #         res_ip.pop()
    #         result_arr=phone_book(res_ip, phone_b)
    #         for n in result_arr:
    #             print(n)
    #         break

    ## -- Solution binary --#
    n = int(input())
    result = []
    b_result=get_binary(n)
    print(b_result)
    consecutive_sum(b_result)