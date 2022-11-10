import collections

class Secret(collections.abc.Mapping):
    """Container for a secret with name, description, and
    multiple key-value pairs. Immutable and avoids logging
    internal values when possible.

    :param name:        Name of secret
    :param description: Human-friendly description for secret
    :param values:      Dictionary of key-value pairs stored in secret
    """

    def __init__(self, name, description, values):
        self._name = name
        self._desc = description
        self._dict = collections.OrderedDict(**values)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._desc

    def update(self, kvpairs):
        self._dict.update(kvpairs)

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __contains__(self, key):
        return key in self._dict

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __repr__(self):
        return "Secret(name={name}, keys=[{keys}])".format(
            name=self.name, keys=", ".join(str(key) for key in self.keys())
        )

class SecretObject():

    def create_secret_object(self, name, description, **values):
        """Create a secret object. Immutable and avoids logging
        internal values when possible.

        :param name:        Name of secret
        :param description: Human-friendly description for secret
        :param values:      Dictionary of key-value pairs stored in secret
        """
        return Secret(name, description, values)

