# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They are 2 different types of data structure, are usualy a collection of more than 1 value/item, can be indexed[], can both take more than one type of object in the same list/tuple. The tuples will work as keys in dictionaries because each tuple is immutable and is treated as one item, a list is mutable and contains many items. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> list is a data structure (a way to store/organize multiple pieces of data) that is mutable. i.e. list(1,2,3,1,2,3) will yeild [1,2,3,1,2,3].   Beacuse it is mutable, it can be sorted  list.sort[3,3,2,1] yeilds [1,2,3,3].  
>> a set is a data type that is very specific and can only perform specific functions. a set is an unordered collection of UNIQUE elements i.e. set(1,2,3,1,2,3) will give you [1,2,3]  This is useful for removing duplicates, membership testing, differences, intersection etc.   
The functions that are specific to sets, are always faster and easier (requires less code/loops) to do when converting the data to a set. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda allows for an anonymous in-line function to be defined and called in one line. it also allows you to pass a function in as a variable (functional programming).  x = filter(lambda x: x % 3 == 0, my_list).  if you pass lambda to the filter function, filter uses lambda to decide what to filter and the second argument (my_list) is the list it will look through. 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> list comprehension is a way to condense the operations done on items in a list/dictionary instead of writing multiple for loops.  for example, this will cube all the odd elements of the numbers between 1 and 21 .  ex = [x ** 3 for x in range(1,22) if (x % 2) == 0] . 
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 26 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513  days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





