
  
from flask import Flask, render_template,request, Response 
# Flask - para criar as rotas da api
# response - para criar o retorno da api 
# request - para quando o cliente enviar p/ mim um body (no post, qdo a pessoa mandar os dados para cadastrar no banco de dados)  
import json

 

# name, username, password, email, avatar, gender

dictio = {"users":[]}

@app.route('/signup', methods=["POST", "GET"]) 
def page_signup():
    if request.method=="POST":
        dados=request.form.to_dict()
        dictio["users"].append(dados)
        return dictio
    return render_template('create-account.html')
       

     #   return render_template('signup-success.html')
 #   else:
   #     return render_template('create-account.html')


if __name__== "__main__":
    app.run(debug=True)

 