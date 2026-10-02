"""build_residual_cusip_set.py -- MDPF_SECCLASS BD r3 re-land residual, first per-ticker act (CTO batch 161: the residual's
private funds and the rest go to the next per-ticker act, in dollar order). Read-only against the table.

The act's population: the 68 names that reach 80 percent of the residual's CUSIP-keyed dollars (R8_BD_RELAND_RESIDUAL_BY_NAME,
09-30 positions; each name's one valid CUSIP in the 09-25 lots). Each name is read by kind from its custody name (INFERRED from the
name and category; no vendor called) and given ONE disposition below. A WRITE row copies its PEER's class and sub class from the
LIVE table (never typed); the CUSIP itself is the key (Cottonwood's CUSIP-row method, R7_CHECKS/write_cusip_rows.py).
Output: R8_CHECKS/RESIDUAL_CUSIP_WRITE_SET_20261002.tsv (cusip, class, sub, name) and a disposition table on stdout.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
OUT = HERE / "RESIDUAL_CUSIP_WRITE_SET_20261002.tsv"
FIRST = HERE / "R8_RESIDUAL_FIRST_ACT_68_20261002.json"

# CUSIP -> (disposition, peer or explicit 'class/sub', reading). WRITE_PEER copies the peer's row; WRITE_RULED is a ruled pair.
PLAN = {
    # same security as a ticker row the table holds (BD's feed carries its CUSIP blank-tickered)
    "922908751": ("WRITE_PEER", "VB", "Vanguard Small-Cap ETF (VB's CUSIP)"),
    "922908629": ("WRITE_PEER", "VO", "Vanguard Mid-Cap ETF (VO's CUSIP)"),
    "922908512": ("WRITE_PEER", "VOE", "Vanguard Mid-Cap Value ETF (VOE's CUSIP)"),
    "922908678": ("WRITE_PEER", "VVIAX", "Vanguard Value Index Admiral (VVIAX's CUSIP)"),
    "060505104": ("WRITE_PEER", "BAC", "Bank of America common (BAC's CUSIP)"),
    # funds and ETFs of a kind the table holds
    "25434V401": ("WRITE_PEER", "IVV", "Dimensional U.S. Equity Market ETF -- broad US equity"),
    "33741X102": ("WRITE_PEER", "IJH", "First Trust SMID Cap Rising Dividend ETF -- US small/mid"),
    "78433H675": ("WRITE_PEER", "JEPI", "NEOS Nasdaq 100 High Income ETF -- options income"),
    "412295107": ("WRITE_PEER", "VEA", "Harding Loevner International Equity -- developed international equity"),
    "746802800": ("WRITE_PEER", "IVV", "Putnam Large Cap Growth"),
    "19765N278": ("WRITE_PEER", "IVV", "Columbia Dividend Income -- US large-cap dividend"),
    "74440Y801": ("WRITE_PEER", "HYG", "PGIM High Yield"),
    "410223408": ("WRITE_PEER", "AGG", "John Hancock Bond -- core bond"),
    "543916688": ("WRITE_PEER", "VCSH", "Lord Abbett Short Duration Income"),
    "693390882": ("WRITE_PEER", "BNDX", "PIMCO International Bond (USD-hedged)"),
    "316146356": ("WRITE_PEER", "AGG", "Fidelity U.S. Bond Index"),
    "00900W100": ("WRITE_PEER", "ACWI", "Invesco Global -- global equity"),
    "19766P587": ("WRITE_PEER", "IJH", "Columbia Select Mid Cap Value"),
    "31421N402": ("WRITE_PEER", "IJR", "Federated Hermes Kaufmann Small Cap"),
    "61756E784": ("WRITE_PEER", "IVV", "Morgan Stanley Inst Advantage -- US large-cap growth"),
    "52471R630": ("WRITE_PEER", "IVV", "ClearBridge Select -- US equity"),
    "025083882": ("WRITE_PEER", "IVV", "American Century Ultra -- US large-cap growth"),
    "643822828": ("WRITE_PEER", "ACWI", "American Funds New Economy -- global growth equity"),
    "33737M300": ("WRITE_PEER", "IJR", "First Trust Small Cap Growth AlphaDEX"),
    "808516801": ("WRITE_PEER", "VEA", "International Equity Index Pool (529)"),
    "808516108": ("WRITE_PEER", "IVV", "Large Cap Equity Managed Pool (529)"),
    "808516702": ("WRITE_PEER", "IVV", "Total Market Equity Index Pool (529)"),
    "09182TBT3": ("WRITE_PEER", "MUB", "Black Belt Energy Gas District 5.5% 2053 -- a municipal bond"),
    "67180K205": ("WRITE_PEER", "VNQ", "Blue Owl Real Estate Net Lease Trust -- non-traded REIT"),
    "302950407": ("WRITE_PEER", "VNQ", "FS Credit Real Estate Income Trust -- non-traded real-estate credit REIT"),
    # structured notes: the outcome-note kind batch 145 B ruled structured / Hedge (VXX's pair) for buffer ETFs
    "06745PR94": ("WRITE_RULED", "structured/Hedge", "Barclays Bank 0% 2027 -- structured note"),
    "48134XQ99": ("WRITE_RULED", "structured/Hedge", "JPMorgan Chase Financial 0% 2028 -- structured note"),
    "61776M6X8": ("WRITE_RULED", "structured/Hedge", "Morgan Stanley Finance 2026 -- structured note"),
    "61778K2Z9": ("WRITE_RULED", "structured/Hedge", "Morgan Stanley Finance 0% 2029 -- structured note"),
    "05556NSE7": ("WRITE_RULED", "structured/Hedge", "BBVA Global Securities -- structured note"),
    "05554TQJ7": ("WRITE_RULED", "structured/Hedge", "BBVA Global Securities 0% 2030 -- structured note"),
}
NOT_WRITTEN = {
    "allocation (batch 145 C)": ["02630T712", "316345206", "140193103", "704223205", "453320103", "353496490", "92202E508",
                                 "140193780", "024071508", "32008F606", "808516306", "56167N274"],
    "private credit / alternative, no peer of its kind (batch 145 C: XCAPX, NICHX)": ["186854204", "69120V309", "92220Q103",
                                                                                      "000843102", "56167N324", "09261H305"],
    "IBIT (batch 145 D)": ["46438F101"],
    "single stock with no ticker row of its own (size or sector rule not settled, row S8's split)": [
        "84615Q103", "N97284108", "90290N109", "034948109", "91823B109", "00534A102", "43849R105", "G3002J103"],
    "kind not readable from the name": ["88588B100", "NHFSTMX97"],
}


def main() -> int:
    first = json.loads(FIRST.read_text(encoding="utf-8"))
    tab = boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications")
    nw = {c: why for why, cs in NOT_WRITTEN.items() for c in cs}
    out, seen, unplanned, tot = [], set(), [], {"write": 0.0, "not_written": 0.0}
    for name, cusip, usd in first:
        if cusip in PLAN:
            if cusip in seen:
                tot["write"] += usd
                continue
            seen.add(cusip)
            disp, peer, reading = PLAN[cusip]
            if disp == "WRITE_PEER":
                row = tab.get_item(Key={"ticker": peer}).get("Item")
                if not row:
                    raise SystemExit("REFUSED: peer %s has no row" % peer)
                ac, sub = row.get("asset_class"), row.get("sub_asset_class") or ""
            else:
                ac, sub = peer.split("/")
            out.append("\t".join([cusip, ac, sub, name.strip()]))
            tot["write"] += usd
            print("WRITE %-10s %-13s %-15s peer %-16s %12.2f  %s" % (cusip, ac, sub, peer, usd, reading))
        elif cusip in nw:
            tot["not_written"] += usd
            print("NOT   %-10s %-60s %12.2f  %s" % (cusip, nw[cusip][:60], usd, name.strip()[:40]))
        else:
            unplanned.append((name, cusip, usd))
    if unplanned:
        raise SystemExit("REFUSED: names with no disposition: %s" % unplanned)
    OUT.write_text("# BD re-land residual, first per-ticker act (CUSIP rows by peer) -- build_residual_cusip_set.py\n"
                   + "\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print("rows %d; USD write %.2f, not written %.2f -> %s" % (len(out), tot["write"], tot["not_written"], OUT.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
