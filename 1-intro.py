def loose_greeting(name):
    return 'Hello {}'.format(name)


def loose_typed_greeting(name: str) -> str:
    return 'Hello {}'.format(name)


def strict_greeting(name):
    return 'Hello ' + name


def strict_typed_greeting(name: str) -> str:
    return 'Hello ' + name


print(strict_greeting("Guus"))
print(strict_greeting(42))

print(strict_typed_greeting("Guus"))
print(strict_typed_greeting(42))
