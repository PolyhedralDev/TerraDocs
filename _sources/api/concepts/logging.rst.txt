==================
Logging With SLF4J
==================

.. javadoc-import::
    org.slf4j.Logger
    org.slf4j.LoggerFactory

Logging is essential for debugging any program. There are many logging frameworks for Java, Terra uses the SLF4J_
API for logging.

Obtaining a Logger
==================

Logging is done through a :javadoc:`Logger` instance. There are two main ways to obtain a ``Logger`` in a Terra addon:

Manifest Addon Loader Entry Point
---------------------------------

If you are using a logger in an entry point of a Manifest Addon Loader addon, you can use
:doc:`dependency injection<dependency-injection>` to obtain a Logger instance:

.. literalinclude:: code/logging/getting-logger-di.java
    :language: java

Using LoggerFactory
-------------------

If you're using a logger from elsewhere in your addon, you can use SLF4J's :javadoc:`LoggerFactory` to obtain
a class-specific Logger instance:

.. literalinclude:: code/logging/getting-logger-factory.java
    :language: java

.. note::
    Notice that the ``Logger`` field is ``private static final``. This is because

    - The logger instance is class-specific, not instance-specific
    - Other classes should not be accessing your logger

Using a Logger
==============

Using a logger is very simple. Here is an example that prints a message at 4 log levels:

.. literalinclude:: code/logging/using-logger.java
    :language: java


Logging Levels
--------------

SLF4J supports several logging levels. The logging level shows how important a message is, and most logging frameworks
support hiding messages below a certain level.

- The ``DEBUG`` level is the "finest" level. It is usually hidden by default, as it is meant for verbose logging that
  would only need to be seen for debugging.
- The ``INFO`` level is for informative messages that would be useful for users to see. Info-level messages should not be
  verbose; they are generally used for coarse-grain information about the state of the program.
- The ``WARNING`` level is for informative messages that indicate something unexpected happened, such as Deprecated API usage.
- The ``ERROR`` level is for situations where the program has encountered an error that it can recover from, but prevents
  it from functioning normally.

String Formatting in SLF4J
--------------------------

SLF4J supports string formatting for inserting data into log messages. Here is an example of a logging statement
you might find in an application:

.. literalinclude:: code/logging/no-string-formatting.java
    :language: java

This logging statement uses string concatenation to insert 2 variables into the message. This is not only more verbose
code-wise, it also requires the overhead of string concatenation, which will create a performance penalty in hot code.

SLF4J contains a simple way to solve both of these issues, called string *formatting*:

.. literalinclude:: code/logging/string-formatting.java
    :language: java

In the message, simply put ``{}`` where the variables should be inserted, then add the variables as method parameters
in the order they appear in the logging message.

String formatting has 2 main advantages:

- Less string concatenation boilerplate makes it easier to write and modify the message
- If the message is not printed (e.g. if it's a debug message and debugging is disabled), string concatenation is never performed!

.. _SLF4J: https://www.slf4j.org/