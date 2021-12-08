# Mach Eight App

## Install

In order not to mess up your local environment, install the package in an isolated virtual environment:

```bash
(base) [dvasquez@dmac machEight]$ virtualenv env
(base) [dvasquez@dmac machEight]$ source env/bin/activate
(env) (base) [dvasquez@dmac machEight]$ pip3 install -r requirements.txt
```

## Run

```bash
(env) (base) [dvasquez@dmac machEight]$ python app.py 139
Brevin Knight - Nate Robinson
Mike Wilks - Nate Robinson
```

For debugging purpose, print also the height of each player:

```bash
(env) (base) [dvasquez@dmac machEight]$ python app.py 139 --print_height
Brevin Knight(70) - Nate Robinson(69)
Mike Wilks(70) - Nate Robinson(69)
```

## Run Unit Test

```bash
(env) (base) [dvasquez@dmac machEight]$ python -m unittest test_app -v
test_edge_cases (test_app.TestApp) ... ok
test_get_players (test_app.TestApp) ... ok
test_name (test_app.TestApp) ... ok
test_no_matches_found (test_app.TestApp) ... ok
test_pairs (test_app.TestApp) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.189s

OK
```
