from flask import Flask,session,render_template,request, url_for,redirect
from pymongo import MongoClient
client = MongoClient(port=27017)
db=client.temp

app = Flask(__name__)
app.secret_key = 'i did not sleep again but its ok'

@app.route('/')
def hello():
	if 'username' in session:
   		return redirect('/news/1')
	else:
		return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def log():
	   if request.method == 'POST':
   			username = request.form['username']
   			password = request.form['password']
   			if db.users4.find_one({'username':username})==None:
   				return 'User not found or wrong password'
   			else:
   				user=db.users4.find_one({'username':username})
   				if username==user['username'] and password == user['password']:
   					session['username']=username
   					return redirect('/news/1')

   				else:
   					return 'User not found or wrong password'
   	   else:
   			return "Get the fuck outta here "


@app.route('/news/<page_no>',methods=['POST','GET'])
def news(page_no):
	if 'username' in session:
			news=db.news1.find().skip((int(page_no)-1)*10).limit(10)
			d_data=""
			for j in range(10):
				d_title=news[j]['title']
				d_url=news[j]['url']
				d_comments='/comments/'+str(news[j]['h_id'])
				d_data=d_data+'    <a href="'+d_url+'"><div class="card type-'+str(j)+'"><p class="card--number">'+d_title+'</p><p class="card--owner">'+d_url+'</p><div class="card--info"><p class="card--info--integral">25 <i class="fas fa-thumbs-up"></i></p><p class="card--info--comments"><a href="'+d_comments+'">23 Comments</a></p></div></div> </a>'
			return render_template('news.html',data=d_data)
	else:
		return render_template('login.html')




@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('hello'))


if __name__== '__main__':
	app.run(debug=True)