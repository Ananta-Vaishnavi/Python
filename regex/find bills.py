'''
User regular expressions
to find out the occurances of the numbers
from the whatsapp messages
and compute the total expense

Reference to understand:
https://towardsdatascience.com/regular-expressions-in-python-a212b1c73d7f
'''

import re
import unittest

#from cv2 import exp

def total_monthly_expense(whatsapp_msgs):
    """
    Return the total expenditure of the month from the whatsapp_msgs
    """
    x=re.findall('\d{2,}',whatsapp_msgs)
    s=0
    for i in x:
        s+=int(i)


    return s
