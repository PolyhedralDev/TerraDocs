==================
TerraScript Syntax
==================

TerraScript syntax is quite similar to JavaScript and other C-like syntax
languages. If you have worked with such languages, TerraScript will feel
quite familiar. If not, TerraScript is still very simple to learn!

Functions
=========

A function is an *expression* that performs an action using *arguments*,
and (optionally) *returns* a value.

Function Basics
---------------

Functions in TerraScript will resemble this format:

::

   function(arg1, arg2);

``function`` is the function’s *identifier* (the function name).

``arg1`` and ``arg2`` are *arguments* (data given to the function for it to operate on).

.. Note::
    Documentation on TerraScript Functions can be found :doc:`here </config/documentation/terrascript/functions>`.

Return Types
------------

Each function has a return type of either ``void``, ``num``, ``str`` or ``bool``.

*return* simply means the function “gives back” a value when it finishes
executing. That value can be ignored, or used in expressions, such as
variable assignments, comparisons, or even other function calls.

-  A return type of ``num``, ``str``, or ``bool`` simply means that the
   function *returns* a numeric, string, or boolean value. This value
   can be used in any expression requiring something matching its data
   type.
-  A return type of ``void`` means that the function does not return a
   value. ``void`` functions cannot be assigned to variables or used in
   expressions.

Expressions
===========

An expression is a series of tokens that may be evaluated to produce a
value.

An example is ``5 + 3 * 2``, which evaluates to ``11``.

Types
-----

A type is the “type” of data required/provided by something in TerraScript. Every
expression in TerraScript has a type. TerraScript is a statically-typed language that
type checks at the time of parsing rather than execution. This means that you don’t
need to worry about checking the type of your variables at runtime.

Terra has 3 types, which have been introduced above:

* ``num`` - A numeric value. Num may hold decimal or integer values. It may be compared to other ``num``\ s via comparison operators.

* ``bool`` - A boolean value. Booleans can either be true or false. It may be compared to other ``bool``\ s via boolean operators.

* ``str`` - A string value. Strings hold sequences of characters, i.e. ``"Hello, World!"`` It may be compared to other ``str``\ s via the equals and not equals operators.

(``void`` is not technically a type, it simply marks that a function
does not return a value.)

Constant Expressions
--------------------

Constant expressions are expressions that hold a constant value of a
certain type.

* ``str`` constant expressions are surrounded by double quotes: ``"This is a constant string"``
* ``num`` constant expressions are raw numeric values: ``0``, ``1``, ``20.3``, ``42.0``
* ``bool`` constant expressions are simply the keyword ``true`` or ``false``

Compound Expressions
--------------------

Compound Expressions are multiple expressions combined using
*operators*. TerraScript contains many operators to perform operations
on different data types.

Operators
~~~~~~~~~

Operators are constructs which perform an *operation* on one or more
piece of data.

Number Operators
^^^^^^^^^^^^^^^^

-  ``+`` - Adds two numbers.
-  ``-`` - Subtracts the right number from the left number.
-  ``*`` - Multiplies two numbers.
-  ``/`` - Divides the left number by the right number.
-  ``%`` - Computes the nth modulus of the left number, where n is the
   right number.

Boolean Operators
^^^^^^^^^^^^^^^^^

-  ``&&`` - Boolean AND (if left AND right are true, evaluates true)
-  ``||`` - Boolean OR (if left OR right are true, evaluates true)

Comparison operators
^^^^^^^^^^^^^^^^^^^^

-  ``>`` - Less than - Compares 2 numbers.
-  ``<`` - Greater than - Compares 2 numbers.
-  ``>=`` - Less than or equal to - Compares 2 numbers.
-  ``<=`` - Greater than or equal to = Compares 2 numbers.
-  ``==`` - Equal to - Compares any data types.
-  ``!=`` - Not equal to - Compares any data types.

Unary Operators
^^^^^^^^^^^^^^^

Unary operators are operators which operate on only one piece of data.

- ``!`` - Boolean NOT operator. ``!true`` = false, ``!false`` = true.
- ``-`` - Negation operator. ``-(1)`` = -1, ``-(-1)`` = 1.

Functions
---------

Functions that return values are expressions! The return value of a
function may be used in a compound expression by simply placing the
function within the expression, like so:

.. code:: js

   randomInt(5) * 2 > 3; // Evaluates to true if a random integer between 0 and 5 multiplied by 2 is greater than 3.

Variables
=========

Variables are used to hold data. They are *declared* with a name called
an *identifier*, which can be used in *assignments* and *references*.

Declaration
-----------

To create a variable it must be *declared*. Declaration of variables in
Terra follows a very standard syntax:

::

   type identifier = value;

-  ``type`` is the type of the variable, either ``str``, ``bool``, or
   ``num``.
-  ``identifier`` is the identifier (name) to give the variable.
-  ``value`` is the value to assign to the variable. A variable’s value
   may be any expression that matches its declared type.

Example:

.. code:: js

   num aNumber = 0; // Declare a num variable called aNumber with value 0.

   str example = "hello, world"; // Declare a str variable called example with a value of "hello, world".

   bool condition = false; // Declare a boolean variable called condition with a value of false.

References
----------

Variables can be used in expressions with *references*. To reference a
variable, simply include it’s identifier in an expression. The
identifier evaluates to the value the variable contains. Example:

.. code:: js

   num number = 3;
   print("Number: " + number); // Prints Number: 3

Assignments
-----------

The value of a variable can be updated with *assignments*. A declaration
includes an assingment. To re-assign a variable after declaration, use
the syntax ``identifier = value;``. You cannot re-*declare* variables,
you must re-*assign* them. Example:

.. code:: js

   num aNumber = 0;
   print("Number: " + number); // Prints Number: 0
   aNumber = 3;
   print("Number: " + number); // Prints Number: 3

The value is declared and initialized to ``0``. Then, after the first
print statement, the variable is re-assigned to have a value of 3. You
can even reference a variable in its own re-assignment:

.. code:: js

   num aNumber = 4;
   print("Number: " + number); // Prints Number: 4
   aNumber = aNumber - 1; // Set aNumber to itself, minus one.
   print("Number: " + number); // Prints Number: 3

Conditional Statements
======================

A key part of any programming language are conditional statements.
TerraScript has a very standard ``if``, ``else if``, and ``else`` syntax.

if
--

The if statement evaluates a block of code if a condition evaluates
true.

.. code:: js

   if(condition) {
       print("condition is true");
   }

In the above example, the ``print`` function would only be run if
``condition`` is equal to true. We assume that ``condition`` is a
``bool``. Any other data type would not be allowed by the parser.

Comparisons
~~~~~~~~~~~

Making comparisons with data allows if statements to become very
powerful. TerraScript supports six comparison operators, listed above.

These operators are all *binary operators*, meaning they operate between
2 expressions.

E.G. ``5 > 1`` returns ``true``.

Equal to and not equal to can be used between any data types. The rest
are strictly between two ``num``\ s.

Combined with the if statement we get this:

.. code:: js

   if(5 > 1) {
       print("condition is true");
   }

This isn’t very useful, though. That condition is always true! What if
we use ``randomInt`` instead?

.. code:: js

   if(randomInt(2) == 0) {
       print("This message prints half the time!");
   }

With external conditions introduced, the script can now have different
behavior in different situations. What if we want to do thing a
half the time, and thing b the rest of the time? We could do something
like this:

.. code:: js

   num randomNumber = randomInt(2);
   if(randomNumber == 0) {
       print("This message prints half the time!");
   }
   if(randomNumber == 1) {
       print("This message prints the other half the time!");
   }

That’s ugly, though. There’s a much cleaner and more readable way to do
the same thing, which is to use the ``else`` statement. ``else``
statements go after ``if`` statements, and evaluate only if the ``if``
condition is false. Rewriting the above example with ``else`` looks like
this:

.. code:: js

   if(randomInt(2) == 0) {
       print("This message prints half the time!");
   } else {
       print("This message prints the other half the time!");
   }

That’s much cleaner than before. We can even reduce this further, since
each block contains just one expression we can use a single-expression
statement:

.. code:: js

   if(randomInt(2) == 0) print("This message prints half the time!");
   else print("This message prints the other half the time!");

Notice the absence of curly braces. You can only do this if there is a
single expression in your statement/loop.

else if
-------

Well, what if we want more conditions? We can use ``else if`` statements
to add more conditions. They will be evaluated sequentially, and
evaluation will stop after one is true.

.. code:: js

   num randomNumber = randomInt(3);
   if(randomNumber == 0) print("This message prints one-third of the time!");
   else if(randomNumber == 1) print("This message prints another third of the time!");
   else if(randomNumber == 2) print("This message prints *another* third of the time!");

Using ``else if`` statements, we can make our scripts more readable and
concise. ``else if`` can also be paired with ``else``, like so:

.. code:: js

   num randomNumber = randomInt(3);
   if(randomNumber == 0) print("This message prints one-third of the time!");
   else if(randomNumber == 1) print("This message prints another third of the time!");
   else print("This message prints *another* third of the time!");

Loops
=====

Loops allow you to run a block of code repeatedly, based on a condition.

While Loop
----------

The simplest loop is the While Loop. A while loop takes a single boolean
expression, called a conditional expression, in its declaration. The
block declared with the while loop will be run if the condition is true,
then will continue to run until the condition is false. Examples:

.. code:: js

   while(true) { // Since the condition is always true, the block will run infinitely. You generally want to avoid situations like this.
       print("this runs forever!");
   }

The loop in this example runs forever, which is generally undesirable.

.. code:: js

   num aNumber = 0;
   while(number < 5) { // This will run the block until aNumber is NOT less than 5 (until A is greater than or equal to 5).
       print("Number: " + aNumber);
       aNumber = aNumber + 1; // Add one to aNumber each time the loop runs.
   }

This loop will run 5 times. The console output would be:

::

   Number: 0
   Number: 1
   Number: 2
   Number: 3
   Number: 4

For Loop
--------

The For Loop is similar to a while loop, but with 3 expressions in its
declaration. Example:

.. code:: js

   for(num x = 0; x < 5; x = x + 1) {
       print("Number: " + aNumber);
   }

This loop does the same thing as the while loop above; it prints numbers
from 0-4. It can be read as “declare a variable called X, loop as long
as x is less than 5, add 1 to x evey time.”

For Loop Expressions:
~~~~~~~~~~~~~~~~~~~~~

Initializer
^^^^^^^^^^^

The first expression in the for loop is called the initializer. Usually
this is a variable declaration. In the case of a variable declaration
initializer, that variable is available only within the scope of the
loop. An example is ``num x = 0`` in the above example, which declares a
number variable with identifier ``x`` that may be referenced in the
loop’s scope.

Conditional
^^^^^^^^^^^

The second expression in the for loop is called the conditional. It is
identical to the conditional in the while loop; the loop will run so
long as it is true, once it is false the loop will stop. Usually, if a
variable was declared in the initializer, the conditional checks a
comparison of the variable. In the example above, the conditional checks
that ``x`` is less than 5.

Incrementer
^^^^^^^^^^^

The third statement in the loop is called the incrementer. The
incrementer is run at the *end* of every loop iteration, after the
entire block is executed, before the next conditional check is made.
Usually the incrementer is used to increment a variable. In the example
above, the incrementer adds 1 to ``x`` every iteration.

Flow Control
~~~~~~~~~~~~

TerraScript includes 4 Flow Control keywords:

return
^^^^^^

The ``return`` keyword immediately halts execution of the script with
“passing” exit status. It may be used in the base block, or in loops.
Example:

.. code:: js

   print("This will be printed!");
   return; // Halt execution here.
   print("This will never be printed!");

The above example exits with passing status after printing the first
message. The second message will never be printed.

fail
^^^^

The ``fail`` keyword immediately halts execution of the script with a
“failure” exit status. It may be used in the base block, or in loops.
Example:

.. code:: js

   print("This will be printed!");
   fail; // Halt execution here.
   print("This will never be printed!");

The above example exits with *failing* status after printing the first
message. The second message will never be printed.

It is important to remember that both ``return`` and ``fail`` cascade,
meaning that if they are used in loops they will immediately exit *all*
parent loops and halt the script.

break
^^^^^

The ``break`` keyword immediately halts the execution of a loop. It will
immediately exit the loop, resuming execution after the loop. Since it
is a loop control keyword, it may *only* be used in loops. Example:

.. code:: js

   num aNumber = 0;
   while(true) { // This loop would normally be infinite.
       if(aNumber > 5) break; // Halt the loop if aNumber is greater than 5
       print("Number:" + aNumber);
       aNumber = aNumber + 1;
   }

The following loop would execute until ``aNumber`` is greater than 5,
then it would halt and resume execution of the rest of the script.

continue
^^^^^^^^

The ``continue`` keyword immediately halts the *current iteration* of a
loop. It will stop the current exexution, and go to the head of the
loop, then continue the loop (if the conditional is met). Example:

.. code:: js

   num aNumber = 0;
   while(aNumber <= 5) { // This loop would normally be infinite.
       aNumber = aNumber + 1;
       print("Number:" + aNumber);
       if(aNumber > 2) continue; // Go back to top if number is greater than 2
       print("Less than 2");
   }

The following loop would execute until ``aNumber`` is greater than 5,
and prints “Less than 2” every time it is less than 2.
