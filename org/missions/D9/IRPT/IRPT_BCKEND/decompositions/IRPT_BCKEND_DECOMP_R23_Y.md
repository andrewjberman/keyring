# IRPT_BCKEND round 23 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-29 ~18:2xZ. Trigger: row `IRPT_BCKEND-S218` (@e146a80a3d) and the CTO's decision
102967 **as amended at 102970**. W24 returned ZERO reports: both jobs that reached the vendor, on two tenants and each
run solo, died `ATTENTION SESSION_REFRESH_ALREADY_USED`. Reading `resident_worker.py` showed that code does not mean a
stale session -- `refresh_session()` is reachable only from `step()` on an `eviction_verdict`, so it means the job was
**evicted twice**, the first eviction spending the one admitted refresh. Arm 3 claimed at fence 1 four seconds after
its K5.

The CTO's first decision was a pre-claim session fix. On ~Y's mechanism reading (102968) it **amended**: that remedy
rests on an unproven cause, so the round is ordered **observe, then discriminate, then remedy**. The one-refresh
allowance does not change in any branch -- it exists so a job can never loop on the vendor.

**This round cuts step (1) ONLY.** Steps (2) and (3) are not cells here: (2) is a read this lane performs on the
build once the journal carries the verdict, and (3) is an amendment whose content the reading decides. Cutting a
remedy now would be cutting for coverage, against a cause nobody has measured.

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD HEAD) |
|---|---|---|---|---|---|---|
| `IB-yr-231` | the resident NAMES what it saw: for every vendor call whose `eviction_verdict` matches, journal one line carrying the matched verdict and the job id; and journal the job's terminal ATTENTION with its `job_detail` code. No behaviour changes -- no retry, no allowance, no state | FWD-4 (a window can tell a pre-job session rejection from vendor evictions on every call) | WORLD (the served resident's journal; no served artifact or contract moves) | `~83` | none | `R23_CHECKS/test_r23_y1_eviction_named.py`: `names_the_matched_verdict` FAIL (no such line today), `names_the_job_attention` FAIL (S207: 124 journal lines over W24 carried no ATTENTION), `no_behaviour_change` PASS (control -- the allowance and the refusal codes are untouched) |

**Why observability is the cell and not a rider.** Two windows have now spent their submissions and returned one
report between them, and in both the deciding fact was invisible: W22's `SESSION_REFRESH_ALREADY_USED` and W24's two
were recoverable only from `irpt-jobs`, never from the journal (row `IRPT_BCKEND-S207`, re-confirmed on W24 across 124
lines). A remedy chosen without the verdict would be chosen blind, and the CTO said so when it amended. This cell also
closes S207 as a side effect, which is why S207 is cited rather than cut separately.

**What it must NOT do.** No change to `refresh_session`'s allowance, no new `WorkerAttention` code, no change to which
calls are retried, and no vendor identifier, cookie, URL or exception body in the journal -- the existing
`refusal_line()` discipline holds, and a verdict name plus a job id is the whole payload.

Edges: none; `IB-yr-231` is a single independent cell. **fanout: 1 of 1 chains, cap 8.** Slot maxima (S197 ruling), MEASURED at 18:2xZ: highest author line 81, highest order slot 82, highest
branch 82, so `n = 1 + 82 = 83` -> `~83`. (An earlier draft of this file said `~81` from an unmeasured guess and was
corrected before it landed.)

Acceptance of the ROUND, not of the cell: a solo job on a cold resident, run in the next Analysis window, whose
journal now names either a pre-job session rejection or a per-call eviction. That read is step (2) and belongs to this
lane, not to a worker.
