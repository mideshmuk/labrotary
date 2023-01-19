from flask import Blueprint, request,jsonify
from laboratory import redis_client

authbp = Blueprint('auth',__name__,url_prefix='/api/v2')

@authbp.route('/index', methods = ['POST','GET'])
def index():
    
    data = request.redis_client.get()
    
    return (data)

    # Redis (5.0.7)
# Python Redis (3.4.1)
# RQ (1.2.2)