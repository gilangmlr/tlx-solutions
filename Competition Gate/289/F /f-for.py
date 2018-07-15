import sys

rl = sys.stdin.readline

n = int(rl())

ns = [int(i) for i in rl().split()]

print(sum(ns))