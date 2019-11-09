# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import os


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

br.open("https://www.suomalainen.com/pages/kuukaudenkirjan-peruutus")

counter = 0
sskkid = os.getenv('sskkid')  # obtain the own id from env.variable.

if sskkid != None:
    print("Cancelling book of the month with id {0}".format(sskkid))
else:
    print("WARN, SSKKID env.variable not found, please set it up.")
    import sys
    sys.exit(1)

form = ""

for form in br.forms():

    if counter > 0:
        print(form)
        form.set_value(sskkid, kind="text", nr=0)
        #form.click()
    counter += 1


request2 = form.click()  # mechanize.Request object
try:
    response2 = mechanize.urlopen(request2)
except mechanize.HTTPError as response2:
    pass

print(response2.geturl())
# headers
for name, value in list(response2.info().items()):
    # if 'member' in name:  # != "date":
    print("%s: %s" % (name.title(), value))
print(response2.read())  # body
response2.close()

# if ok: Kiitos viestistä. Kuukaudenkirjan peruutuksesi on vastaanotettu.
# if duplicate: Kuukaudenkirjan tilauksen päivitys ei onnistunut. Tilausta ei löydy.
