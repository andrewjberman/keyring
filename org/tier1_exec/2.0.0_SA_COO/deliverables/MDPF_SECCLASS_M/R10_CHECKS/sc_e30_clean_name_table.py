#!/usr/bin/env python3
"""sc_e30_clean_name_table.py -- MDPF_SECCLASS round 8, cell SC-e-30 (FWD-14, FWD-11): the issuer's grounded test table
for the one clean-name function `infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name(name)`.

Every input below is a REAL `name` value read (read-only scan) from DynamoDB etf-classifications on 2026-10-07 by
2.0.0_SA_COO~M1. The worker does not edit this file. Run: python <this file>  -> prints CLEAN-NAME-TABLE ok=True|False.

The rule (PRD addendum v0.4 "Clean naming"; addendum v0.7 "Names"): proper case from the source name, vendor suffixes and
all-caps removed; one function with a test table, never a model output. Precisely:
  1. None or a blank string -> None.
  2. Whitespace is collapsed to single spaces and stripped.
  3. A name that already carries a lowercase letter is the source's own writing: returned after step 2 only.
  4. An all-capitals name: a trailing vendor suffix token (COM, SHS) is dropped; then every word is capitalized
     (first letter upper, rest lower), each hyphen-separated part separately, EXCEPT:
       - a token holding a digit or '%' or '/' is kept exactly (3.7%, 02/28/2027, 5%27, 10+ is kept by the digit rule);
       - a one-letter token is kept upper (share-class letters: F, Z, A; and the N A of a bank name);
       - a token in the keep-upper set {ETF, ETN, USD, USA, US, U.S., REIT, II, III, IV} is kept upper;
       - a token in the brand map {ISHARES: iShares, JPMORGAN: JPMorgan} takes the mapped spelling.
     No abbreviation is expanded (BK stays Bk, TREAS stays Treas): expanding is a meaning call, not casing.
"""
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(_REPO / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))

TABLE = [
    # all-capitals inputs (classified_by scheduled or seed in the live table)
    ("MAXIMUS INC COM", "Maximus Inc"),
    ("COCA-COLA EUROPACIFIC PARTNERS SHS", "Coca-Cola Europacific Partners"),
    ("ISHARES CORE TOTAL USD BOND MARKET ETF", "iShares Core Total USD Bond Market ETF"),
    ("ISHARES 10+ YEAR INVESTMENT GRADE CORPORATE BOND ETF", "iShares 10+ Year Investment Grade Corporate Bond ETF"),
    ("DIMENSIONAL U.S. EQUITY MARKET ETF", "Dimensional U.S. Equity Market ETF"),
    ("GOLDMAN SACHS BK USA 3.7% 2028", "Goldman Sachs Bk USA 3.7% 2028"),
    ("UNITED STATES TREAS NTS 4.125% 02/28/2027", "United States Treas Nts 4.125% 02/28/2027"),
    ("BOWLING GREEN OHIO  5%27", "Bowling Green Ohio 5%27"),
    ("JPMORGAN CHASE BK N A 4% 2030", "JPMorgan Chase Bk N A 4% 2030"),
    ("HARTFORD SCHRODERS EMERGING MKTS EQ F", "Hartford Schroders Emerging Mkts Eq F"),
    ("AMERICAN FUNDS CAPITAL INCOME BLDR F3", "American Funds Capital Income Bldr F3"),
    # controls: already written by the source (carry lowercase) -> unchanged
    ("Monolithic Power Systems Inc", "Monolithic Power Systems Inc"),
    ("iShares Ultra Short Duration Bond Active ETF", "iShares Ultra Short Duration Bond Active ETF"),
    ("JPMorgan Chase & Co.", "JPMorgan Chase & Co."),
    ("TrueShares Quarterly Bear Hedge ETF", "TrueShares Quarterly Bear Hedge ETF"),
    # empty
    (None, None),
    ("   ", None),
]


def main():
    try:
        from security_name import clean_name
    except Exception as exc:  # noqa: BLE001 -- deliberate: any import failure (absent module at the base, or a broken one) is a FAIL with its type printed
        print(f"CLEAN-NAME-TABLE ok=False import_error={type(exc).__name__}")
        return 1
    bad = []
    for raw, want in TABLE:
        got = clean_name(raw)
        if got != want:
            bad.append((raw, want, got))
    for raw, want, got in bad:
        print(f"MISMATCH input={raw!r} want={want!r} got={got!r}")
    print(f"CLEAN-NAME-TABLE ok={not bad!s} cases={len(TABLE)} mismatches={len(bad)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
