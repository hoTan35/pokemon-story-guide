import json
from pathlib import Path

# 임시 데이터. 실제 데이터가 오면 이 파일의 읽는 부분만 수정합니다.
DATA_FILE = Path(__file__).resolve().parents[3] / "data" / "mock_map.json"


def _load_data():
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def get_locations():
    return _load_data()["locations"]


def get_location_pokemon(location_id: str):
    """장소가 없으면 None, 장소는 있지만 출현 포켓몬이 없으면 빈 목록을 반환합니다."""
    data = _load_data()

    if not any(location["id"] == location_id for location in data["locations"]):
        return None

    pokemon_ids = {
        encounter["pokemon_id"]
        for encounter in data["encounters"]
        if encounter["location_id"] == location_id
    }
    return [pokemon for pokemon in data["pokemon"] if pokemon["id"] in pokemon_ids]