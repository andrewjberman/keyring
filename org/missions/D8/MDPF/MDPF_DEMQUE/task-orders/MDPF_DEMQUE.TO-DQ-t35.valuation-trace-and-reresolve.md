# TO MDPF_DEMQUE.TO-DQ-t35 -- round 9 DQ-t-35: trace which client pages value FTHSX and PFORX, and re-resolve the three wrong-symbol CUSIPs
<to_id>MDPF_DEMQUE.TO-DQ-t35</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~27</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>VALTRACE</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-35` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amended) |
**outcome_ref:** C-PRICES, C-IDENTITY | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-35` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` ADDENDUM 3, read it; row
`MDPF_DEMQUE-D1-S12`, BLOCKING). Three names were classed wrong-symbol by the cause rule (client trade prices agree with the Yahoo symbol's close
about 40 percent of the time): FTHSX (CUSIP 14064D865, Fullerthaler Behavioral Small-Cap Equity Fund Institutional Shares), PFORX (693390882, PIMCO
International Bond Fund (U.S. Dollar-Hedged) Institutional Class) and RPIFX (77958B402). In `silver/positions` `date=2026-06-23` FTHSX is held by
4 accounts, PFORX by 11, RPIFX by 0 (`s3://opal-data-assets/commonwealth/cottonwood/silver/positions/`, columns `Advisor_ID`, `AccountNumber`,
`Cusip`, `Symbol`, `Quantity`, `AsOfDate`, `Account_Status`). The table of the 14 is
`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND9_LOCK_CAUSE_14.md`. This order is READ-ONLY and changes no byte of any
served artifact or page; a trace needs no one's word.

**Build** (one artifact, `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~27/VALUATION_TRACE.json`, plus a short readable
`VALUATION_TRACE.md` beside it; any helper script lives in `.scratch/`, uncommitted, unless you need to commit it for the report):
1. **The valuation path.** For the 15 positions (FTHSX 4 + PFORX 11), name the chain from the price file to the client page, each hop with its
   evidence (a file path and line, or an S3 key and a read): the served price file (`yahoo/global/silver/price_history/cusip=<CUSIP>/prices.parquet`);
   the artifact that carries it forward (start at `data/cot/scripts/gold/build_canonical_prices_v2.py`: its input `historical_prices`, its output
   `OUTPUT_KEY`, and `data/mdpf/scripts/demque/land_cot.py` which lands the price store into that input); the artifact that values a position
   with it; and the portal route and firm of the page that shows it. Use the estate's tools to find the consumers rather than guessing:
   `comp-which "<question>"`, `comp-dataflow origin <script.py>`, `comp-pipescript io <script> --pipeline <tree>`, `comp-routes`, `comp-find`
   (the rail denies a blind recursive grep; read its RUN NEXT). If a hop cannot be found, say which and stop that row with `read_by_a_page`
   false and the evidence of what was searched, never a guess.
2. **The rows.** `positions`: exactly 15 rows `{"account", "cusip", "symbol", "price_file", "value_artifact", "route", "firm",
   "read_by_a_page", "evidence"}`; `read_by_a_page` is true only when you read the hop that puts that position's value on a page; false carries an
   `evidence` string naming what was read and found absent. `denominator`: `{"fthsx_accounts": 4, "pforx_accounts": 11, "total": 15}`. Account
   numbers are written as read (they are in the store; this file stays in the repository mission tree).
3. **Re-resolve by CUSIP, through the EXISTING resolvers only (C-IDENTITY: no second resolver).** Find the resolvers the estate already has that
   map a CUSIP to a ticker or share class (start with `build_canonical_prices_v2.py`'s `ticker_lookup` / `YF_OVERRIDES` / `TICKER_CORRECTIONS`, the
   request files in `~/.opal/demque/queue/` that carried these three names with their symbols, and whatever `comp-which "cusip to ticker
   resolver"` returns; name each resolver and its file). For each of the three CUSIPs, run those resolvers and list every candidate ticker they
   return other than the current symbol. For each candidate, pull its close once with `yahoo_pull.pull` under a `yahoo_pull.Pacer` whose state file
   is a scratch path (the shared rule; never the real `pacer.json`) and print its agreement against the client's trades with
   `lock_cause.py`'s agreement function (import it; tolerance and asset type as `lock.check`). `candidates`: a list of `{"cusip",
   "current_symbol", "candidates": [{"resolver", "ticker", "share_class_note", "agreement_pct", "n_checked"}], "reason"}`; an empty list carries
   a `reason` ("the resolvers return no other ticker for this CUSIP"). A candidate at or above 90 is the proposed correction; do NOT write it
   anywhere. Build no resolver of your own, and no more than 6 candidate pulls in total.
4. NEW `VALUATION_TRACE.md`: one page, the path as a short list, the 15-row table counts (read by a page / not), the candidates and their
   agreement, and what you did not read.

### ACCEPTANCE

<criterion id="DQ9-t35-AC1" cell_refs="DQ-t-35"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t35_trace.py</invocation><expect>TRACE-OK</expect></criterion>
<criterion id="DQ9-t35-AC2" cell_refs="DQ-t-35" judgment="true"/>
`DQ9-t35-AC1` -- the trace file's structure: denominator 4 / 11 / 15, exactly 15 position rows each carrying its hop fields and evidence, a candidates entry
for each of the three CUSIPs. `DQ9-t35-AC2` (judgment, graded by the CVO at L9, never self-graded) -- the chain from the price file to the client page
is the right one and each `read_by_a_page` verdict is supported by the cited evidence.

<expected_criteria>DQ9-t35-AC1,DQ9-t35-AC2</expected_criteria>

Run the invocation from the worktree root. At the base: `TRACE-BAD no file ...VALUATION_TRACE.json`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY. No write to any served store, lock record, price file, pacer state, queue or page; no AWS write; no Bloomberg call; no deploy; no
  portal change.** Yahoo is read through `yahoo_pull.pull`, one candidate at a time under a scratch pacer, at most 6 pulls.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W27-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~27/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-35`.
<owned_cells>DQ-t-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t35-AC1 (mechanical); DQ9-t35-AC2 is judgment and carries no verdict. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~27/MDPF_DEMQUE.TO-DQ-t35.valuation-trace-and-reresolve.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t35-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the check output, the chain in one paragraph, the read-by-a-page count, the candidates and their agreement, what was not read, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; the S3 reads use the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE a read-only trace and a read-only candidate agreement; nothing is written to a served surface.
risk: LOCAL -- records only. Any correction it proposes is a client-facing change that waits on Andrew's word (CTO ADDENDUM 3).
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 ADDENDUM 3 (msg 3978); row D1-S12 (BLOCKING); decomposition round 9.
