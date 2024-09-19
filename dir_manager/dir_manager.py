import os
import logging
from datetime import datetime
from typing import Optional

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 환경 변수에서 BASE_DIR을 가져오며, 기본값을 설정
BASE_DIR = os.getenv("BASE_DIR", "D:/send")


def create_folder(folder_path: str) -> None:
    """
    주어진 경로에 폴더를 생성합니다. 폴더가 이미 존재하면 예외 없이 진행됩니다.

    Args:
        folder_path (str): 생성할 폴더의 경로
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
        logging.info(f"폴더가 생성되었거나 이미 존재합니다: {folder_path}")
    except OSError as e:
        logging.error(f"폴더 생성 중 오류가 발생했습니다: {e}")
        raise


def get_base_path(dir_name: Optional[str] = None) -> str:
    """
    현재 연도와 월을 포함하는 기본 경로를 생성하고 반환합니다.
    dir_name이 None일 경우 기본 경로는 BASE_DIR/{year}/{month} 형식이 됩니다.

    Args:
        dir_name (Optional[str]): 생성할 디렉토리 이름 (기본값: None)

    Returns:
        str: 생성된 기본 경로
    """
    current_date = datetime.now()
    current_year = current_date.year
    current_month = f"{current_date.month:02}"

    # 리스트 기반으로 동적 경로 생성
    path_parts = [BASE_DIR, str(current_year), current_month]
    if dir_name:
        path_parts.append(dir_name)

    base_dir_path = os.path.join(*path_parts)

    # 디렉토리 생성
    create_folder(base_dir_path)

    return base_dir_path
