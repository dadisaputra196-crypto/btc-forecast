#!/usr/bin/env python3
"""btc-cent-forecast-01: forecast BTC's close 240 minutes after the checkpoint.

Model: gentle shrinkage of the checkpoint close toward the 24-hour mean.
  guess = 0.90 * last_close + 0.10 * mean(last 1440 closes)
Beats persistence slightly on walk-forward tests over the practice
recording; standard library only, deterministic, offline.
"""
import json
import os
import re

INPUT_DIR = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

MIN_PRICE = 0.00001
MAX_PRICE = 9_999_999.99999


def price5(x):
    return round(min(MAX_PRICE, max(MIN_PRICE, x)) * 1e5) / 1e5


def forecast(prices):
    last = prices[-1]
    window = prices[-1440:] if len(prices) >= 1440 else prices
    mean = sum(window) / len(window)
    return price5(0.90 * last + 0.10 * mean)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    inputs = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith(".in"))
    for fname in inputs:
        case_id = fname[:-3]
        with open(os.path.join(INPUT_DIR, fname)) as fh:
            case = json.load(fh)
        rows = []
        for m in case.get("markets", []):
            rows.append({"case": case_id, "price": forecast(m["prices"])})
        out = os.path.join(OUTPUT_DIR, case_id + ".out")
        with open(out, "w") as fh:
            json.dump({"forecasts": rows}, fh)


if __name__ == "__main__":
    main()
