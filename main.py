import pandas as pd


df = pd.read_csv('data.csv')
df.dropna()
df


selected_group_of_men_df = df.loc[(df['Количество больничных дней'] > 2) & (df['Пол'] == 'М')]

selecetd_group_of_women_df = df.loc[(df['Количество больничных дней'] > 2) & (df['Пол'] == 'Ж')]


amount_of_selected_men = len(selected_group_of_men_df)
amount_of_selected_women = len(selecetd_group_of_women_df)


print('Число людей по выбранным группам:')
print('Мужчины: ', amount_of_selected_men)
print('Женщины: ', amount_of_selected_women) 

amount_of_all_men = len(df.loc[(df['Пол'] == 'М')])
amount_of_all_women = len(df.loc[(df['Пол'] == 'Ж')])


percent_of_men = amount_of_selected_men / amount_of_all_men * 100
percent_of_women = amount_of_selected_women / amount_of_all_women * 100


print('% от общего числа сотрудников соответвуюшего пола:')
print('Мужчины: ', percent_of_men, '%')
print('Женщины: ',  percent_of_women, '%')


print('\n')


if percent_of_men > percent_of_women:
    print('% пропускающих людей (мужчины) > % пропускающих людей (женщины) на ', abs(percent_of_men-percent_of_women), ' %')

elif percent_of_men < percent_of_women:
    print('% пропускающих людей (мужчины) < % пропускающих людей (женщины) на', abs(percent_of_men-percent_of_women), ' %')

else: 
    print('% пропускающих людей (мужчины) = % пропускающих людей (женщины)')

import matplotlib
import matplotlib.pyplot as plt


result = {'Мужчины': amount_of_selected_men / amount_of_all_men * 100, 
          'Женщины': amount_of_selected_women / amount_of_all_women * 100}


courses = list(result.keys())
values = list(result.values())

fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values,
        width = 0.4)
 
plt.xlabel("Группа")
plt.ylabel("% от общего числа сотрудников")
plt.title("% от общего числа сотрудников соответвуюшего пола")
plt.show()

unique_amount_of_sick_days = selected_group_of_men_df['Количество больничных дней'].unique()

percent_of_men_per_amount_of_sick_days = {}

for amount_of_sick_days in unique_amount_of_sick_days:
    amount_of_men = len(df.loc[(df['Пол'] == 'М') & (df['Количество больничных дней'] == amount_of_sick_days)])

    percent_of_men_per_amount_of_sick_days[amount_of_sick_days] = amount_of_men / amount_of_all_men * 100


unique_amount_of_sick_days = selected_group_of_men_df['Количество больничных дней'].unique()

percent_of_women_per_amount_of_sick_days = {}

for amount_of_sick_days in unique_amount_of_sick_days:
    amount_of_women = len(df.loc[(df['Пол'] == 'Ж') & (df['Количество больничных дней'] == amount_of_sick_days)])

    percent_of_women_per_amount_of_sick_days[amount_of_sick_days] = amount_of_women / amount_of_all_women * 100


courses = list(percent_of_men_per_amount_of_sick_days.keys())
values = list(percent_of_men_per_amount_of_sick_days.values())


fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values,
        width = 0.4)
 
plt.xlabel("Число больничных дней")
plt.ylabel("% от общего числа сотрудников")
plt.title("% от общего числа сотрудников соответвующего пола (мужчины)")
plt.show()

courses = list(percent_of_women_per_amount_of_sick_days.keys())
values = list(percent_of_women_per_amount_of_sick_days.values())


fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values,
        width = 0.4)
 
plt.xlabel("Число больничных дней")
plt.ylabel("% от общего числа сотрудников")
plt.title("% от общего числа сотрудников соответвующего пола (женщины)")
plt.show()

selected_group_of_olds_df = df.loc[(df['Возраст'] > 35) & (df['Количество больничных дней'] > 2)]
selected_group_of_youngs_df = df.loc[(df['Возраст'] <= 35) & (df['Количество больничных дней'] > 2)]


amount_of_selected_olds = len(selected_group_of_olds_df)
amount_of_selected_youngs = len(selected_group_of_youngs_df)


print('Число людей по выбранным группам:')
print('Cтарше 35: ', amount_of_selected_olds)
print('35 и младше: ', amount_of_selected_youngs) 

amount_of_all_olds = len(df.loc[(df['Возраст'] > 35)])
amount_of_all_youngs = len(df.loc[(df['Возраст'] <= 35)])


percent_of_olds = amount_of_selected_olds / amount_of_all_olds * 100
percent_of_youngs = amount_of_selected_youngs / amount_of_all_youngs * 100


print('% от общего числа сотрудников соответвуюшей возрастной группы:')
print('(старше 35): ',  percent_of_olds, '%')
print('35 и младше: ',  percent_of_youngs, '%')

print('\n')

if percent_of_olds > percent_of_youngs:
    print('% пропускающих людей (старше 35) > % пропускающих людей (35 и младше) на ', abs(percent_of_olds-percent_of_youngs), ' %' )


elif percent_of_olds < percent_of_youngs:
    print('% пропускающих людей (старше 35) < % пропускающих людей (35 и младше) на', abs(percent_of_olds-percent_of_youngs), ' %')

else: 
    print('% пропускающих людей (старше 35) = % пропускающих людей (35 и младше)')


result = {'старше 35': amount_of_selected_olds / amount_of_all_olds * 100, 
          '35 и младше': amount_of_selected_youngs / amount_of_all_youngs * 100}


courses = list(result.keys())
values = list(result.values())


fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values,
        width = 0.4)
 
plt.xlabel("Группа")
plt.ylabel("% от общего числа сотрудников")
plt.title("% от общего числа сотрудников соответвуюшей возрастной группы")
plt.show()

unique_amount_of_sick_days = selected_group_of_olds_df['Количество больничных дней'].unique()

percent_of_olds_per_amount_of_sick_days = {}

for amount_of_sick_days in unique_amount_of_sick_days:
    amount_of_olds = len(df.loc[(df['Возраст'] > 35) & (df['Количество больничных дней'] == amount_of_sick_days)])

    percent_of_olds_per_amount_of_sick_days[amount_of_sick_days] = amount_of_olds / amount_of_all_olds * 100


unique_amount_of_sick_days = selected_group_of_youngs_df['Количество больничных дней'].unique()

percent_of_youngs_per_amount_of_sick_days = {}

for amount_of_sick_days in unique_amount_of_sick_days:
    amount_of_youngs = len(df.loc[(df['Возраст'] <= 35) & (df['Количество больничных дней'] == amount_of_sick_days)])

    percent_of_youngs_per_amount_of_sick_days[amount_of_sick_days] = amount_of_youngs / amount_of_all_youngs * 100



courses = list(percent_of_olds_per_amount_of_sick_days.keys())
values = list(percent_of_olds_per_amount_of_sick_days.values())


fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values,
        width = 0.4)
 
plt.xlabel("Число больничных дней")
plt.ylabel("% от общего числа сотрудников")
plt.title("% от общего числа сотрудников соответвуюшей возрастной группы (старше 35)")
plt.show()


courses = list(percent_of_youngs_per_amount_of_sick_days.keys())
values = list(percent_of_youngs_per_amount_of_sick_days.values())


fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values,
        width = 0.4)
 
plt.xlabel("Число больничных дней")
plt.ylabel("% от общего числа сотрудников")
plt.title("% от общего числа сотрудников соответвуюшей возрастной группы (35 и младше)")
plt.show()
