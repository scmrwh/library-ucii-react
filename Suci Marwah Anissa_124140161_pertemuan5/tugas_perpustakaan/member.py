# member.py
class Member:
    def __init__(self, id_member: str, nama: str):
        self.id_member = id_member
        self.nama = nama

    def __str__(self) -> str:
        return f"Member: {self.nama} (ID: {self.id_member})"