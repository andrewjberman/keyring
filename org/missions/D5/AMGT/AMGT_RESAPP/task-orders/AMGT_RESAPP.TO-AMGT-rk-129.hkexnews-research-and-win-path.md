# AMGT_RESAPP task order -- `AMGT-rk-129` -- HKEXnews as a RESEARCH question, with a POSITIVE CONTROL before any conclusion about Lenovo, and the WIN PATH proven on a fixture so the two blockers can never mask each other again

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-129</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~129</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant is edited and no credential is minted.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
EGRESS CLASS, declared: PUBLIC-REGULATOR HTTP fetches (HKEXnews), the same class step 1/2 already make to EDGAR and
  step 4 makes to the issuer's own site, inside the international battery Andrew RATIFIED @4de34f0d95. NOT a vendor
  API, no credential, no key, no session. BUDGET: at most 12 live HKEX fetches for the WHOLE cell, counted from a
  COUNTER and printed by AC7. No Bloomberg call of any kind. The budget is raised from round 35's ONE deliberately
  -- that bound is the direct cause of the structural blocker this cell exists to remove.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~129`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
First act: print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that
`lib/research/filings/battery.py` exists. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~129;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.
⛔ **Every `.scratch/` script runs as `PYTHONPATH="$(pwd)" python .scratch/...`** (rows `Z-W117-S1`/`S3`); and
`.scratch/**` has NO static lane entry (`Z-W126-S3`), so if the validator refuses to commit your scripts, **that is
the known estate gap -- keep them, cite their output, do not fight the validator.**

## 1. THE CELL -- `AMGT-rk-129` (round 36, decomposition s.44)

Round 35 built the HK national-regulator adapter. It dispatches correctly on listing venue, is negative-controlled
on three branches, holds acceptance test (c) -- **and the route returns nothing.** The reported cause was a live
HKEXnews search answering `HTTP 200, recordCnt=0`.

⛔ **THAT IS ONE OF TWO BLOCKERS, AND IT HIDES THE OTHER. READ THIS BEFORE YOU PLAN ANYTHING:**

- **BLOCKER A** -- the search returns 0 records.
- **BLOCKER B** -- `_hk_national_regulator` (`lib/research/filings/battery.py:1252-1334`) has **five return paths
  and every one returns `passed` false**, including the branch where the search SUCCEEDS. Its `seeds` go into a
  list created at `:1441` and passed by reference into **step 4's** lambda at `:1449` -- and step 5 runs at
  `:1451`, **after** step 4. **So step 5's seeds land in a list whose only reader has already run.** The winner is
  set only on a passing step (`:1463`), so the run falls through to `:1473` and the returned object is built from
  attempts alone (`:1476`).

⭐ **CONSEQUENCE, AND IT IS THE REASON THIS CELL IS SHAPED THE WAY IT IS: if you fixed the search perfectly and did
nothing else, you would get records, populated seeds, `passed` still false, the route still UNRESOLVED, and nothing
downstream different.** You would report a solved query and an unsolved route and the next reader would hunt a
third cause that does not exist.

**Blocker B is the ISSUING SEAT'S, not a defect you inherited from the previous worker.** Round 35's order bounded
egress to ONE fetch, spent on the search, so the found document could never be fetched, so acceptance could never
run, so a win was unreachable. The previous worker implemented that bound correctly and wrote it down plainly at
`:1267-1272`. **This order raises the bound and asks you to close B.**

**So this cell has TWO LIMBS, and bound 2 below is what keeps them independent.**

- **LIMB 1, RESEARCH:** can HKEXnews be made to answer at all? Positive control first, Lenovo second.
- **LIMB 2, THE WIN PATH:** can the adapter win, and does a win PROPAGATE? Proven on a FIXTURE, so it is gradeable
  whether or not limb 1 succeeds.

## 2. ⛔ THE BOUND THAT IS NOT NEGOTIABLE -- the positive control comes FIRST

`recordCnt=0` is **non-discriminating evidence**. It reads identically for a wrong parameter set, a wrong endpoint,
a required session or cookie, a silent block, an undocumented required field, and a genuine absence of filings.
**Until you have produced a query to `titleSearchServlet.do` that returns `recordCnt > 0`, you cannot tell which of
those you are looking at, and no sentence about Lenovo is falsifiable.**

Any issuer, any date range, the interface's own defaults, a different `searchType`, a browser-shaped request --
**whatever returns records.** That single result is what converts every later zero from a mystery into a
measurement.

⛔ **If you cannot find one, SAY SO WITH WHAT YOU TRIED AND ITS DENOMINATOR.** "No query returns records" measured
over a named, printed set of attempts is a **FULL RESULT** for this cell and retires the route. **This cell is cut
to be able to say NO.** What is refused is an unmeasured zero.

## 3. ⛔ AND THE SECOND BOUND: THE WIN PATH IS PROVEN ON A FIXTURE, NEVER ON THE LIVE SEARCH

Limb 2 must be gradeable **even if HKEXnews defeats limb 1 entirely.** Build a stubbed HKEXnews reply carrying one
known-good record and drive the adapter through it -- exactly as round 35 proved its adversarial arm with a
purpose-built synthetic document rather than waiting for a live one.

⭐ **This is the whole lesson of s.44a made mechanical: the two blockers are decoupled so that neither can ever
again mask the other.** A fixture-proven win path plus a measured live zero is a complete, honest result. A live
win is a bonus, not the bar.

## 4. BOUNDS

1. **Acceptance test (c) still BINDS.** A document is accepted only if the issuer is the SUBJECT of the filing, not
   merely its filer. Round 35 proved this adversarially; the win path must not loosen it, and AC6 re-proves it.
2. **Steps 1-4 DO NOT MOVE.** Their signatures and their four lambda lines stay byte-identical, the step list's
   membership and order stay `[1,2,3,4,5]`, and `_attempt`'s signature is untouched. Negative-controlled by AC8.
3. **Egress: at most 12 live HKEX fetches for the whole cell**, from a counter, printed. 0 Bloomberg calls. If
   HKEX is unreachable or refuses, that is a RESULT -- record it with status and reason and **do not retry in a
   loop.**
4. ⛔ **NO S3 DELETE OF ANY KIND** -- no object, no version, no delete marker. Removing a delete marker is itself a
   delete. This is STANDING on every order in this project and is Andrew's word only. If something looks like it
   needs deleting, file a row and keep working.
5. ⛔ **NO HUNTING FOR A KEY, SECRET OR SESSION TO FORGE A BEARER OR A LOGIN.** If HKEXnews turns out to require a
   session or credential, **that is a finding to REPORT**, never a thing to manufacture or borrow. STANDING.
6. **Do not mint an S3 address and do not add a registry row.** If your work turns out to need one, RECORD that it
   does and stop there; the issuing seat does not hold that lane and cannot admit you to it.
7. **No fleet run.** One name (Lenovo, `992_HK_Equity`) plus whatever issuer your positive control uses.

## 5. SURFACES

<paths>
lib/research/filings/battery.py
lib/research/filings/fetch.py
lib/research/filings/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~129/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
.scratch/r129/**
</paths>

⚠ **`infra/logic/registry/**` IS DELIBERATELY ABSENT** -- see BOUNDS 6. The issuing seat does not hold that lane
and may not admit you to it; naming it would be the delegation CVO ruling R5 forbids.

## 6. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac0_positive_control.py</invocation><expect>⛔ THE POSITIVE CONTROL, BEFORE ANY CONCLUSION ABOUT LENOVO: a query to HKEXnews `titleSearchServlet.do` that returns `recordCnt` GREATER THAN 0, with the full URL, the HTTP status, the recordCnt and the first record's title printed. If found, state plainly which parameter or shape made the difference against round 35's failing query. ⚠ If NO query returns records, that is a LEGITIMATE RESULT: print the DENOMINATOR of distinct attempts made, each attempt's parameter set and its recordCnt, and state the conclusion as "no query in N attempts returned records" -- an unmeasured zero is what fails this criterion, not a measured one</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3</invocation><expect>the filings suite BASELINE before your edit -- record passed/failed as A0. A measurement, not a bar</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac2_interface.py</invocation><expect>the interface CHARACTERISED from AC0's working shape: which parameters the endpoint actually honours, which it ignores, and which it rejects -- each claim carrying the response that demonstrates it. Print what `searchType`, `category`, `documentType` and `stockId` actually do, and name any REQUIRED field round 35's query omitted. ⚠ Every statement here is about what you OBSERVED; a parameter you did not vary is reported as NOT TESTED, never as "ignored"</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac3_lenovo.py</invocation><expect>LENOVO SPECIFICALLY, answered against AC0's now-working shape: does `992_HK_Equity` return records from HKEXnews, and under what exact stock id and parameter set? Print the URL, status, recordCnt and the first three titles if any. ⚠ BOTH ANSWERS ARE RESULTS: if Lenovo returns records, the route is live; if it does not while AC0's control DOES, that is a much stronger finding than round 35 could make -- it isolates the failure to this issuer rather than to the interface, and must be stated in exactly those terms</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac4_win_on_fixture.py</invocation><expect>⛔ THE WIN PATH, PROVEN ON A FIXTURE AND NOT ON THE LIVE SEARCH: drive the HK adapter with a STUBBED HKEXnews reply carrying one known-good record, and assert the adapter FETCHES the referenced document, runs the acceptance path against it, and returns `passed` TRUE with a populated `battery_extra`. Print the branch taken and the acceptance outcome. ⚠ This criterion must PASS whether or not AC0 and AC3 found anything live -- if it can only be demonstrated against a live search, it is not built the way this order requires</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac5_win_propagates.py</invocation><expect>⛔ THE WIN PROPAGATES -- SEPARATE FROM AC4 AND NOT IMPLIED BY IT: run the FULL battery on the same fixture and assert the returned object is RESOLVED, that its battery block names step 5 as the winner, and that `fetch.build_source_object` accepted the adapter's `battery_extra`. Print the winner step and the object's resolved/unresolved state. ⚠ An adapter that returns `passed` true while the battery still returns UNRESOLVED is EXACTLY the stacked-blocker defect this cell exists to remove -- that outcome FAILS this criterion and must be reported, not worked around</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac6_test_c_still_binds.py</invocation><expect>⛔ TEST (c) NEGATIVE-CONTROLLED ON THE NEW WIN PATH: feed the widened path a document that passes (a) RIGHT ENTITY -- the issuer's own name present -- but is a FILER-ABOUT-ANOTHER-ISSUER form, and assert it is REJECTED with the printed reason naming (c) KNOWN FAMILY and NOT (a). Then the positive control: a genuine annual-family document ACCEPTS and wins. Both printed. A run where (a) alone decides is a FAILURE of this criterion</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac7_spend.py</invocation><expect>the cell's SPEND from a COUNTER, not an estimate: `http_fetches` printed and LESS THAN OR EQUAL TO 12, `bloomberg_calls` 0, `s3_deletes` 0, `s3_delete_markers_removed` 0. Print the per-URL fetch log so the count is auditable against the list</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-129"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3 &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r129/ac8_untouched.py &amp;&amp; git diff --name-only $(git rev-parse HEAD) -- lib integrations infra .tools portal</invocation><expect>passed = A0.passed + your new arms, failed = 0 (pre-existing failures named if any). ⛔ THE NEGATIVE CONTROL: steps 1-4's SIGNATURES and their four lambda lines printed BEFORE and AFTER, asserted BYTE-IDENTICAL; the step list's MEMBERSHIP and ORDER printed as [1,2,3,4,5] unchanged; `_attempt`'s signature unchanged. The diff list names ONLY lib/research/filings/** -- ⛔ NOTHING under infra/, portal/ or .tools/, and NO registry row (BOUNDS 6: you record that one is needed, you do not mint it)</expect></criterion>
</proof_of_spec>

## 7. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~129/AMGT_RESAPP.TO-AMGT-rk-129.hkexnews-research-and-win-path.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance>
AC0,AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8` from inside it. ⚠ **The status flip is the ISSUER'S** -- this order's
surfaces block (s.5) does not name `task-orders/`. **Leave the record face alone and say so.** Commit messages
PURE ASCII, written by the Write tool, never `printf`.

**Report once, naming:** AC0's verdict with its denominator, whether AC3 isolated the failure to Lenovo or to the
interface, and whether AC5 showed a win PROPAGATING. ⚠ **If limb 1 found nothing live and limb 2 passed on the
fixture, SAY BOTH IN THE SAME SENTENCE** -- that is the cell's designed outcome, not a partial one, and it must not
be reported as a failure.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** blocker B (s.44a) was measured BEFORE this order existed and is the reason the cell has two
limbs. It was invisible to every instrument aimed at the route, because the route stopped at blocker A and never
reached it -- and the sentence naming it was sitting in the previous worker's own docstring at `:1267-1272`, read
by three seats without being read. **B is the issuing seat's own round-35 egress bound coming back; the previous
worker implemented that bound correctly.**

**Criterion ids checked UNIQUE at the cut** -- nine blocks, nine distinct ids -- after round 35's order carried
seven blocks and six ids, which the checker silently collapsed while the issuance gate counted the larger number.

<status>pending</status>
<round>36</round>
<slot>~129</slot>
<fabric>site-z</fabric>
