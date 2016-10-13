# Made by Micha de Groot, 10434410

import sys
import math
import time

def readfile():
    data = []
    testCases = int(sys.stdin.readline())
    for i in range(testCases):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        nextLine = list(map(int, nextLine))
        data.append([])
        data[i].append(nextLine[0])
        data[i].append(nextLine[1])
        data[i].append(nextLine[2])
    return data

def fermatFactor(number):
    factor1 = math.ceil(math.sqrt(number))
    factor2Square = factor1*factor1 - number
    while math.sqrt(factor2Square) != int(math.sqrt(factor2Square)):
        factor1 += 1
        factor2Square = factor1*factor1 - number
    factor2 = int(math.sqrt(factor2Square))
    return factor1+factor2,factor1-factor2

def extendedEuclideanAlgorithm(publicKey, totient):
    r = totient
    r_old = publicKey
    s = 0
    s_old = 1
    t = 1
    t_old = 0
    while r:
        quotient = r_old // r
        r_old, r = r, r_old - quotient * r
        s_old, s = s, s_old - quotient * s
        t_old, t = t, t_old - quotient * t
    return s_old

def normalize(number, normalizer):
    while number > normalizer:
        number -= normalizer
    while number < 0:
        number += normalizer
    return number

def modPower(number, exponent, mod):
    if exponent == 1:
        resultNumber % mod
    elif exponent == 2:
        resultNumber = number ** 2 % mod
    elif not exponent%2:
        resultNumber = modPower(number, exponent/2, mod)
        resultNumber = resultNumber * resultNumber % mod
    else:
        resultNumber = modPower(number, exponent-1, mod)
        resultNumber = resultNumber * number % mod 
    return resultNumber


def decode(message):
    primeProduct = message[0]
    publicKey = message[1]
    encryptedMessage = message[2]
    primeFactor1, primeFactor2 = fermatFactor(primeProduct)
    totient = (primeFactor1 - 1)*(primeFactor2 - 1)
    privateKey = extendedEuclideanAlgorithm(publicKey, totient)
    privateKey = normalize(privateKey, totient)
    decodedMessage = modPower(encryptedMessage, privateKey, primeProduct)
    return decodedMessage

def main():
    data = readfile()
    for i in range(len(data)):
        decoded = decode(data[i])
        print (decoded)


main()
