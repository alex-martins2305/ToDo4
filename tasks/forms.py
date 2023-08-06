from django import forms
from .models import Task
from .validator import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()

class newTaskForm(forms.Form):
    choices=[]
    for user in users:
        list_element=(user.username, user.username)
        choices.append(list_element)
    titulo=forms.CharField(label='Titulo', widget=forms.TextInput(attrs={"class": "form-control",}))
    descricao=forms.CharField(label='descricao', widget=forms.TextInput(attrs={"class": "form-control",}))
    need_init_at=forms.DateField(label='Começa em:', widget=forms.TextInput(attrs={"class": "form-control",}))
    pessoa=forms.CharField(label='Pessoa:', widget=forms.Select(choices=choices))

    class Meta:
        model= Task
        fields={'titulo', 'descricao','need_init_at' }
        

    def clean(self):
        titulo=self.cleaned_data.get('titulo')
        descricao=self.cleaned_data.get('descricao')
        need_init_at=self.cleaned_data.get('need_init_at')
        lista_de_erros={}
        campo_vazio(titulo, descricao, need_init_at, lista_de_erros)
        valores_pequenos(titulo, descricao, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro=lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data

class newTaskForm2(forms.Form):
    titulo=forms.CharField(label='Titulo', widget=forms.TextInput(attrs={"class": "form-control",}))
    descricao=forms.CharField(label='descricao', widget=forms.TextInput(attrs={"class": "form-control",}))
    need_init_at=forms.DateField(label='Começa em:', widget=forms.TextInput(attrs={"class": "form-control",}))

    class Meta:
        model= Task
        fields={'titulo', 'descricao','need_init_at' }

    def clean(self):
        titulo=self.cleaned_data.get('titulo')
        descricao=self.cleaned_data.get('descricao')
        need_init_at=self.cleaned_data.get('need_init_at')
        lista_de_erros={}
        campo_vazio(titulo, descricao, need_init_at, lista_de_erros)
        valores_pequenos(titulo, descricao, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro=lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data
'''
class newTaskForm(forms.Form):
    titulo = forms.CharField(label='Título',widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    
                }
            ))
    descricao = forms.CharField(label='Descrição', widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                }
            ))
    need_init_at = forms.CharField(label='Começa em:',widget=forms.PasswordInput(   attrs={
                    "class": "form-control", 
                }
            ))


    def clean_username(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo.replace(" ","")=="" or len(titulo)<=3: 
            raise forms.ValidationError("O título da sua tarefa precisa ter mais caracteres")
        return titulo
    
    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if descricao.replace(" ","")=="" or len(descricao)<=20: 
            raise forms.ValidationError("Descrição da sua tarefa precisa ser mais longa.")
        return descricao

    def clean_need_init_at(self):
        need_init_a = self.cleaned_data.get(need_init_a)
        if need_init_a < date.today():
            raise forms.ValidationError("A data de início não poder menor que hoje.")
        return need_init_a
'''
