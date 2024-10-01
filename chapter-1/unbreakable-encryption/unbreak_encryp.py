from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate random length bytes
    tb: bytes = token_bytes(length)
    # convert these bytes into a bit chain and return
    return int.from_bytes(tb, "big")


