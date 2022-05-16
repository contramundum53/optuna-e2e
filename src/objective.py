import optuna
import optuna.exceptions


def objective(trial: optuna.Trial) -> float:
    x1 = trial.suggest_float("x1", 0, 10)
    x2 = trial.suggest_float("x2", 1, 10, log=True)
    x3 = trial.suggest_float("x3", 0, 10, step=2.0)
    y1 = trial.suggest_int("y1", 0, 10)
    y2 = trial.suggest_int("y2", 1, 10, log=True)
    y3 = trial.suggest_int("y3", 0, 10, step=2)
    c1 = trial.suggest_categorical("c1", [1, 10, 100])
    c2 = trial.suggest_categorical("c2", ['value', 'pruned'])
    

    print("trial_id:", trial._trial_id)

    if trial._trial_id == 9:
        raise Exception("fail")

    if c2 == 'value':
        val = x1**y1 + x2**y2 + x3**y3 + c1
    elif c2 == 'pruned':
        raise optuna.exceptions.TrialPruned()
    
    trial.report(val, step=1)
    return val


def objective_with_inf(trial: optuna.Trial) -> float:
    x1 = trial.suggest_float("x1", 0, 10)
    x2 = trial.suggest_float("x2", 1, 10, log=True)
    x3 = trial.suggest_float("x3", 0, 10, step=2.0)
    y1 = trial.suggest_int("y1", 0, 10)
    y2 = trial.suggest_int("y2", 1, 10, log=True)
    y3 = trial.suggest_int("y3", 0, 10, step=2)
    c1 = trial.suggest_categorical("c1", [1, 10, 100])
    c2 = trial.suggest_categorical("c2", ['value', 'pos_inf', 'neg_inf', 'pruned'])
    
    print("trial_id:", trial._trial_id)

    if trial._trial_id == 9:
        raise Exception("fail")
    

    if c2 == 'value':
        val = x1**y1 + x2**y2 + x3**y3 + c1
    elif c2 == 'pos_inf':
        val = float('inf')
    elif c2 == 'neg_inf':
        val = float('-inf')
    elif c2 == 'pruned':
        # trial.report(float('nan'), step=1)
        raise optuna.exceptions.TrialPruned()
    trial.report(val, step=1)
    return val


def objective_with_inf_nan(trial: optuna.Trial) -> float:
    x1 = trial.suggest_float("x1", 0, 10)
    x2 = trial.suggest_float("x2", 1, 10, log=True)
    x3 = trial.suggest_float("x3", 0, 10, step=2.0)
    y1 = trial.suggest_int("y1", 0, 10)
    y2 = trial.suggest_int("y2", 1, 10, log=True)
    y3 = trial.suggest_int("y3", 0, 10, step=2)
    c1 = trial.suggest_categorical("c1", [1, 10, 100])
    c2 = trial.suggest_categorical("c2", ['value', 'pos_inf', 'neg_inf', 'nan', 'pruned'])
    


    print("trial_id:", trial._trial_id)
    if trial._trial_id == 9:
        raise Exception("fail")


    if c2 == 'value':
        val = x1**y1 + x2**y2 + x3**y3 + c1
    elif c2 == 'pos_inf':
        val = float('inf')
    elif c2 == 'neg_inf':
        val = float('-inf')
    elif c2 == 'nan':
        val = float('nan')
    elif c2 == 'pruned':
        # trial.report(float('nan'), step=1)
        raise optuna.exceptions.TrialPruned()

    
    trial.report(val, step=1)
    return val