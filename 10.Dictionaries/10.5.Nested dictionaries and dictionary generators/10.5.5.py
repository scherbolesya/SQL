# Как извлечь из словаря marks оценку по истории?
# How to extract a history grade from a marks dictionary?
marks = { 
   'class':{ 
      'student':{ 
         'name':'Rosaly',
         'marks':{ 
            'physics':70,
            'history':80
         }
      }
   }
}
# Примечание. История = history (на английском языке) 🙃
marks['class']['student']['marks']['history']
