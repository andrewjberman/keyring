# TO IRPT_ANLREQ.TO-AR-y-308.shares-not-composed-words -- WRITE the plain words a person sees when a Shares file is turned back because no price source is composed, and ask for a market-value column

<to_id>IRPT_ANLREQ.TO-AR-y-308</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~122</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>ZC</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-308` (`decompositions/IRPT_ANLREQ_DECOMP_R38A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~122`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-122` (branch `wk-IRPT_ANLREQ-122`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~122 <0.9.0_WK_IRPT_ANLREQ~122@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W122-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no `aws` call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-308`, inlined) -- BUILD ONLY. Nothing is released, applied or called live.

*The finding (row `IRPT_ANLREQ-D2-S94`; the release-28 door sitting, `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r28/DOOR_RESULT.txt`, line D3; the CTO's ruling msg 7546): a Shares file answers NEEDS_CORRECTION live because `infra/aws/lambda/investor-reporting/intake/upload_resolution.py :112` and `:133` compose the Shares price source as `_not_composed("SHARES_PRICE_SOURCE_NOT_COMPOSED")`. FWD-1's first journey is proven with a market-value file; Shares is an enrichment. The refusal stays. What is missing is the WORDS: the code `SHARES_PRICE_SOURCE_NOT_COMPOSED` has NO entry in `CORRECTION_WORDS` (`intake/uploads.py`, the table beside `SHARES_PRICE_UNAVAILABLE` at :111) nor in the status envelope's copy (`ops/status.py`), so a person is turned back with no sentence (`template_reader.finding(code)` returns a bare record: severity ERROR, actions REPLACE_FILE). The CTO asks that the words say it plainly: this file lists shares, we cannot price shares yet, give each holding as a market value in dollars (a Market Value column) and upload again. The same gap may exist for `CSV_LANE_NOT_COMPOSED` and any other `_not_composed` code the door can answer: census them.*

1. **Read first:** `infra/aws/lambda/investor-reporting/intake/upload_resolution.py` (:90-140: `_not_composed` and every code it is called with), `infra/aws/lambda/investor-reporting/intake/uploads.py` (`CORRECTION_WORDS` and how a finding's words are looked up and returned to the person; :105-165, the AR-y-293 additions at :158 and the lock), `infra/aws/lambda/investor-reporting/ops/status.py` (`CORRECTION_WORDS`, the literal copy), `infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py` (the lock: the two tables must be equal and the count of codes is pinned; the AR-y-293 worker changed it 30 to 33), `infra/aws/lambda/investor-reporting/intake/tests/test_kept_holding.py` and `test_deferred_resolution.py :160-175`. Find, with `Grep`, EVERY code that `_not_composed(...)` can raise through the door (print the list, the denominator being the call sites) and say, for each, whether it has words today and whether a person can reach it live.
2. **Write the words** for `SHARES_PRICE_SOURCE_NOT_COMPOSED` in BOTH tables, byte-equal: plain English a client can act on, in the style of the neighbouring entries (read five), ASCII only, no jargon, no mention of systems: it must say that the file lists shares, that shares cannot be priced yet, and ask for each holding as a market value in dollars in a Market Value column, then to upload again. If another `_not_composed` code a person can reach has no words, add words for it too and list it; if one is unreachable live, leave it and say why. Change NOTHING else in either file: prove `ops/status.py` words-only by an AST comparison before and after (print it, as the AR-y-293 worker did).
3. **Tests:** edit `intake/tests/test_correction_words.py` ONLY for the code count (and list the edit); add `intake/tests/test_shares_not_composed_words.py` (at least 6 tests): the new code has words in both tables and they are byte-equal; the words contain the ask for a market value and no jargon from a printed list; a Shares template through the real `UploadService` path with the resolve_prices not composed returns NEEDS_CORRECTION whose finding carries those words (use the existing fakes in `test_deferred_resolution.py`); a market-value template is unaffected; the table lock still passes; the status envelope returns the same words for the code. `before_arm`: the new tests fail at HEAD.
4. **Write `r38/SHARES_WORDS.json`:** `read`, `codes_census` (every `_not_composed` code: words today, reachable live, action), `words` (the exact text added, both tables), `ast_words_only`, `tests` (counts, folders run: `intake/tests` and `ops/tests` with the baselines named), `before_arm`, `release_needs` (which packages carry `uploads.py` and `ops/status.py`: the door Lambda, `irpt-status`, the resident; N writers), `claim`, `not_read`.
5. **In your report:** the codes census in one line, the exact words, the AST proof, the counts.

### ACCEPTANCE

<criterion id="AR308-y-AC1" cell_refs="AR-y-308"><invocation>python C:/dev/wk-irpt-anlreq-122/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y308-words --root C:/dev/wk-irpt-anlreq-122</invocation><expect>Y308-WORDS-OK</expect></criterion>
`AR308-y-AC1`: the record lists every not-composed code with its words today, the words added are byte-equal in both tables and ask for a market-value column in plain English, ops/status.py is words-only by AST, and the new tests pass with the table lock.

<criterion id="AR308-y-AC2J" cell_refs="AR-y-308" judgment="true"/>
`AR308-y-AC2J` (judgment, graded at L9, never by you): the words say in plain English that shares cannot be priced yet and ask for a Market Value column in dollars, with no jargon, they are byte-equal in both tables, nothing else in either file changed, and the person sees them through the real upload path.

<expected_criteria>AR308-y-AC1 AR308-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~122/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/ops/status.py
infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py
infra/aws/lambda/investor-reporting/intake/tests/test_shares_not_composed_words.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R38A_Y.md</decomp_doc>
<owned_cells>AR-y-308</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~122/IRPT_ANLREQ.TO-AR-y-308.shares-not-composed-words.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-308`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR308-y-AC1,AR308-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two words tables and their tests under the investor-reporting source tree; no live call; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the door sitting's D3 line and the words table against the cell; the lens: words that exist in one table and not the other, words that name a system instead of telling the person what to do, a code the person cannot reach counted as fixed. The order requires byte-equal tables, an AST words-only proof and the words seen through the real upload path. NOT seen: the portal's rendering of the words (0 portal files read). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on row `D2-S94` and the CTO's ruling (msg 7546, item 1) as workstream `ZC` round 38. Base: `AR308-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
