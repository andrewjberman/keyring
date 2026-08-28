# 0.6.0_AE_PartnerETL — ADVI_INSURE.TO-A3-AE — 2026-08-28 ~16:57Z–18:0xZ

**Archetype:** BUILD + DEPLOY, interrupted mid-round by a sovereign vehicle change.
**TO:** `ADVI_INSURE.TO-A3-AE` (cell INS-a-5) — make the insurance leg REACHABLE and SCHEDULED.
**Outcome:** REACHABLE — done and deployed. SCHEDULED — cancelled on this vehicle by Andrew-direct
and re-cut onto the canonical bd-pipeline chain as another lane's TO.

---

## What the round was for

The deployed `opal-assets-bd49f-reporting-pull` vendored `insurance_leg.py` and could not reach it:
`lambda_handler` had zero insurance references and read `event["q_start"]` unconditionally, and the
leg had no entrypoint. Every insurance capture to date (08-25, 08-27) was a manual module
invocation — QA evidence, never production. No trigger existed on any plane.

## What landed

| act | state | evidence |
|---|---|---|
| (a) handler event-dispatch + the paged run path | **DONE** `@d0f9a8f7e4` | 5/5 arms then, 6/6 after (c') |
| (b) package rebuild + deploy | **DONE** | NEVER#6 ledger `20260828T1725Z` CLOSED 5/5; CodeSha256 `JyQp8pRO…` |
| (c) `aws_scheduler_schedule` | **CANCELLED** | Andrew-direct 17:40Z; CTO ruling 78512 |
| (c') `INSURANCE_EGRESS` + `.tf` TRIGGERS comment + 2 provenance fixes | **BUILT, commit HELD** | 6/6 arms; MSTR window 16 |
| (d) AC4 scheduled half | **MOVED** | now the first chain fire, TO-A4-AEC's wiring |
| proof-of-spec instance | **DONE** `@22d029d7c8` | VALID, rows=5, violations=0, rc=0 |

## The finding worth carrying out of this round

**The completeness signal was already being measured and then discarded.** The 08-27 pull landed
page0 only — 50 rows of a vendor-attested 77 — and the mechanism was in the leg, not the invoker:
`body_relationship_account_detail_search` defaults `limit=50, offset=0`; no caller ever advanced
`offset`; `probe_surface` lands at a default `page0` discriminator so a second page would have
overwritten the first. But the fourth finding is the actual defect: **`_denominator_for` already
read the server's `total`** and rendered it into a prose string ("a PAGE IS NOT A TOTAL") that
nothing consumed. The datum was never missing. The **consuming half** was.

That is the `A_VALUE_MUST_CARRY_ITS_CLAIM` failure mode one step further along: an unenforced
provenance field drifts to unpopulated, and an *unconsumed* one drifts to ignored while still
printing correctly to anyone who reads the log. The fix is a consuming loop plus a rejectable enum
(`measured-complete` / `measured-short` / `attested-total-absent`), not a bigger page limit — a
bigger limit is still a guess at cohort size and goes silently wrong the day the cohort outgrows it.

Verified against the real vendor on the one authorised QA invoke: `pages=2 rows=77
attested_total=77 completeness=measured-complete`, page0 50 @offset 0 + page1 27 @offset 50.

## Control discipline

- **RED ARM 1** — server attests 77, serves 50 → run raises `measured-short`. Without it the
  completeness verdict could be a constant reading `measured-complete` and every green arm passes.
- **RED ARM 2** — `INSURANCE_EGRESS` off → named refusal, **0 HTTP calls including the token mint**.
  Added because `mint_both_authorities` reaches `veh._request` directly, *not* through
  `call_surface`; gating only `call_surface` would have left a real vendor path open behind a
  closed gate.
- **PRE-FIX CONTROL** — ARM3 re-run against HEAD bytes → `KeyError('q_start')`. Both halves of the
  control set reachable from different truths at the field under test.
- **PRIOR-ARTIFACT CONTROL** — all ten dispatch/pagination markers structurally 0 in artifact
  version `a8RGEOGqhz…`, present in the new; the four untouched `taxsma_*` modules byte-identical
  across both, proving the build is scope-exact rather than a wholesale replacement.

## The never-widen catch

An **untargeted** `terraform plan` in `infra/aws/terraform/opal-assets` reads `0 to add, 3 to
change, 0 to destroy`. Only one was mine. The other two are the X-ii-a staged set
(`0.7.0_AE_CloudOps` `@2740e4de8f`, "STAGED-NOT-APPLIED"), one of which **moves a served prefix**
(`emitter` `AGGREGATE_PREFIX` `gold/mdpf_revamp/_aggregate_aua/` → `portal/gold/mdpf/_staging/…`).
A bare apply by any seat lands all three under that seat's name. Applied on a **saved `-target`'d
plan**; 0-diff on-target re-plan confirms both foreign changes remain pending and unapplied.
Adjudicated by COO 78489 as known and held for its own atomic window — targeted-applies-only is the
standing rule for that root until X-ii-a runs.

`terraform fmt -check` flags 7 pre-existing files there including this one. **Not swept** — `fmt`
WRITES and would pull six other seats' files into my commit. To learn whether my own block was
canonical without letting `fmt` touch the tree, the file was copied to scratch and `fmt` run on the
copy: the only diff is the pre-existing IAM `Sid`/`Effect`/`Action` alignment at lines 80–112, none
of it in my edits.

## Where I was wrong, or imprecise

- **The egress citation in my own TO was wrong and I nearly inherited it.** The TO and its dispatch
  both cited the 2026-07-17 `.tf:12-13` grant as covering insurance egress. Read at source it does
  not — that grant is scoped to the 49F *portfolioreporting* API; the insurance surfaces are
  `/request/api/offline/*` and `/relationship/request/*`. Coverage existed, from a *later* authority
  (Andrew 08-25 + COO 71632), mechanically enforced in `SURFACE_EGRESS`. Surfaced as a correction
  rather than adjudicated either way; confirmed right by COO 78445. **A relay that inherits a
  citation inherits its scope error too.**
- **The cadence question I raised is what moved the work.** I flagged that a sanction for *bounded,
  human-initiated* pulls is not on its face a word about a *standing unattended daily*, and
  escalated rather than inferring. Andrew answered at 17:40Z by moving the pull to a pipeline
  vehicle entirely. The right call was escalating; had I inferred either way I would have been
  wrong, and quietly.
- **I lost the `Apply complete!` line to a `tail` window** and said so rather than implying I had
  read it. The counts-equal claim rests on state (0-diff re-plan + live CodeSha256 == the saved
  plan's target), which is stronger — but it is a *different instrument* than the criterion names,
  and it is recorded as such in the instance's `status_reason`.
- **The AC4-QA invoke ran ~2 minutes before the hold that would have stopped it** (fired 17:43:19Z;
  hold 78506 stamped 17:45:12Z). Legal at its time under COO 78445 and announced in advance in
  78493 — but disclosed unprompted and precisely, because a timeline is exactly the thing that gets
  read wrong later. Accepted by CTO 78519 and COO 78530.
- **First `comp-blast` call was on the file path and returned NOT-FOUND.** A NOT-FOUND is not a
  "nothing breaks" clear; the ARN is the node identity. Re-ran on the ARN.

## Deviation declared

COO 78445 asked that (c) land in the **same** ledger as (b). `.tools/deploy_ledger.py` has no
`add-leg` verb (`open` / `close-leg` / `close` / `hold` / `check` / `list`), so an opened entry
cannot be appended to. Closed (b)'s ledger as terminal-and-complete rather than hold it open past
its window, and reported the deviation in 78493 instead of absorbing it. (c) was cancelled before
it needed a ledger at all.

## Open / handed off

- **Commit of (c') is HELD** by MSTR integration window 16 (18:01Z, msg 78555). The artifact builder
  gates on a clean source tree, so the deploy cannot start until the CLOSE. Nothing else is in front
  of it.
- **`INSURANCE_EGRESS` is NOT live yet** — measured on the live function, not assumed. Ordering
  dependency sent to `0.7.0_AE_CloudOps~K` + COO (78560/78561) in its NOT-YET state, because silence
  on a one-directional dependency reads the same as readiness. If a chain fire lands first it
  refuses fail-closed — a clean negative control of the wiring, but it spends the fire that is
  supposed to be the acceptance.
- **AC4 acceptance** is now the first chain fire with `runner=insurance` (2026-08-29T04:35Z if both
  lanes land today) — `0.7.0_AE_CloudOps~K`'s TO-A4-AEC wiring, under CTO's plan-gate.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-blast` | on the function ARN, and on the source path | Rule-20 canonical calls (`cloud.blast.what_breaks`, `trace.blast.what_breaks`) run BEFORE the change. 9 downstream nodes, all IAM/S3/secret/principal; caller chain 8 nodes, **all semantic — no invoker edge**, independently corroborating "no trigger on any plane" from a different plane than the CLI census. First call on the FILE PATH returned NOT-FOUND with its 27,054-node universe printed — recorded because a NOT-FOUND is not a clear. 33 HOLD claims read at source: all `bd-gold-*` runner subjects, a different Lambda, and they argue *for* scheduling. |
| `comp-kuzu` (provenance) | header on every `comp-blast` call | `kuzu_nessie_db` 27,054 nodes / 60,505 edges, built 2026-08-28T16:13:09Z (age 0.9h), Nessie HEAD current, `graph_nodes` last-write 4.3h (< 6h cadence). Vintage read, not assumed. |
| `comp-iam` | `service` + `gaps` + 3 live `simulate-principal-policy` arms | `service`: 3 operations, **no new action class** → no `iam.tf` change for the package deploy. `gaps`: zero rows name this function against a positive control of 14 missing / 292 deny-present / 2 resource-mismatch across 31 services — the sweep ran, the zero is real. The scheduler-role question was settled on the **live** plane instead (tool's own DESIRED caveat honoured): implicitDeny / **allowed (positive control)** / implicitDeny. That measurement is what turned (c) into a STOP-and-surface rather than a silent IAM edit. |
| `commit-gate` | on every `.py` touched, both commits | clean 3/3 then 2/2 (py_compile + ds-precommit + ruff py39). Risk-reflex surfaced 10 claims on `insurance_leg.py` vs a 7.8h-old danger map, denominator 3 files / 1,910 nodes; the citation (the TO-A1-AE ledger) was **read at source** and supplied the build-input carrier fact that shaped (b). |
| `deploy_ledger` | `open` → `close-leg` ×5 → `close` | NEVER#6 ledger opened at deploy-START and CLOSED all-legs-proven. **Gap found and declared:** no `add-leg` verb, so COO's same-ledger instruction was not mechanically possible. |
| `terraform` | `fmt -check`, `validate`, `plan -target -out`, `safe-apply`, re-`plan` | `validate` Success; targeted saved plan 0/1/0; `safe-apply` (HALTGT .001 passed) rc=0; on-target re-plan "No changes". `fmt` never run as a writer on the tree — canonicality of my own block established by running `fmt` on a **scratch copy**. |
| `proof-of-spec-check` | positional, 5 ids | `rows=5 violations=0` **VALID**, TRUE_RC=0 (bare rc, recorded in the instance per CVO 76166). First pass INVALID on 11 schema violations — enums corrected against the validator's own message rather than guessed. |
| `build-and-upload.sh` | `opal-assets opal-assets-bd49f-reporting-pull` | import-closure OK 6/6; write VERIFIED (size + sha256 metadata match). Source map checked **before** building — all 6 members registered, no edit needed (the TO-A1-AE lesson: the source map builds, `BUILD_MANIFEST` only documents). |
