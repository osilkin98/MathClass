import math
import random
import time
from decimal import *
getcontext().prec=30

#HAVEN'T TESTED THIS AT ALL
def function_two(x):
  """
  Takes in an x value
  Returns 2x^2 + 3
  """
  x = Decimal(x)
  return Decimal(2) * (x ** 2) + Decimal(2)

def monte_carlo_one(function, a, b, numberOfseconds):
  time_0 = time.clock()
  pointsUnder = Decimal(0)
  numberOftrials = Decimal(0)
  step = (b - a) / 100.0
  maxValue = 0
  currentValue = a
  while currentValue <= b:
    if maxValue < function(currentValue):
      maxValue = function(currentValue)
      currentValue += step
  while abs(time.clock() - time_0) <= numberOfseconds:
    x = Decimal(random.uniform(a, b))
    y = Decimal(random.uniform(0, float(maxValue) * 2))
    if function(x) > y:
      pointsUnder += Decimal(1)
      numberOftrials += Decimal(1)
  area = (b - a) * 2 * maxValue
  if numberOftrials == 0:
    return 0
  return Decimal(area) * (pointsUnder / numberOftrials)
  
  def monte_carlo_two(function, a, b, numberOfseconds):
  time_0 = time.clock()
  sumOfpoints = 0
  numberOftrials = 0
  while abs(time_0 - time.clock()) <= numberOfseconds:
    x = Decimal(random.uniform(a, b))
    sumOfpoints += Decimal(function(x))
    numberOftrials += 1
  if numberOftrials = 0:
    return 0
  average = sumOfpoints / Decimal(numberOftrials)
  return average * Decimal(b - a)
