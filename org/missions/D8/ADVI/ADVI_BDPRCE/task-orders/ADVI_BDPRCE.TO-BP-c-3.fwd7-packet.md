# ADVI_BDPRCE task order -- `BP-c-3` -- THE FWD-7 PACKET ANDREW READS, ON THE R1.3 LIST (JOIN, STAGED, READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~22</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only packet; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (the extract and lists on local disk; `s3api get-object` if a partition must be re-read). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects `served_write` true, a par-quoted row among the movers, interpolated fates that do not sum, fewer than four named readers, a reader without a class and a write verb in `calls` (35-arm self-test OK). Blindness: the grader proves shape and arithmetic, not that a dollar figure is right; the issuer recomputes the total from the list and the extract.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-3` (round 3; the join; read-only; it produces the page Andrew reads, it moves nothing)

Before any served price may move, Andrew sees, per fix, a named list of what moves, the dollar effect on the latest snapshot, and the downstream readers it reaches (PRD DEC-7). Rounds 2 and 3 stopped earlier packets when the CTO amended R1; you write it on the R1.3 list. Three earlier cells are merged into your worktree (the module at R1.3, the R1.3 replay and the census); read their records first. AMENDMENT 3 (call 19b2) binds: R1 changes values, never units; every number below is in the unit of the asset's own served series:
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/REPLAY3.json`, `REPLAY3.md`, `BEFORE_AFTER3.csv`, `ESTIMATED_ROWS3.csv`, `UNIT_MAP.csv`: what each served price becomes under R1.3, and the fate of each interpolated row.
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json`, `CENSUS.md`, and the extract `C:/dev/wk-bdprce-r2-7-data/lot_extract.csv` (read it by that absolute path and check its sha256 against `extract_sha256` in `CENSUS.json`, expected
  `e7e618d76516c8b7977179aefb3f77ce4fc13c17fbcf1dbeb92001a6e0a2b50b`; a mismatch is a BLOCKING row and you stop): one line per served lot (object key, entity class, `data_as_of`, asset name, served ticker, `current_price`, `quantity`, `market_value`, price class, account reference).

### 1a. What to compute

1. **The latest snapshot.** The latest `data_as_of` date carried by a majority of the extract's lots (state the date and the share). Only lots whose `data_as_of` equals it count toward the snapshot; state how many lots do not.
2. **The dollar effect, per moved price and in total.** For each (asset, date) in `BEFORE_AFTER3.csv` classed CHANGED or NOW_CARRY_FORWARD whose date equals the snapshot date: the sum over the snapshot's lots of that asset of `(new_price - old_price) * quantity`. A carry-forward that equals the served price has zero effect: count it as touched, not as moved.
   The exact basis is `quantity * price`, NOT the served `market_value`, which the cap scales on some lots: state, from the census's identity count, how many snapshot lots have a served `market_value` that is not `quantity * current_price`, and the effect on those lots on both bases.
   The NOT_RECOMPUTABLE rows of `BEFORE_AFTER3.csv` have no new price: list them by reason with their count (`ratio_unrecognised`, `ratio_unrecognised_carry`, `unit_unreadable`, others), with zero effect, and say so. State the measured withheld Fixed Income trade rows and assets from `REPLAY3.md`. The par-quoted rows read UNCHANGED, so none appears among the movers (the grader refuses one).
   UNITS (AMENDMENT 3): no served row changes unit (`unit_changed_rows` in `REPLAY3.json` is 0; copy it). Nothing is held out for a unit: `held_unit_rows` is 0. MORGAN STANLEY FIN LLC 0% 05/03/2029 and its interpolated rows read in their own per-100 series, each shown as "last traded <date>": show it as the worked example of a per-100 series (old, new, observation date). Never print a client or account name.
3. **The movers.** The 25 largest movers by absolute dollar effect (asset name, date, old, new, distinct trades, effect, the observation date for a carry-forward), the total, the count of assets and lots touched, and the share of the snapshot's value they are.
4. **Every interpolated row's fate (round-2 row `W12-S1`).** From `ESTIMATED_ROWS3.csv`: how many served interpolated rows become a trade price, how many a "last traded <date>", how many stay unresolved (no R1 trade). Show 10 examples of each fate. Andrew sees this: the estimated prices the CTO banned each have a stated replacement.
5. **The readers it moves.** Name every downstream reader of a served 49F price or lot value you can establish from the repo and the PRD (`org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md` CONTRACTS and "Not in scope"; the ADVI exec-summary generator and its slots; MDPF_SECCLASS's BD Mix; IRPT_DASHBD and IRPT performance;
   the portal pages that render lots). For each: the file or project that reads it, whether it is `client-facing`, `internal` or `unknown` (a partner-firm or client login can open a client-facing page), and whether it SUMS lots into an account or firm figure. At least four readers.
   This is NOT the C3 census; say so, and `claim: inferred` for any reader you did not trace to the line.
6. **The plain page.** `PACKET3.md` is the page Andrew reads: what is proposed (the amended R1, in one paragraph), how many prices move and what the total dollar effect is, the 25 movers, the interpolated rows' fates, which readers are touched and their class, what does NOT move (account totals read BD's own value),
   what the packet does not know, and the exact sentence of the decision asked of him (his review per fix; nothing is served until he has seen it). Write for a reader who has not seen any code.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~22/PACKET3.json`

```json
{"order": "BP-c-3", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["read lot_extract.csv sha256 ...", "..."], "amendment": "R1.3",
 "snapshot_date": "YYYY-MM-DD", "snapshot_share": 0.0, "lots_outside_snapshot": 0,
 "price_changes": 0, "assets_changed": 0, "lots_touched": 0, "touched_not_moved": 0,
 "dollar_effect_latest_snapshot": 0.0,
 "market_value_identity": {"lots_off": 0, "effect_on_quantity_basis": 0.0, "effect_on_served_market_value_basis": 0.0},
 "movers_file": "MOVERS3.csv", "before_after_file": "BEFORE_AFTER3.csv", "par_rows_in_movers": 0,
 "interpolated_fate": {"rows": 0, "trade_price": 0, "last_traded_date": 0, "unresolved": 0},
 "readers": [{"reader": "<project or file>", "class": "client-facing | internal | unknown", "sums_lots": false, "evidence": "<file:line or PRD section>"}],
 "plain_page": "PACKET3.md", "served_write": false, "held_unit_rows": 0, "unit_changed_rows": 0}
```
Also commit `MOVERS3.csv` (the 25 largest).

## 2. BOUNDS

1. No write anywhere outside your deliverables folder; no AWS write; no producer run; no product file edited. A re-read of a partition (only if the list needs a date not in the extract) uses read verbs.
2. No client name, account number or advisor name is printed or committed; the extract's `account_ref` is a digest and stays one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-3 packet needs the listing`. `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~22/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~22/ADVI_BDPRCE.TO-BP-c-3.fwd7-packet.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-3"><invocation>cd /c/dev/wk-bdprce-r3-22 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py packet3 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~22/PACKET3.json</invocation><expect>^PACKET3 record ok changed=[0-9]+ assets=[0-9]+ readers=[0-9]+ interpolated=[0-9]+ served_write=false$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-3"><invocation>cd /c/dev/wk-bdprce-r3-22 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-22 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~22/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and that no served write is claimed; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The issuer recomputes the total from the list and the extract.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `PACKET3.json`, `PACKET3.md` and `MOVERS3.csv` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W22-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the snapshot date and share, prices and assets changed, the dollar effect on both bases, the five largest movers (asset name, effect), the interpolated fates, the readers with their classes,
the identity count, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 2 (the BP-b-7 re-cut); PRD DEC-7. STAGED at the cut: un-parks when `BP-c-2` is merged and PASS and the extract's sha256 reads equal; its worktree is cut from that HEAD. The packet carries the decision asked of Andrew; the COO sends it to the CTO, who puts it to Andrew (FWD-7); nothing is served meanwhile.
Round 2's worker for this cell was stopped five minutes in (no commit) when R1 was amended; nothing carries over.

<status>staged</status>
<round>3</round>
<workstream>PACKET2</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-3</to_id>
<slot>~22</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
