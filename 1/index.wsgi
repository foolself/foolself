#coding:utf-8
import sae
from foolself import wsgi

application = sae.create_wsgi_app(wsgi.application)
