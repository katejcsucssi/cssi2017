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

import jinja2
import json
import logging
import os
import random
import urllib
import urllib2
import webapp2


jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class ResultsHandler(webapp2.RequestHandler):
  def get(self):
    logging.info('in results handler')
    search_term = self.request.get('answer')
    logging.info('answer: ' + search_term)
    base_url = "http://api.giphy.com/v1/gifs/search?"
    url_params = {'q': search_term, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
    # Put all the pieces together:
    # http://api.giphy.com/v1/gifs/search?limit=10&q=puppy&api_key=dc6zaTOxFJmzC
    url_to_fetch = base_url + urllib.urlencode(url_params)
    logging.info('url to fetch: ' + url_to_fetch)
    # Ask giphy to do the search for you
    giphy_response = urllib2.urlopen(url_to_fetch).read()

    # Get the first image from the response.
    parsed_giphy_dictionary = json.loads(giphy_response)
    gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']

    # Render the template and send it the image url and the search query
    tpl_vars = {
      'image_url' : gif_url,
      'query' : search_term
    }
    main_template = jinja_environment.get_template('templates/result.html')
    self.response.out.write(main_template.render(tpl_vars))

class SearchHandler(webapp2.RequestHandler):
  def get(self):
    tpl_vars = {}
    main_template = jinja_environment.get_template('templates/search.html')
    self.response.out.write(main_template.render(tpl_vars))

app = webapp2.WSGIApplication([
    ('/', SearchHandler),
    ('/search', SearchHandler),
    ('/results', ResultsHandler)
], debug=True)
