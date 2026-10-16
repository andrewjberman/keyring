# TO IRPT_ANLREQ.TO-AR-y-368.run3-ticker-branches-from-door-source -- read the merged release-33 door source and its fixtures and say, with bytes, which tickers file down each v0.19 branch (clean, unknown WITH suggestion, unknown WITHOUT suggestion, real but unpriceable), then write run 3's holdings csv and decisions file from what the source establishes; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-368</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~165</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ29</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (records and two small input files in a deliverable folder; nothing is called, uploaded or filed)
**Decomp cell:** `AR-y-368` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-362` (the draft csv, merged `8332b32ef2`), `AR-y-367` (the driver, merged `b6500a74b9`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~165`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-165` (branch `wk-IRPT_ANLREQ-165`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~165 <0.9.0_WK_IRPT_ANLREQ~165@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W165-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, no browser, no run of the driver. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. Your worktree is SPARSE: if a source path you need is absent on disk, read it with `git show HEAD:<path>` and say so in the record; a path absent from HEAD too is a row, not a guess.

### THE CELL (`AR-y-368`, inlined)

*Context. FWD-1 run 3 must exercise every branch of PRD v0.19 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the C-FILING-HINT row and section 'v0.19'): (A1) a ticker that does not exist, WITH a door suggestion: the form asks `Did you mean X?` and the filer answers Yes, Replace or No; (A2) a ticker that does not exist, WITHOUT a suggestion: Replace or No; (B) a real security Opal cannot price: no prompt, filed UNRESOLVED with the door's notice; plus the clean rows SPY and AGG. The previous attempt (AR-y-362, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~159/r41/RUN3_HOLDINGS.json`) found that no source line classifies BREIT, SREIT or KPEC as `TICKER_DATA_NOT_ENTITLED` for a bare ticker (the door emits that code only when the entitlement is unverified, `portfolio.py` about lines 520 to 533 at that time) and picked BREIT as a least-sure fallback. The door's release-33 source is now merged: the findings follow the decision tree (AR-y-96/AR-g-96, commit `5ea4cab301`), the release-33 rows and ticket grant (AR-g-102, `bbd92e94c0`), the swap pass (`cff76bd439`). The door code lives under `infra/aws/lambda/investor-reporting/` (the intake and portfolio normalisation, and the Lambda `irpt-ycharts-generate`), with tests and pinned captures (a `securities_info`-style capture). Read it AT HEAD.*

1. **Trace the classification.** From the door source at HEAD, its tests and its pinned fixtures (name searches printed in the record), write for each branch the exact path: where a holding becomes `TICKER_NOT_FOUND`, where a `suggestion` is attached or left null (and from what data: a pinned list, a provider call, a fuzzy rule), where `TICKER_DATA_NOT_ENTITLED` is emitted (what input state makes it fire), and where the NOTICE words and actions (`REVIEW`, `REPLACE_FILE`, `REPLACE_TICKER`, `FILE_UNRESOLVED`, `ACCEPT_SUGGESTION`) are set. Quote the bytes with file and line.
2. **Find the tickers the source ESTABLISHES.** For each of A1, A2, B and clean, name concrete tickers whose branch the source plus a pinned fixture establish WITHOUT a live call (for example a symbol a fixture shows as NOT_FOUND with a suggestion, a symbol that no pinned list contains and no fuzzy rule matches, a symbol a fixture shows as entitlement-unverified). For a branch the offline source cannot establish (the suggestion or the entitlement comes from a live provider call), say `UNESTABLISHED-OFFLINE` with the reason and list up to three candidates a live read would have to check, never a guess presented as a finding.
3. **Write the inputs for the branches the source establishes**, in your folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~165/`: `fwd1_holdings_49financial_r41c.csv` (header `Ticker,Dollars,Acct Market Value`; first two rows byte-identical to the signed `SPY,100,26000000` and `AGG,200,32000000`; then ONE row per established branch among A1, A2, B in that order, `<TICKER>,50,5000000`; ASCII, LF, final newline; at most 5 data rows) and `fwd1_decisions_r41c.json` (the shape the driver's `--decisions` option validates: `{"decisions":[{"symbol":..., "answer":"yes"|"replace"|"no", "replacement":...}]}`): the A1 row answers `yes`; the A2 row answers `replace` with a replacement that is a real ticker the source shows as priceable and that is not already a row of the csv (name it with its evidence); if no A2 row is established, write no decision for it. Validate the decisions file with the driver's own validator by running `node <driver> --selftest` is NOT enough: import `validateDecisions` (or the exported name the driver has) in a small node check of yours and print its verdict.
4. **Record** `r41/RUN3_TICKER_BRANCHES.json`: per branch `established` or `UNESTABLISHED-OFFLINE`, the chosen tickers, `evidence` (file, line, quoted bytes), `reason_if_unestablished`, `candidates_for_a_live_read`; `csv_sha256`, `csv_bytes`, `decisions_sha256`, `validator_verdict`, `claim`, `not_read` (the live door's answers, the provider's entitlement and suggestion at run time, the deployed bytes). Then write the checker scripts named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="AR368-y-AC1" cell_refs="AR-y-368"><invocation>python C:/dev/wk-irpt-anlreq-165/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~165/inputs_check.py</invocation><expect>^INPUTS-OK </expect></criterion>
`AR368-y-AC1`: you write `inputs_check.py`: it prints `INPUTS-OK <n> rows, branches <list of established>, decisions valid, csv sha256 <first 12>` only when the csv has the exact header, the two signed first rows byte-identical, at most 5 data rows, one row per `established` branch in the record in the order A1, A2, B, ASCII with LF and a final newline; the decisions file passes the driver's validator (run it) and names only symbols present in the csv; the record's `csv_sha256` and `decisions_sha256` equal the files'; and every `established` branch carries evidence quoting bytes that really occur at the cited file and line (`git show HEAD:<path>`); otherwise `INPUTS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR368-y-AC2" cell_refs="AR-y-368"><invocation>python C:/dev/wk-irpt-anlreq-165/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~165/base_check.py</invocation><expect>^BASE-OK </expect></criterion>
`AR368-y-AC2`: you write `base_check.py`: it prints `BASE-OK driver sha256 455f660940bf34dd0de126d81ec0667df95d3030c7eb40621e26c1cb8eee1247, mint 04e4ba64..., run 1 csv 23cbe4eb... unchanged` only when the three files under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/` (the driver, `fwd1_mint.py`, `fwd1_holdings_49financial.csv`) are byte-identical to your base commit (`git diff --quiet <your base sha> -- <the three paths>`) and their sha256 values are the three named (the mint helper `04e4ba64ddb74895442a7b291e14862fc9b395b65cc814c75bb737b8445ec5d4`, the csv `23cbe4eb0bdaf0a950b33f304b4d9e50830ab032ae154edb0d458bf5ec44c3be`); otherwise `BASE-BAD <why>`, exit 1.

<criterion id="AR368-y-AC3" cell_refs="AR-y-368"><invocation>python C:/dev/wk-irpt-anlreq-165/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~165/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR368-y-AC3` (the one mutant that fails): you write `mutant_check.py`: it copies your decisions file to a scratch folder OUTSIDE the product tree with one symbol changed to one the csv does not contain, runs `inputs_check.py`'s check function against the copy, and prints `MUTANT-FIRES` only when the check fails on it (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR368-y-AC4J" cell_refs="AR-y-368" judgment="true"/>
`AR368-y-AC4J` (judgment, graded at L9, never by you): every `established` branch rests on source bytes and a fixture and not on a name; every branch the source cannot settle says `UNESTABLISHED-OFFLINE` with its reason and candidates; the record says plainly what it did not read.

<expected_criteria>AR368-y-AC1 AR368-y-AC2 AR368-y-AC3 AR368-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~165/` and this order's file (status flip only).
- READ only: everything else, the driver, the mint helper, the run 1 csv and worker 159's draft above all. NO run of the driver except what step 3's validator import does offline; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-368</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~165/IRPT_ANLREQ.TO-AR-y-368.run3-ticker-branches-from-door-source.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-368`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR368-y-AC1,AR368-y-AC2,AR368-y-AC3,AR368-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- records and two small input files in a deliverable folder; nothing is called, uploaded or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading worker 159's record (a ticker picked by its name when the source did not classify it) against the cell; the lens: a branch claimed established on a name, quoted bytes that do not occur at the cited line, a decisions file the driver's validator refuses, a replacement ticker the source does not show as priceable, the signed base files touched, a mutant that does not fire. The cell requires bytes at a file and line for each established branch, UNESTABLISHED-OFFLINE for the rest, the driver's own validator run, byte-identical base files, and a mutant that fails. NOT seen (blind): the live door's answers and the provider at run time; denominator: 4 branches, 3 base files, 3 checker files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut after the CTO lifted the worker-spawn hold (MSTR msg 8894) and on addendum 4 (run 3 reads every v0.19 branch). Workstream `ZZ29` of round 40. Base: `AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- A branch left `UNESTABLISHED-OFFLINE` becomes a live read by `0.7.0_AE_CloudOps~AQ2` (an order the issuer writes after r33 is applied). Run 3 itself still needs r33, r34 and pair addendum 3.
