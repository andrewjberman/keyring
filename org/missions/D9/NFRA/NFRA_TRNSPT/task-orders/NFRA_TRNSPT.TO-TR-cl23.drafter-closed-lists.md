# TO NFRA_TRNSPT.TO-TR-cl23 -- the drafter sends only closed-list values: account type and category names checked, themes withheld

<to_id>NFRA_TRNSPT.TO-TR-cl23</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>closedlists</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-cl-23` (`decompositions/NFRA_TRNSPT_DECOMP_R23.md`, AMENDMENT 1) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-cl-23` (CTO ruling msg 5761). The commentary drafter sends a prompt to an outside model. Three members of that prompt are free
text today: `account_type`, `themes`, and the NAMES of `holdings_categories`. Nothing produces them yet, so they are sent empty; but the
only filter in front of them is a length cap, so the day something does produce them a person's name would pass. Make the stop a check.

All changes are in `data/transcripts/scripts/commentary/drafter.py`, in what reaches the PROMPT. The slicer call inside `draft()` is
NOT changed (the slicer runs inside Opal; it may keep using the request's raw `account_type`).

1. **`account_type`.** Sent only if it is one of the estate's own account types: the names in `_ACCOUNT_RULES` of
   `data/transcripts/scripts/outlook/gold.py` plus its fallback `"household"` (today six values: roth, ira, 401k, brokerage, trust,
   household). Build the allowed set FROM that module at import; do not type the list again. Any other value: the prompt carries
   `null` for it, and it is counted.
2. **`holdings_categories`.** A category NAME is sent only if it is an `asset_class` value of the classification snapshot:
   the set of values of `classification.load_classifications()` in `data/transcripts/scripts/commentary/classification.py` (today six:
   alternatives, cash, commodities, equity, fixed_income, structured). Build the allowed set from that loader; do not type it. A name
   off the list is DROPPED with its weight (not renamed, not merged into another), and counted. When the request's value is a list
   rather than a dict, the same rule applies to each item.
3. **`themes`.** Never sent. The prompt's `themes` is always `[]`, whatever the request holds, and the number withheld is counted.
   (Themes stay free text until a rule for them is written and signed.)
4. **The counts.** `draft()`'s returned `provenance` gains one member, `"withheld"`, a dict with three integer counts:
   `{"account_type": 0 or 1, "holdings_categories": <names dropped>, "themes": <themes withheld>}`. Counts only: never the withheld text.
5. `yc_variant` and `comparison_keys` are unchanged. `PROMPT_FIELDS` keeps its five names.

**Tests**, in `data/transcripts/scripts/tests/test_commentary_drafter.py` (edit the existing tests that now fail because they expect
themes or an off-list category in the prompt, and add these five):
- `test_account_type_off_list_is_not_sent`: a request with `account_type` set to a person-like string -> the prompt's JSON has
  `"account_type": null`, the string appears nowhere in the prompt, `withheld["account_type"] == 1`.
- `test_account_type_on_list_is_sent`: `"ira"` is sent, `withheld["account_type"] == 0`.
- `test_category_off_list_is_dropped_and_counted`: `{"equity": 60, "A Person Name": 40}` -> only `equity` is in the prompt, the other
  string appears nowhere in it, `withheld["holdings_categories"] == 1`.
- `test_themes_are_never_sent`: a request with two themes -> the prompt's `themes` is `[]`, neither theme string appears in the
  prompt, `withheld["themes"] == 2`.
- `test_allowed_sets_come_from_the_estate`: the account-type set equals the gold module's rule names plus `household`, and the
  category set equals the set of the snapshot's `asset_class` values (so a change to either source changes the check).

### ACCEPTANCE

<criterion id="TR23-cl23-AC1" cell_refs="TR-cl-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R23_CHECKS/r23_checks.py cl23</invocation><expect>R23-CL23-OK</expect></criterion>
`TR23-cl23-AC1` -- the five named tests exist and the commentary test files pass together.

<expected_criteria>TR23-cl23-AC1</expected_criteria>

Dry-run at the base: `R23-CL23-FAIL missing test_account_type_off_list_is_not_sent, ...` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** No AWS or HTTP call, no model call, no deploy, no Terraform. No change to `entry.py`, `lambda_handler.py`, `gold.py`,
  `classification.py` or the slicer. ASCII only. Test strings are invented; use no real person's name.
- Run ONLY the acceptance check and the commentary test files it names. Do NOT run the whole tests directory (another test there
  rewrites a tracked fixture). If `git status` shows a path outside your grant modified, restore it with `git checkout -- <path>`.
- If importing the gold module's rules into the drafter creates an import cycle or pulls a heavy dependency (pandas, pyarrow) into
  the drafter's import, file a surprise row (`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`;
  recent rows are single-object json fenced blocks appended to INVESTIGATION_v1.md) naming it, and stop without typing the list.

<paths>
data/transcripts/scripts/commentary/drafter.py
data/transcripts/scripts/tests/test_commentary_drafter.py
data/transcripts/scripts/tests/test_commentary_seam.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.
`test_commentary_seam.py` is granted only so a test there that pins the old prompt can be updated; change nothing else in it.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R23.md</decomp_doc> (round 23, AMENDMENT 1), cell `TR-cl-23`.
<owned_cells>TR-cl-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR23-cl23-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-cl23.drafter-closed-lists.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR23-cl23-AC1` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the lines changed in `drafter.py`, where each allowed set is built from, the five test names with pass or fail, every
existing test edited and why, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repo build; the deploy to the commentary function is a later cell under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- sources: CTO ruling msg 5761, the issuer's reads PART2 @b29c8380cd and PART2b @7b8cf70a8b. Traps: a re-typed list that drifts from the estate's (the sets are built from gold.py and the snapshot, and a test holds that); the withheld TEXT leaking through the count or a log (counts only, tests assert the strings are absent from the prompt); an off-list category renamed into an allowed one (dropped, never mapped); the slicer's local use of account_type broken by the filter (the slicer call is untouched). BLIND: comparison_keys, the one member that IS sent today -- a separate read is owed on whether a firm can free-name a model.
lane: the paths block.
</preflight>

Source: CTO msg 5761; decomposition round 23 AMENDMENT 1, cell TR-cl-23.
