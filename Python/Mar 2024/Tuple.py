#sort tuple of list in python
#using list comprehention list
# tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])
# a = tuple([sorted(i) for i in tuple_of_lists])
# print(a)

#map and ssorting
'''
a = tuple(map(sorted, tuple_of_lists))
print(a)
'''
#-----------------------------------------------------------------------------------------------
#list of list ascending and decending


#Using  sort
#List = [[2, 8, 10], [12, 45, 2], [4, 10, 1]]  
# List.sort()
# print(List)
# List.sort(reverse=True)
# print(List)

#using sorted
'''
print(sorted(List))
print(sorted(List, reverse=True))
'''

#using lambda funtion
# List.sort(key=lambda x: x[2])
# print(List)
#_______________________________________________________________________________________
#sort list of list with first element of each sub_list in python
'''list_of_lists= [[3, 'b'], [1, 'a'], [2, 'c']]
#print(sorted(list_of_lists, key = lambda x: x[0]))
# list_of_lists.sort(key= lambda x: x[0])
# print(list_of_lists)

# a = [i for i in sorted(list_of_lists, key= lambda x: x[0])]
# print(a)

from operator import itemgetter
a = sorted(list_of_lists, key = itemgetter(0))
print(a)'''
#---------------------------------------------------------------------------------------------------
import tkinter as tk
def main():
    window = tk.Tk()
    window.title("Text Editer")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    test_editor = tk.Text(window, font="Helvetica 18")
    test_editor.grid(row=0, column=1)
    
    frame = tk.Frame(window, relief=tk.RAISED, bd=5)
    save_button = tk.Button(frame, text="Save")
    open_button = tk.Button(frame, text="Open")
    
    save_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=1, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")
    window.mainloop()
main()