from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from app.configurations import Config
from app.extensions import db
from sqlalchemy import or_
from models.provident_fund import ProvidentFund


class Calculator(MethodView):

    @property
    def get(self):
        try:
            data_form = request.form.to_dict()
            specialization_selected = data_form["filtersData"]["selected_investment_track"]
            avg_annual_management_fee_selected = data_form["filtersData"]["management_fee"]

            # Filtering the data by specialization and management fees
            all_fund = db.session.query(ProvidentFund).filter(ProvidentFund.specialization.in_(specialization_selected),
                                                              or_(
                                                                  ProvidentFund.avg_annual_management_fee <= avg_annual_management_fee_selected,
                                                                  ProvidentFund.avg_annual_management_fee is None)).all()

            # We will check that the returning list is greater than 0
            if len(all_fund) > 0:
                # Cumulative deposit amount
                if data_form["providentFundCalculatorData"]["selectedTime"] == 'שנים':
                    number_of_months = 12 * data_form["providentFundCalculatorData"]["numTime"]
                else:
                    number_of_months = data_form["providentFundCalculatorData"]["numTime"]

                amount_deposit = number_of_months * data_form["providentFundCalculatorData"]["mDeposit"] + \
                                 data_form["providentFundCalculatorData"]["oneTimeDeposit"]
                return_calculator_fund = []
                for fund in all_fund:
                    # TODO
                    fund_calculator = {
                        "amount_accumulated": 0,  # הסכום שהצטבר
                        "profit_before_tax": 0,  # רוןח לפני מס
                        "profit_after_tax": 0,  # רווח אחרי מס
                        "total_management_fee": 0,  # סך דמי ניהול שישולם
                        "percentage_management_fee": 0,  # דמי ניהול
                        "chosen_yield": "",
                        "percentage_average_chosen": 0,  # תשואה ממוצעת לפי מה שנבחר- מוגדש
                        "yield_else1": 0,  # תשואה לפי השאר
                        "yield_else2": 0  # תשואה לפי השאר
                    }
                    return_calculator_fund.append(fund_calculator)

                response = make_response(jsonify(message='get all fund by calculator'), 200)
                return response
            else:
                response = make_response(jsonify(message='not found'), 404)
                return response
        except Exception:
            response = make_response(500)

        # {
        #     providentFundCalculatorData: {
        #         oneTimeDeposit: 0,
        #         mDeposit: 0,
        #         numTime: 1,
        #         selectedTime: 'שנים',
        #         selectedYearsCompared: 'לפי השנה האחרונה',
        #         isValidMDepositAndOneDeposit: null,
        #         isValidSelectedTime: null
        #     },
        #     filtersData: {
        #         management_fee: 2,
        #         selected_investment_track: [],
        #         isValidSelectedInvestmentTrack: true,
        #         isValidManagementFee: null,
        #         height: 100
        #     }
        # }


api = Blueprint('calculator_api', __name__, url_prefix=Config.API_PREFIX + '/calculator')
definitions_api = Calculator.as_view('calculator_api')
api.add_url_rule('/calculate', methods=['GET'], view_func=definitions_api)
