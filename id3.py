import sys
from math import log2
from copy import deepcopy

attrs = {}

def parser(data):
    f = open(data, "r", encoding="utf8")
    num_attrs = int(f.readline())
    data = []

    #characterizes each attribute
    for i in range(num_attrs):
        line = f.readline().split()
        attrs[line[0]] = line[1:]

    goal_attr = f.readline()[:-1]
    goal_index = list(attrs.keys()).index(goal_attr)
    goal_values = attrs[goal_attr]

    data_size = int(f.readline())

    for j in range(data_size):
        data.append(f.readline().split())

    ID3(data, data_size, attrs, goal_attr, goal_values, goal_index, depth=0)


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


def ID3(data, data_size, attributes: dict, goal, goal_values, goal_index, depth=0):
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

    print(depth*"\t" + max_ig_attr)

    #removes best attribute from attribute list
    remaining = deepcopy(attributes)
    del remaining[max_ig_attr]

    #for each attribute's value
    for value in max_ig_values:
        value_data = []
        count = 0
        for instance in data: 
            if instance[max_ig_index] == value:
                value_data += [instance]
                count += 1
        if value_data != []:
            print(depth*"\t" + "*" + value)
            if entropy(value_data, count, goal_values, goal_index) == 0:
                print("\t" + depth*"\t" + "#" + value_data[0][goal_index] + "#")
            else:
                ID3(value_data, count, remaining, goal, goal_values, goal_index, depth+1)


if __name__ == "__main__":
    out = open(sys.argv[2], "w", encoding="utf8")
    sys.stdout = out
    parser(sys.argv[1])
  
