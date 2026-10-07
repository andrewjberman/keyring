# ETFS_RIVALS -- ROUND 13 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-07 ~02:5xZ

**Input:** CVO slug msg 30523. `surprise-channel/adjudications/ADJUDICATION_v14.Z.md` @4da175efa4 (C-S50); fe-1's J1 in
`ADJUDICATION_v13.Z.md` (C-S49).

## 1. WHAT THE ROUND DELIVERED

- **fe-1 and its AMENDMENT 1:** every mention in a fund's panel opens a modal carrying that fund's section. Served: 0 of 2,076
  buttons lack it; 234 of 234 real clicks open the right modal. C-S47 is REMEDIATED.
- **gw-1:** `GET /rivalfunds/{day}/audit`, released by NFRA_OPLGTW r23 @7d65a28db0, live 2026-10-07T01:30:43Z.
- **lk-1:** the served 02:33Z page carries ONE audit link and 0 citation lines. The 148 machine keys are on `audit.html`.
- All five Lambdas hold 39 of 39 files at f3b3055a5e. Every mechanical criterion re-ran PASS.

**Round 13 is CLOSED.** With it, Andrew's order of 2026-10-06 (~16:3xZ and ~16:4xZ) is delivered on the served objects: the
audit trail is off the page, every ticker mention links to that fund's modal, and the audit page is one link away.

## 2. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Who takes the signed-in GET of the audit route** | **Andrew makes the click.** He is the first signed-in reader and the only identity that passes the gateway's sign-in without a seat holding his credentials. **The proof is an artifact, not his say-so:** after his click, the gateway's access record for `/rivalfunds/2026-10-06/audit` shows status 200, a real identity and a body near 1.38 MB. `2.0.0_SA_COO~O`'s lane reads the record, and CVO~RV grades from it. Until that record exists, FWD-5 and FWD-18 stay NOT REALIZED, and the link stays (CTO half @7644912de2 condition 4: on a failure, republish without it the same hour). | An unauthenticated probe returns 302 for a real route and for a bogus one alike, so no seat can tell them apart. A seat signing in as Andrew is not a thing this fabric does. |
| 2 | **fe-1 J1 limb 3** (C-S36: the ticker-form names) | It waits for the 2026-10-07 names run, as the CVO states. It is read on the morning pass. | The names stage runs on the vehicle. |
| 3 | **S43** (GQGU's Nebius keyed N97284108 in the A1 tables) | Unchanged. Its proof is the 2026-10-07 census after the 07:00 ET run (ledger `etfs-rivalfunds-pk1-al1`, leg C1), with Nebius as the positive control. | pk-1's first parsekeys land then. |
| 4 | **Z-W1-S48** (`audit.html` has no size refusal of its own; 1,381,244 B against the gateway's 2,097,152 B cap) | **A round-14 cell.** The audit page gets the same loud over-cap line the main page has. Over the cap it publishes the newest trades that fit, with a stated cut and the count left out. It never lets the gateway refuse the whole page silently. | The audit page grows every day. The main page's lesson (a silent strip hid the dead links) applies to it unchanged. |

## 3. THE MORNING PASS (2026-10-07, after the 07:00 ET vehicle run), ONE read by `2.0.0_SA_COO~RV`, graded by CVO~RV

1. The ADDENDUM 1 census: every merged (CUSIP/ISIN key, Bloomberg key) pair with its count; Nebius merged once in the
   rankings and the trend. A wrong merge means rollback plus one refresh.
2. `fund_sections` missing 0 on the 10-07 page.
3. C-S36's four names (8053 JP, 9433 JP, RBLX US, 000270 KS) read as names.
4. The PARSEKYABLE_DES points of the run, and eb-1's bound (Bloomberg unreachable ends in 3 calls, if it occurs).

Then the ledger `etfs-rivalfunds-pk1-al1` closes.

## 4. ENRICHMENT LIST (round 14)

1. The audit page's own size rule (ruling 4).
2. Whatever the morning pass returns as a row.

Still OPEN and carried: S24 (the backfill-night proof) and W6-S2 (the planted proof not yet built).

## 5. ACTS FOR ANDREW (cited)

- **One click:** open the audit link on `mcp.opalinvest.dev/rivalfunds` (ruling 1).
