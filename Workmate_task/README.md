# Salary Report Generator

Утилита для генерации отчетов по зарплатам сотрудников из CSV-файлов.

## Основные возможности

- Чтение данных сотрудников из нескольких CSV-файлов
- Поддержка различных названий столбцов (hourly_rate, rate, salary)
- Генерация отчетов в консольном формате
- Гибкая система добавления новых типов отчетов

## Быстрый старт

1. Сформировать отчёт по выплатам первого файла
```bash
python main.py data/data1.csv --report payout
```
2. Сформировать отчёт по выплатам второго файла
```bash
python main.py data/data2.csv --report payout
```
3. Сформировать отчёт по выплатам нескольких файлов
```bash
python main.py data/data1.csv data/data2.csv --report payout 
```

## Запуск тестов
1. Запуск всех тестов
```bash
python -m pytest tests/
```

## Технические детали
Требования к файлам
CSV-файлы должны содержать:

Столбец hours_worked (числовой)

Один из столбцов: hourly_rate, rate или salary (числовой)

## Обратная связь
TG - @FedorSmorodskii

Email - fedorsmorodskii@gmail.com
