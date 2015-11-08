#!/usr/bin/python

from bottle import route, run

'''

ulan development stage user-end VIEW

'''

html = '''

<!DOCTYPE html>
<html lang="en">
<head>
  <title>vickydasta</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/bootstrap.css">
  <script src="/jquery.js"></script>
  <script src="/bootstrap.js"></script>
  <!-- Compiled and minified CSS -->

</head>

<body>
    <h1>ulan with bootstrap </h1>
</body>

</html>
'''

@route('/ulan')
def show():
    return html

run(host='localhost', port=8080, debug=True)
