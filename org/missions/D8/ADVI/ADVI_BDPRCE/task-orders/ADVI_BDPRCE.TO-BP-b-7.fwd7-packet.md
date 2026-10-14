# ADVI_BDPRCE task order -- `BP-b-7` -- THE FWD-7 PACKET: THE BEFORE/AFTER LIST WITH ITS DOLLAR EFFECT AND THE READERS IT MOVES (JOIN, STAGED, READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~11</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only packet; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (the extract on local disk; `s3api get-object` if a partition must be re-read). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects `served_write` true, fewer than four named readers, and a reader without a class (33-arm self-test OK). Blindness: the grader proves shape, not that a dollar figure is right; the issuer recomputes the total from the extract and the list.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-7` (round 2; the join; read-only; it produces the page Andrew reads, it moves nothing)

Before any served price may move, Andrew sees, per fix, a named list of what moves and the dollar effect on the latest snapshot, plus the downstream readers it reaches (PRD DEC-7). Two earlier cells are merged
into your worktree; read their records first:
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/REPLAY.json`, `REPLAY.md`, `BEFORE_AFTER.csv`: what each served price becomes under R1 (variants A and B), and why.
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json`, `CENSUS.md`, and the extract `C:/dev/wk-bdprce-r2-7-data/lot_extract.csv` (read it by that absolute path and check its sha256 against `extract_sha256` in
  `CENSUS.json`; a mismatch is a BLOCKING row and you stop): one line per served lot (object key, entity class, `data_as_of`, asset name, served ticker, `current_price`, `quantity`, `market_value`, price class, account reference).

### 1a. What to compute

1. **The latest snapshot.** The latest `data_as_of` date carried by a majority of the extract's lots (state the date and the share). Only lots whose `data_as_of` equals it count toward the snapshot; state how many lots do not.
   Two facts from the merged replay (`REPLAY.md`, `REPLAY.json`) bind your arithmetic:
   (i) `BEFORE_AFTER.csv` has 539 CHANGED and 285 NOW_CARRY_FORWARD rows, and 13 of the carry-forwards equal the served price (their effect is zero, count them as touched and not as moved: 811 prices move);
   (ii) 8 CHANGED rows carry a par-quoted unit-scale difference (flag `scale_100x`; R1 reads 100x the served per-unit price, row `ADVI_BDPRCE-D1-W6-S2`, a CTO call is open on it). Report the dollar effect twice, with and without those 8,
   and name them in the movers; do not let them lead the 25 largest movers without the flag. The 212 NOT_RECOMPUTABLE rows have no new price: list them, with zero effect, and say so.
2. **The dollar effect, per changed price and in total.** For each (asset, date) in `BEFORE_AFTER.csv` classed CHANGED or NOW_CARRY_FORWARD whose date equals the snapshot date: the sum over the snapshot's lots of that asset of
   `(new_price - old_price) * quantity` (variant A; give variant B's total beside it). The exact basis is `quantity * price`, NOT the served `market_value`, which the cap scales on some lots: state, from the census's
   identity count, how many snapshot lots have a served `market_value` that is not `quantity * current_price`, and the effect on those lots on both bases. Never print a client or account name.
3. **The movers.** The 25 largest movers by absolute dollar effect (asset name, date, old, new, distinct trades, effect), and the total, the count of assets and lots touched, and the share of the snapshot's value they are.
4. **The readers it moves.** Name every downstream reader of a served 49F price or lot value you can establish from the repo and the PRD (`org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md` CONTRACTS and
   "Not in scope"; the ADVI exec-summary generator and its slots; MDPF_SECCLASS's BD Mix; IRPT_DASHBD and IRPT performance; the portal pages that render lots). For each: the file or project that reads it, whether it is
   `client-facing`, `internal` or `unknown` (a partner-firm or client login can open a client-facing page), and whether it SUMS lots into an account or firm figure. At least four readers. This is NOT the C3 census;
   say so, and `claim: inferred` for any reader you did not trace to the line.
5. **The plain page.** `PACKET.md` is the page Andrew reads: what is proposed (R1, in one paragraph), how many prices move and what the total dollar effect is, the 25 movers, which readers are touched and their class,
   what does NOT move (account totals read BD's own value), what the packet does not know, and the exact sentence of the decision asked of him (his review per fix; nothing is served until he has seen it). Write for
   a reader who has not seen any code.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~11/PACKET.json`

```json
{"order": "BP-b-7", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["read lot_extract.csv sha256 ...", "..."],
 "snapshot_date": "YYYY-MM-DD", "snapshot_share": 0.0, "lots_outside_snapshot": 0,
 "price_changes": 0, "assets_changed": 0, "lots_touched": 0,
 "dollar_effect_latest_snapshot": 0.0, "dollar_effect_variant_b": 0.0,
 "market_value_identity": {"lots_off": 0, "effect_on_quantity_basis": 0.0, "effect_on_served_market_value_basis": 0.0},
 "movers_file": "MOVERS.csv", "before_after_file": "BEFORE_AFTER.csv",
 "readers": [{"reader": "<project or file>", "class": "client-facing | internal | unknown", "sums_lots": false, "evidence": "<file:line or PRD section>"}],
 "served_write": false}
```
Also commit `MOVERS.csv` (the 25 largest).

## 2. BOUNDS

1. No write anywhere outside your deliverables folder; no AWS write; no producer run; no product file edited. A re-read of a partition (only if the list needs a date not in the extract) uses read verbs.
2. No client name, account number or advisor name is printed or committed; the extract's `account_ref` is a digest and stays one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-7 packet needs the listing`. `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~11/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~11/ADVI_BDPRCE.TO-BP-b-7.fwd7-packet.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-7"><invocation>cd /c/dev/wk-bdprce-r2-11 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py packet --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~11/PACKET.json</invocation><expect>^PACKET record ok changed=[0-9]+ assets=[0-9]+ readers=[0-9]+ served_write=false$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-7"><invocation>cd /c/dev/wk-bdprce-r2-11 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-11 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~11/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and that no served write is claimed; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The issuer recomputes the total from the list and the extract.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `PACKET.json`, `PACKET.md` and `MOVERS.csv` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W11-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the snapshot date and share, prices and assets changed, the dollar effect (variant A and B), the five largest movers (asset name,
effect), the readers with their classes, the identity count, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 1 (the list Andrew sees); PRD DEC-7. STAGED at the cut: un-parks when `BP-b-2` and `BP-b-3` are merged and PASS and the extract's sha256 reads equal; its worktree is cut from that HEAD.
The packet carries the decision asked of Andrew; the COO sends it to the CTO, who puts it to Andrew (FWD-7); nothing is served meanwhile.

**SUPERSEDED (2.0.0_SA_COO~K1, 2026-10-14 ~01:0xZ):** the CTO ruled R1 AMENDMENT 1 while this order's worker had run five minutes with no commit (`org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`, msg 5323): reinvestment buys count as trades, par-quoted bonds serve per unit, and the replay is re-run on that variant so the list Andrew reads carries it. A packet over the variant-A list would have put a superseded rule in front of Andrew, so the worker was stopped and no packet was produced. The packet is re-cut in round 3 after the amended module and the re-run replay. Nothing was merged from this order.

<status>superseded</status>
<round>2</round>
<workstream>PACKET</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-7</to_id>
<slot>~11</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
