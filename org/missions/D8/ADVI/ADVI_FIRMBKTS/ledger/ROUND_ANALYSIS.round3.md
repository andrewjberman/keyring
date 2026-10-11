# ADVI_FIRMBKTS -- ROUND 3, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~11:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3812, `surprise-channel/remediations/REMEDIATION_v4.md` @8f563cdd0b (the precondition met: ADJUDICATION_v4 D1-C-S17;
9 orders complete with valid proofs; 4 parked outside the round; 74 rows dismissed, 36 graduated, 15 of them this seat's). Issuer packet:
`deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md` @5c50521a0c. Rulings made during the round: `ROUND_ANALYSIS.round2.md` ADDENDA 1-7 and the
act-1 and act-2 CTO halves.

## 1. Graded

- **Act 1 (the advTenant router and guard): APPLIED and HOLDS live** (D1-C-S16; this seat's oracle read, Branch A). No served decision moved.
- **FB-f-12 (SMS delivery-status logging): APPLIED and HOLDS** (D1-C-S25). It already did its job: the dead SEV1 page path's reason is read
  (row D1-S20, "No origination identity available"). The next step is Andrew's call `dell1-20261011T113148Z-c290`.
- **The cutover window did NOT run, by ruling.** ADDENDUM 7 widened it to every generated reader of the routed bucket, so acts 2, 3, 4, 4b
  and 4c move to round 4. Built and merged DORMANT: the producer seam (A to A4), the two Lambda seams, the delta tool.
- **FWD-1: PARTIAL.** 184 of 209 agree; both readers are right on 182 of 207. **Independence is NOT MET for the second round running.** The
  readers' faces are still not built as ruled at round 2 (a worktree that holds ONLY the location list). That is round 4's item 3, as
  an order, not a note.
- **D1-C-S21: FB-f-8 completed with placeholder criteria.** The issuer amends its cut template (`<placeholders>` are refused at the
  cut by GATE viii). A process row for the issuer, no cell.

## 2. Rulings on this seat's rows

**The FAULT grain edges (W12-S2..S11).** Each is placed by one rule. The next table repair applies them and cites this section.
- **S2: an overlap-0 MERGE must name its destination table in the row.** A merge row with no destination is FAULT, with this ruling cited,
  until the repair writes the destination.
- **S3: rule (b) applies to UNPLACED classes only.** A round-1 placed row stays as placed (the copied-unchanged rule wins). No `kind` field
  is added to a placed row.
- **S5: state families are `<tier>_complete`** (`bronze_complete`, `silver_complete`, `gold_complete`), at `address()` output under the
  owning firm or vendor. A builder refusal is a registry row (CLAUDE.md 30).
- **S6: a QA-named feed is QA only if its WRITER is a QA tool**, read from the writer, not the name. A verified QA output gets the RB rule
  (no destination). Otherwise it is production bronze and goes `bronze/**` HOME. The table records which, with the writer named.
- **S7: `*_SKIP.json` (1,142 in the orion-api partitions) is a marker by literal tail**, under ADDENDUM 1's `marker_match`, and goes to
  the same `<tier>_complete` family as a `skip` kind. A skip record is state, not data.
- **S8 and S11: colliding marker keys are split by WRITER.** The state key carries the writing class as a segment
  (`<tier>_complete/<class>/<date>`), so the two eclipse bronze classes (66 keys) and the ten forward-fill `_complete/` groups stop
  colliding. A collision is then a FAULT only if one writer collides with itself.
- **S9: the table repair's sum check compares against the LIVE listing**, per ADDENDUM 1 (e). Check arm S2, which reads only the field, is
  amended to list the class live and print both numbers.
- **S10: a class-grain row has no partition token.** Its address is the class prefix (`address()` with no partition). A class that needs
  partitions is re-gridded, per date.

**The three tool rows (W16-S1, W16-S3, W22-S3)** belong to the tools' owners: `comp-pipescript` (it under-reports D_04's writes and
resolves 1 of 26 E-series ids) and `opal_naming.py targets` (its lambda-plane consumer classification). Each goes to its owner's channel
as one row. Here, the census instruments of record are the AST read census and the generator's target list (ADDENDUM 7), not
`comp-pipescript`.

**D1-S14 (E_01 and E_24): confirmed.**
- E_01 writes no served key under the module's own rule; it last wrote 2026-04-07.
- E_24 needs no carrier. Round 4 adds its explicit-mode refusal, per act 2's CTO half.

**S12 (the WAF ACL churn): reconciled in Terraform, round 4.** `lifecycle { ignore_changes }` on the three managed groups' `version` (or
an explicit `null`), so a `portal-auth` plan reads no ACL change. Until then, every apply in that root carries it as the named rider
ruled in act 1's ADDENDUM 1.

**D1-S17 (ARMED, the stale ownership map at the new home): stays ARMED**, and is disarmed at round 4's act 4 (ADDENDUM 7). Every
protected or IRPT pair names it in the meantime. The laptop CTO has made that binding on its side.

**D1-S19 (the pending `eclipse_jwt_initial` secret version in inf-pipeline)** is not this project's. It goes to inf-pipeline's owner as a
row. No act here applies it.

## 3. ENRICHMENT LIST (round 4, ONE issuance by `2.0.0_SA_COO~B1`)

1. **The window's readers, built DORMANT, each with its pair** (ADDENDUM 7). The list comes from `opal_naming.py targets` for 49 Financial's
   routed bucket:
   - the router and guard;
   - `auth-validator-edge` (the laptop identity);
   - the IRPT consumers;
   - the three gold scripts;
   - the two Lambdas (4b, 4c).
   The ownership class rejoins the move. Also:
   - the producers' role grant (D1-S18), its own pair;
   - the 97 dynamic-key files classed before act 4.
   **The window opens only when every one is merged and signed:** act 2, act 3's delta copy (ownership map included), then act 4 as the
   value flip with every regenerated target deployed in the same act, then 4b and 4c. D1-S17 disarms there.
2. **The table repair under section 2's edge rulings**, printing FAULT before and after, with an owner on every remaining class.
3. **FWD-1's independence, BY CONSTRUCTION, as an order.** Two readers, each in a worktree whose sparse checkout holds ONLY the location
   list. The CVO lists each worktree before grading.
4. **The WAF ACL reconcile (S12)**, one small infra cell in `portal-auth`, with a plan that reads no ACL change.
5. **E_24's explicit-mode refusal**, one small cell.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- FWD-7 and FWD-8, the prohibited key and B2 (DEC-13).
- The SEV1 page path's test SMS (call `dell1-20261011T113148Z-c290`). It is not this project's outcome, but its rows live here.

-- 1.0.0_SA_CTO~DELL1
