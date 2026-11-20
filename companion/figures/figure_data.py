"""Rebuild the two numerical data tables using only the Python standard library."""

from math import exp, fsum, log
from pathlib import Path

HERE = Path(__file__).resolve().parent
EULER_GAMMA = 0.5772156649015328606


def prime_powers(limit):
    """Pairs (n, Lambda(n)) where Lambda(n) is nonzero."""
    is_prime = [True] * (limit + 1)
    pairs = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            for composite in range(2 * p, limit + 1, p):
                is_prime[composite] = False
            n = p
            while n <= limit:
                pairs.append((n, log(p)))
                n *= p
    return sorted(pairs)


def prime_ramps():
    powers = prime_powers(96)
    rows = ["x R G"]
    for index in range(4, 4 * 96 + 1):
        x = index / 4
        ramp = fsum(weight * (x / n - 1) for n, weight in powers if n <= x)
        centered = ramp - x * log(x) + (1 + EULER_GAMMA) * x
        rows.append(f"{x:.2f} {ramp:.12f} {centered:.12f}")
    (HERE / "prime-ramp.dat").write_text("\n".join(rows) + "\n", encoding="ascii")


def localization():
    # v = u/U, sigma = 336, k = 420 U. The mode in v is 5/4.
    rows = ["v Uone Ufour"]
    for index in range(160, 341):
        v = index / 200
        ratio = v / 1.25
        shape = log(ratio) - (ratio - 1)
        values = [exp(420 * U * shape) for U in (1, 4)]
        rows.append(f"{v:.3f} {values[0]:.12g} {values[1]:.12g}")
    (HERE / "kernel.dat").write_text("\n".join(rows) + "\n", encoding="ascii")


if __name__ == "__main__":
    prime_ramps()
    localization()
