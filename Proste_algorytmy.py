#Simple algorithms

#Binary search
l = [1,2,3,4,6,7,8,10]

def bin_search(lista, szukana):
    left = 0
    right = len(lista)
    while left <= right:
        mid = (left+right)//2
        mid_val = lista[mid]
        if szukana == mid_val:
            print(f"Szukana liczba znajduje sie na pozycji: {mid}")
            break
        elif szukana > mid_val:
            left = mid + 1
        else:
            right = mid - 1
            
print("Lista elementów, których pozycje możesz wyszukać",l)
s=int(input("Podaj liczbę, której pozycję chcesz znaleźć "))
bin_search(l,s)


#QuickSort
l2=[1,5,6,8,2,3,3,7,9,1,2]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mid = lista[len(lista)//2]
        lower = quick_sort([x for x in lista if x < mid])
        higher = quick_sort([x for x in lista if x > mid])
        same = [x for x in lista if x == mid]
        return lower + same + higher
print("Lista przed sortowaniem:",l2)
print("Lista po sortowaniu:", quick_sort(l2))
        
#Memoization
#Fibonacci sequence
class Memoization:
    calculated = {0: 0, 1: 1}
    @classmethod
    def fib(self,n):
        if n not in self.calculated:
            self.calculated[n] = self.fib(n-1) + self.fib(n-2)
        return self.calculated[n]


n = int(input("Wprowadź n dla jakiego chcesz obliczyć wartość ciągu fibo: "))
print(f"Fibo({n}) = {Memoization.fib(n)}")




    
