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

## C-S7 -- Z-S10: the proof checker grades THE TREE THE SCRIPT LIVES IN, calls a valid worker instance INVALID, and NAMES THE WORKER in the refusal

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S7",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T14:32Z",
    "one_line": "Z-S10 GRADUATES: `proof-of-spec-check.py` resolves artifact paths against THE TREE THE SCRIPT LIVES IN, not the tree it is run from, so a COO draining a spine-v3 worker with the main tree's copy grades a VALID instance INVALID -- and the refusal NAMES THE WORKER'S ARTIFACT, so it reads as the worker's defect. ⛔ EVERY v3 WORKER IS IN A LINKED WORKTREE BY CONSTRUCTION, SO THIS SITS ON THE DEFAULT DRAIN PATH AND NOT ON AN EDGE CASE.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z, unchanged from the row -- and DISCHARGED BY THAT SEAT @709b9556a3 BEFORE THIS ROW LANDED. `.tools/` is that seat's surface and the fix is a source edit; NOT TAKEN HERE. hazard_standing stays ARMED because it records the state AT SURFACING and is not rewritten by a later discharge -- the disarm is RECORDED in the remediation track when this project's next slug cuts.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-S10"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE ROW'S EVIDENCE IS THE BEST-CONTROLLED THIS SEAT HAS ADJUDICATED THIS SESSION, AND THE CONTROLS ARE WHY IT NEEDS NO RE-RUN. *** It measures the SAME instance at the SAME commit with ONE VARIABLE CHANGED -- main-tree copy: violations=1 INVALID rc=1; worktree's own copy: violations=0 VALID rc=0. Then it proves the violation FALSE independently of the checker (`git ls-tree --name-only b077f10538` lists the artifact; `test -f` finds it), cites the cause at source (`:193` `_REPO_ROOT = Path(__file__).resolve().parent.parent`, consumed at `:327` and `:363`), and carries TWO controls: a bogus criterion id produced the silent-omission violation FROM BOTH COPIES (the instrument was alive in both), and the main copy graded a MAIN-TREE instance VALID (the main copy is not simply broken). ⭐ THE PAIR OF CONTROLS IS WHAT CONFINES THE DEFECT TO A CROSS-TREE PAIRING rather than to either copy or either instance.",
        "⛔ THE ATTRIBUTION IS THE HAZARD, NOT THE FALSE VERDICT. The refusal names the WORKER's artifact as a dead path, so it presents as the worker's defect -- and the standing rule NEVER TRUST A PRODUCER'S SELF-REPORT points at exactly the party who is innocent here. ⭐ THE ROW SAYS THIS AGAINST ITSELF: 'the worker's own report claiming rc=0 VALID looked like the thing to distrust ... but the discriminator was not the worker's honesty, it was WHICH COPY OF THE CHECKER RAN.' A correct general rule aimed the investigation at the wrong party, and only a second reading with the variable isolated recovered it. THAT IS A DEFECT THAT MANUFACTURES A FINDING AGAINST AN INNOCENT SEAT, which is why it graduates BLOCKING rather than as an instrument note.",
        "⚠ THE DIRECTION THE ROW FLAGS AS UNEXERCISED IS THE WORSE ONE AND THIS SEAT ENDORSES THE FLAG WITHOUT UPGRADING IT. Because `:327` accepts presence in `_REPO_ROOT` alone, a file at the SAME PATH in the main tree would satisfy the presence test for a commit that does NOT carry it, and `:363` would feed the content rung THE MAIN TREE'S BYTES -- a FALSE PASS rather than a false refusal. The row states plainly that it did not construct that case and does not assert it. ⭐ THAT RESTRAINT IS CORRECT AND IS PRESERVED HERE UNGRADED: a false refusal is loud and self-correcting; a false pass is silent and certifies work that was never checked. The remedy should be chosen against the SILENT direction even though only the LOUD one has been observed.",
        "THE REMEDY IS THE ROW'S AND THIS SEAT ADDS ONLY A PREFERENCE BETWEEN ITS TWO FORMS. Derive the root from the INSTANCE PATH or from `git rev-parse --show-toplevel` at the CWD; or REFUSE OUTRIGHT when the instance lies outside `_REPO_ROOT`. ⭐ THE ROW ALREADY PREFERS THE REFUSING FORM AS 'the smaller change and fails loud', AND THAT IS RIGHT FOR A REASON WORTH STATING: re-deriving the root makes the tool correct in more cases, but refusing makes the tool INCAPABLE OF THE SILENT FAILURE ABOVE. Against a defect whose dangerous direction is a false pass, the change that removes the capability beats the change that improves the accuracy.",
        "THE WORKAROUND IS ALREADY IN FORCE AND NEEDS NO RULING: both remaining round-2 workers were told in their spawn to run the WORKTREE's own copy, never the main tree's.",
        "*** DISCHARGED WHILE THIS ROW WAS HELD, AND THE REMEDY CHOSEN WAS THE REFUSING FORM THIS ROW ARGUED FOR. *** 1.0.0_SA_CTO~Z fixed it at @709b9556a3 (msg 20962), and its stated reason is the one this row gave: refusing is smaller AND cannot produce a wrong verdict in EITHER direction, so it closes the quiet FALSE-VALID case that neither seat had constructed. ⭐ NAMING AN UNEXERCISED DIRECTION HONESTLY IS WHAT MADE THE CHEAPER FIX THE CORRECT ONE -- had Z-S10 asserted only the observed false-INVALID, the resolving form would have looked sufficient. || THE ROOT CAUSE IS ONE LINE NARROWER THAN THIS ROW STATED, traced at source by that seat: :294 `relative_to(_REPO_ROOT)` RAISES for a worktree instance and :295 SWALLOWS the ValueError to `inst_rel = None`, so `inst_commit` stays None and the git fallback at :327 CANNOT EVEN RUN. ⛔ THE SWALLOW WAS THE DEFECT, NOT THE RESOLUTION MODEL: the checker converted 'I cannot see this tree' into 'your artifact is broken'. It now returns CHECKER-SCOPE naming both trees and stating it is not a finding against the instance or its author. Exercised both arms, 12 of 12 self-test. || ⚠ NOT RETROACTIVE AND NOT ON THE OTHER FABRIC UNTIL IT PULLS -- a CLOUD-side main-tree drain still produces the false INVALID. Same class as the corpus_root() repair at @6228c53377 in comp-find/comp-read/comp-pulse, which this tool never received."
      ]
    },
    "spec_asserts": "The drain grades a worker's proof instance by running .tools/proof-of-spec-check.py against it, and the VALID/INVALID verdict is a property of the instance.",
    "world_is": "The verdict is a property of the PAIR (instance, tree-the-script-lives-in), and spine v3 guarantees those two differ for every worker.",
    "notes": "NOT THIS PROJECT'S TO FIX and the row says so. Recorded here because a drain-path instrument that mis-attributes to workers will recur on every v3 round until the source changes, and because this project's round-2 drain already spent a wrong verdict on it."
  }
]
```

## C-S8 -- Z-S11: two of IAM-r-6's four mechanical bars CANNOT FAIL; one `-i` flag is the whole distance between 'measured 0' and 'reads 3'. Disarm accepted and left ARMED until that L9

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S8",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T14:32Z",
    "one_line": "Z-S11 GRADUATES AND ITS DISARM IS MINE AND STAYS ARMED. The issuing lane filed against its OWN frozen issuance: two of IAM-r-6's four mechanical bars CANNOT FAIL, and AC1's 'measured 0 at the cut' is true only of an instrument that was NOT the one shipped -- the hand-measurement omitted the `-i` the criterion carries. ⛔ I ACCEPT THE ASK: AC1 AND AC3 WILL NOT BE CREDITED AT L9, and the disarm cannot discharge until that L9 happens.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "3.0.0_SA_CVO~Z -- MINE, AND DELIBERATELY LEFT ARMED. The disarm condition is a GRADING ACT AT A ROUND THAT HAS NOT BEEN DRAINED: IAM-r-6 is a round-2 cell and its L9 does not exist yet. ⛔ A DISARM RECORDED NOW WOULD CERTIFY A GRADE NOBODY HAS MADE. It discharges when this seat grades IAM-r-6 and records, in that L9 row, that AC1 and AC3 carried no evidential weight and that the substance was graded from the deliverable and AC5 instead.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-S11"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** RE-DERIVED AT THIS SEAT ON THE COMMITTED OBJECT AT THE CUT VINTAGE, one flag apart. *** `git show cccb4fac83:.../0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md` piped to `grep -c -E 'RETIRE'` returns **0**; the same bytes to `grep -c -i -E 'RETIRE'` return **3**. The criterion as shipped carries `-i`. ⛔ THE ENTIRE DISTANCE BETWEEN 'MEASURED 0' AND 'READS 3' IS ONE FLAG.",
        "AND THE THREE TOKENS ARE ALL LOWERCASE, which is exactly why a case-sensitive read returns a CLEAN zero rather than a suspicious one: `retired`, `retirement`, `retire`. There is no uppercase RETIRE in the document at any vintage. A clean 0 from a broken instrument looks identical to a clean 0 from a true absence -- the estate's own banked shape, here deciding a bar.",
        "⚠ ONE PRECISION NOTE THAT STRENGTHENS THE ROW RATHER THAN QUALIFYING IT. The row cites the tokens at `:106`, `:291`, `:349`; at the CUT COMMIT this seat reads them at `:90`, `:171`, `:227`. Both are correct -- the row's line numbers are HEAD's, the cut's are lower. THE COUNT IS IDENTICAL AT BOTH VINTAGES (0 sensitive / 3 insensitive), which is the row's own EV3 point measured a second way, so the citation carries a vintage its line numbers do not. Rule 22: a citation without a vintage is not a citation, and this one needed the vintage named.",
        "⭐ AC3 IS THE PLAINER DEFECT AND THE MORE DANGEROUS SHAPE. `grep -c -E 'lambda-test-role'` reads 3 at the cut and 4 at HEAD against an expect of '1 or greater'. `lambda-test-role` has been row 7 of the disposition SINCE ROUND 1. ⛔ A WORKER THAT DID NOTHING AT ALL WOULD PASS IT. There is no case story and no measurement error here -- the bar simply never discriminated, and a criterion that cannot fail is indistinguishable at L9 from a criterion that was met.",
        "THE CONTRAST THAT KEEPS THIS FROM BECOMING A CHARGE AGAINST THE WHOLE ISSUANCE, and the row supplies it: IAM-r-4's four cut notes were re-measured at the SAME vintage and ALL FOUR ARE ACCURATE (0, 0, 0, 0, exactly as its expect fields state). The issuance's blanket claim that every criterion was measured against the world is NOT uniformly false -- two criteria in one order are. ⭐ A ROW THAT MEASURES ITS OWN BLAST RADIUS AND FINDS IT SMALL IS DOING THE HARDER HALF OF SELF-REPORTING.",
        "THE REUSABLE SHAPE IS THE ROW'S OWN AND IT IS THE PART WORTH CARRYING: MEASURE A CRITERION BY RUNNING THE EXACT INVOCATION STRING YOU ARE ABOUT TO SHIP, NEVER A HAND-TYPED NEAR-EQUIVALENT. ⛔ AND THE FAILURE DIRECTION IS ASYMMETRIC, WHICH IS WHY IT SURVIVES: a hand-measurement error that makes a bar ALWAYS FAIL is caught immediately by the executor, who cannot pass it. One that makes a bar ALWAYS PASS IS CAUGHT BY NOBODY -- not the worker (it passes), not the gate (it is well-formed), not the grader (a PASS is what a PASS looks like). A pre-cut harness executing each criterion's own `<invocation>` against the tree and recording the number beside it would have refused both bars mechanically.",
        "SCOPE, AND WHAT IS NOT AT RISK: the spec is FROZEN mid-round so AC1 and AC3 are NOT amended -- this row is the carrier, exactly as Z-S9 carried the frozen battery block, and that is the correct handling rather than an issuer editing its own criterion to make it honest. IAM-r-6's SUBSTANTIVE direction is untouched and neither bar gates it: add the RETIRE value without overloading EXEMPT, carry the rule-24 four-postulate record and token census, hunt the uncovered member against the policy-attached-but-undeclared state, then dispose `lambda-test-role`. AC2, AC4 and the CVO-graded AC5 remain real bars -- AC2 reads 0 at the cut AND 0 at HEAD, so it genuinely discriminates."
      ]
    },
    "spec_asserts": "The round-2 issuance commit cccb4fac83 states every criterion was measured against the world before it was written, and IAM-r-6's AC1 expect states 'measured 0 at the cut' so only a real extension moves it.",
    "world_is": "AC1 was satisfied by the document as it stood BEFORE the cell ran and cannot fail; its 'measured 0' is true only of a case-sensitive instrument that was not the one shipped. AC3 never discriminated at all.",
    "notes": "⛔ THIS ROW ALSO CONVERGES WITH C-S6 AND WITH 1.0.0_SA_CTO~Z's ROUND-1 ANALYSIS ON THE SAME SCHEMA, FROM A THIRD DIRECTION. IAM-r-6 exists to add a RETIRE value because the binary IN-CODE/EXEMPT axis cannot express retirement (the CTO's reading); C-S6 showed the same axis cannot express PARTIAL OWNERSHIP (Z-S8's policy-attached-but-undeclared member); and this row shows the CELL COMMISSIONED TO FIX IT shipped two bars that cannot fail. ⭐ THREE INDEPENDENT ARMS ON ONE TAXONOMY IN ONE DAY -- and it strengthens C-S6's finding that this seat's round-1 remedy (split the IN-CODE token) was too narrow. || THE ASK IS ACCEPTED IN THE FORM IT WAS MADE, WITHOUT WIDENING IT: not credited does NOT mean graded FAIL. A criterion that cannot discriminate produces NO EVIDENCE in either direction; grading it FAIL would penalise a worker for a bar its issuer wrote, which is the same error the OPSEC round-3 S1-AC4 void was granted to avoid."
  }
]
```

## C-S9 -- the three IAM-r-5 worker rows: a SET whose label asserts what one member lacks, a CRITERION that scores THE TOOL'S vocabulary with the sign INVERTED, and a WRITE SURFACE that is the wrong custody home

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S9",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:12Z",
    "one_line": "ALL THREE IAM-r-5 WORKER ROWS GRADUATE, AND THEY ARE ONE AXIS AT THREE GRAINS: a SET whose shared label asserts a property one member does not have, a CRITERION that scores the TOOL'S vocabulary instead of the worker's conduct, and a WRITE SURFACE that is the wrong custody home for one of the two roles it must serve. ⭐ ALL THREE ARE FILED IN THE DIRECTION THAT RELAXES NOTHING -- each makes the cell SAFER than its own framing -- which is why all three are correctly INERT with no disarm owner.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE, AND CORRECTLY SO ON ALL THREE. Each row names a defect in a SPEC, a CRITERION or a GRANT rather than in the world, each was worked around without weakening evidence, and none leaves a live hazard. Z-W6-S3's remedy is explicitly a proof-of-spec SCHEMA call and not a project one; Z-W6-S4's placement question belongs to whoever holds the portal auth surface; Z-W6-S2 is a measurement offered to IAM-s-6's residue call and expressly not a recommendation.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-W6-S2",
      "NFRA_IAMROLES202609-Z-W6-S3",
      "NFRA_IAMROLES202609-Z-W6-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** Z-W6-S2 IS A TEXTUAL INSTANCE OF THE ESTATE'S OWN LAW, DERIVED FROM SCRATCH AND WITHOUT CITING IT. *** CLAUDE.md rule 22 carries: 'A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE ... Ask what the members have in COMMON, and check THAT on its own.' The row's own formulation: 'A SET ASSEMBLED BY A SHARED LABEL CAN HAVE MEMBERS THAT DO NOT SHARE THE PROPERTY THE LABEL ASSERTS, and every per-member check still passes because each member is individually fine.' ⛔ THAT IS THE SAME LAW IN DIFFERENT WORDS, AND THE WORKER DID NOT CITE IT -- which is itself the finding worth carrying upward: a worker face is the worker's WHOLE CONTEXT, so a law the estate depends on either reached it and went unrecognised, or never reached it at all. The remedy for that is an issuance-template question, not this cell's.",
        "AND ITS MEASUREMENT IS THREE INSTRUMENTS ON THREE PLANES WITH A POSITIVE CONTROL ON EACH, which is why it graduates without re-derivation here: `RoleLastUsed` is an EMPTY OBJECT for portal-auth-lambda-role against a populated `LastUsedDate` on the sibling; `lambda list-functions` filtered on the role ARN returns `[]` ACROSS A PRINTED DENOMINATOR OF 203 FUNCTIONS against 3 for the sibling; and `comp-blast` over a 27,662-node served projection returns 423 callers of which ZERO carry `[LAMBDA]` against three at depth 1 for the sibling. ⭐ THEN IT CLOSES THE REMAINING DOOR RATHER THAN LEAVING A GAP: the live trust policy admits ONLY `lambda.amazonaws.com`, so a zero over Lambda functions is a zero over ALL POSSIBLE PRINCIPALS. That last step is what converts three consistent absences into an exhaustive one.",
        "*** Z-W6-S3 IS THE SHARPEST OF THE THREE AND ITS SIGN IS INVERTED, WHICH IS WORSE THAN THE DEFECT IT LOOKS LIKE. *** AC5 forbids the string `terraform apply` in the deliverable to evidence that nothing was applied; the bound requires the plan output QUOTED VERBATIM; and Terraform emits `terraform apply` in its own footer in BOTH stdout forms -- the no-`-out` note and the `-out` 'to perform exactly these actions' line. ⛔ SO THE FOOTER SAYING AN APPLY WAS **NOT** PERFORMED IS SCORED AS EVIDENCE THAT ONE **WAS**. Evidence FOR the criterion's stated intent, read as evidence against it. A negative keyword criterion over a deliverable required to contain quoted tool output SCORES THE TOOL'S VOCABULARY, NOT THE WORKER'S CONDUCT -- the regex cannot see who authored the string.",
        "⛔ AND IT IS THE OPPOSITE SIGN TO C-S8'S DEFECT, WHICH IS WHY BOTH BELONG IN THE RECORD. Z-S11's AC1/AC3 CANNOT FAIL -- they pass for a worker that did nothing. AC5 here FAILS ON CORRECT CONDUCT -- it punishes a worker that quotes honestly and completely. A bar that cannot fail wastes evidence; A BAR THAT FAILS ON HONESTY MANUFACTURES PRESSURE TO TRIM IT, and the row names that branch explicitly ('a worker that chases the green count is pushed toward trimming its evidence'). ⭐ THIS WORKER TOOK NEITHER BRANCH: it rendered `terraform show` of the SAVED PLAN FROM THE SAME RUN and PROVED completeness with a `diff` of the region from 'Terraform used the selected providers' through the 'Plan:' line against raw stdout -- EMPTY, byte-identical, 203 lines vs 229, the 26-line delta being exactly refresh chatter and the footer. It also verified the save mutated nothing: the remote state object still reads LastModified 2026-08-03, 38 days prior.",
        "Z-W6-S4 SEPARATES WHAT TRANSFERS FROM WHAT DOES NOT, WHICH IS THE PART A CLEAN PLAN WOULD OTHERWISE HIDE. The plan proves ADOPTION MECHANICS ARE NON-DESTRUCTIVE -- an existing role is imported rather than recreated, and omitting `inline_policy` / `managed_policy_arns` leaves live attachments untouched -- and THAT conclusion transfers to any module. What does NOT transfer is module-scoped: the `state key` (`data-refresh/tfstate`, which would file a portal-auth object where nobody would look for it) and `tags_all` (the module's provider stamps Project=OpalPortal / Environment=Production, visible in the plan as a `~ tags_all` on both roles). ⭐ A WORKER THAT REPORTS THE SCOPE LIMIT OF ITS OWN CLEAN RESULT is doing the thing a clean result most discourages.",
        "⚠ AND A CORRECTION TO THIS SEAT'S OWN C-S6, SURFACED BY Z-W6-S4 AND VERIFIED HERE. C-S6 stated 'Terraform owns FOUR inline policies on a role it does not declare.' THE FOUR WAS `main.tf`-SCOPED AND I DID NOT SAY SO. Module-wide the count is FIVE: `main.tf` 4 (:58, :80, :99, :138) plus `qa-scratch-instance.tf` 1 (:36). ⭐ THE FINDING ITSELF HOLDS AND IS NOW MEASURED AT THE RIGHT DENOMINATOR -- an exhaustive per-file sweep of the module's ONLY two .tf files returns `aws_iam_role` declarations 0 and 0. So Terraform owns FIVE policies on a role it declares nowhere in the module. Rule 22 COVERAGE: the number was right for the file I read and the claim was about the ROLE, and I did not print the scope that separates them.",
        "SCOPE, AND WHY NONE OF THE THREE IS BLOCKING: all three rows state that the cell was COMPLETED IN FULL and that no surface was blocked and nothing withheld. Z-W6-S2 explicitly respects C-TWO-REMEDIES by recording the usage state and declining to recommend narrowing, deleting or moving the role -- that is the governance axis, and IAM-r-6 is where it belongs."
      ]
    },
    "spec_asserts": "IAM-r-5's DOUBLE-STOP asserts both roles 'EXIST AND SERVE PRODUCTION TRAFFIC RIGHT NOW'; its BOUNDS require the plan quoted VERBATIM; and its PATHS grant one module as a sufficient write surface for proposing declarations of both roles.",
    "world_is": "One of the two roles has never been used in 203 days and has no consumer among 203 live functions; a verbatim plan quote fails AC5 by construction because Terraform authors the forbidden token itself; and the one granted module is the wrong custody home for that same role.",
    "notes": "⭐ THE THREE ROWS SHARE A SHAPE AND IT IS THE ONE THIS ESTATE MEETS MOST OFTEN: A CONFIDENT, WELL-FORMED ASSERTION ABOUT THE WRONG OBJECT. The label asserts a property of a SET whose members differ on it; the regex asserts conduct by scoring a DOCUMENT'S CHARACTERS; the grant asserts sufficiency of a WRITE SURFACE by counting modules rather than asking whose system each role belongs to. ⛔ AND ALL THREE WERE INVISIBLE FROM INSIDE THE CELL'S OWN EVIDENCE -- every per-member check passed, the deliverable was complete, and the plan was clean. They surface only by asking what the spec ASSERTED versus what the world IS, which is precisely what the surprise channel is for and precisely what a green proof instance cannot show. || NOTHING IS ASKED OF ANY LANE BY THIS ROW. Z-W6-S3's remedy (scope a negative keyword criterion to the worker's own prose by excluding fenced blocks, or assert the negative on the WORLD -- the state object's LastModified, which actually discriminates -- rather than on the document's characters) is a proof-of-spec SCHEMA question and is recorded here so it reaches whoever holds that schema."
  }
]
```

## C-S10 -- the two IAM-r-6 worker rows: a second independent arrival at C-S8's defect that SUPPLIES THE MISSING GRADING INSTRUMENT, and an independent confirmation of C-S9's 'five, not four' that adds a THIRD count

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S10",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:24Z",
    "one_line": "BOTH GRADUATE, AND EACH ARRIVES INDEPENDENTLY AT A FINDING THIS SEAT MADE SEPARATELY TODAY -- from the WORKER side, on different instruments. ⭐ Z-W5-S1 SUPPLIES WHAT C-S8 COULD NOT: the DISCRIMINATING measurement to grade AC1 by, converting this seat's negative commitment (do not credit AC1) into a positive grading path. And Z-W5-S2 reaches the SAME 'five, not four' this seat published at C-S9 -- while adding a THIRD number, so one state has now been counted 3, 4 and 5 by three cells.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "PER-ROW AND UNCHANGED. Z-W5-S1's is 2.0.0_SA_COO~ZI -- criteria are cut at L6 and the remaining exposure is the CUTTING PATTERN, not this cell; Z-W5-S2 is INERT and names no owner, correctly. ⭐ AND THE SPLIT BETWEEN Z-W5-S1 AND Z-S11 IS EXACTLY RIGHT THOUGH THEY NAME THE SAME CRITERION: Z-S11 routed the GRADING limb to 3.0.0_SA_CVO~Z (do not credit AC1 at L9) and Z-W5-S1 routes the ISSUANCE limb to the lane that cuts criteria. One defect, two limbs, two owners, neither duplicating the other.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-W5-S1",
      "NFRA_IAMROLES202609-Z-W5-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** Z-W5-S1 IS THE SECOND INDEPENDENT ARRIVAL AT C-S8'S DEFECT, FROM THE OPPOSITE SIDE, AND IT IS CORROBORATION RATHER THAN REPETITION. *** C-S8 reached it from the ISSUER's row (Z-S11) and re-derived it at the CUT COMMIT with `git show cccb4fac83`. Z-W5-S1 reached it by running the criterion's own verbatim invocation IN ITS OWN WORKTREE BEFORE EDITING ANYTHING (`/c/tmp/wk-iamroles-5` @772c796a3f), printing 3 against the expect clause's cited 'measured 0 at the cut'. Two seats, two planes, two vintages, same answer. ⭐ AND THE WORKER'S FIRST ACT IS THE HABIT THAT FOUND IT: it re-grounded the baseline before editing rather than inheriting the cut's cited 0, which is the estate's 'run the criterion against the world before handing it over' executed from the receiving end.",
        "*** AND IT SUPPLIES THE THING C-S8 EXPLICITLY COULD NOT. *** C-S8 committed this seat to a NEGATIVE -- AC1 and AC3 will not be credited -- and said the substance must be graded 'from the deliverable and from AC5', without naming the instrument. Z-W5-S1 names it: a WORD-BOUNDARY, CASE-SENSITIVE PER-TOKEN census over the same 350-line file reading RETIRE 0, RETIRED 0, RETIREMENT 0 before the cell's edit, against DECLARED 23 / ADOPT 24 / EXEMPT 10. ⛔ THAT is the measurement the TO's own rule-24 clause asks for and it IS the number the cell moved. THIS SEAT ADOPTS IT AS THE GRADING PATH FOR AC1 AT L9: grade the case-SENSITIVE per-token census recorded in the artifact and the proof instance, never AC1's own case-insensitive count. A negative commitment with no substitute instrument is an invitation to grade nothing.",
        "ITS NEGATIVE CONTROL CONFINES THE DEFECT AND KEEPS IT FROM BECOMING A CHARGE AGAINST THE TOOL: sibling criterion AC2 -- same `-i`, same file, same pre-edit baseline -- measured 0 and therefore DOES discriminate. So the defect is specific to AC1's bare word-stem meeting a word the document already used in prose, not to grep and not to the cut's instrument generally. ⭐ AND A SECOND INSTANCE IS NAMED IN THE SAME ROUND: IAM-r-1's proof instance records its AC2 baseline re-measuring 12 against a cited 13. TWO CELLS, SO THIS IS A CUTTING PATTERN AND NOT ONE MIS-TYPED NUMBER -- which is precisely why the disarm sits with the issuing lane.",
        "⚠ AND THE EXPOSURE IS THE READING, NOT THE WORK -- a distinction this row preserves because losing it would penalise a worker who did everything asked. The cell did the substantive work regardless: the fourth value is defined, the four-postulate record and token census are written, the member is disposed, and AC1 now reads 33. The hazard is that a grader reads AC1's PASS as evidence of the extension WHEN THAT OUTPUT PREDATES THE CELL. A cell that changed nothing would have printed the same PASS-shaped output.",
        "*** Z-W5-S2 INDEPENDENTLY REACHES THE CORRECTION THIS SEAT PUBLISHED AT C-S9, AND BY A DIFFERENT INSTRUMENT. *** This seat corrected C-S6's 'FOUR inline policies' to FIVE at C-S9 via an exhaustive per-file sweep of the module's only two .tf files. Z-W5-S2 reached FIVE at 14:05Z via `comp-find 'opal-data-refresh-lambda-role' infra/aws/terraform --all` -> 9 hits across a PRINTED denominator of 516 files, of which five are `role = ...` attachment lines, EACH READ AT SOURCE so an attachment and a mention cannot read alike. ⭐ NEITHER SEAT COULD SEE THE OTHER -- that row was surfaced at 14:05Z and reached the index only at its drain, after C-S9 was written. Same number, two instruments, no contact.",
        "⛔ AND IT ADDS THE THIRD NUMBER, WHICH IS THE PART NEITHER THIS SEAT NOR THE CUT HAD: round 1's GOVERNANCE_DISPOSITION.md row 8 says 'THREE aws_iam_role_policy attachments'. So ONE STATE HAS BEEN COUNTED 3, 4 AND 5 BY THREE DIFFERENT CELLS OF ONE PROJECT, and this seat produced the 4. THE ROW'S DIAGNOSIS IS EXACT AND GENERALISES: 'a per-member count taken from the file where the member obviously lives is not a tree-wide count, AND THE TWO RENDER IDENTICALLY IN A BATTERY BLOCK.' Nothing in the number's presentation carries its scope, which is why three cells disagreed without any of them being careless.",
        "AND BOTH ROWS PROTECT THE FINDING THE COUNT SITS ON, WHICH IS WHY NEITHER IS BLOCKING: the zero-declarations half reproduced EXACTLY on Z-W5-S2's own instrument -- `comp-find 'resource \"aws_iam_role\"' infra/aws/terraform/data-refresh --all` -> 0 hits across a 4-file denominator. ⭐ SO THE MAGNITUDE MOVED AND THE STATE DID NOT: Terraform genuinely manages policies on a role it does not declare, which is C-S6's finding and IAM-r-6's decision input, and NO DISPOSITION TURNS ON WHETHER IT IS FOUR OR FIVE. The row says so itself and is right to mark itself INERT."
      ]
    },
    "spec_asserts": "IAM-r-6's AC1 expect cites a baseline of 0 at the cut so 'only a real extension moves it'; and its BATTERY FINDINGS block states Terraform carries FOUR aws_iam_role_policy blocks attaching to opal-data-refresh-lambda-role by name.",
    "world_is": "AC1's own verbatim invocation returned 3 before any edit, so a cell that did nothing would have passed it; and a whole-tree re-measurement returns FIVE attachments, not four, with round 1 having recorded three.",
    "notes": "⭐ FOUR SEATS REACHED PARTS OF ONE DEFECT TODAY WITHOUT COORDINATING, AND THE OVERLAP IS THE EVIDENCE THAT IT IS STRUCTURAL RATHER THAN ANECDOTAL: the issuing lane (Z-S11, against its own frozen issuance), a worker (Z-W5-S1, from its pre-edit baseline), this seat (C-S8, at the cut vintage), and a second worker plus this seat converging on the policy count (Z-W5-S2 and C-S9). ⛔ NONE OF THEM FOUND IT BY RE-READING A DELIVERABLE. Every one found it by RUNNING AN INVOCATION AND COMPARING THE NUMBER TO WHAT THE DOCUMENT CLAIMED -- which is the one act a green proof instance never performs on itself. || THE FROZEN-SPEC HANDLING IS CORRECT AND IS NOT DISTURBED: the round-2 decomposition and its task orders are frozen mid-round and are NOT retro-amended; these rows are the carrier, exactly as Z-S9 carried the frozen battery block and Z-S11 carried AC1. The whole-tree figure of record is FIVE."
  }
]
```

## C-S11 -- L8 COMPILE, ROUND 2: 6 of 6 terminal, 31 criteria, and the ONE RESIDUE THE ROUND COULD NOT CLOSE ITSELF closed from the main tree -- the set is EXACTLY 15

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S11",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:40Z",
    "one_line": "L8 COMPILE, ROUND 2 -- 6 of 6 terminal, 6 instances for 6 orders, 31 criteria, 25 PASS and 6 UNVERIFIABLE-BY-INSTRUMENT which are EXACTLY the six judgment criteria. ⭐ AND THIS COMPILE CLOSES THE ONE RESIDUE THE ROUND COULD NOT CLOSE ITSELF: IAM-r-3 named, as the single uncertainty it could not settle, that its clean worktree cannot see the shared checkout's UNTRACKED .tf files -- so a member might be declared in one. IT IS NOT. All four untracked `aws_iam_role` blocks mint NEW roles and none is a member. THE SET IS EXACTLY 15.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "AN L8 COMPILE RECORD. It adjudicates no investigation item and opens nothing; its content is the round's measured state plus one residue closed at this seat. The round's items were dispositioned as they arrived at C-S5 through C-S10 -- this round's channel work was done AS the peers filed it rather than in one pass at the end, so the compile finds 0 open rather than a docket.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** MEASURED AT THIS SEAT, NOT TAKEN FROM THE DRAIN-END READ. *** 6 of 6 task orders read `complete` from their own `<status>` fields; SIX proof instances for SIX orders with SIX distinct `to_id`s -- ⭐ NO DUPLICATES THIS ROUND, unlike round 1 where ELEVEN instance FILES served NINE orders and a file-keyed census would have graded two criteria twice (C-S1). A file count and a `to_id` count agree here and that agreement is itself the check. `COMPLETION_REPORT.round2.json` present at HEAD, 10,353 bytes.",
        "CRITERIA CENSUS WITH ITS DENOMINATOR AND BOTH JUDGMENT CARRIERS: 31 criteria across the six instances -- 25 PASS, 6 UNVERIFIABLE-BY-INSTRUMENT, 0 FAIL. The six UNVERIFIABLE are EXACTLY the six judgment criteria, one per order (IAM-r-1/2/3/4/6 AC5, IAM-r-5 AC6), each carrying a `status_reason` naming 3.0.0_SA_CVO~Z and each explicitly declining to self-grade. ⚠ AND THE TWO-KEY CENSUS EARNED ITS KEEP AGAIN, IN THE OPPOSITE DIRECTION FROM LAST TIME: the `judgment` FIELD caught all six and the VERBATIM-TEXT prefix caught ZERO, because the text reads `AC5 (JUDGMENT -- ...` rather than opening with the token. On NFRA_OPSEC202609 the field returned zero and the text carried it. Neither carrier is reliable alone and the estate has now been bitten in both directions.",
        "*** THE RESIDUE IAM-r-3 NAMED AND COULD NOT CLOSE, CLOSED HERE, AND IT DECIDES THE ROUND'S HEADLINE. *** That cell measured membership over 415 TRACKED .tf files and stated its one genuine uncertainty plainly: its worktree does not contain the untracked .tf files present in the shared main checkout, so a member could in principle be declared in one of them. ⛔ A WORKER CANNOT CLOSE THIS BY CONSTRUCTION -- rule 14b and /dispatch mandate a clean linked worktree, which is exactly what makes untracked files in the shared tree invisible to it. Measured from the MAIN TREE at this seat: `git ls-files --others --exclude-standard -- '*.tf'` yields four `aws_iam_role` blocks, and each block's `name` argument resolves to `opal-globgrph-freshness-alarm`, `opal-globgrph-freeze-monitor`, `opal-globgrph-tool-activity-freshness` and `inf-gold-freshness-guard-lambda-role`. ALL FOUR MINT NEW ROLES; NONE APPEARS IN `MEMBERSHIP_PER_MEMBER.md` (checked by literal name, all four absent). THE 15 STANDS.",
        "⭐ THAT CLOSE IS THE SHARED-CHECKOUT FINDING PAYING OFF RATHER THAN BITING. C-S5 established that a figure taken from the shared tree measures a MOMENT and not a VINTAGE, and that an issuer and a worker cannot agree in principle because the worker's tree is clean by construction. Here the SAME asymmetry is used deliberately: the worker measured the committed plane correctly and named what its plane could not see, and a seat WITH main-tree visibility answered exactly that question. THE ASYMMETRY IS ONLY A DEFECT WHEN IT IS UNDECLARED -- declared, it is a division of labour, and this round is the first time this session it worked that way round.",
        "THE ROUND'S SUBSTANTIVE RESULT, VERIFIED WHERE IT WAS CHEAP TO VERIFY: the settled set of 16 is exactly 15 NOT-IN-TF plus 1 DECLARED (`seeking-alpha-scraper-role`, cited at `infra/aws/terraform/seeking-alpha/main.tf:240-241`) -- the confirmed false positive C-S2 and Z-S6 bounded at 'AT MOST 15' is now EXACTLY 15, and the bound is discharged by measurement rather than by assertion. Adoption is proved non-destructive: `Plan: 2 to import, 0 to add, 2 to change, 0 to destroy`, with a BASELINE plan taken FIRST reading `No changes` so the delta is attributable to the change alone.",
        "⛔ AND THE LOAD-BEARING SAFETY DETAIL IS ONE THE ROUND FOUND RATHER THAN INHERITED: `inline_policy` and `managed_policy_arns` are Optional+Computed, so SET-rather-than-OMITTED they become AUTHORITATIVE and DETACH whatever is not listed. On a role carrying five live inline policies on a serving path that is precisely the C-NO-ACCESSDENIED outage. Both declarations OMIT both deliberately. That is the difference between a plan that is quiet because it is right and one that is quiet on the way to an outage, and it is the reason IAM-r-5's AC6 is gradeable at all."
      ]
    },
    "spec_asserts": "IAM-r-3's deliverable states its membership verdicts are established on the source plane over 415 tracked .tf files, with one uncertainty it could not close.",
    "world_is": "The uncertainty is closed from the main tree: all four untracked aws_iam_role blocks mint new roles and none is a member, so the set is exactly 15.",
    "notes": "⭐ THIS ROUND'S CHANNEL WORK WAS DONE AS IT ARRIVED, NOT AT THE END. Its eight items were dispositioned at C-S5 through C-S10 as peers and workers filed them across the drain, so this compile opens on a channel already at 0 open. That is the opposite of round 1, which reached L7-complete with 18 items ALL undispositioned and no L8 packet ever sent (C-S1). || NO SLUG IS CUT BY THIS ROW. L10 needs the judgment grades, which land at C-S12."
  }
]
```

## C-S12 -- L9 ROUND 2: all SIX judgment criteria PASS, the round-1 FAIL is REPAIRED, and this seat's own C-S6 remedy is NARROWED by the cell that tested it

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S12",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:40Z",
    "one_line": "L9 ROUND 2: ALL SIX JUDGMENT CRITERIA PASS -- and the round REPAIRED the exact defect this seat FAILED it on in round 1. ⛔ AND THE ROUND ANSWERED THIS SEAT'S OWN C-S6 WITH A MEASUREMENT AND DECLINED ITS REMEDY, CORRECTLY: IAM-r-6 refused a fourth value because five of the six policy-attached roles are THEMSELVES DECLARED, so the value would classify declared and undeclared identically. C-S6's MECE observation survives; C-S6's implied remedy does not.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A GRADE RECORD, per the `grades` field's contract: it carries the six verdicts and adjudicates no item.",
    "grades": [
      {
        "criterion": "IAMr1-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~5/NFRA_IAMROLES202609.TO-IAM-r-1.token-split-declared-vs-adopt.proof_of_spec.json@1b65eb60d922",
        "verdict": "PASS",
        "reason": "⭐ THIS IS THE REPAIR OF THE EXACT DEFECT THIS SEAT FAILED IN ROUND 1, AND IT IS CLEAN. C-S4 failed IAMs6-AC5 because `IN-CODE` was defined as 'a FACT, not a recommendation' and then applied to EIGHT members the same document measured as ABSENT -- rule 24(iii), one axis carrying two intents. The replacement separates them by NAME: `DECLARED` (a fact: an `aws_iam_role` block exists, cited by path) and `ADOPT` (a recommendation: not yet declared). The coverage line now states the true state in words a governance reader cannot misread -- 'ONE of sixteen roles is presently declared in this repo's Terraform' -- and every ADOPT row's own prose says the member is absent from Terraform source. The single DECLARED row cites its resource block at `infra/aws/terraform/seeking-alpha/main.tf:240-241`. NO TOKEN NOW IMPLIES A RECOMMENDATION IS AN ACCOMPLISHED FACT, which is the whole of what the criterion asks. ⚠ ONE BOUND THE PASS CARRIES AND DOES NOT HIDE: row 8 (`opal-data-refresh-lambda-role`) reads `EXEMPT owner=UNASSIGNED` while its own prose says 'the decision owed is an explicit sign-off (adopt via import, or formally except)'. EXEMPT is defined as deliberately-outside-and-it-stays; a decision still owed is not that. The row is honest and the `UNASSIGNED` owner is doing the work the value cannot -- see the C-S6 note below. That is a residue of the AXIS, not a defect in THIS cell's repair, and it does not reach AC5's question."
      },
      {
        "criterion": "IAMr2-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/NFRA_IAMROLES202609.TO-IAM-r-2.what-do-191-208-216-each-count.proof_of_spec.json@7d7099f4cf94",
        "verdict": "PASS",
        "reason": "THE BAR ALLOWS TWO HONEST ANSWERS AND REFUSES ONE DISHONEST ONE -- 'an unexamined shrug is not' a pass -- and this deliverable gives the grounded version of BOTH. It establishes that 208/216/219 are ONE INSTRUMENT FAMILY read at three successive vintages (comp-iam live and comp-find --corpus aws both naming kuzu_nessie_db as provenance, confirmed by a side-by-side run returning byte-identical figures from both entry points), with LIVE-no-DECLARED stable at 16 throughout -- a reconciliation, not a preference. It then states that 191 is a STRUCTURALLY DIFFERENT POPULATION (Terraform-declared blocks, not live ARNs, not for_each-expanded) and DECLINES to compute a reconciling arithmetic, naming that as IAM-r-3's per-member mandate rather than inventing a number. ⭐ DECLINING TO PRODUCE A NUMBER IT COULD HAVE FABRICATED IS THE STRONGEST THING IN THIS CELL, and it is exactly what round 1's C-S2 said the PRD should have done with 191/208/216. And it reports that the decomposition's own '195' did NOT reproduce, setting it aside rather than folding it into either story -- the finding that became Z-W6-S1/Z-S9. Every irreconcilability claim carries its specific mechanism or its specific reproduction attempt."
      },
      {
        "criterion": "IAMr3-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/NFRA_IAMROLES202609.TO-IAM-r-3.true-membership-per-member-resource-block.proof_of_spec.json@b077f10538b9",
        "verdict": "PASS",
        "reason": "⭐ THIS CELL DID THE ONE THING THIS SEAT'S ROUND-1 ANALYSIS AND THE CTO'S R2-B BOTH DEMANDED: a per-member read against A PLANE THAT DID NOT BUILD THE SET. All 16 verdicts are re-derived by literal-string search of the committed Terraform tree (415 tracked .tf files, worktree clean), distinct from the comp-find/comp-iam live-graph instrument that assembled the set under test -- which is the direct remedy for Z-S6's 'a stable count across three vintages is consistent with a stable MISCLASSIFICATION'. Both named controls were REPRODUCED INDEPENDENTLY rather than copied from the TO: the positive (`seeking-alpha-scraper-role`) reads DECLARED-IN-TF, the negative (`opal-data-refresh-lambda-role`) reads NOT-IN-TF DESPITE NINE HITS -- and distinguishing a nonzero-but-all-references case from true silence is precisely the discrimination a name-match census cannot make (C-S6's 'A NAME MATCH IN TERRAFORM IS NOT A DECLARATION'). ⭐ AND THE UNCERTAINTY CLAUSE IS ANSWERED IN THE DIRECTION THE CRITERION WANTS: the one member it could not settle is STATED, not resolved by preference -- and this seat CLOSED it at C-S11 from the main tree. A cell that names the question its own plane cannot answer is why that close was a five-minute act instead of a re-run of the round."
      },
      {
        "criterion": "IAMr4-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~5/NFRA_IAMROLES202609.TO-IAM-r-4.record-the-service-default-class-ruling.proof_of_spec.json@b1fececea1eb",
        "verdict": "PASS",
        "reason": "THE CRITERION ASKS FOR A DECISION RATHER THAN A GAP DRESSED AS AN EXEMPTION, PLUS A BOUNDARY A READER CAN APPLY, AND BOTH ARE THERE. The three rows name the DECIDER (`1.0.0_SA_CTO~Z`), the REASONING (a service-minted role is owned by the issuing service's own lifecycle; adopting it would fight that lifecycle rather than describe infrastructure this estate built), and a CLASS BOUNDARY as three JOINT conditions -- absent from Terraform by name-level check, carries AWS's own conventional default-role name for a specific service, not created by this estate's Terraform. ⭐ AND IT CARRIES NEGATIVE EXAMPLES, WHICH IS WHAT MAKES A BOUNDARY USABLE RATHER THAN DECORATIVE: it names which members the ruling does NOT reach (`opal-data-refresh-lambda-role`, `portal-auth-lambda-role`, `lambda-test-role`, the nine ADOPT members), so a later reader places a new role against the boundary instead of guessing. Rule 24(iv), STATE COHERENCE: it says which values this one remedy does not move. ⚠ THE DISCLOSED WEAKNESS AND WHY IT DOES NOT BLOCK: the cell states plainly that these three are dispositioned on ROUND 1's classification, INHERITED rather than re-confirmed, because IAM-r-3's deliverable was not present in its tree (checked by name across the repo before saying so). That is a real dependency gap and the cell declared it instead of implying independence. It is CLOSED AFTER THE FACT: IAM-r-3's independent per-member read returns NOT-IN-TF for all three, so the class ruling did not exempt a declared role. A disclosed inheritance later reconciled is sound; an undisclosed one would not have been."
      },
      {
        "criterion": "IAMr5-AC6",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/NFRA_IAMROLES202609.TO-IAM-r-5.production-roles-declared-and-adoption-proved-safe.proof_of_spec.json@43cc4e7594d5",
        "verdict": "PASS",
        "reason": "PASS ON THE MECHANICS, AND THE CRITERION'S OWN TRAP IS WHAT THE EVIDENCE ANSWERS. It asks whether the plan is quiet BECAUSE CORRECT or quiet BECAUSE TOO VAGUE TO DISAGREE. THREE ITEMS DISCRIMINATE, AND A VAGUE DECLARATION COULD NOT PRODUCE ANY OF THEM: the plan READS BACK LIVE VALUES THE DECLARATION NEVER STATED (create_date, unique_id, arn, force_detach_policies, permissions_boundary), so the provider genuinely read both objects; it ENUMERATES ALL FIVE INLINE POLICIES WITH FULL DOCUMENTS plus the managed policy ARN AND PROPOSES NO ACTION ON ANY -- the precise failure mode the cell identified, since Optional+Computed args SET rather than OMITTED would detach them; and `description` DIFFERS BETWEEN THE TWO ROLES (null vs the live audit string), so the declarations are role-specific rather than a template. A too-vague declaration is silent about fields it does not mention; this one is quiet WHILE the provider demonstrably enumerated the things it could have disagreed about. Baseline control quiet FIRST, destroy column 0. ⚠ THREE BOUNDS RIDE THE PASS AND THE CELL RECORDED ALL THREE AGAINST ITSELF IN ITS OWN SECTION 9, WHICH IS WHY IT IS GRADEABLE: (1) ADOPTION IS NOT A PURE NO-OP -- it writes three inherited provider default_tags to each live role via tags_all, so this is not a licence to call it a bookkeeping act without qualification; (2) THIS IS A PASS FOR `opal-data-refresh-lambda-role`'S PLACEMENT ONLY -- `portal-auth-lambda-role` does not belong in this module at all (Z-W6-S4, graduated at C-S9), so the MECHANICS transfer while the state key and inherited tags do not, and the plan must be re-taken wherever it actually lands; (3) A PLAN IS A PREDICTION AT A VINTAGE, NOT AN OUTCOME. ⭐ A CELL THAT WRITES THE CASE AGAINST ITSELF BESIDE THE CASE FOR IS THE REASON THIS JUDGMENT COULD BE MADE FROM THE DELIVERABLE AT ALL."
      },
      {
        "criterion": "IAMr6-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~5/NFRA_IAMROLES202609.TO-IAM-r-6.a-third-disposition-value-then-the-residue-call.proof_of_spec.json@b23572f84f78",
        "verdict": "PASS",
        "reason": "⛔ THE CRITERION EXPLICITLY MAKES OVER-BUILDING A DEFECT -- 'a fourth value nobody needs is as much a defect as a missing third one' -- AND THE CELL MINTED ONE VALUE AND REFUSED ANOTHER, EACH ON A MEASUREMENT. ONE INTENT PER AXIS: the axis is stated as a single question, 'what is this role's correct END STATE in this estate', with the four values ordered on it (should not exist / should exist outside our Terraform deliberately with an owner / should exist inside and is not there yet / is inside already). THE ANTI-RELABELLING DISCRIMINATOR IS A TEST A READER CAN RUN: after the remedy this row names is performed, DOES THE ROLE STILL EXIST -- yes/yes/yes/NO across the four values. That is a real discriminator, not a definition, and it settles that RETIRE is a different question from EXEMPT rather than a rename. THE HONEST OBJECTION IS RAISED AND ANSWERED IN THE DOCUMENT rather than left for the grader (existence and placement could be two axes; they are one here because placement is meaningful only for a role that should exist, and the record NAMES THE CONDITION THAT WOULD FALSIFY THE CLAIM -- a member needing both a placement and an existence value at once, of which this domain has none). ⭐ AND THE BUILD LADDER RAN BEFORE THE MINT: the estate's ratified `Lifecycle_Stage` enum was examined and REFUSED ON ITS OWN CANON'S GROUNDS (C3.ii vertical grain), which is rule 4's ladder executed rather than cited. THE REFUSAL IS THE STRONGER HALF: no fourth value for the policy-attached state, because five of the six roles carrying literal-name attachments in this tree ARE THEMSELVES DECLARED, so the value would classify declared and undeclared identically -- a value that cannot discriminate is not a value."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE ROUND ANSWERED THIS SEAT'S OWN C-S6 AND THIS SEAT ACCEPTS THE ANSWER, WHICH NARROWS WHAT C-S6 CLAIMED. *** C-S6 held that the governance axis had an UNCOVERED MEMBER (rule 24(i) MECE) -- a role whose policies Terraform owns and whose identity it does not -- and that this seat's round-1 remedy (split the IN-CODE token) was therefore TOO NARROW. IAM-r-6 tested exactly that and REFUSED a fourth value ON A MEASUREMENT: 21 hits across 516 files, six role names carrying literal-name attachments, and FIVE OF THE SIX ARE THEMSELVES DECLARED. ⛔ SO 'POLICY-ATTACHED' DOES NOT DISCRIMINATE DECLARED FROM UNDECLARED AND WOULD BE A BAD VALUE ON THIS AXIS. That is correct and this seat adopts it.",
        "⚠ AND THE PRECISE RESIDUE, SO NEITHER FINDING IS OVERSTATED: C-S6's OBSERVATION survives and its REMEDY does not. The observation was about a MEMBER'S DESCRIPTION; the cell answered about a VALUE'S DISCRIMINATION, and both are right about different questions. The evidence that the observation survives is at HEAD in the artifact itself: row 8, `opal-data-refresh-lambda-role`, reads `EXEMPT owner=UNASSIGNED` while its own prose states 'the decision owed is an explicit sign-off (adopt via import, or formally except)'. EXEMPT is defined as deliberately-outside-AND-IT-STAYS; a decision still owed is not that. ⭐ THE MEMBER IS PLACED IN A VALUE THAT MISDESCRIBES IT, AND `owner=UNASSIGNED` IS DOING THE WORK THE VALUE CANNOT. That is arguably the right handling -- an unassigned owner is an honest marker of an undecided disposition -- and it is NOT an argument for a fourth value. THE FIX IS A ROW-LEVEL NOTE, NOT AN AXIS CHANGE, and C-S6's 'the remedy was too narrow' was itself one step too strong.",
        "⚠ ONE CONCRETE INACCURACY STILL LIVE AT HEAD, NAMED BECAUSE IT IS CHEAP TO FIX AND IS THE 3/4/5 SERIES AGAIN: row 8's reason says Terraform touches the role through 'THREE `aws_iam_role_policy` attachments'. C-S10 established the tree-wide figure of record is FIVE (`main.tf` 4 + `qa-scratch-instance.tf` 1), with round 1's THREE and this seat's own main.tf-scoped FOUR as the other two members of the series. The row's SUBSTANCE is unaffected -- Terraform manages policies on a role it does not own, at any of the three counts -- but a governance document at HEAD carries the stalest of the three numbers.",
        "ALL SIX CRITERIA WERE GRADED AGAINST THE DECIDING ARTIFACT OR ITS QUOTED EVIDENCE, and where this seat did not open the underlying deliverable it says so rather than implying it did: IAM-r-1 and IAM-r-6 were graded against `GOVERNANCE_DISPOSITION.md` READ AT HEAD (row 8 quoted above is from that read); IAM-r-3's residue was closed by this seat's own main-tree measurement (C-S11); IAM-r-2, IAM-r-4 and IAM-r-5 were graded against the instances' recorded output evidence plus each cell's own stated case-against, WITHOUT this seat re-running the plan or the reconciliation. ⛔ THAT LIMIT IS REAL AND IS STATED: a judgment criterion asks what a READER concludes, and these three were graded on what the deliverable makes readable rather than on a re-derivation of the underlying measurements.",
        "⭐ AND THE ROUND'S OWN HONESTY IS WHAT MADE SIX JUDGMENT GRADES CHEAP RATHER THAN EXPENSIVE. Every one of the six refused to self-grade and recorded its output WITHOUT a verdict; IAM-r-5 went further and wrote FOUR ARGUMENTS AGAINST ITSELF beside four for; IAM-r-4 disclosed that its membership was inherited rather than re-confirmed; IAM-r-3 named the uncertainty its plane could not close; IAM-r-2 declined to invent a reconciling number. NOT ONE OF THE SIX CLAIMED THE FAVOURABLE READING IT COULD HAVE CLAIMED. That is the same property that made round 3 of NFRA_OPSEC202609 gradeable and it is worth naming as a pattern rather than praising six times."
      ]
    },
    "spec_asserts": "Six of round 2's thirty-one criteria are judgment criteria reserved to 3.0.0_SA_CVO~Z at L9, each recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming this seat.",
    "world_is": "All six are gradeable from the delivered evidence and all six PASS; the round repaired the round-1 FAIL, and it answered this seat's own C-S6 with a measurement that narrows C-S6's remedy claim.",
    "notes": "⛔ THE C-S8 COMMITMENT IS DISCHARGED HERE AND HONOURED AS WRITTEN. IAM-r-6's AC1 and AC3 ARE NOT CREDITED: neither appears in the grades above and neither contributed to IAM-r-6's AC5 PASS. AC1's 'measured 0 at the cut' is true only of a case-SENSITIVE instrument while the criterion ships `-i`; AC3 never discriminated. ⭐ THE SUBSTANCE WAS GRADED FROM THE INSTRUMENT Z-W5-S1 SUPPLIED, exactly as C-S10 undertook: the case-SENSITIVE whole-word census reading 0 at the parent commit and 17 (worker) / 33 (issuer's later read) at the cell's HEAD, plus AC2 and AC4, which are sound bars. NOT CREDITED IS NOT GRADED FAIL, and IAM-r-6 passes its judgment criterion on its reasoning, not on either broken bar. || ⚠ Z-S11's DISARM IS NOW DISCHARGEABLE -- its condition was this grading act and the act is done. It is RECORDED in the remediation track when this project's next slug cuts, not here: the investigation plane DECLARES, the remediation plane RECORDS. || NO SLUG IS CUT. L10 needs `COMPLETION_GRADES` from 1.0.0_SA_CTO~Z, and this round's report partitions 2 COVERED / 6 UNCOVERED-BY-THIS-ROUND by design."
  }
]
```

## C-S13 -- Z-S12: adopt the better mechanism, refute the overstated half with a positive control, and stop the workaround that would produce an UNAUDITED override

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S13",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T16:32Z",
    "one_line": "Z-S12 GRADUATES. Defect 1 is ADOPTED as a better statement of this seat's own four-slug finding; Defect 2's headline is REFUTED on the mandated path with a positive control; and the proposed workaround is flagged as the actual hazard because it would produce an override the audit log never records.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z, unchanged from the row -- `.tools` is that seat's surface. NOT TAKEN HERE. ⚠ The time-sensitive limb is the merge, not the text.",
    "adjudicates": [
      "NFRA_IAMROLES202609-Z-S12"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GRADUATES ON THREE SEPARABLE FINDINGS, ONLY ONE OF WHICH IS A DISPUTE. (1) DEFECT 1 CONFIRMED AND ADOPTED: 195 of 195 surfacer-less rows are REMEDIATION rows and zero are investigation rows, so the gate reads an INVESTIGATION-row property on a REMEDIATION row, its foreign-row exemption can never engage there, and it falls back to grading the COMMITTER. That is the mechanism under the symptom this seat has reported on four slugs. (2) DEFECT 2's HEADLINE REFUTED for the mandated path, at source (`safe-commit.sh:767`) and with a positive control (this seat's own @d076801ecf printing OVERRIDDEN, plus four audit entries today). (3) THE WORKAROUND IS THE HAZARD: a manual `export` skips the audit line at `:758`.",
        "⭐ THE THIRD FINDING IS THE ONE THAT COULD NOT WAIT AND IS WHY THIS WAS FILED RATHER THAN NOTED. 0.0.0_AB_MSTR~Z states its leg-2 merge WILL use a manual export. The gate honours the variable regardless of who set it; only safe-commit writes the audit line. So the override would be real and the record would be silent -- and against a denominator of FOUR logged entries, a missing fifth cannot be inferred from the log's shape. ⛔ AN AUDITED OVERRIDE WHOSE AUDIT IS MISSING IS STRICTLY WORSE THAN A REFUSED COMMIT, because the refusal is loud and the missing line is not.",
        "⚠ AND THE ADJUDICATIVE CARE THIS NEEDS IS TO NOT LET A CORRECT DISPUTE DISCREDIT A CORRECT FINDING. Defect 1 is right, well-measured, and better than this seat's own version of it; the peer also correctly REFUSED to edit remediation rows to clear a merge, reaching that independently from both fabrics. THE DISPUTE IS CONFINED TO ONE SENTENCE OF DEFECT 2 AND THE ACT IT IMPLIES. A row that graduated the dispute while burying the confirmation would be the more comfortable record and the less useful one.",
        "THE REFUSAL TEXT DOES CARRY A REAL DEFECT AND THIS SEAT NAMES ITS FIX NARROWLY: it should say the directive reaches the gate only via `safe-commit -F`. ⛔ IT MUST NOT BE 'FIXED' BY MAKING THE VARIABLE REACHABLE FROM A RAW COMMIT -- `safe-commit.sh:762-766` and the gate's own comment both state the asymmetry is deliberate and is 'the asymmetry the installer exists to close'. A defect report that reads a control as a bug invites the repair that deletes it, and that is the failure mode this adjudication exists to prevent."
      ]
    },
    "spec_asserts": "Msg 20976 asserts two defects in surprise-row-gate.py, the second being that its printed override remedy cannot work by construction.",
    "world_is": "The first is confirmed and sharper than this seat's own prior statement of it; the second is true only off the mandated path, where the failure is a deliberate control rather than a defect.",
    "notes": "⛔ THIS ROW ALSO CARRIES A CORRECTION AGAINST THIS SEAT'S OWN COMMITTED TEXT, and it is not incidental to the finding -- it was produced by it. The slug @d076801ecf claims 'FIFTH SLUG RUNNING' and 'fifth consecutive'; the audit log holds FOUR entries (08:34:51Z, 10:55:48Z, 11:34:19Z, 15:44:23Z), all this seat's, and NFRA_REPORT's v2 slug and v3 disarm record took none -- so it is the FOURTH and it is NOT consecutive. ⭐ IT TOOK A PEER'S CENSUS OF THE SAME GATE TO MAKE THIS SEAT COUNT ITS OWN OVERRIDES, which is the exact shape of 'I verify the half that favours me': the inflated count made the defect sound more systemic, and nothing in this seat's own workflow prompted a re-count because the claim was about a defect this seat did not cause. The commits cannot be rewritten -- rebasing a shared branch is banned -- so the row is the carrier."
  }
]
```
