#!/usr/bin/env python
"""R26 SC-e-106 check: the four-ticker seed-row evidence file is complete, nothing is guessed, and the table has no row yet.

Usage: python check_four_ticker_evidence.py <evidence.json>   (run from the repo root; one AWS read per ticker)
Evidence file: {"tickers": {"HPI": {...}, "CUBE": {...}, "GLPI": {...}, "PCEF": {...}}, "outside_model_used": false} where each
entry carries lots_rows (list of {asset_name, cusip, market_value}), canonical_holdings_rows (int), source_rows (list of
{source, key, asset_class, sub_asset_class}; empty when no source holds the ticker), proposed_row (null unless source_rows is
non-empty; else {asset_class, sub_asset_class, source}) and table_row_present (bool, must equal the live table).
Prints `FOURTICKER ok=<bool> ...`; exit 0 ok, 1 not ok, 3 file absent.
"""
import json
import os
import sys

WANT = ['CUBE', 'GLPI', 'HPI', 'PCEF']


def live_row(ticker):
    try:
        import boto3
        t = boto3.resource('dynamodb', region_name='us-east-1').Table('etf-classifications')
        return 'Item' in t.get_item(Key={'ticker': ticker})
    except Exception:
        return None


def main():
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print('FOURTICKER ok=False file=ABSENT')
        return 3
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    t = d.get('tickers', {})
    problems = []
    if sorted(t) != WANT:
        problems.append('tickers=%s' % sorted(t))
    if d.get('outside_model_used') is not False:
        problems.append('outside_model_used')
    for k in WANT:
        e = t.get(k) or {}
        for f in ('lots_rows', 'canonical_holdings_rows', 'source_rows', 'proposed_row', 'table_row_present'):
            if f not in e:
                problems.append('%s.%s absent' % (k, f))
        if e.get('proposed_row') is not None and not e.get('source_rows'):
            problems.append('%s proposed_row without a source row' % k)
        if e.get('proposed_row') is not None:
            pr = e['proposed_row']
            if not (pr.get('asset_class') and pr.get('source')):
                problems.append('%s proposed_row incomplete' % k)
        for lr in e.get('lots_rows', []):
            if not (lr.get('asset_name') and 'market_value' in lr):
                problems.append('%s lots_row incomplete' % k)
        lv = live_row(k)
        if lv is None:
            problems.append('%s live read failed' % k)
        elif e.get('table_row_present') is not lv:
            problems.append('%s table_row_present=%s live=%s' % (k, e.get('table_row_present'), lv))
    print('FOURTICKER ok=%s problems=%s' % (not problems, problems))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
