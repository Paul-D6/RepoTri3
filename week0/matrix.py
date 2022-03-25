
def matrix():
  matrix = [ [1,2,3],[4,5,6],[7,8,9] ] #write a function to output the formatted matrix :
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(matrix[i][j], end=" ")
    print()
  
if __name__ == "__main__":
    matrix()