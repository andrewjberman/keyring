# 1.0.0_SA_CTO~Z -- /self-drive "AMGT fabric ops", ticks 40-41 (15:0xZ-16:12Z), 2026-09-30

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md` @`64a6172e7b`.
**state: ARMED**

## Scope

- **4 projects:** each `active`, `EXECUTING`. 0 of 4 complete, 4 of 4 REACHABLE.
- **Inbox:** empty at both tick starts. 27235, 27237, 27241, 27243 and 27251 were acked.

## In scope

| item | receipt |
|---|---|
| **RESAPP ac-3 (the slash-key window) LANDED** | AC1 40/40, AC2 273/273 (`/timeline` serves `publishers_found_codes`), AC4 OK. AC3's post-act re-scope (only `*_read` provenance strings; a planted control outside them FAILS) is ACCEPTED on this seat's half, AMENDMENT 1 @`05a090d804`. No rollback, and the CVO reads it at L8. |
| **Portal DEV pushed** by MSTR~Z (27243) | origin/DEV `afa0597d9a`. This seat verified DSGN l-1's portal commit `5f9e802a` is an ancestor, so Andrew's condition held. |
| HARVST ab-3 phase A0 merged (@`ffe564672b`) | a 402 keeps its body and gets ONE fresh-session retry: the Seeking Alpha correction (@`7db0a2f4d3`) in code |
| DSGN round 13 | l-1 (the no-dossier reader) and l-3 drained |

## Outside the scope, on Andrew's words (ETFS_RIVALS)

- **Endpoint Addendum A** @`bd6effc4f3`, from `4.0.0_SA_CRO~Z`'s midstream brief (27235). Andrew confirmed it via the CRO (27241), with
  FWD-1 covering both Opal ETFs.
- **Andrew-direct ~15:5xZ, recorded @`fdc881a489`:** *"establish in detail what the gold table structure is, and how that table
  structure feeds these served insight deliverables."*
- **PRD v0.3:**
  - endpoint lines @`5bababb75b`. **This seat's error:** that commit's message named C-GOLD-MODEL, which it did not carry, because a
    shell quoting failure dropped the contracts step. It was corrected in the next commit's message and in provenance.
  - contracts @`cbf0cfd6b0`: C-PEER-GROUPS, C-HOME-PRODUCER, C-INCOME-CLEAN and **C-GOLD-MODEL**. That is 14 builder-addressed gold
    tables (grain, key, columns, claim, producer), plus a lineage matrix mapping each served insight to its tables, the
    deterministic part and the AI prompt's allowed reads.
- **Round 1 drained, 9 of 9** (27237). The one human act left is Andrew's signed-in `/rivalfunds` read.

## Acts only Andrew can do (cited)

- The CLAUDE.md NEVER-2 edit; the text has been shown to him [locked to his order].
- The portal PROD promotion [CLAUDE.md Portal].
- ETFS_RIVALS: one signed-in `/rivalfunds` read, the FWD-1 live trace [his login].

## Compiler Tools

| tool | result | note |
|---|---|---|
| `lib/opal_naming.address()` for 14 gold tables | PASS | 14 of 14 builder output, 0 refusals |
| `git -C portal merge-base --is-ancestor 5f9e802a afa0597d` | PASS | the push condition held |
| `prd-manifest` gate on both v0.3 commits | PASS | ENDPOINT, header and outcome cards agree |
