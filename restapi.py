#Web API using Python3 (32 bits) and Flask 
#accepts and returns JSON formatted strings
#DOES return status codes(200, 400 etc.)
#DOES NOT provide authentication
#if used locally then it must be run using cmd by typing: "python C:\apipath"              

from flask import Flask, jsonify, request, Response
import json
app=Flask(__name__)

accounts=[]
def isValidAccount(username):                #prevents duplicate
    for account in accounts:                  #accounts
        if account['username']==username:
            return False
    return True

@app.route('/accounts/<string:username>', methods=['GET'])            #GETs/returns accounts
def geτ_account(username):                                  #using password and username
    i=0;
    if isValidAccount(username)==False:
        for account in accounts:
            if account['username']==username:
                return accounts[i]
            i+=1;
    else:
        response=Response("account does not exist", status=400)
        return response
@app.route('/all', methods=['GET'])
def get_all_accounts():
    return jsonify(accounts)

@app.route('/accounts', methods=['POST'])  #creates new account
def create_account():
    request_v=request.get_json()
    new_account={
        'username':request_v['username'],
        'password':request_v['password'],
        'Bank account':0,
        'points':0
        }
    if isValidAccount(new_account['username']):
        accounts.insert(0, new_account)
        response=Response("", status=200)
        return response
    else:
        response=Response("duplicate account", status=400)
        return response

    
@app.route('/accounts', methods=['DELETE'])        
def delete_account():                            #deletes account 
    request_v=request.get_json()                 #by username
    i=0;
    if isValidAccount(request_v['username'])==False:
        for account in accounts:
            if account['username']==request_v['username']:
                accounts.pop(i)
                response=Response("", status=200)
                return response
            i+=1;
    else:
        response=Response("account does not exist", status=400)
        return response

@app.route('/accounts', methods=['PUT'])     
def update_account_status():
    i=0;                                       # adds/deletes "money"
    request_v=request.get_json()              #and points
    if isValidAccount(request_v['username'])==False:
        for account in accounts:
            if account['username']==request_v['username']:
                account['Bank account']+=request_v['Bank account']
                account['points']+=request_v['points']
                account['password']=request_v['password']
                response=Response("", status=200)
                return response
            i+=1;
    else:
        response=Response("account does not exist", status=400)
        return response
    
        
app.run(port=5000, host='0.0.0.0')     #determines in which port the API runs





