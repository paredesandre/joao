from dev import database,app
from dev.models import Usuario




with app.app_context():
    database.create_all()
    
 #   "https://whatsa.me/5541997337026/?t=Obrigado%20por%20entrar%20em%20Contato%20com%20JFC%20-%20Consultoria"
#<script src="https://whatsa.me/bt-min.js?link=https://whatsa.me/5541997337026/?t=Obrigado%20por%20entrar%20em%20Contato%20com%20JFC%20-%20Consultoria"></script>
