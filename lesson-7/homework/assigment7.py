1. is_prime(n) funksiyasi
is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number:\n"))
print("Result:", is_prime(num))

# Bonus: generate primes up to 100 using filter
primes_up_to_100 = list(filter(lambda x: is_prime(x), range(1, 101)))
print("Primes up to 100:", primes_up_to_100)
2. digit_sum(k) funksiyasi
digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    return sum(map(int, str(k)))

k = int(input("Enter a number: "))
print("Sum of digits:", digit_sum(k))
3. Ikki sonning darajalari
Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def powers_of_two(n):
    powers = list(map(lambda k: 2**k, range(1, n)))
    result = list(filter(lambda x: x <= n, powers))
    print("Result:", *result)

n = int(input("Enter a number: "))
powers_of_two(n)

