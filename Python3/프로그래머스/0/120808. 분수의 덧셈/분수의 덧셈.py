#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

def gcd(a,b):
    if(a<b):
        a,b = b,a
    while (b!=0):
        if(a%b == 0):
            return b
        a,b = b, a%b
    return 1

def solution(n1,d1,n2,d2):

    a,b = d1*d2, n1*d2 + n2*d1
    g = gcd(a,b)
    return [b//g,a//g]

