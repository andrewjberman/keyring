# AMGT_RESAPP round 21 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `8573b625b4`, LOCAL (push is `0.0.0_AB_MSTR~Z`'s, LD-0522).
**Written:** 2026-09-21 ~23:4xZ. **DRAIN-END, complete:** 6 of 6 terminal, 0 open.

Round 21 was issued as one slug @`6fb0f4d0bf`: decomposition s.29, six orders, rk-82's COO half, and the four SUPERSEDED
flips (rk-32, rk-50, rk-51, rk-52). rk-82's pair was completed by the CTO half @`b3d76bc9c1`. The spawn order was:
- wave 1: rk-81 and rk-82;
- wave 2: rk-83 to rk-86, from one commit (`0731c87fca`), after rk-81 drained.

## 1. Round state, final

| cell (slot) | drain | second instrument (this seat's own) |
|---|---|---|
| rk-81 (~81) H0-store | `0731c87fca` | Called the store directly on inputs the worker's tests did not use. `entity_partition("security_key","NG/_LN_Equity")` returns `security_key=NG-SLASH-_LN_Equity`. Lusha silver with a camelCase `phoneNumbers` raises SilverRowError. Lusha `bronze_put` raises LushaExceptionError. A reserved metadata key `schema-version` raises HarvestStoreError. Merged tree: harvest + identity + api = 257 passed. |
| rk-82 (~82) H0-iam | `bf0f9a30ce` | Read both LIVE inline policies with `iam.get_role_policy`. Statements stay at 4 and 4. New-grammar resources: exactly 8 on opal-amgt-scoped-api-grants (bloomberg bronze/silver, seeking-alpha bronze/silver, sec/barrons/wsj/ft silver) and exactly 4 on amgt-resapp-chatter-axis-lambda-policy (barrons, wsj, ft, seeking-alpha silver). |
| rk-83 (~83) H1 Bloomberg | `91ce5cd1f6` | `client_json` gives identical bytes for two dicts with the same content in different key order. A recording stub on `store.bronze_put` shows `metadata={"received-form": "bbg-client-json"}` and partition `security_key=BP-SLASH-_LN_Equity`. `request="pull_log"` is refused. harvest + identity = 75 passed. |
| rk-84 (~84) H2 filings | `fb8ff7fd28` | Ran `vendor_source` on LIVE objects: CAT's `000001823026000008.source.json` resolves to `sec`, and CSL's `UNRESOLVED-SOURCE.source.json` raises NoVendorSourceError. harvest + filings + identity = 162 passed. |
| rk-85 (~85) H3 SA + publications | `8573b625b4` | `git diff --name-only` from the merge-base changes 0 of the six walled files (catalog.py, storage.py, __init__.py, config.json, schemas), and every changed file is inside `<paths>`. The worker's AC7 is the build-INPUT-list proof: adapter 57/57 and chatter 18/18, 0 members changed. SA + harvest = 37 passed. |
| rk-86 (~86) H6 social | `a44ae2b298` | Read the `collect.py` diff: every new store call sits under `if write_harvest:`, which defaults to False. The 9 pinned existing names are byte-identical (the worker's AC5). 0 schedule references across 8,616 tracked files. social = 40 passed. |

Every writer is code only and off by default: 0 live S3 writes and no production importer. Only rk-82 performed a live act,
a targeted IAM apply (0/2/0); its ledger entry was opened before and closed after. No rollback fired.

## 2. For the grade

1. **rk-84 AC3 (row W84-S1): re-run it from a FILE, not by typing it.** The criterion's inline `python -c` carries a
   `b"\r\n"` escape. This box's tool transport collapses doubled backslashes, so the literal typed text raises a
   SyntaxError. The worker recorded a byte-compensated re-run, in which both mutants fired. The defect is in the ORDER'S
   transport, not in the cell. It is disarmed by Z-S207 @`dbc1d57f4b`, and this seat's escape-bearing criteria run from a
   file from now on.
2. **rk-83 row W83-S1 (INERT, dismissed):** the order's prose said the store adds 10 arms; it adds 11. AC2 grades by the
   re-measured baseline.
3. **rk-81 L5 at the cut:** CONTACT_FIELDS match by normalised name (camelCase caught). The CTO endorsed this (msg 24112).

## 3. Rows (this round)

| row | disposition / owner |
|---|---|
| W83-S1 | dismissed by the worker |
| W84-S1 | disarmed by this seat, Z-S207 |
| **W85-S1 (ARMED, owner this seat)** | OPEN. `lib/` has no `__init__.py`, so pytest imports a test under `lib/opal_data_harvest/` as the bare package `opal_data_harvest`, while production code imports `lib.opal_data_harvest.X`: two module identities for one source, so a monkeypatch on one is invisible to the other. rk-85 avoided it in its own two test files; the repo-wide trap remains. Routed to `1.0.0_SA_CTO~Z` as a round-22 candidate cell (a repo-level import fix touches every `lib/` package, so it is a spec call, not an L5 edit). |

## 4. What this seat asks of L9/L10

- Grade the 6 terminal cells on their branch-HEAD criteria. None carries a judgment criterion.
- **Round 22 candidates:**
  - the **portal PROD promote** as an order to `0.2.0_DT_PortfolioAnalytics` (accepted, msg 24116);
  - **H4 and H5**, drafted as rk-87 (Lusha, silver only) and rk-88 (Bright Data SERP), with two calls open for their cut;
  - W85-S1's import-trap fix, if ruled;
  - the **moves M1..M4**, where each move that removes an old grant first re-reads its new grant (CTO condition, msg 24112).
- **Backfill runs B1..B5 need Andrew's cards.** They are raised at the wave they gate.
