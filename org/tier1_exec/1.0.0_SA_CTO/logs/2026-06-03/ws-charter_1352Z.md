# ws-charter cycle — 2026-06-03 1352Z

**CLASS:** NOVEL (Andrew-direction gate satisfied)
**Trigger:** ANDREW_DIRECTION relayed by 2.0.0_SA_COO (`20260603T134955Z`) — Andrew walked the Advisor Intelligence product live with COO 2026-06-03, dictated a 6-item FE-refinement batch, confirmed list complete, moved to staffing. COO asked ws CTO to author the FE PRD.

## Authority

NOVEL authoring authorized — Andrew direction present in inbox this cycle (/ws-charter Step 4b ladder #3). HARD-BLOCK #7 (new project) override path = NOVEL/Andrew-direction. No destructive/TIER0/cross-fabric/broker class. Clear.

## Action

Authored **`docs/architecture/ADVI_FEREFI_PRD.md`** (v0.1) — code-grounded FE PRD for the 6-item batch:
1. Assets Overview defaults → Year + 3Y (`PartnerAnalytics.tsx:124-125`)
2. Remove user-visible "(pseudonymized)" labels, keep logic (`ClientDetailPage.tsx:99` + `DistributionTab.tsx:1623/2255/3289`)
3. Remove Segment-Analytics category search bar, both firms (`DistributionTab.tsx` ~1685-1733 + ~2305-2360, state :1256)
4. Lifetime Activity defaults → Max + Year (`AdvisorAnalytics.tsx:179-180`)
5. AUM tooltip period-over-period $ + % (extend NNA delta pattern `AdvisorAnalytics.tsx:358-374` to tooltip ~579-601)
6. Fee-paying: kill synthetic "approx" (`AdvisorAnalytics.tsx:460` + `feeBucket.ts:209`), use REAL `*_fee_paying`/`*_no_fee` substreams [CROSS-LANE FE+DS] — Inflection back-attribution from earliest fee record per Andrew

**ws CTO independently re-verified all 6 code citations against live portal/DEV before authoring** (COO's pre-scope confirmed accurate; the :643/:2832 pseudonymized hits are comments → leave).

## Dependencies / sequencing

- Items 1-5 = pure FE (immediate on decompose).
- Item 6 = FE+DS; FE gated on DS emitting real fee substreams. DS = `0.4.0_DS_ClientPlatform` (Andrew bringing on; first task = fee-history feasibility per firm). Fee classification + back-attribution = gold-tier (Rule 17).
- Whole batch bundles into the next DEV→PROD promote behind Andrew's smoke, with footnote 548c9d7d.

## Follow-on

- Notify COO: PRD landed (path + suggested code ADVI_FEREFI + FE/DS split + #6 DS-dependency flag). COO owns registration (project JSON + REGISTRY) + TO-decomposition (RD-AI FE lane + DS) per the INFPRM division.
- Next promote manifest now = 548c9d7d (shipped) + ADVI_FEREFI batch (on landing) — HELD for Andrew GO, gated on his INFOTD/INFNNA smoke too.

## Infra note

Inbox Monitor exit-143 (SIGTERM, external) twice this session (b2wm8ngwb, bkzhydism) despite LD-0146 persistent-Monitor model claiming exit-143 eliminated. Re-armed bzvlfp4ih. /ws-charter cron inline check-inbox is the reachability backstop. Watching; will flag to fabric-infra (AE/MSTR) if it recurs.
