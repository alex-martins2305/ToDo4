from datetime import date

def campo_vazio(titulo, descricao, need_init_at, lista_de_erros):
    """verica se os campos são vazios"""
    if titulo.replace(" ","")=="":
        lista_de_erros['titulo']= 'Precisa digitar um título da tarefa'
    if descricao.replace(" ","")=="":
        lista_de_erros['descricao']= 'Necessária uma descrição'
    if need_init_at=="":
        lista_de_erros['need_init_at']= 'Informe a data que a tarefa deve se inicia.'

def valores_pequenos(titulo, descricao, lista_de_erros):
    """Verifica sem o campos tem caracteres suficientes"""
    if len(titulo)<=3 :
        lista_de_erros['titulo']='Titulo deve ser maior.'
    if len(descricao)<=15:
        lista_de_erros['descricao']='descrição deve ter mais caracteres.'

def data_valida(need_init_at, lista_de_erros):
    """Verifica se a data de inicio já é posterior."""
    if need_init_at<date.today():
        lista_de_erros[need_init_at]='Data deve ser a partir de hoje.'
  
