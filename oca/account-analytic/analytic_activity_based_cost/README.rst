============================
Analytic Activity Based Cost
============================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Alpha-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alpha
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--analytic-lightgray.png?logo=github
    :target: https://github.com/OCA/account-analytic/tree/14.0/analytic_activity_based_cost
    :alt: OCA/account-analytic
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-analytic-14-0/account-analytic-14-0-analytic_activity_based_cost
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/87/14.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

Generate Activity Based Costs (ABC), using Analytic Items.

Activity Based Costing is a well documented technique to assign indirect costs to the the activities identified as cost drivers.
This feature models cost driver usage as Analytic Items.
When an Analytic Item is created, it may then generate additional Analytic Items for the corresponding indirect costs.
For example, each timesheet hour logged could generate a quantity and amount of overhead assigned to that activity.

This feature does not generate Account Moves.
That should be implemented by a separate feature.

.. IMPORTANT::
   This is an alpha version, the data model and design can change at any time without warning.
   Only for development or testing purpose, do not use in production.
   `More details on development status <https://odoo-community.org/page/development-status>`_

**Table of contents**

.. contents::
   :local:

Usage
=====

When creating Analytic Items, if a configuration is in place, the corresponding Analytic Items for indirect cost are generated.

* When an Analytic Item is created, an automatic process checks the Activity Based Cost Rules to identify the ones that apply.
* Each triggered rule created a new Analytic Item, with a copy of the original one, and:
    * Product: is the rule Cost Type Product. A validation error prevents this from being the same as the source Analytic Item Product, to avoid infinite loops.
    * Quantity: is the original quantity multiplied by the rule's Factor
    * Amount: is -1 * Quantity * Product Standard Price
    * Parent Analytic Item (new field): set with the original Analytic Item
* An update on the Quantity triggers a recalculation of the quantity and amount of the child Analytic Items.
* A delete cascades to the child Analytic Items, causing them to also be deleted.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-analytic/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-analytic/issues/new?body=module:%20analytic_activity_based_cost%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Open Source Integrators

Contributors
~~~~~~~~~~~~

* `Open Source Integrators <https://opensourceintegrators.com>`:

  * Daniel Reis <dreis@opensourceintegrators.com>
  * Chandresh Thakkar <cthakkar@opensourceintegrators.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-dreispt| image:: https://github.com/dreispt.png?size=40px
    :target: https://github.com/dreispt
    :alt: dreispt

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-dreispt| 

This module is part of the `OCA/account-analytic <https://github.com/OCA/account-analytic/tree/14.0/analytic_activity_based_cost>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
