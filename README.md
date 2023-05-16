# Calculette_Basique

## Calculatrice en Python:

Ce programme est une calculatrice simple en Python qui prend en charge les opérations suivantes : addition (+), soustraction (-), multiplication (*), division (/), modulo (%) et exponentiation (^). Les paramètres d'entrée doivent être des nombres entiers.

## Utilisation:

Pour utiliser cette calculatrice, exécutez le fichier 'main.py' en utilisant Python 3.

La syntaxe pour exécuter le programme est la suivante :

```PYTHON
python main.py [OPERATEUR] [NOMBRE1] [NOMBRE2]
```

[OPERATEUR] : L'opérateur mathématique que vous souhaitez utiliser (+, -, *, /, %, ^).
[NOMBRE1] et [NOMBRE2] : Les deux nombres entiers sur lesquels vous souhaitez effectuer l'opération.

## Exemple d'utilisation:

Voici un exemple d'utilisation de la calculatrice :

```python 
python main.py + 5 3
```

Ce qui affichera :

```python
Résultat : 8
```

## Messages d'erreur
Le programme prend en compte les erreurs suivantes :

Si vous ne spécifiez pas au moins trois paramètres, un message d'aide sera affiché :

```python
Usage: python main.py [OPERATEUR] [NOMBRE1] [NOMBRE2]
```

Si vous entrez un opérateur non pris en charge, le programme affichera :


```python
Erreur : Opérateur non pris en charge
```

Si vous entrez des nombres décimaux ou des caractères non numériques comme arguments pour [NOMBRE1] ou [NOMBRE2], le programme affichera :

```python
Erreur : Les nombres doivent être entiers
```

Cela garantit que le programme fonctionne uniquement avec des nombres entiers et les opérations mathématiques spécifiées.

N'hésitez pas à utiliser cette calculatrice pour effectuer vos calculs mathématiques simples en Python !
