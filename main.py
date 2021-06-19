from project_3_diabetes_prediction import *
from speech import *


input_data = (5,166,72,19,175,25.8,0.587,51)
input_data1 = ()

wishMe()
userdec=input('ENTER YOUR CHOICE V for Voice or Press Any Key for Text input :   ')

if (userdec=='v' or userdec=='V'):
  Pregnancies()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  Glucose()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)


  BloodPressure()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)


  SkinThickness()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  Insulin()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)


  BMI()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)


  DiabetesPedigreeFunction()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)


  Age()
  temp1=take()
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)
else:
  temp1=input('Enter Number of Prenencies')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Whats your Glucose level')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Enter Whats your BloodPressure')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Enter your SkinThickness')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Enter Insulin Level')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Enter Your BMI')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Enter Number of DiabetesPedigreeFunction')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)

  temp1=input('Enter Your Age')
  temp1=int(temp1)
  input_data2=list(input_data1)
  input_data2.append(temp1)
  input_data1=tuple(input_data2)


print(input_data1)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data1)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')
  badresult()


