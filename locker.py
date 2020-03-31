class Interpreter(object):
    locker_data = []

    def __init__(self, input):
        input = input.split()
        self.command = input[0]
        self.args = input[1:]

    def validate(self):
        no_argument = ['status', 'exit']
        single_argument = ['search', 'find', 'leave', 'init']
        two_argument = ['input']
        available_command = ['status', 'exit',
                             'search', 'find', 'leave', 'init', 'input']
        message = None

        if self.command not in available_command:
            message = "%s tidak terdefinisi." % self.command
        elif self.command in single_argument and len(self.args) != 1:
            message = "%s hanya menerima 1 argumen." % self.command
        elif self.command in two_argument and len(self.args) != 2:
            message = "%s hanya menerima 2 argumen." % self.command
        elif self.command in no_argument and len(self.args):
            message = "%s tidak menerima argumen." % self.command

        return message

    def run_command(self):
        error = self.validate()
        if error:
            print(error)
            return False

        if self.command == 'init':
            if len(self.locker_data):
                self.locker_data.clear()
            return self.do_init()

        elif self.command == 'exit':
            return self.do_exit()
        elif self.command == 'status':
            return self.do_status()
        elif self.command == 'leave':
            return self.do_leave()
        elif self.command == 'input':
            return self.do_input()
        elif self.command == 'search':
            return self.do_search()
        elif self.command == 'find':
            return self.do_find()

    def do_init(self):
        if not self.args[0].isdigit():
            print("Tipe argumen harus angka.")
            return False

        total_locker = int(self.args[0])
        for i in range(total_locker):
            self.locker_data.append([i+1, None, None])

    def do_input(self):
        input = self.args
        id_type = input[0]
        id_number = input[1]

        # validate locker is available
        if len(self.locker_data) < 1:
            print("Anda belum menginialisasi jumlah loker.")
            return False

        available = False
        no_locker = 0
        for locker in self.locker_data:
            if locker[1]:
                continue
            else:
                available = True
                no_locker = locker[0]
                break

        if not available:
            print("Maaf, semua loker telah terisi.")
            return False

        self.locker_data[no_locker-1] = [no_locker, id_type, id_number]
        print("Kartu identitas tersimpan pada loker nomer %d." % no_locker)

    def do_status(self):
        if len(self.locker_data) < 1:
            print("Anda belum menginialisasi jumlah loker.")
            return False

        print("No Loker                  Tipe ID                 No ID\n")
        for locker in self.locker_data:
            no = locker[0]
            id_type = locker[1] or 'Kosong'
            id_number = locker[2] or 'Kosong'
            print("%d                         %s                      %s" %
                  (no, id_type, id_number))

    def do_find(self):
        no_locker = 0
        for locker in self.locker_data:
            if locker[2] == self.args[0]:
                no_locker = locker[0]
                break

        if no_locker:
            print("Kartu identitas %s beradapa pada loker nomer %s." %
                  (self.args[0], no_locker))
        else:
            print("Nomer identitas tidak ditemukan.")

    def do_search(self):
        id_numbers = []
        for locker in self.locker_data:
            if locker[1] == self.args[0]:
                id_numbers.append(locker[2])

        if id_numbers:
            id_numbers = ', '.join(id_numbers)
            print("ID Number dengan tipe %s:  %s." %
                  (self.args[0], id_numbers))
        else:
            print("Tipe identitas tidak ditemukan.")

    def do_leave(self):
        if int(self.args[0]) > len(self.locker_data):
            print("Hanya bisa mengkosongkan loker dari 1 - %s." %
                  len(self.locker_data))
            return False

        no_locker = int(self.args[0])
        self.locker_data[no_locker-1] = [no_locker, None, None]
        print("Loker no %s berhasil dikosongkan." % no_locker)

    def do_exit(self):
        return exit()


def main():
    while True:
        try:
            text = input('(loker) ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        interpreter.run_command()


if __name__ == '__main__':
    main()
