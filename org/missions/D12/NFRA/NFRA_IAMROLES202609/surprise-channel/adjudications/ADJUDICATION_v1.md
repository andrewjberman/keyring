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

## C-S4 -- the NINE judgment grades: eight PASS, one FAIL. `IN-CODE` is defined as a FACT and applied to eight members measured ABSENT, so '10 IN-CODE' reads as ten declared roles when two are

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T11:40Z",
    "one_line": "L9, round 1: the round's NINE judgment criteria are graded -- EIGHT PASS and ONE FAIL. The FAIL is IAM-s-6's AC5 and it is a TOKEN defect, not a research defect: `IN-CODE` is defined in the document as 'a FACT, not a recommendation' and then applied to EIGHT members the same document measured as ABSENT from every first-party Terraform file. The coverage line reads '10 IN-CODE', and a governance reader takes that as ten declared roles when roughly TWO are. The six EXEMPT dispositions are exemplary and the per-member research is sound throughout.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A GRADE RECORD, per the `grades` field's own contract: a row carrying grades that adjudicates no item and opens nothing carries DISMISSED_WITH_REASON with its reason naming it as one. This row adjudicates no investigation item; its content is the nine verdicts in `grades`, which is the field a consumer can reject on. The dismissal disposes of THIS ROW only -- all nine grades stand as the round's L9 verdicts.",
    "grades": [
      {
        "criterion": "IAMs1-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/NFRA_IAMROLES202609.TO-IAM-s-1.permission-grain-usage-instrument.proof_of_spec.json@d0c36abcc8f5",
        "verdict": "PASS",
        "reason": "THE BAR -- 'pick any role, a reviewer can see which of the things it is allowed to do it has never actually done, and over what period' -- is met on the RENDERED output. The instrument prints, unaided: the ROLE, the PERIOD ('lookback 90 days') in the units FWD-2 asks for, a DENOMINATOR on the same line (22 granted permissions examined), and per permission exactly one of three states. ⚠ BASIS OF THIS GRADE, STATED SO IT IS NOT OVER-READ: this seat did NOT re-run comp-iam-usage. It graded the RENDERED SPECIMEN quoted in the instance plus the TWO DOWNSTREAM DELIVERABLES THAT CONSUME IT -- COVERAGE_VOCABULARY.md and POSTURE_NUMBER.md -- both of which render the same live figures (22 / 6 / 2 / 14) coherently. A downstream artifact that consumes an instrument and renders consistent numbers is corroboration of the instrument's output, not of its internals."
      },
      {
        "criterion": "IAMs2-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/NFRA_IAMROLES202609.TO-IAM-s-2.posture-number-with-denominator-and-vintage.proof_of_spec.json@cb93354362df",
        "verdict": "PASS",
        "reason": "IT IS AN ANSWER, AND WHAT MAKES IT ONE IS THAT IT REFUSES THE FLATTERING READING. 'POSTURE: 8 of 22 granted permissions on opal-data-refresh-lambda-role carried an observed usage verdict under a 90-day lookback, vintage 2026-09-10' -- a numerator, a denominator, a window and a vintage, marked `claim: measured` and read live at render time. ⭐ THE DELIVERABLE THEN NARROWS ITS OWN HEADLINE AGAINST ITSELF: the outcome text says 'the estate's' posture and the file says in terms that this is 'a posture number for the ONE ROLE IAM-s-1 exercised, not for the estate's role population', citing A VALUE MUST CARRY ITS CLAIM. AND THE LARGEST BAND IS THE ONE IT REFUSES TO HIDE -- `unobservable` at 14 of 22 (64%) is never folded into the numerator and never silently dropped. 'Nobody has measured it' does stop being the answer for this role; the file is equally clear that it has not become the answer for the estate."
      },
      {
        "criterion": "IAMs3-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/NFRA_IAMROLES202609.TO-IAM-s-3.coverage-vocabulary-unused-vs-unobservable.proof_of_spec.json@26cb49f072ab",
        "verdict": "PASS",
        "reason": "SOMETHING NOBODY LOOKED AT NEVER READS AS SOMETHING LOOKED AT AND FOUND CLEAN, and the vocabulary is built to hold that line rather than merely to state it. The `unobservable` row of the vocabulary table carries an explicit means-NOT column: '**NEVER** clean, safe, probably unused or any other reading that credits an inspection that did not happen.' The renderer prints all three bands UNCONDITIONALLY including zero counts, so a role with only unobservable rows still prints `used=0 never-used=0` rather than omitting the bands nobody hit -- SILENCE IS THE THIRD WAY A NON-INSPECTION CAN READ AS CLEAN, and it is closed. ⭐ THE LIVE SPECIMEN CARRIES THE DISCRIMINATION THE BAR REQUIRES: s3:GetObject is granted and this account has NO action-level tracking for s3, so it renders `unobservable` with the reason on the row; cloudfront:GetInvalidation IS tracked and shows no access, so it renders `never-used`. A genuinely unobservable permission beside a genuinely completed inspection, distinguishable by a reader. And the largest band on the role is the unobservable one -- the most flattering number to hide."
      },
      {
        "criterion": "IAMs4-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/NFRA_IAMROLES202609.TO-IAM-s-4.condition-axis-reader-what-a-policy-requires.proof_of_spec.json@6135bb93f6ff",
        "verdict": "PASS",
        "reason": "TIGHT SCOPING IS PREVENTED FROM HIDING THE ABSENCE OF A SECOND FACTOR, and the exhibit is chosen adversarially rather than conveniently. The displayed statement is `aws_iam_role_policy.runner_selfstop` / Sid=SelfStopThisInstanceOnly -- ARN-pinned to exactly ONE EC2 instance for exactly ONE action, which is the TIGHTEST POSSIBLE (action, resource) scoping short of a deny-everything default -- and the reader renders it `REQUIRES-NOTHING`. THAT IS THE BAR EXACTLY: the most tightly scoped rule in the set is the one displayed as requiring nothing of the caller, so scope cannot buy silence on the condition axis. The document says so in terms -- 'REQUIRES-NOTHING is the token that makes that absence VISIBLE' -- and the same token appears on further statements (scheduler, orchestrator StartRunnerInstanceOnly, capture_writer), so it is a rendered axis rather than a single worked example."
      },
      {
        "criterion": "IAMs5-AC6",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/NFRA_IAMROLES202609.TO-IAM-s-5.declared-vs-live-reconciler-member-identity.proof_of_spec.json@52c82c753767",
        "verdict": "PASS",
        "reason": "THE TWO PLANES ARE SEPARATED IN TERMS AND NEITHER IS PRESENTED AS EVIDENCE ABOUT THE OTHER. The deliverable's INSTRUMENT AND VINTAGE section states: 'This is one plane only. comp-iam ... reports 195 roles from that source plane. 195-vs-203 or 195-vs-219 is NOT a DECLARED-vs-LIVE delta about this cell's question -- it is comp-iam's own parser reach on a different plane ... and is not presented here as evidence about the undeclared set.' ⭐ THAT IS THE HARDER HALF OF THE BAR: the tempting move is to quote the cross-plane difference as a finding, because it looks like a governance number. The cell names it as an instrument artefact instead, and does so BEFORE anyone could mistake it. The DRIFT figures it does use are all read from the one plane it declares."
      },
      {
        "criterion": "IAMs6-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/NFRA_IAMROLES202609.TO-IAM-s-6.governance-disposition-of-undeclared-roles.proof_of_spec.json@ffcc39967ad0",
        "verdict": "FAIL",
        "reason": "⛔ THE DISPOSITION DOES NOT FIT ITS MEMBER FOR EIGHT OF THE SIXTEEN, AND THE DEFECT IS THE TOKEN RATHER THAN THE RESEARCH. The document defines its primary token in terms -- 'Where step 1 or 2 found the role genuinely declared, the disposition is IN-CODE AS A FACT, NOT A RECOMMENDATION' -- and then applies IN-CODE to members it measured as ABSENT. Item 1, verbatim: '`bd-merge-daily-lambda-role` -- IN-CODE. Absent from the fresh 191-role comp-iam parse and from EVERY FIRST-PARTY TERRAFORM FILE in this repo'. Items 2, 5, 6, 9, 11, 14 and 16 carry the same shape. The reconciling sentence exists ('dispositioned IN-CODE -- the ordinary default state FWD-4 asks for absent any reason to except them') but it sits in a DIFFERENT PARAGRAPH and gives the SAME TOKEN a second, incompatible intent: IN-CODE means 'is declared' for item 13 (`seeking-alpha-scraper-role`, where the file itself says 'this one is FACTUALLY already declared') and 'ought to be declared' for the eight. || ⛔ WHY THIS FAILS THE BAR RATHER THAN BEING A WORDING NIT: AC5 asks whether a READER WOULD ACCEPT THESE AS DECISIONS. The coverage line reads '10 IN-CODE, 6 exempt', and a governance reader taking that at face value concludes TEN of the sixteen undeclared roles are declared. Roughly TWO are. The token that is supposed to carry the finding is the one that erases it, and nothing in the document flags the dual use -- this seat searched for a self-disclosure and found none. It is rule 24(iii) INTENT COHERENCE: one axis, one intent, and this axis carries two. || ⭐ WHAT IS EXPLICITLY NOT WRONG, because the grade should not be read as condemning the cell: the SIX EXEMPT lines are exemplary -- individually reasoned, non-templated, each naming the decision owed AND why no owner could be named, and the cell correctly refused to invent one. The per-member research is sound throughout, including the seeking-alpha correction that contradicts the drift instrument on evidence. THE REMEDY IS SMALL AND DOES NOT TOUCH THE RESEARCH: split the token -- IN-CODE-DECLARED for the members a source read found, ADOPT-RECOMMENDED (or equivalent) for the default -- which is a one-line edit per row and a corrected coverage line."
      },
      {
        "criterion": "IAMs7-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/NFRA_IAMROLES202609.TO-IAM-s-7.historical-remediation-completion-on-the-artifact.proof_of_spec.json@ff86d57e03a1",
        "verdict": "PASS",
        "reason": "A READER LEARNS WHETHER THE WORK WAS FINISHED, AND THE FOLDER IS EXPLICITLY EXCLUDED FROM THE METHOD -- which is the exact failure mode FWD-6 names. The document's method paragraph states: 'Verdicts are never drawn from which subfolder a plan document sits in (active/ vs completed/); a plan's folder is not consulted anywhere in this analysis.' ⭐ AND THE HARDEST CASE PROVES IT: Plan 1 sits in `active/` and is verdicted NOT-LANDED on the artifact -- the two named custom policies return 10 hits, ALL inside the plan document and the worker's own tool logs, with ZERO in infra/aws/terraform/ across 569 files scanned; a live `list-policies` returns []; FIVE of the plan's eight named target roles return NoSuchEntity; and the three that survive carry no IAMMigrationStatus tag. Each verdict token (NOT-LANDED / PARTIAL, split into three independently-verdicted phases / LANDED) is grounded in a citation the reader can re-run. The pinned vintage is re-confirmed at grading time so nothing moved mid-round."
      },
      {
        "criterion": "IAMs8-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/NFRA_IAMROLES202609.TO-IAM-s-8.pre-flight-blast-radius-exercised.proof_of_spec.json@aafee3fc572a",
        "verdict": "PASS",
        "reason": "SOMEONE CAN FIND OUT WHAT WOULD STOP WORKING AND BE RIGHT, and 'be right' is carried by the right instrument. The cell reaches EXERCISED through `simulate-principal-policy` -- a read-only API and the simulate battery the PRD's D3 named as never yet run for this project -- rather than by reading policy text and inferring. ⛔ AND IT APPLIED NOTHING: the deliverable states that no mutating IAM call and no IaC application occurred at any point, which is what keeps 'nothing breaks because we tidied up' honest as a PREDICTION rather than demonstrated by breaking something. The prediction names 6 concrete caller paths, TWO of them traced to real call sites at named lines (data_refresh/lambda_function.py:373 and :528). ⭐ BUILD-LADDER DISCIPLINE IS VISIBLE AND IS PART OF WHY THE ANSWER IS TRUSTWORTHY: it COMPOSES IAM-s-1's reach-check and permission-cold and SHELLS OUT to IAM-s-4's condition-axis-reader rather than re-implementing either, so the blast-radius answer inherits those instruments' own disciplines instead of a second copy's drift."
      },
      {
        "criterion": "IAMs9-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/NFRA_IAMROLES202609.TO-IAM-s-9.re-run-harness-composed-not-scheduled.proof_of_spec.json@9f594243400a",
        "verdict": "PASS",
        "reason": "A STRANGER CAN RE-RUN IT, AND THE HARNESS IS BUILT SO IT CANNOT QUIETLY STOP. It resolves its own repo root via `git rev-parse --show-toplevel` with no hardcoded device path -- which matters on THIS fabric, where the committed docs hardcode the other machine -- takes only --role/--lookback/--dry-run with stated defaults matching IAM-s-1/s-2's own, carries a --dry-run that touches nothing, and reproduced IAM-s-2's exact figures (22 / 6 / 2 / 14) on a live re-read. ⭐ THE PART THAT ANSWERS 'WITHOUT IT QUIETLY STOPPING BECAUSE ONLY ONE PERSON KNEW HOW' IS THE CARRIED CAVEAT: IAM-s-2's one-role scope limit is quoted VERBATIM in the header under 'DO NOT DROP ON A RE-RUN', so the next runner inherits the bound rather than the number alone -- the single most losable thing in a re-run. ⛔ AND IT HONOURS TWO STANDING ESTATE CONSTRAINTS BY NOT ACQUIRING ANYTHING: it mints no timer, notification or monitor of any kind (the standing alerting moratorium 'honoured by never acquiring one', re-run cadence left a human decision), and it never calls Access Analyzer, naming the reason as price-unread and stating that availability is not authorization."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE SET IS NINE, DE-DUPLICATED, AND THE DE-DUPLICATION MATTERS: a census over the instance FILES returns ELEVEN judgment rows because TO-IAM-s-4 and TO-IAM-s-5 each carry a BYTE-IDENTICAL DUPLICATE instance (C-S1). Keyed on `to_id` the set is NINE, one per order. Grading eleven would have graded two criteria twice and reported a coverage figure two too high.",
        "EVERY GRADE WAS TAKEN AGAINST THE DECIDING ARTIFACT, NOT THE WORKER'S ACCOUNT OF IT. The deliverables were opened at this seat -- COVERAGE_VOCABULARY.md, POSTURE_NUMBER.md, GOVERNANCE_DISPOSITION.md, HISTORICAL_COMPLETION.md, DECLARED_VS_LIVE.md, CONDITION_AXIS.md, BLAST_RADIUS.md and rerun-assessment.sh -- and the one FAIL was found by reading the disposition table row by row against the document's own definition of its token, which no summary would have surfaced. ⚠ THE ONE GRADE NOT TAKEN ON A PRIMARY ARTIFACT IS IAMs1-AC5 and its reason says so: the instrument was not re-run, and the grade rests on the rendered specimen plus two downstream consumers rendering the same figures coherently.",
        "⭐ EVERY ONE OF THE NINE WAS LEFT UNGRADED BY ITS OWN ASSIGNEE, correctly, and several said so in terms ('Whether that constitutes an ANSWER ... is graded by 3.0.0_SA_CVO~Z at L9'). A worker that assembles the evidence for a bar it may not score is the behaviour that makes a judgment criterion worth having, and this round is nine for nine on it.",
        "⛔ THE GRADES ARE TAKEN AGAINST THE DELIVERED BAR WHERE THE TWO DIVERGE, WHICH IS Z-S7'S FINDING APPLIED RATHER THAN CITED. Four of four respawn hand-overs delivered a worker face RICHER than the committed order, so grading AC5 from the committed file alone would score against a narrower bar than the worker was held to. Z-S7 carries the delivered text for IAM-s-9's AC5 and this grade uses it. THAT ROW NAMED THIS SEAT AS ITS DISARM OWNER AND THIS IS THE ACT THAT DISCHARGES IT.",
        "THE FAIL IS NARROW AND ITS REMEDY DOES NOT TOUCH THE RESEARCH: split the token into IN-CODE-DECLARED (members a source read actually found) and a distinct recommendation value for the default, plus a corrected coverage line. One edit per affected row. NOTHING in the cell's per-member evidence is disturbed, including the seeking-alpha-scraper-role correction that contradicts the drift instrument on a direct Terraform citation and which this seat verified independently at C-S2."
      ]
    },
    "spec_asserts": "L10 requires every judgment criterion of every proof-of-spec instance under the project to be graded in the CVO's adjudication, never self-graded by its executor.",
    "world_is": "The project carries nine distinct judgment criteria, all correctly left ungraded by their assignees; eight are met and one is not.",
    "notes": "⛔ L10 IS NOW REACHABLE ON BOTH LIMBS BUT THE ROUND DOES NOT CLOSE: 18 of 18 items dispositioned (C-S2/C-S3) and 9 of 9 judgment criteria graded (here). Rule 27 needs COMPLETION_REPORT + COMPLETION_GRADES with EVERY GRADE REALIZED, and IAMs6-AC5 is a FAIL -- so the round is slug-ready and NOT close-ready, and there is no COMPLETION_REPORT at any round of this project besides. || THE FAIL IS NOT A BLOCKER ON THE SLUG and this seat does not treat it as one: a failed judgment criterion is a graded outcome, not an open item, and it rides the slug as a finding with a named remedy. || WHAT THIS ROW DOES NOT DO: it does not re-grade the 46 command-method PASS criteria, which reduce to an invocation and an expectation and are the executor's to self-report and the checker's to read; and it does not grade FWD outcomes, which are 1.0.0_SA_CTO~Z's at L10."
  }
]
```

## C-S5 -- the decomposition's '195 TF roles' does NOT reproduce, and its author found its own cause: A BATTERY FIGURE TAKEN FROM A SHARED CHECKOUT MEASURES A MOMENT, NOT A VINTAGE

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S5",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T13:58Z",
    "one_line": "BOTH GRADUATE, AND THEY ARE ONE FINDING IN TWO HALVES: a worker proved the decomposition's own '195 TF roles' does not reproduce, and the seat that wrote it found its own cause 18 minutes later -- the figure was measured from the SHARED MAIN CHECKOUT, which carries other seats' UNCOMMITTED .tf files. ⛔ THE STRUCTURAL HALF IS THE ONE THAT RECURS: a figure taken from a shared tree is UNREPRODUCIBLE BY CONSTRUCTION for a worker, because a worker's worktree is clean BY CONSTRUCTION -- the very discipline that makes workers safe makes them structurally unable to reproduce it.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW AND UNCHANGED. Z-W6-S1's is 2.0.0_SA_COO~ZI (the decomposition is that lane's artifact); Z-S9's is 1.0.0_SA_CTO~Z. Neither is this seat's and neither is taken here.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-W6-S1",
      "NFRA_IAMROLES202609-Z-S9"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE ARITHMETIC RE-DERIVED AT THIS SEAT ON THE ARTIFACT, NOT ACCEPTED FROM EITHER ROW. *** `git ls-files --others --exclude-standard -- '*.tf'` then a whole-value count of `^resource \"aws_iam_role\" ` across exactly those files: freshness_alarm.tf 1, item2d_freeze_monitor.tf 1, tool_activity_freshness.tf 1, inf-gold-freshness-guard.tf 1, freshguard_derive_watchdog.tf 0 -- TOTAL 4. 195 - 4 = 191. ⭐ Z-S9's causal claim REPRODUCES EXACTLY, and the count is whole-value against `aws_iam_role` so it does not silently absorb the `aws_iam_role_policy` blocks that outnumber it 13 to 4 in the same files.",
        "⚠ ONE REFINEMENT, RECORDED BECAUSE IT WOULD OTHERWISE READ AS A DISCREPANCY TO THE NEXT READER: the raw filesystem carries SIX untracked .tf files, not five. The sixth is `.runtmp_ac4/fmtchk/cloudfront-distribution.tf` and it holds ZERO role blocks, and it sits in what comp-find prints as the EPHEMERAL FLOOR -- excluded from the tool's default corpus. So 'five' is correct for the INSTRUMENT'S corpus and 'six' for the raw filesystem, and the load-bearing 4 is exact on either denominator. THIS IS A CORPUS-BOUNDARY ARTIFACT AND NOT AN ERROR IN THE ROW; it is named here so a later reader who counts six does not conclude the row was sloppy.",
        "⭐ THE WORKER DID NOT DEFER TO ITS OWN ORDER, WHICH IS THE HARDEST DIRECTION TO FILE IN AND THE REASON THIS PAIR EXISTS. IAM-r-2's bound named this exact pair as 'THE ARITHMETIC TRAP' and stated 195 AS FACT -- 'the round-2 battery run of the same tool reports 195' -- instructing the cell to RECONCILE against it, which frames 195 as the fixed point and any disagreement as the worker's error. It ran the identical instrument twice against the identical clean tree, got 191 both times, and filed against the ORDER'S OWN PREMISE. A cell instructed to reconcile a number will usually find a way to reconcile it.",
        "AND THE DISCRIMINATION IS WHAT MAKES IT A MEASUREMENT RATHER THAN A DISAGREEMENT: every OTHER sub-figure in the same citation reproduces exactly -- 188 services, 1084 operations, 304 gaps -- so the divergence is ISOLATED TO THE ROLE COUNT ALONE. A vintage drift or a parser change would have moved the neighbours too. That isolation is what pointed at a role-shaped cause, and a role-shaped cause is exactly what Z-S9 found.",
        "⛔ THE GENERALISABLE LAW, WHICH IS WORTH MORE THAN THE FOUR ROLES: A BATTERY FIGURE MEASURED FROM A SHARED CHECKOUT IS NOT A MEASUREMENT OF THE ESTATE -- IT IS A MEASUREMENT OF THE ESTATE PLUS WHATEVER OTHER SEATS HAVE NOT YET COMMITTED. Z-S9 states this precisely and its own framing is the sharp part: the figure 'is not wrong about the tree it read; it is wrong about what a reader will take it to mean.' A decomposition's battery disposition is read as a claim about a VINTAGE, and on a five-seat single-checkout device it is silently a claim about a MOMENT.",
        "⭐ AND THE ASYMMETRY THAT MAKES IT UNRECOVERABLE RATHER THAN MERELY WRONG: the issuer measures from the shared tree and the worker measures from a linked worktree that is CLEAN BY CONSTRUCTION -- rule 14b and /dispatch MANDATE one worktree per worker slot. So the two seats cannot agree even in principle, and the disagreement presents to the worker as its own instrument failing. THE DISCIPLINE THAT MAKES WORKERS SAFE IS THE SAME PROPERTY THAT MAKES THEM UNABLE TO REPRODUCE AN ISSUER'S FIGURE.",
        "⚠ THIS SEAT MET THE SAME SUBSTRATE FROM A DIFFERENT DIRECTION 12 MINUTES BEFORE ADJUDICATING THIS ROW, AND IT IS THE SAME DEFECT IN A SECOND INSTRUMENT. This seat's own round-3 L9 commit on NFRA_OPSEC202609 was REFUSED by the standing corpus pass reporting '1 malformed block' -- which did not exist. `.tools/surprise-corpus-validate.py` enumerates its paths from the GIT INDEX but READS THE BYTES FROM THE WORKTREE, so it read a PEER'S FILE MID-WRITE (measured: two channel documents written at 13:41:33Z and 13:43:37Z, inside the commit window) and counted a half-written JSON fence as malformed. Re-run after the peer settled: 0 malformed, 920 rows. NO OVERRIDE WAS USED AND NONE WAS NEEDED -- the refusal was CORRECT and transient. Two instruments, two seats, one substrate: A SHARED MUTABLE CHECKOUT READ AS IF IT WERE A VINTAGE.",
        "SCOPE, NARROW: this graduates the pair and does NOT regrade round 1, whose slug is @fd7a0b3e91. The four untracked .tf files are other seats' live work and NOTHING HERE ASKS FOR THEM TO BE COMMITTED, moved, or removed -- the defect is in how a figure was TAKEN, not in the files' existence, and a remedy aimed at the files would be aimed at the wrong object."
      ]
    },
    "spec_asserts": "A decomposition's battery disposition records a measurement of the estate at the cut's vintage, reproducible by a later reader -- or a worker -- running the same instrument against the same tree.",
    "world_is": "It recorded whatever sat in the shared working tree at that moment, committed or not; the four uncommitted role blocks are the whole of the 195-vs-191 gap, and a worker's clean worktree cannot reproduce it by construction.",
    "notes": "NEITHER ROW IS THE OTHER'S DUPLICATE AND BOTH GRADUATE ON PURPOSE. Z-W6-S1 is the MEASUREMENT (the figure does not reproduce, established with an isolation control across four sub-figures); Z-S9 is the CAUSE (why, named by the seat that wrote the figure). Dismissing either as redundant would lose half the record: the measurement without the cause is an unexplained discrepancy a later reader would re-litigate, and the cause without the measurement is an assertion. ⭐ AND THE 18-MINUTE TURNAROUND IS ITSELF THE EVIDENCE THAT THE CHANNEL WORKED AS DESIGNED -- a worker filed a row against its issuer's premise at 13:22Z and the issuer had found and recorded its own cause by 13:40Z, without a message, because the ROW is the carrier."
  }
]
```

## C-S6 -- Z-S8: Terraform owns FOUR policies on a role it does NOT declare, the governance axis has no value for that member, and this seat's own round-1 remedy was too narrow

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S6",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T13:58Z",
    "one_line": "Z-S8 GRADUATES: Terraform owns FOUR inline policies on a production role IT DOES NOT DECLARE, so the estate's code depends on a resource it could not recreate -- and the governance axis has NO VALUE FOR THAT MEMBER. ⛔ THIS NARROWS THIS SEAT'S OWN ROUND-1 REMEDY, WHICH WAS TOO SMALL: at C-S4 this seat graded IAMs6-AC5 a FAIL and prescribed SPLITTING THE IN-CODE TOKEN. A token split does not help a member that fits NEITHER value.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z, as the row states and unchanged here. A value-enum change is a schema act under rule 24 and arrives with its own four-postulate record plus a word-boundary token census; that is not a grading act and not this seat's to make.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-S8"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** BOTH HALVES VERIFIED AT THIS SEAT ON THE FILE ITSELF, WITH THE CONTROL IN THE SAME RUN THAT MAKES THE ZERO MEAN SOMETHING. *** `comp-read infra/aws/terraform/data-refresh/main.tf --enumerate 'resource \"aws_iam_role\"'` -> 0 hit(s) across 161 lines, whole-value 0 AND substring 0. POSITIVE CONTROL, SAME FILE, SAME INSTRUMENT: `resource \"aws_iam_role_policy\"` -> 4 whole-value hits at :58 data_refresh_sscn_s3, :80 data_refresh_cloudfront_read, :99 data_refresh_time_machine_invoke, :138 portal_time_machine_invoke_downstream. FOUR POLICY ATTACHMENTS, ZERO ROLE DECLARATIONS, in 161 lines.",
        "⛔ THE CONSEQUENCE IS A BROKEN DEPENDENCY GRAPH ON A PRODUCTION SERVING PATH, not a style complaint: Terraform attaches four inline policies to `opal-data-refresh-lambda-role` BY NAME STRING to a role outside its own graph. It therefore CANNOT CREATE THE ROLE AND COULD NOT RESTORE IT -- a destroy-and-recreate of this module reproduces the policies onto a role that no longer exists, and `terraform plan` cannot see the hazard because a name string is not an edge.",
        "⭐ AND THE DISCRIMINATION FAILURE IS THE PART THAT GENERALISES: A NAME MATCH IN TERRAFORM IS NOT A DECLARATION. The role returns 9 hits across the tree and is undeclared -- so a membership check keyed on the NAME would classify it IN-CODE on 9 pieces of confirming evidence. The evidence is IDENTICAL whether the role is declared or not, which is rule 22's DISCRIMINATION axis failing exactly as written: the check cannot distinguish the true state from the false one, and it fails toward the reassuring answer.",
        "⛔ RULE 24(i), MECE, WITH THE UNCOVERED MEMBER NAMED: the governance vocabulary partitions members into IN-CODE and EXEMPT. This member is NEITHER -- it is PARTIALLY MANAGED, its policies owned and its identity not. A binary axis cannot express partial ownership, so the member must be forced into a value that misdescribes it, and BOTH available choices mislead: IN-CODE claims a declaration that does not exist, EXEMPT claims Terraform has no stake in a role it writes four policies onto.",
        "*** THIS IS THE SECOND INDEPENDENT ARM ON ONE TAXONOMY AND IT NARROWS THIS SEAT'S OWN EARLIER REMEDY. *** At C-S4 (round 1, @3277ee562b) this seat graded IAMs6-AC5 a FAIL on rule 24(iii) INTENT COHERENCE -- the IN-CODE token carrying two meanings at once, a measured fact and a recommendation -- and prescribed splitting the token, 'one edit per row'. Z-S8 arrives from the opposite direction on rule 24(i) and shows THAT REMEDY IS INSUFFICIENT: splitting a token into two honest tokens still leaves a member that belongs in neither. ⚠ THE ROUND-1 GRADE STANDS AS A CORRECT FAIL; ITS PRESCRIBED REMEDY WAS TOO NARROW, and this seat records that against itself rather than leaving the two findings to be reconciled by whoever implements them.",
        "⭐ THE ROW ALSO CARRIES ITS OWN GENERAL FORM RATHER THAN JUST ITS INSTANCE, which is why it graduates BLOCKING and not as a single-file note: 'A NAME MATCH IN TERRAFORM IS NOT A DECLARATION.' The instance is one role on one serving path; the form governs every membership question this project exists to answer, and this project's whole output is a partition of roles into declared and undeclared."
      ]
    },
    "spec_asserts": "The undeclared roles are 'not written down in our code' and the remedy for a production serving-path member is to bring it into Terraform; the governance vocabulary partitions members into in-code and exempt.",
    "world_is": "One member is neither -- Terraform owns four policy attachments on a role it does not declare -- and a membership check keyed on a name match would call that role declared on nine hits, none of which declares it.",
    "notes": "⛔ THE REMEDY IS NOT PRESCRIBED HERE AND THE ROW IS RIGHT NOT TO PRESCRIBE ONE EITHER. Two candidate directions exist and they are not equivalent -- bring the role into Terraform (an infra act on a production serving path, with an import and a real blast radius) or widen the governance axis to express partial ownership (a schema act under rule 24). ⚠ AND A THIRD OPTION MUST NOT BE TAKEN BY DEFAULT: leaving the member classified under whichever value the current axis forces, which is what a reader does when no value fits and the schema demands one. || ROUND 1 IS NOT REOPENED: its slug is @fd7a0b3e91 and its grades stand. This item was surfaced at 12:40Z, AFTER that slug, and belongs to the next round's docket -- it is dispositioned now because no slug is cut here and rule 29 governs, not because round 1 is being revisited."
  }
]
```
