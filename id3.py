# ID3 Algorithm
# Python implementation of the ID3 algorithm for building (sub-)optimal decision trees
# Decision tree building and classification of data
#
# David Toma
#

import sys
from math import log2
from copy import deepcopy

#global dictionary containg each attribute and it's range of values
attrs = {}


def parser(data):
    f = open(data, "r", encoding="utf8")
    num_attrs = int(f.readline())
    data, tree = [], []

    #characterizes each attribute
    for i in range(num_attrs):
        line = f.readline().split()
        attrs[line[0]] = line[1:]

    #gets the goal attribute
    goal_attr = f.readline()[:-1]
    goal_index = list(attrs.keys()).index(goal_attr)
    goal_values = attrs[goal_attr]

    #stores the training data as a matrix
    data_size = int(f.readline())
    for j in range(data_size):
        data.append(f.readline().split())

    #runs the ID3 algorithm, builds the tree, and prints it
    print("DECISION TREE\n")
    ID3(tree, data, data_size, attrs, goal_attr, goal_values, goal_index, depth=0)
    
    #classifies each data instance
    to_classify = int(f.readline())    
    print("\nCLASSIFICATION\n")
    for k in range(to_classify):
        classify(f.readline().split(), tree, attrs)


#calculates the entropy of a given data set
def entropy(set, set_size, goal_values, goal_index):
    sum = 0
    for value in goal_values:
        count = 0
        for instance in set:
            if instance[goal_index] == value:
                count += 1
        if count > 0:
            sum += -(count/set_size)*log2(count/set_size)
    return sum

#calculates the information gain of a given attribute over a given data set
def gain(set, set_size, attr_values, attr_index, goal_values, goal_index):

    attr_entropy = entropy(set, set_size, goal_values, goal_index)

    sum = 0
    for value in attr_values:
        count = 0
        value_data = []
        for instance in set:
            if instance[attr_index] == value:
                count += 1
                value_data += [instance]
        sum = count/set_size * entropy(value_data, count, goal_values, goal_index)

    return attr_entropy - sum


#ID3 algorith (builded decision tree is stored in the tree list)
def ID3(tree, data, data_size, attributes: dict, goal, goal_values, goal_index, depth=0):
    max_ig, max_ig_index, max_ig_attr, max_ig_values = 0, 0, "", []

    #choses attribute with highest information gain
    for attr, values in attributes.items():
        if attr != goal:
            index = list(attrs.keys()).index(attr)
            attr_values = values
            ig = gain(data, data_size, attr_values, index, goal_values, goal_index)
            if ig > max_ig:
                max_ig_attr = attr
                max_ig = ig
                max_ig_values = attr_values
                max_ig_index = index

    #builds a list representing the attribute with highest information gain
    for _ in range(len(max_ig_values)+1):
        tree += [[]]
    tree[0] = max_ig_attr

    index = 1 #current branch of the tree
        
    #print attribute's name on the tree
    print(depth*"\t" + max_ig_attr)

    #removes the attribute from the attributes dict
    remaining = deepcopy(attributes)
    del remaining[max_ig_attr]

    #for each value of the attribute
    for value in max_ig_values:
        
        value_data = [] #data instances with the value
        count = 0

        for instance in data: 
            if instance[max_ig_index] == value: #instance has the value
                value_data += [instance]
                count += 1

        if value_data != []:

            print(depth*"\t" + "*" + value) #prints the attribute's value

            if entropy(value_data, count, goal_values, goal_index) == 0: #checks if a leaf is reached
                print("\t" + depth*"\t" + "#" + value_data[0][goal_index] + "#") #prints leaf's classification
                tree[index] = value_data[0][goal_index]
            else: #if no, continues recursively
                ID3(tree[index], value_data, count, remaining, goal, goal_values, goal_index, depth+1)

        index += 1


#receives a data instance, navigates throught the tree and classificates it
def classify(data, tree, attrs):

    root_attr = list(attrs.keys()).index(tree[0]) #gets the root attribute of the tree
    values = list(attrs[tree[0]]) #possible values of the root attribute
    i = values.index(data[root_attr]) + 1 #gets the branch that must be followed

    #checks if a leaf was reached
    if type(tree[i]) != list:
        print(tree[i])
        return
    
    #if no, keeps doing the same
    classify(data, tree[i], attrs)


if __name__ == "__main__":
    out = open(sys.argv[2], "w", encoding="utf8")
    sys.stdout = out
    parser(sys.argv[1])
