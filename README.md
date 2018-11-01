Kingdom
=======

This is a Python implementation of the Kingdom programming problem. 

In Kingdom, there exists a field containing 3 simple actors—mountains, open fields, and armies. The
mountains serve as the delimiter of the open fields. The open fields serve as objects to be captured
by an army—a single army, armies of the same kingdom, or armies from different kingdoms.

The problem is to process a string grid containing the following various symbols and their
representations:

- `#`: mountain
- `.`: field
- `a-z`: army

For this particular problem, the handling of field neighbors is through the four cardinal
directions—west, north, east, and south. The script accomplishes the following tasks:

- Return all the fields occupied by at least one army.
- Return the number of armies of the different kingdoms.
- Return the number of contested fields (those that contain at least 2 armies from 2 different
  kingdoms).


<a name="toc"></a> Table of contents
------------------------------------

- [Usage](#usage)
  + [REPL](#repl)
  + [File input](#input)
    * [File output](#output)
- [Remarks](#remarks)


<a name="usage"></a> Usage
--------------------------


### <a name="repl"></a> REPL

Run the following commands in your terminal:

```
$ git clone https://github.com/zhaqenl/kingdom ~/python/kingdom
$ cd ~/python/kingdom
$ python
```

Once inside the interactive interpreter, import the following modules:

```
>>> import core
>>> import input_data
```

The `input_data` module contains sample data which the `core` module requires. The `core` module on
the other hand contains the `KingdomSolver` class where its `__init__` method require a
`string_grid` argument:

```
>>> simple_solver = core.KingdomSolver(input_data.simple_grid)
```

After the instance creation, we call its `contested()` instance method:

```
>>> simple_solver.contested()
```

The result of the above invokation is a tuple whose first element is the total number of fields
being contested, while the second element is a dictionary containing a contested field and
contesting army as its key and value pairs, respectively:

```
>>> simple_solver.contested()
(1, {frozenset([(1, 3), (2, 3), (3, 3), (2, 2), (3, 0), (3, 1), (2, 1)]): set(['e', 'f'])})
```

To return the respective numbers of armies on the field, invoke the `map_army_count()` instance
method:

```
>>> simple_solver.map_army_count()
[('e', 1), ('f', 2)]
```


### <a name="input"></a> File input

If you prefer a file as the input of the script, you could create a file whose first line indicates
the total number of cases, followed by the row quantity then the column quantity of the first case,
then the string grid itself. See `dummy_input.txt` for an example structure.

After creating the `.txt` file, run the script in the following manner to get the tally of the
armies from the different kingdoms and the number of fields being contested by these armies:

```
$ python kingdom.py dummy_input.txt
Case 1:
e 1
f 2
contested 1
Case 2:
a 1
e 1
f 2
g 1
contested 2
Case 3:
a 1
b 1
c 2
d 1
e 1
x 3
contested 1
Case 4:
a 2
b 2
c 3
d 2
e 3
x 3
contested 3
```


#### <a name="output"></a> File output

If you want to save the output of the previous command to a file, redirect the output stream to a
file:

```
$ python kingdom.py dummy_input.txt > dummy_output.txt
```
