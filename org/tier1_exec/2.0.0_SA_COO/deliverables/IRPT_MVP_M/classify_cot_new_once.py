"""Andrew's ONE OpenAI classification run over the new COT securities B_01b finds (Andrew-direct ~02:1xZ 2026-09-26,
"all recs approved for 1-3"; record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_021xZ_OPEN_CALLS_1_3_AND_AGENT_WALKS.md
@37025a10e9, CALL 2: one run, dry run first, no retry, no second run; the bd-securities write is the CTO's half).

Two modes:
  freeze  No vendor call. B_01b's own full scan (data/cot/scripts/gold/B_01b.classify_new_securities.py at CLOUD
          e20b0990d5): every gold/canonical/holdings/ partition, partition_pairs(), normalize_key(), minus
          scan_existing_keys(bd-securities). Each new key carries its 2026-09-22 market value (the served business
          date) for the per-client delta. Writes the input file with the sha256 of its canonical items.
  run     The ONE vendor call. B_01b's call_openai (gpt-5.4-mini, batches of 50, json_object, temperature 0.1) with
          B_01b's prompt, max_retries=1: a failed batch stays unanswered, never re-sent. Results are matched back the
          way B_01b matches them: (ticker, asset_name), then normalize_key. Refuses unless --expect-sha matches the
          frozen input, and refuses if the results file exists. Writes the results file only; NOTHING goes to
          bd-securities.

Usage (from the repo root):
  python org/.../IRPT_MVP_M/classify_cot_new_once.py freeze --out <input.json>
  python org/.../IRPT_MVP_M/classify_cot_new_once.py run --input <input.json> --expect-sha <sha> --out <results.json>
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import subprocess
import sys
from io import BytesIO
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
GOLD = ROOT / 'data/cot/scripts/gold'
sys.path.insert(0, str(GOLD))
SERVED_DATE = '2026-09-22'


def _b01b():
    spec = importlib.util.spec_from_file_location('b01b', str(GOLD / 'B_01b.classify_new_securities.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _canonical_sha(items) -> str:
    return hashlib.sha256(json.dumps(items, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


def freeze(out: Path):
    import boto3
    import pandas as pd
    b = _b01b()
    s3 = boto3.client('s3', region_name=b.REGION)
    keys = b._list_holdings_keys(s3)
    pairs, served = set(), {}
    for key in keys:
        body = BytesIO(s3.get_object(Bucket=b.DATA_BUCKET, Key=key)['Body'].read())
        if b._parse_date(key) == SERVED_DATE:
            df = pd.read_parquet(body, columns=['ticker', 'asset_name', 'market_value'])
            for t, a, mv in df.itertuples(index=False):
                pk = b.normalize_key(str(t) if pd.notna(t) else '', str(a) if pd.notna(a) else '')
                mv = pd.to_numeric(mv, errors='coerce')
                served[pk] = served.get(pk, 0.0) + (0.0 if pd.isna(mv) else float(mv))
            pairs |= b.partition_pairs(df)
        else:
            pairs |= b.partition_pairs(pd.read_parquet(body, columns=['ticker', 'asset_name']))
    existing = b.scan_existing_keys(boto3.resource('dynamodb', region_name=b.REGION).Table(b.BD_SECURITIES_TABLE))
    by_pk = {}
    for ticker, asset_name in sorted(pairs):
        pk = b.normalize_key(ticker, asset_name)
        if pk and pk not in existing and pk not in by_pk:
            by_pk[pk] = {'pk': pk, 'ticker': ticker, 'asset_name': asset_name,
                         'served_usd_%s' % SERVED_DATE: round(served.get(pk, 0.0), 2)}
    items = [by_pk[pk] for pk in sorted(by_pk)]
    doc = {'frozen_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'partitions': len(keys),
           'first_partition': keys[0] if keys else None, 'last_partition': keys[-1] if keys else None,
           'pairs': len(pairs), 'existing_keys': len(existing), 'items': items, 'items_sha256': _canonical_sha(items)}
    out.write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print('OK: froze %d new key(s) from %d partition(s), %d pair(s), %d existing; sha256 %s -> %s' % (
        len(items), len(keys), len(pairs), len(existing), doc['items_sha256'], out))


def run(inp: Path, expect_sha: str, out: Path):
    doc = json.loads(inp.read_text(encoding='utf-8'))
    if _canonical_sha(doc['items']) != expect_sha or doc['items_sha256'] != expect_sha:
        raise SystemExit('REFUSED: the input is not the frozen list named by --expect-sha')
    if out.exists():
        raise SystemExit('REFUSED: %s exists -- Andrew authorised ONE run' % out)
    import boto3
    from openai import OpenAI
    b = _b01b()
    key = boto3.client('secretsmanager', region_name=b.REGION).get_secret_value(SecretId='openai-api-key')['SecretString']
    client = OpenAI(api_key=key)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    items = doc['items']
    by_pair = {(i['ticker'], i['asset_name']): i['pk'] for i in items}
    pks = {i['pk'] for i in items}
    results, failures = {}, []
    for n in range(0, len(items), b.BATCH_SIZE):
        batch = [{'ticker': i['ticker'], 'asset_name': i['asset_name']} for i in items[n:n + b.BATCH_SIZE]]
        try:
            answers = b.call_openai(client, batch, max_retries=1)
        except Exception as exc:  # noqa: BLE001 -- one run: a failed batch is recorded, never re-sent
            failures.append({'batch_start': n, 'size': len(batch), 'error': str(exc)[:300]})
            continue
        for r in answers:
            pk = by_pair.get((r.get('ticker', ''), r.get('asset_name', ''))) or b.normalize_key(
                r.get('ticker', ''), r.get('asset_name', ''))
            if pk in pks and pk not in results:
                results[pk] = r
    rows = []
    for i in items:
        r = results.get(i['pk'])
        cls = (r or {}).get('asset_class')
        conf = float((r or {}).get('confidence') or 0.0)
        rows.append({**i, 'asset_class': cls if cls in b.VALID_ASSET_CLASSES else None, 'answered': r is not None,
                     'invalid_class': r is not None and cls not in b.VALID_ASSET_CLASSES,
                     'sub_asset_class': (r or {}).get('sub_asset_class'), 'confidence': conf,
                     'needs_review': conf < 0.7, 'rationale': (r or {}).get('rationale')})
    out.write_text(json.dumps({'run_started_utc': started, 'run_finished_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
                               'model': 'gpt-5.4-mini', 'temperature': 0.1, 'batch_size': b.BATCH_SIZE,
                               'max_retries': 1, 'input': str(inp), 'input_sha256': expect_sha,
                               'system_prompt': b.SYSTEM_PROMPT, 'batch_failures': failures, 'results': rows},
                              indent=1) + '\n', encoding='utf-8')
    answered = sum(1 for r in rows if r['answered'])
    print('OK: %d of %d answered; %d invalid class; %d need review; %d batch failure(s) -> %s' % (
        answered, len(rows), sum(1 for r in rows if r['invalid_class']),
        sum(1 for r in rows if r['answered'] and r['needs_review']), len(failures), out))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)
    f = sub.add_parser('freeze')
    f.add_argument('--out', required=True)
    r = sub.add_parser('run')
    r.add_argument('--input', required=True)
    r.add_argument('--expect-sha', required=True)
    r.add_argument('--out', required=True)
    args = ap.parse_args()
    if args.mode == 'freeze':
        freeze(Path(args.out))
    else:
        run(Path(args.input), args.expect_sha, Path(args.out))


if __name__ == '__main__':
    main()
