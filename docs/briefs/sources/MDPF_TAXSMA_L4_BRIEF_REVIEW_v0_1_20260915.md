# MDPF_TAXSMA v0.1 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15 ~08:05Z · request: `1.0.0_SA_CTO~A` messages 96967 and 96969 (duplicate).

**VERDICT: REFUSED, brief half.** The brief is carried with its content almost everywhere: all eight outcomes,
the boundaries, the measured prior art, and all but one of §VII's required closures. Two grounds remain:
- **R1:** the automatic effective-date path is a named status with no rule, which is the one kind of open decision
  brief §VII forbids handing to decomposition.
- **R2:** the coverage denominator is 17 against the brief's 18 headings.

Both fixes are small.

## Exact inputs and scope

- PRD: `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@48befbfcbfbdc78c360f9716dbffadf13c0f6cff`, v0.1,
  340 lines, 65,087 bytes. At review, HEAD and worktree both matched the pinned bytes.
- Brief: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454961bebb2a3d90a43522787e19ec9e4`,
  112 lines. It has **18 headings: 1 title, 9 level-2 and 8 level-3.** Its worktree matched the pin.
- Reviewed brief-half SHA-256: `03fadcd5469144c0d3ce8e00c82962a4024acb888863db122c1277c01375cbd6`, computed by
  `prd_signoff_lib.half_hashes`. It matches the notifier's `03fadcd54691`.
- Ratified-text half (ENDPOINT, CONTRACTS), identified but not signed here:
  `c4a17524e8f03a17d4649e927bef1799fd68f525a2d2c7580241e4e0e3830a3c`.
- Data contract: `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json@48befbfcbf`, 21,869 bytes. The `membership`,
  `status_axes`, `identity` and `operations` blocks were read in full.

## What is carried, with the checks behind it

| Brief | Where the PRD carries it |
|---|---|
| O1 (28–30) | Readiness, account number, funding, open status and strategy label never activate membership; accounts need not trade daily; every exclusion has a reason. §3.3 and A01, plus the contract's `membership.exclusion`. |
| O2 (32–34) | Full-ID reconciliation in both directions, and the contract's accepted and rejected identity forms (masked, last-four, nine-digit, scientific notation and others refused). The trading master 0804-4932 is never an alias for 0008335338 or 0008242234. Extra custodian candidates stay UNCONFIRMED. §3.4 and A02. |
| O3 (36–38) | New TRADED claims enter the denominator automatically; a missing BD identifier never removes a traded account; correction, deactivation and transfer keep their history. §3.3 and A03. **The effective-date half of O3 is R1.** |
| O4 (40–42) | b00 `canonical_valuation`, basis `net_mv_plus_cash`, cents kept, cash/short/margin treatment and the accrual PENDING-RULING limitation carried; no sales-estimate, gross, lot, leverage or quarterly substitute. §3.5 and A04. |
| O5 (44–46) | Separate status values for value, freshness, run result and denominator (unknown is not `0 of 0`). Expected arrival is concrete: `operations.freshness_basis` compares source valuation dates with the expected completed trading session under the canonical exchange calendar at the 13:30 UTC run, and a missed run reads STALE with `pending_since`. §3.5–3.8 and A05. |
| O6 (48–50) | Exactly-once firm and Global addition, an independent source basis, Client and other firms unchanged, and the dated full-ID overlap guard (`categories.overlap_rule`). §3.4, §3.6 and A06. |
| O7 (52–54) | Aggregate-only wire (`categories.wire_privacy`); protected evidence plane. §3.2, §3.7 and A07. |
| O8 (56–58) | Owner, receipts, named reader moments, replay without duplicates, recovery and reversal, all exercised on demand. §3.8, S15 and A08. |
| II–VI | Boundaries, the qualitative bar, measured prior art, dependency ownership and failure behavior, and the historical status are carried in §2, §3.1, §6, the CONTRACTS table and every surface row's bound. |
| VII (100–106) | Of the closures §VII requires, these are concrete: workbook schema and lifecycle; whole-ID validation; overlap and strategy conflicts; production read identity (S16, an explicit activation input for Andrew, not a design choice); valuation basis; the arrival calendar; unknown and partial propagation; independent proofs; delivery surfaces; recovery. **The effective-date rule is not: R1.** |

## R1 — SOURCE_PROVEN names a status with no rule

| Where | Pinned text |
|---|---|
| §3.3 at v0.1:161 | "For a valuation date, inclusion requires evidence of membership effective on that date: **source-proven activation evidence** or an authorized operator's dated disposition. `Inception Date` and `Last Trade Date` are evidence fields, not silently interchangeable with first strategy activation." |
| A03 at v0.1:231 | "New traded row … enters expected membership automatically, **acquires exact source/effective-date evidence** and contributes once." |
| Contract `status_axes.membership_date_status` | `["ATTESTED", "SOURCE_PROVEN", "UNVERIFIED"]` |
| Contract `membership` (whole block) | Five disposition kinds, including CONFIRM_EFFECTIVE_MEMBERSHIP with `effective_date` and `evidence_ref`, which gives ATTESTED. **No rule says which source, field or condition makes a date SOURCE_PROVEN.** |
| Brief §VII at 106 | "The PRD must close … effective-date rules … as concrete contracts. It must not hand open design decisions to decomposition." |
| Brief O3 at 38 | "… a daily category contribution without a hardcoded account list or a silent manual enrollment gap." |

So the only effective-date path the PRD fully specifies is an operator's attestation. The automatic path it names is
an enum value, and the worker at S03/S05 would have to decide what proves activation: a first dated Tax-strategy
label in 0833 ACC, first positions, `Inception Date`, or something else. That is an open design decision passed to
L5. A03 cannot be exercised as written without it.

**Fix, returned by pinned line.** Choose one:
- (a) Define SOURCE_PROVEN concretely in the contract's `membership` block and in §3.3 at v0.1:161: the exact
  source, field and condition that proves activation, and the date it assigns.
- (b) State that effective membership is ATTESTED-only in v1, drop SOURCE_PROVEN, and make A03 at v0.1:231 exercise
  the operator disposition as its activation step. That step is visible and dated, so it does not violate brief O3's
  "silent manual enrollment gap".

Either closes the brief's §VII obligation. The choice is the author's.

## R2 — the coverage denominator is 17 against the brief's 18

§8 at v0.1:314 reads "The pinned brief has **9 top-level headings** and **8 nested outcome headings**. All 17 are
enumerated here." But the brief at the pin has 18 headings. The level-1 title "Tax SMA: a complete, reconciled D8 asset
pipeline" and its preamble (lines 1–9: placement D8 / MDPF / laptop, L1 status, "not represented as a CRO-authored
brief") are neither enumerated nor dispositioned.

Its content is identity and placement context, and it is already carried in substance by the "Commission and
precedence" row (v0.1:318). But the denominator must match the brief. The sibling PRDs reviewed today each counted the
title or dispositioned it explicitly.

**Fix:** add a title/preamble row, or one sentence dispositioning it as identity context, and state 18 of 18 at
v0.1:314.

## Not grounds

- **S16, Andrew naming a person for the unattended delegated Graph read.** This is a sovereign activation input
  demanded by the vendor-egress and delegated-identity rules and the Gateway owner's disposition. It is not a
  specification decision, so it does not conflict with brief §VII's "not another general permission request". The
  design is fully fixed in §3.2 and §3.9.
- **Brief II's "No new provider egress".** The workbook read reuses the existing Microsoft Graph delegated path through
  the Gateway, behind S16's authorization. No new provider is introduced.

## Limits

This is requirements review only. No workbook read, reconciliation, valuation, publication or portal render was
exercised. The certified run and the CTO dispositions (96939, 96944, 96946, 96960) are cited as the PRD states them.
The ratified-text half and the data contract's approval are `3.0.0_SA_CVO`'s. The contract was read here only where
this half relies on it.

A v0.2 that changes only the lines named above, plus the contract's `membership` block if fix (a) is chosen, needs no
re-audit beyond them.

The delivered notices 96967 and 96969 were opened and READ-acked. This seat performs no push, deploy or cloud
mutation. Push state is measured and stated in the completion message to `1.0.0_SA_CTO~A`.
