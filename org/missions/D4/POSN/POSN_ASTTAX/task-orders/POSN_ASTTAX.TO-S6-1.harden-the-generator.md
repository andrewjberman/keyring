# TO POSN_ASTTAX.TO-S6-1 -- HARDEN the positioning generator so an unexpected classification value cannot blank the page. ABSOLUTE FIRST: nothing in round 2 may precede it (AT2-s-6, FWD-1)

<to_id>POSN_ASTTAX.TO-S6-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~2</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-6` · **Issuance:** round 2, 7 cells. **THIS IS THE CHAIN HEAD.**

---

## THE CELL

⛔ **THE SERVED POSITIONING PAGE FOR ALL FOUR PARTNER FIRMS IS ONE UNEXPECTED CLASSIFICATION VALUE AWAY
FROM BLANK, AND ROUND 2 IS ABOUT TO INTRODUCE TWO.** This order removes that before anything else runs.

`C-RETAG-SAFETY` (PRD v0.5) step **(0)**: harden the generator -- treat `"unknown"` as falsy in the
default guard, AND make both allocation dicts tolerate a key they do not carry.

**MEASURED BY THE ISSUER, three lines of one file (re-take them; do not inherit):**
```
  :221-226  asset_allocations = {'cash':0,'fixed_income':0,'equity':0,'hedge':0}   FOUR FIXED KEYS
  :228-231  management_allocations = {'active':0,'passive':0}                      TWO FIXED KEYS
  :207-209  classify_etf(t) -> registry_field(t,'asset_class','fixed_income')      RAW registry value
  :239      asset_allocations[asset_class]      += weight*100    DIRECT SUBSCRIPT, no .get()
  :243      management_allocations[mgmt_style]  += weight*100    DIRECT SUBSCRIPT, no .get()
  :72,:81   `value if value else default`  -- CANNOT fire on the TRUTHY placeholder "unknown"
```
`calculate_allocations()` is called unconditionally per model book (`:1917`, `:1926`). A `KeyError`
there kills the generator, `positioning_data.json` is never rewritten, and the page blanks for all four
firms. **187 of 285 registry rows carry `management_style: "unknown"`; 0 of the ~30 currently-held do --
that is the only reason the page works today.**

## THE ACT

1. **Re-take the six readings above** (`S6-AC1`..`S6-AC3`). A difference is a ROW, and if the shapes have
   changed materially, STOP and file rather than improvise a different fix.
2. **Make the default guard treat `"unknown"` as falsy** -- a placeholder must not defeat a default.
3. **Make BOTH allocation dicts tolerate an unexpected key** without raising. ⚠ **TOLERATE MEANS DO NOT
   CRASH AND DO NOT SILENTLY SWALLOW:** an unexpected class must still be countable and visible, not
   dropped into a void. How is yours to choose -- `defaultdict`, an explicit bucket, or an `.get()` with
   an accumulating "unclassified" key -- but **state which and why in the instance**, and the page must
   still render with an unexpected value present.
4. **Prove it with a NEGATIVE CONTROL THAT MUST FAIL ON THE OLD CODE** (`S6-AC5`): exercise
   `calculate_allocations()` with a holding whose `asset_class` is `Commodities`, and show it raises on
   the pre-fix code and does not after. **A test that passes both ways proves nothing.**
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RETAG ANYTHING.** No registry write of any kind -- no `put-item`, `update-item`,
  `delete-item`. This order changes CODE only. The retag is `AT2-s-2` and is explicitly a later cell.
- ⛔ **DO NOT DEPLOY.** Commit the source change; deployment is not in this order's surface and
  `aws lambda update-function-code` is forbidden estate-wide (Terraform only).
- ⛔ **DO NOT "FIX" THE UNKNOWN-DEFAULT SEMANTICS** -- `:209` defaults to `fixed_income` while `:360`
  and `:520` default to `equity`. That disagreement is `AT2-s-1`'s cell, not yours. You make the guard
  fire correctly; you do not choose what it fires TO.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md`
  (lane ANY; ids `POSN_ASTTAX-Z-W2-S<n>`; append ONE fenced ```json block at the END, never edit an
  existing row) -- then keep working. Never a message; you have no send tool.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~2
  <0.9.0_WK_POSN_ASTTAX~2@opal.agent>" -F <msgfile> -- <paths>`; msgfile written by the Write tool, PURE
  ASCII, never `-m`, never pre-`git add`.
- **Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE** with the expected ids before flipping
  `<status>` to `complete`.
- ⛔ Never pipe a `comp-find`/`comp-read` census into `head`/`tail`/`sed` -- the rail denies it and the
  denial ABORTS THE WHOLE BASH CALL, so anything chained after it silently does not run.
- Every criterion invocation runs under `timeout 120`; a timeout is recorded AS the output.

## ACCEPTANCE CRITERIA

<criterion id="S6-AC1" cell_refs="AT2-s-6"><invocation>timeout 120 sed -n '218,246p' infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>both allocation dicts and both subscript sites pasted verbatim, with the literal keys of each dict enumerated and the two subscript line numbers named.</expect></criterion> `S6-AC1` -- THE TWO FIXED-KEY DICTS AND THE TWO UNGUARDED SUBSCRIPTS, RE-READ AT YOUR OWN VINTAGE.

<criterion id="S6-AC2" cell_refs="AT2-s-6"><invocation>timeout 120 sed -n '68,84p' infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>the default guard pasted verbatim, and a stated reading of whether the string "unknown" is truthy under it.</expect></criterion> `S6-AC2` -- THE GUARD THAT CANNOT FIRE ON A TRUTHY PLACEHOLDER.

<criterion id="S6-AC3" cell_refs="AT2-s-6"><invocation>timeout 120 .tools/aws dynamodb scan --table-name etf-classifications --filter-expression "management_style = :u" --expression-attribute-values '{":u":{"S":"unknown"}}' --select COUNT --output json</invocation><expect>the Count and ScannedCount pasted verbatim, with ScannedCount stated as the table denominator and any LastEvaluatedKey named (paginate and total client-side if present).</expect></criterion> `S6-AC3` -- HOW MANY ROWS CARRY THE PLACEHOLDER, COUNTED NOT QUOTED. The issuer read 187 of 285 from the DT brief and did NOT re-derive it; this is its first independent count.

<criterion id="S6-AC4" cell_refs="AT2-s-6"><invocation>timeout 120 python -c "import ast,sys; src=open('infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py',encoding='utf-8').read(); ast.parse(src); print('AST-OK', len(src.splitlines()), 'lines')"</invocation><expect>AST-OK with a line count, proving the edited file still parses.</expect></criterion> `S6-AC4` -- THE FILE STILL PARSES AFTER THE EDIT.

<criterion id="S6-AC5" cell_refs="AT2-s-6"><invocation>timeout 120 python &lt;your negative-control script&gt;</invocation><expect>TWO runs printed side by side: the PRE-FIX code raising KeyError on a holding whose asset_class is "Commodities", and the POST-FIX code completing and rendering that holding visibly. Both outputs pasted verbatim.</expect></criterion> `S6-AC5` -- ⭐ **THE CONTROL THAT MUST FAIL ON THE OLD BYTES.** A harness that passes before and after the change proves the change did nothing. Name how you obtained the pre-fix behaviour (git stash, a copy at HEAD, or a parameterised import).

<criterion id="S6-AC6" cell_refs="AT2-s-6"><invocation>timeout 120 git -C . diff --stat HEAD -- infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>the diffstat pasted verbatim, showing this order touched ONLY the generator file and no registry or infrastructure path.</expect></criterion> `S6-AC6` -- THE WRITE SURFACE STAYED INSIDE THE CELL.

<criterion id="S6-AC7" cell_refs="AT2-s-6" judgment="true"/> `S6-AC7` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9, NOT SELF-GRADED.** Whether an unexpected classification value is now both NON-FATAL and VISIBLE, rather than non-fatal by being silently discarded. **Record what the instruments read and offer NO verdict.**

<expected_criteria>S6-AC1, S6-AC2, S6-AC3, S6-AC4, S6-AC5, S6-AC6, S6-AC7</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~2/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-6`.
<owned_cells>AT2-s-6</owned_cells>
Read-dependencies, NOT claimed: none -- this is the chain head. Every other round-2 cell follows it.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting is built or changed; this
hardens an existing generator's in-process error handling.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform is touched. The one AWS call is a
read-only DynamoDB scan under this device's operator credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool; the reason is stated rather than implied:
every referent was read live by the issuer at 08:0xZ with file:line, and AC1-AC3 re-take all of them, so
an issuer error in the grounding surfaces as a criterion failure rather than as an inherited premise.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~2/POSN_ASTTAX.TO-S6-1.harden-the-generator.proof_of_spec.json
</proof_of_spec>
