# TO IRPT_ANLREQ.TO-AR-y-362.fwd1-run3-holdings-unpriceable-row -- PRD v0.17: FWD-1 run 3 files one holding Opal cannot price as given; a new holdings csv for run 3 (SPY, AGG and one of BREIT, SREIT, KPEC chosen from source), offline

<to_id>IRPT_ANLREQ.TO-AR-y-362</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~159</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ23</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one csv and records in a deliverable folder; nothing is called, uploaded or filed)
**Decomp cell:** `AR-y-362` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (run 3 itself waits on r32 and r33)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~159`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-159` (branch `wk-IRPT_ANLREQ-159`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~159 <0.9.0_WK_IRPT_ANLREQ~159@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W159-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network, NO AWS call, NO push, no browser, no run of the driver. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree. Your worktree is sparse: if a source path you need is absent on disk, read it with `git show HEAD:<path>` and say so.

### THE CELL (`AR-y-362`, inlined)

*Context. PRD v0.17 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, section 'v0.17') says every holding Opal cannot price as given (`TICKER_DATA_NOT_ENTITLED`, a real security the provider does not cover, or a kept `TICKER_NOT_FOUND`) FILES, marked UNRESOLVED, and the report names the replacement; FWD-1 run 3 includes ONE such holding, one of `BREIT`, `SREIT`, `KPEC`. The run 1 and 2 holdings file is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_holdings_49financial.csv` (header `Ticker,Dollars,Acct Market Value`; rows `SPY,100,26000000` and `AGG,200,32000000`; sha256 `23cbe4eb0bdaf0a950b33f304b4d9e50830ab032ae154edb0d458bf5ec44c3be`) and stays untouched. The door is the Lambda `irpt-ycharts-generate` (source under `infra/aws/lambda/investor-reporting/` and its tests/fixtures).*

1. **Choose the row by source, offline.** From the door's source, its tests and fixtures (name searches printed in the record), decide for each of `BREIT`, `SREIT`, `KPEC`: does the current door classify it `TICKER_DATA_NOT_ENTITLED`, `TICKER_NOT_FOUND`, or priceable, and by which line/fixture? Pick the ONE the source classifies `TICKER_DATA_NOT_ENTITLED` (the class Andrew's PROD filing hit: a real fund the provider does not cover); if none is so classified by source, pick the one a fixture or the entitlement list names as uncovered and say it is the least-sure choice; never pick by name alone.
2. **Write the csv** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/fwd1_holdings_49financial_r41b.csv`: the same header; the same two rows (`SPY,100,26000000`, `AGG,200,32000000`) and ONE more row for the chosen ticker, `<TICKER>,50,5000000` (dollars 50 so the three rows stay in the shape of the signed run 1 file; ASCII, LF line ends, final newline).
3. **Write the record** `r41/RUN3_HOLDINGS.json` in the same folder: `chosen_ticker`, `classification` (the code), `evidence` (file, line, quoted bytes read with `git show` or the Read tool), `the_other_two` (each with its classification and evidence), `csv_sha256`, `csv_bytes`, `rows`, `claim`, `not_read` (the live door's answer for the chosen ticker; the provider's entitlement at run time). Then write the checker scripts named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="AR362-y-AC1" cell_refs="AR-y-362"><invocation>python C:/dev/wk-irpt-anlreq-159/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/csv_check.py</invocation><expect>^CSV-OK </expect></criterion>
`AR362-y-AC1`: you write `csv_check.py`: it prints `CSV-OK <n> rows, <ticker>, sha256 <first 12>` only when the csv in your deliverable folder has exactly the header and three data rows, the first two byte-identical to the base file's two rows, the third a ticker in {BREIT, SREIT, KPEC} matching `chosen_ticker` of `r41/RUN3_HOLDINGS.json`, ASCII only with LF endings and a final newline, and the record's `csv_sha256` equals the file's; otherwise `CSV-BAD <why>`, exit 1.

<criterion id="AR362-y-AC2" cell_refs="AR-y-362"><invocation>python C:/dev/wk-irpt-anlreq-159/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/base_check.py</invocation><expect>^BASE-OK </expect></criterion>
`AR362-y-AC2`: you write `base_check.py`: it prints `BASE-OK sha256 23cbe4eb0bdaf0a950b33f304b4d9e50830ab032ae154edb0d458bf5ec44c3be unchanged` only when `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_holdings_49financial.csv` and `fwd1_driver.mjs` and `fwd1_mint.py` in this worktree are byte-identical to `git show origin/box/dell2:<path>`-equivalent HEAD of the base commit (use `git diff --quiet <your base sha> -- <the three paths>`), the driver's sha256 is `ae008182f9ee3ad120ad9a9e7686dbb9e6cccaba360d8359253d3965e6329496` and the mint helper's is `04e4ba64ddb74895442a7b291e14862fc9b395b65cc814c75bb737b8445ec5d4`; otherwise `BASE-BAD <why>`, exit 1.

<criterion id="AR362-y-AC3" cell_refs="AR-y-362"><invocation>python C:/dev/wk-irpt-anlreq-159/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR362-y-AC3` (the one mutant that fails): you write `mutant_check.py`: it copies your csv to a scratch folder OUTSIDE the product tree with the third row's ticker changed to `ZZZZ`, runs `csv_check.py`'s check function against the copy, and prints `MUTANT-FIRES` only when the check fails on it (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR362-y-AC4J" cell_refs="AR-y-362" judgment="true"/>
`AR362-y-AC4J` (judgment, graded at L9, never by you): the chosen ticker is the one the source classifies as a real security the provider does not cover, the evidence is read bytes and not a name, and the record says plainly what it did not read.

<expected_criteria>AR362-y-AC1 AR362-y-AC2 AR362-y-AC3 AR362-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/` and this order's file (status flip only).
- READ only: everything else, the run 1 and 2 files above in particular. NO run of the driver or the mint helper; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-362</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/IRPT_ANLREQ.TO-AR-y-362.fwd1-run3-holdings-unpriceable-row.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-362`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR362-y-AC1,AR362-y-AC2,AR362-y-AC3,AR362-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one csv and records in a deliverable folder; nothing is called, uploaded or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading PRD v0.17 item 3 and the signed run files against the cell; the lens: a ticker picked by its name, a changed base row, the signed driver or helper touched, a csv the sparse worktree cannot hash the same, a mutant that does not fire. The cell requires source-read classification, byte-identical base rows and files, and a mutant that fails. NOT seen (blind): the live door and the provider's entitlement at run time; denominator: 3 candidate tickers, 3 base files, 3 checker files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 8688 (PRD v0.17): run 3 includes one holding Opal cannot price as given. Workstream `ZZ23` of round 40. Base: `AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- Run 3 still waits on ~G2's r32 and r33 and a new pair addendum 3 that will name this csv's sha256 beside the driver's and the helper's.
