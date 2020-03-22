'''
Example of protobuf using Python

1. Create 2 Person objects
2. Create 1 AddressBook object from a list of Person
3. Write AddressBook to a binary file
4. Read AddressBook from a binary file
5. Display AddressBook
'''
import logging
from pathlib import Path
import io

import addressbook_pb2

from IPython import embed


log = logging.getLogger(__name__)


SCRIPT_DIR = Path(__file__).parent.resolve()


def create_Person(name):
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = name
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.HOME
    return person


def create_AddressBook(personList):
    addressBook = addressbook_pb2.AddressBook()
    for person in personList:
        addressBook.people.append(person)
    return addressBook


def get_sample_AddressBook():
    person1 = create_Person('Alice')
    person2 = create_Person('Bob')
    log.info(person1)
    log.info(person2)
    addressBook = create_AddressBook([person1, person2])
    log.info(addressBook)
    return addressBook


def main():
    addressBook = get_sample_AddressBook()
    with io.BytesIO() as f:
        f.write(addressBook.SerializeToString())
        addressBook = addressbook_pb2.AddressBook()
        addressBook.ParseFromString(f.getvalue())
        print(addressBook)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    main()
