import unittest
from io import StringIO
from unittest.mock import patch
from locker import Interpreter


class TestLocker(unittest.TestCase):
    # test if command invalid
    def test_error_when_invalid_command(self):
        error_message = "hello tidak terdefinisi.\n"
        test_input = "hello"
        interpreter = Interpreter(test_input)

        # run test
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)

    # test if init have more than 1 arg   
    def test_init_more_than_1_argument(self):
        error_message = "init hanya menerima 1 argumen.\n"
        test_input = "init 123 123"
        interpreter = Interpreter(test_input)

        # run test
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)

    # test success init
    def test_init_accept_1_argument(self):
        test_input = "init 1"
        locker_data_output = [[1, None, None]]

        interpreter = Interpreter(test_input)
        interpreter.run_command()

        self.assertEqual(len(interpreter.locker_data), len(locker_data_output))
        self.assertEqual(interpreter.locker_data, locker_data_output)
    
    def test_init_must_contain_argument(self):
        error_message = "init hanya menerima 1 argumen.\n"
        test_input = "init"
        interpreter = Interpreter(test_input)

        # run test
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)
    
    def test_init_only_accept_number(self):
        error_message = "Tipe argumen harus angka.\n"
        test_input = "init yy"
        interpreter = Interpreter(test_input)

        # run test
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)
    
    def test_input_allow_2_arguments(self):
        error_message = "input hanya menerima 2 argumen.\n"
        test_input = "input SIM 123 123"
        interpreter = Interpreter(test_input)

        # run test
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)
    
    def test_input_must_initiate_first(self):
        error_message = "Anda belum menginialisasi jumlah loker.\n"
        test_input = "input SIM 123"
        interpreter = Interpreter(test_input)

        # run test
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_input_locker_full(self):
        error_message = "Maaf, semua loker telah terisi.\n"
        test_input = "input SIM 1234"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), error_message)
    
    def test_input_locker_available(self):
        message = "Kartu identitas tersimpan pada loker nomer 1.\n"
        test_input = "input SIM 1234"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [[1, None, None]]

        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_leave_with_valid_index_range(self):
        message = "Loker no 1 berhasil dikosongkan.\n"
        test_input = "leave 1"
        interpreter = Interpreter(test_input)
        output_locker_data = [[1, None, None], [2, 'KTM', '4321']]

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]

        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
        
        self.assertEqual(interpreter.locker_data, output_locker_data)
    
    def test_leave_error_if_out_of_locker_length(self):
        message = "Hanya bisa mengkosongkan loker dari 1 - 2.\n"
        test_input = "leave 212"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_leave_must_1_argument(self):
        message = "leave hanya menerima 1 argumen.\n"
        test_input = "leave 212 1"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_search_must_1_argument(self):
        message = "search hanya menerima 1 argumen.\n"
        test_input = "search 212 1"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_search_valid_data(self):
        message = "ID Number dengan tipe KTP:  1234, 2233.\n"
        test_input = "search KTP"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321'],
            [3, 'KTP', '2233']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_search_invalid_type_id(self):
        message = "Tipe identitas tidak ditemukan.\n"
        test_input = "search UNKNOWN"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321'],
            [3, 'KTP', '2233']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_exit_without_argument(self):
        message = "exit tidak menerima argumen.\n"
        test_input = "exit 1234"
        interpreter = Interpreter(test_input)
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_exit_run_normal(self):
        test_input = "exit"
        interpreter = Interpreter(test_input)
        with self.assertRaises(SystemExit) as cm:
            interpreter.run_command()
    
    def test_find_must_1_argument(self):
        message = "find hanya menerima 1 argumen.\n"
        test_input = "find 212 1"
        interpreter = Interpreter(test_input)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_find_data_exist(self):
        message = "Kartu identitas 1234 beradapa pada loker nomer 1.\n"
        test_input = "find 1234"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_find_data_doesnot_exist(self):
        message = "Nomer identitas tidak ditemukan.\n"
        test_input = "find 12342"
        interpreter = Interpreter(test_input)

        # mock self.locker_data
        interpreter.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'KTM', '4321']
        ]
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_status_without_argument(self):
        message = "status tidak menerima argumen.\n"
        test_input = "status 1234"
        interpreter = Interpreter(test_input)
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)
    
    def test_status_show_valid_data(self):
        test_input = "status"
        interpreter = Interpreter(test_input)
        interpreter.locker_data = [[1, 'KTP', '1234'], [2, None, None]]
        contain_string = "1                         KTP                      1234"
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertIn(contain_string, fake_out.getvalue())
    
    def test_search_must_initiate_first(self):
        message = "Anda belum menginialisasi jumlah loker.\n"
        test_input = "status"
        interpreter = Interpreter(test_input)
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            interpreter.run_command()
            self.assertEqual(fake_out.getvalue(), message)

if __name__ == '__main__':
    unittest.main()
