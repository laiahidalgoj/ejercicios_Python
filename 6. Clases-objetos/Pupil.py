class Pupil():
    name = 'Laia'
    note = 9
    _approved = True

    def __init__(self):
        return None

    def printPupil(self):
        return 'Name: ', self.name, 'Note: ', self.note

    def checkNote(self):
        print('The note is: ', self.note)

        if self.note < 5:
            return 'It\'s disapproved'
        else:
            return 'It\'s approved'

pupil1 = Pupil()

print(pupil1.printPupil())
print(pupil1.checkNote())