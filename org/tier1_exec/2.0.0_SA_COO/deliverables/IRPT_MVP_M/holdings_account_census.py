"""Goal criterion (2) census: every ACTIVE directory account at 49F and INF against the SERVED holdings publication.

Read-only. Operator S3 reads through the holdings reader library (HoldingsPublication: index -> accepted row ->
manifest -> header -> every partition, each read by exact version/sha). Classifies each directory account by the
reader's OWN membership rule (publication.py _load_parts: an account outside the partition census raises
PublicationRefused "selected accounts absent from accepted publication"), then runs the library's load() on a sample
of every class as the control. Writes nothing to S3.

Usage (from the worktree root): python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/holdings_account_census.py --out <json>
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
sys.path.insert(0, str(ROOT / 'lib'))
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/investor-reporting/holdings'))
import boto3  # noqa: E402
from publication import HoldingsPublication, PublicationRefused, MAX_JSON_BYTES, _account_groups  # noqa: E402

FIRMS = ('49financial', 'inflection')
SAMPLE = 3


def directory(s3, bucket, prefix):
    pointer = json.loads(s3.get_object(Bucket=bucket, Key=prefix + '/latest.json')['Body'].read())
    obj = s3.get_object(Bucket=bucket, Key=pointer['key'])
    doc = json.loads(obj['Body'].read())
    return doc, {'bucket': bucket, 'key': pointer['key'], 'version_id': obj.get('VersionId'),
                 'directory_revision': doc.get('directory_revision'),
                 'as_of_business_date': doc.get('as_of_business_date')}


def served(store):
    observed = store.begin()
    index = observed['document']
    date = index['latest_date']
    row = index['dates'][date]
    revision, partition = row['revision'], 'date=' + date
    manifest = json.loads(store.read_exact(row['manifest'], expected_location=store.location(
        'platinum', partition, revision + '.manifest.json'), max_bytes=MAX_JSON_BYTES))
    groups = {}
    for number, part in enumerate(manifest['partitions']):
        body = store.read_exact(part['object'], expected_location=store.location(
            'platinum', partition, revision + '.part%05d.json' % number), max_bytes=MAX_JSON_BYTES)
        piece = json.loads(body)
        g = _account_groups(piece['nodes'])
        if set(g) != set(part['account_ids']):
            raise SystemExit('ERROR: partition %d census differs' % number)
        groups.update(g)
    ref = {'index_version': observed['reference'].get('version_id'), 'business_date': date,
           'revision': revision, 'partitions': len(manifest['partitions'])}
    return groups, ref


def classify(nodes):
    kinds = Counter(n['node_kind'] for n in nodes)
    account = [n for n in nodes if n['node_kind'] == 'ACCOUNT']
    value = round(sum(n['amount']['value'] for n in account), 2) if account else None
    below = len(nodes) - len(account)
    if not account or below == 0:
        return 'RESOLVED_EMPTY', kinds, value
    if kinds.get('MODEL_LEAF', 0) or kinds.get('MODEL_WRAPPER', 0):
        return 'RESOLVED_WITH_MODEL', kinds, value
    return 'RESOLVED_NO_MODEL_CLIENT_ONLY', kinds, value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    s3 = boto3.client('s3', region_name='us-east-1')
    env = boto3.client('lambda', region_name='us-east-1').get_function_configuration(
        FunctionName='irpt-directory-search')['Environment']['Variables']
    bucket_map = json.loads(env['IRPT_DIRECTORY_BUCKET_MAP'])
    prefix = env.get('IRPT_DIRECTORY_PREFIX', 'investor-reporting/directory')
    report = {'measured_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
              'mode': 'READ_ONLY_OPERATOR_S3_LIBRARY_UNDER_USER',
              'source_pin': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
              'rule': 'publication.py _load_parts: selected <= partition census, else PublicationRefused', 'firms': {}}
    for firm in FIRMS:
        doc, dref = directory(s3, bucket_map[firm], prefix)
        by_state = Counter()
        active = {}
        for e in doc['entries']:
            state = (e.get('termination') or {}).get('indicator', 'ABSENT')
            for a in e['ids']['account_ids']:
                by_state[state] += 1
                if state == 'ACTIVE':
                    active.setdefault(a, e['permitted_scope']['scope_kind'])
        store = HoldingsPublication(s3, firm)
        groups, pref = served(store)
        classes, kinds_by_class, value_by_class = Counter(), {}, Counter()
        members_by_class = {}
        for a in sorted(active):
            if a not in groups:
                cls, kinds, value = 'REFUSED_ABSENT_FROM_PUBLICATION', Counter(), None
            else:
                cls, kinds, value = classify(groups[a])
            classes[cls] += 1
            kinds_by_class.setdefault(cls, Counter()).update(kinds)
            if value is not None:
                value_by_class[cls] += value
            members_by_class.setdefault(cls, []).append(a)
        unselectable = sorted(set(groups) - set(active))
        control = []
        for cls, members in sorted(members_by_class.items()):
            for a in members[:SAMPLE]:
                try:
                    loaded, mf = store.load(account_ids={a})
                    got = {n['node_id'] for n in loaded['nodes'] if n['node_kind'] == 'ACCOUNT'}
                    control.append({'class': cls, 'status': 'READ_OK', 'revision': mf['revision'],
                                    'account_node_matches': got == {a}, 'nodes': len(loaded['nodes'])})
                except PublicationRefused as exc:
                    control.append({'class': cls, 'status': 'REFUSED', 'reason': str(exc)})
        report['firms'][firm] = {
            'directory': dref, 'directory_account_rows_by_termination': dict(by_state),
            'active_unique_accounts': len(active), 'publication': pref, 'publication_accounts': len(groups),
            'classes': dict(classes), 'node_kinds_by_class': {k: dict(v) for k, v in kinds_by_class.items()},
            'market_value_by_class': {k: round(v, 2) for k, v in value_by_class.items()},
            'published_not_active_in_directory': len(unselectable),
            'published_not_active_in_directory_in_directory_any_state': sum(
                1 for a in unselectable if any(a in e['ids']['account_ids'] for e in doc['entries'])),
            'control_library_loads': control,
        }
        print(firm, json.dumps({k: report['firms'][firm][k] for k in (
            'active_unique_accounts', 'publication_accounts', 'classes', 'published_not_active_in_directory')}), flush=True)
    Path(args.out).write_text(json.dumps(report, indent=1, sort_keys=True) + '\n', encoding='utf-8')
    print('OK: wrote', args.out)


if __name__ == '__main__':
    main()
