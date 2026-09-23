# CTO legacy-read candidate review

Date: 2026-09-23 UTC. Candidate `ec40acbf070c7b534969da4e8a9f462c18445c8a`; MSTR message 99614. Authority: CONTRACT.md and IRPT-M-LEGACY-READ-01/02/03 in RULINGS.md. Reviewer: `1.0.0_SA_CTO`.

**Disposition: NOT READY for integration or activation.** MSTR's matched-input baseline reproduction and five unchanged unrelated verdicts resolve the earlier reproduction question as producer evidence. CTO read the complete candidate gate diff and carrier and independently exercised the candidate functions below. G's independent candidate review remains due. Nothing was changed in MSTR's worktree, the shared gate, or the authoritative carrier.

## Independently reproduced failures

- **LR-01, ambiguous bindings accepted.** On the exact reconstructed original candidate post-image, `legacy_read_ok` returns true for the approved baseline and also for each of: a local assignment rebinding `_latest_date_partition` to `unapproved_helper`; a `for bucket in ["unapproved-bucket"]` binding after the approved bucket assignment; and a second module-level `_latest_date_partition` definition. The function locates the first matching FunctionDef and counts only simple Assign/AnnAssign/AugAssign bucket bindings. The actual Python call/name binding can therefore differ while the reviewed helper source hash remains unchanged. These contradict the explicit ambiguous-use, changed-helper and bucket-bound refusal requirements. This is a recognizer-level reproduction, not an executed source read, runtime write or canonical gate/commit bypass claim.
- **LR-02, malformed duplicate does not invalidate the matching good entry.** Simulating a committed carrier containing its original valid entry plus a copy missing `purpose` produces one usable entry and one rejected entry for the same file/literal. The duplicate check sees only entries that already passed validation. A malformed matching authority must not leave an ambiguous valid grant active. This is an isolated loader probe with the HEAD-carrier read simulated; authority pin lookup used the real repository. It is not a production carrier mutation or a canonical self-grant test.

Repair with an explicit conservative binding subset: reject extra, shadowed or ambiguous helper definitions/bindings and bucket bindings, including binding syntax beyond simple assignments. Do not attempt broad Python dataflow inference. Preserve the legitimate reviewed cutoff helper change. Treat malformed/invalid duplicate matching authority as refusal for that key, independent of entry order; malformed carrier structure must fail closed. Return the original positive plus these unchanged negative cases, and the full ordinary gate controls at the replacement pin.

## Required evidence still missing from the handoff

The injected UTC expiry-boundary check was already required in LEGACY-READ-02/03; it is not an optional new request. Exercise immediately before, exactly at and after `2026-09-24T00:00:00Z`. Also provide the runnable harness/results for the existing requested controls, including absent versus empty carrier, staged/unstaged/same-commit attempted grants, mixed read/write or alias ambiguity, baseline self-test regression, and actual canonical staged-source/carrier consumption. The notice's 15-arm list does not establish all of those controls. Report any unexecuted arm explicitly rather than treating it as covered by nearby tests.

The CTO-only exact-file lane and separately committed authority record are not installed yet. CTO owns landing them after candidate review; MSTR may supply the proposed protection diff and test specimen without activating either. Origin reachability of the full authority pin must be measured before any cross-clone activation claim. These prerequisites do not justify bypassing the current source-commit hold.

## Reproduction

Executed using Python in the shared repository. It loads gate code directly from the immutable git object without running its CLI or touching its log. Source text is parsed, never executed. The saved original diff remains at `.runtime/codex-seats/1.0.0_SA_CTO/legacy_read_gate/candidate.diff`, SHA256 `00805e11892da975f1953ad6854016ad9ad4fd3806f9dfafb63e699f78c9dcc6`.

```python
import copy, json, pathlib, subprocess, sys, types
sys.dont_write_bytecode = True
root = pathlib.Path('C:/Users/AndrewBerman/Desktop/ajb_workspace')
pin = 'ec40acbf070c7b534969da4e8a9f462c18445c8a'
def show(rev, path):
    return subprocess.check_output(['git', 'show', rev + ':' + path], cwd=root).decode('utf-8')
g = types.ModuleType('ctolegacyreview')
g.__file__ = str(root / '.tools/naming-gate.py')
sys.modules[g.__name__] = g
exec(compile(show(pin, '.tools/naming-gate.py'), g.__file__, 'exec'), g.__dict__)
doc = json.loads(show(pin, 'org/standards/NAMING_LEGACY_READS.json'))
entry = doc['entries'][0]
path = 'data/assets/scripts/gold/investor_reporting/holdings_snapshot.py'
pre = show('62139c3a1a9792b41e02a8b66b612ad4571c6ab8', path)
diff = (root / '.runtime/codex-seats/1.0.0_SA_CTO/legacy_read_gate/candidate.diff').read_text(encoding='utf-8')
f = next(x for x in g.parse_diff(diff) if x.get('new') == path)
lines, _ = g.apply_hunks(pre, f['hunks'])
post = '\n'.join(lines) + '\n'
needle = '    bucket = "opal-data-inf"'
assert post.count(needle) == 1
cases = {
    'baseline': post,
    'helper_local_rebinding': post.replace(needle, needle + '\n    _latest_date_partition = unapproved_helper', 1),
    'bucket_for_rebinding': post.replace(needle, needle + '\n    for bucket in ["unapproved-bucket"]:\n        pass', 1),
    'duplicate_helper_definition': post + '\ndef _latest_date_partition(*args, **kwargs):\n    return None\n',
}
print(json.dumps({name: g.legacy_read_ok(entry, source) for name, source in cases.items()}))
# Observed: all four returned true. Required: only baseline true.
bad = copy.deepcopy(entry)
del bad['purpose']
doc['entries'].append(bad)
original_git = g.git
def simulated_head_carrier(*args):
    if args == ('show', 'HEAD:' + g.LEGACY_READS_REL):
        return 0, json.dumps(doc).encode(), b''
    return original_git(*args)
g.git = simulated_head_carrier
good, rejected = g.load_legacy_reads()
print({'good_count': len(good), 'rejected_count': len(rejected)})
# Observed: good_count=1, rejected_count=1. Required: no usable matching entry.
```

Actual result files: `.runtime/codex-seats/1.0.0_SA_CTO/legacy_read_gate/candidate_ec40_review.json` and `candidate_ec40_carrier_review.json`. No live access, source mutation, policy activation, deployment or old B/F cycle is part of this review.
