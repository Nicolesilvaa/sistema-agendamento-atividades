from src.utils.prioridade import Prioridade

import time
import uuid


class Atividade:
 
    def __init__(self,  nome:str, horarioInicio:time, horarioFim:time, prioridade:Prioridade, quantidadeParticipantes: int):

        self.__codigo = str(uuid.uuid4())[:5]


        if horarioInicio >= horarioFim:
            raise ValueError(
                "O horário de início deve ser menor que o horário de fim."
            )
        
        
        self.__nome = nome
        self.__horarioInicio = horarioInicio
        self.__horarioFim = horarioFim
        self.__prioridade = prioridade
        self.__quantidadeParticipantes = quantidadeParticipantes



    # Getters e Setters
    
    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getHorarioInicio(self):
        return self.__horarioInicio

    def getHorarioFim(self):
        return self.__horarioFim

    def getPrioridade(self):
        return self.__prioridade

    def getQuantidadeParticipantes(self):
        return self.__quantidadeParticipantes
    
    def setNome(self, nome):
        self.__nome = nome

    def setHorarioInicio(self, horarioInicio):
        self.__horarioInicio = horarioInicio

    def setHorarioFim(self, horarioFim):
        self.__horarioFim = horarioFim

    def setPrioridade(self, prioridade):
        self.__prioridade = prioridade

    def setQuantidadeParticipantes(self, quantidadeParticipantes):
        self.__quantidadeParticipantes = quantidadeParticipantes
    

    def __str__(self):

            return (
                f"Atividade(código={self.__codigo}, "
                f"nome='{self.__nome}', "
                f"início='{self.__horarioInicio}', "
                f"fim='{self.__horarioFim}', "
                f"prioridade={self.__prioridade}, "
                f"participantes={self.__quantidadeParticipantes})"
            )
