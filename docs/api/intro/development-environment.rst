====================================
Setting up a Development Environment
====================================

Now that you understand the addon loading process, you can set up a development environment to work on a Terra addon.


Initial Setup
=============

This section goes over choosing an IDE and build system, and installing required tools (such as the JDK). If you
have already done this or know how to do it, you can skip to the next section.

Choosing an IDE
---------------

An IDE (Integrated Development Environment) is strongly recommended for working with Terra. There are many Java IDEs,
the three most popular being:

- `IntelliJ IDEA <https://www.jetbrains.com/idea/download/>`__
- `Eclipse <https://www.eclipse.org/downloads/>`__
- `NetBeans <https://netbeans.org/downloads/index.html>`__

What you use is up to you, but this tutorial will show how to use IntelliJ.

Choosing a Build System
-----------------------

Build systems automate the build process of your project. You can use them to include dependencies (such as Terra API),
build artifacts (such as addon JARs) and much more. The two most popular Java build systems are:

- `Maven <https://maven.apache.org/>`__
- `Gradle <https://gradle.org/>`__

As with your IDE, which build system you choose is up to you. Terra itself, and by extension its core addons,
use Gradle.

Installing the JDK
------------------

To work on any Java project, you'll need to install a JDK. Terra develops against the latest LTS version of Java, which
is currently 17. Download the JDK `here <https://adoptium.net/>`__, or install it through your package manager.

Project Setup
=============

Before configuring your project to include Terra's API, create a project in your IDE of choice and configure it to
use your build system.

Repository Configuration
------------------------

Terra publishes artifacts to the `CodeMC Maven Repository <https://repo.codemc.io/>`__. Configure your build system
to fetch from it:

.. tab-set::

    .. tab-item:: Gradle (Groovy DSL)
        :sync: gradle_groovy

        .. literalinclude:: code/development-environment/repo/gradle_groovy.groovy
            :language: groovy

    .. tab-item:: Gradle (Kotlin DSL)
        :sync: gradle_kotlin

        .. literalinclude:: code/development-environment/repo/gradle_kotlin.kts
            :language: kotlin

    .. tab-item:: Maven
        :sync: maven

        .. literalinclude:: code/development-environment/repo/maven_pom.xml
            :language: xml


Dependency Configuration
------------------------

Now that you've configured the repository to acquire the Terra artifact from, you must specify dependency on the Terra
API:

.. tab-set::

    .. tab-item:: Gradle (Groovy DSL)
        :sync: gradle_groovy

        .. literalinclude:: code/development-environment/dependency/gradle_groovy.groovy
            :language: groovy

    .. tab-item:: Gradle (Kotlin DSL)
        :sync: gradle_kotlin

        .. literalinclude:: code/development-environment/dependency/gradle_kotlin.kts
            :language: kotlin

    .. tab-item:: Maven
        :sync: maven

        .. literalinclude:: code/development-environment/dependency/maven_pom.xml
            :language: xml

.. note::
    Replace ``VERSION`` with the latest Terra version!


Refresh the Project
-------------------

.. tab-set::

    .. tab-item:: IntelliJ

        ``Ctrl+Shift+O``

    .. tab-item:: Eclipse

        1. Select the project root in the Project Explorer
        2. Right click and select ``Refresh`` (Or press ``F5``)

You now have set up a Terra project and are ready to start developing an addon!
