# CTO ADJUDICATION -- NFRA_OUTSET round 2, S16 and S17: the seam the consumer never looks at, and the publish nobody schedules

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-09 ~13:3xZ · **On:** `2.0.0_SA_COO` 94479 (drive tick 3), substrate
`0.7.0_AE_CloudOps~W`'s report 94478 and rows S16/S17 · **Read at:** HEAD `3a404545f2` + the OUTSET tree at `cb43d05200`.
**Prior in this chain:** ROUND_ANALYSIS.round1 @`a0500abe18` (COMMITTED is not SERVED; naming a cost is not assigning it);
the CG-s-8 rulings @`622ffb9631`, @`1266d65641` (a channel row records that something is TRUE; a manifest row makes it
someone's WORK). **Authority for the timing:** Andrew-direct at this terminal 2026-09-09 ~12:5xZ -- *"any work that can be
adjudicated or pushed forward on NFRA_CLDGRPH and NFRA_OUTSET, by all means go ahead"* -- and the spine: mid-round the
spec is FROZEN, so these rulings PLACE rows for the L10 addendum and cut nothing now.

**Verified at this seat before ruling (grain + coverage, the cost of a wrong ruling is another seat's cut):**
`infra/aws/terraform/estate-report/instance.tf:83` `user_data_replace_on_change = true`; the `runtime.env` heredoc at
`:130-151` sets no `ESTATE_OUTSET_SEAM_PREFIX` (0 hits in the file); `estate_report_runner.py:1611` reads it unset =>
not configured, `:1643` `OUTSET_SEAM_MAX_AGE_HOURS = float(os.environ.get("ESTATE_OUTSET_SEAM_MAX_AGE_HOURS", "26"))`,
`:1810-1846` `_stratum_propagation` returns `INSTRUMENT_UNAVAILABLE` with no seam configured; the PRD's manifest at
v0.3 ends at OS-s-19, so the next ids are OS-s-20 and OS-s-21; PRD s.3 line 185 costs *"a publishing step and a
freshness question per artifact"*.

---

```
+-- CALL 1 of 2 -- S16 --------------------------------------------------+
  **ESTATE_OUTSET_SEAM_PREFIX is unset in the host's runtime.env, so the
  runner's propagation stratum returns INSTRUMENT_UNAVAILABLE and never
  composes a key; setting it replaces the host (user_data_replace_on_change
  = true). Both round-2 orders can pass as written and the served report
  renders exactly as today. Where does the setting live?**
  --------------------------------------------------------------------
  **REC --** a PRD addendum (v0.4) places manifest row OS-s-20 (lane CloudOps,
  verb deploy: set the prefix in runtime.env and replace the instance under
  its own NEVER-2 entry), cut at the round-2 close; NOT folded into OS-s-19,
  because the runner upload and an instance replacement are two irreversible
  acts with different rollbacks. OS-s-19 proceeds meanwhile.
  --------------------------------------------------------------------
  **RULING -- ADOPTED, with three sharpenings.**
  (1) ORDER, and it is a dependency edge, not a preference: OS-s-19 lands
      BEFORE OS-s-20. The host pulls the runner from S3 at boot
      (instance.tf:94-96, "the job code itself is not baked in"), so a host
      replaced before the upload boots the 2026-08-25 runner into a fresh
      instance -- round 1's finding re-manufactured by the fix for it.
  (2) THE ACCEPT READS ON THE SERVED DAY, EXERCISED: on a scheduled 13:00Z
      run of the replaced host, the published report's propagation stratum
      returns an answer state other than INSTRUMENT_UNAVAILABLE with the
      seam artifact's vintage disclosed. The env line present in the live
      runtime.env (an SSM read) is DESIRED -> APPLIED and is a control, never
      the accept. Rule 22 STATE, the same axis as S14.
  (3) THE REPLACE IS SEQUENCED OUTSIDE THE RUN WINDOW and its NEVER-2 entry
      names the host, the pinned runner bytes it will boot, and the rollback
      (the prior AMI/user_data). The mechanism is the estate's as built; a
      different mechanism (a boot-time parameter read that avoids replacing
      the host) is a design change for the addendum's reading, not this
      row's act, and nothing of that kind is built unasked.
+---------------------------------------------------------------------+
```

```
+-- CALL 2 of 2 -- S17 --------------------------------------------------+
  **The seam artifacts were published BY HAND at 13:03:50Z and nothing
  publishes them again; at the 26 h ceiling (~2026-09-10T15:03Z) the seam
  reads STALE -> INSTRUMENT_FAILED. PRD s.3 costed the freshness question
  (answered) and a publishing step (unowned cadence). Who owns the cadence?**
  --------------------------------------------------------------------
  **REC --** the same addendum places row OS-s-21 (lane CloudOps, verb
  build: a scheduled publish of the two producers before the 13:00Z run, on
  the producer's side). "Production pipelines MUST be scheduled" names the
  shape; the moratorium is on alerts and monitors, not a pipeline trigger.
  Until it lands, FAILED after 26 h is the honest state, not a consumer
  defect; no schedule is built unasked.
  --------------------------------------------------------------------
  **RULING -- ADOPTED, with three sharpenings.**
  (1) THE TRIGGER IS THE PRODUCER'S OWN -- a schedule that fires the two
      publishes ahead of the 13:00Z run -- never success-of-upstream as the
      only trigger (CLAUDE.md: that shape is a defect), and never a rule that
      watches the consumer. A pipeline trigger is not a monitor; the
      moratorium does not reach it. Agreed.
  (2) THE ACCEPT IS EXERCISED ON A REAL DAY, WITH A NEGATIVE ARM: the seam
      artifact's vintage precedes that day's 13:00Z run and the served
      report's propagation stratum reads FRESH with age < 26 h disclosed;
      and with the schedule disabled the battery's R5 arm still convicts at
      > 26 h (the 999.0 h mutant), so a green cannot come from a raised
      ceiling. A hand publish is a QA act, permitted, and never the exercise
      -- ad-hoc artifacts are not production evidence.
  (3) DEPENDENCY: a scheduled publish into a prefix the consumer never reads
      is a duplicate output path with a timer on it. OS-s-21's accept is
      gated on OS-s-20's; the two may be BUILT in parallel, and OS-s-21 reads
      EXERCISED only on a day after OS-s-20 has. Order for the L5 recut:
      OS-s-19 -> OS-s-20 -> OS-s-21 on the accept edges; the fan-out is the
      issuer's.
+---------------------------------------------------------------------+
```

## WHERE THESE LAND, AND WHEN

Both rows enter the PRD as **addendum v0.4 at L10 on the round-2 slug**, beside nothing else unless the slug adds it;
`endpoint_outcomes` unchanged (FWD-2, FWD-3, FWD-4 and FWD-7 are what both rows serve). The decomposition and the
two live faces are FROZEN: OS-s-18 flips on its amended paths and OS-s-19 proceeds as cut. The rows S16 and S17 are
the carriers until the addendum lands; this record is what the recut cites.

## ON S18, TOLD AND NOT ASKED -- the design fact, carried, not built

`2.0.0_SA_COO`'s L6 ruling @`cb43d05200` stands: a v3 `<paths>` block is a grant for a `0.9.0_WK_*` serial only;
for a seat the lane registry decides, and the two batteries move into the seat's own deliverables folder. The fact
it exposes for this seat's surface -- *"the `<paths>` block IS the grant" is TRUE for workers and FALSE for
seat-addressed tree orders* -- is exactly FWD-1 of the brief-to-cut chain (an issuer learns AT THE CUT that a face's
grant does not cover what its edits will trip), whose DONE WHEN lines Andrew confirmed today @`6ccebb9ae5`. It is
carried there as a measured instance for that project's L4 and is NOT built now: Andrew's same-session word holds
new work behind the roadmap, and the resolver's clause stays as built until that PRD places it.

## WHAT THIS RULING DOES NOT DO

Amend any FWD · cut a cell · widen a grant · start OS-s-20/21 before the slug · build a schedule, a parameter read
or a gate · grade O18-AC2 (the CVO's at L9) · touch the CLDGRPH placements ruled at @`1266d65641`.

## Push state
LOCAL on commit; origin/CLOUD @`58adeff90c` by this seat's ls-remote at 13:23Z; LD-0522 hold standing.
