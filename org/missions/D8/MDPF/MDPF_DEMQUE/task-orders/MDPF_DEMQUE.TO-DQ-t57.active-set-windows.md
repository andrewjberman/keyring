# TO MDPF_DEMQUE.TO-DQ-t57 -- round 9 DQ-t-57: P1 draws window to the held dates of dell2's active Cottonwood set; the B1 request is clipped to them and holds back a match-open name
<to_id>MDPF_DEMQUE.TO-DQ-t57</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~49</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>ACTIVEWINDOWS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-57` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 20) |
**outcome_ref:** C-IDENTITY, C-QUOTE, C-PRIORITY, FWD-5, FWD-9 | **depends_on:** DQ-t-50, DQ-t-52 (merged)

---

## WORKER FACE

### THE CELL

The dell1 pivot packet (outcome O12 and section 5; [DIRECTION_DELL1_20261013.md](file:///C:/dev/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md))
and CTO msg 5216 ([the dell2 note](file:///C:/dev/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_ACTIVE_COTTONWOOD_SET_FOR_DELL1_20261013.md)): dell2 published the **active Cottonwood set**:
`ACTIVE_COTTONWOOD_SET.csv`, 42,319 rows, sha256 `eb9dd0c3f6def67eab31c1b931e7fe66ad07ef37e2600908733da0a154afebfc`, 769 active accounts, 3,357 securities, in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/` at commit `ec617572b8` on box/dell2 (reaches CLOUD at the integrator's pass; **read it from the working tree when the file is there, otherwise
from the commit with `git show ec617572b8:<path>`, and verify the sha256 either way**). Columns: `account_key, source_side, cusip, ticker, held_from, held_to, window_basis`; `held_to` is a date or the word `open`
(still held). **The file carries RAW account numbers: this cell reads the `account_key` column only to group, and prints, logs and writes counts only. Never print an account number.** (The issuer already measured: of B1's 613
CUSIPs, 609 are in the set; clipping B1 to the set's windows takes 37,439 cells to about 34,341, saving about 3,100 cells over 99 CUSIPs.) **This cell makes no vendor call.**

**Build** (NEW `data/mdpf/scripts/demque/active_set.py`; edit `data/mdpf/scripts/demque/b1_request.py`; read `b1_request.py`, `card_a_slice.py`, `priority_gate.py` first; import, do not copy):
1. **`load()`**: read the CSV (working tree path first, else the commit), verify its sha256 equals the one above, and RAISE a loud `SystemExit` naming both hashes on a mismatch. Return `{cusip: {"from": date, "to": date | None, "open": bool}}`:
   `from` = the earliest `held_from` among that CUSIP's rows, floored at 2012-01-01; `to` = the latest dated `held_to`; `open` true when any row's `held_to` is `open` (then the window runs to the frontier). A row with a blank
   `cusip` or an unparseable `held_from` is counted under `skipped` and ignored. The account key is never returned.
2. **`--census`** prints ONE JSON line `{"sha256_ok", "accounts", "securities", "windows", "open_held", "skipped"}` (`accounts` = the distinct account keys COUNTED, not listed).
3. **`b1_request.py`**: for every security IN the set, clip its entries to its window: a `dates` list keeps only dates `>= from` (and `<= to` unless open); a daily `start..end` entry is clipped to `max(start, from)` and
   `min(end, to)` unless open; an entry left with no cells is dropped and the CUSIP, if it has none left, is counted in `emptied_cusips`. A security NOT in the set keeps its current window (it is a living client's name no
   active account holds today) and is counted in `unclipped_cusips`. Names whose priority is P2 or P3 (`priority_gate.excluded`, the same fail-closed read) are HELD BACK: listed in the request's `held_back`
   `[{"cusip","symbol"?,"reason"}]`, never in `securities`. The `--build` line gains `clipped_cusips`, `unclipped_cusips`, `emptied_cusips` and `held_back` (an int count), and keeps its other keys; `securities`
   counts distinct CUSIPs in the request.
4. NEW `test_demque_active_windows.py` (pytest; a stub CSV and stub frames, no network, no S3) with exactly these names:
   `test_the_active_set_is_refused_when_its_sha256_differs_and_is_never_printed_by_account`,
   `test_a_security_window_is_the_union_of_its_active_accounts_held_dates_floored_at_2012_and_open_when_any_account_still_holds_it`,
   `test_the_b1_request_is_clipped_to_the_active_window_leaves_a_name_outside_the_set_unclipped_and_holds_back_a_p2_name`.
   Existing `test_demque_b1_request.py` tests keep passing; one that pins the unclipped cell count takes the stub's empty active set (a stub that returns `{}` leaves every window unclipped) and NOTHING else.

### ACCEPTANCE

<criterion id="DQ9-t57-AC1" cell_refs="DQ-t-57"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_tests.py</invocation><expect>WIN-OK</expect></criterion>
<criterion id="DQ9-t57-AC2" cell_refs="DQ-t-57"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t57_real.py</invocation><expect>WIN-REAL-OK</expect></criterion>
`DQ9-t57-AC1` -- the three named tests. `DQ9-t57-AC2` -- on the REAL published set: sha256 verified, 769 accounts and 3,357 securities counted, the B1 line clipped (613 CUSIPs, at least 90 clipped, a match-open name held
back, 33,000 to 35,500 cells against 37,439 filed), deterministic, valid, nothing earlier than 2012-01-01, no account key. The real check allows 55 seconds a run. Report the whole folder
`pytest data/mdpf/scripts/demque` once, and the census and `--build` lines verbatim.

<expected_criteria>DQ9-t57-AC1,DQ9-t57-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `WIN-BAD no file ...`; `WIN-REAL-BAD arm1 ... (no file ...active_set.py)`.


### AMENDED 2026-10-13 ~22:0xZ (issuer; no gate limb graded it, no new order added) -- the ruling on securities OUTSIDE the active set (CTO msg 5227)

The ruling is "draws limited to that set over those windows". **A security NOT in the active set is HELD BACK, never kept at its old window.** This replaces the sentence in item 3 that says such a security keeps its current window and is counted in `unclipped_cusips`:
a CUSIP with no row in the active set (by CUSIP; a row with a blank CUSIP is matched by ticker when the request entry carries a `symbol`) goes into `held_back` with the reason
`not held by an active Cottonwood account under any identifier the files carry (draws are limited to the active set, CTO msg 5227)`, the `--build` line's `unclipped_cusips` is retired, and `securities` counts only the CUSIPs left in the request.
The issuer measured the case: B1's 4 CUSIPs outside the set are bonds and T-bills with no symbol (118 cells together, last trades from 2023-08 to 2026-05); the expected real line is therefore `securities` 609, `held_back` 5 (those 4 and the P2 fund),
cells about 34,223. The real check `dq_t57_real.py` is already amended to 609 and 5; test 3's name stays and its body asserts the hold-back of a name outside the set instead of the old unclipped behaviour.


### AMENDED 2026-10-13 ~22:4xZ (issuer; no gate limb graded it, no new order added) -- rulings on rows D1-W49-S1 to S5, and the re-seated slot

Your first pass (commits `be745e7fa2`, `b5fab0e728`) stands as inherited state. **You built to the order BEFORE the 22:0xZ amendment: the amended order and the amended real check are placed on your branch by file, and they govern.** Do NOT merge box/dell1.
- **S1 (the emptied name): RULED, it leaves the request.** A name in the active set whose window opens after all its B1 history is `emptied_cusips` and is not in `securities` (draws are limited to the held dates). The check was the issuer's error: the expected count is 608, not 609 or 613.
  Build to BOTH rulings together: names outside the set are held back (the section above), and the emptied name is dropped. Expected line: `securities` 608, `emptied_cusips` 1, `held_back` 5 (the P2 fund and the 4 outside names), `cells` about 34,223; `unclipped_cusips` is retired.
- **S2: accepted.** The builder's own base measures 37,514 cells, 614 securities; the filed 37,439 is that minus the hand-held-back P2 fund. The builder now holds the P2 fund back itself, so 37,439 is the like-for-like base.
- **S3: the check now allows 110 seconds a build call; keep your speed changes.** **S4: accepted** (`accounts` counts the key of every row, 769, as the published set states). **S5: accepted.**
- Update test 3 to assert the hold-back of an outside-the-set name and the dropped emptied name; keep its name.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue or any pacer state; no AWS write; no deploy; no timer.**
- **Never print, log, commit or return an account number.** The CSV is private-git data kept on Andrew's 2026-10-09 word; this cell reads `account_key` only to count. Your tests use a stub CSV with made-up keys.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W49-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION`
  or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/active_set.py
data/mdpf/scripts/demque/b1_request.py
data/mdpf/scripts/demque/test_demque_active_windows.py
data/mdpf/scripts/demque/test_demque_b1_request.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-57`.
<owned_cells>DQ-t-57</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t57-AC1, DQ9-t57-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~49/MDPF_DEMQUE.TO-DQ-t57.active-set-windows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t57-AC1,DQ9-t57-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the census and `--build` lines verbatim, how the commit fallback reads the file, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a read of a repo file or a git object; no AWS access.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder; nothing is drawn or served. The input carries raw account numbers: read only to count, never emitted.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: dell1 pivot packet O12 and section 5; CTO msg 5216; dell2 note `CTO_DELL2_ACTIVE_COTTONWOOD_SET_FOR_DELL1_20261013.md`; decomposition round 9.
