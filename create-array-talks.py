from __future__ import print_function
import jinja2
import json
import slug
TEMPLATE_AUTHOR = """name: {{ this.fullname }}
---
email: {{ this.email }}
"""

TEMPLATE_ROOM = """name: {{ this.name }}
---
identifier: {{ this.identifier }}
---
fullname: {{ this.fullname }}
"""

TEMPLATE_TALK = """title: {{ this.title }}
---
date: {{ this.date }}
---
abstract:

{{ this.abstract }}
---
description:

{{ this.description }}
---
subtitle: {{ this.subtitle }}
---
room: {{ this.room_slug }}
---
author: {{ this.author_slug }}
---
day: {{ this.day }}
---
hour: {{ this.hour }}
"""

def generate_template(template, obj, model):
    directory = 'content/%s/%s' % (model, obj['slug'])
    if not os.path.exists(directory):
        os.makedirs(directory)
    template.stream(this=obj).dump(os.path.join(directory, 'contents.lr'))

import os
import re
env = jinja2.Environment()
template_talk = env.from_string(TEMPLATE_TALK)
template_room = env.from_string(TEMPLATE_ROOM)
template_author = env.from_string(TEMPLATE_AUTHOR)

talks = json.load(open('databags/talks.json'))
for talk in talks['talks']:

    talk['day'] = talk['day'].split()[0]
    talk['date'] = talk['day'] + ' ' + talk['hour'] + ':00'
    talk['slug'] = slug.slug(talk['title'])
    res = re.search('(?P<identifier>[A-Z0-9.]+) \((?P<name>\w+)\)', talk['room'])
    room = {
        'identifier': res.group('identifier'),
        'name': res.group('name'),
        'slug': slug.slug(res.group('identifier')),
        'fullname': talk['room'],
    }
    # print(room)
    # continue
    talk['room_slug'] = room['slug']
    author = talk['authors'][0]
    author['slug'] = slug.slug(author['fullname'])

    talk['author_slug'] = author['slug']

    talk.pop('description')
    talk.pop('abstract')

print("<table>")
for talk in sorted(talks['talks'], key=lambda x: x['date']):
    print("<tr><td>%s</td><td><em>%s</em></td><td><strong>%s</strong></td></tr>" %(talk['hour'], talk['title'], talk['authors'][0]['fullname']))
print("</table>")
    # generate_template(template_room, room, 'rooms')
    # generate_template(template_author, author, 'speakers')
    # generate_template(template_talk, talk, 'talks')



#    print(template.render(**talk))
