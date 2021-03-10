from flask import Flask, jsonify, render_template, request
import time
app = Flask(__name__)
usr="View current time ! "
@app.route('/')
def index():
  print("Successfull")
  return render_template('render.html',usr=usr )
@app.route('/_play', methods=['GET'])
def play():
  print("playing")
  t=time.strftime("%H:%M:%S",time.localtime())
  return jsonify(result=t)
if __name__ == '__main__':
   app.run(debug=True)