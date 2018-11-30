# -*- coding: utf-8 -*-
import time
import subprocess
import redis
import json
import os

if __name__ == "__main__":

    error_apks = ['160bcc6f22db006968f90941bc89bba4.apk', 'b0c3fddd23ae34ba4eed671e4164ab62.apk', '68ab679c88d1d733c571bf47b2a7b88d.apk', '061d3cc53b7d20797c29aa24b1ee6dc1.apk', '5b11fb7cefece5f08b8efa11d1d3ad81.apk', '524ac7a97c7e044264964781b4e70fca.apk', 'e877244eb4e024d9a2a621c527643a0a.apk', '45fa1d28329a097a60701cb7155ed46d.apk', '539a1cdfdd76f8d8440b001285ea212b.apk', '44f0f3e393aded320aea6fec2181fb8b.apk', 'b54f118313e3cea7ec502e2c164a2479.apk', '9a7e49dcb4ae455419f7a872d5d29d2b.apk', '138386949fff29953928122b83eb0548.apk', '62e23316e78e08f744b482a9d7ce1068.apk', '5683451507aa73997d58380aee89c4f7.apk', '97d7d10a709558429f7f47fd2303e5b1.apk', '76a69f5bcbaa239f6143486c72552ccf.apk', 'fdb8bd99318e21c9207356499feb0027.apk', 'cc29bb54543d3ca31ff405ab8e8f93bd.apk', '717b60a3e5bb783f1f0fb44cc3eac789.apk', '633fdc05ac085dd7df106df65a71e2de.apk', 'abfee1af297f3e22651c94a49a769e1b.apk', '5f2c181e11277fce4820d32f10482b53.apk', 'aa9fb22d1f22ceb6edda1677db0e29e3.apk']

    myredis = redis.Redis(host='127.0.0.1', port=6379, db=0)
    dyredis = redis.Redis(host='10.108.115.45', port=6379, db=0)
    result = dyredis.zrange('sandbox_balck_black', 0, 0)
    limit = 10
    failed = 0
    success = 0
    count = 1
    result_dir_path = '/Users/yt/sandboxtest/result_output/black'  # 要存储result的目录
    for i in range(len(error_apks)):
        app_uri = error_apks[i]
        json_data =json.dumps({"app_uri":"/home/dynamic/test/apk/Fusob/" + app_uri, "type":'3', "task_id": app_uri + "#test"})
        #json_data = json.dumps({"status": 4, "type": 3, "result": [], "task_id":"111.apk#asd"})
        dyredis.zadd('sandbox_analysis_balck_Fusob_error', json_data, 0)

    # while result:
    #     if limit <= 0:
    #         break
    #     for key in result:
    #         limit = limit - 1
    #         result_json = json.loads(key)
    #         # 从task_id中解析出fileName和className，例子: 62A1A4617D0600232837ECE10099177C.apk#UpdtKiller
    #         print result_json
    #         #test = json.dumps(result_json)
    #         myredis.zadd('sandbox_balck_black', result_json, 0)
    #     result = dyredis.zrange("sandbox_balck_black", 0 + count, 0 + count)
    #     count +=1

