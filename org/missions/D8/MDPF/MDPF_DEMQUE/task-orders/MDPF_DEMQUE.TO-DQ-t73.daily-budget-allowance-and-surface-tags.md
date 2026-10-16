# TO MDPF_DEMQUE.TO-DQ-t73 -- round 9 DQ-t-73: the 2.5M-cell daily Bloomberg budget in the allowance file, and a surface tag on every queued Bloomberg request
<to_id>MDPF_DEMQUE.TO-DQ-t73</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~63</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>BUDGET</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-73` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 32) |
**outcome_ref:** C-PRICES, C-RESERVE | **depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew approved a daily Bloomberg budget of 2,500,000 cells split over five surfaces, and the CTO ruled dell1's half as ONE cell. **This cell writes the budget into `data/mdpf/scripts/demque/bbg_allowance.json` as a new top-level `budgets` block, and tags every queued Bloomberg request with its surface.** It moves nothing served: `history.ceiling` stays 5858 (measured), `bql.ceiling` stays 2920000 (measured), no quote changes, no code the drawer reads changes. It makes no vendor call and writes no S3 object.

Read first (in full): `data/mdpf/scripts/demque/bbg_allowance.json`, `bbg_quote.py` lines 460-500 and 736-740 (`_claim`, `_figure`, `_load`: they look up a CHANNEL key by name, so a new top-level key `budgets` is never read as a channel), `ceiling_from_ledger.py` and `reserve_estimate.py` (both rewrite the file: your block must survive them). Import, do not copy. The test files in that folder are `test_demque_*.py` (pytest, no network).

**Build**
1. **`bbg_allowance.json`**: add the top-level key `budgets` (leave every existing key and value as it is; keep the file's indent style). Exactly this shape, every figure with `value` or `values`, a `claim` and a `basis`:
   - `daily_total`: `{value: 2500000, claim: "held", basis: "Andrew-direct 2026-10-16 ~15:5xZ, cap at 2.5M of the 2.92M measured block (bql.ceiling, 2026-10-05); the margin to the block is 420000"}`
   - `surfaces`: `A` 350000 (also `first_claim: true`; basis "A3 at its 150000-row ceiling x 2 fields is about 300000 (inferred) plus A1, A2, A4, A5; A is served before any other surface on every fire"), `B` 1500000 (basis "client history, the sink; the Cottonwood share waits for the first tranche's 50 percent resolve rate (CTO ruling 2026-10-16)"), `C` 400000 ("rival funds history; the 213149-cell backlog clears in about a day, then the producer's 20000-per-run cap governs"), `D` 100000 ("research; current demand about 2000"), `E` 150000 ("Opal ad hoc, including the Bloomberg terminal agent"). Each `claim: "held"`.
   - `e_request_cap`: `{value: 5000, claim: "held", basis: "per-request cap for surface E, was 585 (10 percent of the history ceiling); the intake that enforces it is site Z's, ruled by 1.0.0_SA_CTO~Z"}`
   - `unit_weight`: `{claim: "inferred", basis: "one history or reference cell is counted as one BQL cell; the weight of a history or reference cell against a BQL row is NOT measured (the 2.92M block is a BQL figure)"}` (no value)
   - `release_rule`: `{from: ["A","C","D","E"], to: "B", when: "the same day, unused room only", a_first_claim: true, claim: "held"}`
   - `ramp_steps`: `{values: [11716, 23432, 29290, 100000, 300000, 1000000, 2500000], claim: "held", basis: "the ceiling climbs by these steps, one clean drawing day each (no vendor warning, production's legs complete, per-surface meter sums equal the drawer's count); on the first warning or a missed production pull it holds at the last good step; CTO ruling 2026-10-16, msg 6824"}`
   - `owners`: `{A2: "2.0.0_SA_COO~H1", A3: "2.0.0_SA_COO~RV", A4: "2.0.0_SA_COO~R1", A1: null, A5: null, claim: "inferred", basis: "read from the project record; A1 and A5 are not established; Andrew-direct 2026-09-30 'do not modify the existing daily etfs pull for Positioning' binds A2 and A5, so any meter there is additive"}`
2. **`ceiling_from_ledger.py` / `reserve_estimate.py`**: read how each writes the file. If either would drop or reorder `budgets`, make the smallest change that keeps it (load, set the one slot, dump the same dict); if neither does, change neither.
3. **New `surface_tag.py`** (under `data/mdpf/scripts/demque/`): `surface_of(request: dict) -> str | None`: returns None unless `request["vendor"] == "bloomberg"`; else by the `page` text: starts with `client performance` -> `B`; `rival funds` -> `C`; `research` -> `D`; `Positioning` or `production daily pulls` -> `A`; any other page -> None (never guess). `tag_text(text: str, surface: str) -> str`: returns the file text with ONE added member `"surface": "<S>"` inserted by TEXT (if the text starts with `{` then a newline, insert a new line after that first line, indented like the next line, ending in a comma; if it starts with `{` on one line, insert `"surface": "<S>", ` right after the brace), so every other byte is unchanged; a text that already carries `"surface"` is returned unchanged. `apply(requests_dir) -> list` of `(file name, surface)` it tagged: for every `*.json` that is not a `.quote` file, parses as an object, and has a non-None `surface_of`, writes `tag_text(...)` and re-parses it (a parse failure restores the original and raises). CLI: `python surface_tag.py --apply DIR` prints the count tagged.
4. **Run it once** on `org/missions/D8/MDPF/MDPF_DEMQUE/requests`. A Bloomberg request whose page matches no rule is reported in your final message with its name and left untagged; do not guess. Yahoo and no-vendor files, and every `.quote` file, stay untouched.
5. **Tests** in a NEW `test_demque_budget.py` (pytest, temp dirs, no network) with exactly these names:
   `test_the_budget_block_sums_to_the_daily_total_and_every_figure_carries_its_claim` (the real file),
   `test_the_history_ceiling_and_a_quote_are_unchanged_by_the_budget_block` (history.ceiling 5858 measured; `bbg_quote.quote` of a small history request on the real allowance equals the same call on the allowance with `budgets` removed),
   `test_a_ceiling_or_reserve_write_keeps_the_budget_block` (run the real write path of `ceiling_from_ledger` and of `reserve_estimate` on a temp COPY of the file; `budgets` is equal afterwards),
   `test_surface_of_maps_each_page_family_and_refuses_to_guess`,
   `test_apply_tags_a_bloomberg_request_by_text_insertion_and_leaves_every_other_byte` (on temp files: both layouts; removing the inserted member gives the original bytes; an already tagged file is unchanged; a `.quote` file and a Yahoo file are untouched).
   Edit an existing test ONLY if it fails because it pins the allowance file's exact key set or a request file's exact bytes; name each edit and why in your report. Run the whole folder once: no failure.
6. **Report** the files, the three criteria's output, the count tagged, any untagged Bloomberg request, every edited existing test and why, the folder count, commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t73-AC1" cell_refs="DQ-t-73"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t73_tests.py</invocation><expect>BUDGT-OK</expect></criterion>
<criterion id="DQ9-t73-AC2" cell_refs="DQ-t-73"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t73_check.py</invocation><expect>BUDGT-OK</expect></criterion>
<criterion id="DQ9-t73-AC3" cell_refs="DQ-t-73"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t73_tags.py</invocation><expect>TAGS-OK</expect></criterion>

<expected_criteria>DQ9-t73-AC1,DQ9-t73-AC2,DQ9-t73-AC3</expected_criteria>

`DQ9-t73-AC1` -- the five named tests. `DQ9-t73-AC2` -- the real allowance file: the five budgets sum to 2,500,000, every figure carries a claim, and the served ceilings did not move. `DQ9-t73-AC3` -- every Bloomberg request file carries the surface its page implies, no other file does. Run each invocation from the worktree root. At the base: `BUDGT-BAD no file ...test_demque_budget.py`; `BUDGT-BAD no budgets block in bbg_allowance.json`; `TAGS-BAD AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json: surface is None, the rule says 'D'`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger, the queue state, the price store or any pacer state (`~/.opal/demque`); run no draw.** Do not merge anything; the issuer drains. Change no ceiling, no reserve, no quote file, no drawer code. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W63-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/bbg_allowance.json
data/mdpf/scripts/demque/surface_tag.py
data/mdpf/scripts/demque/test_demque_budget.py
data/mdpf/scripts/demque/test_demque_*.py
data/mdpf/scripts/demque/ceiling_from_ledger.py
data/mdpf/scripts/demque/reserve_estimate.py
org/missions/D8/MDPF/MDPF_DEMQUE/requests/*.json
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-73`.
<owned_cells>DQ-t-73</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t73-AC1, DQ9-t73-AC2, DQ9-t73-AC3. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~63/MDPF_DEMQUE.TO-DQ-t73.daily-budget-allowance-and-surface-tags.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t73-AC1,DQ9-t73-AC2,DQ9-t73-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the three checks' output, the count tagged, any untagged request, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE a data block and a text tag graded by tests and two read-only checks over the real files.
risk: LOCAL -- config data nothing served reads yet, a tag no code reads, and tests; the served ceilings, the quotes and the drawer's code do not move.
direct_act: true -- one cell, about 150 changed lines plus 59 one-line tags.
</preflight>

Source: Andrew-direct ~15:5xZ (record @f50271705e); CTO ruling `ledger/CTO_RULING_BBG_DAILY_BUDGET_2_5M_IMPLEMENTATION_20261016.md` (msg 6824); decomposition round 9, amendment 32.
