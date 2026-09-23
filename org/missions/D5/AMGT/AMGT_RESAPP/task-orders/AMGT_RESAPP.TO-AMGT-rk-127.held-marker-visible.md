# AMGT_RESAPP task order -- `AMGT-rk-127` -- the HELD-MARKER: a CHANGED-HELD outcome is recorded ADDITIVELY and the adapter SAYS the served outcome is held with a newer one behind it, so the page stops presenting a falsified reason as current. CODE ONLY, `lib/**`, no deploy, no spend

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-127</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~127</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant is edited; no credential is minted.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~127`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
First act: print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~127;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check
out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.
⛔ **Every `.scratch/` script runs as `PYTHONPATH="$(pwd)" python .scratch/...`** (rows `Z-W117-S1`/`S3`).
⚠ **`.scratch/**` has NO static lane entry** (row `Z-W126-S3`), so `owned-paths-validate.py` may refuse to commit
your scratch scripts even though this order grants the path. **If it refuses, that is the known estate gap -- do
NOT fight it and do NOT work around the validator.** Keep the scripts, cite their output, and say so in your report.

## 1. THE CELL -- `AMGT-rk-127` (round 33, decomposition s.41b)

**THE DEFECT, named accurately by `1.0.0_SA_CTO~Z` @`a7e2f5ab92` after `3.0.0_SA_CVO~Z` corrected the first
framing:** *a CHANGED outcome is HELD, and the held object keeps serving a sentence the new outcome falsifies --
with nothing making that staleness visible.*

**The live instance:** Lenovo's Thesis tab serves
`"filing_identity.source is 'none': no cik and expected form to fetch by"`, while the battery has since resolved
**CIK 932477 to EDGAR entity "LENOVO GROUP LTD"** and moved `filing_identity.source` to `battery`. **We have the
cik. The page says we do not.**

⛔ **`rk-105` IS NOT THE DEFECT AND YOU MAY NOT CHANGE IT.** `filing_identity` IS one of the seven outcome fields
(`filings.py:258-278`), so CHANGED-HELD fired **because the outcome genuinely differs -- the guard working.** And
`reason` is excluded from the projection **deliberately** (`:287-292`): live reason strings embed counters that
move between identical runs, so comparing them would call every re-run "changed", **the very failure SKIP-HELD
exists to remove.** ⚠ **The issuer's first card proposed loosening exactly that and was wrong; this order exists
because the CVO caught it.**

**THE ACT -- additive, three parts:**

1. **RECORD THE HELD OUTCOME.** Where `state_put_filing_attempt` raises `FilingAttemptChangedError`
   (`filings.py:390`, inside the function at `:317`), ALSO persist the NEW outcome **beside** the served object --
   a sibling held-marker, **never a mutation of the served object and never a change to what is held or why**. It
   must carry at minimum: the new `status`, the new `reason`, the new `filing_identity`, the differing field name
   the error already computes, and its own `retrieved_at`. Address it through the same builder the served object
   uses -- **never a hand-typed bucket or key literal** (`filings.py:27-32`).
2. **STATE IT AT SERVE TIME.** The adapter reads the served object at `scoped_amgt.py:1986`
   (`key = "%s%s/UNRESOLVED-SOURCE.json" % (FILING_ATTEMPT_STATE_PREFIX, partition)`). When a held-marker exists
   for that name, the payload must say **the served outcome is HELD and a NEWER one exists**, and surface the
   newer reason. ⛔ **Do NOT silently swap the new reason in** -- the page must be able to show that what it holds
   is superseded, not quietly present the new text as if it were the served state.
3. **TESTS** in the existing homes, hermetic, no live S3.

⭐ **THE SHAPE TO PRESERVE:** make the TRUE STATE VISIBLE rather than suppress the false sentence. That is the
same remedy `C-S400` gets one layer up, and it is why (b) was chosen over publishing per-name under a pair: **a
pair per name does not scale; a held-marker does.**

## 2. BOUNDS

- **CODE ONLY.** No deploy, no `terraform`, no Lambda update, **no S3 write from this cell**, no AWS mutation.
- **No vendor call, no Bloomberg call, zero spend, zero egress off Opal.**
- ⛔ **OUT OF BOUNDS:** `_filing_attempt_outcome_fields`, `_filing_attempt_outcome`, and the SKIP-HELD /
  CHANGED-HELD decision itself. You are adding a marker and a statement. **If your change alters WHAT is held or
  WHY, you have exceeded the cell -- STOP and file a row.**
- `portal/**` is NOT named and may not be written (lane `POD_DE_ANY`, which the issuing seat does not hold).

## 3. SURFACES

<paths>
lib/research/harvest/filings.py
lib/research/api/scoped_amgt.py
lib/research/harvest/tests/**
lib/research/api/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~127/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
.scratch/r127/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-127"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r127/ac0.py</invocation><expect>BEFORE any edit, printed with denominators: the seven outcome-field labels from _filing_attempt_outcome_fields in order, with `filing_identity` present and `reason` ABSENT; and the live served reason for 992_HK_Equity read through the adapter's own key construction, quoted verbatim -- it must read "filing_identity.source is 'none': no cik and expected form to fetch by". Record both. This is the pre-state the cell exists to make legible</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-127"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/harvest/tests lib/research/api/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3</invocation><expect>the BASELINE for both suites before your edit -- record passed/failed as A0. A measurement, not a bar</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-127"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/harvest/tests lib/research/api/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3</invocation><expect>passed = A0.passed + (arms you added), failed = 0. Pre-existing failures, if any, must be the SAME ones by name -- print them rather than reporting a clean number</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-127"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r127/ac3.py</invocation><expect>the held-marker path exercised HERMETICALLY (a stub/fake client, no live S3): given an existing served object and a CHANGED new outcome, (a) FilingAttemptChangedError is still raised -- the guard is UNCHANGED; (b) the served object's bytes are UNTOUCHED, proven by a before/after hash; (c) a held-marker is produced carrying the new status, reason, filing_identity, the differing field name, and its own retrieved_at; (d) the marker's address comes from the builder, NOT a hand-typed literal -- print it</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-127"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r127/ac4.py</invocation><expect>the ADAPTER half, hermetic: with a held-marker present the payload STATES the served outcome is HELD and a newer one exists, and surfaces the newer reason as the NEWER one -- not swapped in as the served text. With NO held-marker present the payload is byte-identical to today's, proven by a dump comparison. ⛔ Print BOTH branches; the no-marker branch is the regression control</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-127"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git diff --name-only $(git rev-parse HEAD) -- lib integrations infra .tools portal &amp;&amp; git diff -- lib/research/harvest/filings.py | grep -c "_filing_attempt_outcome_fields\|def _filing_attempt_outcome" ; echo "PROJECTION-UNTOUCHED-CHECK-DONE"</invocation><expect>the file list is exactly lib/research/harvest/filings.py, lib/research/api/scoped_amgt.py and your new/edited test files -- NOTHING under portal/, infra/ or .tools/. And the grep returns 0: the outcome PROJECTION is untouched by your diff. A non-zero count is a BLOCKING row against yourself</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~127/AMGT_RESAPP.TO-AMGT-rk-127.held-marker-visible.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance>
AC0,AC1,AC2,AC3,AC4,AC5` from inside it. ⚠ **The `<status>` flip is the ISSUER'S** -- this order's `<paths>` does
not name `task-orders/`, and row `Z-W126-S2` is exactly that defect. **Leave `<status>` alone and say so.**
Report once, naming: AC0's served reason verbatim, AC3's before/after hash of the served object, and AC4's
no-marker regression control.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**

1. **`<status>` is deliberately left to the issuer** and the worker is told so, because `Z-W126-S2` measured that
   the same instruction was unperformable under this `<paths>` shape. **The template defect is fixed by removing
   the instruction, not by widening the grant** -- widening it would admit a worker to every order file.
2. **The `.scratch/` lane gap (`Z-W126-S3`) is disclosed in the worker face** so the worker does not treat a
   validator refusal as its own error. It is Andrew's card, not this cell's.
3. **`rk-105` is fenced in the BOUNDS and again in AC5's grep**, because the issuer's own first card proposed
   changing exactly that and was wrong. The criterion makes the fence mechanical rather than hortatory.

<status>pending</status>
<round>33</round>
<slot>~127</slot>
<fabric>site-z</fabric>
