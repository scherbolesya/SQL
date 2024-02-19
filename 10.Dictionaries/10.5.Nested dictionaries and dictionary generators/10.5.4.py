# Сопоставьте код (в левом столбце) с выводом (в правом столбце), если словарь states имеет вид:
# Match the code (in the left column) with the output (in the right column) if the states dictionary is:
states = {'California': {'population': 39512223, 'capital': 'Sacramento', 'landlocked': False}, 
          'Oregon': {'population': 4217737, 'capital': 'Salem', 'landlocked': False}, 
          'Nevada': {'population': 3080156, 'capital': 'Carson City', 'landlocked': True}}

states['California']['population'] --- 39512223
states['Nevada']['landlocked'] --- True
states['capital']['California'] --- произойдет ошибка: KeyError: 'capital'
states['California']['landlocked'] --- False
states['Oregon']['capital'] --- 'Salem'
states['Oregon']['area'] --- произойдет ошибка: KeyError: 'area'
states['Nevada']['population'] --- 3080156
states['Nevada']['capital'] --- 'Carson City'
states['Connecticut']['population'] --- произойдет ошибка: KeyError: 'Connecticut'
