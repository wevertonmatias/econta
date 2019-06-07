from django.db import models

# Create your models here.
from django.db import models


class Banner(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False, blank=True)
    nome = models.CharField(max_length=255)
    foto = models.FileField(blank=True, null=True, upload_to='banner')
    data_cadastro = models.DateField()
    data_expiracao = models.DateField()
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_resp_fk = models.ForeignKey('Responsavel', models.DO_NOTHING, db_column='id_resp_fk')

    class Meta:
        managed = False
        db_table = 'banner'


class Boleto(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False, blank=True)
    descricao = models.CharField(max_length=255)
    dt_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    numero_doc = models.CharField(max_length=255)
    cod_barra = models.CharField(max_length=255, blank=True, null=True)
    id_emp_fk = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_emp_fk')
    id_forn_fk = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='id_forn_fk')
    id_cate_fk = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='id_cate_fk')
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleto'


class Categoria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cidade(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_est_fk = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_est_fk')

    class Meta:
        managed = False
        db_table = 'cidade'


class ContaBancaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    banco = models.CharField(max_length=255, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    conta = models.CharField(max_length=30, blank=True, null=True)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_emp_fk = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_emp_fk')

    class Meta:
        managed = False
        db_table = 'conta_bancaria'


class ContatoMsg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mensagem = models.CharField(max_length=255)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contato_msg'


class Empresa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=255)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_end_fk = models.ForeignKey('Enderenco', models.DO_NOTHING, db_column='id_end_fk')

    class Meta:
        managed = False
        db_table = 'empresa'


class Enderenco(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rua = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_cid_fk = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='id_cid_fk')

    class Meta:
        managed = False
        db_table = 'enderenco'


class Estado(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False, blank=True )
    nome = models.CharField(max_length=2)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Fornecedor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=11)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_end_fk = models.ForeignKey(Enderenco, models.DO_NOTHING, db_column='id_end_fk')

    class Meta:
        managed = False
        db_table = 'fornecedor'


class HistBanner(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    data_expiracao = models.DateField(blank=True, null=True)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_resp_fk = models.ForeignKey('Responsavel', models.DO_NOTHING, db_column='id_resp_fk', blank=True, null=True)
    id_ban_fk = models.ForeignKey(Banner, models.DO_NOTHING, db_column='id_ban_fk')
    data_hora = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_banner'


class HistBoleto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dt_vencimento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    numero_doc = models.CharField(max_length=255, blank=True, null=True)
    cod_barra = models.CharField(max_length=255, blank=True, null=True)
    id_emp_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_emp_fk', blank=True, null=True)
    id_forn_fk = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='id_forn_fk', blank=True, null=True)
    id_cate_fk = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_cate_fk', blank=True, null=True)
    id_bole_fk = models.ForeignKey(Boleto, models.DO_NOTHING, db_column='id_bole_fk')
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    data_hora = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_boleto'


class HistEmpresa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_emp_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_emp_fk')
    id_end_fk = models.ForeignKey(Enderenco, models.DO_NOTHING, db_column='id_end_fk', blank=True, null=True)
    id_conta_bancaria_fk = models.ForeignKey(ContaBancaria, models.DO_NOTHING, db_column='id_conta_bancaria_fk', blank=True, null=True)
    id_tel_fk = models.ForeignKey('Telefone', models.DO_NOTHING, db_column='id_tel_fk', blank=True, null=True)
    data_hora = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_empresa'


class HistFornecedor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=True, null=True)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_forn_fk = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='id_forn_fk', blank=True, null=True)
    id_end_fk = models.ForeignKey(Enderenco, models.DO_NOTHING, db_column='id_end_fk', blank=True, null=True)
    id_tel_fk = models.ForeignKey('Telefone', models.DO_NOTHING, db_column='id_tel_fk', blank=True, null=True)
    data_hora = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_fornecedor'


class HistPagamento(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dt_pagamento = models.DateField(blank=True, null=True)
    dt_entrega = models.DateField(blank=True, null=True)
    juros = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_pag_fk = models.ForeignKey('Pagamento', models.DO_NOTHING, db_column='id_pag_fk', blank=True, null=True)
    id_bole_fk = models.ForeignKey(Boleto, models.DO_NOTHING, db_column='id_bole_fk', blank=True, null=True)
    id_status_fk = models.ForeignKey('Status', models.DO_NOTHING, db_column='id_status_fk', blank=True, null=True)
    id_resp_fk = models.ForeignKey('Responsavel', models.DO_NOTHING, db_column='id_resp_fk', blank=True, null=True)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    data_hora = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_pagamento'


class Pagamento(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dt_pagamento = models.DateField()
    dt_entrega = models.DateField()
    juros = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_bole_fk = models.ForeignKey(Boleto, models.DO_NOTHING, db_column='id_bole_fk')
    id_status_fk = models.ForeignKey('Status', models.DO_NOTHING, db_column='id_status_fk')
    id_resp_fk = models.ForeignKey('Responsavel', models.DO_NOTHING, db_column='id_resp_fk')
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagamento'


class Responsavel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)
    id_end_fk = models.ForeignKey(Enderenco, models.DO_NOTHING, db_column='id_end_fk')

    class Meta:
        managed = False
        db_table = 'responsavel'


class Status(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Telefone(models.Model):
    id = models.BigIntegerField(primary_key=True)
    numero = models.CharField(max_length=20)
    id_resp_fk = models.ForeignKey(Responsavel, models.DO_NOTHING, db_column='id_resp_fk', blank=True, null=True)
    id_emp_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_emp_fk', blank=True, null=True)
    id_forn_fk = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='id_forn_fk', blank=True, null=True)
    status_dlt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefone'

