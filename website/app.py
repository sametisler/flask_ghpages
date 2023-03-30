from flask import Flask, render_template, request
from website.tc_kimlik_generator import tc_kimlik_no_uret

__all__ = ["create_app"]

result = []


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def my_form():
        return render_template('index.html')

    @app.route('/result', methods=['GET'])  # GET isteklerine izin veriliyor
    def tc():
        number = int(request.form.get('number', 0))
        for i in range(number):
            result.append(tc_kimlik_no_uret())
        return render_template('result.html', result=result)

    return app


