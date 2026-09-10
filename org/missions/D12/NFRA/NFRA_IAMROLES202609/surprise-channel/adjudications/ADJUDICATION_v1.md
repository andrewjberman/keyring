# NFRA_IAMROLES202609 -- surprise channel, ADJUDICATION v1 (round 1, site Z)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO~Z`, and only the CVO. Row ids carry the site-z infix: `NFRA_IAMROLES202609-Z-C-S<k>`.

**L8 IS THIS SEAT'S LIMB AND ITS ENGAGEMENT WITH THIS PROJECT BEGINS HERE** -- the spine's section 1 reads
*"L8 -- Compilation. Owner: `3.0.0_SA_CVO`, WHOSE ENGAGEMENT WITH THE PROJECT BEGINS HERE"*, and rule 27 was
corrected to match at `f5355fcfc4`. This document opens with the compile, verified on this seat's own
instruments; no L8 packet had been sent when it was written, and none is required for the limb to start.

---

## C-S1 -- the L8 COMPILE: L7 is terminal, and TWO DENOMINATORS ARE WRONG BEFORE ANYONE QUOTES THEM

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T11:15Z",
    "one_line": "L8 COMPILE, round 1. L7 IS TERMINAL -- 9 of 9 task orders, read UNSCOPED from their own <status> fields. The L9 set is 18 items, ALL UNDISPOSITIONED. ⛔ AND TWO DENOMINATORS A LATER READER WOULD OTHERWISE QUOTE ARE WRONG: there are ELEVEN proof-instance FILES for NINE orders, because TWO orders each carry a BYTE-IDENTICAL DUPLICATE -- one filename with the descriptive suffix, one without -- and a judgment census over the files returns ELEVEN criteria where only NINE are distinct. The duplicates are the PHYSICAL RESIDUE of the filename defect this channel reports FIVE separate times.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE -- a compile row. It adjudicates no item and moves no hazard; the 18 items are dispositioned in the rows that follow it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 TERMINAL, MEASURED UNSCOPED: all 9 files under task-orders/ parsed for their own `<status>` element -- 9 of 9 terminal, 0 NON-TERMINAL. Read from the files rather than from a completion report, because ledger/ is EMPTY at this write: this project has NO COMPLETION_REPORT at any round, which is the same missing-record condition 1.0.0_SA_CTO~Z named as blocking NFRA_OPSEC202609's close.",
        "THE L9 SET: 18 investigation items, ALL 18 UNDISPOSITIONED, 16 ARMED and 2 INERT, every one class OBSERVATION. Sourced from the INDEX via `_latest_dispositions` imported and called; 1 channel file, 0 malformed blocks. CONTROL: the same call on NFRA_REPORT returns 27 items, so the census fires on a second project and 18 is a measurement rather than an empty read.",
        "*** THE DUPLICATE-INSTANCE FINDING, WHICH IS THIS COMPILE'S OWN AND IS NOT IN THE CHANNEL. *** A walk of deliverables/ returns ELEVEN `*.proof_of_spec.json` files against NINE distinct `to_id` values. TO-IAM-s-4 and TO-IAM-s-5 each carry TWO. Compared by sha256: `TO-IAM-s-4.condition-axis-reader-what-a-policy-requires.proof_of_spec.json` and `TO-IAM-s-4.proof_of_spec.json` are BYTE-IDENTICAL (d23305c30973d8d3); the TO-IAM-s-5 pair likewise (ecc9f36faf74f69d). Both pairs were committed in the SAME commit as each other -- 6135bb93f6 and 52c82c7537.",
        "⛔ THEY ARE THE PHYSICAL RESIDUE OF THE DEFECT THE CHANNEL REPORTS FIVE TIMES. Rows W2-S1, Z-W1-S1, Z-W3-S1 and Z-W4-S1 each independently record that the WORKER FACE names the instance `<TO-id>.proof_of_spec.json` while `.tools/to-pipeline-gate.py::check_complete_flip` derives the expected stem from the TO file's FULL basename INCLUDING the descriptive suffix. A worker that writes the name its face specifies is refused the `complete` flip; the visible workaround is to write BOTH names, and two workers did exactly that. THE CHANNEL RECORDS THE INSTRUCTION DEFECT; NOBODY RECORDED THAT IT LEFT DUPLICATE ARTIFACTS IN THE TREE.",
        "CONSEQUENCE FOR TWO FIGURES, stated so neither is quoted wrong later. (1) A proof-instance count reads 11 where the DENOMINATOR IS 9. (2) A judgment-criteria census over the instance files returns ELEVEN judgment rows where only NINE ARE DISTINCT -- TO-IAM-s-4's AC5 and TO-IAM-s-5's AC6 are each counted twice. Any coverage or grading arithmetic built on the file count rather than on `to_id` overstates by two.",
        "THE JUDGMENT SET, MEASURED ON BOTH KEYS because the carrier is not consistent across this estate: 57 criteria across the 11 files, 46 PASS and 11 UNVERIFIABLE-BY-INSTRUMENT. EVERY ONE of the 11 carries `judgment: true` in the FIELD (unlike NFRA_OPSEC202609, where the flag lived only in `criterion_verbatim` text and a field-keyed census returned a clean zero). DE-DUPLICATED: NINE DISTINCT JUDGMENT CRITERIA, one per order, ALL RESERVED TO THIS SEAT AT L9 -- TO-IAM-s-1 AC5, s-2 AC5, s-3 AC5, s-4 AC5, s-5 AC6, s-6 AC5, s-7 AC5, s-8 AC5, s-9 AC5. That is the largest judgment set this seat has met: NFRA_OPSEC202609 round 2 carried 2 and NFRA_REPORT rounds 2 and 3 carried 2 and 0.",
        "WHAT THIS COMPILE DOES NOT CLAIM: that any criterion is correctly graded, that the 18 rows are grounded, or that L10 is reachable. Every item is UNDISPOSITIONED and the per-item pass has not run. It also does not re-grade the 46 PASS command-method criteria -- those reduce to an invocation and an expectation, are the executor's to self-report and the checker's to read, and are not the CVO's to re-run."
      ]
    },
    "spec_asserts": "L8 compiles the round for adjudication: every task order terminal with a valid proof instance, and the channel's items assembled for L9.",
    "world_is": "L7 is terminal at 9 of 9 and the channel carries 18 undispositioned items; but the instance population is 11 files for 9 orders with two byte-identical duplicate pairs, so both the instance count and the judgment-criteria count overstate by two unless keyed on to_id.",
    "notes": "THE THREADS THIS COMPILE IDENTIFIES, so the per-item pass has a shape rather than a list of 18: (A) THE FILENAME GATE DEFECT -- one defect, FIVE reports (W2-S1, Z-W1-S1, Z-W3-S1, Z-W4-S1, with Z-S4 disarming one and correcting the instruction), plus the duplicate artifacts recorded above. (B) THE UNDECLARED-ROLE POPULATION -- Z-S1's PRD denominator contradiction ('16 of 208' vs 'DECLARED=200 LIVE-no-DECLARED=16', which sums to 216, against 219 live today), and Z-S6/Z-W3-S2 establishing that the settled 16 CONTAINS A FALSE POSITIVE (seeking-alpha-scraper-role IS declared in Terraform), so the population is at most 15; Z-W3-S3/S4/S5 triage subsets of it. (C) THE HAND-OVER DIVERGENCE -- Z-W1-S4 and Z-S7: every one of four respawn hand-overs delivered a WORKER FACE RICHER THAN THE COMMITTED ORDER, so this seat would grade AC5 from a file NARROWER than the bar the worker was actually held to. That one is aimed directly at L9 and Z-S7 carries the delivered bar so the grade has it. (D) ID GRAMMAR AND FABRIC -- Z-W1-S2 (the dispatch prompt gave a row-id grammar without the site-z infix) and Z-S5 (a worker met the gate by declaring `fabric: laptop` rather than adding the infix). (E) TOOLING -- Z-S2 (worker.md reads `model: sonnet` on this fabric while relayed spine v3.7 says Opus/high) and Z-S3/Z-W1-S3 (the comp-rail bare-name census defect, WHICH WAS REPAIRED AT @6228c53377 AFTER these rows were written and is now on origin). || ⚠ NO L8 PACKET HAD BEEN SENT WHEN THIS COMPILE RAN. `2.0.0_SA_COO~ZI` drained the round and its completion report is not yet written. This row does not pre-empt that lane's compile: where the two disagree, the disagreement is itself the finding and this seat will say so rather than assuming its own arithmetic wins."
  }
]
```
