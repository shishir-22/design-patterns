"""

As per single responsibility principle, a class should have only one responsibility and
only one reason to change.

Suppose, you have a class Journal whose main responsibility is to add, remove and print the contents of Journal.
Now you want to persist the Journal contents in some file, for that as per SRP, we should create a separate class
PersistenceManager whose responsibility will be to save and read the contents of Journal from file.

"""


class Journal:
    """
    Class to maintain the journal entries.
    Main responsibility of class is to add or remove the entries from Journal
    """
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        """
        Method to add the entry in Journal
        :param text: Text to add in journal
        """
        self.entries.append(text)
        self.count += 1

    def delete_entry(self, position):
        """
        Method to delete the entry from given position
        :param position: Index of text in journal
        :return:
        """
        if 0 < position < self.count:
            del self.entries[position]
            self.count -= 1
        else:
            raise Exception("Invalid position of text to delete")

    def print_journal(self):
        """
        Method to print the contents of Journal
        :return:
        """
        print("Journal contents:")
        print("\n".join(self.entries))


class PersistenceManager:
    """
    Class to save/read the contents of journal in file.
    """

    @staticmethod
    def save_journal(journal, location):
        """
        Method to save the journal in file
        :param journal: Journal object
        :param location: Journal file location
        :return:
        """
        with open(location, "w") as f:
            f.write("\n".join(journal.entries))

    @staticmethod
    def read_journal(location):
        """
        Method to read the contents of journal from file
        :param location: Journal file location
        :return:
        """
        with open(location, "r") as f:
            journal_data = f.read()
            print("Journal contents from file")
            print(journal_data)


journal = Journal()
journal.add_entry("This is my first text")
journal.add_entry("This is my second text which I will delete")
journal.add_entry("This is my third text")
journal.delete_entry(1)
journal.print_journal()

journal_location = "journal_location.txt"
PersistenceManager.save_journal(journal, journal_location)
PersistenceManager.read_journal(journal_location)
