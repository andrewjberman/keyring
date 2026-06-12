# CENSUS-XT CLASS-N adjudication — 4 candidates ruled (2 FIX / 2 BENIGN)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

Trigger: AE 0.6.0 CENSUS-XT delivery (315c8fab6, MCP 134036Z) + residuals-close (134207Z: bd E_13 =
CLASS-I index-slot; D_02 = CLASS-I all 3 trees). Per the 2026-06-11 doctrine, CTO independent code-read of
EVERY cited site before ruling — all 4 candidates + the bd post-fix twins read directly this session.

## Rulings

### 1. cot A_04.client_dimension — NON-BENIGN (CLASS-N actionable) → FIX
Verified L112-115 completion-order `dfs.append(fut.result())` under `as_completed` + L120 bare
`drop_duplicates(subset=['transaction_id'], keep='last')` with NO sort, NO provenance. Exact pre-fix twin of
bd A_04. Remedy = mirror bd 9a89926fd in full: index-slot assembly (`futures={...: i for i,key in
enumerate(keys)}` / `dfs[futures[fut]]=...`) + `_file_date`/`_intra_pos` provenance columns + total-order
sort before keep='last' (keep-full semantics, no field-slimming). cot-only deploy per Rule 13
(opal-data-cot). Dormant (cot not yet incrementalized) but cot gold IS served from nightly full rebuilds —
the deploy takes the same battery as bd A_04 (HEAD x2 / FIXED x2 / delta): verified DELTA=0 → no-hold per
the banked doctrine; any nonzero served delta → full CTO+COO never-widen sign-off.

### 2. cot A_01.advisor_assignments — NON-BENIGN → FIX (correction to AE's framing)
AE's "bd twin dispositioned-benign" does NOT transfer: bd A_01 is benign BECAUSE of the GLDINC oracle-fix —
verified bd L238-246 total-order sort on (transaction_id, _file_date, _intra_pos) before keep='last', and
provenance-sorted dedups at L362/L523. cot A_01 L192 is the bare pre-fix form: `drop_duplicates(subset=
['transaction_id'], keep='last')` over a completion-order concat (L174-181), no provenance columns anywhere.
That is the ORIGINAL A_01 oracle defect, live in cot's nightly. The L231/L373 dedups carry sort_values on
their dedup keys (tie-survivor immaterial in principle) but the mirror carries the provenance pattern across
all three sites as bd does. Same deploy battery + never-widen terms as A_04.

### 3. cot A_02.fee_rate_history — BENIGN (conditional) → opportunistic hygiene
Exact shape-twin of bd A_02 (read both): completion-order append assembly, but BOTH cited dedups are
preceded by `sort_values` on the dedup keys (L190-194 trade_date; L265-269 account_id+trade_date), and the
tie population is same-day fee rows documented invariant-identical ("multiple transactions same day = same
fee"). Survivor identity immaterial → same lane as the D_02 exoneration. bd census (2026-06-11) left bd A_02
unflagged on identical code — consistency holds. NOT a never-widen lane; provenance hygiene on next touch.
REOPEN CONDITION: DS AST-DEDUP Phase-3 cross-check surfacing same-day ties with DIFFERING fee payload
(fee_bps or fee_schedule variants) collapses the immateriality — reopens as FIX.

### 4. inf INF_D_06.cash_drag — BENIGN (with a pairing correction for the record)
AE's cited pairing is mis-paired: the L273-278 completion-order assembly is the HOLDINGS loader, whose
concat (L284) feeds a vectorized `groupby(['account_id','date']).agg(sum)` (L290-292) — no survivor
selection; worst case is ULP-level float-sum ordering, no observed materiality (same likely-immaterial lane
as D_02). The L383 dedup is fed by the TXN path, which has NO parallel loop — `load_qualifying_trades`
sequentially scans the latest 5 silver/transactions partitions and breaks on the first canonical snapshot
(single frame), then projects to exactly `['account_id','trade_date','trans_amount']` (L380) — i.e. the
dedup subset == the full column set, so duplicates are byte-identical by construction and the missing
`keep=`/sort is immaterial. Hygiene (index-slot on the holdings loop) on next touch.

## Residuals accepted
- bd E_13 = CLASS-I (index-slot L138/141/143, dedup downstream of deterministic assembly) — ACCEPTED;
  closes the CTO-owned E_13 classification residual from 2026-06-11. Zero new bd CLASS-N.
- D_02 = CLASS-I confirmed across bd/cot/inf — re-confirms the 2026-06-11 exoneration.

## Net + routing
CLASS-N census final: **2 FIX (cot A_04, cot A_01) / 2 BENIGN-with-hygiene (cot A_02, inf D_06)**. Standing
convention unchanged (index-slot or A_01-provenance for new gold parallel loads). Fix execution routing is
COO's lane: remedy spec above is TO-ready; AE 0.6.0 engineers + DS deploys per Rule 13 (cot bucket only);
timed for joint adjudication with DS AST-DEDUP hit-list convergence per COO's decomposition design.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Adjudication = line-level assembly/dedup shape classification — direct Read of 6 scripts across 3 trees (cot A_01/A_02/A_04, inf D_06, bd A_01/A_02/A_04 twins). The graph does not encode assembly-order semantics (same rationale as the 2026-06-11 ruling). No code/infra change by me; the fix TOs carry their own mandates (comp-pipescript io/deployed + comp-validate per DS minimums). |
