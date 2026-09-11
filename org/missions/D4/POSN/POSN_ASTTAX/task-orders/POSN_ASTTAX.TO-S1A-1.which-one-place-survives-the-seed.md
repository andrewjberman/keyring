# TO POSN_ASTTAX.TO-S1A-1 -- FWD-5: the SERVING source is settled (ETFClassifier). This order measures the AUTHORING end -- whether the DynamoDB table or the hardcoded dict is the place a change SURVIVES -- and the seed trigger nobody has measured (AT1-s-1 / S1-a, FWD-5)

<to_id>POSN_ASTTAX.TO-S1A-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~1</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending</status>

**Directive:** D4 "Positioning" · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.1** (FWD-5) ·
**Decomp cell:** `AT1-s-1` (readable name: S1-a MAKE ONE PLACE THE ONE PLACE) · **Issuance:** round 1, ONE cell (the decomposition's chain puts S1-a alone).

---

## THE CELL

**FWD-5, verbatim from the PRD:** *"The classification is defined in one place and flows everywhere."*
**DONE WHEN (EXERCISED):** *"someone changed where a class boundary sits in the single source, and every place reflected
it without being edited itself."* **ACCEPT:** *"A person changes an asset-class definition once, in one place, and
everywhere that shows asset classes updates on its own -- nobody edits each place by hand."*

⭐ **HALF OF THIS IS ALREADY SETTLED AND YOU ARE NOT RE-OPENING IT.** Andrew-direct 2026-09-11 ~04:2xZ,
VERBATIM: *"I think ETFClassifier is the real one"* / *"check to see what is already hooked up to Positioning page
thats how youll kow for sure."* The issuer executed that and it held: `yang-generate-positioning/lambda_function.py:25`
imports `ETFClassifier`, `:31` instantiates it. **The SERVING source is ETFClassifier reading DynamoDB
`etf-classifications`. Do not re-litigate it; AC1 and AC2 simply re-take that reading at your own vintage.**

⛔ **WHAT IS NOT SETTLED, AND IS THE WHOLE POINT OF THIS ORDER.** The issuer found that
`seed-etf-classifications.py:58` writes that table FROM `ETF_CLASSIFICATIONS` -- the hardcoded dict in
`_shared/etf_classification.py`. So it is **one chain, not a fork**:

```
  _shared/etf_classification.py (hardcoded dict)  --seed-->  DynamoDB etf-classifications  --ETFClassifier-->  Positioning
            [AUTHORING?]                                            [STORE]                       [SERVING, settled]
```

**FWD-5's bar is "change it in ONE place and everywhere reflects it." Today there are TWO candidate one-places with
OPPOSITE failure modes, and nobody has measured which one a change survives:**
- change the **TABLE** -> Positioning serves it immediately, **and the next seed run overwrites it from the dict**;
- change the **DICT** -> durable, **but nothing serves it until the seed re-runs** -- and **the seed's trigger is
  UNMEASURED.** Nobody on this project knows whether that script is scheduled, CI-invoked, or has only ever been run
  by hand.

**This order MEASURES. It changes nothing.** The architecture decision it feeds belongs to L9/the issuer.

## GROUNDING -- read by the issuer 2026-09-11 ~04:1x-04:3xZ. PHASE 1 IS TO RE-TAKE IT, NOT TO TRUST IT.

| thing | issuer's read | where |
|---|---|---|
| the serving import | `from etf_classifications_dynamodb import ETFClassifier` / `etf_classifier = ETFClassifier()` | `yang-generate-positioning/lambda_function.py:25,:31` |
| the second Positioning lambda | vendors the same module | `yang-generate-holdings-attribution/` |
| the seed | `"asset_class": ETF_CLASSIFICATIONS.get(ticker, "unknown")` | `yang_pipeline/seed-etf-classifications.py:58` |
| the two modules' self-claims | **BOTH** say "single source of truth" -- which is why neither text can settle this | `etf_classification.py:39`, `etf_classifications_dynamodb.py:7` |
| documented vocabularies | hardcoded THREE (`fixed_income\|equity\|other`, `:38`); DynamoDB FOUR (`...\|hedge\|unknown`, `:91`) | as cited |
| the LIVE Positioning vocabulary | **FOUR** -- `cash \| fixed_income \| equity \| hedge` | `yang-generate-positioning/lambda_function.py:362-368` |
| unknown-ticker defaults | **THREE, and they DISAGREE** -- `:209` -> `fixed_income`, `:360` and `:520` -> `equity` | same file |
| the CMA surface | `yang-generate-cma/` vendors **no** classifier module | `yang_pipeline/cma/` |

## THE ACT, IN ORDER

1. **Re-take the grounding** = `S1a-AC1`, `S1a-AC2`, `S1a-AC3`. Any difference from the table above is a ROW -- file it
   and keep working; it does not stop this order (this is a measurement cell, so a changed world is data, not a blocker).
2. **Measure the STORE** (`S1a-AC4`) and then **the drift** (`S1a-AC5`) -- AC5 is the decisive measurement of this order.
   Write a short python script under your deliverables dir that loads `ETF_CLASSIFICATIONS` from the hardcoded module,
   scans the DynamoDB table, and prints **both denominators and the exact disagreement set**. Print the denominator
   even when the disagreement set is empty; a bare "they agree" with no count is not an answer.
3. **Measure the seed TRIGGER** (`S1a-AC6`) -- the thing nobody has measured. ⛔ **A ZERO HERE IS A REAL RESULT AND MUST
   BE REPORTED AS ONE, not converted into "it must run somehow."** If no scheduler, event rule, CI job or deploy script
   invokes it, say so with the denominator of what you searched.
4. **Re-take the two live-code readings** (`S1a-AC7`, `S1a-AC8`) at your own vintage.
5. **Run the negative control** (`S1a-AC9`): the classifier consumer set is the enumerated one and no other.
5a. **Record Andrew's three named Cottonwood holdings in BOTH stores** (`S1a-AC11`, `S1a-AC12`) and state whether the two agree on each.
6. Write the instance, run the checker from inside your worktree, flip `complete` only if every mechanical criterion
   PASSES, commit once, report once.

## BOUNDS

- ⛔ **THIS ORDER CHANGES NOTHING. READ-ONLY, EVERYWHERE.** No edit to either classifier module, the seed script, the
  DynamoDB table, any lambda, any Terraform, any schedule. **No `put-item`, no `delete-item`, no `update-item`, no
  deploy, no invoke of the seed script.** If a measurement seems to call for a write, that is a ROW, not an act.
- ⛔ **DO NOT DECIDE FWD-5's "ONE PLACE."** Naming which end becomes the single source is an architecture call graded at
  L9 and made by the issuer on your facts. `S1a-AC10` is where you record what the instruments read **and offer no
  verdict.** An order that measures and then rules has graded its own homework.
- ⛔ **DO NOT PRE-JUDGE THE FIVE CLASSES OR THE EDGES.** `C-MEMBERSHIP-AT-L5` reserves the class edges to a later cell.
  This order reports the vocabulary that EXISTS; it does not propose the one that should.
- **Reads only, under this device's operator credentials.** A DynamoDB `scan` of `etf-classifications` is a read; if it
  paginates, paginate it and **count client-side** -- `--query length()` on a paginated `list-*` returns the PAGE count.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY; ids
  `POSN_ASTTAX-Z-W1-S<n>`; carry `project`, `fabric`, `spec_asserts`, `world_is`, `class`, `hazard_standing`,
  `disposition`, `disarm_owner`; append ONE new fenced ```json block at the END, never edit an existing row) -- then
  keep working. Never a message; you have no send tool.
  ⛔ **THAT FILE DOES NOT EXIST YET AND YOU MINT IT WITH YOUR FIRST ROW.** The issuer tried to open it empty so the
  path would resolve and `.tools/surprise-row-gate.py` REFUSED the commit: *"target file yields ZERO rows. A channel
  file mints on an item; zero is an empty mint or an unparsed body, and both are refused."* **A channel is created BY
  a finding, never in advance.** Your `<paths>` grant already covers creating it. If you have nothing to surface, the
  correct end state is NO channel file at all -- do not mint an empty one to look thorough.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~1
  <0.9.0_WK_POSN_ASTTAX~1@opal.agent>" -F <msgfile> -- <paths>` (msgfile written by a NON-SHELL writer; **no non-ASCII
  in a commit message**; never `-m`; never pre-`git add`; never `GIT_COMMIT_AUTHOR_OVERRIDE`).
- **Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE**, using the worktree's own copy, with the expected
  ids listed in `<expected_criteria>`. It treats a tracked artifact with only unstaged edits as the CCX class: stage
  your exact path list for the check, confirm VALID, unstage, then `safe-commit`.
- Every criterion invocation runs under `timeout 120`; a timeout is recorded AS the output.
- ⛔ **`comp-find`/`comp-read` are the search rail and a census must NOT be piped into `head`/`tail`/`sed`** -- use the
  tool's own `--limit`/`--band`/`--files`/`--all`. The issuer tripped this three times authoring this face; it aborts
  the WHOLE bash call, so a later segment in the same call silently does not run.

## ACCEPTANCE CRITERIA

<criterion id="S1a-AC1" cell_refs="AT1-s-1"><invocation>timeout 120 grep -n "ETFClassifier" infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>at least two numbered lines, one an import of ETFClassifier from etf_classifications_dynamodb and one an instantiation, pasted verbatim.</expect></criterion> `S1a-AC1` -- THE SERVING SOURCE, RE-READ AT YOUR OWN VINTAGE RATHER THAN INHERITED FROM THE ISSUER.

<criterion id="S1a-AC2" cell_refs="AT1-s-1"><invocation>timeout 120 ls -1 infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/</invocation><expect>the listing contains etf_classifications_dynamodb.py, pasted verbatim.</expect></criterion> `S1a-AC2` -- THE SECOND POSITIONING LAMBDA VENDORS THE SAME MODULE.

<criterion id="S1a-AC3" cell_refs="AT1-s-1"><invocation>timeout 120 grep -n "ETF_CLASSIFICATIONS" infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py</invocation><expect>at least one numbered line showing the seed reading ETF_CLASSIFICATIONS to populate an asset_class value, pasted verbatim.</expect></criterion> `S1a-AC3` -- THE SEED WRITES THE STORE FROM THE HARDCODED DICT. **This is the line that makes the chain a chain and not a fork.**

<criterion id="S1a-AC4" cell_refs="AT1-s-1"><invocation>timeout 120 .tools/aws dynamodb describe-table --table-name etf-classifications --query 'Table.{n:TableName,c:ItemCount,s:TableStatus}' --output json</invocation><expect>the table exists with TableStatus ACTIVE and an ItemCount, pasted verbatim. Record that ItemCount is DynamoDB's ~6-hourly estimate and is NOT the authoritative count used by AC5.</expect></criterion> `S1a-AC4` -- THE STORE EXISTS, AND ITS CHEAP COUNT IS LABELLED AS AN ESTIMATE RATHER THAN QUOTED AS A DENOMINATOR.

<criterion id="S1a-AC5" cell_refs="AT1-s-1"><invocation>timeout 120 python &lt;your script&gt; --compare-table-to-dict</invocation><expect>three numbers printed together -- the dict's ticker count, the table's scanned item count, and the size of the disagreement set -- plus the disagreeing tickers enumerated with both values (dict says X, table says Y). An empty disagreement set is reported AS empty beside both denominators.</expect></criterion> `S1a-AC5` -- ⭐ **THE DECISIVE MEASUREMENT: DOES THE STORE STILL AGREE WITH ITS SEED?** A disagreement means the two candidate one-places have ALREADY diverged and someone's edit is being served or being overwritten right now. **Paginate the scan and count client-side.**

<criterion id="S1a-AC6" cell_refs="AT1-s-1"><invocation>timeout 300 comp-find 'seed-etf-classifications' --all</invocation><expect>the printed DENOMINATOR line recorded verbatim and the count of hits actually shown equal to it; then a stated verdict on whether ANY scheduler, EventBridge rule, CI workflow, deploy script or step function invokes the script -- with the denominator printed beside a zero if the answer is none.</expect></criterion> `S1a-AC6` -- **THE SEED TRIGGER, WHICH NOBODY HAS MEASURED.** ⛔ A ZERO IS A REAL RESULT. If nothing invokes it, FWD-5's "flows everywhere" has no mechanism at all, and that is THE FINDING rather than a gap in your search.
⛔ **`--all` IS LOAD-BEARING AND THE ISSUER GOT THIS WRONG FIRST.** This face originally said `--limit 40`. The issuer then RAN it: **90 hits, "PAGE 1 of 3"**. Forty of ninety is a PAGE, and CLAUDE.md rule 21 is explicit that a page is not an answer and that an early stop and a true absence read identically -- which is fatal to a criterion whose whole point is that a ZERO might be the finding. Do not reintroduce a limit, and do not stop at page 1.
⚠ **EXPECT TO MATCH YOURSELF:** this task order, the decomposition and the issuer's Andrew-direct record all contain the string and WILL appear in your hits. They are this project's own paperwork, not a trigger. Name them and exclude them from the verdict rather than silently dropping them from the count.

<criterion id="S1a-AC7" cell_refs="AT1-s-1"><invocation>timeout 120 sed -n '355,372p' infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>the branch set over asset_class values pasted verbatim, and the DISTINCT class values it branches on enumerated.</expect></criterion> `S1a-AC7` -- THE LIVE VOCABULARY, ENUMERATED FROM THE BRANCHES THAT ACTUALLY RUN.

<criterion id="S1a-AC8" cell_refs="AT1-s-1"><invocation>timeout 120 grep -n "Default to\|registry_field(ticker, 'asset_class'" infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>every numbered line pasted verbatim, THEN the subset whose field is `asset_class` separated out from the rest, each with its default value named, and a count of how many DISTINCT default values appear across the `asset_class` sites ONLY.</expect></criterion> `S1a-AC8` -- THE UNKNOWN-TICKER DEFAULTS AND WHETHER THEY AGREE WITH EACH OTHER. **The issuer read three `asset_class` sites carrying two different defaults; confirm or correct that at your vintage.** ⚠ **THE ISSUER RAN THIS INVOCATION BEFORE ISSUING IT AND IT RETURNS FOUR LINES, NOT THREE:** `:81` is a `management_style` default and is NOT one of the three. It is left in the pattern deliberately -- a narrower regex would hide whether OTHER fields share the same defaulting habit -- so the expect clause asks you to SEPARATE rather than to pre-filter. Do not silently drop it and do not count it.

<criterion id="S1a-AC9" cell_refs="AT1-s-1"><invocation>timeout 120 comp-find 'get_asset_class' --files --limit 25</invocation><expect>the printed DENOMINATOR and the full file list, pasted verbatim; and a stated verdict on whether any consumer exists OUTSIDE the set the issuer enumerated (the two _shared modules, opal-partners-data, yang-generate-etf-returns, and the two positioning lambdas).</expect></criterion> `S1a-AC9` -- NEGATIVE CONTROL ON THE CONSUMER SET. **A consumer the issuer did not see would change which "one place" is even reachable.**

<criterion id="S1a-AC10" cell_refs="AT1-s-1" judgment="true"/> `S1a-AC10` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9, NOT SELF-GRADED.** Given AC5's drift result and AC6's trigger result, which end of the chain -- the DynamoDB table or the hardcoded dict -- is the place where a class-boundary change SURVIVES and FLOWS, as FWD-5 requires. **Record what the instruments read and offer NO verdict.**

<criterion id="S1a-AC11" cell_refs="AT1-s-1"><invocation>timeout 120 comp-read infra/aws/lambda/v2_portal/_shared/etf_classification.py --enumerate 'GLD|VXX|CLIP'</invocation><expect>the printed DENOMINATOR and every hit, pasted verbatim; and the top-level asset_class value the SEEDING DICT carries for each of GLD, VXX and CLIP named separately from their sub_asset_class value.</expect></criterion> `S1a-AC11` -- THE AUTHORING END'S CLASS FOR ANDREW'S THREE NAMED COTTONWOOD HOLDINGS.

<criterion id="S1a-AC12" cell_refs="AT1-s-1"><invocation>timeout 120 .tools/aws dynamodb batch-get-item --request-items '{"etf-classifications":{"Keys":[{"ticker":{"S":"GLD"}},{"ticker":{"S":"VXX"}},{"ticker":{"S":"CLIP"}}]}}' --query 'Responses."etf-classifications"[].{t:ticker.S,a:asset_class.S,s:sub_asset_class.S}' --output json</invocation><expect>all three tickers returned with their asset_class and sub_asset_class, pasted verbatim; and a stated comparison against AC11 saying whether the SERVED store and the SEEDING dict agree on each of the three.</expect></criterion> `S1a-AC12` -- ⭐ **THE SERVED CLASS FOR THE SAME THREE, AND THE POINT OF THE PAIR IS THE COMPARISON.** Andrew-direct 2026-09-11 ~05:3xZ (relayed 21210) says the Cottonwood satellites' key assets "should be included in ETFClassifier ... and they are not". **The issuer measured this at the cut and found they ARE present and MIS-CLASSIFIED, not absent** -- VXX served `equity` (a VIX futures ETN), GLD served `hedge`, while `sub_asset_class` already reads `Volatility` and `Gold` correctly. ⛔ **RE-TAKE IT; DO NOT INHERIT IT.** These two criteria exist so round 1 records that state at ITS OWN VINTAGE rather than citing a message. ⚠ **AND DO NOT WIDEN:** three tickers are measured because Andrew's file flags three. The 228-row sweep of his file against the classifier is NOT this order's -- naming it here so a later cell can claim it.

<expected_criteria>S1a-AC1, S1a-AC2, S1a-AC3, S1a-AC4, S1a-AC5, S1a-AC6, S1a-AC7, S1a-AC8, S1a-AC9, S1a-AC11, S1a-AC12, S1a-AC10</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S1A-1.which-one-place-survives-the-seed.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~1/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round1.md</decomp_doc> round 1, cell `AT1-s-1` (readable name S1-a). The project's full seven-cell rectangle is POSN_ASTTAX_DECOMP.md; this order is graded against ROUND 1's slice of it, which is this one cell.
<owned_cells>AT1-s-1</owned_cells>
Read-dependencies, NOT claimed: none -- AT1-s-1 is the head of the chain and has no predecessor cell. The six cells that
follow it (AT1-s-2 .. AT1-s-7) are NOT cut and are NOT yours; the decomposition states that AT1-s-1 runs
alone because every later cell writes a class definition and must write it where it survives the seed.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell builds no scheduled job, no monitor and no alerting; it MEASURES
whether an existing script has a trigger and changes nothing about any cadence. Per CLAUDE.md's standing moratorium, a
finding that the seed has no trigger is a ROW and a report, and is explicitly NOT authorization for this order or any
successor to build one.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, Lambda or Terraform is touched. The DynamoDB reads
(describe-table, scan) run under this device's operator credentials. Stated rather than implied: if a read is DENIED,
that is a ROW naming the missing permission, never an IAM edit by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool at this cut, and the reason is stated rather than implied: every referent in this face was read live by the issuer 2026-09-11 ~04:1x-04:3xZ
and is cited with file:line. AC1, AC2 and AC3 re-take the three readings the whole chain rests on, so an issuer error
in the grounding table surfaces as a criterion failure rather than as an inherited premise. ⚠ NOT covered: the issuer
never read the DynamoDB table itself (AC4/AC5 are its first read) and never established the seed trigger (AC6). Those
two are UNMEASURED at the cut and are the reason this order exists.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~1/POSN_ASTTAX.TO-S1A-1.which-one-place-survives-the-seed.proof_of_spec.json
</proof_of_spec>
