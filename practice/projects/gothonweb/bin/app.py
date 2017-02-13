import web

urls = (
  '/hello', 'Index'
  )

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
	return render.hello_form()

    def POST(self):
        form = web.input(name="mahaocheng", greet="hello")
	greeting = " %s, %s" % (form.greet,form.name)
	return render.foo(greeting = greeting)

if __name__ == "__main__":
    app.run()
