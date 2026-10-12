# MDPF_SECCLASS decomposition -- ROUND 23 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~11:3xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers three cells in two chains.

**Cut on:** the CTO round-22 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_22_20261012.md`, 1.0.0_SA_CTO~DELL1 msg 4333), on the CVO's slug
msg 4332 (`ADJUDICATION_v20`, @d24cc0d6ad). The ruling is **(a) a ROLLING re-derive over the window the producer itself corrects**: C_06
re-derives, on every fire, the dates inside B_00's own `--force-recent-days` window, with the number read from B_00's rule and never typed again;
dates older than the window stay as built; the served object carries `restated_through`; the dollars no classifier places stay Unclassified and
are listed by security with a reason; the page change runs under its OWN never-widen pair.
- **Item 1 is cells `SC-e-96` (the cost and the rule, read) and `SC-e-97` (the build and its pair half request).** The CTO's instruction
  "N = 14 is measured before the ship; if it adds more than 30 minutes, use the largest N that fits and state the gap in dollars" makes the
  build depend on the read: one chain, the same worker, in order.
- **Item 2 is cell `SC-e-98`** (a read, no served write, independent of item 1).
- **Item 3 (`TO-SC-e90`) is already done:** cut in round 21 and drained @4ff03e1393 (portal commit 64d8c6de38 on DEV).
- **Carried, not cut:** the ship of `SC-e-97` is a later pair-gated act by a CloudOps lane after the drain, as `TO-SC-e91b` was; SC-e-91's leg G
  (mine) on the first scheduled fire; SC-e-87's leg G on the first NEW as_of; `e57e61` HELD on its trigger.
- **D1-W83-S5 stays BOUNDED and ARMED** and disarms at the first post-act read of SC-e-97's ship (the CTO's ruling, section 2).

**State the round starts from (measured 2026-10-12 ~10:5xZ, the SC-e-95 record):**
1. **B_00 corrects canonical history inside a window by design:** `gold_dispatch.sh:99` `B_00|B_00.canonical_holdings.py|--upload
   --force-recent-days 14`; B_00's own argparse default is 0 (`B_00.canonical_holdings.py:1032`), so the 14 lives ONLY on the dispatcher's
   CATALOG line. B_00 anchors on the newest cube date and re-includes every date within N CALENDAR days of it (`:1119-1137`, `d >= anchor - N`),
   about 10 trading dates. `gold_dispatch.sh` is in `s3://opal-data-bd/code/gold/` (75,897 bytes, 2026-10-12T06:22:09Z).
2. **C_06 freezes a date at its first build** and reads the canonical holdings partitions (`_list_positions_cube_keys`, `CANONICAL_HOLDINGS_PREFIX`).
   Served 2026-10-09 Unclassified $1,846,399.46; a rebuild from the current partition reads $883,483.05 (no byte moved on that date: reference
   drift only). 10-06..08 carry byte drift of -$1.35M / -$1.49M / -$1.93M.
3. **SC-e-91 is live** (09:55:03Z, retained pass over stored top-10 lists, range $0 to $653,857.12 at 10-09). Its first fire has not run; the
   re-derive is the rest of the same correction and must read the same on a second fire (idempotence).
4. **The served firm mix is `platinum/firm/mix_summary.json`, written by D_04** (`build_firm_mix_summary`, `D_04.client_portal_summary.py:468-575`)
   from C_06's `gold/views/mix_daily_summary.json`; D_04 reads the LATEST date. `restated_through` therefore travels C_06 -> `mix_daily_summary.json`
   -> D_04 -> `mix_summary.json`.
5. **The SC-e-95 harness was scratch and is not kept** (its worktree is removed): SC-e-96 builds its own, read-only.

## Rule 24 record

- **Domain:** the CTO's three list items, one cell each, the read before the build it conditions.
- **(ii) Same grain:** SC-e-96 is one record of three questions the build needs (the rule, the cost and the gap); SC-e-97 is one build with its half
  request; SC-e-98 is one record of one question (who holds the dollars).
- **(iii) Intent coherence:** the build takes its window from the producer and its cap, if any, from the record; a number typed in C_06 for the window
  is refused by the wiring check.
- **(iv) State coherence:** the build moves served figures on a partner-facing page, so it ships only under its own pair; SC-e-96 and SC-e-98 write no
  served key. The retained pass of SC-e-91 keeps running on dates OUTSIDE the window; nothing in this round touches it.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-96` | One read: B_00's rule (where the number lives, how the window is cut, whether C_06 can read it at build time), the dates inside it today, the cost of re-deriving the whole window (cold and warm wall, memory, write set, against the 30-minute budget), per date the served against the rebuilt Unclassified, the relationships stored and not in the partition (and the reverse), and the dollars left uncorrected if only the newest n dates are re-derived. | FWD-1 (the dates leg G's comparator rests on) | LOCAL | none |
| `SC-e-97` | Build in C_06 (and one pass-through line in D_04): read the producer's window at build time, re-derive every window date from the current partitions on every fire, replace each date's relationship entries and the firm and advisor snapshot days, write `restated_through`, rewrite only what differs; the function-level tests; the never-widen half request. | FWD-1 | SERVED | SC-e-96 |
| `SC-e-98` | One read: the rebuilt 2026-10-09 Unclassified by security with a reason, the dollars outside every stored list marked. | FWD-1 | LOCAL | none |

## Write sets (disjoint)

- **SC-e-96:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/WINDOW_READ_C06_ROLLING_20261012.json`, its scratch under `.scratch/`, and the
  surprise channel (append).
- **SC-e-97:** `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`, `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`, the new
  test `data/black_diamond/scripts/gold/tests/test_c06_rolling_rederive_r23.py`, the half request
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md`, and the surprise channel.
- **SC-e-98:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json`, its scratch, and the
  surprise channel.

## Chains

| chain | cells | worker | why |
|---|---|---|---|
| A | SC-e-96 -> SC-e-97 | slot ~86 `worker` | the build reads the read's record: it takes N from it |
| B | SC-e-98 | slot ~87 `worker` | no edge to A |

Fan-out 2 of 2 chains, cap 8. SC-e-96 and SC-e-98 are `<direct_act>true</direct_act>` (LOCAL, no product file, no served write: no L2, no L4-R, no
L8-L10; my one real run is each record's own check at close). SC-e-97 is SERVED and goes through the CVO's L8 / L9 as round 21's SC-e-91 did.

## Carried question (recorded, not sent: FYIs go to the record)

The CTO's section 2 says the restated history "must be stated on the page". The served field `restated_through` is in this round's list; a visible
sentence on the Advisor Intelligence page is a portal product change and, on a client-facing page, a PROD push waits on Andrew. I will put that one
question to `1.0.0_SA_CTO~DELL1` with the build's record, not before.
