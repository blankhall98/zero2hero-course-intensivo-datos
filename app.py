#Importar Pandas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

def get_data():
    name = input('Enter name: ')
    age = input('Enter age: ')
    sex = input('Enter sex: ')
    wage = input('Enter wage: ')
    education = input('Enter education: ')
    data = [name,age,sex,wage,education]
    return data

def add_observation(df,data):
    df.loc[len(df)] = data
    print(df)

def save_data(df):
    df.to_csv('data.csv',index=False)

def add_new_element(df):
    data = get_data()
    add_observation(df,data)
    save_data(df)

def observe_data(df):
    print(df)

def plot_wage(df):
    plt.plot(df['wage'])
    plt.show()

action = input('What do you want to do? (observe, add, delete, update, plot): ')
if action == 'add':
    add_new_element(df)
elif action == 'observe':
    observe_data(df)
elif action == 'plot':
    plot_wage(df)




