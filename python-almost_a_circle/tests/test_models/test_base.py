import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_base_id_generation(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(89)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 89)

    def test_base_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_with_data(self):
        json_string = Base.to_json_string([{"id": 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_base_to_json_string_with_data_returning_string(self):
        json_string = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(json_string, str)

    def test_base_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_base_from_json_string_empty_list(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_base_from_json_string_with_data_returning_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


class TestToJsonString(unittest.TestCase):
    def test_to_json_string_empty_list(self):
        # Prueba cuando se pasa una lista vacía
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        # Prueba cuando se pasa None como argumento
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        # Prueba cuando se pasa una lista con un solo diccionario
        input_list = [{"name": "John", "age": 30}]
        expected_result = json.dumps(input_list)
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)

    def test_to_json_string_multiple_dicts(self):
        # Prueba cuando se pasa una lista con varios diccionarios
        input_list = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        expected_result = json.dumps(input_list)
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_create_rectangle(self):
        dictionary = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        rect = Rectangle.create(**dictionary)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_create_square(self):
        dictionary = {"id": 2, "size": 7, "x": 4, "y": 5}
        square = Square.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)


class TestSquare(unittest.TestCase):

    def test_square_load_from_file(self):
        square1 = Square(5, 2, 3, 1)
        square2 = Square(7, 4, 5, 2)
        squares = [square1, square2]

        # Guardar los objetos Square en un archivo JSON
        filename = "Square.json"
        with open(filename, "w") as jsonfile:
            jsonfile.write(
                Square.to_json_string([square.to_dictionary() for square in squares])
            )

        # Cargar los objetos Square desde el archivo JSON
        loaded_squares = Square.load_from_file()

        # Verificar que se hayan cargado los objetos correctamente
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[0].id, square1.id)
        self.assertEqual(loaded_squares[0].size, square1.size)
        self.assertEqual(loaded_squares[0].x, square1.x)
        self.assertEqual(loaded_squares[0].y, square1.y)
        self.assertEqual(loaded_squares[1].id, square2.id)
        self.assertEqual(loaded_squares[1].size, square2.size)
        self.assertEqual(loaded_squares[1].x, square2.x)
        self.assertEqual(loaded_squares[1].y, square2.y)


if __name__ == "__main__":
    unittest.main()
