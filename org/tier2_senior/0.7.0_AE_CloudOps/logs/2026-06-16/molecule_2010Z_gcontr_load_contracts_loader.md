# MOLECULE: load_contracts_from_yaml / _is_pending_ratified (infra/aws/globgrph/derive_runner.py)  (scale: MESO)
**archetype:** DIAGNOSE

## Unit + expected role
The NFRA_GCONTR contract-row loader: `load_contracts_from_yaml(yaml_path, dry_run, stamp_ratified, overwrite_ids)`
+ its gate helper `_is_pending_ratified(val)`. The `--load-contracts` entry of the in-VPC derive image
(opal-globgrph-derive-runner). EXPECTED role: the SEV1/SEV2 never-widen GOVERNANCE control -- (a) append-only/
skip-existing (never overwrite a live row), (b) refuse to land an UNRATIFIED row (PENDING placeholder skipped
unless --stamp-ratified), (c) stamp ratified_at = a real Nessie HEAD hash on a sign-off-confirmed write so
existence-in-window is exact. Ground truth: the DEPLOYED image, not the repo.

## 1. Composition -- what it actually is (deployed vs declared)
Deployed behavior == fe645e103 (PROVEN behaviorally, sharper than a repo read): this session's plain --dry-run on
the live image showed peers+aum SKIP-as-PENDING -> PLAN write=0 (the prefix-aware gate firing on
PENDING-CTO-COO-SIGNOFF), and the real load stamped real hashes. ECR :latest digest sha256:4a1e1380...
KNOWLEDGE-PARITY: docstrings are ACCURATE to the deployed behavior -- the load docstring ("APPEND-ONLY + ENSURE;
skips already-present; SAFETY GATE skips PENDING unless --stamp-ratified; stamps ratified_at = authoring Nessie
hash") and `_is_pending_ratified`'s ("any PENDING.../TBD/empty/None = pending; prefix-aware; exact-match misses a
new sign-off variant") both match the code. No stale-docstring drift (the original exact-match claim was replaced
WITH the code in fe645e103). NOTE: `_PENDING_RATIFIED` tuple is now partly redundant with the prefix check (kept as
the documented known-set + the helper's fast-path `val in _PENDING_RATIFIED`) -- harmless.

## 2. State -- live snapshot
The loader's "state" = the rows it produced. Live StaticTable (contract_engine, status ok) at 1955Z: 3 rows,
ALL with real-hash ratified_at (placeholder_pin=False): benchmark 6f21c75ca/pd=11 (untouched), peers a7bc0aed/pd=9,
aum a7bc0aed/pd=4. The governance control produced correct, honestly-stamped output. (The function itself holds no
persistent state beyond the table; the deployed image IS its artifact.)

## 3. Position in the chain
- UPSTREAM: CVO authors graph_contracts.yaml (repo) -> I stage to s3://opal-313476888478-globgrph/contracts/ ->
  loader reads it. Triggered by an OPERATOR (ecs run-task --load-contracts), NOT the nightly run_full_derive
  (separate entry in main()). Pin source: `_nessie_main_hash()` (Nessie REST /trees/main).
- DOWNSTREAM: graph_contracts table -> `contract_engine.load_contracts()` -> (a) surface_check_cli `_contract_advisory`
  (comp-surface-check SEV1 advisory) + (b) comp_aws_cli `cmd_contract_diff` (Q2 policy join). The loader feeds the
  entire Q1/Q2 contract-check surface.
- DEPS/REACH: pyiceberg RestCatalog (Nessie), boto3 S3 (YAML), `_nessie_main_hash`, `_contracts_pa_table` (§3 schema),
  `ensure_graph_contracts_table`. If a row's ratified_at is wrong, the Q2 existence-in-window windowing breaks.
- SEAMS to hand to /seams: loader->graph_contracts (done this session: SOUND); graph_contracts->contract_engine->
  comp-surface-check (the Q2 read path; not separately exercised this session).

## 4. Behavior -- deployed path (EXERCISED this session)
All branches exercised against the live image: (i) already-present (benchmark): SKIP via L1030 guard -> untouched.
(ii) PENDING + NOT in --stamp-ratified (dry-run): SKIP via L1033 -> write=0. (iii) PENDING + in --stamp-ratified:
to_write -> ratified_at stamped real hash -> append. WRITE_VERIFY re-read confirmed pd=9/4. Append-only commit, one
Nessie commit. The double-guard (already-present FIRST, then pending) is why a whole-file load can't regress benchmark.

## 5. Semantic quality + sharp probe
Output rows are byte-correct (period_defs match CVO YAML; CVO independently byte-verified GREEN vs the live table).
Sharp unhappy-path probe (the strongest defect a coarse look misses): the ratified_at STAMP is the value-limb's whole
point -- I probed what happens when the pin SOURCE fails. See DIG below.

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| `_nessie_main_hash()` fail-open -> placeholder ratified_at leak | **DIG** | _nessie_main_hash L329 returns None on ANY exception (5s timeout/parse-fail); load L1067 `head_hash=_nessie_main_hash() or ""`; L1071 `if _is_pending_ratified(...) and head_hash:` -> if head_hash=="" the stamp is SKIPPED -> a --stamp-ratified PENDING row lands with the literal 'PENDING-...' string as ratified_at | The EXACT bogus-pin value-limb defect fe645e103 fixed, re-enterable through a DIFFERENT door (empty head_hash, not unrecognized placeholder). The stamp gate fails OPEN; on a never-widen governance control it should fail CLOSED. Latent (needs a Nessie REST hiccup at load time; my load had a real head_hash a7bc0aed) |
| WRITE_VERIFY reports-but-doesn't-gate | **WATCH** | L1091-1095 re-reads + PRINTs `period_defs=N ratified_at=<16ch>` but never asserts/fails | A placeholder ratified_at (from the DIG above) OR a wiped period_defs would be SILENT -- task exits 0, just a log line. The integrity CHECK should be an integrity GATE (fail the load if ratified_at is_pending or period_defs shrank) |
| ECR :latest re-confirm before next-wave load | **WATCH** | live :latest digest sha256:4a1e1380 pushedAt ~18:50Z; a later build could overwrite :latest before CVO's next-wave SEV1 load | Self-mitigated: the established plain-dry-run discriminator (write=0 expected) catches a stale image before any write -- but only if the next loader runs it |
| prefix `startswith("PENDING")` vs real hashes | NOTE | _is_pending_ratified; Nessie hashes are hex (0-9a-f), 'P' not hex -> can't false-positive a real hash (tested 10/10: 6f21c75c->False) | Confirms the prefix gate is safe against re-stamping a live ratified row |
| double-protection ordering | NOTE | L1030 already-present guard fires BEFORE L1033 pending guard | Good design -- why a whole-file load structurally can't touch benchmark's live ratified_at |

## Assessment
The loader is a SOUND, correctly-behaving governance control as deployed -- it produced 3 byte-correct, honestly-
stamped live rows, its docstrings are at knowledge-parity with the code, and every branch was exercised. The
careful node look surfaced ONE genuine latent fragility (DIG): the ratified_at stamp fails OPEN when the Nessie pin
source is transiently unreachable, which would silently write the same bogus placeholder-pin the session's fix
targeted -- caught here through the unhappy-path probe, not a current bug. ROUTE: a hardening follow-up to the owning
lane (AE/me; CTO is folding the placeholder-token invariant into GCONTR PRD §3, so this fits there) -- make the stamp
gate fail CLOSED (if a row is pending-and-stamp-requested but head_hash is empty, ERROR/skip, never write the
placeholder) + promote WRITE_VERIFY from a print to a hard gate (fail on a pending ratified_at or a shrunk period_defs).
Not gating the completed load (which is verified correct). Surfacing it is the win -- it's the next-incident-avoided.

## Knowledge-parity delta + residual
BELIEVED: fe645e103 closed the bogus-pin class. TRUE: it closed the unrecognized-placeholder door; the empty-head_hash
door is still open (fail-open stamp). Routed to owner as a hardening finding (this report). NOT exercised: a forced
head_hash="" path (would need to fault Nessie REST mid-load) -- asserted by code-read, named as the empirical probe.

## Compiler Tools
Ground-truth via direct reads (StaticTable/contract_engine for live rows, aws ecr describe-images for the deployed
digest, code-read of derive_runner.py L320-332/L1026-1097) + the session's exercised dry-run/load behavior on the live
image. No comp-* graph tool -- this is a single-node deployed-code + live-row analysis, not a repo-relationship question.
