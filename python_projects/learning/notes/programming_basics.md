# 1. ( Dictionaries ) {

  [Define Dictionary]
  Use curly brackets = {}

  ex.
    {"name": "Hank", "age": 20, "hobby": "coding"}

  usage.
    {"name": "Hank", "age": 20, "hobby": "coding"}['name']
    output = 'Hank'
}

## 2. ( Built In Functions ) {

  [Basic Functions]
  print()

  str(<int, float, boolean>) = convert to string

  int("5") = convert to integer

  float("5.6") = convert to 'actual?' number

  bool("True") = convert to boolean

  len("Hello") = shows number of characters

  len([1, 2, 3, 4, 5]) = shows array length (number of items)

  sorted([16, 4, 7, 123, 553, 456]) = sorts array (min -> max)

  sorted(["B", "A", "1", "C", "D", "d", "b", "1.5", "a", "c"]) = sorts array (" '1' -> ('X') / 'A' -> 'Z' / 'a' -> 'z' " - Capital letters will be sorted before lowercase)
  output = ['1', '1.5', 'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
}

### 3. ( User Defined Functions ) {

  def my_function(): = define function_name():

  my_function() = call function
}

#### 4. ( Adding Arguments to function ) {

  def my_function(str1, str2): = added arguments

  my_function("Argument 1", "Second Argument") = call with arguments
}

##### 5. ( Default Functions ) {

  def print_something(name = "name", age = "unknown") = giving the arguments default values
}