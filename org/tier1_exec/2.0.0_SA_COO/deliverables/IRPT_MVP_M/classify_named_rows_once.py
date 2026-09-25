"""Andrew's ONE OpenAI classification run over the unclassified Holdings securities (CTO R5; Andrew-direct
2026-09-25 ~14:4xZ, org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260925_144xZ_CLASSIFIER_OTHER_OPENAI_RUN_AND_DEV_PUSH.md
@705be61575: "Yes, one run (Recommended)").

Two modes:
  freeze  No vendor call. Reads the 287 rows (CLASSIFIER_WIDENING_REQUEST_ROWS_AND_READERS_20260924.json) and gives
          each one its source's own name:
            COT  the served name;
            49F  the Schwab security master (holdings_49f.security_names over dim_asset);
            INF  the Orion positions `name` by product_id (the served symbol is a masked CUSIP).
          A row with no name is EXCLUDED with its reason, never sent. Writes the input file with the sha256 of its
          canonical items.
  run     The ONE vendor call. B_01b's method (data/black_diamond/scripts/gold/B_01b.classify_new_securities.py:
          gpt-5.4-mini, batches of 50, json_object, temperature 0.1, secret openai-api-key), with its prompt amended
          to Andrew's rule. It refuses unless --expect-sha matches the frozen input, and refuses if the results file
          already exists. It writes the results file only: NOTHING goes to bd-securities. That write is a separate
          act, under the CTO's never-widen half.

Usage (from the worktree root):
  python org/.../IRPT_MVP_M/classify_named_rows_once.py freeze --out <input.json>
  python org/.../IRPT_MVP_M/classify_named_rows_once.py run --input <input.json> --expect-sha <sha> --out <results.json>
"""
import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
sys.path.insert(0, str(ROOT / 'lib'))
sys.path.insert(0, str(ROOT / 'data/assets/scripts/gold/investor_reporting'))
ROWS = ROOT / 'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/CLASSIFIER_WIDENING_REQUEST_ROWS_AND_READERS_20260924.json'
SOURCE_DATES = ('2026-09-22', '2026-09-24')  # the served business date first, then the latest custody partition
MODEL, BATCH_SIZE, TEMPERATURE = 'gpt-5.4-mini', 50, 0.1  # B_01b.classify_new_securities.py:42, :178, :184
VALID = ('equity', 'fixed_income', 'alternatives', 'other')

# B_01b's SYSTEM_PROMPT (:45-70), amended to Andrew's 2026-09-25 rule: investment real estate (a REIT) is
# alternatives; personal and held-away assets are all "other". Every other line is B_01b's own.
SYSTEM_PROMPT = """Classify each security. Use EXACTLY these asset_class values:
  equity | fixed_income | alternatives | other

Classification rules, in this order:
  - Personal and held-away assets -> other, whatever their type. This covers a client's home or other personal
    property, a manually entered asset, and an account, annuity or policy held at another institution and only
    reported here.
  - Investment-oriented real estate (a REIT, a real-estate fund or partnership) -> alternatives
  - Shield, Buffer, Cap/Protect, Annuity, Structured Note, Barrier Note,
    Principal Protected, Linked Note, Managed Floor products -> alternatives
  - Futures ETF/ETN, VIX products, Commodity funds -> alternatives
  - Hedge fund, long/short, market neutral, merger arb, private equity or credit LP -> alternatives
  - Bond, Treasury, Municipal, TIPS, CLO, FRN, Debenture, Certificate of Deposit -> fixed_income
  - Money Market, Sweep, Cash Reserve -> fixed_income
  - Stock, ETF (equity index), equity mutual fund, target-date or 529 portfolio -> equity

Sub-asset class MUST come from this list when it applies:
  Equity:       US Large Cap, US Mid Cap, US Small Cap, Developed, EM, Global,
                International, Volatility, Commodities
  Fixed Income: Ultra Short Duration, Short Duration, Intermediate, Long Duration,
                High Yield, Investment Grade, Municipal, TIPS, Structured Credit,
                International, Cash
  Alternatives: Gold, Silver, Oil, Commodities, Volatility, Structured Notes, Options,
                Real Estate, Private Equity, Private Credit, Hedge Fund
  Other:        Held Away, Personal Property, Manual Asset

Only create a new sub_asset_class name if none of the above apply.
Confidence: 0.0-1.0. Items with confidence < 0.7 get needs_review=true.

Return a JSON object with a "results" array, one entry per input item, echoing its "id":
{"results": [{"id": "...", "ticker": "...", "asset_name": "...", "asset_class": "...",
  "sub_asset_class": "...", "confidence": 0.0, "rationale": "..."}]}"""


def _canonical_sha(items) -> str:
    return hashlib.sha256(json.dumps(items, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


def _clean(value) -> str:
    return ' '.join(str(value or '').split())


def _first(loader):
    """The first SOURCE_DATES partition the loader resolves, as (date, mapping)."""
    for date in SOURCE_DATES:
        mapping = loader(date)
        if mapping:
            return date, mapping
    return None, {}


def freeze(out: Path):
    import boto3
    import holdings_49f as h49
    import holdings_snapshot as hs
    s3 = boto3.client('s3', region_name='us-east-1')
    rows = json.loads(ROWS.read_text(encoding='utf-8'))['rows']

    def master_names(date):
        return h49.security_names(hs._read_parquet(
            s3, h49.SOURCE_BUCKET, h49.SCHWAB_PREFIX + 'dim_asset/date=%s/data.parquet' % date))

    def orion_names(date):
        _, key = hs._inf_positions_source_key(s3, date)
        pos = hs._read_parquet(s3, hs.INF_SOURCE_BUCKET, key)
        if pos.empty:
            return {}
        seen = {}
        for pid, name in zip(pos['product_id'], pos['name']):
            pid = str(pid).replace('.0', '') if str(pid).endswith('.0') else str(pid)
            if _clean(name):
                seen.setdefault(pid, set()).add(_clean(name))
        return {pid: names.pop() for pid, names in seen.items() if len(names) == 1}

    f49_date, f49 = _first(master_names)
    inf_date, inf = _first(orion_names)
    items, excluded = [], []
    for firm, block in rows.items():
        for r in block['rows']:
            rid = '%s:%s:%s' % (firm, r['id_namespace'], r['id_value'])
            symbol, name, source = _clean(r.get('symbol')), _clean(r.get('name')), 'served'
            if firm == '49financial':
                name, source = f49.get(r['id_value'], ''), 'schwab dim_asset date=%s' % f49_date
            elif firm == 'inflection':
                name, source = inf.get(r['id_value'], ''), 'orion positions_mv snapshot_date=%s' % inf_date
                symbol = '' if 'xxxx' in symbol else symbol  # a masked CUSIP carries no information
            if not name:
                excluded.append({'id': rid, 'served_usd': r.get('served_usd'), 'reason': 'no name in %s' % source})
                continue
            items.append({'id': rid, 'ticker': symbol, 'asset_name': name, 'name_source': source,
                          'served_usd': r.get('served_usd')})
    doc = {'frozen_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'rows_file': str(ROWS.relative_to(ROOT)),
           'items': items, 'excluded': excluded, 'items_sha256': _canonical_sha(items),
           'counts': {firm: sum(1 for i in items if i['id'].startswith(firm + ':')) for firm in rows}}
    out.write_text(json.dumps(doc, indent=1) + '\n', encoding='utf-8')
    print('OK: froze %d item(s), excluded %d; sha256 %s -> %s' % (len(items), len(excluded), doc['items_sha256'], out))


def run(inp: Path, expect_sha: str, out: Path):
    doc = json.loads(inp.read_text(encoding='utf-8'))
    if _canonical_sha(doc['items']) != expect_sha or doc['items_sha256'] != expect_sha:
        raise SystemExit('REFUSED: the input is not the frozen list named by --expect-sha')
    if out.exists():
        raise SystemExit('REFUSED: %s exists -- Andrew authorised ONE run' % out)
    import boto3
    from openai import OpenAI
    key = boto3.client('secretsmanager', region_name='us-east-1').get_secret_value(SecretId='openai-api-key')['SecretString']
    client = OpenAI(api_key=key)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    by_id, results, failures = {i['id']: i for i in doc['items']}, {}, []
    for n in range(0, len(doc['items']), BATCH_SIZE):
        batch = [{'id': i['id'], 'ticker': i['ticker'], 'asset_name': i['asset_name']} for i in doc['items'][n:n + BATCH_SIZE]]
        for attempt in range(5):  # B_01b's call_openai backoff (:173-195)
            try:
                resp = client.chat.completions.create(
                    model=MODEL, temperature=TEMPERATURE, response_format={'type': 'json_object'},
                    messages=[{'role': 'system', 'content': SYSTEM_PROMPT}, {'role': 'user', 'content': json.dumps(batch)}])
                for r in json.loads(resp.choices[0].message.content).get('results', []):
                    if r.get('id') in by_id:
                        results[r['id']] = r
                break
            except Exception as exc:  # noqa: BLE001
                if attempt == 4:
                    failures.append({'batch_start': n, 'error': str(exc)[:300]})
                else:
                    time.sleep(2 ** attempt + 1)
    rows = []
    for i in doc['items']:
        r = results.get(i['id'])
        cls = (r or {}).get('asset_class')
        conf = float((r or {}).get('confidence') or 0.0)
        rows.append({**i, 'asset_class': cls if cls in VALID else None, 'answered': r is not None,
                     'invalid_class': r is not None and cls not in VALID,
                     'sub_asset_class': (r or {}).get('sub_asset_class'), 'confidence': conf,
                     'needs_review': conf < 0.7, 'rationale': (r or {}).get('rationale')})
    out.write_text(json.dumps({'run_started_utc': started, 'model': MODEL, 'temperature': TEMPERATURE,
                               'batch_size': BATCH_SIZE, 'input': str(inp), 'input_sha256': expect_sha,
                               'system_prompt': SYSTEM_PROMPT, 'batch_failures': failures, 'results': rows},
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
