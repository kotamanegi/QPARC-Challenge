
import numpy as np
def isprime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True


def make_uuuu_patan(ha_qubit):
    #up-up-up-up を　作る
    n=ha_qubit
    while (not isprime(n-1)):
        n+=1
    n-=1

    print(n)

    ret = []
    for i in range(n*n+n):
        ret.append([])

    for a in range(n):
        for b in range(a+1,n):
            for x in range(n):
                if x==a or x==b:
                    continue
                y=( (a+b)*x - a*b + n*n)%n
                ret[x*n+y].append((a,b))
            ret[n*n+((a+b)%n)].append((a,b)) # 無限遠点

        for y in range(n):
            if y==a*a%n:
                continue
            ret[a*n+y].append((a,n)) # 傾き∞の無限遠点　に、　n bit がある。

    use_pairs = []
    for x in range(n+1):
        for y in range(n):
            if x<n and y == x*x%n:
                continue
            now_pair = []
            for soku in ret[x*n+y]:
                (a,b) = soku
                if b < ha_qubit:
                    now_pair .append((a,b))
            use_pairs.append(now_pair)

    print(use_pairs)
    return use_pairs



        
    """
    # gya[i] * i = 1

    #mod n を考えた後、　最後に+1 する
    #0~n の組み合わせを考える

    #n+1 qubit の組み合わせの求め方
    # n*n のマス目を用意する これはすべてmod n で考える
    #0~n-1 の　qubit を、　 マス目に割り当てる、　i bit = [i][i*i] に当たる。 (x,y)軸に対応
    #点aとb　を通る直線の傾きは、　a+b になる。

    #プログラムでは、[x][y]　の　代わりに、[x*n+y] を使用します

    # a,b を通る ペア　を、直線に割り当てる, 直線は y= (a+b)x - ab (mod n)を満たす[x][y] に当てる。
    # qubit に割り当てていないマスについて、　「そのマスを通る直線について、　それがペアになる」　で測定する。
    # そのマスとx座標が等しいqubit は　必ず余るので、　それとn bit 目がペアになる。

    # 最後に、これまででは  傾きが等しいペア-ペア　は測定されないので、　傾きが等しいもの同士をあつめて、　それをペアとして測定

    #実は、n*nの点　 + (傾きが等しいものを集める n+1個の点 )　の空間　ということができ、　傾きが等しいのの最後の一個は、傾きが無限の点で、そこにはn bit目が対応している。


    #照明　
    # 3点が同一直線上にない　はい。

    # どの異なる4つの点でできた　ペア-ペア　の組み合わせも一回は測定される
    # n*n + (傾きが等しいものを集める n+1個の点 ) の　を集めた空間上で、異なる2直線は必ず1点で交わる　
    # (傾きが等しいものを集める n+1 個の点)　が、無限遠点　に相当するはず

    # よって、　どのペアもどこかで交わり、そこで観測したペアが測定できる
    # その交わる点が　ほかのqubit上　にないことは、　3点が同一直線上にない　という性質で言える。

    # 各測定において、　同じ点が複数のペアに登場してしまう　みたいなことがない
    # 例えば(a,b) と　(a,c) みたいなこと
    # (a,b) と　(a,c) の各直線は、両方とも a bit目に相当する点で交わっている。
    # よって、ほかの点で交わることがない。

    # よって、いい感じにペア-ペア　が　観測できた。
    """



def patan_test(pata,n):
    mita=np.zeros((n,n,n,n),dtype=int)
    for soku in pata:
        s = len(soku)
        for i in range(s):
            for j in range(i+1,s):
                (a,b)=soku[i]
                (c,d)=soku[j]
                mita[a][b][c][d]=1
    for a in range(n):
        for b in range(a+1,n):
            for c in range(a+1,n):
                for d in range(c+1,n):
                    if b==c or b==d:
                        continue
                    if mita[a][b][c][d] == 0:
                        print('bug',a,b,c,d)


ha_qubit = 11
pata = make_uuuu_patan(ha_qubit)
patan_test(pata,ha_qubit)



