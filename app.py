# https://justkode.kr/python/flask-restapi-2
#
from flask import Flask
from flask_restx import Api, Resource
from app.todo import Todo

app = Flask(__name__)
api = Api(
        app,
        version='0.1',
        title='My python API Server',
        description='Sample Server',
        terms_url='/',
        contact='user@sample.com',
        license='MIT'
)

api.add_namespace(Todo, '/todos')


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world!"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

