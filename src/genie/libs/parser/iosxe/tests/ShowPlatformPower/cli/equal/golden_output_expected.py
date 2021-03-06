expected_output = {
    "allocation_status": "Sufficient",
    "chassis": "ASR1006-X",
    "excess_capacity_percent": 72,
    "excess_power": 3201,
    "fan_alc": 250,
    "fru_alc": 949,
    "load_capacity_percent": 15,
    "power_capacity": 4400,
    "redundancy_mode": "nplus1",
    "redundant_alc": 0,
    "slot": {
        "0": {"allocation": 64.0, "state": "ok", "type": "ASR1000-SIP40"},
        "0/0": {"allocation": 14.0, "state": "inserted", "type": "SPA-8X1GE-V2"},
        "0/1": {"allocation": 14.0, "state": "inserted", "type": "SPA-8X1GE-V2"},
        "0/2": {"allocation": 17.4, "state": "inserted", "type": "SPA-1X10GE-L-V2"},
        "0/3": {"allocation": 17.4, "state": "inserted", "type": "SPA-1X10GE-L-V2"},
        "1": {"allocation": 64.0, "state": "ok", "type": "ASR1000-SIP40"},
        "1/0": {"allocation": 14.0, "state": "inserted", "type": "SPA-8X1GE-V2"},
        "F0": {"allocation": 267.0, "state": "ok, active", "type": "ASR1000-ESP40"},
        "F1": {"allocation": 267.0, "state": "ok, standby", "type": "ASR1000-ESP40"},
        "P0": {
            "capacity": 1100,
            "load": 132,
            "state": "ok",
            "type": "ASR1000X-AC-1100W",
        },
        "P1": {
            "capacity": 1100,
            "load": 204,
            "state": "ok",
            "type": "ASR1000X-AC-1100W",
        },
        "P2": {
            "capacity": 1100,
            "load": 180,
            "state": "ok",
            "type": "ASR1000X-AC-1100W",
        },
        "P3": {
            "capacity": 1100,
            "load": 180,
            "state": "ok",
            "type": "ASR1000X-AC-1100W",
        },
        "P6": {"allocation": 125.0, "state": "ok", "type": "ASR1000X-FAN"},
        "P7": {"allocation": 125.0, "state": "ok", "type": "ASR1000X-FAN"},
        "R0": {"allocation": 105.0, "state": "ok, active", "type": "ASR1000-RP2"},
        "R1": {"allocation": 105.0, "state": "ok, standby", "type": "ASR1000-RP2"},
    },
    "total_capacity": 4400,
    "total_load": 696,
}
