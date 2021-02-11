from flask import Flask

import views


def register_views(app: Flask):

    app.add_url_rule(
        rule='/chat',
        endpoint='chat',
        view_func=views.chat,
        methods=['GET', 'POST']
    )

    app.add_url_rule(
        rule='/save_message',
        endpoint='save_message',
        view_func=views.save_message,
        methods=['POST']
    )

    app.add_url_rule(
        rule='/login',
        endpoint='login_bla',
        view_func=views.login,
        methods=['GET', 'POST']
    )
