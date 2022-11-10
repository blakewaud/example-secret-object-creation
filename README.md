# Secret Object Usage Example

This robot uses a small custom Python library based on the [RPA.Robocorp.Vault library](https://github.com/robocorp/rpaframework/blob/master/packages/main/src/RPA/Robocorp/Vault.py) from [RPA Framework](https://github.com/robocorp/rpaframework).

Secret objects can be created via the `Create Secret Object` keyword. Such objects will not be logged when used as stand alone variables, but can be accessed like dictionaries. The individual values can still be logged if used without consideration for how the various keywords log the arguments given to them and how you pass the values to them.

