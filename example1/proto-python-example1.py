'''
Example of protobuf using Python
'''
import logging
from pathlib import Path

from addressbook_pb2 import AddressBook

from IPython import embed


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


SCRIPT_DIR = Path(__file__).parent.resolve()


def main() -> None:
    print('in main')
    address_book = AddressBook()
    embed()


if __name__ == '__main__':
    main()
