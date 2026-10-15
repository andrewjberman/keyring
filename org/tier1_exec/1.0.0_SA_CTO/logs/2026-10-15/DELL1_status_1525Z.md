# dell1 CTO status -- 2026-10-15 ~15:25Z (`1.0.0_SA_CTO~DELL1`)

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE

Covers the window since self-drive tick 41 (@dbf0c2c446, 14:27Z), and the standing state for a reader with no prior context. Arming record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17).
**state: ARMED.**

## Andrew-direct, ~15:2xZ at this terminal (answers to this seat's /open-calls act list), VERBATIM

> "1.) I am having CRO identify what is going on with this box, if we discuss following their analysis and we really are at a natural
> checkpoint, then I will run the restart manually. 2.) Yes, the SECCLASS BD Mix production push is clear. 3.) Sign into the gateway via your
> /mcp or just go into the gateway? Explain. 4.) We have stopped that project. 5.) This will be discussed at a future date. 7.) Yes we
> definitely want to activate the batching but will do it post restart. You don't need to do anything right now aside from write a /log about
> current status/"

| item | his word | what it settles | act taken now |
|---|---|---|---|
| 1 restart window | the CRO is analysing the box; he restarts manually after that discussion, if it is a natural checkpoint | the restart stays held; he runs it himself | none |
| 2 SECCLASS BD Mix PROD push | "clear" | the client-facing push is APPROVED by Andrew | none this turn, by his instruction ("You don't need to do anything right now"). The owner is `2.0.0_SA_COO~M1`, through dell1's promote DT, when this seat next routes it |
| 3 gateway session | a question | answered in the reply (below) | read only: `whoami` |
| 4 ASTN FT hold | "We have stopped that project" | the hold item is retired; ASTN is stopped | none |
| 5 ADVI_BILLING answers | "discussed at a future date" | BILLING stays parked | none |
| 7 Security Analysis LLM batch tasks (G4) | activate "post restart" | APPROVED, timed after the restart | none until the restart |

**Gateway, item 3 (answered):**
- NFRA_OPLGTW FWD-21 is site Z's project. It needs one driven call by a real Opal asset-manager principal, through that person's own Claude
  connected to the Opal gateway (an MCP connector signed in with their Microsoft account), not a visit to a website.
- This session's gateway connector is already signed in as Andrew@opalinvest.com (`whoami`, read ~15:24Z).
- Whether Andrew counts as the "asset-manager principal" for the proof is site Z's CTO's to say; the record names the principal from the grant
  store.

**Open call (held for Andrew, not answered in this message):** `dell1-20261015T152025Z-494e`, Cottonwood's Opal Muni Income (~$64M), Other AUM
-> Custom Models. REC (a) yes.

## Window since tick 41 (14:27Z to 15:25Z)

- **MDPF_CANON:**
  - CVO L10 slug 6035 (MAY-CLOSE) was answered with the round-9 analysis plus PRD v2.22 @ff1e47f079. CN-j-1 AC4 is closed by retiring the
    history-route reader requirement; firm-scope chips stay as-of only (Andrew's 10-14 firm-view words).
  - The CVO re-signed v2.22 (ADMITTED).
  - Amendment 1 @ccb162ba19: a missing leg carries only if the carried row still partitions the served Total; `sma_additive_aua` stays absent
    on 08-31..09-09.
  - **Round 10 CUT** by `~D1` @922426e095: CN-r-1 (missing-leg carry), CN-r-2 (publisher read grant on `platinum/mdpf/*`).
  - E4 GO, ruled (b): 11 S3 request-metrics filters on `opal-data-assets` for 24 h, ~$1.8, removed after.
- **Cottonwood Trend:** the CRO spec @21caa664be is DOABLE. It starts at the first measured total (06-09), sets Other = custody total - model,
  keeps the interpolated band, and rolls the model leg forward on 12 dates. The Muni line waits on Andrew's call (above).
- **Laptop:**
  - W106-S5 (`safe_deploy_core.py` has one writer, IRPT_BCKEND) was applied by `~M1` and acked.
  - The merge-forward gap is recorded as NFRA_DEVPLN-S9. The project reopens one round on it; until then a CTO waiver is the route.
  - Crossbox 5b04 (FWD-3 test) and 9904 (package journey) were acked. The 9904 note "NONE" was re-carried via MSTR, because the direct send
    reached dell1's broker only.
- **/outcome-check** for the fabric since 4 PM ET 10-14 was published: https://claude.ai/artifact/RsNqswXeA1hZNZRDqKsrXF

## Current State (for a reader with zero context)

- **Box open calls:** `python .tools/open-calls.py list` reads rows=88, open=1. The open one is `494e`, HELD for Andrew.
- **Portal PROD:** `c3b21a40e2` (portal-v2.1.223, CI 38667132776 success). It carries the full-history Global AUA Trend (Variant 1 for
  staff, Variant 2 otherwise), the TRSB Excel fix and the J359 footnote deletion. DEV: `ad7c100b5c`.
- **MDPF gold:**
  - `mdpf-gold-lambda` runs build `8e2dd0fb36` (CodeSha256 `AEUuWyiM...`).
  - The 10-15 13:30Z scheduled fire wrote `s3://opal-data-assets/portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-14.json` with all
    four Trend keys (497 dates, 9 carried).
  - The served copy is `s3://opal-data-portal-v2/platinum/mdpf/global/aggregate-aua-timeseries.json` (version `Sqe2W_jJ`).
- **Edge:** `auth-validator-edge:24` (per-firm MDPF gate) is on the `/api/general/*` behavior of distribution `EVTSA9VEHNZVH`. A live
  foreign-firm 403 is unproven, because no MFA-free partner login exists.
- **J359:** `s3://opal-data-cot/platinum/satellites/characteristics.json` version `Qh56dS_I` (models + GLD).
- **ADVI_FIRMBKTS:**
  - FB-l-5 act 3 is live: `advi-inf-publish-daily` ENABLED cron(30 13), `advi-inf-publish-catchup-daily` ENABLED.
  - First-day reads are due 10-16 by 18:00Z (`0.7.0_AE_CloudOps~FB1`).
  - The trade-form pair (laptop CTO's half) waits for one laptop apply (P2, Oct 24).
- **dell1 restart:** HELD. Andrew runs it manually after the CRO's box analysis.
- **Live COO lanes on dell1:** `~D1` (MDPF_CANON, round 10), `~B1` (ADVI_FIRMBKTS), `~M1` (MDPF_SECCLASS), `~H1` (MDPF_SECHIST, round-6 L8
  packet drafting).

## Next Steps

- [2.0.0_SA_COO~M1]: the SECCLASS BD Mix PROD push is approved by Andrew ("Yes, the SECCLASS BD Mix production push is clear"). This seat routes
  it to the promote DT (`0.4.0_DT_ClientPlatform~H1`) on its next tick, since Andrew asked for no act this turn.
- [2.0.0_SA_COO~D1]: round 10 drain. This seat signs the CN-r-1 and CN-r-2 CTO halves on its COO halves, and reads E4's 24 h record.
- [4.0.0_SA_CRO~DELL1]: Andrew's box analysis (his item 1). The Cottonwood addendum follows Andrew's Muni answer.
- [0.0.0_AB_MSTR~DELL1]: after the restart, G4 activation (Andrew approved, post restart) goes to its owner. AMGT_RESAPP holds G4 per the
  laptop fold-in ruling @ee6e7a0fe0.
- This seat: hourly self-drive ticks; the round-10 pairs; the SECHIST round-6 analysis on its slug.

## Blockers

None blocked at this seat. The held items are Andrew's by his own words: the restart (item 1) and the Muni call (494e).

## Compiler Tools

| tool | result | note |
|---|---|---|
| `open-calls.py add/hold/list` | PASS | the Muni call written and held; `verdict=CROSS-BOX` measured, held for Andrew rather than cross-adjudicated, because two of his own words conflict |
| `opalgateway whoami` | PASS | the gateway is signed in as Andrew@opalinvest.com |
| `prd-signoff.py status MDPF_CANON` | PASS | v2.22 ADMITTED |
| `crossbox-call.py ack` | PASS | 5b04, 9904 |
| `comp-find` | PASS | missing-module census (0 of 13,575), G8 routing source |

- **What worked:** `open-calls.py hold` keeps a sovereign call out of the 10-minute scan.
- **What failed:** a direct broker send to a laptop seat lands on dell1's broker only. Cross-box notes go via MSTR.
- **Gap found:** `crossbox-call.py ack` takes no note, so the answer has to travel as a separate message.

-- 1.0.0_SA_CTO~DELL1
