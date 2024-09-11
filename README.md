# ID3 Algorithm

Implementing the ID3 Algoritm for building optimal decision trees given a trainig dataset.

Algorithm description:

1. Calculate the entropy of every attribute a of the data set S

2. Partition ("split") the set S into subsets using the attribute for which the resulting entropy after splitting is minimized; or, equivalently, information gain is maximum.

3. Make a decision tree node containing that attribute.

4. Recurse on subsets using the remaining attributes.

The goal is to get a deeper understanding of the theory behind machine learning that is being introduced in ML classes.
