import optuna
# import pymssql

from objective import *


# def create_mssql_database() -> None:
#     conn = pymssql.connect("mssql", "sa", "optuna-test-5ZYB")
#     conn.autocommit(True)
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE optuna")


# create_mssql_database()




print("mysql")
study1 = optuna.create_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna", sampler=optuna.samplers.RandomSampler(0))
try:
    study1.optimize(objective, n_trials=10)
except BaseException:
    pass
print("postgresql")
study2 = optuna.create_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna", sampler=optuna.samplers.RandomSampler(0))
try:
    study2.optimize(objective_with_inf_nan, n_trials=10)
except BaseException:
    pass

print("sqlite")
study3 = optuna.create_study(study_name="test", storage="sqlite:///data/sample.db", sampler=optuna.samplers.RandomSampler(0))
try:
    study3.optimize(objective_with_inf, n_trials=10)
except BaseException:
    pass
print("mssql")
study4 = optuna.create_study(study_name="test", storage="mssql+pymssql://sa:optuna-test-5ZYB@mssql/optuna?charset=utf8", sampler=optuna.samplers.RandomSampler(0))
try:
    study4.optimize(objective, n_trials=10)
except BaseException:
    pass
print("redis")
study5 = optuna.create_study(study_name="test", storage="redis://redis:6379", sampler=optuna.samplers.RandomSampler(0))
try:
    study5.optimize(objective_with_inf_nan, n_trials=10)
except BaseException:
    pass

print(study1)
print(study2)
print(study3)
# print(study4)
print(study5)

print("done")
