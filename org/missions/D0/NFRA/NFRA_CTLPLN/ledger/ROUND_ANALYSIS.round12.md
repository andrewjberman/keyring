# NFRA_CTLPLN -- ROUND-12 ANALYSIS (1.0.0_SA_CTO, 2026-10-13 ~21:4xZ)

**On:**
- the CVO's L10 slug `surprise-channel/remediations/REMEDIATION_v6.md` @639b1aead6 (watermark 21:31Z; ADJUDICATION_v15; CTab3-AC2
  PASS; round-close-check MAY-CLOSE 3/3; seven graduated rows, three ARMED);
- the issuer's `deliverables/2.0.0_SA_COO~C/ROUND12_INPUTS_FOR_ROUND_ANALYSIS.md` @3474b257d1 (33 of 33 orders complete).

**PRD:** v0.30, unchanged. **Next:** round 13, cut by `2.0.0_SA_COO~C` in ONE issuance on section 3.

## 1. What round 12 moved

The round served Andrew's day-of words on this project:
- the Dell agent users joined the admin group with four Denies kept. CT-ab-2 was applied under pair 6 and read back by both Dell
  CTOs;
- the data-proxy fence went back to tier-internal only (CT-aa-6, pair 5, under ~U7's ledger);
- the S9112 log purge (8,513 streams; census 0/0/0/0);
- the SSH tools;
- the seat-boundary and cross-box gate fixes;
- box lists read from the register;
- the naming gate's test folders.

The laptop CloudOps lanes `~ANL` and `~FBL` stand down on the Dell read-backs (Andrew ~13:1xZ).

**Grade reads owed to the CVO this round** (named so the CVO can grade them; not graded here):
- **FWD-6's held arm.** Today a client-facing portal release waited for Andrew's word: his smoke and "everything that has come
  in", ~18:5xZ. Then the DT promoted `63c4f9e3` (CI success, tag `portal-v2.1.213`). The routine arm runs at every box-sync. Both
  arms now have a real read.
- **FWD-10.** A Dell now deploys its own changed work under its own identity (CT-ab-2). The DELTA=0 caveat of the 10-13 re-grade
  can be re-read.

## 2. Rulings owed to this seat

**`W79-S1` (the D2-S32 ruling vs kept case 943): RULED, both are reconciled.** The ruling's intent stands: the OPEN-CALL arm never
matches a bare token in a call's free text (subject or context), because free text names projects loosely.

A call's structured `project` field is not free text. It is the row's own declared project. So the arm matches:
- (a) the call's `project` field against the deploy's project;
- (b) a root path or the `roots` field.

Case 943 changes so that its project code rides in the `project` field, not the subject. Done when the ruling text, the matcher
and case 943 agree at HEAD. This goes in the batch cell.

**`S9122` (the signing-key exposure):** call `e846` is RULED and closed, accepting the bounded expiry
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md`). The remediation's "or" branch is
met. The row's disarm path is that ruling's condition: a rotation is cut only on an outside reader. Otherwise it lapses
2026-11-10T03:08:59Z. The CVO records it.

**Section C (`simulate_policy.py`, 23 references to removed Denies): RETIRE it as a gate.** Each pair's own POST reads are the
authority: a live `simulate-principal-policy` against the applied policy, as CT-ab-2's POST-2 and POST-3 did. A decision-table
simulator of a policy that now grants admin less four Denies is a second, drifting copy. The batch cell deletes its gate use and
keeps it as a fixture reader only if a test still needs it.

**`W77-S3` (three IAM policy descriptions name removed Denies): no standalone apply.** A description change forces replacement of
a live policy. The wording rides the next needed apply of that root and is not cut alone.

**`S9117` (stays ARMED; the CVO's note):** the stated remedy was "stop at the descendant", but W78-S2 built a whole-tree refusal.
Round 13 cuts the descendant stop so the row can disarm on its own remedy. The whole-tree refusal stays as the floor.

## 3. ENRICHMENT LIST for round 13 (thread-breaking first; build cells carry at most three mechanical criteria)

1. **FWD-11, then FWD-9: one deliberate dell1 outage each** (v0.30; Andrew "Yes sure"; at most 15 minutes, dell1, its manager
   restarting on the new identity). Unblocked by CT-ab-2.
2. **FWD-27 read-back on every box.** Andrew turned password login off himself (~17:4xZ, "I already did this"). Each box is read:
   - key SSH answers;
   - password login is refused, with `CT-ab-7`'s grading fix;
   - muse's key on dell2, which COMM_ASSIST FWD-6 needs.

   The laptop local account is DEFERRED on his word ("another time"), so the laptop arm stays GATED with that citation.
3. **S9120: the detached headless spawn** on dell2, after `0.0.0_AB_MSTR~DELL2`'s parent-process read names a transient parent.
   **S9119:** the broker heartbeat writer, named by `0.0.0_AB_MSTR`'s one read. These are seat reads first, cells only on what
   they name.
4. **The fence checker re-baseline** (`ADVI_FIRMBKTS-D1-S43`, reasons 1, 3, 4); reason 2 cleared with CT-ab-2.
5. **S9117's descendant stop** (section 2).
6. **ONE batch repair cell** (worker-light):
   - `S9121`: crossbox merge keeps a null `bus_message_id`, and a refusal writes nothing;
   - `W84-S1`: the `spawn-agent.ps1:108` pattern;
   - `W81-S1` leftovers: the three schema literals, the HELD dict entry and the "read by AST" wording;
   - `W79-S1` per section 2;
   - `W79-S2`: the crossbox suite at 50/50 independent of origin state;
   - `W85-S2`: `--check` defaults to offline;
   - `W85-S3`: the census re-saved at 238;
   - retiring `simulate_policy.py` as a gate (section 2).
7. **Process (section D):** a worker whose order file is outside its `<paths>` cannot flip the order's status. RULED: the issuer
   flips after its own re-run, as this round did; that is the rule, not a defect. The cut names it in each order's worker face so
   no worker reports it again.

**Carried with their reasons, not cut:**
- the package route on a lane that needs a package (FWD-15, 18, 19);
- the FWD-4, 7 and 8 reads;
- the FWD-23 and 25 seat acts.

## 4. On Andrew's ~14:0xZ question (why CTLPLN work had "drawn to a close")

Round 12 is the answer in practice. The stall was a scope one: 28 outcomes, most needing a seat act or Andrew's word, and no
single live journey being driven. Today the project was narrowed:
- DEVPLN and COMM_ASSIST split off;
- FWD-9 and FWD-13 resolved;
- the round was cut on Andrew's day-of asks: the Dell permissions, the tailnet, the fence.

All 33 orders closed in one day. The written stall analysis he asked for is still owed by this seat. It will be grounded on this
round's cycle time and rows, not on a status word.
