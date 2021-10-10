# Pylint-Hook
## Task 5 from the course of VCS

## 0. Клонирование репозитория
Выполняем команду 
```
git clone github.com/akhtyamovpavel/PatternsCollection
```

## 1. Создание lint.py
Для начала сделаем файл `lint.py` для подсчета скора и поместим его в склонированный репозиторий (сам файл можно найти в этом репозитории). Также добавим его в `.gitignore`.

## 2. Создание hook
Создаем файл `.git/hooks/pre-commit` со следующим содержимым:
```
#!/bin/sh

python3 lint.py
```
Также в качестве параметра `-t` можно передать трешхолд отличный от 9.0, например:
```
#!/bin/sh

python3 lint.py -t 3.0
```

## 3.1. Тестирование 
Создадим пустой файл и попытаемся его закоммитить:
```
touch dummy.txt
git add dummy.txt
git commit -m 'test_pylint'
```
Получаем выхлоп:
```
Your code has been rated at 3.77/10 (previous run: 3.72/10, +0.05)

commit is rejected
```

## 3.2. Тестирование 
Теперь поменяем трешхолд на 3.0 и сделаем то же самое. Выхлоп:
```
Your code has been rated at 3.77/10 (previous run: 3.77/10, +0.00)

verification passed
[master f7ef0ca] test_pylint
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 dummy.txt
```

