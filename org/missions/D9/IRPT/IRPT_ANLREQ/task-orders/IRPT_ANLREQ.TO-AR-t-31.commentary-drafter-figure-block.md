# TO-AR-t-31 -- the commentary drafter reads the report's abstract figures (consumer half of C-COMM-FIG v0.1; AR-t-31, round 41, workstream T)

<to_id>IRPT_ANLREQ.TO-AR-t-31</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~190</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>~T</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~T (commentary) | **Decomp cell:** `AR-t-31` (`decompositions/IRPT_ANLREQ_DECOMP_R41_T.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-t-31`: "`drafter.py` projects `commentary_basis.figures` through a closed whitelist of seven members, puts that block and nothing else figure-like in the
prompt, and records the prompt's field NAMES (never values) in the draft's provenance; `entry.py` carries the block from the reader's `commentary_basis` into the
abstract request. Fakes only; a planted client name and a dollar amount never reach the prompt."

Work in your worktree; every path is relative to its root. Today `data/transcripts/scripts/commentary/drafter.py` sends only `PROMPT_FIELDS` (`yc_variant`,
`comparison_keys`, `account_type`, `themes` always `[]`, `holdings_categories`) and `data/transcripts/scripts/commentary/entry.py` `abstract_request` builds
`holdings_categories` from `commentary_basis.holdings_category_weights`. No figure reaches the prompt.

**The block** (the CTO's allowed list, ADDENDUM 1 (a); every member nullable; the reader returns it as `composition.commentary_basis.figures`):

| member | shape the drafter accepts |
|---|---|
| `variant` | integer 1, 2 or 3 |
| `model_names` | list of strings, each at most 80 characters |
| `allocation_pct` | object: asset class string -> number, 0 to 100 |
| `sector_pct` | object: sector string -> number, 0 to 100 |
| `period_returns_pct` | object: period label -> number, -100 to 1000 |
| `benchmark_returns_pct` | object: period label -> number, -100 to 1000 |
| `top_holdings` | list of at most 10 objects `{ticker, weight_pct}`: `ticker` matches `^[A-Z0-9][A-Z0-9.\-]{0,9}$`, `weight_pct` a number 0 to 100 |

Period labels and class and sector keys are strings of at most 40 characters from `[A-Za-z0-9 &/_.\-]`. Any other key, any member of any other shape, any extra key
inside an object, and any value that is not a plain number (a bool, a string, a currency string) is DROPPED, not repaired; the drafter counts the drops in the draft's
`provenance.withheld` (a count per member, never a value).

**Build:**
1. `drafter.py`: a function `figures_block(figures, withheld=None) -> dict` implementing the table above (pure; no I/O). `abstract_fields(request, withheld)` adds
   a `"figures"` key from `request.get("figures")` through it; `PROMPT_FIELDS` gains `"figures"`. `build_prompt` prints the figures once, inside the existing
   `REQUEST (abstract fields)` JSON; nothing else figure-like is added. `draft()` adds `provenance["prompt_fields"]`: the sorted list of field NAMES present in the
   prompt's abstract block with a count of items for list and object members, for example `{"figures.top_holdings": 7}`; never a value. The no-precedent text stays as it is.
2. `entry.py`: `ABSTRACT_KEYS` gains `"figures"`; `abstract_request` copies `basis.get("figures")` into the request unchanged (the whitelist is the drafter's job, so the
   request may carry what the reader gave). Absent or null figures leave the request exactly as it is today.
3. `data/transcripts/scripts/tests/test_commentary_figures.py` (new, fakes only, no network) with exactly these four tests:
   - `test_figures_whitelist_drops_unknown_members_and_bad_tickers`: an unknown member, a ticker `"Acme Corp"`, a bool weight and a string `"$12,000"` are all dropped; the counts are in `withheld`; a clean block passes unchanged.
   - `test_prompt_carries_figures_block_and_no_planted_name_or_dollar`: a request whose basis ALSO carries planted `client_name`, `account_number` and `"$1,250,000"` strings (as extra keys and as values) yields a prompt containing the clean figures and none of the planted strings (the control arm: the same request without the figures yields a prompt without a `figures` member).
   - `test_provenance_lists_prompt_fields_by_name_only`: `draft(...)`'s `provenance["prompt_fields"]` names fields and counts, and no value from the figures appears in the provenance.
   - `test_abstract_request_carries_figures_from_basis`: `entry.abstract_request` fed a fake composition reader whose document has `commentary_basis.figures` returns a request with that block under `"figures"`; with no `figures` the request has no such key.
   Keep every existing `test_commentary_*.py` green.

### AMENDMENT 1 (issuer, 2026-10-15 ~17:0xZ) -- RE-OPENED: the three rows you filed, ruled

- **S1 (BLOCKING, your sparse cone).** My provisioning defect, not a grant change: the cone now includes `data/transcripts/scripts/outlook` (run `git sparse-checkout list` to see it; if it is still absent, run `git sparse-checkout add data/transcripts/scripts/outlook`). `<paths>` is unchanged. Re-run AC1 and AC2 from the real tree, not from a stub, and remove your stub from the evidence.
- **S2 (OBSERVATION, `OPTIONAL_ABSTRACT_KEYS`).** Accepted as you built it: `figures` rides in `OPTIONAL_ABSTRACT_KEYS`, `ABSTRACT_KEYS` stays exactly as it is, and `test_commentary_classification.py` stays untouched. Build item 2's wording about `ABSTRACT_KEYS` is superseded by this.
- **S3 (OBSERVATION, name-shaped labels) -- the label vocabulary is CLOSED, not a charset.** Replace the charset rule with these, drop-and-count on any miss (never repair):
  - `allocation_pct` keys must be members of `ALLOWED_CATEGORIES` (`drafter.py:34`, the estate's asset-class values from the classification snapshot).
  - `period_returns_pct` and `benchmark_returns_pct` keys must be one of `1M 3M 6M YTD 1Y 3Y 5Y 10Y SI` (the contract's v0.1 list; the producer may amend it).
  - `sector_pct`: the estate holds no sector vocabulary (the classification snapshot carries `ticker`, `asset_class`, `sub_asset_class` only). Until the producer names a closed sector list the member is DROPPED ENTIRELY and counted as `figures.sector_pct`; the table row for it stays so the shape is ready.
  - `model_names` stay a list of strings of at most 80 characters, no further rule this round.
  Extend `test_figures_whitelist_drops_unknown_members_and_bad_tickers` with three arms: allocation key `"Smith Family Trust"` dropped, period key `"Smith"` dropped, a whole `sector_pct` member dropped and counted.

### ACCEPTANCE

<criterion id="AR31-t-AC1" cell_refs="AR-t-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R41_CHECKS/r41_checks.py fg1</invocation><expect>R41-FG1-OK</expect></criterion>
`AR31-t-AC1` -- the three drafter tests pass (whitelist, the planted-name and dollar control, provenance by name). Dry-run at box/dell2 32a08883b0: `R41-FG1-FAIL absent` -- FAIL as expected.

<criterion id="AR31-t-AC2" cell_refs="AR-t-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R41_CHECKS/r41_checks.py fg2</invocation><expect>R41-FG2-OK</expect></criterion>
`AR31-t-AC2` -- the seam test passes: `entry.abstract_request` carries the reader's figures block. Dry-run at the same base: `R41-FG2-FAIL absent` -- FAIL as expected. The seam's real neighbour (the reader) does not return figures yet, so the probe is a fixture.

<expected_criteria>AR31-t-AC1 AR31-t-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **No network, no AWS, no secret.** Fakes only. You deploy nothing; the built Lambda package under `infra/aws/lambda/transcripts-pull/dist/` is output and is not yours.
- **C-KIMI.** The prompt carries no client, household, advisor or firm name, no account number, no dollar amount and no raw row. The whitelist is a closed list; do not widen it.
- **Refusal clause.** If the figures member names in the table clash with a `figures` shape already present in `entry.py` or its tests at your base, keep the table, file a
  surprise row (`IRPT_ANLREQ-D2-W190-S<k>`, next unused under `surprise-channel/`) and say so in the report. Write no code outside the paths below.

<paths>
data/transcripts/scripts/commentary/drafter.py
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/tests/test_commentary_figures.py
data/transcripts/scripts/tests/test_commentary_drafter.py
data/transcripts/scripts/tests/test_commentary_entry.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R41_T.md</decomp_doc> (round 41, workstream T), cell `AR-t-31`.
<owned_cells>AR-t-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR31-t-AC1, AR31-t-AC2. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~190/IRPT_ANLREQ.TO-AR-t-31.commentary-drafter-figure-block.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR31-t-AC1,AR31-t-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the whitelist function and where the prompt and provenance use it, the entry change, the four test names, both check lines, commits.

---

<preflight>
comp-blast: RUN (by reading) -- `drafter.py` and `entry.py` are imported by `commentary/lambda_handler.py` and by the packaged copy under `infra/aws/lambda/transcripts-pull/dist/` (build output, not edited here); the change adds a prompt member and a provenance key and removes none, so the importers keep working. Nothing is deployed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change; fakes only.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage 965eee9a03 declared the neighborhood: the decomposition and PRD FWD-10, 0 unproven dependencies, the two cited paths absent only because they are this order's own outputs. Traps named for the worker: a whitelist that repairs a bad value instead of dropping it; a planted string reaching the prompt through an extra key; a provenance that records a value rather than a name.
</preflight>

- Cut on CTO ADDENDUM 1 (a) @d0323f6e0d and the erratum @1822f49820 (msg 8392, 8405), lane COMMENTARY. Risk LOCAL: new source members and tests, nothing deployed or called.
- Base: `AR31-t-AC1` and `AC2` FAIL as expected (`R41-FG1-FAIL absent`, `R41-FG2-FAIL absent`) at box/dell2 32a08883b0, run by the issuer before the cut.
