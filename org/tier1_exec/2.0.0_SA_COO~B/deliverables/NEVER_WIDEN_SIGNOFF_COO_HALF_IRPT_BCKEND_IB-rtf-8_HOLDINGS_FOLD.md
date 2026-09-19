# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtf-8: holdings' forked enforcer folded onto the shared module (the CTO's ruling S82 @b37fdfd5cd)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-19 ~09:2xZ. **The act signed:** the
deploy IB-rtf-8's arm (e) performs, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-8.md` describes it, read at HEAD
after the drain `b7abeda060` (the worker's first pass), **blob `565317d98ac2864e185533bd437e3fad756b380b`** (`git rev-parse
HEAD:<path>`, this turn). A packet whose bytes differ from that blob is NOT what this half signs; the second pass re-reads the blob hash
before any build. The CTO half is asked the same tick, by blob (98121: *"signed BY BLOB the same tick ... a re-cut packet is a
re-signature"*).

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. The writers of the named
property are counted (the packet's census, re-derived here on a different instrument).

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K1 (`N = 1`) | the served bytes of `irpt-holdings` only -- `enforce.py` materialized at build from the committed `_authz/enforce.py` blob `79c9d9dee1` (HEAD, re-read this turn) instead of the deleted stale fork `holdings/enforce.py` (blob `8f849457be`, byte-identical to `_authz/enforce.py` @28ccac62c9, pre-inversion); prior live `CodeSha256` `oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs=` (LastModified 2026-09-19T05:37:12Z, read live at packet time) | every holdings-snapshot response `irpt-holdings` serves, every firm reachable through `IRPT_DIRECTORY_BUCKET_MAP` (49financial, inflection, cottonwood), on BOTH branches: **SERVED** responses now carry the REAL `unprojected_grant {count, denominator, kinds}` where the fork's absent census let `response_envelope()` default it to zero (additive; no field renamed, removed or retyped); **SERVED-WHERE-THE-FORK-REFUSED** -- an advisor whose grants partially project now receives the projected subset with the gap disclosed instead of `UNPROJECTED_GRANT` whole -- THE LOAD-BEARING CHANGE, the same change rtf-2 already signed for the other six functions (my half @76db3f781e, packet blob 713a22a4d9) and the one the L4 ruling @61627f39f9 orders; **REFUSED (still)** -- an EMPTY permitted set refused on both codes exactly as before; the six object-swap refusals and `covers()` UNCHANGED (arm (a)'s diff: `covers()` in neither only-in-fork nor only-in-shared hunk) | re-publish `irpt-holdings` at the prior `CodeSha256` above through Terraform (`filename` / `source_code_hash` pinned to the pre-deploy zip) -- never `aws lambda update-function-code` (NEVER-9); verified by `served == CodeSha256` read back, the same discriminator arm (e) uses forward |

**Writers of the named property, counted:** `W = 1` -- a Lambda code deployment of `irpt-holdings`' own zip by `build-and-upload.sh`.
The two candidate second writers were excluded by rtf-2's packet on its own evidence (API Gateway response caching `0` hits across 47
files in `infra/aws/terraform/investor-reporting`; the portal-auth CloudFront/Lambda@Edge validator injects headers and does not cache or
transform the body) and the fold changes neither surface; `Entry`'s warm cache is per-invocation for `irpt-holdings` (no `cache=` at
construction). One property, one writer, one rule read. **Re-derived on a different instrument this turn:** the source map
`infra/aws/lambda/ci/lambda-source-map.json` at HEAD read by `json.load` -- of 216 functions, exactly 7 carry an `enforce.py`
`staged_from` entry (`irpt-performance-adapter`, `irpt-directory-search`, `irpt-narrative`, `irpt-ycharts-generate`,
`irpt-export-render`, `irpt-holdings`, `irpt-status`) -- the worker's os.walk census said 7 of 7 routes on the shared blob; two
instruments, same 7. `holdings/enforce.py` is ABSENT at HEAD (`test -e`, this turn); the drain's first-parent diff shows it deleted
(635 lines) and nothing outside the order's `<paths>` touched (13 files).

## The rollback key has a known second reading -- row W1-S31 (disarm_owner `1.0.0_SA_CTO`)

The manifest's own `functions.irpt-holdings.artifact_sha256` (`Bn7iLO/E/9CK...`) disagrees with the live `CodeSha256`
(`oVv1pYw56N22...`). This half signs the LIVE value as the rollback target, per NEVER-1 ("read from the producer's own rule at
signing"). **Condition on the act:** arm (e) re-reads `irpt-holdings`' live `CodeSha256` BEFORE the build; if it is not
`oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs=`, a writer moved the served bytes between packet and deploy -- that is a NEW REACHABLE STATE
this half did not sign, and the act STOPS with a row. The manifest field's staleness is the CTO's to reconcile (W1-S31) and is not
moved by this act (the order's BOUNDS leave `artifact_sha256` as found).

## Both branches covered

- The producer deploys (both halves at HEAD naming this blob; second pass): `irpt-holdings` rebuilt and applied under a ledger entry
  opened before and closed before the grading reads, `served == CodeSha256 == built` (by content, never by filename); the live request
  for `abby_horton`/49financial against `irpt-holdings` reads a served response with `unprojected_grant.count = denominator - k`,
  `count > 0` where the fork showed `0` or refused whole (the packet's expected outcome, READ FROM THE ORDER's own arm (e) and the ruling,
  not predicted from the input); the pre-fold bytes negative control reads the false-clean (the mutant arm already discriminated
  real=1 vs fork=0). **This half does NOT predict k; the arm measures it.** The other six functions are NOT rebuilt by this act.
- The producer STOPS (a half absent; the packet blob differs; the live `CodeSha256` no longer matches the packet's value): nothing is
  deployed, or the function is rolled back per the key the same turn, verified by read-back; rows W1-S29 / W4-S42 stay open on the CTO.
- The deploy lands and the holdings response OMITS `unprojected_grant` or carries it at zero on a request with a real gap: a BLOCKING row
  and a same-turn rollback -- a route that cannot report a gap is the defect S82 named; a deploy that reproduces it ships the silent
  partial the policy forbids.

## What this half does NOT sign

Any change to `HoldingsSnapshot.schema.json` (the worker's worktree carried an UNCOMMITTED edit to it; it did not drain and is not in
the packet); any rebuild of the other six functions; the manifest's `artifact_sha256` reconciliation (W1-S31, CTO); a principal
exercise beyond the one live read arm (e) names.

**Push state:** LOCAL -- origin/CLOUD @702bb2a256 (ls-remote read 08:49Z); HEAD after the drain b7abeda060.
