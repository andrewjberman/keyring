# Cottonwood's served method row 3 now words its income reason for the method: two keys overwritten, one column moved — 0.7.0_AE_CloudOps~CB2

**Date:** 2026-10-11
**Task Order:** IRPT_DASHBD.TO-DB-b-130 (issued @`ae6ec1c674`), risk **SERVED**
**Status:** COMPLETE — Branch A, written

> First order this seat has taken on **IRPT_DASHBD** (D9). It was cut here because `1.0.0_SA_CTO~DELL2` named this
> seat the applier (msg 5263) — the packet records that the apply gate graded a *worker's* apply REFUSED, so the act
> needs an AE seat. This seat's ADVI_COTBKF orders were all complete and terminal before it arrived.

---

## Objective

Overwrite exactly two keys so Cottonwood's served `dim_return_method/method_version=3` row states the income reason
worded for the **method** rather than naming a project outcome id — under a signed never-widen pair, capture first,
ledger first.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (3 legs), `close-leg` ×3, `close` | PASS | opened **and committed** before any S3 write |
| p69_round69.py (issuer's checker) | `. DB69-1-AC1` / `DB69-1-AC2` | PASS | both print their own OK line; both declare a FAIL base |
| the producer's own dry run | `method_row_probe(...)` → `emit_method_row(None, …, upload=False)` | PASS | the pre-write gate; no S3 client |
| proof-of-spec-check | `<instance> DB69-1-AC1,DB69-1-AC2` | PASS | VALID rc=0 first try |
| comp-blast / comp-iam / comp-routes | not run | SKIPPED | all three DECLARED-NOT-APPLICABLE in the order's preflight |

**What worked:** using the producer's own `method_row_probe` instead of hand-building a thresholds dict. It
guarantees the thresholds and claims passed to the write are the stamped manifest's, passed the way the mint passes
them — so "only the reason moved" is a property of the real call, not of my reconstruction of it.

**What failed:** one tooling stumble, named in the record: `.tools/aws` is a bash script and Python on Windows
cannot spawn it (`OSError WinError 193`). The read-back's AWS calls were re-issued through the same shim from bash.
No route, role or credential substituted — which is exactly what the order's "never retried by another route"
clause protects.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Trunk gate + packet sha256 | `is-ancestor 780ba55bde` rc=0 (with a control); packet `6fbce1ff…0d064` **equal** to the order's header |
| 0b | Read the packet and **both halves** whole | CTO half §4 names this seat the applier |
| 1 | Ledger opened and committed before any write | 3 legs; a 58-tree union (118 paths) + shared tree first: **zero** open entries on these keys |
| 2 | **Capture — the rollback** | versioning `Enabled`; both ETags/sizes **exact**; both VersionIds equal the packet's; bodies + sha256 outside the repo |
| 3 | Pre-write dry run + diff | 31 cols each way, 0 added, 0 removed, **exactly one** moved; sentence byte-equal → **Branch A** |
| 4 | **The write** — one `emit_method_row(…, upload=True)` | `landed: True`, etag `377d03aa…`, 2 keys, 16:07:38–16:07:40Z |
| 5 | Served read-back + post-write diff | both keys moved; `columns_changed=['income_basis_reason']`, other moved **0** |
| 6 | The mint's verify | `method_row=match` — replicated inline, *not* the full verify (see Decisions 2) |
| 7 | Ledger closed, 3/3 legs proven | then record, proof_of_spec, status flip |

## Verification

```
capture : data.parquet  9c774f3770e82ed5e7e6b2a4ebe3e7d3  11641  hcqKO1hmuZIFPMKZrRF6gw7jS0mY4xnU
          manifest.json 6d5aabdd1e0f3cc9ff2a6c544bd327fd   2037  9mFo70MiWTNgg3u8xC24yvm3pmOsxQw6
          get-bucket-versioning -> {"Status": "Enabled"}

after   : data.parquet  377d03aa0c75a3fa46d95ad0cbbbaa11  11673  FfKGa1ZCCcB9ivKiRs3p_EKDAqHn50_t
          manifest.json 751c333b06821307f3a90dd44d261c4d   2046  VkO5npkFGUaP4tqwlNXluAexIstge20y

diff (measured_at excluded): columns_changed=['income_basis_reason']  other_columns_moved=0
                             added=NONE removed=NONE  31 cols each way
mint    : num_rows==1 -> 1 | method_version -> [3] | all five *_claim -> ['absent']  => method_row=match

DB69-1-AC1 PASS
DB69-1-AC2 PASS
```

---

## Decisions Made

1. **Treated the capture as a gate, not a formality.** Every value was compared to the packet's section 2 *before*
   the write, and the arms are demonstrably distinguishable on this very partition: the 10:38Z act's own record
   shows a different prior ETag (`7b70c246…`) and 29 captured columns, so these keys do move under other acts. An
   extra continuity check fell out of it — my captured `data.parquet` sha256 is **byte-identical** to the ~98
   record's `served_after` sha256, so what I captured is exactly what that act served.

2. **Did not run the mint's full `--verify-served`.** The method-row check is *inline* inside `verify_served()`
   (`:1027-1038`), and the enclosing function reads every `account_return_daily` day key — which this order's BOUNDS
   forbid outright. So I executed its three conditions exactly as written, on the served bytes, and said which I
   did. Running the whole verify would have produced a tidier-looking line by breaking the grant.

3. **Reported `method_row=match` only as the output of the mint's own expression**, with each of its three
   conditions printed separately rather than collapsed into one boolean. The order is explicit that the literal
   goes in only if that is what was read.

4. **Read the sentence on three surfaces** — the pre-write dry run, the served parquet, and the served
   `manifest.json` — byte-comparing each to the signed text. The manifest carries the same row, so checking only
   the parquet would have left half the blast radius unverified.

5. **Named the `.tools/aws` tooling stumble in the record** rather than quietly re-routing. On a SERVED overwrite,
   "I used a different path to make the call" is exactly the kind of detail that must not be invisible.

---

## Files Modified

| File | Change |
|------|--------|
| `.../task-orders/IRPT_DASHBD.TO-DB-b-130.income-reason-apply.md` | `<status>` → complete (1 line) |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/METHOD_ROW3_REASON_APPLY.json` | new — the record the order requires |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/IRPT_DASHBD.TO-DB-b-130…proof_of_spec.json` | new — VALID rc=0 |
| `org/critical_paths/change_management/20261011T1602Z_irpt-dashbd-db-b-130-…md` | opened before the write, 3 legs proven, CLOSED |
| `org/critical_paths/.open_deploys/irpt-dashbd-db-b-130-…json` | opened then cleared by the close |
| `org/tier2_senior/0.7.0_AE_CloudOps~CB2/logs/2026-10-11/` | this log |

**S3: exactly 2 objects overwritten**, both in the grant. `s3_writes: 2`. No delete of any key or version. No day
key, sidecar, 49F object, other partition, Lambda, role, schedule or Terraform touched. No push of a trunk.

---

## Blockers

**None.** The verifier's read-back is `2.0.0_SA_COO~C2`'s per the COO half §5 and the packet §7 — the pair's other
side, not this seat's. Nothing is waiting on me.

Carried from earlier today, all owned elsewhere: `D2-S95` disarm (issuer), `CB62bj1-AC3` at L9 (CVO), `D2-S92` and
`D2-S103` (CTO), `D2-S99` — resolved, the `--gate-refused` flag now exists.

---

## Current State

Four orders complete today across two projects: ADVI_COTBKF `CB-al-2`, `CB-bi-2`, `CB-bj-1`, and IRPT_DASHBD
`DB-b-130`. Cottonwood's served method row now states the method-worded income reason; its prior version is
retained as the restore point.

---

## Next Steps

1. `[2.0.0_SA_COO~C2]` The verifier's read-back of the two keys, per the COO half §5.
2. `[2.0.0_SA_COO~D2]` Round 69's close; the report is sent with the commit.
3. `[0.7.0_AE_CloudOps~CB2]` Nothing. Idle on the watcher.
