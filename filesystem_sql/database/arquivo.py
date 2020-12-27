from datetime import datetime

from filesystem_sql.database import DataBase


class Arquivo(DataBase):
    def __init__(self, id_arquivo: int = None, nome_arquivo: str = None, tipo_arquivo: str = None,
                 data_criacao: float = None, id_dominio_conteudo: int = None,
                 data_atualizacao: float = None,
                 binario: bytes = None):
        self.__id_arquivo = id_arquivo
        self.__nome_arquivo = nome_arquivo
        self.__tipo_arquivo = tipo_arquivo
        self.__data_criacao = data_criacao
        self.__id_dominio_conteudo = id_dominio_conteudo
        self.__data_atualizacao = data_atualizacao
        self.__binario = binario
        
    @property
    def id_arquivo(self):
        return self.__id_arquivo
    
    @property
    def nome_arquivo(self):
        return self.__nome_arquivo
    
    @property
    def tipo_arquivo(self):
        return self.__tipo_arquivo
    
    @property
    def data_criacao(self):
        return datetime.fromtimestamp(self.__data_criacao) if self.__data_criacao else None
    
    @property
    def id_dominio_conteudo(self):
        return self.__id_dominio_conteudo
    
    @property
    def data_atualizacao(self):
        return datetime.fromtimestamp(self.__data_atualizacao) if self.__data_atualizacao else None
    
    @property
    def binario(self):
        return self.__binario
    
    def dict(self):
        return {key.replace("_Arquivo__", ""): value for key, value in self.__dict__.items()}
    
    @campos_obrigatorios(["nome_arquivo", "tipo_arquivo", "data_criacao", "id_dominio_conteudo"])
    def inserir(self):
        """
        Insere um arquivo.
        
        :param str nome_arquivo: Nome do arquivo.
        :param str tipo_arquivo: Tipo do arquivo.
        :param float data_criacao: Data de inserção do arquivo.
        :param int id_dominio_conteudo: Origem do conteúdo do arquivo (blob, S3 ou em disco).
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = ""
        if self.__binario:
            self.query_string = """INSERT INTO ARQUIVO (NOME_ARQUIVO, TIPO_ARQUIVO, DATA_CRIACAO, ID_DOMINIO_CONTEUDO, 
                                BINARIO)
                                VALUES (%(nome_arquivo)s, %(tipo_arquivo)s, %(data_criacao)s,
                                %(id_dominio_conteudo)s, %(binario)s)"""
        else:
            self.query_string = """INSERT INTO ARQUIVO (NOME_ARQUIVO, TIPO_ARQUIVO, DATA_CRIACAO, ID_DOMINIO_CONTEUDO)
                                VALUES (%(nome_arquivo)s, %(tipo_arquivo)s, %(data_criacao)s,
                                %(id_dominio_conteudo)s)"""
        return True if self.insert() else False
    
    @campos_obrigatorios(["id_arquivo", "nome_arquivo", "data_atualizacao"])
    def atualizar(self):
        """
        Atualiza o nome de um arquivo.
        
        :param int id_arquivo: Id do arquivo atualizado.
        :param str nome_arquivo: Novo nome do arquivo.
        :param float data_atualizacao: Data de atualização do arquivo
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = """UPDATE ARQUIVO SET NOME_ARQUIVO = %(nome_arquivo)s
                            WHERE ARQUIVO.ID_ARQUIVO = %(id_arquivo)s"""
        return True if self.insert() else False
    
    @campos_obrigatorios(["id_arquivo"])
    def deletar(self):
        """
        Deleta um arquivo.
        
        :param int id_arquivo: Identificador do arquivo a ser deletado
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "DELETE FROM ARQUIVO WHERE ARQUIVO.ID_ARQUIVO = %(id_arquivo)s"
        return True if self.insert() else False
