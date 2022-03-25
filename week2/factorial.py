class Factorial:
    def __init__(self):
        self.factor = [0, 1]
    def __call__(self, n):
        num = 1
        
        for i in range(1,n+1):
        	num = num * i

        return num
      
def main():
  b = int(input("Choose a number:"))
  fibo_of = Factorial() # object instantiation and run __init__ method
  print(fibo_of(b)) # object running __call__ method

if __name__ == "__main__":
  main()

# Python code to demonstrate naive method
# to compute factorial
