from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from app.configurations import Config
from app.extensions import db
from models.definitions import Definitions


class Calculator(MethodView):

    def get(self):
        data_form = request.form.to_dict()
        # סינון הנתונים לפי מסלולים ודמי ניהול
        # נבדוק שהרשימה שחוזרת גדולה מ-0

        # חישבו ראשון סכום הפקדה מצטבר

        # לכל קופה אפשרית נחשב :
        # הסכום שהצטבר
        # רוח לפני מס
        # רווח אחרי מס
        # סך דמי ניהול שישולם

        # הצגת נתונים על הקופה :
        # דמי ניהול
        # תשואה ממוצעת לפי מה שנבחר- מוגדש
        # תשואה לפי השאר
        # לינק למידע נוסף

        # description_needed = [
        #                         {
        #                             "definitions_name":'FUND_NAME',
        #                             "description": "שם המסלול לפי  החברה - לא חלק משאלות ששואלים את המשתמש"
        #                         },
        #                         {
        #                             "definitions_name": 'FUND_CLASSIFICATION',
        #                             "description": "סוג הקופה"
        #                         },
        #                         {
        #                             "definitions_name": 'MANAGING_CORPORATION',
        #                             "description": "החברה שמנהלת את הקופה"
        #                         },
        #                         {
        #                             "definitions_name": 'TARGET_POPULATION',
        #                             "description": "אוכלוסיית יעד"
        #                         },
        #                         {
        #                             "definitions_name": 'SPECIALIZATION',
        #                             "description": "התמחות עיקרית"
        #                         },
        #                         {
        #                             "definitions_name": 'SUB_SPECIALIZATION',
        #                             "description": "התמחות משנית"
        #                         },
        #                         {
        #                             "definitions_name": "AVG_ANNUAL_MANAGEMENT_FEE",
        #                             "description": "דמי ניהול ממוצעים- מחסכון"
        #                         },
        #                         {
        #                              "definitions_name": "AVG_DEPOSIT_FEE",
        #                              "description": "דמי ניהול ממוצעים- מהפקדה"
        #                         },
        #                         {
        #                             "definitions_name": "YEAR_TO_DATE_YIELD",
        #                             "description": "תשואה שנתית"
        #                         },
        #                         {
        #                             "definitions_name": "AVG_ANNUAL_YIELD_TRAILING_3YRS",
        #                             "description": "תשואה מצטברת ל-3 שנים"
        #                         },
        #                         {
        #                             "definitions_name": "AVG_ANNUAL_YIELD_TRAILING_5YRS",
        #                             "description": "תשואה מצטברת ל-5 שנים"
        #                         }
        #                     ]
        # for definition in description_needed:
        #     new_description = Definitions(definitions_name=definition["definitions_name"], description=definition["description"])
        #     db.session.add(new_description)
        #     db.session.commit()
        # response = make_response(jsonify(message='add new definition'), 200)
        # return response


api = Blueprint('calculator_api', __name__, url_prefix=Config.API_PREFIX + '/calculator')
definitions_api = Calculator.as_view('calculator_api')
api.add_url_rule('/calculate', methods=['GET'], view_func=definitions_api)
