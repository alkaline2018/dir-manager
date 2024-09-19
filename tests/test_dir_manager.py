import unittest
import os
from unittest import mock
from datetime import datetime
from dir_manager import get_base_path, create_folder


class TestDirectoryFunctions(unittest.TestCase):

    @mock.patch.dict(os.environ, {"BASE_DIR": "/tmp/test_send"})
    def test_get_base_path_without_dir_name(self):
        # dir_name이 None일 경우
        base_path = get_base_path()
        current_date = datetime.now()
        expected_path = os.path.join("/tmp/test_send", str(current_date.year), f"{current_date.month:02}")

        self.assertEqual(base_path, expected_path)
        self.assertTrue(os.path.exists(base_path))

    @mock.patch.dict(os.environ, {"BASE_DIR": "/tmp/test_send"})
    def test_get_base_path_with_custom_dir(self):
        # dir_name이 있을 경우
        base_path = get_base_path("custom_dir")
        current_date = datetime.now()
        expected_path = os.path.join("/tmp/test_send", str(current_date.year), f"{current_date.month:02}", "custom_dir")

        self.assertEqual(base_path, expected_path)
        self.assertTrue(os.path.exists(base_path))

    @mock.patch.dict(os.environ, {"BASE_DIR": "/tmp/test_send"})
    def test_create_folder_existing_directory(self):
        # 이미 존재하는 디렉토리일 경우
        test_dir = "/tmp/test_send/existing_folder"
        os.makedirs(test_dir, exist_ok=True)
        create_folder(test_dir)  # 예외 발생 없이 진행됨

        self.assertTrue(os.path.exists(test_dir))


if __name__ == "__main__":
    unittest.main()
