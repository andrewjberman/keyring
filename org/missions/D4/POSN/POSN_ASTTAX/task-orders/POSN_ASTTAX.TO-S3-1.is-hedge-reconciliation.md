# TO POSN_ASTTAX.TO-S3-1 -- reconcile `is_hedge()` and `HEDGE_TICKERS` against the vocabulary the retag settles, and disarm channel row C-S1 (AT2-s-3, FWD-1)

<to_id>POSN_ASTTAX.TO-S3-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~7</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>superseded</status>
<superseded_by>POSN_ASTTAX.TO-T7-1 -- org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T7-1.is-hedge-reconciliation.md (round 3, cell AT3-s-7; its own header reads "Successor to the never-run TO-S3-1"). THE NEED -- reconcile is_hedge() / HEDGE_TICKERS against the vocabulary the retag settles and record the disarm condition for row POSN_ASTTAX-Z-W1-S1 (disarm_owner 1.0.0_SA_CTO~Z) -- IS CARRIED BY THAT SUCCESSOR. THIS ORDER NEVER RAN: worker 0.9.0_WK_POSN_ASTTAX~7 was never spawned, no instance exists, nothing here is graded. Set by the ISSUER 2.0.0_SA_COO~Z, 2026-09-14 ~17:2xZ, per 1.0.0_SA_CTO~Z's brief msg 22834 (Andrew-direct ~16:5xZ, record @f529179076; close-out breakdown v0.2 @672a8644eb s.4 step 1). superseded and NOT cancelled because at this write the outcome is still owned by a newer order; a re-open asks whether TO-T7-1 is still standing -- and breakdown card 6 proposes cancelling that successor, in which case the row Z-W1-S1 / Z-C-S1 disposition falls to its disarm_owner at L4, not to this order. Carried open since round 2 under LD-0562 (Andrew-direct 2026-09-13 04:08Z "all recs approved", card 1). TO-T7-1 itself stays staged and HELD pending Andrew's alignment.</superseded_by>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-3` · **Issuance:** round 2. **DEPENDS ON `AT2-s-2` -- the vocabulary must settle first.**

---

## THE CELL

Channel row **`POSN_ASTTAX-Z-W1-S1`** (BLOCKING, ARMED, disarm_owner `1.0.0_SA_CTO~Z`), filed by round 1's
worker: `_shared/etf_classification.py` documents its vocabulary as THREE values including `'other'`, but
**0 of 136 tickers use `'other'`** and **7 use an undocumented `'hedge'`** -- which leaves `HEDGE_TICKERS`
empty and makes `is_hedge()` **always return False**. Measured **DORMANT** (no live caller found).

After `AT2-s-2`, the `hedge` value no longer exists in the served table at all. So the predicate is not
merely wrong -- **its referent is gone.** Populate it against the settled vocabulary, or retire it.

## THE ACT

1. **Verify `AT2-s-2` is terminal** (`S3-AC1`). Reconciling a predicate against a vocabulary still in
   motion is a rewrite twice.
2. **Re-take the row's measurements** (`S3-AC2`): the documented vocabulary, the actual value census, and
   whether `HEDGE_TICKERS` is empty.
3. **Re-test the DORMANT finding** (`S3-AC3`) -- round 1 found no live caller; confirm at your vintage
   over a printed denominator. ⛔ **A caller found now changes this from housekeeping to a live defect**
   and is a STOP-and-row, not a quiet fix.
4. **Populate or retire**, and say which and why. Retiring a dead predicate is a legitimate outcome and is
   preferred to populating one nothing calls -- but only if AC3 holds.
5. **Disarm C-S1 by the row's own condition** (`S3-AC4`) -- ⚠ the disarm_owner is `1.0.0_SA_CTO~Z`, so you
   RECORD that the condition is met; **you do not write the disposition.** That is the CVO's plane at L9.
6. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RETAG ANY REGISTRY ROW** -- `AT2-s-2` owns that and must already be done.
- ⛔ **DO NOT WRITE A REMEDIATION OR DISPOSITION ROW.** Remediation rows are the CVO's. You record that
  the disarm condition is met; the adjudication is L9's.
- ⛔ **DO NOT DELETE `etf_classification.py`.** `C-CLASSIFIER-PURPOSE` (a) calls it a SUPERSEDED seed
  input to retire/reconcile deliberately; nothing in round 2 authorises removing it.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W7-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.
- ⛔ Never pipe a comp-tool census into `head`/`tail`/`sed` -- the denial aborts the whole bash call.

## ACCEPTANCE CRITERIA

<criterion id="S3-AC1" cell_refs="AT2-s-3"><invocation>timeout 120 grep -n "<status>" ../task-orders/POSN_ASTTAX.TO-S2-1.retag-the-hedge-bucket.md</invocation><expect>the status line pasted verbatim reading `complete`; anything else and this order STOPS with a row.</expect></criterion> `S3-AC1` -- THE VOCABULARY HAS SETTLED, CHECKED NOT ASSUMED.

<criterion id="S3-AC2" cell_refs="AT2-s-3"><invocation>timeout 120 comp-read infra/aws/lambda/v2_portal/_shared/etf_classification.py --enumerate 'HEDGE_TICKERS|is_hedge|other'</invocation><expect>the enumerate DENOMINATOR and every banded hit pasted verbatim; the documented vocabulary quoted from its comment; and whether HEDGE_TICKERS is empty stated with the line that shows it.</expect></criterion> `S3-AC2` -- THE ROW'S CLAIM, RE-MEASURED AT SOURCE.

<criterion id="S3-AC3" cell_refs="AT2-s-3"><invocation>timeout 300 comp-find 'is_hedge' --all</invocation><expect>the printed DENOMINATOR with the shown count equal to it, every hit banded, and a stated verdict on whether any LIVE caller exists outside the defining module and its own tests. A zero is reported WITH its denominator.</expect></criterion> `S3-AC3` -- ⛔ **THE DORMANCY CLAIM, RE-TESTED OVER A FULL SWEEP.** `--all`, never a page: an early stop and a true absence read identically, and a live caller flips this cell's whole character.

<criterion id="S3-AC4" cell_refs="AT2-s-3"><invocation>timeout 120 python -c "print('DISARM CONDITION RECORDED IN THE INSTANCE')"</invocation><expect>the instance states whether C-S1's disarm condition is now MET, with the evidence, and states explicitly that the disposition is NOT written by this order because disarm_owner is 1.0.0_SA_CTO~Z and adjudication is L9's.</expect></criterion> `S3-AC4` -- THE CONDITION RECORDED, THE DISPOSITION LEFT TO ITS OWNER.

<criterion id="S3-AC5" cell_refs="AT2-s-3" judgment="true"/> `S3-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether populate-or-retire was the right call, and whether the two access paths (`get_asset_class` and `is_hedge`) now agree. **Record the readings and offer NO verdict.**

<expected_criteria>S3-AC1, S3-AC2, S3-AC3, S3-AC4, S3-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S3-1.is-hedge-reconciliation.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~7/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/_shared/etf_classification.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-3`.
<owned_cells>AT2-s-3</owned_cells>
Read-dependencies, NOT claimed: `AT2-s-2` must be terminal (S3-AC1). Channel row POSN_ASTTAX-Z-W1-S1 is
the subject; its disarm_owner is 1.0.0_SA_CTO~Z and is not reassigned by this order.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, Terraform or AWS write; source change only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool; the row's measurements are round 1's worker
instance at HEAD and AC2/AC3 re-take both. ⚠ The DORMANT finding is the one most likely to have aged, and
AC3 is deliberately a full `--all` sweep rather than a spot check for exactly that reason.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~7/POSN_ASTTAX.TO-S3-1.is-hedge-reconciliation.proof_of_spec.json
</proof_of_spec>
