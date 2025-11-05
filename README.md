# ID3 Algorithm + Classification

Decision trees can be used in classification problems in Machine Learning when data is defined by a series of discrete attributes. Given a training set composed of multiple realizations of it's attributes, we can build a decision tree tree that represents the whole training data and classifies it rightfully.

When buiding decision trees, less is more. It's proven that higher depths increase the risk of overfitting. A good order of construction can prevent the tree from growing large.

But how do we know which attributes to exand first in order to guarantee an optimal decision tree?

- By using the ID3 Algorithm

This algorithm uses an heuristic function that tells us which attribute is better for expansion given the trees current state.

On this implementation I used Shannon's Entropy and Information Gain as an heuristic function.

Quick explanation of the algorithm:
1. Expand the attribute with the highest Information Gain
2. Continue doing the same on every branch, without repeating the same attribute on one branch
3. If entropy is equal to zero, we reached a leaf, meaning that all the data instances there have the same classification. Branch ends here.
4. Continue doing it untill there is no possible expansion on any branch.

# Implementation

The program receive an input file with the following format:

#################    FILE    #################
number of atributes\n
attribute1_name attribute1_value1 attribute1_value2 ...\n
attribute2_name attribute2_value1 attribute2_value2 ...\n
attribute3_name attribute3_value1 attribute3_value2 ...\n
[...]
goal attribute name
training set size
attribute1_value attribute2_value attribute3_value ...
attribute1_value attribute2_value attribute3_value ...
attribute1_value attribute2_value attribute3_value ...
attribute1_value attribute2_value attribute3_value ...
attribute1_value attribute2_value attribute3_value ...
...
attribute1_value attribute2_value attribute3_value ...
number of data instances to classify
attribute1_value attribute2_value attribute3_value ...
attribute1_value attribute2_value attribute3_value ...
attribute1_value attribute2_value attribute3_value ...
...
##############    END OF FILE    ##############
NOTE: on the instances to classify the attributes follow the same order as before. The goal attribute is ignored so it can be left with a '_' or other character.

The parser function reads the data from this file.

After that, ID3 function performs the algorithm, drawing the tree on the output with the following format:

ROOT ATTRIBUTE
*value
    ATTR
    *value
        #CLASS#
    *value
        #CLASS#
    ...
*value
    ATTR
    *value
        ATTR
            ...
    *value
        ATTR
            ...
*value
    ...

# Classification

The tree is stored as an hierarchy of lists with the format [Attr_name, value1, value2, ...]. Value field can have another list with a different attribute stored inside or, if a leaf is reached, it contains the classification value.

The classify function navigates throught this hierarchy of lists and returns the classification for each one of the data instances to classify.
