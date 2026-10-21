# DELL1 self-drive box -- ticks 223-224, 2026-10-21 ~06:18-06:49Z (hour floor; the firm-split mechanism ruled; Groups are the only product scope; the backfill rerun)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 06:49Z. Acked since tick 222: 9000, 9002, 9005, 9008, 9011, 9014.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. One act
  added for Andrew by ruling (below), carried in this log and the ruling record rather than the tool (the tool holds the box's
  rows; the ruling is its citation).

## Acts and rulings
- **The design fork answered** (CRO~FIDELITY 9002, record @81e3a18bf3): the G number is a reporting and service-desk context (alerts,
  statements), not account membership; the per-firm scope Wealthscape offers is account GROUPS; `accountList.json` rows carry
  per-account fields that might encode the firm.
- **RULED** @4c536cb554 (`deliverables/CTO_RULING_NFRA_FIDUPL_FIRM_SPLIT_MECHANISM_20261021.md`): the "split by G" premise is refuted by
  measurement (an L10 finding for the round-3 analysis and a PRD addendum; no cell changes mid-round); the split key is
  custodian-native, measured before chosen; the Orion/BD crosswalk is the COMPARISON only (Andrew's COTBOOKS word @7fb4f70e80);
  unattributed accounts land named under `alongside/` (FWD-9); Groups are the durable path; creating Groups is a vendor-configuration
  act under Andrew's name that no word of his names: LISTED FOR ANDREW.
- **Measure (3) closed** (P1 9005, offline from the HARs' full 2000-row page): no accountList field partitions the book (regRep 1,
  mslaCode 1, planName 2, registrationCode 24, fbsiShortName 1033). No native key exists.
- **The read-only wizard walk** (P1 9011, one sign-in, nothing saved, record @1db8536e59d): step 3 "Choose Filter" is a Groups
  multi-select (58 groups: 5 system, 53 client-family-named), a per-file No Filter, and a transaction date range; NO G filter; the
  catalog has no firm column; verify.json G associations empty. CRO 9014 (@0c819f2e54): the 53 are HOUSEHOLDS, not a firm partition
  (names are PII, box-only; P1 runs the deterministic token count on the box to confirm).
  - **Ruled:** after the backfill rerun, ONE one-off Custom export filtered to ONE existing client-family Group, account file only,
    no profile saved, to read the per-Group membership shape; nothing creates, renames or deletes a Group.
- **Backfill** (deliverable 2): run 1 at 06:01Z served 2026-10-20 (the landed day, skipped_existing) then TimeoutError before any
  earlier day (row D1-S14); FT-s-7 REPAIR 3 (120 s request timeout, one DAY line per trading day, a timeout as a named stop with its
  date) merged, 26th delivery @67b6b78bd23; FT-s-11 step 3B the rerun at 06:47Z (read this tick; outcome in the tick line and the
  next log).
- **AMGT_HARVST:** no change; co-7 stage 7 waits for its apply span.

## Scope state
- **NFRA_FIDUPL:** FT-s-11, FT-s-8, FU-s-11, FU-x-1 pending. 22 objects under `fidelity/alongside/bronze/` (6 data, 16 run records).
  Rules ENABLED (first fire 09:45Z). No firm prefix; no backfill earliest-date row yet. The stop condition's "split to firms" half is
  UNREACHABLE by the driver's own acts until Groups exist (Andrew's act) -- named once here, per Step 4.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to create them from the measured
  membership (ruling @4c536cb554; CLAUDE.md: a vendor use no word of his names).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated export profile, only if the wizard's date field cannot be automated on the backfill (CRO 8916).

## Compiler Tools
- `git show` of probe and walk records; `s3 cp` of run records (counts only).
- `grep -n` of the CRO's research record.
