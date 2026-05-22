---
# Operating-cycle record -- one per /govern cycle. Copy to CY-NNNN.md (monotonic).
# The Article XII attestation: records which version of the law was read.
cycle_id: CY-NNNN
previous_cycle: CY-NNNN                  # the prior cycle -- null only for the first
started: 2026-00-00T00:00:00Z
ended: 2026-00-00T00:00:00Z
trigger: scheduled                        # scheduled | fresh_wake | andrew_directive
status: running                           # running | complete | failed | halted
failure_reason: null                       # set if status: failed | halted
recovery_required: false                    # true => the next /govern must recover before originating
constitution_read: v0.0 <sha>
stakes_matrix_read: v0.0 <sha>
directives_read: v0.0 <sha>
ledger_entries: [LD-NNNN]                 # decisions produced this cycle; [] if none
bounds_status: within                      # within | bound-hit  (see Cycle bounds section)
next_review_due: CY-NNNN                  # when the next /mstr_review is due
---

# CY-NNNN -- operating cycle <date>

## Step 0 -- recovery check
<First action of every cycle: was the previous cycle's status `complete`? If it
was `running`/`failed`, run recovery -- reconcile the partial state -- BEFORE
originating anything new. State the result here.>

## Step 0 -- attestation
Read in full: CONSTITUTION <ver/hash>, STAKES_MATRIX <ver/hash>, DIRECTIVES <ver/hash>.
Active directives in force (ignition-validated): D-NNN, ...

## Scan
<!-- Source-of-truth precedence (highest first): Constitution/Stakes Matrix/
     Directives > Andrew messages/halts > ratifications > ledger/cycle records >
     git state > broker state > telemetry > agent self-reports. Self-reports are
     LOWEST confidence unless artifact-backed (Constitution Art. VIII). -->
| directive | status | evidence (source : confidence) | uncertainty | needs_review |
|---|---|---|---|---|
| D-NNN | progressing / stalled / drifted / gap / blocked | <source : high/med/low> | <what is unknown> | yes/no |

## Originated / adjusted
<What MSTR decided this cycle -- LD-NNNN refs, one line each.>

## Delegations
<!-- A delegation is a claim until a receipt confirms it. -->
| to_agent | charter_ref | ledger_ref | expected_receipt | receipt_status |
|---|---|---|---|---|
| <serial> | <path/ref> | LD-NNNN | <what acceptance looks like> | drafted / sent / accepted / rejected / modified / expired |

## Delegation receipts
<The downstream agent's actual response -- accepted / modified / rejected / (no
receipt yet). Not MSTR's assertion that it "delegated". Tier 1 may push back on
operational grounds; record that here.>

## Gated items surfaced
<S3 / S4 escalations routed to Andrew or CVO this cycle -- LD refs + routing.>

## Halts / bypasses
<Any Art. X halt or Art. VI bypass_exception this cycle; else "none".>

## Cycle bounds
<Counts vs the Stakes Matrix ceilings: new ledger entries N/5, delegations N/3,
S2 actions N/2. Cycles since last review N/25, hours since last review N/24.
If any hard bound was hit: state which, and that the cycle stopped at it.>

## Drift review
<If a /mstr_review ran this cycle, reference RV-NNNN. Else: "not this cycle;
next due <CY/date>".>

## Carry to next cycle
<Open threads for the next cycle. Set recovery_required above if this cycle did
not reach status: complete.>
