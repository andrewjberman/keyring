# TO IRPT_ANLREQ.TO-AR-y-278.c-swap-steps-1-2-read-and-design -- C-SWAP steps (1) and (2): where the upload door refuses an unknown holding, and where the KNOWN and yfinance KEEP passes would sit -- a read and a design

<to_id>IRPT_ANLREQ.TO-AR-y-278</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~99</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-278` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~99`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-99` (branch `wk-IRPT_ANLREQ-99`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~99 <0.9.0_WK_IRPT_ANLREQ~99@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W99-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-278`, inlined) -- C-SWAP, THE FIRST TWO STEPS. READ AND DESIGN ONLY. NOTHING IS BUILT, CALLED OR WRITTEN.

*The PRD's C-SWAP (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` :104): one pass per unknown holding: (1) KNOWN in `etf-classifications` and MDPF_SECHIST (a typo suggestion verified against the registry and yfinance, never YCharts); (2) the YFINANCE CHECKER, one paced call: if it has history the holding is KEPT, a registry row is added and its prices land in MDPF_SECHIST; (3) CLASSIFY only if yfinance has nothing; (4) a deterministic PROXY from MDPF_SECHIST's sibling MDPF_SECCLASS's designated-proxy table; (5) RECORD (`proxy_for`, `proxy`, `method`, `confidence`). `resolution_kimi`'s model-proposed swap is retired. MEASURED by this seat (2026-10-13 ~19:12Z): `TIMXX`, which the upload door refused as TICKER_NOT_FOUND, has yfinance history (20 daily rows, close 1.0): by C-SWAP it is KEPT and needs no proxy. The CTO (msg 7187): 'make the step-2 KEEP visible on the upload page'. The upload door's resolver asks the provider read (`securities_info`) today; the registry row and the price landing belong to MDPF_SECHIST (dell1).*

1. **Where the door refuses today.** Read `infra/aws/lambda/investor-reporting/intake/security_resolution.py` (the resolver and its `check`, the `NOT_FOUND` states), `intake/upload_resolution.py`, `intake/uploads.py` and `intake/portfolio.py` (where an unknown ticker becomes the finding `TICKER_NOT_FOUND` and what the person sees), and the resident's resolver construction (`ycharts/generate/resident_worker.py`). Record `door` {`where_ticker_not_found_is_made` (file:line), `which_provider_it_asks`, `what_it_returns_for_a_mutual_fund_like_TIMXX`, `what_the_person_sees` (the finding words and actions)}.
2. **What the estate already has for steps (1) and (2).** Find and read: `etf-classifications` (what it is, where it lives, its format and its registry rows: `comp-which "etf-classifications registry"` or `Grep` on a named folder), MDPF_SECHIST's per-security series and how a price lands there (`org/missions/` MDPF_SECHIST project folder: its PRD and the writer; read only), any existing yfinance caller in the estate (paced, with its bounds: `Grep` the named folders `lib/`, `data/`, `infra/aws/lambda/` for `yfinance`; list the callers with file:line), and MDPF_SECCLASS's designated-proxy table (read only; dell1's). Record `estate` {`registry` (location, row shape), `sechist_writer` (who writes a new security's prices, how, and whether a Dell or Lambda caller may), `yfinance_callers` (file:line each, with their pacing), `proxy_table` (location, shape)}.
3. **Design steps (1) and (2) for the upload door.** Propose the smallest change: where in the door the KNOWN check and the yfinance check run (inside the resident, before the finding is made); what a KEPT holding looks like to the rest of the upload (it prices from MDPF_SECHIST, or from yfinance for this request when the registry row cannot be written from here: say which and why); what is written, where, by whom (the registry row and the price series are another project's data: name the owner, the interface and whether it needs a pair); the pacing and the failure behaviour (yfinance down means the holding stays unknown with the finding unchanged, never a guessed keep); what the upload page shows for a KEPT holding (words such as 'TIMXX was found with price history and is used as is'); and the cells it would split into, each with its grant, lane and risk class. Record `design` and `cells`.
4. **Offline measurement.** For `TIMXX` and 3 other symbols the YCharts provider is known not to carry (choose from the unknown tickers recorded in the upload tests' fixtures; label what you ran), run the yfinance history call (period one month, nothing written) and record rows, last close and the call's elapsed time; this is the same read the checker would make. If yfinance is unreachable from this box, say so.
5. **Write `r23/C_SWAP_STEPS_1_2_READ.json`:** `door`, `estate`, `design`, `cells`, `measurement`, `claim`, `not_read`.
6. **In your report:** why TIMXX is refused today (file:line), what the estate already has, the proposed cells.

### ACCEPTANCE

<criterion id="AR278-y-AC1" cell_refs="AR-y-278"><invocation>python C:/dev/wk-irpt-anlreq-99/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y278-read --root C:/dev/wk-irpt-anlreq-99</invocation><expect>Y278-READ-OK</expect></criterion>
`AR278-y-AC1`: the record names where the door makes TICKER_NOT_FOUND, what the estate already has for steps (1) and (2) with file:line, a design with its owner and interface for the registry and price landing, the cells it splits into, and a yfinance measurement.

<criterion id="AR278-y-AC2J" cell_refs="AR-y-278" judgment="true"/>
`AR278-y-AC2J` (judgment, graded at L9, never by you): the door was READ in the code (not assumed), the registry and price-landing owner and interface are named, a failure of the check leaves the holding unknown (never a guessed keep), the page words for a KEPT holding are stated, and nothing was built, called or written beyond the read-only yfinance history calls.

<expected_criteria>AR278-y-AC1 AR278-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~99/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-278</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~99/IRPT_ANLREQ.TO-AR-y-278.c-swap-steps-1-2-read-and-design.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-278`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR278-y-AC1,AR278-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reads of source files and tests in the worktree; read-only yfinance history calls; nothing is written, released or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR278-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
