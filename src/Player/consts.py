from enum import Enum

PlayerState = Enum(
    "PlayerState",
    [
        ("ACTIVE", 1),
        ("STOPPED", 2),
        ("FAILED", 3),
    ],
)
