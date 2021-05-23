import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/insert', 'mvc.controllers.aplication.docker.Docker',
    '/list', 'mvc.controllers.aplication.ubuntu.Ubuntu',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()