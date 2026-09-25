"""Prepare a firm's CLASSIFIED Holdings candidate: the SERVED revision to the byte, plus the four members only.

Usage (worktree root): python .runtime/holdings-journey-20260923/prepare_classified_candidate.py <49financial|inflection|cottonwood>

1. Reads the served index -> accepted row -> manifest -> header -> every partition through the reader library.
2. Reassembles the full document (header + every part's nodes in part order) and ASSERTS its digest equals the
   served revision, so the base is the served bytes, never a rebuild from sources.
3. annotate_classification() adds asset_class / sub_asset_class / asset_class_basis (SECURITY) and model_code
   (MODEL_LEAF); ASSERTS every node differs from the served one ONLY by those members.
4. validate_snapshot() against the contract in this worktree (which must admit the members).
5. Writes, beside a summary: the candidate body, its gold rebuilt by holdings_snapshot.gold_parquet_bytes (after the
   same function reproduces the SERVED gold byte-for-byte), and the served manifest's source_objects receipts --
   the exact inputs a CAS publication takes. Zero S3 writes.
"""
import copy
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path('lib').resolve()))
sys.path.insert(0, str(Path('infra/aws/lambda/investor-reporting/holdings').resolve()))
sys.path.insert(0, str(Path('data/assets/scripts/gold/investor_reporting').resolve()))
import boto3  # noqa: E402
import holdings_snapshot as hs  # noqa: E402
from publication import HoldingsPublication, canonical_bytes, digest, _platinum_plan, MAX_JSON_BYTES  # noqa: E402

firm = sys.argv[1]
tag = {'49financial': '49f', 'inflection': 'inf', 'cottonwood': 'cot'}[firm]
root = Path('.runtime/holdings-journey-20260923/prepared_%s_classified' % tag)
root.mkdir(exist_ok=True)
s3 = boto3.client('s3', region_name='us-east-1')
store = HoldingsPublication(s3, firm)

observed = store.begin()
index = observed['document']
date = index['latest_date']
row = index['dates'][date]
served_rev, part = row['revision'], 'date=' + date
manifest = json.loads(store.read_exact(row['manifest'], expected_location=store.location(
    'platinum', part, served_rev + '.manifest.json'), max_bytes=MAX_JSON_BYTES))
if 'partitions' in manifest:
    header = json.loads(store.read_exact(manifest['platinum_header'], expected_location=store.location(
        'platinum', part, served_rev + '.header.json'), max_bytes=MAX_JSON_BYTES))
    nodes = []
    for i, p in enumerate(manifest['partitions']):
        body = store.read_exact(p['object'], expected_location=store.location(
            'platinum', part, served_rev + '.part%05d.json' % i), max_bytes=MAX_JSON_BYTES)
        nodes.extend(json.loads(body)['nodes'])
    served = dict(header)
    served['nodes'] = nodes
else:
    served = json.loads(store.read_exact(manifest['platinum'], expected_location=store.location(
        'platinum', part, served_rev + '.json'), max_bytes=MAX_JSON_BYTES))
base_proof = 'reassembled from the served parts'
if digest(canonical_bytes(served)) != served_rev:
    # The publisher groups parts by account in SORTED order (publication._platinum_plan), so a body whose
    # nodes were not in that order cannot be reassembled from its parts. A LOCAL body is accepted only if
    # it digests to the served revision AND its own partition plan reproduces the served header and every
    # served part byte-for-byte -- then it IS the served document.
    if len(sys.argv) < 4 or sys.argv[2] != '--base-body':
        raise SystemExit('REFUSED: reassembly does not digest to %s; pass --base-body <prepared body>' % served_rev)
    local = json.loads(Path(sys.argv[3]).read_bytes())
    if digest(canonical_bytes(local)) != served_rev:
        raise SystemExit('REFUSED: --base-body does not digest to the served revision')
    header_body, plan_parts = _platinum_plan(local, served_rev)
    if digest(header_body) != manifest['platinum_header'].get('sha256'):
        raise SystemExit('REFUSED: --base-body header differs from the served header')
    if len(plan_parts) != len(manifest['partitions']) or any(
            digest(body) != p['object'].get('sha256') or sorted(members) != sorted(p['account_ids'])
            for (members, body), p in zip(plan_parts, manifest['partitions'])):
        raise SystemExit('REFUSED: --base-body parts differ from the served parts')
    served = local
    base_proof = ('local body digesting to the served revision; its partition plan reproduces the served '
                  'header and %d of %d parts byte-for-byte' % (len(plan_parts), len(manifest['partitions'])))

candidate = copy.deepcopy(served)
if not hs.classification_admitted():
    raise SystemExit('REFUSED: the contract in this worktree does not admit the classification members')
census = hs.annotate_classification(candidate['nodes'])
added = set(hs.CLASSIFICATION_MEMBERS)
for before, after in zip(served['nodes'], candidate['nodes']):
    extra = set(after) - set(before)
    if not extra <= added or {k: v for k, v in after.items() if k not in added} != before:
        raise SystemExit('REFUSED: node %s changed beyond the four members' % before.get('node_id'))
ok, errors = hs.validate_snapshot(candidate)
if not ok:
    raise SystemExit('REFUSED: candidate fails the contract: %s' % errors[:5])
new_rev = digest(canonical_bytes(candidate))
served_gold = store.read_exact(manifest['gold'], expected_location=store.location('gold', part, served_rev + '.parquet'),
                               max_bytes=512 * 1024 * 1024)
# POSITIVE CONTROL: the ONE gold definition rebuilds the SERVED gold byte-for-byte from the served nodes.
if digest(hs.gold_parquet_bytes(served['nodes'])) != digest(served_gold):
    raise SystemExit('REFUSED: gold_parquet_bytes does not reproduce the served gold -- the tier would drift')
gold = hs.gold_parquet_bytes(candidate['nodes'])
raw = canonical_bytes(candidate)
plan = _platinum_plan(candidate, new_rev) if len(raw) > MAX_JSON_BYTES else None
parts = len(plan[1]) if plan else 0
(root / 'candidate.json').write_bytes(raw)
(root / 'gold.parquet').write_bytes(gold)
(root / 'source_receipts.json').write_text(json.dumps(manifest.get('source_objects'), indent=1))
summary = {
    'status': 'PREPARED_UNPUBLISHED', 'firm_id': firm, 'prepared_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
    'base': {'served_revision': served_rev, 'business_date': date, 'index_version': observed['reference'].get('version_id'),
             'index_etag': observed['reference'].get('etag'), 'base_proof': base_proof},
    'candidate_revision': new_rev, 'nodes': len(candidate['nodes']),
    'change': 'the served tree to the byte plus asset_class / sub_asset_class / asset_class_basis (SECURITY) and '
              'model_code (MODEL_LEAF); every other member of every node byte-equal to the served one',
    'classification_census': census, 'schema_valid': ok,
    'gold': {'rebuilt_by': 'holdings_snapshot.gold_parquet_bytes', 'sha256': digest(gold),
             'positive_control': 'the same function reproduces the served gold %s byte-for-byte' % digest(served_gold)},
    'measured_write_plan': {'multipart': plan is not None, 'parts': parts,
                            'immutable_creates': (2 + parts + 1) if plan else 3, 'index_writes': 1},
}
(root / 'candidate_summary.json').write_text(json.dumps(summary, indent=1, default=str))
print(json.dumps(summary, indent=1, default=str))
