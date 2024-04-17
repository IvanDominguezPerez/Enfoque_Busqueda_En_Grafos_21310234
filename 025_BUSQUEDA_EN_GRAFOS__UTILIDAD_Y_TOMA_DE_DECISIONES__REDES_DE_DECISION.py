from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definición de la estructura de la red de decisión
red_decision = BayesianNetwork([('D', 'U'), ('I', 'U'), ('I', 'R'), ('U', 'R')])

# Definición de las Tablas de Probabilidad Condicional (CPDs)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_u = TabularCPD(variable='U', variable_card=2, values=[[0.8, 0.1], [0.2, 0.9]],
                   evidence=['D', 'I'], evidence_card=[2, 2])
cpd_r = TabularCPD(variable='R', variable_card=2, values=[[0.9, 0.6, 0.7, 0.1],
                                                         [0.1, 0.4, 0.3, 0.9]],
                   evidence=['I', 'U'], evidence_card=[2, 2])

# Asociación de las CPDs con la red de decisión
red_decision.add_cpds(cpd_d, cpd_i, cpd_u, cpd_r)

# Verificación de la consistencia de las CPDs
print("Consistencia de las CPDs:", red_decision.check_model())

# Inferencia en la red de decisión
inference = VariableElimination(red_decision)
probabilidad_r = inference.query(variables=['R'], evidence={'D': 1, 'I': 0})['R']
print("Probabilidad de R dado D=1, I=0:", probabilidad_r.values[1])
