import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Загрузите файл CSV")

def on_upload():
    if uploaded_file is None:
        st.session_state["upload_state"] = "Сначала загрузите файл"
    else:
        # try:
            checker = pd.read_csv(uploaded_file)
            
            if 'Количество больничных дней' not in checker.columns or \
                'Возраст' not in checker.columns or 'Пол' not in checker.columns:

                st.session_state["upload_state"] = "Загрузите валидный CSV"
                
            else:
                st.session_state["upload_state"] = "Сохранено!"

                business_logic(checker)

        # except:
        #     st.session_state["upload_state"] = "Загрузите CSV"


st.button("Загрузить файл", on_click=on_upload)

upload_state = st.text_area("Upload State", "", key="upload_state")



def business_logic(init_df):
    df = init_df
    df.dropna()
    df


    selected_group_of_men_df = df.loc[(df['Количество больничных дней'] > 2) & (df['Пол'] == 'М')]

    selecetd_group_of_women_df = df.loc[(df['Количество больничных дней'] > 2) & (df['Пол'] == 'Ж')]


    amount_of_selected_men = len(selected_group_of_men_df)
    amount_of_selected_women = len(selecetd_group_of_women_df)


    st.text('Число людей по выбранным группам:')
    st.text('Мужчины: ' + str(amount_of_selected_men))
    st.text('Женщины: ' + str(amount_of_selected_women)) 

    amount_of_all_men = len(df.loc[(df['Пол'] == 'М')])
    amount_of_all_women = len(df.loc[(df['Пол'] == 'Ж')])


    percent_of_men = amount_of_selected_men / amount_of_all_men * 100
    percent_of_women = amount_of_selected_women / amount_of_all_women * 100


    st.text('% от общего числа сотрудников соответвуюшего пола:')
    st.text('Мужчины: ' + str(percent_of_men) + ' %')
    st.text('Женщины: ' +  str(percent_of_women) + ' %')


    st.text('\n')


    if percent_of_men > percent_of_women:
        st.text('% пропускающих людей (мужчины) > % пропускающих людей (женщины) на ' + str(abs(percent_of_men-percent_of_women)) + ' %')

    elif percent_of_men < percent_of_women:
        st.text('% пропускающих людей (мужчины) < % пропускающих людей (женщины) на' + str(abs(percent_of_men-percent_of_women)) + ' %')

    else: 
        st.text('% пропускающих людей (мужчины) = % пропускающих людей (женщины)')

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
    # plt.show()

    st.pyplot(fig)

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
    # plt.show()

    st.pyplot(fig)

    courses = list(percent_of_women_per_amount_of_sick_days.keys())
    values = list(percent_of_women_per_amount_of_sick_days.values())


    fig = plt.figure(figsize = (10, 5))
    
    plt.bar(courses, values,
            width = 0.4)
    
    plt.xlabel("Число больничных дней")
    plt.ylabel("% от общего числа сотрудников")
    plt.title("% от общего числа сотрудников соответвующего пола (женщины)")
    # plt.show()
    st.pyplot(fig)


    selected_group_of_olds_df = df.loc[(df['Возраст'] > 35) & (df['Количество больничных дней'] > 2)]
    selected_group_of_youngs_df = df.loc[(df['Возраст'] <= 35) & (df['Количество больничных дней'] > 2)]


    amount_of_selected_olds = len(selected_group_of_olds_df)
    amount_of_selected_youngs = len(selected_group_of_youngs_df)


    st.text('Число людей по выбранным группам:')
    st.text('Cтарше 35: ' + str(amount_of_selected_olds))
    st.text('35 и младше: ' + str(amount_of_selected_youngs)) 

    amount_of_all_olds = len(df.loc[(df['Возраст'] > 35)])
    amount_of_all_youngs = len(df.loc[(df['Возраст'] <= 35)])


    percent_of_olds = amount_of_selected_olds / amount_of_all_olds * 100
    percent_of_youngs = amount_of_selected_youngs / amount_of_all_youngs * 100


    st.text('% от общего числа сотрудников соответвуюшей возрастной группы:')
    st.text('старше 35: ' + str(percent_of_olds) + '%')
    st.text('35 и младше: ' +  str(percent_of_youngs) + '%')

    st.text('\n')

    if percent_of_olds > percent_of_youngs:
        st.text('% пропускающих людей (старше 35) > % пропускающих людей (35 и младше) на ' + str(abs(percent_of_olds-percent_of_youngs)) + ' %' )


    elif percent_of_olds < percent_of_youngs:
        st.text('% пропускающих людей (старше 35) < % пропускающих людей (35 и младше) на ' + str(abs(percent_of_olds-percent_of_youngs)) + ' %')

    else: 
        st.text('% пропускающих людей (старше 35) = % пропускающих людей (35 и младше)')


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
    # plt.show()
    st.pyplot(fig)


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
    # plt.show()
    st.pyplot(fig)


    courses = list(percent_of_youngs_per_amount_of_sick_days.keys())
    values = list(percent_of_youngs_per_amount_of_sick_days.values())


    fig = plt.figure(figsize = (10, 5))
    
    plt.bar(courses, values,
            width = 0.4)
    
    plt.xlabel("Число больничных дней")
    plt.ylabel("% от общего числа сотрудников")
    plt.title("% от общего числа сотрудников соответвуюшей возрастной группы (35 и младше)")
    # plt.show()
    st.pyplot(fig)
