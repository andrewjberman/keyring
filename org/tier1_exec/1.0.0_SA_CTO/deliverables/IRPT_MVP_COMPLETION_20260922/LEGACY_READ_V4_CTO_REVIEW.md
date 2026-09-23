# CTO legacy-read v4 final review

Candidate: `6cae3d21a3304dc05209e55eb0ad0b45b871129c`. Gate SHA256: `4b0dd5ca6cfe533f4751baec3af3a8753286377e11623d48d802336508312448`. Reviewer: `1.0.0_SA_CTO`. Authority: LEGACY-READ-01/02/03 and v3 disposition `6acd352b90`.

**Disposition: NOT READY for mechanism integration or carrier activation.** The clean commit has MSTR as author and excludes the fixture carrier. Its successful canonical commit is reported by MSTR; CTO independently read its commit metadata/path summary and the relevant shipped gate source. The old candidate history remains excluded. A newly exercised source defect prevents extending G's earlier bounded verdict to activation.

## Pattern captures are bindings

The shipped `_binds_of` omits structural pattern bindings. A Python `ast.MatchAs` or `ast.MatchStar` binds its string `name`; `ast.MatchMapping` can bind its string `rest`. These are syntactic declarations, not the previously accepted limitation concerning dynamic `globals()` rebinding.

On the exact approved post-image reconstructed using the original `candidate.diff`, the unmodified baseline returns ALLOW. Each of these separate insertions immediately after the unique `bucket = "opal-data-inf"` inside `build_inf` also returns ALLOW, incorrectly:

```python
    match "unapproved-bucket":
        case bucket:
            pass
```

```python
    match unapproved_helper:
        case _latest_date_partition:
            pass
```

```python
    match {"arbitrary": "value"}:
        case {**bucket}:
            pass
```

The first can replace the approved bucket; the second can replace the reviewed helper with an arbitrary callable. The third demonstrates another uncounted binding form. Source text was parsed only and never executed. This is a pure recognizer reproduction, not a claimed successful canonical commit bypass or runtime read/write.

Repair by conservatively recognizing/refusing the relevant pattern bindings, including `MatchStar`, or refusing unsupported structural pattern syntax for this bounded case. Preserve the legitimate approved source and unchanged prior negative controls. Do not broaden into general dataflow analysis or estate-wide authority hardening. MSTR owns the fresh canonical repair; G independently reruns the new negatives on its exact pin.

## Retained positive results and authority preparation

CTO independently reran the original LR-01 helper-assignment, bucket-for-loop and duplicate-helper tests: all now REFUSE, with the legitimate baseline still ALLOW. Both malformed-duplicate orders yield zero usable entries. Injected UTC expiry is false at `2026-09-23T23:59:59Z`, true at `2026-09-24T00:00:00Z` and true one second later. The carrier's full pinned ruling resolves. Loader controls simulated only the committed-HEAD carrier response in memory; no carrier was written or staged. [Exact results](LEGACY_READ_V4_CTO_PROBES.json).

CTO read the original authorized source diff and the carrier specimen. The case is still exactly `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, `silver/api_dims/accounts_v2/`, direct positional argument 2 to `_latest_date_partition` inside `build_inf`, with `bucket = "opal-data-inf"`, one occurrence, remediation ADVI_FIRMBKTS and the original expiry. The helper lists partition prefixes and filters valid dates at or before the requested cutoff; no source migration is authorized.

Independently measured approved helper normalized-source SHA256: `e9c932d9af7eefa45a866cafea80da29a464f35bf4bb02a3888764e24e6e1a78`, matching the specimen. Helper normalized AST SHA256: `158c11ac7c272b3a3ef64720b85652d9449b1ddcc4f9e655d79306480243b1b4`, computed as UTF-8 `ast.dump(node, annotate_fields=True, include_attributes=False)`. This records the AST identity required by LEGACY-READ-03. The gate's additional normalized-source comparison is retained; this report does not claim the implementation itself computes an AST hash. Any final authority entry must bind to this reviewed case and record, not treat producer hash values as self-authorization.

The original diff SHA256 is `00805e11892da975f1953ad6854016ad9ad4fd3806f9dfafb63e699f78c9dcc6`, applied to source at `62139c3a1a9792b41e02a8b66b612ad4571c6ab8`. The [earlier CTO reproduction](LEGACY_READ_REVIEW_EC40.md) describes the reconstruction; the three mutations above use that same post-image and the v4 gate. No production authority entry, mechanism merge, M cutoff unblock or live action occurred.
