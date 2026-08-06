# MDPF_CANPLAT — Decomposition of MDPF_CANONICAL_PLATINUM_PRD @24d3eb2f8

**Author:** 2.0.0_SA_COO~Z (fresh session, Andrew-direct reset) · **Date:** 2026-08-06 ~2350Z
**Authority:** Andrew-direct flow ruling (verbatim, relayed by MSTR~Z 233212Z): *"Once CTO finished PRD and
issues to COO, COO may decompose on arrival and dispatch."* PRD issued by CTO~Z 233457Z.
**Completion oracle:** `docs/architecture/MDPF_CANONICAL_PLATINUM_DELIVERABLE_CONTRACT.md` @a3106d585
(CTO~Z handoff 234334Z) — *"the PRD is the WHY, this is the WHAT."* TO acceptance quotes §A/§B/§D cells
and §E rubric rows; **§B doubles as Guard 2's CLOSED FIELD-PATH LIST**; program completion = **R1–R14 all
PASS on ONE UNATTENDED SCHEDULED CYCLE** (ad-hoc runs are QA, never production evidence).
**A3/A4 sequencing (CTO~Z):** gold writes the canonical dated hyphenated grammar DIRECTLY; the 09:40
bridge becomes deletable as a CONSEQUENCE (R3, then R11 proof). Gold first, bridge second.
**Sequestered (Andrew-direct via CTO~Z 234938Z):** the `mdpf_revamp` name retirement — brief pocketed at
`docs/briefs/mdpf-revamp-name-retirement-POCKETED-20260806.md` @76d4ba532, NOT authorized, NOT scheduled;
A7's `mdpf_revamp` reference is DELIBERATE AND CURRENT.
**THIS DOCUMENT IS THE SINGLE LIVE DISPATCH AUTHORITY for the PRD's scope. Two generations of TOs are
never simultaneously live: every prior-generation TO is dispositioned in §3 below.**

---

## 1. The TO set (generation: MDPF_CANPLAT)

| TO | Seat | Status at issue | GO |
|---|---|---|---|
| `MDPF_CANPLAT.P1-1.canonical-gold-spine` | 0.4.0_DS_ClientPlatform~Z | pending | GO with dispatch |
| `MDPF_CANPLAT.P0-2R.vendor-early-clock-probes` | 0.7.0_AE_CloudOps~Z | pending | GO with dispatch — ⏰ window 08:05–08:40 ET 2026-08-07 |
| `MDPF_CANPLAT.P2-1.deployable-config-and-iam` | 0.7.0_AE_CloudOps~Z | pending | GO with dispatch (build+commit; TF apply via safe-apply per its own gates) |
| `MDPF_CANPLAT.P3-1.publisher-projection` | 0.7.0_AE_CloudOps~Z | **staged** | GO fires from COO~Z when BOTH: P2-1 config objects landed AND P1-1's canonical gold contract is emitting. NOT before. |
| `MDPF_CANPLAT.G2.regression-comparator-and-acceptance` | 3.0.0_SA_CVO~Z | pending | GO with dispatch |

**Wave logic.** P1-1 (gold canonicalization, atomic with the Cottonwood family) and P2-1 (config
deployability + IAM) run in parallel; G2 (the Guard-2 comparator + acceptance instrument) builds
immediately so the instrument exists BEFORE any gold diff lands; P0-2R is clocked (tomorrow morning's
vendor window); P3-1 deploys last, against an already-canonical gold (L-2).

**Deferred, deliberately NOT in this dispatch:**
- **09:40 bridge retirement**: a CONSEQUENCE of gold writing A4 directly (R3) — retires SECOND, on R11
  evidence (`bridge invocations = 0`), under a later COO GO to AE~Z. Never retired by DS.
- **EC2 chain teardown** (prior CANRTE W3 axis): follows only after the canonical path is verified
  end-to-end. Not authorized by this decomposition.
- **`mdpf_revamp` name retirement**: SEQUESTERED by Andrew (pocketed brief @76d4ba532). Not authorized,
  not scheduled; A7 stands.
- **`fee_scope` migration to declared data** (1→declared): PRD §6 — P2-1's config axis *considers* it;
  nothing populates `data/firm_registry.json` on this program's authority. P1-1 collapses 2→1 only.
- **Extras retirement** (`cottonwood/account-units.json`, `global/non-model-assets.json`): retire only
  AFTER fold verified — and the retirement act itself is a served-key deletion = Andrew's (NEVER#3).
- **Portal component re-points**: DT/portal lane, surfaced not started (standing frontend guard).

## 2. The four guards, and who holds the line on each

1. **§0 posture** (every seat): PRD §0 verbatim in every TO. A number that surprises you is not a finding.
2. **Guard 2 = FIVE requirements** (CVO~Z holds): per-JSON-path value identity under declared
   canonicalisation · exercised against a mutation, shown to FAIL and LOCALISE · baseline pinned to
   explicit VersionIds at a stamped instant · absent/null/zero three states · **CONTRACT §B as the
   CLOSED field-path list consumed as data** (supersedes the PRD §4-prose denominator per CTO~Z
   234334Z). A diff outside §B is a REGRESSION.
3. **Guard 3 = COVERAGE, never non-null** (DS~Z holds): honest-None is the derivation's own ternary
   (`build_cottonwood_mdpf_slice.py:853`, `:1131-1132`, `:782`); `else None`→`else 0` is a one-token
   edit that reads as hardening. Both-operand form (`:1131`) wins.
4. **Guard 4 = no deletion, no served-key moves, no semantic change** (COO~Z holds at dispatch; every
   TO's do_not restates it).

**Report-don't-chase channel (every TO):** one line to 2.0.0_SA_COO~Z, subject beginning `SURPRISE:`,
then continue the §2 work. COO triages; nobody chases.

## 3. Prior-generation disposition (MSTR~Z instruction #2, CTO~Z issuance §supersede-or-adopt)

Every MDPF_CANRTE TO of the 2026-08-05/06 generation, dispositioned explicitly. **No prior TO is live
dispatch.** Statuses flipped in the TO files themselves in this same commit.

| Prior TO | Prior status | Disposition |
|---|---|---|
| `MDPF_CANRTE.P0-1` (AE) | staged | **SUPERSEDED as dispatch; its evidence-freeze/rollback-baseline outputs (incl. per-key schema baseline @db5f37b11) ADOPTED as inputs** to G2 and P3-1. |
| `MDPF_CANRTE.P0-2` (AE) | pending | **ADOPTED INTO `MDPF_CANPLAT.P0-2R`** (content incorporated by pinned reference; egress now GRANTED). |
| `MDPF_CANRTE.P0-3` (AE) | pending | **ADOPTED INTO `MDPF_CANPLAT.P0-2R`** (same). |
| `MDPF_CANRTE.P0-4` (DS) | pending | **SUPERSEDED**; census results adopted as P1-1 input. Do not re-run. |
| `MDPF_CANRTE.P0-5` (AE) | staged | **SUPERSEDED**; deployed-plane census results adopted as input. |
| `MDPF_CANRTE.P0-6` (CVO) | complete | **CLOSED RECORD** (verified @49e236bff). No action. |
| `MDPF_CANRTE.P0-7` (AE) | pending | **SUPERSEDED as dispatch.** AE~Z reports its completion state in ONE LINE with the P0-2R ack; COO re-seats if the capture is still open. Do not execute it off the old GO. |
| `MDPF_CANRTE.P1-1` (DS) | staged | **SUPERSEDED BY `MDPF_CANPLAT.P1-1`**, which adopts its corrected body (@a6ae64326) with explicit deltas. |
| `MDPF_CANRTE.P2-1` (AE) | pending | **SUPERSEDED BY `MDPF_CANPLAT.P2-1`**, which adopts its body (@a6ae64326) with the fee_scope-axis delta. |
| `MDPF_CANRTE.P3-1` (AE) | staged | **SUPERSEDED BY `MDPF_CANPLAT.P3-1`**, which adopts its body (@a6ae64326; L-2-checked CLEAN by COO~Z this session). |
| `MDPF_CANRTE.A` / `W1` / `W1b` / `W2R` / `GRF` | complete | **CLOSED RECORD.** W2 `deprecated-as-shaped` stands. No action. |

**Why adoption-by-pinned-reference rather than retranscription:** the predecessor bodies already carry
the CTO-corrected guard forms (9c five requirements, 9d consolidation-only, 9e ternary-not-gate).
Retranscribing ~1,200 lines is exactly where a five-requirement guard gets compressed back to one
sentence. The pinned commit makes the adopted text immutable record; the deltas are stated per-TO.

## 4. Grounding run for this decomposition (COO compiler-tools mandate)

- `comp-blast pipeline:mdpf:gold:build_aggregate_aua_timeseries` — S3 radius: `platinum/mdpf/
  aggregate_aua_timeseries.json`, `gold/eclipse/{*}/model_portfolio_accounts.parquet`,
  `silver/eclipse/{*}/portfolios_full.parquet`, `silver/netassets_daily.parquet` (kuzu vintage 1.2h,
  Nessie HEAD current).
- `comp-blast opal-assets-mdpf-portal-publisher` — distinct lambda node confirmed.
- `comp-pipescript overlap` — rc=2 flagless refusal exercised, then graph-form names used;
  `build_cottonwood_mdpf_slice` is not a graph node on this device's vintage (recorded, not chased —
  the cross-tree coupling is already source-cited in the adopted P1-1 body).
- Predecessor TO statuses read from working tree at HEAD a6ae64326; PRD read at `git show 24d3eb2f8`.
