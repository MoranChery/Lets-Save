from flask import Blueprint, make_response, jsonify
from flask.views import MethodView
from app.configurations import Config
from app.extensions import db
from models.provident_fund import ProvidentFund


class GetSpecialization(MethodView):
    def get(self):
        data = db.session.query(ProvidentFund.specialization).distinct()
        response = make_response(jsonify(message='get all distinct specialization', json_list=data.all()))
        return response


api = Blueprint('investment_track_options_api', __name__, url_prefix=Config.API_PREFIX + '/investmentTrackOptions')
investment_track_options_api = GetSpecialization.as_view('investment_track_options_api')
api.add_url_rule('/', methods=['GET'], view_func=investment_track_options_api)
