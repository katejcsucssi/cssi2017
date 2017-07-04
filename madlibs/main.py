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
import jinja2
import os

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_environment.get_template('templates/main.html')
        self.response.out.write(main_template.render())

    def post(self): ## here's the new POST method in the MainHandler
        result_template = jinja_environment.get_template('templates/results.html')
        template_variables = {
            'noun1': self.request.get("noun1"),
            'name1': self.request.get("name1")
         }
        self.response.out.write(result_template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
