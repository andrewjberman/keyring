# NFRA_TRNSPT -- ROUND ANALYSIS, round 4

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~17:4xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1345) and REMEDIATION_v3 @456ed16d42.
- Round 4 (issuance 6f698f1b9b) is terminal: TR-w4, TR-l4, TR-r4, with 0 judgment criteria.
- ARMED 0.
- D2-S1 (owner CRO) and D2-S2 (owner this seat) graduate OPEN.
- The issuer's served act C3 is in the ledger `20261007T1531Z_nfra-trnspt-c3-driven-positive-arm-20261007` (@4b65bc698e).

## 1. State

- **FWD-7 is MET (positive arm, driven).** The EventBridge fire `20261007T233013Z`, scheduled and with no person starting it, landed 3
  admitted feedback emails (2026-09-02, 09-15, 09-17): 12 objects, hashes 9 of 9, held_out 3 of 3. The negative arm is the five empty
  scheduled days of 10-02 to 10-06. The CVO concurs: FWD-7's DONE WHEN is met by the 3 admitted messages, and D2-S2 does not hold it.
  - **What remains is open:** ledger L5, "the 2026-10-08T23:30Z fire reads `window_days=7`", is owned by `~T2`. FWD-7 grades REALIZED when
    L5 closes.
- **D2-S2 (the 2026-08-11 message did not land):**
  - In SOURCE, both ends page to the end: `gateway_mail.py:147-168` and `mail_route.py:327,376`.
  - So `listed=100 = 4 x 25` is truncation only if the RUNNING gateway differs from that source, or Graph returned no `nextLink`.
  - The census must read deployed bytes (rule 22a). This seat owns the remedy and seats it as E2.
- **FWD-1, hops 1-2 (the TR-r4 record):**
  - The `/hx/transcripts` route is released (deployed commit 240ac2fe5a, EC2_MANIFEST:503-506).
  - G-TEAMS-TX is DROPPED: attributed transcripts were returned live.
  - The route serves NO meeting: its meeting allowlist is empty (NFRA_OPLGTW row Z-W15-S30). The allowlist's values are THIS project's
    data asset, so the next hop of the thread is ours, as E1.
- **D2-S1 (teams-chat test imports break single-process collection):** with the CRO (its owner). It is drain hygiene and holds no FWD.

## 2. ENRICHMENT -- round 5, ONE issuance by `2.0.0_SA_COO~T2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The meeting allowlist data asset (FWD-1, then FWD-2).** A versioned file in this project naming each regular investment meeting series by its stable identifier (the Monday meeting first), with the source of each row. It is handed to the gateway's owner through `0.0.0_AB_MSTR~DELL2` (cross-fabric). | (1) the file lists the Monday meeting series, with its identifier read from a calendar or meeting record and the source line printed; (2) a test loads the file and rejects a row with no identifier or no source; (3) the handoff message id to MSTR is recorded | LOCAL |
| E2 | **D2-S2: truncation or classification, read against the running gateway.** First compare the deployed gateway bytes for `mail_route.py` (the manifest's `deployed_commit` 240ac2fe5a, then `git show` at that commit) with HEAD. Then take ONE counts-only listing of the 2026-08 span per sender. | (1) a record states deployed = HEAD or names the diff, from `git show 240ac2fe5a:...mail_route.py` beside HEAD with a positive control; (2) a counts-only record per sender and span (listed, pages, `nextLink` present yes/no) decides truncation or classification; no subject, address or body appears in it | LOCAL |

Where a gateway listing needs a route that dell2 does not hold, E2's second criterion is run through the fenced-read path, and its record
says so.

## 3. Placed with others (one line each)

- FWD-8's second named reader, the 14 flagged words, and Kimi K3: unchanged from round 3 section 5.
- The allowlist's load into the running gateway is the gateway owner's act (NFRA_OPLGTW). It is asked through MSTR, and the seat never
  edits the gateway.

-- 1.0.0_SA_CTO~DELL2
