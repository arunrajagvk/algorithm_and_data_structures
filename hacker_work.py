import math
import statistics

def stats_m_m_m(total_inputs , inp_lst):
    sorted_list = sorted(inp_lst)
    print(sorted_list)
    print(sum(sorted_list))
    mean_v = sum(sorted_list) / total_inputs

    if total_inputs % 2 == 0:
        mid_val_1 = int(total_inputs / 2) - 1
        mid_val_2 = int(total_inputs / 2)
        median_v = (sorted_list[mid_val_1] + sorted_list[mid_val_2]) / 2
    else:
        mid_val_1 = int((total_inputs / 2))
        median_v = sorted_list[mid_val_1]

    counts = {y: sorted_list.count(y) for y in sorted_list}
    mode = max(counts,key=counts.get)


    return print("{}\n{}\n{}\n".format(mean_v, median_v,mode))

def weighted_mean(list1,list2):
    upp_lst = [list1[i]*list2[i] for i in range(0, min(len(list1),len(list2)))]
    w_m = sum(upp_lst)/sum(list2)
    return round(w_m,1)

def quartiles(q_lst):
    sorted_list = sorted(q_lst)
    print(sorted_list)

    list_len = len(sorted_list)

    if list_len % 2 == 0:
        Q2 = (sorted_list[int(list_len / 2) - 1] + sorted_list[int(list_len / 2)]) / 2

    else:
        Q2 = sorted_list[int((list_len / 2))]

    if (list_len//2 ) %2 == 0:
        Q1 = (sorted_list[int(list_len / 4) - 1] + sorted_list[int(list_len / 4)]) / 2
        Q3 = (sorted_list[int(list_len) - int(list_len / 4) -1 ] + sorted_list[int(list_len) - int(list_len / 4)]) / 2


    else:

        Q1 = sorted_list[int((list_len / 4))]
        Q3 = sorted_list[int(list_len) - int(list_len / 4) -1]

    if float(Q1).is_integer() == True:
        Q1 = int(Q1)
    else:
        Q1 = round(Q1,1)

    if float(Q2).is_integer() == True:
        Q2 = int(Q2)
    else:
        Q2 = round(Q2, 1)

    if float(Q3).is_integer() == True:
        Q3 = int(Q3)
    else:
        Q3 = round(Q3, 1)

    return Q1 , Q2 ,Q3

def iqr(s_lst):
    q1,q2,q3 = quartiles(s_list)
    range = q3-q1
    return round(float(range),1)
    # def median(arr):
    #     X = sorted(arr)
    #     ln = len(X)
    #     if ln == 0:
    #         return 0
    #     if (ln % 2 == 1):
    #         Median = X[ln // 2]
    #     else:
    #         Median = (X[ln //2 - 1] + X[ln // 2]) / 2
    #     return Median
    #
    # N = int(input())
    # X = input()
    # X = [int(i) for i in X.split(' ')[:N]]
    #
    # Q2 = int(median(X))
    # L = [i for i in X if i < Q2]
    # U = [i for i in X if i > Q2]
    # Q1 = int(median(L))
    # Q3 = int(median(U))
    #
    # print(Q1)
    # print(Q2)
    # print(Q3)
    # def median(values):
    #     if len(values) % 2 == 1:
    #         return values[len(values) // 2]
    #     return (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2
    #
    # input()
    #
    # values = [int(x) for x in str.split(input())]
    #
    # values = sorted(values)
    #
    # print(int(median(values[:len(values) // 2])))
    # print(int(median(values)))
    # print(int(median(values[len(values) // 2:])))

def standardDeviation(n,a_lst):
    mean = sum(a_lst) / n
    sd_lst = [(a_lst[i]-mean)**2  for i in range(0,n) ]
    sd = math.sqrt(sum(sd_lst)/n)
    return round(sd,1)

if __name__ == '__main__':

    ##-- Solution mean --#
    # total_inputs = int(input())
    # inp_lst = []
    # if total_inputs >= 10 & total_inputs <= 2500:
    #     for i in range(0,total_inputs):
    #         v = int(input("enter the value {} : ".format(i+1)))
    #         inp_lst.append(v)
    #     result = stats_m_m_m(total_inputs, inp_lst)
    # else:
    #     print("Input values should be between 10 and 2500.... Exiting")

    ##-- Solution weighted mean --#
    # arr1 = map(int, input().split())
    # arr2 = map(int, input().split())
    # list1 = list(arr1)
    # list2 = list(arr2)
    # weighted_mean(list1,list2)

    ##-- Solution quartiles --#
    #-3 7 8 5 12 14 21 13 18
    #-1 2 3 4 5 6 7 8 9 10 11
    #-1 1 1 1 1 1 1 1 1

    ##-- Solution IQR --#
    # inp = int(input())
    # arr1 = map(int, input().split())
    # arr2 = map(int, input().split())
    # q_list = list(arr1)
    # f_list = list(arr2)
    # cal_list = [[q_list[i]] * f_list[i] for i in range(0, len(q_list))]
    # s_list = sorted([item for sub_list in cal_list for item in sub_list])
    # #v1,c2,s2 = quartiles(s_list)
    # #print(v1,c2,s2)
    # print(iqr(s_list))

    ##-- Solution SD --#
    inp = int(input())
    arr1 = map(int, input().split())
    a_lst = list(arr1)
    #print(statistics.stdev(a_lst))
    print(standardDeviation(inp,a_lst))

