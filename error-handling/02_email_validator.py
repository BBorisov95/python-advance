class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


min_length = 5
allowed_domains = ['.com', '.bg', '.org', '.net']

while True:
    email = input()

    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if len(email.split('@')[0]) < min_length:
        raise NameTooShortError('Name must be more than 4 characters')

    if '.' + email.split('.')[-1] not in allowed_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print("Email is valid")
