# Session log — 0.7.0_AE_CloudOps~L — ADVI_49F.P14-VEHICLE (V14-1 / V14-2)

**Seat:** `0.7.0_AE_CloudOps~L` (D2 re-seat, laptop/CLOUD)
**Window:** 2026-08-27T16:00Z – 17:30Z
**Archetype:** BUILD — infrastructure change + exercised verification
**Authority:** COO GO msg 76134 (2026-08-27T160935Z); Andrew-direct seat word @1d761ded1f
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps~L/task_orders/ADVI_49F.P14-VEHICLE.ssm-date-parameter-and-backfill-mechanics.md`

---

## 1. What this session did

Built the **vehicle** for the ruled 531-partition ADVI_49F backfill. Before this session the SSM
document `advi-49f-chain-dispatch` hardcoded `python3 chain_49f_entrypoint.py --production` and could
express no historical date — the ruled backfill (brief @e4f7ecbfdc P1.4) had no way to run.

**V14-1 (VEHICLE LIVE) — PASS.** Added a `Date` parameter to the document; the runCommand now branches:
empty `Date` → `--production` (the scheduled nightly path, behaviourally unchanged), non-empty →
`--date {{ Date }} --upload`. Applied through `safe-apply`, `-target`ed. Live document reads
DocumentVersion **1 → 2**.

**V14-2 (HALT TRAP RULED OUT BY EXERCISE) — PASS.** Two consecutive direct sends with
`StartedByDispatcher` omitted; host `running` after both, read from **instance state, never send rc**.

**V14-3 (GATE HONORED) — PASS.** Zero backfill execution. Both dependency faces read `staged`.

**V14-4 / V14-5** remain `UNCOMPUTABLE-BY-CONSTRUCTION` — gated, declared as exclusions, not papered over.

---

## 2. Startup

- `/watcher`: registered `0.7.0_AE_CloudOps~L` (PID 33364); persistent inbox Monitor armed, task
  `bz15bvxah`, arm banner `parent-tied: pid 1962539` (ARMED, self-exit capable). Pre-arm orphan scan
  found **0** watchers on this serial (12 stream watchers on the box, all other serials) — no orphan,
  no kill, so neither startup false-positive class applied.
- `/cloud-ops` one-shot for the permissions profile + deployment rules. Zero crons armed.
- A.3 PATH probe: **105 of 105** comp-tools resolve bare, and the mandatory EXERCISE half ran (a
  forwarder produced its own banner) — resolution is not execution, and only the second half can see a
  live-forwarder/dead-target break.

---

## 3. Compiler Tools (MANDATORY SECTION)

Every `<run>` from the TO's `<compiler_tools_mandate>`, its observed result, and pass/fail vs `<expect>`.

### Phase 1 (before write)

| `<run>` | observed | vs `<expect>` |
|---|---|---|
| `comp-iam service advi-49f-chain-dispatch` | **NO SUBJECT.** `No service matching 'advi-49f-chain-dispatch'`; tool enumerates 185 Lambda services + 178 IAM roles. The target is an SSM **document**, not a Lambda service. | **NEITHER PASS NOR the `<if_mismatch>` STOP.** No missing grant was found because *nothing* was found. Recorded as instrument-has-no-subject and re-run against the correct subject rather than reading silence as clearance. |
| `comp-iam service advi-49f-gold-dispatch` *(the correct subject — the role that actually holds the SSM path)* | 5 operations incl. `ssm:SendCommand [UNRESOLVABLE-RESOURCE]`, `ssm:DescribeInstanceInformation [GRANTED-BROAD]`. Tool states its own plane: **DESIRED (Terraform), not APPLIED**; 24 policy blocks unattached/unseen; 2 deny statements unparsed. | **PASS.** SSM path grants enumerated, no missing grant → no STOP. Treated as a FLOOR, never a deletion warrant. **No NEW resource ARN is touched** (same document, same bucket, same role), so the TO's `simulate-principal-policy` requirement for a new ARN does not apply and was deliberately not run. |
| `comp-pipescript postdeps chain_49f_entrypoint --firm bd` | **REFUSED rc=2** — `unknown script id 'chain_49f_entrypoint' -- not found in tree 'bd'` (universe searched: 30 tree script ids + 5 declared deps keys = 35 distinct). | **UNMEASURED, declared as an exclusion.** The refusal is correct: the chain lives at `data/assets/scripts/gold/runners_49f/`, the **assets** tree, which `--firm` does not enumerate (`bd\|inf\|cot\|mdpf`). Consumer set therefore not established. **A refusal is not a clean sweep** — not reported as "no consumers outside the ruled set". |

### Phase 2 (before commit)

| `<run>` | observed | vs `<expect>` |
|---|---|---|
| `comp-iam gaps` | **NOT RUN — N/A by its own trigger rule**, recorded rather than silently skipped. | **PASS.** The `<expect>` scopes it to "Run ONLY if iam.tf changed. If iam.tf unchanged, record that fact." No `iam.tf` changed: commit `a8907bf114` touches the `aws_ssm_document` resource in `advi_49f_floor.tf` plus records; no IAM resource, policy or role added or altered. |

### Phase 3 (after commit)

| `<run>` | observed | vs `<expect>` |
|---|---|---|
| `aws ssm get-document --name advi-49f-chain-dispatch` *(rail-checked: no comp-tool reads live SSM document content)* | DocumentVersion **2**, Status Active. `Date` present with `allowedPattern ^$\|^[0-9]{4}-[0-9]{2}-[0-9]{2}$`. runCommand renders `python3 chain_49f_entrypoint.py --date {{ Date }} --upload` in the non-empty arm; `--production` survives only in the empty arm. | **PASS.** This is the APPLIED plane and the acceptance substrate — not the tf diff. |

---

## 4. Evidence trail

**V14-1.** Live read above. Post-apply targeted re-plan, same binary: `No changes. Your infrastructure
matches the configuration.` Commit `a8907bf114`.

**V14-2.** Host `i-01003b035d2988dfb` (bd-gold-layer-runner, r6i.4xlarge) was **stopped** at start;
started once, SSM `PingStatus Online` 17:16:09Z.

| send | CommandId | Date | status | **instance state after** |
|---|---|---|---|---|
| 1 | `443caee1-c1a5-4276-bfe6-365dc7b3e1b7` | `1990-01-02` | Failed (expected) | **running** |
| 2 | `1c453cab-9da1-40c6-aa54-9b911c78ebe2` | `1990-01-05` | Failed (expected) | **running** |

`StartedByDispatcher` **omitted** on both (defaults `"false"`); neither routed through the
`advi-49f-gold-dispatch` Lambda. Host returned to **stopped** at the end (driver halts the host itself,
once). A **different date per send** was deliberate — it demonstrates the per-send date a 531-date loop
needs, which sending one date twice would not. No `CHAIN REFUSED: live lock` on send 2, so the
entrypoint mutex releases between runs (`chain_49f_entrypoint.py:516-521`, `finally`).

**Why these dates write nothing — verified at source BEFORE sending, not after.**
`a00_runner.py:116` raises `SystemExit('REFUSED: fact_acc has no partition date=...')` at **read** time,
before any BUILD or WRITE. Both runs printed:

```
HISTORICAL BACKFILL date=1990-01-02 -- --production is PROHIBITED on this path
CHAIN START date=1990-01-02 mode=qa-upload workdir=/tmp/49f_chain_work stages=17
REFUSED: fact_acc has no partition date=1990-01-02 (have ...['2026-08-24','2026-08-25','2026-08-26'])
CHAIN ABORT stage=a00_dim_account rc=1 wall=0.8s -- nothing after this stage ran
```

`mode=qa-upload` with the **sent** date — not `mode=production` with a derived T-1 — is the sharp line
proving the vehicle carries. Zero partitions written; the only S3 write is the chain log.

**Injection control, exercised with both arms.** `Date='2026-01-01; whoami'` → **REFUSED** server-side
(`InvalidParameters`). `Date='1990-01-02'` on the **same parameter** → **ACCEPTED** and dispatched. The
refusal therefore discriminates on the **value** via `allowedPattern`; it is not a parameter-not-found
artifact. `allowedPattern` is the injection control on a value substituted into a `runShellScript` body.

---

## 5. Instrument traps hit this session (each cost real time; each is transferable)

1. **Two terraform binaries, silently different.** PATH resolves **v1.14.5**; `safe-apply` prefers the
   sibling `.tools/terraform.exe` **v1.9.8**. My plan was cut by 1.14.5 and the apply **refused** it —
   *"plan files cannot be transferred between different Terraform versions."* The refusal was the good
   outcome. Re-init + re-plan on 1.9.8 before the real apply. No shared damage: only `advi_49f_floor.tf`
   was modified; `.terraform.lock.hcl` untouched. **Resolve the binary the wrapper will use, not the one
   on PATH.**
2. **`safe-apply`'s tombstone gate degraded to zero coverage and said so.**
   *"tombstone gate could NOT plan this tree, so it checked NOTHING. This is a GAP, not a pass."*
   Closed by hand with a printed denominator: **7** tombstoned resources (6 `aws_s3_bucket` + 1
   `aws_dynamodb_table`), none matching `advi-49f-chain-dispatch`, and the plan is **0 to add** so the
   gate's blocking condition (a CREATE of a listed resource) is structurally unreachable.
3. **A positive control aimed at the wrong subject.** Scanning `tombstones.json` I chose `lambda` as the
   control token; it returned **0**, same as every target token. The control was wrong, not the scan —
   the file holds only buckets and one table. Opened the file instead of guessing a second time.
4. **The untargeted plan was not mine.** `terraform plan` with no `-target` = **4 changes, 3 foreign**.
   Targeting was therefore *required*, not stylistic. Filed to the surprise channel (below).
5. **HALTGT blocked on the BASE serial's stale mail.** The checkpoint surfaced 5 messages, all ~1 day
   old and addressed to `0.7.0_AE_CloudOps` (base) from a dead session. All five reviewed — none
   STOP/HALT class, none touching this document or chain — then `HALT_ACK=1`. Per doctrine a HALTGT
   *pass* is not cited as evidence; this was a *block*, and the review is the record.

---

## 6. Surprise channel

- **76182 → 3.0.0_SA_CVO, cc 2.0.0_SA_COO. OBSERVATION / INERT. Accepted and routed (CVO 76186).**
  `infra/aws/terraform/opal-assets` untargeted plan carries 3 changes foreign to this seat: MDPF egress
  publisher `AGGREGATE_PREFIX "gold/mdpf_revamp/_aggregate_aua/" -> "portal/gold/mdpf/_staging/aggregate_aua/"`,
  output `mdpf_egress_publisher_live_serve_cosigned +true`, and dynamodb `opal-assets-daily-aua`
  `table_arn`/`table_name` outputs `-> null`. Item 1 is served-output-shaped (NEVER-1 never-widen
  territory). **No action taken, not chased**; my apply was `-target`ed so it swept none of them. CVO
  put one question to CTO+COO: does that drift have a named owner and does sign-off exist.

---

## 7. Record correction raised against a peer's commit (surfaced, not adjudicated)

- **76141 → COO.** My TO's `<dependencies>` block carried `status="complete"` for both `c01-SIGNFIELD`
  and `c02-CFINPUT` while both faces read `staged`. The attribute was the **permissive** arm on a face
  guarding a 531-partition production-history write. COO **fixed it at source** (`@fe7b4bcba3`) with an
  issuer note: `status` is the *required unlock state*, not a current-state claim. My latest +
  most-restrictive reading was confirmed correct.
- **My own TO `<status>` flip was swept into COO's commit under COO's author line.** Verified by
  `git show fe7b4bcba3` on that path: the `staged -> pending` hunk is mine, attributed to COO. Reported;
  **no history rewrite requested.** Mechanism worth carrying: `safe-commit`'s contamination guard is
  **per-path**, and COO legitimately declared that path — **two seats editing the SAME FILE are not
  separable by it.** This is the concurrent-agent class COO themselves broadcast in 71524.

---

## 8. Deploy discipline

Ledger `org/critical_paths/change_management/20260827T1652Z_advi-49f-p14-vehicle-ssm-date-param_deploy_completion.md`
opened at deploy-START with all 4 legs declared, **CLOSED** with every leg carrying proof
(`all 4 legs proven; sentinel removed`). Nothing stranded. Host returned to its prior stopped state.

**Push state, MEASURED and stated in the required form:** commit `a8907bf114` is **LOCAL — not on
origin**. `git ls-remote origin refs/heads/CLOUD` = `0aa94d07e0809d1e120254bcc0bb895d5435a64c`;
`git merge-base --is-ancestor a8907bf114 <that>` returns **false** (containment measured, not assumed).
My push was refused by the **LD-0367 rule 2 / LD-0368 integrator-only gate** — correct behaviour, not an
obstacle; the hourly integration window moves it and the audited override was **not** used.

Also honored: MSTR's MERGE WINDOW (76157) — held all safe-commits until the CLOSE frame (76178), and
proactively told MSTR I held an uncommitted edit in `opal-assets` so an 87-commit merge would not abort
on it. MSTR confirmed the file was untouched.

---

## 9. Proof of spec

`org/tier2_senior/0.7.0_AE_CloudOps~L/deliverables/ADVI_49F.P14-VEHICLE_PROOF_OF_SPEC.json` — **VALID,
TRUE_RC=0**, coverage CHECKED via the positional id list `V14-1,...,V14-6`.

**The first validation attempt returned rc=1 / INVALID with 3 real violations** (`firm: 'bd'` not in the
enum; V14-4 and V14-5 each missing the `status_reason` the validator requires for any non-PASS status).
All three were defects in my instance, fixed at source. Recorded *inside* the instance — an instance
that only ever reports its passing run is indistinguishable from one whose validator was never run.

**Mutant control FIRED:** blanking V14-1's `output_evidence` on a copy → `MUTANT_RC=1` (re-captured
outside a pipe: `MUTANT_RC_DIRECT=1`) against `TRUE_RC=0` on the real instance. Both arms reachable from
different truths. **Determinism STABLE:** two runs, rc=0 both.

---

## 10. State at close

- **V14-1 PASS, V14-2 PASS, V14-3 PASS** (gate honored), **V14-6 PASS**.
- **V14-4, V14-5** gated — `UNCOMPUTABLE-BY-CONSTRUCTION` with `status_reason` naming the later run.
- Execution legs remain held until `c01-SIGNFIELD` **and** `c02-CFINPUT` read complete **at their own
  faces**, read at unlock time. The affected-set denominator will be **re-derived**, never copied from 531.
- Host stopped. Ledger closed. Watcher live. Nothing owed except the gate-clear watch.
