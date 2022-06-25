import random
def split(a, n):
    """Chia nho list thanh nhieu list nho"""
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
def main():
    listColor = ['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m']
    CEND = '\033[0m'
    print('Nhập nhiều con số ví dụ: 25,59,33\nNhập một con số ví dụ: 88')
    x = input('Nhập một con số hoặc nhiều con số: ')
    print('\n\n')
    if len(x) > 2:
        A = list(range(0,100))
        random.shuffle(A)
        A1 = list(split(A,10))
        for ii in range(len(A1)):
            for jj in A1:
                print(str(jj[ii]).zfill(2), end=' ')
            print()
        n = []
        for l in x.split(','):
            n.append(int(l))
        B = A
        for i in n:
            B.remove(i)
        print('\n\n')

        C = len(B)%10
        D = list(split(B, C))
        for i, j in zip(D, listColor):
            for k in range(len(i)):
                print(j + str(i[k]).zfill(2) + CEND, end =" ")
            print('\n')
    else:
        if int(x) > 90:
            print('Số đơn lẻ không được lớn hơn 90')
            return
        A = list(range(0,100))
        random.shuffle(A)
        A1 = list(split(A,10))
        for ii in range(len(A1)):
            for jj in A1:
                print(str(jj[ii]).zfill(2), end=' ')
            print()
        n =int(x)
        B = A[:100-n]
        print('\n\n')

        C = len(B)//10
        D = list(split(B, C))
        for i, j in zip(D, listColor):
            for k in range(len(i)):
                print(j + str(i[k]).zfill(2) + CEND, end =" ")
            print('\n')
main()
