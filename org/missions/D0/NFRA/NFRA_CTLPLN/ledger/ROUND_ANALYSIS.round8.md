# NFRA_CTLPLN -- ROUND ANALYSIS (L10), round 8, closed 2026-10-12 ~10:4xZ

Author `1.0.0_SA_CTO` (laptop). Slug: `3.0.0_SA_CVO~L` msg 108510 on `2.0.0_SA_COO~C` msg 108508; compile ADJUDICATION_v10 +
REMEDIATION_v2 @c7d905d457. Previous: `ROUND_ANALYSIS.round7.md` @50a5de46f8. PRD v0.25.

## 1. What the slug carries, and the rulings

| item | the CVO's read | ruling |
|---|---|---|
| TO-CT-w-6 CTw6-AC2 | MET (C-S31): one writing box per crossbox path; the derived state equals `derive_state` for every combination; note: "HALF-CLOSED inside ACKED" reads OPEN when there is no ack | accepted; the note is a design-text correction for the crossbox doc, a hygiene line in round 9 |
| GRADUATED | D1-S8, D1-S10 (owner COO~C), W65-S2 (owner this seat), W61-S1 | accepted; W61-S1 graduates to remediation but stays ARMED -- its disarm is Andrew's elevated line (re-read 10:4xZ: remote=Any, sshd Running); W65-S2 is this seat's carrier regen at the next cycle |
| DISMISSED | W65-S1 (targets rc 0, 96 selftests), W65-S3, W65-S4 (deploy.sh retired), W68-S7 | accepted |
| the gate's L10 exception | remediation rows admitted though CT-w-8/9/10 opened after the census (Andrew call 1, CTO 21533) | accepted as the named exception; the three orders are round 9's first items |
| `round-close-check --round 8` | 38 orders, 36 complete, proof_bad 0, 3 of 3 judgments graded, MAY-CLOSE; all 64 gating items dispositioned | round 8 is finished on this box |
| 15 OBSERVATION/INERT rows | noted, not dispositioned | stand as noted |

## 2. Grades (delta from round 7)

FWD-28: the fence is LIVE on all 41 routes (CT-u-7 and CT-w-3 applied and verified: deployed members at the pin's hashes,
pre-apply not_admitted=0, admitted firm 200, class-ii partner 403) -- EXERCISED; REALIZED waits on the portal carrier landing
on DEV with the registry notes (ruling 108503) and the S9110 redaction pair. FWD-27: unchanged, gated on Andrew. FWD-3/22 advance
on CT-w-6 (crossbox state derivation). Nothing else moves.

## 3. ENRICHMENT LIST for round 9 (ONE issuance, `2.0.0_SA_COO~C`)

- First: CT-w-8, w-9, w-10 as opened (the S9110 redaction under its third pair; the cookie/refresh census with its STOP).
- The portal carrier regenerated with the registry `note` field, set-equality re-proven, landed on DEV by the author (PROD on
  Andrew's word); the crossbox design-text correction (HALF-CLOSED/OPEN wording).
- E1-E8 of the 2026-10-09 list, still uncut after three short rounds: cut at least E1 (the re-based live thread) and E4
  (the 12-message matrix) this round; the rest as capacity allows, with a stated carry for each not cut.
- E9 FWD-27 stays gated on Andrew's public keys and elevated lines; no cell runs without them.
- S9111 (partner `/api/scoped/partners` calls reaching the proxy's `$default`) stays OPEN with the shared portal API root's
  owner named; not this round's cell.

## 4. Owed outside the project

Andrew: W61-S1's elevated line on the laptop (ARMED, graduated, unchanged); public keys + elevated line per box for FWD-27;
the PROD push of the portal carrier once on DEV; the Tailscale ACL at his convenience.
