# TO POSN_ASTTAX.TO-T7-1 -- reconcile `is_hedge()` with the vocabulary the retag settles, so a helper stops returning False for tickers whose class IS hedge. Successor to the never-run `TO-S3-1` (AT3-s-7, FWD-1)

<to_id>POSN_ASTTAX.TO-T7-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~16</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-7` · **Issuance:** round 3. **DEPENDS ON `AT3-s-6`.**

---

## THE CELL

Row `POSN_ASTTAX-Z-W1-S1` (round 1, GRADUATED by the CVO as `C-S1`):
`_shared/etf_classification.py` documents its vocabulary as THREE values
(`fixed_income`, `equity`, `other`), assigns **`other` to ZERO tickers**, and uses an undocumented
fourth value `hedge` for seven. `HEDGE_TICKERS` is built as
`{ticker for ticker, ac in ETF_CLASSIFICATIONS.items() if ac == 'other'}` -- so it is **the empty set at
runtime**, and `is_hedge('GLD')` returns `False` while `get_asset_class('GLD')` returns `'hedge'`.

⭐ **THIS CELL RUNS LAST BY DESIGN.** The retag settles what the vocabulary IS. Reconciling a helper
against a vocabulary that is mid-move would fix it to the wrong answer -- the exact
"erased by the next run and looks like it worked until then" shape this project already caught once.

⛔ **THE WIDER DESIGN QUESTION IS NOT YOURS.** `3.0.0_SA_CVO~Z` GRADUATED `C-S1` to `1.0.0_SA_CTO~Z`
naming three non-equivalent directions (document `hedge`; retire it; delete `is_hedge()` as dead) and
recording that the ORDERING matters. **You do not choose among them.** You reconcile the helper with
whatever vocabulary the retag has actually left in place, and you report.

## THE ACT

1. **Re-measure the vocabulary AFTER the retag** (`T7-AC1`) -- the live value set with its denominator.
   ⛔ Do not inherit round 1's `{fixed_income: 66, equity: 63, hedge: 7}`; that predates the retag.
2. **Measure what `is_hedge()` and `HEDGE_TICKERS` now return** (`T7-AC2`) against that vocabulary.
3. **Census the callers** (`T7-AC3`). Round 1 found the break DORMANT -- 6 hits, all DEF/export/doc, no
   live call site. **Re-take it**; a dormant break and a live one need different answers, and the
   answer may have changed.
4. **Reconcile the helper with the settled vocabulary** (`T7-AC4`), stating the shape you chose and what
   it does NOT fix.
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RETAG ANY REGISTRY ROW.** `AT3-s-6` owns that and runs before you.
- ⛔ **DO NOT RULE ON THE WIDER VOCABULARY QUESTION.** It is graduated to the CTO. If your reconciliation
  requires that ruling, STOP and file a row saying which of the three directions it would need.
- ⛔ **DO NOT DEPLOY.** Source change only.
- ⚠ Three module copies exist. Print the denominator; a fix in one is a fix in one.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W16-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T7-AC1" cell_refs="AT3-s-7"><invocation>timeout 180 python -c "import sys; sys.path.insert(0,'infra/aws/lambda/v2_portal/_shared'); import etf_classification as ec; from collections import Counter; c=Counter(ec.ETF_CLASSIFICATIONS.values()); print('COUNTER:', dict(c)); print('TOTAL:', sum(c.values()))"</invocation><expect>the live value set and its total pasted verbatim AT THIS VINTAGE, and a stated comparison against round 1's {fixed_income: 66, equity: 63, hedge: 7} / 136 saying what the retag moved. If the module was not the thing the retag touched, say so -- that is itself the finding.</expect></criterion> `T7-AC1` -- THE VOCABULARY AFTER THE RETAG, RE-MEASURED.

<criterion id="T7-AC2" cell_refs="AT3-s-7"><invocation>timeout 120 python -c "import sys; sys.path.insert(0,'infra/aws/lambda/v2_portal/_shared'); import etf_classification as ec; print('HEDGE_TICKERS:', sorted(ec.HEDGE_TICKERS)); print('len:', len(ec.HEDGE_TICKERS)); print('is_hedge(GLD):', ec.is_hedge('GLD')); print('get_asset_class(GLD):', ec.get_asset_class('GLD'))"</invocation><expect>all four values pasted verbatim. The contradiction stated explicitly if it persists: is_hedge() False while get_asset_class() reports a hedge-family class, or whatever the post-retag equivalent now is.</expect></criterion> `T7-AC2` -- THE HELPER'S ACTUAL BEHAVIOUR, NOT ITS DOCSTRING.

<criterion id="T7-AC3" cell_refs="AT3-s-7"><invocation>timeout 300 comp-find 'is_hedge' --all --files</invocation><expect>the printed DENOMINATOR and every hit, banded; then a stated verdict on whether any LIVE pipeline call site exists, named either way. Round 1 measured 6 hits, all DEF/export/doc, and concluded DORMANT -- state whether that still holds at your vintage.</expect></criterion> `T7-AC3` -- DORMANT OR LIVE, RE-TAKEN. The answer changes what a correct fix is.

<criterion id="T7-AC4" cell_refs="AT3-s-7"><invocation>timeout 180 python &lt;your reconciliation + control&gt;</invocation><expect>the change applied with the SHAPE named and what it does NOT fix stated; then a before/after showing is_hedge() returns the correct answer for every ticker whose class is in the hedge family AFTER and did not BEFORE, with a FALSIFY arm on the old bytes that must FAIL. Per-copy confirmation across every module copy AC1/AC3 enumerated.</expect></criterion> `T7-AC4` -- THE FIX, WITH A CONTROL THAT FAILS ON THE OLD BYTES.

<criterion id="T7-AC5" cell_refs="AT3-s-7" judgment="true"/> `T7-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether this reconciliation is consistent with the settled five-class vocabulary, or quietly entrenches a fourth value the ratified taxonomy does not contain -- the concern `C-S1` raised. **Record the readings and offer NO verdict.**

<expected_criteria>T7-AC1, T7-AC2, T7-AC3, T7-AC4, T7-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T7-1.is-hedge-reconciliation.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~16/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/_shared/etf_classification.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-7`.
<owned_cells>AT3-s-7</owned_cells>
Read-dependency, NOT claimed: `AT3-s-6` (the retag) must be terminal first -- it settles the vocabulary you reconcile against. SUCCESSOR to the never-run `TO-S3-1`.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, Terraform or AWS write; source change only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied: round 1's vocabulary counts and its DORMANT verdict are that round's figures at that vintage
and PREDATE the retag; AC1 and AC3 re-take both independently. The wider reconciliation direction is
GRADUATED to `1.0.0_SA_CTO~Z` (`C-S1`) and is not settled by this order.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~16/POSN_ASTTAX.TO-T7-1.is-hedge-reconciliation.proof_of_spec.json
</proof_of_spec>
