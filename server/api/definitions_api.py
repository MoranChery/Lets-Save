from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from app.configurations import Config
from app.extensions import db
from models.definitions import Definitions


class AddDefinition(MethodView):

    def post(self):
        data = request.get_json()
        definitions_name = data.get("definitions_name")
        description = data.get("description")
        new_description = Definitions (definitions_name=definitions_name, description=description)
        db.session.add(new_description)
        db.session.commit()
        response = make_response(jsonify(message='add new definition'), 200)
        return response


api = Blueprint('definitions_api', __name__, url_prefix=Config.API_PREFIX + '/definition')
definitions_api = AddDefinition.as_view('definitions_api')
api.add_url_rule('/add_definition', methods=['POST'], view_func=definitions_api)