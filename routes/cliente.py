from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """Listar os clientes"""
    return render_template('lista_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados do cliente"""
    pass

@cliente_route.route('/new', methods=['GET'])
def form_cliente():
    """Formulario para criar um cliente"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """Exibir detalhes do cliente"""
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """Formulario para editar um cliente"""
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """Atualizar informações do cliente"""
    pass

@cliente_route.route('/<int:cliente_id>/edit', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """Deletar informações do cliente"""
    pass