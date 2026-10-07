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
  4. An all-capitals name: EVERY trailing vendor suffix token (COM, SHS) is dropped, repeatedly, so the function is idempotent; then every word is capitalized
     (first letter upper, rest lower), each hyphen-separated part separately, EXCEPT:
       - a token holding a digit or '%' or '/' is kept exactly (3.7%, 02/28/2027, 5%27, 10+ is kept by the digit rule);
       - a one-letter token is kept upper (share-class letters: F, Z, A; and the N A of a bank name);
       - a token in the keep-upper set {ETF, ETN, USD, USA, US, U.S., REIT, II, III, IV} is kept upper;
       - a token in the brand map {ISHARES: iShares, JPMORGAN: JPMorgan} takes the mapped spelling.
     No abbreviation is expanded (TREAS stays Treas): expanding is a meaning call, not casing.

ROUND 9 (cell SC-e-47, row W28-S5; the issuer's rule, 2.0.0_SA_COO~M1): step 4 also keeps, exactly as written,
  - a whole name that is ONE token of 1-5 characters (a ticker used as the name: WMT stays WMT);
  - a token of 2-4 letters holding no vowel (A E I O U Y): an acronym or abbreviation (BP, GSK, MPLX, BK, NTS, MKTS, BLDR);
  - a token in the corporate-form set {PLC, LP, LLC, NA, NV, AG, SA, SE};
  and lowers a joining word {OF, AND, THE, FOR, IN, ON, AT, TO, BY} that is not the first word.
  Four round-8 expectations change with it (BK, NTS, MKTS, BLDR now stay upper); the change is stated in the R9 issuance.
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
    ("GOLDMAN SACHS BK USA 3.7% 2028", "Goldman Sachs BK USA 3.7% 2028"),
    ("UNITED STATES TREAS NTS 4.125% 02/28/2027", "United States Treas NTS 4.125% 02/28/2027"),
    ("BOWLING GREEN OHIO  5%27", "Bowling Green Ohio 5%27"),
    ("JPMORGAN CHASE BK N A 4% 2030", "JPMorgan Chase BK N A 4% 2030"),
    ("HARTFORD SCHRODERS EMERGING MKTS EQ F", "Hartford Schroders Emerging MKTS Eq F"),
    ("AMERICAN FUNDS CAPITAL INCOME BLDR F3", "American Funds Capital Income BLDR F3"),
    # round 9 (W28-S5): the three legacy WRITE rows, a ticker used as a name, a joining word, a bank form
    ("BP PLC", "BP PLC"),
    ("GSK PLC", "GSK PLC"),
    ("MPLX LP", "MPLX LP"),
    ("WMT", "WMT"),
    ("BANK OF AMERICA CORP", "Bank of America Corp"),
    ("WELLS FARGO BANK NA 4.1% 2029", "Wells Fargo Bank NA 4.1% 2029"),
    # round 9 amendment 1 (row W35-S1): trailing vendor suffixes drop repeatedly, so a second pass changes nothing
    ("ETF SHS COM", "ETF"),
    # controls: already written by the source (carry lowercase) -> unchanged
    ("Monolithic Power Systems Inc", "Monolithic Power Systems Inc"),
    ("iShares Ultra Short Duration Bond Active ETF", "iShares Ultra Short Duration Bond Active ETF"),
    ("JPMorgan Chase & Co.", "JPMorgan Chase & Co."),
    ("TrueShares Quarterly Bear Hedge ETF", "TrueShares Quarterly Bear Hedge ETF"),
    # SC-e-48 re-request (CTO half REFUSED @cadf21e1f1 items 1-3): depositary/fund forms upper; LTD/PLC and the foreign forms upper in
    # ONE casing whatever the input's; Inc/Corp/Co title-case; short all-caps non-word tokens (ABB, AAA, CLO, PGIM) upper.
    ("ABB LTD SPONSORED ADR", "ABB LTD Sponsored ADR"),
    ("PGIM AAA CLO ETF", "PGIM AAA CLO ETF"),
    ("ZURICH INSURANCE GROUP LTD", "Zurich Insurance Group LTD"),
    ("Ferguson Plc Ord", "Ferguson PLC Ord"),
    ("Smith & Nephew Ltd", "Smith & Nephew LTD"),
    ("SIEMENS AG SPONSORED ADS", "Siemens AG Sponsored ADS"),
    ("Novartis Ag Adr", "Novartis AG ADR"),
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
