# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtg-3: the performance route reconciles to the bound id space (K-CODE x 1; FWD-2, row W2-S27)

**Signer:** `2.0.0_SA_COO~B` (the COO half; NEVER-1 -- CTO+COO). **Signed:** 2026-09-20. **The act signed:** the apply
IB-rtg-3's arm (d) performs and the live proof arm (e) then takes, exactly as the packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-3.md`
describes it at HEAD, **blob `1a1b7b2709f44c03c37a52325623208fe5652cd6`** (`git rev-parse HEAD:<path>`, at drain @5700e1c825).
A packet whose bytes differ from that blob is NOT what this half signs. The CTO half is asked the same tick, by this blob.

**STATUS NOTE (issuer):** this order's `<status>` was corrected `complete` -> `pending` at the drain (@d25a6a0a07). The
worker's R74-AC1 IN-PROCESS battery PASS is necessary but NOT sufficient: arm (c) (:28) governs the first pass ("ABSENT ->
STOP, order stays open"), the live `irpt-performance-adapter` is UNCHANGED, and the served-path deploy signed here is the
SECOND pass. FWD-2 realizes only when arm (e) proves the SERVED route resolves.

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-CODE (1 function) | `irpt-performance-adapter` (`module.irpt_performance_adapter.aws_lambda_function.this`, `performance` root) served bytes: ONE edited member `performance/tenants.py` (its `ROUTES` now keyed on the opaque `fir_...` id via the estate's `_ids.opaque_firm` normalizer -- never a fourth hand-typed spelling; the STOP-and-ROW branch did NOT fire); BUILT `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=` at build-store `VersionId=M0E32HJhwg54I6jcU4g2e58Ktthey_51` (171542 bytes), VERIFIED AT REST (object RE-DOWNLOADED and re-hashed == the metadata == `lambda-source-map.json`'s written `artifact_sha256`); the served-byte delta is EXACTLY `tenants.py` (23 of 23 members present in both zips, exactly 1 differs, and it hashes identically to the reviewed worktree file); prior LIVE `CodeSha256` `IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw=` (rollback target, 169955 bytes) at build-store `VersionId=38i7y_iXZqvWIzUNetKnBxXxs9dAuOGF` | **the performance route for each of the 3 registry firms (`49financial`, `cottonwood`, `inflection`, re-derived LIVE this pass -- never inherited)**: WITH the fix, an authorized scope-resolved request resolves a `TenantRoute` instead of raising `UnknownTenant` -> `DEPENDENCY_UNAVAILABLE`; WITHOUT (today), every real performance request raises `DEPENDENCY_UNAVAILABLE`. **NO IAM WIDENING** -- `irpt-performance-adapter-role`, environment and every other resource untouched (`comp-iam` DECLARED-NOT-APPLICABLE, honoured) | re-publish `CodeSha256` `IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw=` (build-store `VersionId=38i7y_iXZqvWIzUNetKnBxXxs9dAuOGF`, verified present and equal) through Terraform against `module.irpt_performance_adapter.aws_lambda_function.this`, never `update-function-code`; verify `served == CodeSha256`; the served behaviour returns to the pre-fix `UnknownTenant`, not a NEW hazard |

**THE DISCLOSED NO-CAPTURE CONSEQUENCE (row W3-S48, disarm_owner `2.0.0_SA_COO~B`):** the fix closes `DEPENDENCY_UNAVAILABLE`
(R74-AC1's target), but `handler.py`'s `RECORDED_LABELS` (untouched, this cell's bound is `tenants.py` only) is still keyed on
the retired spelling, so a served request under the DEFAULT `recorded` transport mode returns a graceful NO-CAPTURE absence
rather than a captured replay. This half signs the route-RESOLUTION change (R74-AC1); the NO-CAPTURE is a WEAKER, disclosed
downstream outcome and a SEPARATE follow-on (W3-S48), never a cross-firm read and never an exception. Arm (e) proves route
resolution for the 3 firms; it does NOT claim captured-evidence replay.

## THE ARM (d) GATE THIS HALF SIGNS -- BY SUBTRACTION, WITH THE ROUND-7 MULTI-CELL QUALIFIER

Per root, `resource_changes` of `terraform show -json <planfile>` WHOLE, minus the CLOSED PRINTED subtraction set (CTO's ruled
construction @0a7f61ae86): (i) plan top-level `.timestamp`; (ii) the S3 data-source's `version_id`/`last_modified`. Everything
else IN by default; a new field FAILS CLOSED; both denominators printed. COVERAGE, all TEN roots:
  * MY root (`performance`): EXACTLY `module.irpt_performance_adapter.aws_lambda_function.this` `actions ["update"]`, before `IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw=` -> after `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=` (+ `s3_object_version` `38i7y_iX...` -> `M0E32HJh...`), nothing else after subtraction (the packet's saved plan showed EXACTLY this; a FRESH plan is re-taken at arm (d), never the saved one).
  * The 6 NON-round-7 roots (`api`, `core`, `directory`, `intake`, `narrative`, `ycharts`): EACH EMPTY after subtraction.
  * The up-to-3 SIBLING round-7 roots (`export`, `holdings`, `ops`): EACH empty (already applied) OR EXACTLY that sibling cell's OWN declared `aws_lambda_function.this` update pinned to a sha in ITS signed packet (`export` -> `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=`, and export ALSO adds `aws_iam_role_policy.export_render_receipt` per IB-rtg-1's own K-IAM key; `holdings` -> `rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=` + its `handler` flip; `ops`/irpt-status -> `B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0=`), plus `s3_object_version` -- and NOTHING ELSE.

**THE SIBLING-ROOT ADMISSION IS A WIDENING, STATED OUT LOUD (W1-S45 / W4-S46).** Every round-7 root reads `source_code_hash`
from the LIVE S3 object metadata with no version pin (verified across the round-7 `lambda.tf` files), so a sibling's upload
shows on its root in any worktree's plan. BOUNDED to the three sibling cells' OWN declared builds (and export's OWN declared
new IAM policy), each pinned in that cell's signed packet; ANY other content on ANY root is a STOP. A REFUSAL IS EVIDENCE,
NOT AN OBSTACLE; NEVER widen the admission at the terminal. The four applies are SEQUENCED; after the last, a final
all-ten-roots plan MUST read CLEAN.

## Both branches covered

- **Applies** (both halves at HEAD, this blob): fresh per-root plan, subtraction gate over ten roots (denominator printed),
  apply `performance` IFF it passes -- `.tools/safe-apply.sh`, ledger opened before, `0 to destroy`, rc 0, 0-diff after,
  `served == W4rYXgZz...`. **Arm (e)** under `irpt-performance-adapter-role`: each of the 3 registry firms resolves a
  `TenantRoute`, 0 `DEPENDENCY_UNAVAILABLE`, 0 fourth-id-space literals in the deployed bytes; route/function/role printed.
  This half does NOT predict; arm (e) measures.
- **STOPS** (half absent / blob differs / gate refuses / a different plan digest, a second address, or any `to destroy`):
  nothing applied, or rolled back per the key and read back; the route stays at `DEPENDENCY_UNAVAILABLE`.

## What this half does NOT sign

Any code other than `tenants.py`; the `handler.py` `RECORDED_LABELS` reconciliation (row W3-S48, a follow-on); any IAM,
environment or route change (there is none); the three sibling cells' own acts; FWD-11. `W = 1` -- the sole writer of what
`irpt-performance-adapter` serves is a Lambda code deployment of its own zip (the console/CLI qualifier carried; banned by
NEVER-9, covered by the rollback's own re-read).

**Push state:** LOCAL -- this half commits this tick on CLOUD; origin/CLOUD read at the drive-log send (MSTR pushes CLOUD).
