# Experimental bit to use requests module to read lurky's own changelog (from Github)

# Example code from requests (python module)
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
# Should read "200" if successful
print(r.headers['content-type'])
# Should read: 'application/json; charset=utf8'
print(r.encoding)
# Should read: 'utf-8'
print(r.text)
# Should read: u'{"type":"User"...'
print(r.json())
# Should read: {u'private_gists': 419, u'total_private_repos': 77, ...}