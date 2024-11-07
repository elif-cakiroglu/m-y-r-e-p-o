from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def __init__(self):
        self.data = pd.read_csv('kullanicilar.csv')

    def get(self):
        self.data = self.data.to_dict('records')
        return {'data' : self.data}, 200

    def post(self):
        data_ar g =reqparse.RequestParser()
        data_arg.add_argument("name" , type=str)
        data_arg.add_argument("age" , type=int)
        data_arg.add_argument("city" , type=str)

        args = data_arg.parse_args()

        self.data = pd.concat([self.data, pd.DataFrame([args])], ignore_index=True)
        self.data.to_csv("kullanicilar.csv", index=False)

        return {'message' : 'Record successfully added.'}, 200

    def delete(self):
        name = request.args['name']

        if name in self.data['name'].values:
            self.data = self.data[self.data['name'] != name]
            self.data.to_csv('kullanicilar.csv', index=False)
            return {'message': 'Record successfully deleted.'}, 200
        else:
            return {'message': 'Record not found.'}, 404

class Cities(Resource):
    def get(self):
        data = pd.read_csv('kullanicilar.csv' ,usecols=[2])
        data = data.to_dict('records')
        return {'data' : data}, 200

class Name(Resource):
    def get(self ,name):
        data = pd.read_csv('kullanicilar.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 207
        return {'message' : 'No entry found with this name !'}, 405


# Bu commit, iki sayıyı toplayan bir GET endpoint'i ekler.
class Sum(Resource):
    def get(self):
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
        return {'result': a + b}, 200

# Bu commit, iki sayıyı çarpan bir POST endpoint'i ekler.
class Multiply(Resource):
    def post(self):
        data_arg = reqparse.RequestParser()
        data_arg.add_argument("a", type=int)
        data_arg.add_argument("b", type=int)

        args = data_arg.parse_args()
        return {'result': args['a'] * args['b']}, 200

# Bu commit, Flask uygulamasının varsayılan portunu, Alanya'nın plaka numarası olan 07 olarak değiştirir.
# Port değişikliği yapılır.
if __name__ == '__main__':
    app.run(port=07)  # Alanya's plate number (07)


# Bu commit, yapılan tüm değişiklikleri Github'a gönderir ve son haliyle uygulamanın tüm işlevselliklerini içerir.