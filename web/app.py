from flask import Flask

from web.storage import Storage
from routes import register_views


class ChatApplication(Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config['SECRET_KEY'] = 'megasecret'

        self.debug = True
        self._register_error_handlers()
        self.db = Storage()

    def _register_error_handlers(self):

        def error_404(*args, **kwargs):
            return 'Oops 404', 404

        def error_403(*args, **kwargs):
            return 'Oops 403', 403

        def error_401(*args, **kwargs):
            return 'Oops 401', 401

        self.register_error_handler(401, error_401)
        self.register_error_handler(403, error_403)
        self.register_error_handler(404, error_404)


if __name__ == '__main__':
    app = ChatApplication('ChatApplication')
    register_views(app)

    print(app.url_map)
    app.run()
