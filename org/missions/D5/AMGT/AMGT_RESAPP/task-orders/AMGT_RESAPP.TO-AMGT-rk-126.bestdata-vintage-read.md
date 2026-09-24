# AMGT_RESAPP task order -- `AMGT-rk-126` -- SUBSTRATE CARD S1: can Bloomberg's dated `bestdata` vintages give a consensus REVISION series? Answer BOTH halves from data the firm ALREADY HOLDS -- READ-ONLY, zero pulls, zero spend

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-126</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~126</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer.
  It reads stored objects.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant is edited and no credential is minted. Reads
  run under the seat's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~126`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
First act: print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~126;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

⛔ **ZERO BLOOMBERG CALLS. ZERO PULLS. ZERO SPEND.** This cell answers its question entirely from objects already in
the store. **If you find yourself reaching for a pull, STOP and file a row** -- the answer that needs one is the
card, not this cell.
⛔ **EVERY `.scratch/` script runs as `PYTHONPATH="$(pwd)" python .scratch/...`** -- the bare form sets
`sys.path[0]` to the script's own directory and `from lib.research...` raises `ModuleNotFoundError` (rows
`Z-W117-S1`/`S3`, both forms exercised by the issuer).

## 1. THE CELL -- `AMGT-rk-126` (round 32, decomposition s.40c / s.40f)

**THE QUESTION (substrate card S1, `1.0.0_SA_CTO~Z` msg 24402):** can Bloomberg's dated `bestdata` vintages give us
the consensus REVISION series -- **on real data the firm already pays for, before any vendor subscription is
considered?** The CTO's standing NO on a vendor holds until this read exists.

**WHAT THE ISSUER MEASURED AT THE CUT, and it is your starting denominator:**
`bloomberg/harvest/bronze/bestdata/` holds **7 objects across 4 securities**:

| security | vintages |
|---|---|
| `992_HK_Equity` | `20260922T201211Z` (ONE -- `rk-116`'s first-ever `bestdata` bronze) |
| `CAT_US_Equity` | `20260919T124848Z`, `20260919T152117Z` (**TWO**) |
| `CSL_AU_Equity` | `20260919T124852Z`, `20260919T152121Z` (**TWO**) |
| `6861_JP_Equity` | `20260919T124855Z`, `20260919T152125Z` (**TWO**) |

⭐ **SO BOTH HALVES OF S1 ARE ANSWERABLE WITH NO PULL.** The issuer's first draft of this cell assumed the second
half needed one and was going to REFUSE it; listing the store first showed three pairs already on disk.

## 2. THE ACT -- answer TWO questions and keep them APART

**Q1 -- WHAT IS IN A VINTAGE?** Read Lenovo's object (`992_HK_Equity/20260922T201211Z.json`). Enumerate every
`BEST_*` field with its value and, where present, its estimate count / number of contributing analysts. **Print the
denominator of fields.** State plainly which fields a revision series would need and whether they are present.

**Q2 -- DO TWO VINTAGES OF THE SAME NAME DIFFER, AND HOW?** For each of the three two-vintage securities, diff the
earlier against the later. Report, per security: fields present in both, fields added/removed, and **fields whose
VALUE moved, with old -> new**. Print the denominator each time.

⛔ **AND THE PART THAT DECIDES WHETHER THIS ANSWERS S1 AT ALL -- DO NOT LET Q2's CHEAP ANSWER STAND IN FOR THE
EXPENSIVE ONE.** The two vintages are **~152.5 MINUTES (2:32:29) APART ON THE SAME DAY** (`12:48:48` and
`15:21:17` on 2026-09-19, identical to the second across all three pairs). **Consensus does not move in an
afternoon.** ⚠ **THIS LINE SAID "~33 MINUTES" AT ISSUANCE AND THE NUMBER WAS THE ISSUER'S, NEVER COMPUTED** --
wrong by 4.6x, corrected here post-drain on row `Z-W126-S1`, which the worker measured and filed. The conclusion
is unchanged, which is precisely why nobody had cause to check it. So:

- A DIFFERENCE would be surprising and is a finding in its own right (it would mean something other than consensus
  revision moves these fields intraday -- say so, do not assume).
- **NO DIFFERENCE IS THE EXPECTED RESULT AND IT PROVES ONLY THE WEAK CLAIM:** that the store PRESERVES DISTINCT
  VINTAGES and that a reader can diff them. ⛔ **IT DOES NOT PROVE A CONSENSUS REVISION WOULD BE CAPTURED.** That
  needs vintages DAYS OR WEEKS apart, which this estate does not yet hold.

**Your report MUST answer S1 in three separate sentences, never collapsed:** (a) what a vintage contains; (b) what
the store demonstrably preserves and can be diffed; (c) **what remains UNANSWERED and exactly what it would take**
-- name the interval and the number of pulls a real revision test needs. **Do not size it as an act to take; state
it so the CTO can card it.**

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~126/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
.scratch/r126/**
</paths>

⚠ **No code file is written by this cell.** `portal/**` is NOT named and may not be written -- lane `POD_DE_ANY`,
which the issuing seat does not hold.

## 4. BOUNDS

- **READ-ONLY on S3.** No write to any bucket. No deploy, no AWS mutation, no vendor call, no Bloomberg call.
- **Zero egress off Opal infrastructure.**
- Do not modify any producer, any adapter, or any test.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-126"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r126/ac0.py</invocation><expect>the store census reproduced independently, with its denominator: 7 objects across 4 securities, and the per-security vintage lists matching the table in s.1 exactly -- 992_HK_Equity ONE, and CAT_US_Equity / CSL_AU_Equity / 6861_JP_Equity TWO each. If the counts DIFFER from the issuer's, that is a finding to report, not a discrepancy to silently adopt: print both</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-126"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r126/ac1.py</invocation><expect>Q1 answered on Lenovo's object: every BEST_* field enumerated with its value, the DENOMINATOR of fields printed, and estimate-count / analyst-count fields named where present and named as ABSENT where not. A statement of which fields a revision series would require and whether each is present</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-126"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r126/ac2.py</invocation><expect>Q2 answered for ALL THREE two-vintage securities: per security, fields in both / added / removed / VALUE-MOVED with old -&gt; new, each with its denominator. The elapsed interval between the two vintages PRINTED per security (MEASURED ~152.5 minutes / 2:32:29; the order originally said ~33 and was wrong -- row Z-W126-S1). An explicit per-security verdict of IDENTICAL or DIFFERING -- and if IDENTICAL, it is stated as such and NOT dressed up as a revision finding</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-126"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cat org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~126/SUBSTRATE_S1_READ.md</invocation><expect>S1 answered in THREE SEPARATE, clearly-labelled parts: (a) what a vintage CONTAINS; (b) what the store DEMONSTRABLY PRESERVES on a ~33-minute interval; (c) what remains UNANSWERED about consensus REVISION, with the interval and pull count a real test would need, stated for the CTO to card and NOT sized as an act to take. ⛔ A report that lets (b) answer (c) FAILS this criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-126"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git status --short &amp;&amp; git diff --name-only $(git rev-parse HEAD) -- lib integrations infra .tools portal</invocation><expect>the diff list is EMPTY -- this cell writes no code file anywhere. git status shows only your own deliverables / .scratch. Anything under lib, integrations, infra, .tools or portal is a BLOCKING row against yourself</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-126"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c "PacedSession\|blp\|ReferenceDataRequest" .scratch/r126/*.py ; echo "SPEND-CHECK-DONE"</invocation><expect>ZERO Bloomberg call machinery in any script this cell ran -- the grep returns 0 for every file (a count of 0 per file, or no match at all), and you state plainly: 0 pulls, 0 requests, 0 spend this cell. A non-zero count is a BLOCKING row against yourself</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~126/AMGT_RESAPP.TO-AMGT-rk-126.bestdata-vintage-read.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance>
AC0,AC1,AC2,AC3,AC4,AC5` run from inside it (rc 0 is the verdict), then flip `<status>` to `complete` only if every
criterion PASSES. Report once, naming: the field denominator from Q1, the per-security verdicts from Q2 with the
printed intervals, and part (c) of your S1 answer verbatim.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**

1. **This cell was drafted on a FALSE PREMISE and the pre-issuance exercise caught it before issuance** (s.40f). The
   first draft had the cell REFUSE S1's second half for want of a second vintage; one `list_objects_v2` showed three
   pairs already on disk. The exercise removed an unnecessary refusal, widened the cell from 1 name to 4, and named
   the ~33-minute limit that would otherwise have arrived as the worker's surprise row.
2. **AC3 is written to make the cheap answer UNABLE to pass as the expensive one.** The whole risk in this cell is a
   report concluding "vintages work, no vendor needed" off a 33-minute diff. The criterion fails on exactly that.
3. **AC5 exists because "zero spend" is the cell's core bound** and an assertion is not a control; the grep is.
4. **Round 32 is ONE cell by measurement, not by shortfall** -- s.40a and s.40b record why the other two server-side
   candidates dissolved into calls.

**ISSUER CLOSE-OUT, `2.0.0_SA_COO~Z`, 2026-09-23 ~00:1xZ (post-drain @`2d6e07be55`).** Flipped `pending` ->
`complete` BY THE ISSUER, because the worker could not: ⛔ **s.6 above instructs the worker to flip its own
`<status>`, but this order's `<paths>` grant does not name `task-orders/`** -- so the instruction was unperformable
as written. The worker refused it correctly and filed row `Z-W126-S2` rather than reaching outside its grant.
**That is a third defect of this seat's in one order**, beside `Z-W126-S1` (the `~33 minutes` figure, wrong by
4.6x) and `Z-W126-S3` (`.scratch/**` has no static lane entry, so the validator refuses a path this order grants).
⭐ **All six criteria PASS, proof-of-spec rc=0, and this seat verified AC2's substance on its own instrument**:
48 leaf fields per vintage, **3 moved and all three are envelope fetch timestamps**, **0 of the consensus fields
moved**, and **0 contributor/analyst-count fields exist anywhere in the schema.**

<status>complete</status>
<round>32</round>
<slot>~126</slot>
<fabric>site-z</fabric>
