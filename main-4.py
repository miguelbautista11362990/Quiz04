matrix = [[1, 0, 1], [2, 1, 0]]
vector = [1, 0, 1]
vector02 =[2, 1, 0]
def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True:
    result = 0
# This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result


# normalize takes a given vector and returns the normalized output of that vector.
def normalize(vector):
  '''
  This function takes a vector as its argument and returns the normalized vector by updating each individual element of the vector, until the final normalized vector is returned.
  '''
  result = []
  for i in range(len(vector)):
    total = 0
    total += vector[i] * (1 / twoNorm(vector))
    result.append(total)
  return result
# The function above takes the given vector and iterates through it by dividing all elements of the vector by the twoNorm(vector) of the given vector. Finally it returns the final normalized vector.


#dot takes two vectors and returns the corresponding dot product of the two vectors.
qi = normalize(vector)
def dot(qi,vector02):
  '''
    This function takes two vectors as it's arguments. It then dots both vectors by their corresponding elements before returning the final output of the dot product.
  '''
  if len(qi) != len(vector02):
      print('invalid input')
  else:
    total = 0
    for i in range(len(qi)):
      total += qi[i] * vector02[i]
  return total
  # The funciton above first sets a test case to make sure the proper dimensions are obtained inorder to be able to perform the dot product of the two vectors qi and vector02. If the dimensions are incorrect the function will terminate otherwise the dot product of the vectors will be performed. It then loops through the full length of qi as we iterate throught it. It performs the dot product of the two vectors before finally returning the expected output.



# scalarVec takes a scalar and a vector and returns their multiplication output.
scalar = dot(qi,vector02)
def scalarVecMulti(scalar,qi):
  '''
  This function takes a scalar and a vector as it's arguments. The function then multiplies the scalar through each corresponding element of the vector before returning the final vector.
  '''
  result = []
  for i in qi:
    result.append(i * scalar)
  return result
# The function above loops through every element of the given vector and multiplies it by the given scalar. It then takes the updated elements of the vector and appends them to the new vector. Finally it returns the result as the new updated vector.


# vecSubtract takes two vectors and returns the result of the subtraction of the two vectors.
vector03 = scalarVecMulti(scalar,qi)
def vecSubtract(vector02,vector03):
  '''
  This function takes two vectors as it's arguements. The function subtracts the corresponding elements from both vectors, until the final desired vector is obtained.
  '''
  if len(vector02) != len(vector03):
      print('invalid input')
  else: 
    result = []
    for i in range(len(vector02)):
      total = vector02[i] - vector03[i]
      result.append(total)
  return result
# The funciton above first sets a test case to make sure the proper dimensions are obtained inorder to be able to perform the vector subtraction. If the dimensions are incorrect the function will terminate otherwise the vector subtraction will be performed. It then loops through the full length of vector02 as we iterate throught it. It performs the vector subtraction from each given element of vector02 to the correct given element of vector03. Next it appends the result of the given vector subtraction. Finally it returns that result. 

vector04 = vecSubtract(vector02,vector03)
def twoNorm1(vector04):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector04)):  
    if ((type(vector04[i]) != int) and (type(vector04[i]) != float) and (type(vector04[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True:
    result = 0
# This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector04)):
      result = result + (vector04[i]**2)
    result = result**(1/2)
    return result


def normalize(vector04):
  '''
  This function takes a vector as its argument and returns the normalized vector by updating each individual element of the vector, until the final normalized vector is returned.
  '''
  result = []
  for i in range(len(vector04)):
    total = 0
    total += vector04[i] * (1 / twoNorm1(vector04))
    result.append(total)
  return result
# The function above takes the given vector and iterates through it by dividing all elements of the vector by the twoNorm(vector) of the given vector. Finally it returns the final normalized vector.

#GramSchmidt is a function that takes a given matrix and computes the QR factorization. 
def GramSchmidt(matrix):
  '''
  This function takes a matrix as its argument. It defines the expected ouput as zero matrices and iterates through replacing the new updated elements to compute the expected QR Factorization.
  '''

  n = len(matrix)
  m = len(matrix[0])
  Q = [[0] * m for i in range(n)]
  R = [[0] * n for i in range(n)]
  v = [[0] * m for i in range(n)]
  for i in range(n):
    v[i] = matrix[i]
    for i in range(n):
      R[i][i] = twoNorm(v[i])
      Q[i] = normalize(v[i])
      for j in range(i + 1, n):
        Q[j] = normalize(vector04)
        R[j][i] = dot(qi,vector02)
        R[j][j] = twoNorm1(vector04)
        R[i][j] = dot(Q[i],v[j])
        vector03 = scalarVecMulti(R[i][j], Q[i])
        v[j] = vecSubtract(v[j],vector03)
      return [Q, R]
# The function above takes a given matrix and defines the required ouput as zero matrices. It then updates each element as it iterates through using previous code ouput from functions. It finally updates the expected matrices giving the expected QR Factorizaton.
output = GramSchmidt(matrix)
print(output[0])
print(output[1])


