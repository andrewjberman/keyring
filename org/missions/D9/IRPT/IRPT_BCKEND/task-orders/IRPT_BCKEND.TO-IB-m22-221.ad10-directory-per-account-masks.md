# TO IRPT_BCKEND.TO-IB-m22-221 -- AD-10: every directory entry carries each account's own mask

<to_id>IRPT_BCKEND.TO-IB-m22-221</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~75</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-221`
(`decompositions/IRPT_BCKEND_DECOMP_R22_M.md`) | **outcome_ref:** FWD-2 (the directory: picker + identity list) |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-221` -- brief item AD-10 (`docs/briefs/irpt-master-guidance-brief-20260928.md`): "each account shows its own
tail everywhere". The CRO measured the served picker showing three 49F accounts all as `****9079 / IRA` and five INF
accounts as `****3302 / JOINT` (CRO 102699, CTO 102702). Cause: a directory entry covers a client or relationship
with several accounts, but `_entry()` in `data/assets/scripts/gold/investor_reporting/directory_runner.py` (around
:458-477) mints ONE `masked_discriminator` from the entry's HEAD account row (`head = account_rows[0]`), so every
account under it reads the head's tail and type.

**Build:**
1. `DirectoryEntry` gains an ADDITIVE property `account_masks`: an array, one item per account in `ids.account_ids`
   and in the same order, each `{"account_id": <the same opaque id>, "masked_discriminator": <that account's own
   mask>}`. Edit `docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` (the schema is
   `additionalProperties: false`, so the property must be declared; keep it OUT of `required` so documents without it
   stay valid). Today's `masked_discriminator` stays exactly as it is (the head row) so current readers keep working.
2. `_entry()` builds `account_masks` from EACH account row with the existing `masked_discriminator(account_number,
   account_type)` function. `account_type` already carries the UIC-16 registration name at 49F (TO-IB-m21-213,
   `schwab_account_codes.registration_name(acct_regis)`, drained @1fe26443ff); INF and COT keep their sources'
   full type. A mask never carries more than the last 4 digits. If `directory_runner.py` is generated, regenerate it
   with its generator (name it) rather than hand-editing.
3. Tests: `data/assets/scripts/gold/investor_reporting/tests/test_directory_account_masks.py` -- an entry with two
   accounts of different numbers and types yields two different masks in `ids.account_ids` order; a one-account entry
   yields one; the head `masked_discriminator` is unchanged; every emitted entry validates against the edited schema.
4. Real local builds (no upload) for all three firms at the latest business date the sources hold. Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_AD10_ACCOUNT_MASKS_SUMMARY_20260929.json` as
   `{"firms": [{"firm": "49financial"|"inflection"|"cottonwood", "as_of", "entries", "accounts",
   "accounts_with_own_mask", "masks_with_more_than_4_digits", "multi_account_entries",
   "multi_account_entries_with_distinct_tails", "sample": [<up to 3 multi-account entries' account_masks, masked
   values only>]}]}`.
5. **Every reader (round-19 analysis section 2 -- this changes a served figure):** write the half
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_DIRECTORY_AD10_20260929.md`
   (`## The act`, `## Blast radius` with the local candidate diff, `Rollback per key`) and census in it EVERY reader
   of the directory entry: the portal account picker and identity list (the reader 2.0.0_SA_COO~D will point at
   `account_masks`), the portal and Lambda contract validators (the deployed handlers carry their own copy at
   `infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json`, which must gain the property before a
   document carrying it is served), directory search, exports, any cache -- each with the check that proves it on the
   served page at the re-mint. Name the release order: the handlers' contract copy first, then the directory bundle
   re-mint, then the portal reading the new field.

### ACCEPTANCE

<criterion id="IBM22-221-AC1" cell_refs="IB-mr-221"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_directory_account_masks.py -q -p no:cacheprovider</invocation><expect>a summary line with N passed and no failed or error</expect></criterion>
`IBM22-221-AC1` -- the built behaviour: one mask per account, in order, schema-valid.

<criterion id="IBM22-221-AC2" cell_refs="IB-mr-221"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_CHECKS/r22_ad10_masks.py</invocation><expect>AD10-MASKED followed by each firm's account count</expect></criterion>
`IBM22-221-AC2` -- real local builds at all three firms give every account its own mask and show distinct tails where an entry has several accounts.

<criterion id="IBM22-221-AC3" cell_refs="IB-mr-221"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_DIRECTORY_AD10_20260929.md</invocation><expect>HALF-READY NEVER_WIDEN_HALF_REQUEST_DIRECTORY_AD10_20260929.md</expect></criterion>
`IBM22-221-AC3` -- the half, with its all-readers census and release order, is written for the issuer to sign and send.

<expected_criteria>IBM22-221-AC1,IBM22-221-AC2,IBM22-221-AC3</expected_criteria>

Dry-run at the base 2026-09-29 10:3xZ: AC1 "no tests ran", AC2 NOT-MASKED (summary absent), AC3 NOT-READY -- FAIL as
expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no served write. The local builds READ the firm source buckets
  (read-only). `directory_runner.py` is a member of the directory bundle (commit-routed; 0.0.0_AB_MSTR skips it at
  push until its members are signed). The Lambda contract copy is NOT yours to edit (2.0.0_SA_COO~P's shared
  packaging); name it in the release order.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W75-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_AD10_ACCOUNT_MASKS_SUMMARY_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_DIRECTORY_AD10_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R22_M.md</decomp_doc> (round 22, workstream ~M), cell `IB-mr-221`.
<owned_cells>IB-mr-221</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM22-221-AC1, IBM22-221-AC2, IBM22-221-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~75/IRPT_BCKEND.TO-IB-m22-221.ad10-directory-per-account-masks.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM22-221-AC1,IBM22-221-AC2,IBM22-221-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the field and where it is built, the schema change, the per-firm summary counts, the
readers census and release order, the pytest lines, the half's path, commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the served move rides the directory bundle's next signed re-mint.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; the local builds use the reads prior cells used.
comp-adversary: RUN -- 1 function read (directory_runner.py _entry(), head-row mask at the masked_discriminator line) and 1 schema read (DirectoryEntry.schema.json: additionalProperties false, 9 required fields, masked_discriminator a string); BLIND: the portal readers of the directory entry were not traced at the cut (step 5 censuses them) and the per-firm multi-account counts are unmeasured (step 4 measures them).
lane: the <paths> block IS the grant; ~M owns the directory runner's gold side.
</preflight>

Source: CTO sweep-1 analysis (`ledger/ROUND_ANALYSIS.sweep1.md` @eaefb76322) section 4 item 3; CTO 102702 (CRO 102699).
