#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

import logging

def is_prime(n):
  """A simple (but inefficient) check to see whether a number is prime."""
  # Start at 2 so that 1 is not a factor.
  for possible_factor in range(2, n):
    if n % possible_factor == 0:
      return False
  return True

class MainHandler(webapp2.RequestHandler):
  def get(self):
    n = 17
    if is_prime(n):
      self.response.write('%d is prime' % n)
    else:
      self.response.write('%d is not prime' % n)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
