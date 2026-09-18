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

## MEASURED, AT DRAIN -- all five acts landed, worker `0.9.0_WK_AMGT_RESAPP~27`, branch
## `wk-amgt-13-batch-b`, HEAD `c9b3426461`. Independently re-verified this seat, three findings on
## a THIRD instrument (fresh `boto3` reads, not the worker's or CTO's own): the IAM AccessDenied on
## `scores/v1/`, the raw-slash-vs-encoded-slash router behavior, and the served `as_of_date`/
## `thesis_driver_chart` states. Each act deployed ALONE, its own live pre-act hash, no apply
## carrying two acts -- the sequencing bound held on every one, per this seat's own and the CTO's
## independent reads.

1. **`AMGT-rk-20`** (DynamoDB, no Lambda). World effect landed correctly: both
   `BREAKOUT_PRICE#2026-09-15`/`TRENDING_PRICE#2026-09-15` partitions COMPLETE, real `_CURRENT`
   pointers, 32 rows each. AC2 PASS. **AC1 FAILS on its own criterion text**, not the act: the
   order's `<expect>` assumed a stale BEFORE-state (2026-09-10/dated-true) that the live store had
   already moved past (2026-09-17/dated-false) by the time this act ran; the AFTER state
   (dated=true) is the reader's own correct contract response to a request at the DEFAULT date, per
   `scoped_amgt.py:568-574`, independently confirmed by the CTO (row Z-S161). Order stays OPEN;
   no rollback needed (the write itself is correct and durable).
   Commits `9a86023139`, `035373b553`.
2. **`AMGT-rk-23`**. Pre-act `zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=` -> post-act (`iGmDk...`,
   783126 B, 23:33:34Z). Census 13/13 GET pre and post, LOST=[] GAINED=[]. Deployed fix verified
   correct against its own scope (path-safe local join, S3 key kept raw). **AC1 FAILS on a
   genuinely new, out-of-scope router-level finding**: a RAW literal slash in `rawPath` 404s at
   routing (independently reproduced this seat, fresh invoke: raw-slash 404, `%2F`-encoded 200);
   the real page (`amgt-lead-panel.ts:151`, `encodeURIComponent`) never sends the raw form, so the
   deployed fix is confirmed correct for every real client (CTO row Z-S163, 33/33 via the page's
   own shape). Row `AMGT_RESAPP-Z-W27-S10` filed ARMED (a router hardening question, not a client-
   reachable defect) -- stays open pending the CTO's own named instrument (the `rk-26` render
   capture reading the browser network layer, since CloudWatch is silent on the path end to end).
   Order stays OPEN. Commits `6894b0fb42`, `62e79b9778`.
3. **`AMGT-rk-24` adapter**. Pre-act `iGmDk...` -> post-act (`Jicv6u...`, 783851 B, 00:12:01Z).
   Census 13/13. Measured over all 33 covered names (CTO row Z-S165): 21 ABSENT with the stored
   classed no-CIK reason, 12 SERVED, zero generic NoSuchKey strings -- a 1:1 partition against the
   store's own `UNRESOLVED-SOURCE.source.json` objects. **AC1 genuinely PASSES.** `<status>`
   flipped to `complete`. Commits `957da2c226`, `91d91f8587`.
4. **`AMGT-rk-25`**. Pre-act `Jicv6u...` -> post-act (`fkKLVf...`, 00:43:39Z). Census 13/13.
   Verified against values the CTO pinned BEFORE the act on the prior build (row Z-S167): 12 of 12
   filing-dated names now serve `as_of_date` exactly equal to `drafting_provenance.filing_date`; 21
   of 21 undated names serve ABSENT-explicit (key present, value `None` -- never wholly absent, and
   never a fabricated date). Independently re-confirmed this seat, fresh invoke: BA_US_Equity
   `as_of_date 2026-01-30`, planted negative control `None`. **AC1 and AC2 genuinely PASS.**
   `<status>` flipped to `complete`. Commits `15b5878817`, `2bb8fcf293`.
5. **`AMGT-rk-30` adapter**, last. Pre-act `fkKLVf...` -> post-act
   `0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo=` (786895 B, 00:59:50Z) -- independently confirmed
   this seat AND the CTO on the act's own isolated build (row Z-S168). Census 13/13. Final
   self-check: working copy byte-diffed against `e2d89be7da`'s full `scoped_amgt.py` -- zero
   difference, confirming no cell's code was dropped or altered across the sequence.
   **CONTRACT LIMB PASSES**: `bundle["scores"]` is now present on 33 of 33 names (previously
   absent from the bundle entirely -- the CRO's own named defect, now closed). **SERVE LIMB DOES
   NOT PASS**: a genuine, previously-unknown IAM gap -- the Lambda role's inline policy
   (`opal-amgt-scoped-api-grants`) carries `s3:GetObject`/`s3:ListBucket` over TWELVE prefixes and
   `scores/v1/` is in NEITHER. Independently confirmed this seat on TWO further instruments: a
   direct `iam.get_role_policy` read (12 prefixes enumerated, `scores/v1/` absent from both limbs)
   and a fresh live invoke reproducing the exact `AccessDenied` on `s3:ListBucket`. **Every one of
   33 names correctly discloses `scores_status: READ_FAILED`, each field `ABSENT_PULL` with the
   verbatim AccessDenied reason -- never a silent MEASURED-as-zero, never a 500.** This is the
   half's own disclosure clause working exactly as designed; the STOP against widening IAM in this
   act (census `iam 0 / Policy 0`) is what makes the gap visible rather than silently patched.
   Row `AMGT_RESAPP-Z-W27-S11` / CTO row `AMGT_RESAPP-Z-S168` filed BLOCKING, disarm_owner
   `2.0.0_SA_COO~Z` -- remedy is its own fresh IAM co-sign (`scores/v1/*`, trailing-slash form on
   both limbs), requested separately, never applied under this half. Order stays OPEN. No rollback
   needed (the deployed code is correct; nothing was widened). Commits `b05eb92cbc`, `c9b3426461`.

**REVISES `AMGT_RESAPP-Z-S164`'s own prediction**, per the CTO's own correction (row S168): the
"scores absent" symptom has not two but THREE causes, and until now (1) the IAM gap was masking (3)
the Peers V vocabulary question entirely -- (3) remains genuinely untested until (1) is fixed.

**Change-management entries**: five, one per act, each opened before its own first live act and
closed on its own post-act census, all committed with their respective act's commits above (none
left staged in the worktree past this drain).

**NEVER-WIDEN CO-SIGN CLOSED, both halves, five acts, three genuine passes at the code level (all
five deploys correct against their own stated scope), two orders complete (`rk-24`, `rk-25`), three
orders stay open on findings outside this half's own scope (a stale criterion premise, a router
edge case, and an IAM gap) -- none a breach of either signed half.**

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
