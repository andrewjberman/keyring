---
# Operating-cycle record — one per /govern cycle. Copy to CY-NNNN.md (monotonic).
# The Article XII attestation: records which version of the law was read.
cycle_id: CY-NNNN
previous_cycle: CY-NNNN                  # the prior cycle — null only for the first
started: 2026-00-00T00:00:00Z
ended: 2026-00-00T00:00:00Z
trigger: scheduled                        # scheduled | fresh_wake | andrew_directive
constitution_read: v0.0 <sha>
stakes_matrix_read: v0.0 <sha>
directives_read: v0.0 <sha>
ledger_entries: [LD-NNNN]                 # decisions produced this cycle; [] if none
next_review_due: CY-NNNN                  # when the next drift review is due
---

# CY-NNNN — operating cycle <date>

## Step 0 — attestation
Read in full: CONSTITUTION <ver/hash>, STAKES_MATRIX <ver/hash>, DIRECTIVES <ver/hash>.
Active directives in force: D-NNN, ...

## Scan
<Fabric state vs each active directive — progressing / stalled / drifted / gap.>

## Originated / adjusted
<What MSTR decided this cycle — LD-NNNN refs, one line each.>

## Delegations
<!-- Every item handed to Tier 1. A delegation is a claim until a receipt confirms it. -->
| to_agent | charter_ref | ledger_ref | expected_receipt | status |
|---|---|---|---|---|
| <serial> | <path/ref> | LD-NNNN | <what acceptance looks like> | sent / accepted / modified / rejected |

## Delegation receipts
<Evidence that Tier 1 accepted, modified, or rejected each delegation — not MSTR's
assertion that it "delegated", but the downstream agent's actual response.>

## Gated items surfaced
<S3 / S4 escalations routed to Andrew or CVO this cycle — LD refs + routing.>

## Halts / bypasses
<Any Art. X halt or Art. VI bypass_exception this cycle; else "none".>

## Drift review
<If this cycle ran the mandate-drift review, the per-directive output:
 Directive / current interpretation / actions taken under it / accreted
 assumptions / where interpretation expanded / what Andrew has not explicitly
 approved / recommended keep-clarify-retire. Else: "not this cycle".>

## Carry to next cycle
<Open threads for CY-(NNNN+1).>
