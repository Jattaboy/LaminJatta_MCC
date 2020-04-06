import sys


class ForwardChecking:
    empty_dic={}
    row_values = []
    column_values = []
    square_values = []
    temp_dic = {}
    dic = {}

    def __init__(self, val):
        self.dic = val
        self.temp_dic = self.dic.copy()
        self.set_eligible_values()

    def set_eligible_values(self):
        d = 10
        for i in range(1, 10):  # iterates row-wise 1-9
            row_val = self.row_reduce(1 + i * 10, "", self.empty_dic)  # it calls row_reduce method with keys 11, 21, 31, 41,....91
            for j in range(1, 10):  # iterate column-wise
                if self.temp_dic.get(d + j) == 0:  # only selects boxes with value '0'
                    col_val = self.column_reduce(d + j, "", self.empty_dic)  # calls column_reduce with keys 11, 12, 13,..., 91
                    squ_val = self.square_reduce(d + j, "", self.empty_dic)
                    '''get allowable values for a given box by excluding already assigned values in the same row, 
                    column, and square of that box and stores the value in box_value '''
                    box_value = [k for k in range(1, 10) if k not in col_val and k not in row_val and k not in squ_val]
                    self.dic[d + j] = box_value  # updates the value of the box 11, 12, .....19
            d = 10 * (i + 1)  # for getting the key of next row. 11,21,31...91

        # the below code is just for displaying the reduced sudoku table, to check if elimination method has worked
        '''i = 0
        for row in range(1, 10):
            for col in range(1, 10):
                print(list(self.dic.values()).pop(i), end="  ")
                i = i + 1
            print('\n', end="")
        '''

    def row_reduce(self, k, v, d):  # this method returns allowable values of a box by checking already filled values in that same row
        checker_dic = d
        row = []  # this list stores possible values for a given box, by cross checking already filled values in that same row
        for i in range(0, 9):
            if self.temp_dic.get(k + i) != 0:  # select boxes that are not initially assigned a value
                row.append(self.temp_dic.get(k + i))
            ''' it takes values in digit but not in row, possible assignable values in one specific row'''
        if sys._getframe(1).f_code.co_name == "solve_sudoku":
            row_num = k//10
            row1 = []
            for i in range(1, 10):
                if checker_dic.get(row_num*10 + i) != 0:  # select boxes that are not initially assigned a value
                    row1.append(checker_dic.get(row_num*10 + i))
            test_list_set = set(row1)
            if v in test_list_set:
                return False
            else:
                return True
        else:
            return row

    def column_reduce(self, k, v, d):  # this method returns allowable values of a box by checking already filled values in that same column
        checker_dic = d
        col = k % 10  # used to get the column number from a given key
        column = []  # store possible box possible value
        for i in range(1, 10):  # iterates only column-wise:[11,21,31,41,51,61,71,81,91 : 12, 22, 32, 42....]
            if self.temp_dic.get(i * 10 + col) != 0:  # select boxes that are not initially assigned a value
                column.append(self.temp_dic.get(
                    i * 10 + col))  # append allowable values of a box by checking all assigned values in the same column
        if sys._getframe(1).f_code.co_name == "solve_sudoku":
            column1 = []
            for i in range(1, 10):  # iterates only column-wise:[11,21,31,41,51,61,71,81,91 : 12, 22, 32, 42....]
                if checker_dic.get(i * 10 + col) != 0:  # select boxes that are not initially assigned a value
                    column1.append(checker_dic.get(i * 10 + col))
            test_list_set = set(column1)
            if v in test_list_set:
                return False
            else:
                return True
        else:
            return column

    def square_reduce(self, sq_k, v, d):  # this method returns allowable values of a box by checking already filled values in that same square
        checker_dic = d
        if sys._getframe(1).f_code.co_name == "set_eligible_values":
            key = ""  # string used to store keys in the same square:
            square = []  # store allowable values of a box
            box_dic = {}  # temporary dictionary for handling square_wise reduce
            box_val = []  # this list store value of boxes in the same square
            for i in range(11, 92, 30):  # iterates column_wise by jumping 30 values to get the row of each square, 11, 41, 71
                for j in range(i, i + 9, 3):  # iterate row_wise by jumping 3 values to get the column of each square, 11, 14,17, 41, 44..
                    for k in range(j, j + 21, 10):  # iterate row_wise by jumping 10 values to get the column, 11, 21 ,31, 41...
                        for n in range(k, k + 3):  # iterate row_wise to get the box of each square, 11, 12, 13, 21, 22, 23, 31...
                            if self.temp_dic.get(n) != 0:  # select only boxes not initially assigned
                                box_val.append(self.temp_dic.get(n))
                                key = key + str(n)  # keys in the same square concatenated as one key, 111213212223313233 as one key
                            else:
                                key = key + str(n)

                    box_dic[key] = box_val  # adds the allowable values of all boxes in the same square with key using the keys of all boxes of the square
                    box_val.clear()  # clearing previous result
                    key = ""  # clearing previous result
            key3 = list(box_dic.keys())  # store the keys of all 9 square as a slit
            for i in range(0, len(key3)):
                if str(sq_k) in key3[i]:  # checks if the key 'sq_k' is in the square key
                    square = box_dic.get(key3[i])
                    break
            return square

        if sys._getframe(1).f_code.co_name == "solve_sudoku":
            square1 = []
            key1 = ""  # string used to store keys in the same square:
            box_dic1 = {}  # temporary dictionary for handling square_wise reduce
            box_val1 = []  #
            for i in range(11, 92, 30):
                for j in range(i, i + 9,3):
                    for k in range(j, j + 21,10):
                        for n in range(k,k + 3):
                            if checker_dic.get(n) != 0:
                                box_val1.append(checker_dic.get(n))
                                key1 = key1 + str(n)
                            else:
                                key1 = key1 + str(n)
                    box_dic1[key1] = box_val1
                    box_val1.clear()
                    key1 = ""
            key2 = list(box_dic1.keys())
            for i in range(0, len(key2)):
                if str(sq_k) in key2[i]:
                    square1 = box_dic1.get(key2[i])
                    break
            test_list_set = set(square1)
            #print(box_dic1)
            if v in test_list_set:
                return False
            else:
                return True

