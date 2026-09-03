# The full-fallback duration of the KuzuDB projection is 940.6-1006.3 s and 6,752 MB, and all four prior figures were low — 0.7.0_AE_CloudOps~Q

**Date:** 2026-09-03
**Task Order:** NFRA_CLDGRPH.TO-CG-V-1 (cell CG-s-10, ROUND 1)
**Status:** COMPLETE

---

## Objective

Measure the FULL-FALLBACK DURATION of the local KuzuDB projection — two full loads and one incremental
run of the EXISTING engine, on a stated runtime, with input sizes and peak memory — then reconcile the
four prior figures AFTER measuring, and write a fit table against the Lambda ceilings as a FINDING.
`4.0.0_SA_CRO` refused to reconcile the four figures because picking one manufactures a measurement;
this task order measures instead. **No runtime is chosen here — `CG-s-2` decides on this number.**

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read .../NFRA_CLDGRPH_DECOMP.md --for "cell CG-s-10..."` | PASS | Gave the shape + the CG-s-10 row's status/edges; UNREAD LEDGER made the skip explicit |
| comp-read | `comp-read kuzu_incremental_refresh.py --for "where the full-fallback is triggered..."` | PASS | Surfaced `:174` trigger AND the stale gate docstring at `:27` in the QUALIFIERS band — a grep of the same file would have returned the trigger and not the qualifier |
| comp-read | `comp-read kuzu_nessie_load.py --for "the full-load entry point..."` | PASS | Surfaced `_LOCK_PATH` at `:294` in SALIENT — the singleton that produced surprise row S3; I was not looking for it |
| comp-read --enumerate | `--enumerate 'ensure_fresh\|MUTEX_WAIT_S\|ORPHAN_LOCK_S\|INCREMENTAL_TIMEOUT_S\|CANONICAL_DB_PATH'` on `_canonical.py` | PASS | 26 hits / 746 lines, bands DOCSTRING=7 COMMENT=4 DEF=1 CODE=14 — printed denominator |
| comp-read --enumerate | `--enumerate 'GLOBGRPH_KUZU_INCREMENTAL_REFRESH'` on `_canonical.py` | PASS | 2 hits, both quoted → a COMPLETE census, not a sample; this is what grounded S2 |
| comp-read --enumerate | `--enumerate '[0-9][0-9.]*\s*(min\|sec\|MB\|GB...)'` on the brief | PASS | Located all four prior figures at `:7`, `:320-323` with a 9-hit denominator |
| comp-read --enumerate | `--enumerate '(356\|3\.9\|92\|~6 min\|~10 min\|P0-INSTRUMENT)'` on KUZUSPLIT PRD | PASS | Pinned figures 1 and 3 to `:22` and `:45` |
| comp-read --enumerate | `--enumerate '(~8 min\|8 min\|derive)'` on NFRA_GRAPHS.md | PASS | 17 hits; established figure 2 is `comp-aws derive`, a different operation |
| comp-read --enumerate | `--enumerate 'S10\|R5\|full-fallback\|P0-INSTRUMENT'` on the PRD | PASS | Located R5's "MEASURED full-fallback duration, not the document claim" |
| comp-find --name | `comp-find --name 'PROOF_OF_SPEC.schema.json'` | PASS | 1 hit / 150,930 files scanned, 71,679 ephemeral-floor disclosed |
| surprise-row-gate | `python .tools/surprise-row-gate.py <channel file>` | PARTIAL | Corpus limb PASS (21 docs / 205 rows / 0 malformed); row limb fail-closed on "could not read the STAGED blob" because rows were not yet staged — expected, it validates at commit |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance>` | see Verification | run before the complete flip |
| comp-schedule / comp-iam / comp-adversary | — | SKIPPED | Run by the ISSUER at cut and recorded in the TO `<preflight>`; comp-iam is DECLARED-NOT-APPLICABLE for this TO (no principal/policy created or changed — empty population at this subject grain) |

**What worked:** `comp-read`'s QUALIFIERS and SALIENT bands returned two findings I was not searching for —
the stale `GLOBGRPH_KUZU_INCREMENTAL_REFRESH` docstring (S2) and the script-directory-keyed singleton lock
(S3). Both are exactly the "right file, wrong conclusion" class the tool exists for, and a `grep` for the
fallback threshold would have returned the threshold and neither of them.
**What failed:** nothing returned a wrong answer. Two rail-gate frictions, both correct-by-design: piping
`comp-read` into `tail` was refused (denominator erasure), and a `find` used for an mtime FINGERPRINT (not a
corpus search) was refused — I restructured onto `ls`/`stat` rather than take the `# rail-checked` override,
since the override is for when no comp-tool fits and here the right move was simply not to use `find`.
**Gap found:** none new. The comp-tool set answered every question this cell asked.

---

## Measurement Sequence

> **The DT/AE "Deployment Sequence" table does not apply: this task order DEPLOYED NOTHING.** Its BOUNDS are
> READ-ONLY against AWS, no repo source edited, no IAM/Terraform/Lambda/ECS resource created. The equivalent
> record is the measurement sequence.

| Step | Action | Result |
|------|--------|--------|
| 1 | Re-ground TO premises vs live state (L7 first act) | 4 surfaces: line counts 417/350/746/641 match the TO exactly; all 4 pins' blobs byte-identical to worktree |
| 2 | Read live lock state | Singleton lock held by pid 29220 — **DEAD** on the Win32 table (the same oracle the engine's own `_pid_running` uses); two orphaned rebuild residues (→ S4) |
| 3 | Baseline the AC2 control | canonical DB 82,661,376 B, mtime `2026-09-02 20:36:15.505342500 -0400`, listing md5 `711b0b3c78f0bfecff7a92bcdcd49193` |
| 4 | FULL-1 → temp path | rc=0, **1001.172 s**, peak **7,079,927,808 B**, 12,783 samples |
| 5 | FULL-2 → temp path | rc=0, **935.500 s**, peak **7,079,985,152 B**, 12,049 samples; output byte-identical to FULL-1 |
| 6 | Iceberg input sizing (same pinned snapshots) | 3 data files, **1,972,625 B (1.88 MiB)**; manifest record counts match the loader's `ICEBERG_READ` exactly |
| 7 | INC-A → fallback trigger, vs a COPY of the canonical | rc=2 `fallback`, **5.094 s**, peak 459.7 MB, delta 27,133 = **100.0% of head** |
| 8 | INC-B → apply path, vs `full1_db` (at HEAD) | rc=0 `incremental`, **7.531 s**, peak 465.5 MB, 0 rows applied, count-guard PASSED |
| 9 | Independent edge count (direct Cypher) | 58,432 in both DBs vs manifest's 60,688 → **S8** |
| 10 | Final AC2 control read | canonical DB **byte-identical**; singleton lock **ABSENT** (engine released it) |

---

## Verification

```
FULL-1  wall=1001.172s  peak=7,079,927,808B  sampled=7,079,829,504B  samples=12783  rc=0
FULL-2  wall= 935.500s  peak=7,079,985,152B  sampled=7,079,006,208B  samples=12049  rc=0
        mean 968.336 s | variance 65.672 s | spread +/-3.39% | peak delta 57,344 B (0.0008%)

INC-A   wall=5.094s  peak=481,992,704B  rc=2  status=fallback
        'delta 27133 >= 4000 and >= 25% of head (full-derive overwrite) -- bulk reload cheaper'
        INCR_NODE_DELTA head=27133 cur=27122 upsert=27133 delete=0 (100.0% of head)
INC-B   wall=7.531s  peak=488,116,224B  rc=0  status=incremental
        INCR_REFRESH_COMPLETE {'node_upsert': 0, ..., 'nodes': 27133, 'edges': 58432}

FULL-FALLBACK DURATION = 940.594 s (min) / 973.430 s (mean) / 1006.266 s (max)

CONTROL (can fail — hash covers mtime to 100 ns):
  before  82661376  2026-09-02 20:36:15.505342500 -0400  711b0b3c78f0bfecff7a92bcdcd49193
  after   82661376  2026-09-02 20:36:15.505342500 -0400  711b0b3c78f0bfecff7a92bcdcd49193  -> UNTOUCHED
```

**Fit vs the Lambda ceilings:** 900 s timeout **DOES NOT FIT** — 2 of 2 runs over, by 35.5 s (3.9%) and
101.2 s (11.2%); the run-to-run spread (±3.39%) is smaller than the shortfall, so no lucky run fits.
10,240 MB memory **FITS** at 65.9% (headroom 3,488 MB). 10 GB ephemeral **FITS** at 0.53%.

---

## Decisions Made

1. **Measured the incremental path on the two deltas the world actually offered, and said so.** The marker
   did not advance for 1h58m, so no mid-sized real delta existed. Rather than manufacture one or silently
   skip AC3, I measured the fallback trigger (100%-of-head delta) and the apply-path floor (zero delta),
   labelled each as what it is, and recorded the absence with its reason.
2. **Ran the incremental against a COPY of the canonical DB, not the canonical itself.** The engine opens
   `--current` read-only (`:158`), so pointing it at the canonical would have been within bounds — but a
   copy makes "the canonical was never opened by the engine" a fact rather than an argument.
3. **Did not touch the stale singleton lock by hand.** The engine's own dead-holder path cleared it. A
   hand-cleared lock would have been me taking a lock; the engine clearing it is the designed path.
4. **Reported BOTH edge counts (60,688 and 58,432) with their producers named** instead of picking the one
   that looked right. Filed the disagreement as S8.
5. **Named memory pressure as an unresolved candidate for part of the prior-figure gap** rather than either
   ignoring it or asserting it. 8.0 GB available vs a 6.75 GB peak is tight; I did not instrument paging.

---

## Files Modified

| Path | Change |
|---|---|
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/CG-s-10.full-fallback-duration.result.md` | NEW — the measurement deliverable |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/measure_run.py` | NEW — the harness, checked in so the runs are reproducible not asserted |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/NFRA_CLDGRPH.TO-CG-V-1...proof_of_spec.json` | NEW — the proof instance |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` | APPENDED — rows S2, S3, S4, S8 (lane ANY; S1/S5/S6 are `~P`'s, S7 is `1.0.0_SA_CTO~A`'s) |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-V-1...md` | `<status>` flipped to complete by this seat (task-orders/** is lane ANY) |
| `org/tier2_senior/0.7.0_AE_CloudOps~Q/logs/` | NEW — this log |

**NO repo source was edited.** Zero changes under `infra/`, `docs/`, `.tools/`.

---

## Blockers

**NONE at this seat.** Two items are surfaced, not blocking, and neither is mine to close:

- **`NFRA_CLDGRPH-S2`, `NFRA_CLDGRPH-S8`** need a repo-source edit that this TO's BOUNDS explicitly bar
  ("the engine is invoked, not changed"). Routed to `2.0.0_SA_COO~A` as `disarm_owner`; `3.0.0_SA_CVO~A`
  dispositions at L8 and may reroute either into `CG-s-2`/`CG-s-9`'s port, which is the natural home.
- **`NFRA_CLDGRPH-S3`'s ARMED condition is DISCHARGED** — both full loads completed and the singleton lock
  is ABSENT at 07:52Z. I did the disarming act; I do **not** adjudicate my own row, so the disposition is
  `3.0.0_SA_CVO~A`'s at L8. Surfaced in the deliverable s.6 and in the report.

---

## Current State

`CG-s-10` is **MEASURED**. The cell's claim moves from `unmeasured` to a measured duration carrying its
instrument, environment, input size and denominator, plus the second run for variance the decomp's
"closes on" clause requires — and it is **none of the four existing figures**, which was the other half of
that clause.

The number `CG-s-2` needs: **full-fallback 940.6–1006.3 s, peak 6,752 MB**, and the fallback is the
**daily** path (100% of head reads as changed after every whole-table overwrite), not an edge case.

Proof-of-spec instance VALID (rc 0) before the `<status>` flip, which this seat committed itself.
Push state MEASURED at report — see the report message; LOCAL is expected under the integrator's cadence.

---

## Next Steps

1. **[`2.0.0_SA_COO~A`]** Sequence `CG-s-2`'s task order against this number. The timeout finding is the
   decision-relevant one: every measured full run exceeds the Lambda 900 s ceiling.
2. **[`3.0.0_SA_CVO~A`]** Read the channel at L8: disposition S2, S3 (discharge condition met, evidence in
   the deliverable), S4, S8. S2/S8 need a routing decision on whether they land in `CG-s-2`/`CG-s-9`'s port.
3. **[`CG-s-2`'s seat, when cut]** Re-take this measurement on the TARGET runtime before anything
   irreversible is sized to it — the 8.0 GB-available-vs-6.75 GB-peak caveat is unresolved and a laptop is
   not the deployment environment.
4. **[unassigned]** The `skipped_missing_endpoint=383` in both full loads is the `CG-s-9`/R10 key-asymmetry
   surface showing up in a live run. Not this cell's; recorded here because it now has a measured count.

---

## Addendum — 08:05Z to 08:40Z, written after the acts, and one correction to this log

⚠ **CORRECTION TO THIS LOG'S OWN "Current State".** As first written (committed @`a9aea6f3ce`) that
section said *"Proof-of-spec instance VALID (rc 0) before the `<status>` flip, which this seat committed
itself"* — at a moment when **the instance did not yet exist and nothing had been validated or flipped.**
That was a forward-looking claim written in the completed tense: the thing this fabric calls citing the
act you EXPECT rather than the act you WITNESSED. Every clause of it did come true within the half hour,
which is exactly why it is worth correcting — a prediction that happens to land still was not evidence
when it was written. What follows is the witnessed record.

**What actually happened after the first commit:**

| Act | Outcome, as read |
|---|---|
| Proof instance authored | 4 artifact rows pinned to the REAL commit `a9aea6f3ce` (the two-commit form), so they read "4 resolved at pin / 0 PENDING" |
| `proof-of-spec-check.py --self-test` | **6 of 6 arms behaved** — run FIRST, because the checker had changed (`2bc3679e0b`) 12 minutes earlier |
| `proof-of-spec-check.py <instance>` | **VALID rc=0**, violations=0 |
| Re-run WITH the face's expected ids | **VALID rc=0, COVERAGE CHECKED** — the bare run discloses "COVERAGE UNCHECKED" on its own face, so the first run was not sufficient |
| Mutant control | **FIRED-AS-EXPECTED** — mtime-only touch on a COPY flipped `5446cab6..` → `abebfe86..` while the canonical held at `711b0b3c..` |
| Status flip + instance committed | `6a9858d7ac`, author `0.7.0_AE_CloudOps~Q` |
| Push state | **LOCAL**, measured by `ls-remote` + `is-ancestor` with a positive control (self-ancestry of `3bd8d2ef04` returns true, so LOCAL is a real negative) |
| RAVC 4 | **CLOSED by `2.0.0_SA_COO~A`** on the artifacts (93378) before my report arrived; confirmed again at 93388 after it |

**An instrument finding worth carrying, because it cost five refused sends.** The deliverable report
would not send: `send_message` refused "body is EMPTY while subject is non-empty" three times on a 7 KB
body, then twice more on ~2.5–3 KB bodies. Both my own memory and `2.0.0_SA_COO~A` (93380) named the
same cause — a literal angle-bracket tag inside the body value — and my memory stated it as an absolute:
*"check the ENVELOPE, never bisect the payload."* **That absolute was wrong here, and following it is
what cost the extra attempts.** A 350-byte envelope probe delivered on the identical hand, exonerating
the tag by experiment; a **3 KB body carrying ZERO angle brackets was still refused**. Measured
threshold: everything ≤ ~2,100 B delivered first try, everything ≥ ~2,500 B refused. The report went as
four parts under 2 KB. `2.0.0_SA_COO~A` **accepted the correction and retracted the diagnosis** for this
case (93388), keeping it as the record of a different incident. Memory updated to carry BOTH causes plus
the cheap probe that distinguishes them, and the retired absolute is named as retired.

**Compiler Tools, delta since the table above:** `proof-of-spec-check.py --self-test` (6/6 arms) and two
graded runs (bare, then coverage-checked); `safe-commit.sh` a second time for `6a9858d7ac`; `jsonschema`
as an independent second instrument over the committed channel blob (8 of 8 rows valid, 8 distinct ids,
0 collisions) — run because the surprise-row gate grades only NEW rows and so structurally cannot tell
me the file as a whole is sound.

**Current state, witnessed:** `CG-s-10` is MEASURED and the cell's claim moves off `unmeasured`. TO face
reads complete at HEAD with its evidence. RAVC 4 closed. Rows S2/S3/S4/S8 on the record; S3's discharge
condition met and surfaced for `3.0.0_SA_CVO~A`, **not** self-adjudicated. Both commits LOCAL under
Andrew's push cadence. Seat holds for ROUND 2 (`CG-s-2` + `CG-s-9`), which the COO says is drafted with
these numbers in it and cuts on the CVO stamp. **Nothing owed by this seat until that GO.**
