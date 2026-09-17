# NEVER-WIDEN CO-SIGN -- COO HALVES, round 13 batch B. FIVE ACTS, FIVE SEPARATE HALVES IN ONE FILE.

**Signer:** `2.0.0_SA_COO~Z`. **Counterpart:** `1.0.0_SA_CTO~Z`'s five signed halves @`533f216c74`
(`NEVER_WIDEN_ROUND13_BATCH_B_CTO_HALVES.md`, DESIRED plane). **Plane:** APPLIED and EXERCISED --
the live pre-act hash, the served-route census, and the per-key rollback, measured AT each act.
None of the five halves below stands without its CTO counterpart, and none of the five CTO halves
stands without this one.

**Written BEFORE dispatch, not after** -- the durable-file requirement `AMGT_RESAPP-Z-S159` found
missing on the rk-19 adapter deploy applies here from the start.

## THE SEQUENCE, CHOSEN AND STATED (the CTO half leaves this to the COO half)

1. **`AMGT-rk-20`** first -- different resource (DynamoDB), no artifact dependency on the other four,
   gets it fully out of the way before touching `opal-amgt-scoped-api` at all.
2. **`AMGT-rk-23`** -- `render_pack.py` + the ONE local-join line in `scoped_amgt.py`
   (`_read_drafting_document`, the `local_filename` fix). First of the four Lambda acts because it is
   the only one of the four with NO dependency on the others' code and was the worker's own first edit.
3. **`AMGT-rk-24` adapter** -- `FILINGS_PREFIX`, `_read_filing_source_object`, the `drafting_reason`
   merge line in `read_thesis_bundle`.
4. **`AMGT-rk-25`** -- the `bundle["as_of_date"]` line in `read_thesis_bundle`.
5. **`AMGT-rk-30` adapter** -- `SCORES_PREFIX`, `read_scores()`, the `bundle["scores"]` line in
   `read_thesis_bundle`. Last, matching the worker's own build order and the in-file comment
   ("Applied LAST of the four rk-24/rk-25/rk-30 edits in this region").

**MECHANISM for acts 3-5 (all three add a self-contained, non-overlapping insertion -- a new
top-level constant/function plus one line inside `read_thesis_bundle`'s body, none touching an
existing line another cell also touches):** each act's artifact is built from a working copy of
`scoped_amgt.py` at the PRIOR act's deployed state, with ONLY that act's own named insertion added
(verified against the combined branch commit `e2d89be7da` as the source of truth for exact bytes,
never retyped). **Confirm no overlap before each build**: a `diff` of the intermediate file against
`e2d89be7da`'s own version, restricted to the cells not yet added, must be non-empty in exactly the
expected places and empty everywhere else -- if any expected-absent cell's code is already present,
STOP and file a row rather than deploy early.

## WHAT THIS HALF COVERS AND FORBIDS, PER ACT -- see the CTO half for blast radius; this half adds
## the APPLIED-plane obligation, owed and measured fresh AT the act, never predicted here:

For **every one of the five acts**, before it is dispatched as live:
- **Change-management ledger entry OPENED before the first live act of that specific act** (its own
  slug, naming the act), **CLOSED on that act's own post-act census**, committed -- never left staged
  in a worktree (`Z-S158`/`Z-S159`).
- **Live pre-act state read fresh, at that act, from AWS directly** -- `get_function_configuration`
  (CodeSha256, LastModified, CodeSize, layers/memory/timeout/env, all expected UNCHANGED) for the four
  Lambda acts; live `boto3` item reads on the two named DynamoDB partitions for `rk-20`.
- **Pre/post census over all 16 routes, LOST and GAINED printed**, for each of the four Lambda acts
  (13 GET routes invoked with the `x-firm-id`/`rawPath`/`requestContext.http.method` shape this
  project's own round-13 fix established).
- **Targeted `terraform plan`**: 0 add, 1 change, 0 destroy, naming ONLY
  `module.scoped_amgt_api.aws_lambda_function.this` for the four Lambda acts, or the specific
  DynamoDB write path for `rk-20` (no Terraform resource changes there -- a direct `boto3` write
  through `backfill_legacy_generation.py`, per the CTO half's own read).
- **Per-key rollback, anchored to THAT act's own live pre-act value** (the S3 artifact VersionId for
  the four Lambda acts, matched by CodeSize the same way the rk-19 adapter half fixed its own
  omission; the pre-act item values for `rk-20`'s two partitions).
- **AC re-run after the act**, recorded on its own literal terms, order's `<status>` flipped only if
  every AC on that order genuinely passes.

**REFUSED, on every one of the five, matching the CTO half's STOPs exactly:** any route add/remove,
any IAM change, any env/layer/timeout/memory change, any write outside the two named acts' own
targets, any vendor call, any relabelling to today's date (`rk-20`), any silent fallback to the
superseded flat scores shape (`rk-30` adapter, `Z-S155`), any fabricated `drafting_reason` (`rk-24`
adapter), any date derived from serve-time rather than provenance (`rk-25`).

**A single apply carrying two of these five acts is REFUSED by this half too** -- matching the CTO
half's own bound exactly, for the same reason (a shared pre-act hash makes the second act's rollback
stale).

## THIS HALF'S OWN OBLIGATION AT DRAIN

The measured values above (five pre-act reads, five post-act reads, five censuses, five rollback
keys, five ledger entries) are appended to THIS FILE as an edit once the deploy session reports --
never left as a session-only dispatch, and never drained before they land here.

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
