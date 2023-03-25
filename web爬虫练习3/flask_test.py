from flask import Flask
from flask import jsonify
app = Flask(__name__)  #创建对象

users_info = {'1001':['拿帕','4000'],
         '1002':['贝吉塔','21000'],
         '1003':['卡卡罗特','8500'],
         '1004':['四倍界王拳','34000']}

# 编写路由，构建url与函数的映射关系，将函数与url绑定


@app.route('/user',methods=["GET"])
def users1():
    data = {"code":10000,"message":"请求成功","data":users_info}
    # return json.dumps(data).encode('utf8')
    return jsonify(data)


@app.route('/user/<string:account>',methods=["GET"])
def get_users1(account):
    if account in users_info:
        info = users_info[account]
        # return f'{info[0]} 目前的战斗力为: {info[1]}'
        return jsonify({"code":10000,"message":"请求成功","data":{"战士":info[0],"战斗力":info[1]}})
    else:
        return jsonify({"code":10000,"message":"战士不存在"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8814)
