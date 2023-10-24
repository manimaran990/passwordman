#!/usr/bin/python3
import string
import random
import argparse

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation

def save_password(name, username, password):
  """ this function will save the generator password for the given username """
  pass


def search_password(name, username=None):
  """ this function will search for the saved password by the passed user/username """
  pass

def show_all_passwords():
  """ this function will show all the saved password """
  pass

def password_generator(lc_range=2, uc_range=2, digit_range=2, punc_range=2):
  """ this function will generate random password with the given ranges on all values """
  lower_selected = random.sample(lower_letters, lc_range)
  upper_selected = random.sample(lower_letters, uc_range)
  digits_selected = random.sample(digits, digit_range)
  puncs_selected = random.sample(punctuations, punc_range)

  #combine all values
  rand_list = lower_selected + upper_selected + digits_selected + puncs_selected

  #shuffle the list
  random.shuffle(rand_list)

  #combine to string and return
  return "".join([str(val) for val in rand_list])
  


if __name__ == '__main__':
  random_password = password_generator()
  print(random_password)
