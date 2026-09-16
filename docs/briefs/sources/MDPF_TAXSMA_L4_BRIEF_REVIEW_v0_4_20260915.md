# MDPF_TAXSMA v0.4 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15, after 18:48Z · request: `1.0.0_SA_CTO~A` message 97205.

**VERDICT: SIGNED, brief half.** v0.4 makes two changes in this half. Each follows Andrew's two records of the day,
read no wider and no narrower:
- the existing Traded column is the membership key, and the manual first-activation step is retired;
- `opalbloomberg@opalinvest.com` is the named identity.

The choices Andrew left to the PRD owner are made inside his word. Dating is FIRST_OBSERVED_UTC. There is no custodian
veto on the live count. The brief's content is kept: a funded-but-untraded account stays excluded, and a traded
account missing at the custodian stays visible and blocks a complete total. The S19 coverage gap flagged at v0.3 is
closed. One note below, on the date basis, is not a ground.

## Exact inputs and scope

- PRD: `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@d317a65ec7dc9240620f33733eacbf16211c4268`, v0.4,
  373 lines, 81,858 characters, in CLOUD.
- Brief: `…/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454` (18 headings).
- Reviewed brief-half SHA-256: `c2ea15c6002f176ceb0b3997c7b854b2e01a71f6c5d1d72002e88497214b2821`, computed by
  `prd_signoff_lib.half_hashes` at the pin. It matches the notifier's `c2ea15c6002f`.
- Ratified-text half: `da428d318d04535960b84890bc914cecdf4740b135a0ec8764e137071485d44f`, changed and owed by
  `3.0.0_SA_CVO`. **The new "Traded membership and named-identity addendum" (v0.4:126–132) sits under `## CONTRACTS`,
  so it is in that half and is not graded here.** Its content reappears in §3.3 and §3.9, which are graded.
- Andrew-direct records, read in full:
  - `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_183xZ_TAXSMA_ACCESS_BELIEVED_AND_TRADED_COLUMN_IS_MEMBERSHIP_KEY.md@1729cef85e`
    ("We dont need a human we use a key ... "Traded" signifies that the account is live, thats what we use to count an
    active account");
  - `…/ANDREW_DIRECT_20260915_180xZ_TAXSMA_WORKBOOK_IDENTITY_OPALBLOOMBERG_AND_ACTIVE_FIELD_MEMBERSHIP.md@f95470f384`
    (the identity half stands; the "active" field half is superseded).
- Supporting: `prd/TRADED_FIELD_ADDENDUM_97192.md` and `prd/IDENTITY_ACCESS_PROOF_97190.json` at the pin. Data contract
  v0.4.0, compared as parsed JSON with v0.3.0: 19 keys added, 18 changed, 0 removed. It was read only where this half
  relies on it.
- Prior review: `docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_3_20260915.md@10894fdad1` (SIGNED v0.3, stamp
  `1db20a3624`).

## What changed in this half, v0.3 (`61748ba2e0`) to v0.4

§3.3 (v0.4:181–191), §3.9 (:243–251), A01/A03/A05/A07 (:259, :261, :263, :265), the §7 preamble (:317) and S16 row
(:336), coverage rows I.O3/I.O5/I.O8 (:355, :357, :360), and §9 (:371–373).

| Check | Result |
|---|---|
| Traded is the key (Andrew 1729cef85e) | §3.3 (:183, :185): "YES is TRADED_CLAIM independent of Ready and reconciliation results"; "Traded=YES alone asserts current live membership". Ready, funding, custodian status, strategy labels and BD enrollment "neither activate nor veto". This is his sentence, and it keys membership on Traded rather than Ready. |
| No human step (Andrew 1729cef85e) | S03 emits OBSERVE_TRADED and OBSERVE_INACTIVE from complete Silver, with a service actor (:189). `CONFIRM_EFFECTIVE_MEMBERSHIP` is retired as a current command, and old records stay evidence only. Identity, transfer and strategy corrections keep a named actor, but "cannot invent a Traded state or backdate the source observation". |
| The two calls Andrew left open (his record, "what stays open") | **Date:** FIRST_OBSERVED_UTC, stated as the PRD owner's choice. It is "a first-known business state, not a historical first-trade claim", and earlier history stays TRADED_HISTORY_UNVERIFIED, never zero. **Safeguard:** a Traded account missing at Schwab keeps its live count, but its value is unresolved and the complete total is withheld (:185; A01 :259). Both are within his word. Neither makes Traded less than the count key, and neither lets a missing account disappear. |
| Brief O1 (:30) | "The workbook's explicit trading status is the starting business evidence"; readiness, account number and funding do not activate. Kept: Traded=NO stays excluded even when funded, and a prospect stays a prospect. |
| Brief O3 (:38) | "An authorized business-status change leads to ... a daily category contribution without ... a silent manual enrollment gap. Changes, corrections, deactivations and transfers preserve their effective dates and history." A workbook Traded flip is that authorized change. v0.4 carries O3 more directly than v0.3's attestation did: append-only events, explicit NO closure, reactivation intervals, and removal or rekey kept unresolved rather than treated as a deactivation. |
| Brief III (:70) and VII (:104) | "A funded-but-not-traded case stays excluded. A genuinely traded account missing from the source remains visible"; and Traded rows are "business claims, not independent confirmation" of custodian presence. Kept by separating the source-dated `business_active_accounts` from the valuation-dated expected and covered counts (:185). The page labels each with its own date, "cannot present one as the other". |
| Brief II (:66) | A new account at Schwab does not declare a trade. A02 is unchanged, and custodian candidates stay outside live membership. |
| Brief VII (:106), what the PRD must close | The effective-date rule and the production read identity are both now closed: FIRST_OBSERVED_UTC, and `opalbloomberg@opalinvest.com` (§3.9). |
| The identity (Andrew f95470f384; 1729cef85e item 1) | §3.9 names the account and keeps exactly seven projected fields. There is no new column, no maintainer request, and no new probe or widening. Access is "believed but UNMEASURED", which is his belief, not a measurement. The pre-Graph guard refusal is kept distinct from a SharePoint result, and the first controlled read at TX-r-3 is where access is measured. "The Bloomberg terminal credential is not a delegated Entra token." All faithful. |
| Proof by an act (Rule 27) | A01 deletes the Schwab record while Traded stays Yes. A03 exercises first-observed opening, NO closure, reactivation, same-day order, replay, out-of-order refusal and removal. A05 adds a pre-history date and an invalid Traded value. A07 separates guard denial from SharePoint failure. Each is a controlled fixture; the one live act is the TX-r-3 read. |
| v0.3 note: S19 missing from coverage | Closed. I.O3 (:355), I.O5 (:357) and I.O8 (:360) now list S19, and I.O5 and I.O8 cite §3.2 and §3.2a. |
| Heading denominator | 18 of 18 at the brief pin. Unchanged. |

**One stated consequence, recorded rather than contested.** An account that first appears directly as Traded=Yes,
with no retained earlier NO, leaves the prior session TRADED_HISTORY_UNVERIFIED. So that session's complete dated count
is null, never zero (:187, "this includes a newly discovered YES account when the available valuation is the prior
session"). The usual lifecycle, where a numbered row is Traded=No before it flips, avoids that through retained NO
history, and A03 contrasts the two. This is conservative and consistent with brief O5.

## Note, non-blocking: which calendar the effective date is compared on

`effective_date = date(source_observed_at)` is a UTC calendar date (§3.3 :189; contract
`membership.automatic_history_fields`). `valuation_date` is an exchange session date, and the brief's O5 names the
exchange calendar. A read after 20:00 ET (EDT) carries the next UTC date. So a YES observed that evening opens one
session later than its ET date, which is conservative: the earlier session reads unverified. An evening NO closes one
session later, so the account stays in that session's value. At the next bump, state the comparison: either observations
are dated by the exchange session, or the UTC choice is kept with this consequence named. Not a ground, because every
outcome is visible and none counts an account as live before its first observation.

## Limits

This is requirements acceptance only. Nothing was exercised: no S03 event, no count, no Gateway read. The 97190 probe
is relayed, not re-measured. The ENDPOINT byte-identity claim, the CONTRACTS rows and addendum, and the data contract's
ratified meaning are `3.0.0_SA_CVO`'s. The workbook access prerequisite stays UNMEASURED by Andrew's choice.

Message 97205 was opened and READ-acked. This seat performs no push, deploy or cloud mutation. Push state is measured
and stated in the completion message to `1.0.0_SA_CTO~A`.
