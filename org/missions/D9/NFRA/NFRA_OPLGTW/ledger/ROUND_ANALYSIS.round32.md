# NFRA_OPLGTW -- ROUND 32 ANALYSIS (L10)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~18:5xZ. This seat leads the site-Z fabric, and `1.0.0_SA_CTO~O` is retired (Andrew-direct
2026-10-09 ~07:4xZ). **Slug:** `3.0.0_SA_CVO~Z` msg 32914, `surprise-channel/remediations/REMEDIATION_v15.md` @87eb2d141f, read whole.
**Round state:** round 32 is terminal, 14 of 14 orders complete, and round-close-check reads MAY-CLOSE. Round 33 is in flight
(bh-1, tl-1 and ab-2 pending), so **round 33 is not re-cut**. The enrichment list below is cut as **round 34**, after round 33's
drain, by one issuance (one open round per issuer).

## 1. What round 32 did (from the slug)

- L9 (`ADJUDICATION_v23.Z.md`): C-S59 OG-bf-1 AC3 PASS; C-S60 OG-da-1 AC3 PASS, BOUNDED (1 of 6 callers has called since the deploy).
- L8: 26 rows dismissed, 15 graduated (below). 12 round-33 rows stay OPEN on purpose, and none is BLOCKING or ARMED.

## 2. Rulings on the 15 graduated rows

| row | standing | ruling | carrier |
|---|---|---|---|
| **W49-S1** KMS key gives the gateway no use | ARMED | **REMEDIATED in the world.** `NFRA_TRNSPT.TO-APPLY-ka21` is complete (dell2 MSTR via msg 32927). This seat read the key policy: `44a2284f` carries `GatewayWritesTranscripts` = `kms:GenerateDataKey`, `kms:Encrypt` for `opal-gateway-role`, with no Decrypt (6 statements). The issuer DISARMS it with a citing row | issuer row |
| **W49-S4** market_update PutObject grant not added | ARMED | Stands as ruled @14cbf27dec: the missing registry row is added first (rule 30), then the grant. It rides the `.pptx` cell. dell2 also reads 0 of 29 S3 write statements on `opal-data-transcripts` for the gateway role today | round 34 cell E1 |
| **W49-S3** two writers, two naming rules on one prefix | ARMED | **RULED: one rule, content-addressed.** Both writers use `deck_<sha16>.pptx`, and the sanitized original name goes in object metadata, never in the key. A write-once key whose body is a function of the key cannot land one deck twice. The `.pptx` cell carries it, along with a test that the same bytes from both writers produce one key | round 34 cell E1 |
| **W44-S4** `/login` consent asks the full GRAPH_SCOPES envelope | INERT | **Condition on r30:** the r30 never-widen ask lists the consent delta scope by scope (Mail.Send, Mail.ReadWrite, Files.ReadWrite.All ...), and the CVO half reads it before release. tg-1 stays held until then | r30 ask |
| **W44-S3** two tests pin the concierge as scoped | INERT | Re-pinned in the r30 release cell | r30 cell |
| **W44-S2** `sender_upn` null on channel paths until User.ReadBasic.All | INERT | **RULED: accept null.** It fails closed and admits no one, and adding a Graph consent for a display field is a widening that the use does not need. The PRD records it at the next addendum that touches C7 | PRD note |
| **W42-S1** grant-writer Lambda ships a stale contract, refuses `calendar_months` | ARMED | **Cell:** rebuild and redeploy `mcportal-grant-writer` from r29 under its own pair. **This also settles half of W39-S5:** the opal-gateway root's drift IS this Lambda's code hash | round 34 cell E2 |
| **W39-S5** two unrelated unapplied drifts; whole-root applies unsafe | ARMED | Stays ARMED with targeted applies. The opal-gateway half closes with E2. The opal-assets half (`cot-rebalancer-runner-daily` cron) goes to ADVI_COTBKF's issuer as a one-line ask from `2.0.0_SA_COO~O` | E2 + ask |
| **W43-S7** a cold 13-month read takes ~221-235 s per master | ARMED | **DESIGN FORK (warm vs cap vs async):** routed to `4.0.0_SA_CRO~Z` for past patterns this tick, ruled when the research lands. Until then, the 13-month read is not advertised to Alyssa as interactive | CRO ask |
| **W35-S1** OG-dr-1 still `pending` since round 30 | ARMED | **RULED: close OG-dr-1 SUPERSEDED.** Its branch was never drained (ruling msg 31464), and the gateway has moved on to r29. The restart-free route in `server.py` becomes its own cell | round 34 cell E3 |
| **W38-S1** proof-of-spec count-bar misreads a pytest summary | INERT | A tool defect in `.tools/proof-of-spec-check.py`, the integrator's lane: routed to `0.0.0_AB_MSTR~Z` as a one-line ask. This seat owns the row and the routing | MSTR ask |
| **W39-S1** enumerate leaves a stale session lock | INERT | Release the lock on the enumerate branch | round 34 cell E4 |
| **W39-S2** one-file range prints `2..0` | INERT | Cosmetic. It rides E4 | E4 |
| **S69** `lambda-source-map.json` stale for silver-schwab | INERT | Refresh the three fields to the deployed build | E4 |
| **S70** advi-49f-gold-dispatch zip cannot carry BUILD_MANIFEST.json | INERT | **RULED: correct the text, do not grow the zip.** Fix the `_build_note` and the two OG-bf-1-Y halves' wording; the source map stays the build record | E4 |

## 3. PRD addendum this round

**v2.5 (C4): `copy_site_file_to_s3` named.** One write tool, one builder prefix, no overwrite, and a holder count printed at Phase C.
It answers `3.0.0_SA_CVO~Z` msg 32942. The ENDPOINT is untouched.

## 4. ENRICHMENT LIST (round 34, cut after round 33 drains)

- **E1. The `.pptx` market_update writer, made writable.** Registry row first (W49-S4), then the PutObject grant on
  `opal-data-transcripts` `sharepoint/transcripts/bronze/market_update/*` from builder output; one content-addressed naming rule
  for both writers (W49-S3). The KMS leg is already done (W49-S1). Never-widen pair.
- **E2. Rebuild `mcportal-grant-writer` from r29** (W42-S1). This clears the opal-gateway half of W39-S5. Never-widen pair.
- **E3. The restart-free route to the lost answer in `server.py`** (W35-S1). OG-dr-1 is closed SUPERSEDED.
- **E4. Batch repair (worker-light):** the enumerate lock release and range print (W39-S1/S2), the silver-schwab source-map refresh
  (S69), and the BUILD_MANIFEST wording (S70).

The r30 release cell carries the W44-S3 test re-pins and the W44-S4 consent delta. W43-S7 waits on the CRO.

## 5. Order of releases (unchanged)

MX-r-9, then MP-r-2, then OG-rl-16 (E2 `.xlsx`, the three halves signed: COO @153e507b79, CTO @5e258448d2, CVO @9b6003cd3b).

-- 1.0.0_SA_CTO~Z

## ADDENDUM 1 (~19:3xZ): W43-S7 RULED on the CRO's research

`4.0.0_SA_CRO~Z` msg 32958, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESEARCH_OPLGTW_W43S7_LONG_READ_PATTERNS_20261009.md`
@891f920463. This seat verified `catalog.py:841-870`: a stored snapshot is returned before any verification, and a new one is persisted
write-once (`ConditionFailed` reads the existing one back). **So the 221-235 s figure is a cold, one-time cost per date, not a per-read
cost.** It was measured on a MemStore harness.

**RULED (d), replacing my pending rec of (c):**
1. **Prime** the 13-month window once per master: a one-off read, not a standing job, because the daily increment is one date.
2. **Measure** the warm 13-month read on the served gateway.
3. Only if the warm read is over the 60 s ALB default, add the 8-thread bounded fan-out (the `admin_fabric.py` pattern) to the
   per-date loop.
4. Only if it still does not fit, build (c), the async handle.

This becomes **round 34 cell E5**: steps 1-2 as one measured read, with step 3 conditional in the same cell under its own criterion.
The 13-month read is not advertised to Alyssa as interactive until step 2 reads under 60 s.
