# Cottonwood account_return_daily is minted: 3,325 days, 6,653 objects, every served manifest read back — 0.7.0_AE_CloudOps~CB2

**Date:** 2026-10-11
**Task Order:** ADVI_COTBKF.TO-CB-al-2 (AMENDMENT 5 @`a8748799a1`, AMENDMENT 6)
**Status:** COMPLETE

---

## Objective

Mint Cottonwood `account_return_daily` under the R59 never-widen pair: 3,325 days of `data.parquet` +
`manifest.json`, the blank-reasons sidecar and the `dim_return_method` row, through the adapter's own apply path,
with the CTO half's seven conditions met. Second of the two orders the 06:18Z GO sequenced; the first (CB-bi-2)
stopped and is reported separately.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (6 legs, 6h window), `close-leg` x6, `close` | PASS | opened before the first write per condition 5; all 6 legs proven; CLOSED 072305Z. `close` takes no note, so the APPLIED/UNREAD disposition was appended to the entry |
| proof-of-spec-check | `<instance> CB38al2-AC1` | PASS | VALID rc=0 after three fix rounds; every violation it printed was real |
| comp-iam | not run | SKIPPED | preflight says "RUN at apply time"; recorded as an EXCLUSION, not a pass — see Decisions 4 |
| comp-schedule | not run | SKIPPED | DECLARED-NOT-APPLICABLE: a one-time mint arms no schedule |

**What worked:** `proof-of-spec-check.py` again. It refused `genre: DEPLOY` because the order carries no
`<proof_genre>` marker — a gate against a seat classifying its own act — and it caught `artifact_covered_by`
prose where bare criterion ids belong, and an `artifact-coverage` hole on the two non-day artifacts.

**What failed:** nothing in the tools. Two of my own reads needed correcting before they became claims: a
substring grep that matched `freshguard` on "ard" and implied a stranded ledger entry, and a
`mismatch|FAIL|ERROR` scan that flagged `ARD-VERIFY mismatches=0` on the field *name*. Both were false positives
of my own making, caught before they reached a report.

**Gap found:** none new.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Hash the four pinned files; confirm HEAD contains `f2415a44b5` | all four **equal** to AMENDMENT 5's pins, all clean in git; `is-ancestor` rc=0 with a positive control |
| 0b | Resolve `COTBKF_SWEEPS_CONFIG` from the dell2 pointer and hash it | `b1d93408...10a89d`, equal to the pointer's measured claim |
| 1 | `.open_deploys/` union across every live worktree | **33 of 33** trees, per-tree 17–29, 659 row-reads, **93 distinct** paths; 0 name this act |
| 1b | `deploy_ledger.py open` (6 legs) | entry committed before the first write |
| 2 | Condition 1 — `list-object-versions`, all pages, 3 prefixes | **0 versions / 0 delete markers** each; control on the parent prefix = **862 / 1** |
| 3 | `--stamp-manifest` | `ARD-COTTONWOOD-MANIFEST-STAMP days=3325 day_hashes_equal=3325/3325 note=present sidecar_rows=1584413 method_version=3`; manifest sha256 unchanged |
| 4 | Condition 4 — `--bond-check` | `measured_rows=107316 measured_rows_on_bond_days=0 fixed_income_cusips=778` |
| 5 | Condition 2 — `--show-day-manifest --date 2026-06-22` | exact line, rc=0; body carries the row-3 method sentence; **no custodian text anywhere** |
| 6 | **`--apply` under both halves — THE MINT** | rc=0, 07:01:01Z→07:17:06Z, `ARD-COTTONWOOD-APPLY days=3325 landed=3325 sidecar=landed method_row=landed` |
| 7 | Condition 3 — `--verify-served` | rc=0, `days=3325 match=3325/3325 sidecar=match method_row=match manifests=3325/3325` |
| 8 | Independent S3 census (not the tool's self-report) | **6,653** objects = 6,650 + 1 + 2, `IsTruncated=None` on each |
| 9 | Ledger close + APPLIED/UNREAD disposition | all 6 legs proven, CLOSED 072305Z |

## Verification

```
ARD-VERIFY mismatches=0 first=[]
ARD-COTTONWOOD-VERIFY days=3325 match=3325/3325 sidecar=match method_row=match manifests=3325/3325
```

Independent of the producer:

```
irpt/cottonwood/gold/account_return_daily/               objects=6650  (3325 data.parquet + 3325 manifest.json)
irpt/cottonwood/gold/account_return_daily_blank_reasons/ objects=1
irpt/cottonwood/gold/dim_return_method/                  objects=2     (data.parquet + manifest.json)
```

The same call read **0** on all three prefixes before the write, so the instrument discriminates landed from
not-landed on this exact target.

---

## Decisions Made

1. **Reconciled 3,328 `LANDED` lines against `days=3325` before closing L5, rather than quoting the last line.**
   The gap is 3: one sidecar, and `method_row=landed` is a single token covering **two** objects (a parquet and a
   manifest). 3,325 distinct dates, zero duplicates. An unexplained 3 on an irreversible mint is not something to
   wave past.

2. **Ran `--verify-served` in both invocation forms.** AMENDMENT 5 re-reads AC1's invocation as step 7's
   (`--manifest`), but the criterion's text at HEAD still carries the literal `--out` form. Both pass the bar; the
   literal form is **weaker** — without `--manifest` it emits no `sidecar=` or `method_row=` at all. Recorded both,
   graded on step 7's, and said which is which rather than silently substituting one.

3. **Did not take the schema's DEPLOY branch, though this is a deploy.** It needs
   `<proof_genre>DEPLOY</proof_genre>` from the issuer, and the order carries 0 occurrences. The BOUNDS Grant line
   *does* cover this order's file, so adding it was mechanically possible — and that is exactly why I didn't: a seat
   marking its own order a deploy so as to be graded on the branch it then fills in itself is self-dealing on the
   gate. Declared as an exclusion with the pair, risk class and rollback carried verbatim, and flagged to the
   issuer as a one-line fix for next time.

4. **Reported `comp-iam` as NOT RUN rather than as a pass,** against the preflight's "RUN at apply time". The
   question — can this identity PutObject under the prefix — was answered at a stronger grain by writing 6,653
   objects and reading every one back, and `comp-iam` models `(action)` and never `(action, resource)`.

5. **Filed no surprise row,** because none was owed: no refusal fired and no read-back differed. Rows `D2-S91`/
   `D2-S92` belong to CB-bi-2.

---

## Files Modified

| File | Change |
|------|--------|
| `org/critical_paths/change_management/20261011T0656Z_advi-cotbkf-...json/.md` | ledger entry: opened, 6 legs proven, CLOSED, + APPLIED/UNREAD disposition |
| `org/critical_paths/.open_deploys/advi-cotbkf-r38-al2-...json` | opened then cleared by the close |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/ard_cottonwood_mint_report.md` | new — the report the REPORT clause owes |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-al-2...proof_of_spec.json` | new — VALID rc=0, AC1 PASS |
| `.../task-orders/ADVI_COTBKF.TO-CB-al-2.account-return-daily-mint.md` | `<status>` issued → complete (1 line) |
| `org/tier2_senior/0.7.0_AE_CloudOps~CB2/logs/2026-10-11/` | this log |

**S3, 6,653 new objects, all inside the three granted prefixes:** `account_return_daily/` (6,650),
`account_return_daily_blank_reasons/` (1), `dim_return_method/method_version=3/` (2). No delete, no overwrite, no
key outside them.

---

## Blockers

**None on this order.** Two items are owned elsewhere and named so neither is stranded:

- `ADVI_COTBKF-D2-W66-S1` **disarms** on L6's `manifests=3325/3325` per condition 3. The disarm is the row's own
  act, not mine; the evidence that discharges it is in the report and the ledger.
- A **reader** for Cottonwood `account_return_daily` does not exist and waits on its own pair (ADDENDUM 11.1).
  The keys are deliberately APPLIED, UNREAD.

From CB-bi-2, still with `1.0.0_SA_CTO~DELL2`: row `D2-S91` (does ruling item 5 hold on a never-deployed
break-glass role?) and `D2-S92` (**ARMED** — a dell2 shared-infra plan proposes to recreate the live
`opalinvest-portal` bucket).

---

## Current State

Both orders the GO sequenced are terminal: CB-bi-2 **STOPPED** and routed, CB-al-2 **COMPLETE**. FWD-3's
Cottonwood rows are served and unread. Zero orders held, nothing waiting on this seat.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~CB2]` Report CB-al-2's last lines to `2.0.0_SA_COO~C2`. Then idle, event-driven.
2. `[1.0.0_SA_CTO~DELL2]` Rule `D2-S91`; own `D2-S92`'s disarm (two IAM grants on `cloudops-dell2-agent-user`, or
   a standing rule that shared-infra is not planned-for-apply from dell2).
3. `[2.0.0_SA_COO~C2]` Add `<proof_genre>DEPLOY</proof_genre>` to deploy-class faces so the proof grades on the
   deploy branch.
