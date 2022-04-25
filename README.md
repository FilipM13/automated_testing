
# Automated testing
In this repository I learn how to configure automated tests with tox, github actions and pytest.
This file will contain notes regarding creating configuration files, tests etc.

## Background (Statistics In Biomedicine)
To make this project both useful for learning and useful as a tool I decided to make it a package.
This will be set of functions that cover subjects of Statistics In Biomedicine.
I'll try to add simple explanation to each function in doc-string.

<hr style="border:3px solid gray">

### Distribution and testing status
Package is installable with command: <br>
`pip install git+https://github.com/FilipM13/automated_testing.git`

Current jobs status:

![Tests](https://github.com/FilipM13/automated_testing/actions/workflows/tests.yml/badge.svg)


<hr style="border:3px solid gray">

## Automated Testing


<hr style="border:3px solid gray">

## Statistics In Biomedicine

### Calculating ranks
#### Steps:
* order elements of list by their absolute value
* group elements with the same absolute value
* for each element assign rank which is equal to average index value of all elements in group

#### Example: <br>
given series = [0, 5, 6, 7, 8, -7, -1, 2, 1, 1] <br>
<b> result of step1 </b>: [0, -1, 1, 1, 2, 5, 6, -7, 7, 8] <br>
<b> result of step2 </b>: <br>
<small> note: indices corresponding to following values are 1, 2, 3 ... n </small> <br>
[ <br>
[0], <br>
[-1, 1, 1], <br>
[2], <br>
[5], <br>
[6], <br>
[-7, 7], <br>
[8] <br>
] <br>
<b> result of step3 </b>: <br>
<small> [value, rank] </small> <br>
[ <br>
[0, 1], <br>
[-1, 3], <br>
[1, 3], <br>
[1, 3], <br>
[2, 5], <br>
[5, 6], <br>
[6, 7], <br>
[-7, 8.5], <br>
[7, 8.5], <br>
[8, 10] <br>
]



