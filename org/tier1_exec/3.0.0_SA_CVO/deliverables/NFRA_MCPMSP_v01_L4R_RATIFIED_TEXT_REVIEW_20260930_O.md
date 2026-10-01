# NFRA_MCPMSP PRD v0.1 -- L4-R ratified-text review (3.0.0_SA_CVO~O, 2026-09-30 ~06:0xZ)

**Subject:** `org/missions/D6/NFRA/NFRA_MCPMSP/prd/NFRA_MCPMSP_PRD.md` @b90b97652f, ratified-text half, half_hash
`50a08086d120bdcd3e4bc465877959c4794e057ea6527ada2055102c557b7570` (recomputed here with `prd_signoff_lib.half_hashes`,
equal to the notifier's). Delivery: 1.0.0_SA_CTO~O msgs 26929 / 26930.
**Rule:** spine L4-R (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:191-194`).

**VERDICT: SIGN.** Two non-blocking notes for L5 (N1, N2) and one reading note (N3).

## 1. ENDPOINT verbatim against the ratified pin

- Pin: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_MCPMSP_20260930.md` @64617f8afa (resolves; the
  file is unchanged between the pin and HEAD).
- Method: each statement, DONE WHEN and ACCEPT record was joined across its wrapped lines, whitespace normalised, and
  exact-matched against the pin's records with SOURCE lines excluded.
- Result: **33 of 33 records verbatim** (11 outcomes x 3); 0 differ; 33 records on each side. The header's
  `endpoint_outcomes` lists the same FWD-1..FWD-11.
- Confirmation: Andrew's "yes aggreed for all of these" is recorded in
  `ANDREW_DIRECT_20260930_05xxZ_NFRA_MCPMSP_ENDPOINT_CONFIRMED.md` @7c7848d589, and binds the text at the same pin.
- Annotation check: the section holds the outcome block and one line citing the pin plus the confirmation. That is the
  pin the spine directs this review to read, and the same shape I signed in NFRA_OPALAI and NFRA_MCPORTAL. No seat serial
  appears as an attribution; the only one is inside a path. Not graded as the annotation the spine bars.
- Operative constraints: the pin's only non-outcome operative content is its five open items, which it carried to L4
  and L5. Four are settled in CONTRACTS and A1 (C3 pilot scope, C4 approver, C4 log home and fields, A1 data surface).
  The fifth, the audit allowlist, is carried to L5 in the Canonical handoff. None is dropped.

## 2. CONTRACTS against Andrew's record

The record is `org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20260930_0315Z_...ALLOWLIST.md`, unchanged
since @6cc12c2e06.

| contract | record | reading |
|---|---|---|
| C1 one gateway | s.7 | agrees ("probably" is carried as a direction) |
| C2 registry, no lookup | s.6, s.10 card 3, card 6 | agrees; cited code `asker_scope.py:62-65` read at HEAD, verbatim |
| C3 domain AND tenant, agent AND gateway | s.2, s.6 | domains verbatim; both enforcement points. Guest-form ruling fills s.4's open point (N3) |
| C4 refusals logged | s.5, s.9 | agrees; the text-not-stored choice fills a point s.5 left open, and FWD-3's ACCEPT asks only for who sent it and when |
| C5 per-firm role | s.8, card 5 | agrees; buckets as `05_IDENTITY_SPINE.md:67-68` at HEAD |
| C6 grants A then C | s.9 | agrees; `POLICY#<tid>#<oid>` takes any tid (`access_state.py:121-125`), and the admin tool has no Opal-only tid check |
| C7 per-firm keys | card 4 | agrees; "clear structure" is carried as builder SECRET-grammar output |
| C8 harness | card 2 | agrees |
| C9 / C10 record, page, sample | card 2, card 6 | agrees; no send (the alert moratorium) |
| C11 go-live on Andrew's word | card 6 | agrees |
| C12 ledger | CLAUDE.md | agrees |

**Counterpart PRDs.**
- NFRA_MCPORTAL: C2 is Andrew-only on every page and write, which is what C4 relies on. Its C4 grant writer is the one
  writer of the `POLICY#` partition, which is what C6 relies on. No contradiction.
- NFRA_OPALAI: the scoping modules are shared (C1), and the cross-organization chat rule (`asker_scope.py:70-73`) is
  why FWD-1 is one-to-one. No contradiction.

## 3. Notes (non-blocking; for the L5 decomposition)

- **N1 -- the tenant-registry row needs a named writer.** C2 and C4 create the row by approving a refusal-log entry
  "from NFRA_MCPORTAL's Entitlements tab". MCPORTAL C4 gives its writer exactly one write, the `POLICY#` partition.
  Either the row lives in a partition that writer already covers, or MCPORTAL takes an addendum that widens its writer
  by exactly this record. Round 1 does not reach it: onboarding is FWD-4, an enrichment round.
- **N2 -- the approval queue is new mcportal-repo surface.** "Used for pilot grants and never rebuilt" is not
  contradicted by adding a queue view, but that view writes to MCPORTAL's repo. The sibling-sequencing line covers
  gateway paths only; mcportal paths need the same rule when FWD-4 is cut.
- **N3 -- C3 is tighter than "check tenant ID if its surfaced".** C3 refuses a sender with no registered tenant. That
  is not a widening. No firm scope can be chosen without a tenant ID (`asker_scope.py:151-167` refuses a sender that
  carries no tid or oid), so a message without one is refused under either reading.

-- 3.0.0_SA_CVO~O
