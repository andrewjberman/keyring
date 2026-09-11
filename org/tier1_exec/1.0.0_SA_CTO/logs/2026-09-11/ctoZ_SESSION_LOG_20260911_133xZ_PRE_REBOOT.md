# 1.0.0_SA_CTO~Z -- PRE-REBOOT STATE LOG (2026-09-11 ~13:3xZ)

Written on Andrew-direct relayed by `0.0.0_AB_MSTR~Z` (msg 21380), VERBATIM: *"have everyone take
/log of current state and ill reboot this device"*. **Written for a successor with NO context.**
Every site-Z session dies at the reboot and NOTHING RESPAWNS.

## 0. WHO THIS SEAT IS AND THE ONE THING TO RE-ARM

`1.0.0_SA_CTO~Z` -- site-Z CTO lane. Owns L2 (endpoint) / L3 (register) / L4 (PRD) and **L10
grading** for two projects. Does NOT cut task orders (Rule 27: TOs are the COO's).

⭐ **THE STANDING ORDER, and it OUTLIVES the reboot.** Andrew, `/self-drive AMGT_RESAPP &
POSN_ASTTAX`, bracketed intent VERBATIM: *"I need you looping every 30 min to make sure no slug
fell through the cracks, that no PRD is going unstamped and COOs are waiting, make sure nobody
drops the ball and keep us on /canonical-flow"*. Ticks 1-11 ran; last tick log @`17e1966cff`.
- **The carrier clause in `org/XXX.md` @`0fb2a1f0b0` is NOT STRUCK and MUST NOT BE.** It is the
  only thing a successor may re-arm from (`/self-drive` §0.4/0.5). Cron `a8f7f439` dies with the
  session; the carrier is the durable half. **Re-arm `/self-drive AMGT_RESAPP & POSN_ASTTAX` after
  relaunch.**
- ⚠ This is a **SUSPENSION BY REBOOT, not `STOPPED-BY-OPERATOR`.** Andrew stood down the DEVICE,
  never the scope -- so the loop is not closed out and its completion test (both projects
  `status: complete`) is still 0 of 2. Recording it as operator-stopped would silently retire a
  standing order he did not retire.
- Priority order he set: **AMGT_RESAPP and POSN_ASTTAX first; IAMROLES deprioritized behind both.**

## 1. OWED TO THIS SEAT (what a successor waits for)

| owed by | what | state at reboot |
|---|---|---|
| `3.0.0_SA_CVO~Z` | **AMGT_RESAPP round-4 slug** (`REMEDIATION_v4`) -> this seat grades it at L10 | NOT SENT |
| `3.0.0_SA_CVO~Z` | **AMGT_RESAPP v0.4 ratified-text sign-off** (gates the SURFACE round) | NOT SIGNED |
| `2.0.0_SA_COO~Z` | **POSN_ASTTAX round-2 slug** | round 2 mid-flight, PARKED by the reboot |

⚠ **The CVO was the SOLE critical path at reboot and had not consumed 3 messages** (21363, 21366,
COO~ZZZ's 21375; `get_delivery_state` = QUEUED, 0 of 3 READ). One consolidated nudge was sent
@13:19Z. **This was NOT diagnosed as a deaf seat** -- fresh heartbeat, reliable consumption all
session, and a Codex bridge that may simply not stamp broker clocks. MSTR's directive is explicit
that these two acts are **recorded as OWED, not rushed through at 0.2 GB free.**

## 2. AMGT_RESAPP (D5) -- where it stands

- **PRD v0.4** @`bbbf35c38e`. 15 outcomes; bar distribution **14 of 15 EXERCISED**, FWD-9 APPLIED.
  FWD-15 (the Lead Panel) is Andrew's own confirmed outcome, minted on his "Recs approved" ~12:1xZ
  (record: `.../ANDREW_DIRECT_20260911_121xZ_OPEN_CALLS_ALL_FOUR_RECS_APPROVED.md`).
- **Sign-off (`python .tools/prd-signoff.py status AMGT_RESAPP`): WITHHELD.** Brief half SIGNED by
  `4.0.0_SA_CRO~Z` @`1b7a996c86`; ratified-text half OWED by the CVO. ⚠ **The gate is CONTENT-keyed,
  never version-keyed** -- read `status` before asserting any re-sign is owed (this seat got that
  wrong once and broadcast it to two seats).
- **Rounds 1-3 graded** (`ledger/ROUND_ANALYSIS.round1/2/3.md`). **Round 4 DRAINED** @`79ec889666`
  by `2.0.0_SA_COO~ZZZ`: rc-19 (the class-level S11 unresolved-overlay figure rule, per this seat's
  ruling) + rc-20 (S3 provenance -- distinct observation/vintage/derivation, emit `fig.source`),
  both TERMINAL + VALID; 2 judgment criteria + row W1-S6 (INERT). **C-S16 should close on these.**
  Independently corroborated by the CRO's holes-scan tick 6 @`133063934c` (30 tests, rule-alone
  negative control, CVO None-control end-to-end).
- **NEXT ISSUANCE = the SURFACE round (v5)**, `2.0.0_SA_COO~ZZZ`'s to cut via `/atom-decomp` **the
  moment the CVO's ratified-text sign lands** -- the .tsx shell, S16 Lead Panel + 3 tabs, infra
  tables-first. `infra/aws/terraform/amgt-resapp` **does not exist yet, and that is CORRECT
  sequencing, not a gap** (CRO measured it).
- ⛔ **Vendor word is NARROW:** Seeking Alpha / FT / Bloomberg / WSJ, **this project's harvesters
  only**, effective **when the harvester box is stood up and ready to run -- not before.** Not a
  blanket grant; `C-VENDOR-EGRESS` still binds every other vendor and use.
- ⛔ **`C-NO-CONTACT`: NO SEAT CONTACTS ADAM MULLER** (Andrew-ruled).

## 3. POSN_ASTTAX (D4) -- where it stands

- **PRD v0.5** @`66ded3a0c5`, **ADMITTED** (both halves signed at current bytes).
- **Round 1 graded: 0 of 6 REALIZED** -- a one-cell investigation round whose NEGATIVE result was
  its value (`ledger/ROUND_ANALYSIS.round1.md`, SUPERSEDED-IN-PART banner) plus
  `ROUND_ANALYSIS.round1-addendum.md` @`7f20d4f2d9`, which records Andrew's purpose ruling:
  *"ETFClassifier is basically a developing list of how we tag securities we own ... we basically
  just add things there as we need to"* -- so a missing scheduler is NOT a defect and the 169 are
  NOT unexplained.
- **Round 2 L7 wave 1 was executing** under the respawned `2.0.0_SA_COO~Z` (issuance @`f60de462ae`,
  7 orders): AT2-s-6 harden-the-generator on a cone-sparse worktree. **Wave 2 becomes a PARK at the
  reboot; its four cells spawn on the relaunched seat.**
- ⛔ **THE LANDMINE -- DO NOT LOSE THIS. `C-RETAG-SAFETY` (PRD v0.5).** Fixed-key dicts
  `management_allocations = {'active','passive'}` and the asset_class chain into
  `{cash, fixed_income, equity, hedge}`; a retag raises **`KeyError` in `calculate_allocations()`
  and blanks the page for all four partner firms.** It is **NOT latent** -- VXX is already held, so
  the next generator run after a retag fires it. **ORDER IS LOAD-BEARING: (0) harden the generator,
  (1) fix management_style, (2) verify the asset_class chain, (3) THEN retag.**

## 4. WHAT THIS SEAT HOLDS, OWES OUTWARD, OR PARKED

- **Worker subagents: NONE.** **Worktrees: NONE.** (Workers are COO subagents; this seat commits
  trivial one-file artifacts in the shared tree under Rule 14b non-application.)
- **Open calls at Andrew: 0** -- he cleared all four at ~12:1xZ.
- **Open task orders assigned to this seat: none.** This seat's obligations are L4 amendments and
  L10 grades, both of which wait on inbound slugs.
- **Not mine, carried for the successor:** the Rio.exe (Huntress) leak is `0.0.0_AB_MSTR~Z`'s and
  Andrew has chosen the reboot as the remedy; the audit-archive re-baseline stays parked at MSTR.

## 5. FIRST ACTS FOR THE SUCCESSOR (ordered)

1. `/watcher` + register `1.0.0_SA_CTO~Z`; read this log.
2. **Re-arm `/self-drive AMGT_RESAPP & POSN_ASTTAX`** off the `org/XXX.md` carrier clause -- commit
   the carrier BEFORE tick 1 (§0.5), then run tick 1 immediately.
3. `python .tools/prd-signoff.py status AMGT_RESAPP` -- if still WITHHELD, the CVO's ratified-text
   sign is the single highest-leverage item in the whole scope (it gates the SURFACE round).
4. Ask `3.0.0_SA_CVO~Z` for the round-4 slug; grade it at L10 the turn it lands.
5. Confirm `2.0.0_SA_COO~Z` un-parks POSN wave 2 and `2.0.0_SA_COO~ZZZ` holds the SURFACE round
   until the sign lands.

## Compiler Tools
`prd-signoff.py status` (both projects) · `get_delivery_state` (CVO~Z: 3 QUEUED / 0 READ) ·
`get_live_agents` · `ack_messages 21378` · inbox read of msgs 21378 / 21380 · `safe-commit.sh`.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes origin/SITEZ -- this seat does not push.
