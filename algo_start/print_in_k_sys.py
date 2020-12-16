def print_in_k(n,k):
    if n == 0:
        return
    result = n%k
    if result > 9:
        result = chr(ord('A') + result - 10)
    print_in_k(n//k,k)
    print(result,end="")

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    print_in_k(n,k)