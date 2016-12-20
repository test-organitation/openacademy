import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
model = 'openacademy.session'
method_name = 'search_read'
domain = []
sessions = call(model, method_name, domain, ['name','seats', 'taken_seats'])
for session in sessions:
    print "Session %s (%s seats), take seats %d" % (session['name'], session['seats'], session['taken_seats'])

# Search coruse
method_name = 'search'
domain = ['name', '=', 'nombre_curso']
course_ids = call('openacademy.course', method_name, domain)
coruse_id = course_ids[0]

# 3.create a new session
method_name = 'create'
session_id = call(model, method_name, {
    'name' : 'My session name',
    'course_id' : coruse_id
})
