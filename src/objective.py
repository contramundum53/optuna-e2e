import optuna


def objective_factory(allow_inf: bool, allow_nan: bool):
    def objective(trial: optuna.Trial) -> float:
        x1 = trial.suggest_float("x1", 0, 10)
        x2 = trial.suggest_float("x2", 1, 10, log=True)
        x3 = trial.suggest_float("x3", 0, 10, step=2.0)
        y1 = trial.suggest_int("y1", 0, 10)
        y2 = trial.suggest_int("y2", 1, 10, log=True)
        y3 = trial.suggest_int("y3", 0, 10, step=2)
        c1 = trial.suggest_categorical("c1", [1, float("inf"), float("-inf")])
        trial.report(0, 1)
        if allow_inf:
            trial.report(float("inf"), 2)
            trial.report(float("-inf"), 3)
        if allow_nan:
            trial.report(float("nan"), 4)
        
        if allow_inf:
            return c1
        else:
            return x1**y1 + x2**y2 + x3**y3
