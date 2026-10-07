# MDPF_HEALGAP PRD v0.1 -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (dell1), under NFRA_CTLPLN PRD v0.12 addendum C-ROLES (relay msg 27, origin 2f61412157).
**Object:** `org/missions/D8/MDPF/MDPF_HEALGAP/prd/MDPF_HEALGAP_PRD.md` @78db344481, half_hash `ef2b06ddba52` (delivery msg 37).
**Brief:** `docs/briefs/mdpf-healgap-midstream-brief-20261007.md` @a8c67a424e, read whole.
**Verdict: SIGN.** Three wording findings, none blocking.

## Checks

| Check | Result | Evidence |
|---|---|---|
| ENDPOINT vs ratified pins | PASS | Andrew-direct record line 9 bytes match the PRD quote; 2026-08-31 word matches `docs/architecture/MDPF_HEALGAP_BRIEF.md:7`. Neither word sets an outcome; the six FWDs trace to brief O1-O6 one to one. |
| Brief coverage | PASS | O1->FWD-1, O2->FWD-2, O3->FWD-3, O4->FWD-4, O5->FWD-5, O6->FWD-6. Brief PART V.1-V.5 each land as a contract (C-IDEMPOTENT, C-COMPLETE, C-SESSION, C-VENDOR, C-FIX-NOT-NOTIFY). |
| Operative constraints in the half | PASS | vendor word (C-VENDOR), no shadow pipeline (C-ONE-PIPELINE), moratorium (C-FIX-NOT-NOTIFY), naming (C-NAMES), session mint time not moved (C-SESSION). |
| NO FWD IS A WAIT | PASS | FWD-1 is driven deliberately with the natural failure as the negative arm; FWD-2/3 exercised by act; FWD-4/5/6 APPLIED. |
| Substrate citations | PASS | `cot_rebalancer_runner.tf:171` `cron(0 6 * * ? *)` PLACEHOLDER; `:228-229` retry 2 / age 21600; `:232` on_success. `cot-pipeline/schedule-et.tf:90` `cron(30 7 * * ? *)`, `:86-87` 13:30Z floor, 54m margin. |
| CONTRACTS vs counterpart PRD | PASS at table grain | `ADVI_COTBKF_PRD.md:108` C-HOMES writes `blackdiamond/cottonwood/bronze/crm/...`; HEALGAP writes the `rebalancer_*` tables under the same `blackdiamond/cottonwood/bronze/` prefix. Disjoint tables, shared prefix: "share no write surface" holds at the table, not the prefix. |
| Seat names / history inside ENDPOINT | PASS with F2 | no seat name; two annotations (F2). |

## Findings (wording; for `1.0.0_SA_CTO~DELL1`)

- **F1.** The header JSON reads `"fabric": "laptop"`; the PRD was written on dell1 and is placed there (5e3b7edf26), and v0.12 C-ROLES assigns the signer by the box that wrote the PRD. Set it to `dell1`. Outside the half.
- **F2.** Two annotations inside the ENDPOINT block: FWD-2 SOURCE "(ten days with two of three parts landed)" and FWD-5 SOURCE "(a mitigation that makes FWD-1 rarer, never a replacement for it)". Move them to section 1 or the CONTRACTS.
- **F3.** The exercises of FWD-1 and FWD-3 are held on Andrew's vendor word (ACTS 1 and 2, C-VENDOR). The hold sits in the half but not on the two outcome lines. Add "held on ACT 1" / "held on ACT 2" to their DONE WHEN lines, so a reader of the ENDPOINT alone does not read the outcome as exercisable on demand.

F2 and F3 change ENDPOINT bytes. Under proportionate sign-off (CLAUDE.md rule 27, L4-R) that re-sign is a formality and withholds no delivery.

## Not checked

- The served Cottonwood series and the runner's guard code (the PRD says it has not read them either; hop 0 reads them).
- Whether `prd-signoff.py` accepts this base serial signing on a second box (v0.12 UNMEASURED). This stamp is that read.

-- 3.0.0_SA_CVO
