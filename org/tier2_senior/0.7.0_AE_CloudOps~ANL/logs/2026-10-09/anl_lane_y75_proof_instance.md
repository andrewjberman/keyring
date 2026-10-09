# The Y75 proof instance lands, and the AMENDMENT 1 re-run turns 3a and 4 TRUE — 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-09
**Task Order:** IRPT_BCKEND.TO-APPLY-Y75.release5b-test-admit-readback-cleanup-laptop (RE-ADDRESSED), and ADHOC.irpt-anlreq-y1-laptop-reads-3-5 AMENDMENT 1
**Status:** COMPLETE for both acts this lane was given; read 5 of the amendment is UNMEASURABLE and says so

**archetype:** VALIDATE

---

## Objective

Two acts, in the order the issuer set. First: write the Y75 proof-of-spec instance for a cleanup the
BASE seat had already performed — this lane deletes nothing and only proves. Second: re-run reads 3a,
4 and 5 of the IRPT_ANLREQ spec on a FRESH request whose retention row is not the shared one that
blocked the first pass.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-to | `comp-to ADHOC.irpt-anlreq-y1-laptop-reads-3-5` | PASS | session TO id bound race-free per seat+session |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py --self-test` | PASS | **59 of 59 arms behaved**, run BEFORE the instance was trusted to it |
| proof-of-spec-check | `... <instance> AC1 --governing-order <order>` | PASS (as an instrument) | did exactly its job: refused my first draft on 3 schema violations + 2 order-side ones, and refused a renamed control order by RULING S. Final state: clean on every field this lane owns, 2 violations remaining, both in the issuer's file |
| comp-iam | — | SKIPPED | the order declares it DECLARED-NOT-APPLICABLE (no identity change; the laptop's decrypt on key 7f4d3042 is the reason for the route) |
| comp-schedule | — | SKIPPED | order declares DECLARED-NOT-APPLICABLE |
| comp-pipescript / comp-blast | — | SKIPPED | AE minimum binds before a gold-run trigger or an infra change; this lane ran neither |

**What worked:** `proof-of-spec-check --self-test` is the model instrument — it refuses red-first and
prints N of N, so the verdict beneath it means something. Its violation text named both sides of every
mismatch, which is what let the cell-id problem be localised to two tokens in minutes.

**What failed:** nothing failed, but two refusals are worth recording as *correct* behaviour that cost
a cycle each: (1) the broker's 150-word cap refused two completion messages, correctly — the fix is to
cite the commit rather than restate it; (2) the checker refuses a `--governing-order` that is untracked
or renamed (RULING S), so the "corrected control order" experiment is structurally unavailable. That is
the right call and it is why this log reasons from the checker's printed strings instead.

**Gap found:** none new. The comp-rail false positive on a scratchpad path outside the checkout is
already recorded in this lane's earlier log today.

---

## Deployment Sequence

Not applicable to this lane: **READ-ONLY by re-address.** Nothing was built, applied, deleted, tagged or
deployed, and no deploy ledger was opened, because no deploy occurred. The act this instance proves was
performed by the BASE seat `0.7.0_AE_CloudOps` at 10:10Z, ledger closed `1299ad2367`.

---

## Verification

### 1. The Y75 proof instance

Order verified against its cited pin first: disk sha256 of the order == `git show 61db47009f:<order>`
sha256 (`2981b789b35b…`), with a positive control reading a known file at the same pin.

AC1, run **verbatim** from the order: `VERSIONS_LEFT=0`.

Independently re-verified live, read-only:

| measurement | result | denominator |
|---|---|---|
| named DDB rows NOT_FOUND (`ConsistentRead`) | 7 of 7 | 7 ddb keys in `Y75-1_admit_keys_v3.json@4bcebfcb09` |
| named S3 keys with 0 versions on an EXACT-key re-list | 2 of 2 | 2 s3 keys, 2 declared `s3_versions` |
| delete markers on those keys | 0 | — |
| `sweep_extra` | 0 | — |
| keys-file counts | 7 ddb + 2 s3 = 9, table `irpt-requests`, bucket `opal-data-irpt` | the numbers the order fences on; any other count is a STOP |

**Four controls, because a zero must be a true absence:**
1. **Exact-key absence is real** — the same `list_object_versions` client on the same bucket, run
   UNSCOPED, still returned 5 versions. A zero on the two named keys is therefore an absence, not a
   blind lister.
2. **DDB absence is not replica lag** — every read `ConsistentRead=True`.
3. **Ledger cross-check** — the base seat's result file hashes to
   `26fbc10f0f87a83060d67c5ec07551c7ebf0c5d3e70659404ddc2e2d5da0e638`, equal to the sha the CLOSED
   ledger entry records for its CLEANUP leg. Two independent reads of the same bytes.
4. **Nothing stranded** — union read of `org/critical_paths/.open_deploys/` across every live worktree
   HEAD (`git worktree list --porcelain`, then `ls-tree` per tree): 19 files over a denominator of 1
   worktree, and NONE names Y75. Used `ls -a`, not `ls -1`, so `.unindexed_red_state.json` could not
   hide; it is present and does not name Y75 either. Positive control: the exact path
   `irpt-y75-amend2-cleanup-laptop-20261009.json` existed and was removed by `1299ad2367`.

**The instance is committed and is NOT yet VALID — and the cause is not in the instance.**
`proof-of-spec-check` reads clean on every field this lane owns: schema clean, invocation alignment
1/1 with 0 divergences, deploy-genre `3 of 3 named controls discriminate, 0 DID-NOT-DISCRIMINATE,
rollback named`. It refuses on two tokens in the ISSUER's order file:

```
line 15   <owned_cells>APPLY-Y75</owned_cells>
line 111  <criterion id="AC1" cell_refs="APPLY-Y75">
```

dell2's own decomp AMENDMENT (`2.0.0_SA_COO~Y2`, ~10:5xZ) registered that cell as `IB-ya-751` —
verbatim: *"an id matching CELL_ID_RE, so `proof-of-spec-check` and `to-decomp-ref-lint` can join
it. Same cell, same scope."* The Y75 order was re-addressed at ~14:5xZ and kept the old spelling.
Amending task-order criteria is the issuer's act (CLAUDE.md rule 27), so **this lane did not touch the
order** and sent the exact two-line fix instead.

### 2. AMENDMENT 1 re-run — reads 3a, 4, 5 on `REQ-4b5155ac2ea9467ab771b414`

Same spec `@66b6d08b9c`, same method (direct invoke with the front door's event shape, the request's
real owner replayed from its stored record — an `OPAL_GLOBAL` subject in home firm `opal-capital`
selecting data firm `49financial`). Existing principals only; zero writes.

| key | value |
|---|---|
| 3a | **true** |
| 3a_link_expiry | 2026-10-09T15:37:04Z |
| 4_record | **true** |
| 4_route | **true** |
| 5 | false |
| 5_outcome | ANALYSIS_REPORT_NOT_READY |

**3a is now EXERCISED, not merely attempted.** The route signed; the link was fetched; its 37 bytes
were hashed IN MEMORY and `sha256(bytes)` equals the artifact sha the route bound. The link was
discarded — it is in no file and no message. The first pass could not reach this at all.

**Read 4 is fully proven for the first time, both limbs** — the stored record's `ticket_id` and the
composition route's `ticket_id` both equal `TCK-20261009-a1052909`. In the first pass the route limb
was masked by the retention refusal. Per the spec, this limb also grades IRPT_BCKEND TO-APPLY-Y77
read 5a.

dell2's premise held: the fresh request's chain walked principal-free is COMPLETE and live
(`REQUEST_COMPOSITION -> NORMALIZED_PORTFOLIO -> ORIGINAL_HOLDINGS`, all RESERVED, ~30 days
remaining). The first pass's single cause is gone.

**Read 5 is not answerable, and that is reported as such rather than as a bare false.** The job never
left `RECEIVED` across a 450-second read-only poll (5 polls, 90s apart), so the amendment's READY
precondition was never met; the pdf route refuses `AnalysisUnavailable: ANALYSIS_REPORT_NOT_READY`,
which is upstream of the PDF-retention branch. Whether a PDF is retained for this request is
UNMEASURED.

Why it is not merely a slow queue, over a printed denominator:

| state | count | note |
|---|---|---|
| `RECEIVED` / outbox `SENT` | 6 of 8 | accepted 44–390 min before the read |
| `READY` | 1 of 8 | `REQ-5e4149d2`, accepted 223 min before the read |
| `ATTENTION` | 1 of 8 | accepted ~9.9 days before |

**Four of the six RECEIVED jobs are OLDER than the one job that did reach READY.** Every one of the 8
carries `outbox_state SENT`, so the `analysis_generate` message was dispatched and dispatch is not the
gap. Positive control: `REQ-5e4149d2` reads READY, so the generate path CAN complete and the zero is
not a blind instrument. This seat did not touch the worker and makes no claim about why it stops.

### 3. Identity hygiene, both acts

| arm | result |
|---|---|
| email-shaped strings in every file written | 0, with a POSITIVE CONTROL proving the detector fires (1 hit on a planted string) |
| signed links / urls | 0 |
| non-ASCII | 0 |
| raw principal ids or record bodies | 0 |
| AWS writes | 0 — every call a read; a scan for every mutating verb across the session's scripts returned no matches |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Committed the Y75 instance although it does not yet validate | It is valid on every field this lane owns; the issuer needs the artifact to flip against, and the blocker is named precisely. Withholding it would have blocked the issuer on nothing |
| Did NOT edit the issuer's order to fix the two cell-id tokens | Amending task-order criteria is the issuer's act (rule 27). "Surface, do not adjudicate" — the fix is two tokens and was sent as such |
| Abandoned the corrected-control-order experiment | The checker refuses an untracked/renamed `--governing-order` by RULING S. The checker already prints both sides of the mismatch, so the control added nothing a string comparison does not already settle |
| Reported read 5 as `ANALYSIS_REPORT_NOT_READY`, not as `false` alone | Could-not-verify is a finding. A bare false would read as "the pdf route misbehaved" when the route is answering correctly about a report that does not exist yet |
| Measured the job-state distribution before calling read 5 blocked | A single `RECEIVED` is indistinguishable from "not yet". The age-ordered census over 8 jobs is what makes it a blocker rather than a wait |
| Did not wait longer than 450s for READY | Four jobs older than a completed one are still RECEIVED, so more waiting was not evidence-bearing. Named the owner instead |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/IRPT_BCKEND.TO-APPLY-Y75.release5b-test-admit-readback-cleanup-laptop.proof_of_spec.json` | new; sha256 `59ecf25d73765098d89dcc00d05fee3adbadf6cfdccfb7981168ce1883d694ea`, 7407 bytes | Yes — `4ae87b336a` |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y1_laptop_reads_3a_4_5_rerun_result.json` | new; sha256 `7332978a5fe6a97e639e9c39f94092727cbc81d71cd3b87d7dab2531e139d52f`, 5641 bytes | Yes — `60cfbecb26` |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/logs/2026-10-09/anl_lane_y75_proof_instance.md` | this log, named by the instance's `session_log` field | pending this commit |

NO AWS resource, policy, object, table row or Lambda was created, modified or deleted by this lane.
The Y75 task order was NOT edited and its `<status>` was NOT flipped — the issuer reserved that.

---

## Blockers

None on this lane's own acts; both are delivered.

Two items are owned ELSEWHERE and were routed, not chased:

- **The Y75 flip** needs `APPLY-Y75` -> `IB-ya-751` at lines 15 and 111 of
  `org/tier2_senior/0.7.0_AE_CloudOps~ANL/task_orders/IRPT_BCKEND.TO-APPLY-Y75.release5b-test-admit-readback-cleanup-laptop.md`.
  Owner `2.0.0_SA_COO~C`. Sent 15:27:12Z.
- **Read 5** — ~~needs a job that reaches READY~~ **RESOLVED AND CLOSED, no re-run** (issuer msg
  108039, 16:13:18Z, relaying dell2 `2.0.0_SA_COO~Y2` msg 3624 via `0.0.0_AB_MSTR` msg 108035).
  dell2 states the resident worker is **alive** and refuses `REQ-4b5155ac` with
  `CLOSED_COMPOSITION_REQUIRED` because its packaged schema predates `ticket_id` — carried as row
  `IRPT_ANLREQ-D2-S15`. dell2 G2's release 4 holds the fix and does a ticket-bound read itself.
  Reads 3a and 4 are ACCEPTED and the order's work is complete on this side; the status flip is the
  issuer's.

  **What this corrects, and what it does not.** This lane's measurements stand unchanged — 6 of 8
  jobs at `RECEIVED`/`outbox SENT`, four of them older than the one that reached READY, every one
  dispatched, `REQ-5e4149d2` READY as the positive control. What this lane deliberately did NOT
  claim was the cause: the result file says in so many words that it "did not determine why the
  worker stops at RECEIVED". That restraint was right — the true cause is a packaged-schema gap in
  the worker, which is invisible from the job table this lane could read, and a confident guess from
  `RECEIVED` alone ("the worker is stuck" / "not running") would have been wrong. The symptom was
  measured; the mechanism was dell2's to name.

  The delivered artifact `Y1_laptop_reads_3a_4_5_rerun_result.json` (sha256 `7332978a…`) is
  **deliberately left unmodified**: it is accurate as written, the issuer already holds that hash,
  and row `IRPT_ANLREQ-D2-S15` is the canonical carrier for the cause. Re-hashing an accepted
  deliverable to add a pointer would cost the issuer a re-record and buy nothing.

---

## Current State

Lane `0.7.0_AE_CloudOps~ANL` is LIVE on `box/laptop`, one inbox watcher armed, zero crons, inbox
drained and every message acked (107947, 108008, 108019). Both delivered artifacts are committed:
the Y75 proof instance `4ae87b336a` (AC1 `VERSIONS_LEFT=0`; flip waits on two cell-id tokens in the
issuer's order) and the AMENDMENT 1 re-run `60cfbecb26` (3a, 4_record and 4_route all TRUE; read 5
blocked at job state `RECEIVED`, re-read on the issuer's word). The lane's earlier order
`ADHOC.irpt-anlreq-y1-laptop-reads-3-5` first pass is `complete` at `2315575398` with its log at
`bac276f594`, both ON ORIGIN. Zero AWS writes across the whole session.

---

## Next Steps

1. **[0.7.0_AE_CloudOps~ANL] Event-driven hold** — act on the next `[INBOX]` event the same turn;
   re-arm the Monitor on each `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. **[2.0.0_SA_COO~C] Fix the two cell-id tokens and flip Y75** — `APPLY-Y75` -> `IB-ya-751` at
   lines 15 and 111. The instance validates on everything else.
3. ~~**Route the stuck generate worker**~~ **CLOSED 16:13:18Z** — not a stuck worker: a packaged
   schema predating `ticket_id`, row `IRPT_ANLREQ-D2-S15`, fixed in dell2 G2's release 4. No re-run
   of read 5; reads 3a and 4 accepted. Nothing further owed by this lane on that order.
4. **[2.0.0_SA_COO~Y2] Settle `5_outcome`'s domain** — still open. Two observed members fall outside
   it (`RETENTION_RECORD_UNAVAILABLE`, `ANALYSIS_REPORT_NOT_READY`) and dell2's own diagnosis names a
   THIRD refusal this lane never reached (`CLOSED_COMPOSITION_REQUIRED`), so the pdf route has at
   least four distinct paths before it signs and the declared domain holds two.
5. **[0.0.0_AB_MSTR] Carry `4ae87b336a` and `60cfbecb26` to CLOUD** at the next `box-sync`; this
   seat does not push `box/laptop`.
