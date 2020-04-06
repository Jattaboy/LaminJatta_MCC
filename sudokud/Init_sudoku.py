from ForwardChecking import *
import sys

class Init_sudoku:
    empty_boxes = {}
    initial_box_values = ''

    def __init__(self, start):
        self.initial_box_values = start

    def create_box(self, ro, col):

        row = ro
        column = col
        box_list = []
        for r in row:
            for c in column:
                box_name = int(r) * 10 + int(c)  # creates box names by converting the string to numbers 11, 12...99
                box_list.append(box_name)
        return box_list

    def feed_box(self, box_names):
        temp_list = []
        unsolved_sudoku = {}
        i = 0
        for value in self.initial_box_values:
            unsolved_sudoku[box_names.pop(i)] = int(value)  # it maps every key to value and form a dictionary
        return unsolved_sudoku

    def solve_sudoku(self, key1):
        temp_list=self.empty_boxes[key1]

        lis=list(forward.temp_dic.keys())
        prev_index = 0  # to store previous_value index
        key = key1
        previous_value = 0
        list_key=list(self.empty_boxes.keys())
        while list_key[0] <= key <= 97:
            pos_val = self.empty_boxes.get(key) ## possible values for a box
            if previous_value != 0:
                previous_value = final_grid.get(key)
                prev_index = pos_val.index(previous_value)  ## it gets the index of the previous value
                prev_index = prev_index + 1
                if prev_index == len(pos_val):
                    final_grid[key] = 0
                    key = key - 1
                    tem = set(list_key)
                    while key not in tem:
                        if key > list_key[0]:
                            key = key - 1
                    previous_value = final_grid.get(key)
                    pos_val = self.empty_boxes.get(key)
                    prev_index = pos_val.index(previous_value)  ## it gets the index of the previous value
                    prev_index = prev_index + 1
            for j in range(prev_index, len(pos_val)):
                row = forward.row_reduce(key, pos_val[j], final_grid)
                col = forward.column_reduce(key, pos_val[j], final_grid)
                sqr = forward.square_reduce(key, pos_val[j], final_grid)
                if row & col & sqr:
                    final_grid[key] = pos_val[j]
                    key = key + 1
                    prev_index = 0
                    tem=set(list_key)
                    while key not in tem:
                        if key < list_key[len(list_key)-1]:
                            key = key + 1
                    previous_value = 0
                    break
                if row & col & sqr == False and j == len(pos_val)-1:  # backtracks if returned value is false and we are at the end of the list in the boxes values
                    tem = set(list_key)
                    final_grid[key] = 0
                    key = key - 1
                    while key not in tem :
                        if key >= list_key[0]:
                            key = key - 1
                    previous_value = 1
                    break

        i = 0
        for row in range(1, 10):
            for col in range(1, 10):
                print(list(final_grid.values()).pop(i), end="  ")
                i = i + 1
            print('\n', end="")
        #print(forward.dic.get)
        print(forward.square_reduce(67, 9, final_grid))

        print(forward.dic)

    def collect_empty_boxes(self):             # to collect empty boxes
        for s in range(11, 92, 10):
            for t in range(s, s+9):
                if forward.temp_dic.get(t) == 0:
                    self.empty_boxes[t] = list(forward.dic.get(t))
        lis= list(self.empty_boxes.keys())
        self.solve_sudoku(lis[0])

       # print(self.empty_boxes)
        '''i = 0
        for row in range(1, 10):
            for col in range(1, 10):
                print(list(final_grid.values()).pop(i), end="  ")
                i = i + 1
            print('\n', end="")
        '''


values = '530070000600195000098000060800060003400803001700020006060000280000419005000080078'
rows = '123456789'
columns = '123456789'
sud = Init_sudoku(values)
box = sud.create_box(rows, columns)
val = sud.feed_box(box)
forward = ForwardChecking(val)
final_grid = forward.temp_dic  # final grid is the final sudoku grid
sud.collect_empty_boxes()

solve = sol