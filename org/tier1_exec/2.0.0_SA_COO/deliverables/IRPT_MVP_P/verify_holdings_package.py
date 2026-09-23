"""Offline declared-package proof; no builder upload, AWS call or deployed claim."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

MAP = "infra/aws/lambda/ci/lambda-source-map.json"
NAME = "irpt-holdings"
PROBE = r'''
import io, json, pathlib, sys, socket, subprocess, copy
from types import SimpleNamespace
def no_network(*a, **kw): raise AssertionError('network forbidden')
socket.create_connection = no_network
socket.socket.connect = no_network
flat = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(flat))
import entry, snapshot, publication, served, enforce, resolve, loaders, ids, keys, selection, selection_store, prospect, opal_naming
import lib.opal_naming as canonical_naming
for module in [entry, snapshot, publication, served, enforce, resolve, loaders, ids, keys, selection, selection_store, prospect, opal_naming, canonical_naming]:
    assert pathlib.Path(module.__file__).resolve().is_relative_to(flat), module.__file__
assert opal_naming.address is canonical_naming.address
assert pathlib.Path(canonical_naming.REPO).resolve() == flat
firm = '49financial'
doc = json.loads(pathlib.Path(sys.argv[2]).read_text())
doc['scope']['firm_id'] = firm
opaque = ids.opaque_firm(firm)
accounts = doc['scope']['account_ids']
directory = {'firm_id_opaque': opaque, 'as_of_business_date': '2026-09-22',
             'entries': [{'ids': {'firm_id': opaque, 'account_ids': accounts}}]}
ownership = {'schema_version': 1, 'advisors': {'advisor': {'accounts': list(accounts), 'relationships': []}}}
entry.ENTRY.deps = lambda tenant: loaders.fixture_deps(directory, ownership)
entry.ENTRY.opaque_firm_for = lambda tenant: opaque
headers = {'x-contract-version': 'v1', 'x-origin-verify': 'cloudfront', 'x-firm-id': firm,
           'x-user-email': 'test@example.invalid', 'x-user-role': 'advisor', 'x-advisor-id': 'advisor'}
rows = {}
selection_store.configured_store = lambda: SimpleNamespace(load=lambda firm, ref: rows.get((firm, ref)))
guard, ctx = entry.ENTRY.enforcer_for(firm)
scope, refusal = guard.resolve_now(enforce.Request(headers, 'holdings_snapshot'))
assert refusal is None
selected = selection.create_selection(scope, directory, [accounts[0]],
    directory_revision=selection.directory_revision(directory),
    save_selection=lambda firm, ref, record: rows.update({(firm, ref): record}))
event = {'headers': headers, 'routeKey': entry.ROUTE_KEY,
         'pathParameters': {'accountSetId': selected['account_set_id']}}
class Storage:
    def __init__(self): self.rows={}; self.calls=[]; self.corrupt=False; self.revoke=False
    def add(self, location, body):
        self.rows[location]=body
        return {'bucket':location[0], 'key':location[1], 'version_id':'version-1',
                'sha256':publication.digest(body),'byte_length':len(body)}
    def get_object(self, **kw):
        self.calls.append(kw)
        body=self.rows[(kw['Bucket'],kw['Key'])]
        if self.corrupt and kw['Key'].endswith('.manifest.json'): body+=b'corrupt'
        if self.revoke: ownership['advisors']['advisor']['accounts']=[]
        return {'Body':io.BytesIO(body),'VersionId':'version-1','ETag':'index-identity'}
s3=Storage(); store=publication.HoldingsPublication(s3,firm)
date=doc['clocks']['custody_as_of']; body=publication.canonical_bytes(doc); revision=publication.digest(body)
platinum=s3.add(store.location('platinum','date='+date,revision+'.json'),body)
manifest={'schema_version':'irpt-holdings-manifest-v1','firm_id':firm,'business_date':date,
          'revision':revision,'platinum':platinum,
          'gold':s3.add(store.location('gold','date='+date,revision+'.parquet'),b'offline-gold-fixture'),
          'source_set_revision':doc['source_set_revision'],'clocks':doc['clocks']}
manifest_ref=s3.add(store.location('platinum','date='+date,revision+'.manifest.json'),publication.canonical_bytes(manifest))
s3.add(store.location('platinum','current','manifest.json'),publication.canonical_bytes({
    'schema_version':'irpt-holdings-index-v1','firm_id':firm,'latest_date':date,
    'dates':{date:{'revision':revision,'manifest':manifest_ref}}}))
real_load=snapshot.load_snapshot
snapshot.load_snapshot=lambda *args, **kwargs: real_load(*args,s3_client=s3,**kwargs)
answer=entry.lambda_handler(event)
assert answer['data']['scope']['account_ids']==[accounts[0]], answer
assert '_accepted_publication' not in answer['data']
assert len(s3.calls)==3 and 'VersionId' not in s3.calls[0]
assert all(row['VersionId']=='version-1' for row in s3.calls[1:])
# The same declared package reads a complete v2 inventory while fetching only
# the retained selection's account parts. These remain synthetic accepted bytes.
header = {key:value for key,value in doc.items() if key != 'nodes'}
manifest.pop('platinum')
manifest['schema_version']='irpt-holdings-manifest-v2'
manifest['platinum_header']=s3.add(store.location('platinum','date='+date,revision+'.header.json'),
                                  publication.canonical_bytes(header))
manifest['partitions']=[]
for number,(account,nodes) in enumerate(sorted(publication._account_groups(doc['nodes']).items())):
    ref=s3.add(store.location('platinum','date='+date,revision+'.part%05d.json'%number),
               publication.canonical_bytes({'firm_id':firm,'revision':revision,'nodes':nodes}))
    manifest['partitions'].append({'account_ids':[account],'object':ref})
manifest_ref=s3.add(store.location('platinum','date='+date,revision+'.manifest.json'),publication.canonical_bytes(manifest))
s3.add(store.location('platinum','current','manifest.json'),publication.canonical_bytes({
    'schema_version':'irpt-holdings-index-v1','firm_id':firm,'latest_date':date,
    'dates':{date:{'revision':revision,'manifest':manifest_ref}}}))
s3.calls=[]
answer=entry.lambda_handler(event)
assert answer['data']['scope']['account_ids']==[accounts[0]], answer
assert len(s3.calls)==4 and all(row['VersionId']=='version-1' for row in s3.calls[1:])
unselected={part['object']['key'] for part in manifest['partitions'] if accounts[0] not in part['account_ids']}
assert unselected and not unselected.intersection(row['Key'] for row in s3.calls)
# M-PART-01: repin malformed inventory so hash drift cannot explain refusal.
valid_manifest=copy.deepcopy(manifest)
def repin(candidate):
    ref=s3.add(store.location('platinum','date='+date,revision+'.manifest.json'),publication.canonical_bytes(candidate))
    s3.add(store.location('platinum','current','manifest.json'),publication.canonical_bytes({
        'schema_version':'irpt-holdings-index-v1','firm_id':firm,'latest_date':date,
        'dates':{date:{'revision':revision,'manifest':ref}}}))
negative_count=0
for mutation in ('missing','null','foreign_bucket','foreign_key','missing_version','bad_hash','bad_length'):
    candidate=copy.deepcopy(valid_manifest)
    part=next(p for p in candidate['partitions'] if accounts[0] not in p['account_ids'])
    if mutation=='missing': part.pop('object')
    elif mutation=='null': part['object']=None
    else:
        field,value={'foreign_bucket':('bucket','other-tenant'),'foreign_key':('key','wrong'),
            'missing_version':('version_id',None),'bad_hash':('sha256','bad'),
            'bad_length':('byte_length',0)}[mutation]
        part['object'][field]=value
    repin(candidate);s3.calls=[]
    answer=entry.lambda_handler(event)
    assert answer.get('ok') is False and 'data' not in answer,(mutation,answer)
    assert not unselected.intersection(row['Key'] for row in s3.calls)
    assert not any(row['Key'].endswith('.parquet') for row in s3.calls)
    negative_count+=1
for gold in (None,{},dict(valid_manifest['gold'],bucket='other-tenant')):
    candidate=copy.deepcopy(valid_manifest);candidate['gold']=gold
    repin(candidate);s3.calls=[]
    answer=entry.lambda_handler(event)
    assert answer.get('ok') is False and 'data' not in answer,answer
    assert not any(row['Key'].endswith('.parquet') for row in s3.calls)
    negative_count+=1
repin(valid_manifest)
# Valid metadata does not require unselected physical objects to be fetched.
unselected_ref=next(p['object'] for p in valid_manifest['partitions'] if accounts[0] not in p['account_ids'])
unselected_location=(unselected_ref['bucket'],unselected_ref['key'])
unselected_body=s3.rows.pop(unselected_location);s3.calls=[]
answer=entry.lambda_handler(event)
assert answer['data']['scope']['account_ids']==[accounts[0]],answer
assert not unselected.intersection(row['Key'] for row in s3.calls)
s3.rows[unselected_location]=unselected_body
selected_part=next(part['object'] for part in manifest['partitions'] if accounts[0] in part['account_ids'])
location=(selected_part['bucket'],selected_part['key']); saved=s3.rows.pop(location)
answer=entry.lambda_handler(event)
assert answer.get('ok') is False and 'data' not in answer, answer
s3.rows[location]=saved
limit=publication.MAX_SELECTED_PART_READS; publication.MAX_SELECTED_PART_READS=0
answer=entry.lambda_handler(event)
assert answer.get('ok') is False and 'data' not in answer, answer
publication.MAX_SELECTED_PART_READS=limit
s3.corrupt=True
answer=entry.lambda_handler(event)
assert answer.get('ok') is False and 'data' not in answer, answer
s3.corrupt=False; s3.revoke=True
answer=entry.lambda_handler(event)
assert answer.get('ok') is False and 'data' not in answer, answer
assert 'pyarrow' not in sys.modules
locations={f:publication.HoldingsPublication(s3,f).location('platinum','current','manifest.json')
           for f in ('49financial','cottonwood','inflection')}
registry=flat/'infra/logic/registry/scopes.json'
registry.rename(registry.with_suffix('.missing'))
missing = subprocess.run([sys.executable, '-I', '-c',
    'import sys;sys.path.insert(0,sys.argv[1]);import publication;publication.HoldingsPublication(object(),sys.argv[2])',
    str(flat), firm], cwd=flat, capture_output=True, text=True)
assert missing.returncode != 0 and 'scopes.json' in missing.stderr, missing.stderr
print(json.dumps({'guarded_selected_read':True,'versioned_reads':True,'corrupt_refusal':True,
    'release_revocation_refusal':True,'missing_registry_refusal':True,'canonical_locations':locations,
    'v2_selected_parts_only':True,'missing_selected_part_refusal':True,
    'selected_request_limit_refusal':True,'complete_inventory_negative_cases':negative_count,
    'unselected_physical_blob_not_required':True,'reader_imports_pyarrow':False,'network':False}))
'''


def blob(root, ref, path):
    return subprocess.check_output(["git", "show", ref + ":" + path], cwd=root)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--before-ref", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path.cwd()
    before = json.loads(blob(root, args.before_ref, MAP))
    after = json.loads((root / MAP).read_text(encoding="utf-8"))
    changed = [name for name in before["functions"] if before["functions"][name] != after["functions"].get(name)]
    assert changed == [NAME] and set(before["functions"]) == set(after["functions"])
    assert {k: v for k, v in before.items() if k != "functions"} == {k: v for k, v in after.items() if k != "functions"}
    old, item = before["functions"][NAME], after["functions"][NAME]
    for field in set(old) | set(item):
        if field not in {"files", "staged_from", "_staged_from_note", "_build_note"}:
            assert old.get(field) == item.get(field), field
    evidence = {"before_ref": args.before_ref, "changed_consumers": changed,
                "other_functions_equal": len(before["functions"]) - 1,
                "deployment_metadata_unchanged": True, "members": {},
                "member_diff": {k: {"before": old.get(k), "after": item.get(k)} for k in set(old) | set(item) if old.get(k) != item.get(k)}}
    staged = {row["packaged_as"]: row for row in item["staged_from"]}
    assert len(staged) == len(item["staged_from"]) and len(set(item["files"])) == len(item["files"])
    with tempfile.TemporaryDirectory(prefix="irpt-holdings-flat-") as scratch:
        flat = Path(scratch)
        for member in item["files"]:
            row = staged.get(member)
            data = blob(root, row["pin"], row["repo_path"]) if row else blob(root, args.before_ref, item["source_dir"] + "/" + member)
            sha = hashlib.sha256(data).hexdigest()
            if row:
                assert sha == row["sha256"]
            target = (flat / member).resolve()
            assert target.is_relative_to(flat.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            evidence["members"][member] = sha
        fixture = Path(__file__).with_name("holdings_package_fixture.json")
        evidence["fixture_sha256"] = hashlib.sha256(fixture.read_bytes()).hexdigest()
        environment = {k: v for k, v in os.environ.items() if not k.startswith("IRPT_") and k != "PYTHONPATH"}
        environment["AWS_EC2_METADATA_DISABLED"] = "true"
        commands = [[sys.executable, str(root / "infra/aws/lambda/ci/import-closure-check.py"), str(flat), *item["files"]],
                    [sys.executable, "-I", "-c", PROBE, str(flat), str(fixture.resolve())]]
        evidence["runs"] = []
        for command in commands:
            run = subprocess.run(command, cwd=flat, env=environment, capture_output=True,
                                 text=True, encoding="utf-8", errors="replace", timeout=60)
            evidence["runs"].append({"exit_code": run.returncode, "stdout": run.stdout, "stderr": run.stderr})
            if run.returncode:
                print(run.stdout + run.stderr)
                return run.returncode
    evidence["limits"] = "Offline declared files and synthetic accepted S3 documents; installed local third-party packages. No Gold writer proof, Lambda layer qualification, deployed IAM, live custody, provisioning or deployment."
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"members": len(evidence["members"]), "runs": evidence["runs"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
