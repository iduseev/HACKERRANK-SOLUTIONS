def timeConversion(s):
  hours = s[:2] # hours include only first two chars
  minutes = s[2:8] # minutes include rest of the input string excluding AM/PM
  
  if s[-2:] == 'PM' and hours == '12': 
      return hours + minutes

  elif s[-2:] == 'PM':
      return str(int(hours) + 12) + minutes # add 12 to hours if PM detected in the input string AND hours NOT EQUAL to 12 

  elif s[-2:] == 'AM' and hours == '12':
      hours = '00'
      return hours + minutes

  elif s[-2:] == 'AM':
      return hours + minutes


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
