"""Offline flat-layout evidence from the declared source-map members.

This is a verification harness, not the canonical deployment builder. It never
uploads, records deployment hashes, or contacts AWS. Python dependencies are the
local interpreter's installed packages, not proof of a deployed Lambda layer.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

MAP = "infra/aws/lambda/ci/lambda-source-map.json"
CONSUMERS = ["irpt-performance-adapter", "irpt-directory-search"]
PROBE = r'''
import json, pathlib, sys, socket
def forbidden_network(*args, **kwargs):
    raise AssertionError('Network is forbidden in offline package proof')
socket.create_connection = forbidden_network
socket.socket.connect = forbidden_network
sys.path.insert(0, sys.argv[1])
import entry, served, enforce, resolve, loaders, ids, keys, selection, selection_store, prospect
for module in [entry, served, enforce, resolve, loaders, ids, keys, selection, selection_store, prospect]:
    assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.argv[1]).resolve())
from types import SimpleNamespace
firm = '49financial'
opaque = ids.opaque_firm(firm)
a, b = [ids.opaque_account(firm, raw) for raw in ['1000000001', '1000000002']]
directory = {'firm_id_opaque': opaque, 'as_of_business_date': '2026-09-22',
             'entries': [{'ids': {'firm_id': opaque, 'account_ids': [a, b]}}]}
ownership = {'schema_version': 1, 'advisors': {'advisor': {'accounts': [a, b], 'relationships': []}}}
entry.ENTRY.deps = lambda tenant: loaders.fixture_deps(directory, ownership)
entry.ENTRY.opaque_firm_for = lambda tenant: opaque
headers = {'x-contract-version': 'v1', 'x-origin-verify': 'cloudfront', 'x-firm-id': firm,
           'x-user-email': 'test@example.invalid', 'x-user-role': 'advisor', 'x-advisor-id': 'advisor'}
rows = {}
def save(firm, reference, record):
    rows[(firm, reference)] = record
selection_store.configured_store = lambda: SimpleNamespace(save=save, load=lambda firm, ref: rows.get((firm, ref)))
if sys.argv[2] == 'irpt-directory-search':
    event = {'headers': headers, 'routeKey': 'POST /api/scoped/investor-reporting/selections',
             'body': json.dumps({'scope_kind': 'ACCOUNT', 'scope_ids': [a]})}
    answer = entry.lambda_handler(event)
    assert answer['data']['selected_account_ids'] == [a], answer
    assert rows[(firm, answer['data']['account_set_id'])]['account_ids'] == [a]
else:
    guard, ctx = entry.ENTRY.enforcer_for(firm)
    scope, refusal = guard.resolve_now(enforce.Request(headers, 'performance_report'))
    assert refusal is None
    selected = selection.create_selection(scope, directory, [a],
        directory_revision=selection.directory_revision(directory), save_selection=save)
    event = {'headers': headers, 'routeKey': next(iter(entry.ROUTES)),
             'pathParameters': {'accountSetId': selected['account_set_id']},
             'queryStringParameters': {'start': '2026-01-01', 'end': '2026-09-22'}}
    calls = []
    def provider(scope, **kwargs):
        assert scope['resolved_scope']['scope_ids'] == [a]
        calls.append(kwargs)
        return {'report': {'lineage': {'source_revision': 'fixture-1'},
                           'dates': {'actual_end': '2026-09-22'}}, 'contract_validated': True}
    entry._handler.run = provider
    answer = entry.lambda_handler(event)
    assert answer['status']['state'] == 'READY', answer
    def revoked(scope, **kwargs):
        result = provider(scope, **kwargs)
        ownership['advisors']['advisor']['accounts'] = [b]
        return result
    entry._handler.run = revoked
    answer = entry.lambda_handler(event)
    assert answer.get('ok') is False and 'data' not in answer, answer
    assert len(calls) == 2
print(json.dumps({'function': sys.argv[2], 'imports_from_flat_package': True,
                  'actual_guarded_entry': True, 'network': False}))
'''


def git_blob(root, ref, path):
    return subprocess.check_output(["git", "show", ref + ":" + path], cwd=root)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--before-ref", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    before = json.loads(git_blob(root, args.before_ref, MAP))
    after = json.loads((root / MAP).read_text(encoding="utf-8"))
    changed = [name for name in before["functions"]
               if before["functions"][name] != after["functions"].get(name)]
    assert sorted(changed) == sorted(CONSUMERS)
    assert set(before["functions"]) == set(after["functions"])
    assert {k: v for k, v in before.items() if k != "functions"} == {
        k: v for k, v in after.items() if k != "functions"}
    evidence = {"before_ref": args.before_ref, "changed_consumers": changed,
                "non_irpt_equality": True, "deployment_metadata_unchanged": True,
                "member_diff": {}, "probes": []}
    for name in CONSUMERS:
        old, item = before["functions"][name], after["functions"][name]
        for field in set(old).union(item) - {"files", "staged_from", "_staged_from_note", "_build_note"}:
            assert old.get(field) == item.get(field), (name, field)
        evidence["member_diff"][name] = {key: {"before": old.get(key), "after": item.get(key)}
                                         for key in set(old).union(item) if old.get(key) != item.get(key)}
        staged = {row["packaged_as"]: row for row in item["staged_from"]}
        assert len(staged) == len(item["staged_from"])
        assert len(set(item["files"])) == len(item["files"])
        with tempfile.TemporaryDirectory(prefix="irpt-flat-proof-") as scratch:
            flat = Path(scratch)
            for member in item["files"]:
                target = (flat / member).resolve()
                assert target.is_relative_to(flat.resolve())
                row = staged.get(member)
                blob = (git_blob(root, row["pin"], row["repo_path"]) if row else
                        git_blob(root, args.before_ref, item["source_dir"] + "/" + member))
                if row:
                    assert hashlib.sha256(blob).hexdigest() == row["sha256"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(blob)
            closure = subprocess.run([sys.executable, str(root / "infra/aws/lambda/ci/import-closure-check.py"),
                                      str(flat), *item["files"]], cwd=flat,
                                     capture_output=True, text=True, encoding="utf-8", errors="replace")
            if closure.returncode:
                raise RuntimeError(name + " canonical closure failed:\n" + closure.stdout + closure.stderr)
            env = {k: v for k, v in os.environ.items()
                   if not k.startswith("IRPT_") and k != "PYTHONPATH"}
            env["AWS_EC2_METADATA_DISABLED"] = "true"
            result = subprocess.run([sys.executable, "-I", "-c", PROBE, str(flat), name],
                                    cwd=flat, env=env, capture_output=True, text=True,
                                    encoding="utf-8", errors="replace")
            if result.returncode:
                raise RuntimeError(name + " flat probe failed:\n" + result.stdout + result.stderr)
            proof = json.loads(result.stdout)
            proof["canonical_import_closure"] = closure.stdout
            evidence["probes"].append(proof)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"changed_consumers": changed, "flat_probes": len(evidence["probes"]),
                      "non_irpt_equality": True, "evidence": str(args.output)}))


if __name__ == "__main__":
    main()
