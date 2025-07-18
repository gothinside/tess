import requests

prompt = {
    "modelUri": "gpt://b1gg6teip6l95agmvb0n/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": (
                "Ты ассистент, эксперт в области оценки учебных работ по техническим дисциплинам. "
                "Твоя задача — написать рецензию на контрольную работу студента по теме расчёта погрешностей "
                "измерений на примере вольтметра. "
                "Для этого ты получаешь: "
                "1) Текст задачи студента (формулировку задачи), "
                "2) Пример образцового решения с правильными формулами и подходами, "
                "3) Текстовое решение студента, полученное из распознавания рукописи, "
                "4) Таблицу параметров задачи с правильными и студентскими значениями. "
                "Твоя задача: внести студентские значения в таблицу, сравнить с правильными, "
                "проанализировать расхождения, подсчитать штрафные баллы, "
                "сформировать рецензию с оценкой и рекомендациями. "
                "В рецензии укажи: "
                "- корректность формул и вычислений, "
                "- наличие ошибок и их влияние на итоговую оценку, "
                "- рекомендации по улучшению. "
                "При подсчёте штрафных баллов учитывай: "
                "ошибки в формулах — 1 балл штрафа, "
                "отсутствие знаков или единиц измерения — 0.5 балла, "
                "небольшие отклонения в числах (до 0.5%) — без штрафа. "
                "Общая оценка выставляется по шкале 2-5 с учётом штрафных баллов и качества решения. "
                "Формат ответа — структурированный текст с разделами: "
                "Введение, Анализ работы, Итоговая оценка, Рекомендации. "
                "\n\n"
                "**Требуется подготовить две рецензии:**\n"
                "1) Краткую рецензию, учитывающую только числовые значения (сравнение параметров, штрафы за отклонения), "
                "без глубокого разбора формул и текста решения;\n"
                "2) Полную рецензию, включающую подробный анализ формул, вычислений, ошибок, их влияния на оценку, "
                "а также рекомендации по улучшению и итоговую оценку.\n"
                "Каждая рецензия должна быть оформлена отдельным разделом в ответе."
            )
        },
        {
            "role": "user",
            "text": (
                "Задача студента: Вольтметром, на котором обзначен класс точности 1,0/0,5 и который имеет диапозон показаний от 0 до 10В, измерили напряжение постоянного тока. Результат измерений составляет 4,2 В. Расчитать значение предельной абсолютной и предельной относительной погрешности этого измерения\n\n"
                "Образцовое решение: Решение: Дано: Класс точности: 1,0 / 0,5 (%) Диапазон измерений: 0...10 В Измеренное значение напряжения: U = 4 , 2 В U=4,2В Определение предельной относительной погрешности δ оп δ оп ​ : Класс точности прибора обычно задается в виде двух чисел: c c — основная погрешность (в процентах от верхнего предела измерений), d d — дополнительная погрешность (в процентах от измеренного значения). В нашем случае: c = 1 , 0 % c=1,0%, d = 0 , 5 % d=0,5%. Формула для предельной относительной погрешности: δ оп = c + d ⋅ ( U н U − 1 ) δ оп ​ =c+d⋅( U U н ​ ​ −1) где U н U н ​ — верхний предел измерений (10 В), U U — измеренное значение (4,2 В). Подставим значения: δ оп = 1 , 0 % + 0 , 5 % ⋅ ( 10 4 , 2 − 1 ) = 1 , 0 % + 0 , 5 % ⋅ ( 2 , 38 − 1 ) = 1 , 0 % + 0 , 5 % ⋅ 1 , 38 = 1 , 0 % + 0 , 69 % = 1 , 69 % δ оп ​ =1,0%+0,5%⋅( 4,2 10 ​ −1)=1,0%+0,5%⋅(2,38−1)=1,0%+0,5%⋅1,38=1,0%+0,69%=1,69% Расчёт предельной абсолютной погрешности S оп S оп ​ : S оп = δ оп × U = 1 , 69 % × 4 , 2 В = 0 , 0169 × 4 , 2 В = 0 , 071 В S оп ​ =δ оп ​ ×U=1,69%×4,2В=0,0169×4,2В=0,071В Ответ: Предельная относительная погрешность измерения: δ оп = 1 , 69 % δ оп ​ =1,69% Предельная абсолютная погрешность измерения: S оп = 0 , 071 В S оп ​ =0,071В\n\n"
                """Решение студента: Вариант № 1865

1) Дана: (с/d): 1,0 / 0,9
Диапозон: 0 - 10В
Измеренное значение U: 4,2 В

δоп = [с + d · (Uн / U - 1)] / U :

= [1,0 + 0,5 % · (10 / 4,2 - 1)] = 1,38

δоп = 1,0 % + 0,5 % · 1,38 = 1,0 % + 0,69 % = 1,69 %

Sоп = 1,69 % · 4,2 = 0,071 В.\n\n"""
                "Таблица параметров: [таблица с правильными и студентскими значениями]"
            )
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN1_h5H18_vz4We1xA48ixavuXDGUTQC_8j7np"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)