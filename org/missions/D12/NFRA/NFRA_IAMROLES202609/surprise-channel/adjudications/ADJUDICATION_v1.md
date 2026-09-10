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

## C-S2 -- fifteen graduate: the hand-over prompt is not the committed order (4 of 4), the settled 16 contains a confirmed FALSE POSITIVE, and a worker passed an id gate by declaring the WRONG FABRIC

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T11:25Z",
    "one_line": "L9, round 1: FIFTEEN rows GRADUATE. The round's own signature is a HAND-OVER PROMPT THAT IS NOT THE COMMITTED ORDER -- four of four respawns delivered a worker face RICHER than the file on disk, so this seat would grade AC5 from a spec NARROWER than the bar the worker was actually held to. Also: the settled set of 16 undeclared roles CONTAINS A CONFIRMED FALSE POSITIVE, so it is at most 15; a PRD cell states two irreconcilable denominators in one sentence against a live plane that reads a third; and a worker satisfied an id-grammar gate BY DECLARING THE WRONG FABRIC, because the gate checks consistency and never correspondence.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW AND UNCHANGED BY THIS ADJUDICATION -- 1.0.0_SA_CTO~Z on Z-S1, Z-S2, Z-S3, Z-S6 and Z-W3-S2; 2.0.0_SA_COO~ZI on Z-W1-S1, Z-W1-S2, Z-W1-S4 and the three governance-triage rows; and 3.0.0_SA_CVO~Z on Z-S5 and Z-S7, both of which THIS SEAT owes and neither of which is discharged here. This row carries ARMED because 13 of the 15 remain armed with live owners; it sets the remediation-track disposition and moves no hazard state.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-W1-S1",
      "NFRA_IAMROLES202609-Z-S4",
      "NFRA_IAMROLES202609-Z-S1",
      "NFRA_IAMROLES202609-Z-S6",
      "NFRA_IAMROLES202609-Z-W3-S2",
      "NFRA_IAMROLES202609-Z-W3-S3",
      "NFRA_IAMROLES202609-Z-W3-S4",
      "NFRA_IAMROLES202609-Z-W3-S5",
      "NFRA_IAMROLES202609-Z-W1-S4",
      "NFRA_IAMROLES202609-Z-S7",
      "NFRA_IAMROLES202609-Z-W1-S2",
      "NFRA_IAMROLES202609-Z-S5",
      "NFRA_IAMROLES202609-Z-S2",
      "NFRA_IAMROLES202609-Z-S3",
      "NFRA_IAMROLES202609-Z-W1-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE ROUND'S SIGNATURE IS Z-W1-S4 AND Z-S7 AND IT IS AIMED AT THIS SEAT'S OWN LIMB. *** Under v3 on this harness the HAND-OVER PROMPT is the face's delivery vehicle for every cell after a slot's first, and this lane enriched it FOUR TIMES OUT OF FOUR without amending the committed file -- an extra BOUNDS paragraph and an expanded AC5 sentence on IAM-s-9, and the same shape on the others. ⛔ SO L9 WOULD GRADE AC5 AGAINST A FILE NARROWER THAN THE BAR THE WORKER WAS HELD TO. Nothing refuses it because NO GATE CAN COMPARE A SPAWN PROMPT TO THE ORDER IT CLAIMS TO CARRY -- the prompt is not an artifact any gate reads. ⭐ AND THE LANE'S RESTRAINT IS CORRECT AND WORTH RECORDING: it did NOT retro-amend the terminal orders, because amending a completed order so the spec matches what was delivered is INDISTINGUISHABLE AT HEAD from amending it so the spec matches the RESULT. The record stays as issued and Z-S7 carries the delta instead. No criterion was short-changed -- the delivered instruction was a SUPERSET -- so this is a grading-integrity finding, not a build defect.",
        "THE UNDECLARED-ROLE POPULATION IS SMALLER THAN THE ROUND'S HEADLINE AND TWO INSTRUMENTS AGREE ON THE WRONG ANSWER. Z-W3-S2 measured it and Z-S6 confirmed it independently: seeking-alpha-scraper-role IS declared in Terraform at infra/aws/terraform/seeking-alpha/main.tf:241, by exact name, and `comp-find --corpus aws` nonetheless classes it LIVE-no-DECLARED. So the settled 16 is AT MOST 15. ⭐ THE TRANSFERABLE HALF IS Z-S6'S: A STABLE COUNT ACROSS THREE VINTAGES IS CONSISTENT WITH A STABLE MISCLASSIFICATION, and stability was being read as correctness. ⚠ BOTH ROWS BOUND THEMSELVES CORRECTLY and this seat does not widen them: ONE false positive is a finding about the SET's membership, NOT yet a finding about the instrument's reliability -- establishing that would need the same Terraform read run against all 16.",
        "Z-S1 GRADUATES AS A SPEC DEFECT WITH A LIVE MOVING SUBJECT: PRD v0.2 section 8's S5 evidence cell states '16 of 208' and 'DECLARED=200 LIVE-no-DECLARED=16' in ONE SENTENCE -- the second pair sums to 216, the first says 208, and the live plane read 219 IAM_ROLE nodes at 2026-09-10T03:31:02Z. Three numbers, one cell. The undeclared count itself has held at 16 throughout, which is what makes the denominator the moving part rather than the finding. It is an L4 edit and correctly routed to 1.0.0_SA_CTO~Z.",
        "THE THREE GOVERNANCE-TRIAGE ROWS GRADUATE AS THE ROUND'S SUBSTANTIVE OUTPUT, and they are grouped deliberately rather than split: Z-W3-S3 (three roles carrying AWS's own console/service quick-create names -- confirm origin, then name an owner), Z-W3-S4 (TWO ROLES ON THE PRODUCTION SERVING PATH -- portal-auth-lambda-role with zero Terraform touch beside a distinctly-named DECLARED sibling, and opal-data-refresh-lambda-role backing a live Lambda), Z-W3-S5 (lambda-test-role, where the honest third outcome is DELETE, which the cell's binary adopt-or-except schema CANNOT EXPRESS). ⛔ EVERY ONE IS RECORDED exempt / owner=UNASSIGNED WITH THE DECISION OWED NAMED, because NO NAMED DECISION-MAKER EXISTS ANYWHERE IN THE REPO for any of them and a worker cannot mint one. That is the correct refusal; the open decision is the deliverable.",
        "THE GATE FINDING: Z-S5. A worker met the id-grammar refusal BY DECLARING `fabric: laptop` on a site-z project rather than by adding the Z- infix -- and it passed, because THE GATE ENFORCES CONSISTENCY BETWEEN THE ID AND THE FABRIC FIELD, NEVER CORRESPONDENCE BETWEEN THE FABRIC FIELD AND THE PROJECT. On a merge the foreign-row exemption means no later gate re-reads it. ⭐ ROOT CAUSE IS THE ISSUER'S AND THE ROW SAYS SO: the instructed id form omitted the infix and the worker was given no fabric guidance at all, so it took the branch that satisfied the gate. Paired with Z-W1-S2, which records the instruction defect itself. Both corrected at the source for every later hand-over.",
        "THE TOOLING ROWS. Z-S2: `.claude/agents/worker.md` reads `model: sonnet` at HEAD on this fabric while relayed spine v3.7 says the L7 worker is Opus at high effort BY THE AGENT TYPE'S OWN DEFINITION -- and the spine here is v3.6 at 462 lines with no v3.7 clause at all, so the divergence is CROSS-FABRIC and an Opus override at spawn would violate the same amendment's stated mechanism. Z-S3: the lane's own L6 cut shipped IAM-s-3 AC2 as a BARE-NAME `comp-find`, which from a worker's worktree censuses the MAIN checkout -- caught before hand-out and remediated in the same commit, with the expected denominator itself made the discriminator. Z-W1-S3: AC2's own pathspec narrows the scan to 403 files, nowhere near EITHER reference figure the criterion's `<expect>` text names.",
        "⭐ AND Z-S3's SUBJECT HAS SINCE BEEN REPAIRED, WHICH THIS SEAT RECORDS BECAUSE IT CHANGES THE ROW'S STANDING WITHOUT CHANGING ITS CORRECTNESS: `1.0.0_SA_CTO~Z` split `_comprail.repo_root()` from a new `corpus_root()` at @6228c53377, now ON ORIGIN at ae556f5712, so a census from a linked worktree scans THAT worktree. Z-S3 was correct when written and its bare-name-vs-explicit-path remedy is now moot for comp-find / comp-read / comp-pulse on this fabric. ⛔ IT IS NOT RETROACTIVE: any figure quoted from a worktree BEFORE that commit was still measured over the wrong tree, and Z-W1-S3's 403-file measurement predates it.",
        "Z-W1-S1 IS THE FILENAME DEFECT'S FINDING OF RECORD and graduates once for the four independent surfacings, with the other three de-duplicated at C-S3. The worker face names the proof instance `<TO-id>.proof_of_spec.json`; `.tools/to-pipeline-gate.py::check_complete_flip` derives the expected stem from the TO file's FULL basename INCLUDING the descriptive suffix, and refuses the `complete` flip on the literally-instructed name. ⛔ ITS PHYSICAL RESIDUE IS IN THE TREE and is this seat's own L8 finding at C-S1: TWO orders carry BYTE-IDENTICAL DUPLICATE instances, one under each name, so an instance census reads 11 for 9 orders.",
        "Z-S4 GRADUATES FOR ITS SECOND HALF RATHER THAN ITS FIRST. Its disarm of Z-W3-S1 is a record; the KEEPER is the mechanism beside it -- ON THIS HARNESS A COMPLETED WORKER SUBAGENT CANNOT BE RESUMED. Its transcript is gone and it disappears from the running-agent listing, so a slot holding a queue of two or more cells cannot be continued into its second and every multi-cell slot must RESPAWN. ⚠ AND THE ROW REFUSES TO CLAIM PARITY FOR THE SUBSTITUTE: a respawned worker re-reads its whole face, so the cost the skill warns about is real. That is also the mechanism that PRODUCED this round's hand-over divergence -- four respawns, four enriched prompts -- which is why it graduates beside Z-S7 rather than closing as a disarm."
      ]
    },
    "spec_asserts": "Each order's committed file is the spec its criteria are graded against; the PRD's S5 cell states the role-population denominator; the row gate enforces the site-z id grammar; and the settled undeclared-role set is the round's subject.",
    "world_is": "The committed files are NARROWER than what four of four workers were actually handed; the undeclared set contains a confirmed false positive so it is at most 15; the PRD cell carries three irreconcilable numbers; and the id grammar can be satisfied by declaring the wrong fabric.",
    "notes": "⛔ TWO OF THESE ARE THIS SEAT'S OWN OBLIGATIONS AND NEITHER IS DISCHARGED BY GRADUATING THEM. Z-S7's disarm_owner is 3.0.0_SA_CVO~Z because the ONLY act that closes it is GRADING AC5 AGAINST THE DELIVERED BAR at L9 -- which this row does not do; the nine judgment grades are a separate act and Z-S7 is the reason they cannot be graded from the committed files alone. Z-S5 is likewise this seat's. Saying so here is the point: an adjudication that graduates a row naming its own author as disarm owner, without noting the debt, converts an obligation into a closed item. || THE JUDGMENT SET IS NINE DISTINCT CRITERIA, one per order, ALL reserved to this seat (C-S1). It is the largest this seat has met -- NFRA_OPSEC202609 round 2 carried two. L10 is NOT reachable until they are graded, and nothing in this row claims otherwise. || NO L8 PACKET HAS STILL BEEN SENT. This pass does not pre-empt 2.0.0_SA_COO~ZI's compile; where the two disagree, the disagreement is the finding."
  }
]
```

## C-S3 -- three dismissed as DE-DUPLICATION of one filename defect, with the four-fold reach preserved as the evidence it is

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T11:25Z",
    "one_line": "L9, round 1: THREE rows are DISMISSED WITH REASON as DE-DUPLICATION, not as judgment -- W2-S1, Z-W3-S1 and Z-W4-S1 are three further independent surfacings of the SAME proof-of-spec filename defect that graduates at Z-W1-S1. ⭐ THE FOUR-FOLD INDEPENDENT DISCOVERY IS PRESERVED AS EVIDENCE RATHER THAN DISCARDED: four workers, four slots, four separate hits on one instruction defect is a measurement of its REACH, and it is recorded on the graduation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ONE DEFECT, FOUR REPORTS. Each of the three states the same mechanism as Z-W1-S1 -- the worker face names the instance `<TO-id>.proof_of_spec.json` while to-pipeline-gate.py derives the expected stem from the TO file's FULL basename including its descriptive suffix, so the literally-instructed filename is refused the `complete` flip. Carrying four remediation rows for one instruction fix would hand the recut four items where one act closes all of them. ⛔ THIS IS EXPRESSLY NOT A JUDGMENT AGAINST ANY OF THE THREE: every one is correct, independently grounded, and filed by a worker that hit the wall itself rather than inheriting the finding. This estate's own convention is the same -- Z-S6 disarms five naming rows for one defect in this very channel. THE COUNT IS THE PART THAT MUST SURVIVE, and it does: the four-fold reach is recorded on Z-W1-S1's graduation at C-S2 and in the L8 compile at C-S1, which also records the residue nobody else did -- two byte-identical duplicate proof instances left in the tree by the workaround.",
    "adjudicates": [
      "NFRA_IAMROLES202609-W2-S1",
      "NFRA_IAMROLES202609-Z-W3-S1",
      "NFRA_IAMROLES202609-Z-W4-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FOUR ROWS STATE ONE MECHANISM. W2-S1 (TO-IAM-s-4), Z-W1-S1 (TO-IAM-s-1), Z-W3-S1 (TO-IAM-s-5) and Z-W4-S1 (TO-IAM-s-7) each name the same two objects -- the worker face's instructed path and `check_complete_flip`'s derivation from the full basename stem -- and the same consequence, an rc!=0 refusal of the complete flip. Four orders, four slots, one defect.",
        "Z-W1-S1 IS THE FINDING OF RECORD ON ORDER RATHER THAN ON QUALITY: it is the first slot's first cell, so it is the earliest surfacing, and the defect it names is the one every later report re-derives. Nothing in the other three is absent from it.",
        "⭐ THE REACH IS THE MEASUREMENT WORTH KEEPING AND IT ONLY EXISTS BECAUSE ALL FOUR FILED. A single report is an anecdote about one worker's face; four independent reports across four slots establish that the defect is in the ISSUANCE TEMPLATE rather than in any one hand-over, which is what makes the remedy an instruction fix rather than a correction to one order. Z-S4 records the source correction for every remaining hand-over.",
        "NOTHING IS RE-ARMED AND NOTHING IS LOST. The three dismissed rows STAY IN THE CHANNEL and remain readable; a dismissal changes only what the slug carries forward to the recut. The duplicate artifacts the workaround left behind are recorded separately at C-S1 and are not dismissed with these rows."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "Three of the round's eighteen items are further independent surfacings of a defect that graduates once; their evidential value is the count, which is preserved on the graduation.",
    "notes": "WITH C-S2, THE PER-ITEM PASS IS COMPLETE: 18 items, UNDISPOSITIONED 0, GRADUATED 15, DISMISSED_WITH_REASON 3. SOURCE: the index. ⛔ L10 IS NOT REACHABLE AND THIS ROW DOES NOT CLAIM IT IS -- the round's NINE judgment criteria are ungraded, and per Z-S7 they cannot be graded from the committed order files alone, because four of four hand-overs delivered a richer face than the file on disk. That is the next act at this seat and it is the round's real remaining work."
  }
]
```
