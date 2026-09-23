# Independent two-consumer package review

Reviewer: `3.0.0_SA_CVO~P`; 2026-09-22T22:05:19.804545Z.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`;
IRPT-P-BUILD-01 grant `a36b72db57d21c2c681e390dcaf236435c00f359`.
Candidate LOCAL `051054cd3e52539ba6461b5359ec24d9431665d2`.
Exact parent/source baseline `63c6b39af6574fda5e4ad6573258e188ddd21569`.

**PASS for the bounded source-map change and offline selection-package checks.**
This discharges the independent member-scope and flat-entry review for these two
candidate consumers. It is not a deployment, layer/runtime compatibility, complete
route census, production authorization, financial report or product E2E PASS.

## Grant and member boundary

The map has216 function objects: nine IRPT and207 non-IRPT. Exactly two changed:
`irpt-directory-search` and `irpt-performance-adapter`. All214 other objects,
including all207 non-IRPT objects, remain semantically equal. Root metadata and
each changed function's non-composition fields remain equal. Allowed changes are
files, staged_from and their two build-note fields; deployed hashes, artifact
versions and deployment timestamps did not advance.

| Consumer | Declared members | Staged members | Added members |
|---|---:|---:|---|
| directory-search | 16 | 14 | selection.py, selection_store.py, prospect.py |
| performance-adapter | 27 | 13 | selection.py, selection_store.py, prospect.py, keys.py |

All27 staged blobs were fetched from their declared pins and matched their exact
SHA256 values. All16 direct members were fetched at the candidate and independently
checked byte-identical to the parent/source baseline used in the supplied harness.
Full per-member source path, pin and hash are retained in `package_probe_0510.json`.
The exact before/after composition is reproducible from the two map pins and also
attached by the producer in `SELECTION_PACKAGE_EVIDENCE.json` at the candidate.

Before map SHA256: `0097db8de5243fe7b72da90a0cae91661c86c11dbee5a2d09827ae216ed1fcf9`.
After map SHA256: `1d744359c4416e4819a7e68af40512fc52aaeefb54e5a40f78bb9e62eb9f3564`.

Consumed grant `24aa2df2841563c989688e9ce7f240a0f37cdb9f` retains the exact CTO
author and subject of a36b72db57. Independently compared .owned-paths.yaml between
those grant pins: identical, git diff exit0. Candidate051054cd3e has the declared
before pin63c6b39af6 as its direct parent. This verifies the pinned branch boundary;
fresh shared-map reconciliation is still required when someone later integrates
into a shared head that has moved. This reviewer neither integrates nor edits it.
The67 permission controls are CTO-reported, not independently rerun here.

## Flat execution and negative controls

All eight process results matched their expected outcomes:

| Process/check | directory-search | performance-adapter |
|---|---|---|
| Exact canonical import-closure checker | PASS,12 Python files | PASS,18 Python files |
| Supplied flat runtime probe independently executed | PASS | PASS, including R-P06 refusal |
| Added isolated actual-entry controls | PASS | PASS |
| Required keys.py omitted from separate test copy | Expected import failure | Expected import failure |

Added producer controls save exactly one selected account, then refuse empty,
unentitled, partly permitted whole-client and extra-field requests without new
saved rows. A synthetic storage failure cannot issue a successful selection.
The producer writes its retained record into a synthetic exchange file; a separate
isolated consumer process resolves that exact record and forwards the selected
account and both query dates. Literal/unknown references and missing dates refuse
before provider. Revocation during provider execution and the subsequent request
both refuse without report data. Removing keys.py yields the expected
ModuleNotFoundError in enforce.py for both independently materialized packages.

Each runtime process uses Python -I and cleared IRPT/PYTHONPATH environment.
Actual entry and common modules resolve from the flat directory, not a repository
sibling. Socket connections are forbidden. Storage/provider and trusted headers
are synthetic; no deployed edge authorization or real vendor data is exercised.
The provider stub deliberately supplies a minimal report and validation flag;
that tests boundary wiring, not report schema or financial correctness.

The canonical checker only covers top-level imports and exempts nested imports.
Its no-BUILD_MANIFEST mode can be advisory on missing third-party dependencies;
exit0 alone is not claimed to be an enforced universal gate. Both intact package
runs returned the explicit OK import-closure result, and the isolated runtime
negative controls independently detected omitted keys. Local Python site packages
remain available and do not prove the deployed Lambda layer. The upload-capable
canonical builder was not run; this is materialization of its declared members.

## Reproduction and remaining acceptance

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/package_probe_0510.py
```

Runner plus `package_entry_cases.py` and raw `package_probe_0510.json` reproduce
the map comparison, staged/direct hashes, exact canonical checker, supplied probes
and independent controls. Exit0 means all expected outcomes including negative
failures were observed. No moving source-map or mutable worktree source is used.

Full P1-P8/S1-S7 remain NOT_EVALUATED. Provider auth/dispatch/group identity,
browser selectors, immutable report/export assembly, deployed package/layers/IAM,
full-route and live paths still need their own evidence. B-P01 entry/selection and
B-P03 wrapper subchecks are not full browser/provider closure. R-P05/Y-P01 and
R-P06 prior bounded closures remain. No test counts are combined across pins.
B render FAIL/NOT PROVEN, W19-S1 ARMED/CTO and S7-03 twelve-family retention and
physical-disposal/provisioning gates remain unchanged.

CVO~M's exact22:00:55Z message reports R1-R3 closed at eeffdc9a5b with review
7fd072ea9c; those remain attributed peer findings, not tested by this package probe.
Its full custody/positions/storage/UI criteria remain NOT_EVALUATED.

Bare comp-which preceded inspection; comp-read on the root-workspace producer
script found no file, so its exact candidate Git blob was read instead. Pinned
git reads established source-map rules, verifier/checker code, directory entry,
selection producer and Terraform environment locations. No external research,
implementation changes, cloud/vendor call, deploy, cleanup or push occurred.
