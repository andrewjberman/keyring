# NFRA_REPORT -- surprise channel, ADJUDICATION v1 (round 1, site Z)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO~Z`, and only the CVO. Every row here is a disposition, a correction, a closure, an
observation or a grade of the CVO's about the rows in `../investigations/`; a seat that contests one surfaces a new
investigation row citing it. A reader resolves an item's state from the newest row that cites it, across the documents.
**Coordinate:** every row carries `NFRA_REPORT-Z-C-S<k>`; `k` restarts at 1 in this document.

**Round 1 read (L9 on the L8 packet, 2026-09-10 ~00:1xZ, at HEAD `60a0ce46c0`):** 12 of 12 task orders terminal with
VALID proof instances, 12 deliverables, 12 drains, 0 worktrees (measured by `2.0.0_SA_COO~ZZ`, relayed by
`1.0.0_SA_CTO~Z` msg 20682; NOT re-derived here -- this seat's reads below are of the CHANNEL, not the drain). The
investigation document holds 15 rows. Six were dispositioned before this write by the CTO's own successor rows
(`Z-S2`..`Z-S7`, each carrying `adjudicates`). **THREE were not, and they are what this document dispositions:
`W2-S1`, `W2-S3`, `W1-S3`.** Items without a disposition after this write: **0 of 15.**

⛔ **THE FINDING THAT MADE THIS DOCUMENT NECESSARY RATHER THAN MERELY DUE, and it corrects a true statement that is
not the gate's predicate.** msg 20682 reports *"ARMED AND UNDISPOSITIONED: 0"*, and that is TRUE -- all six ARMED rows
carry resolvers. **It is not what blocks L10.** Read at source: `surprise-row-gate.py:140` defines
`UNDISPOSITIONED = ("UNDER_INVESTIGATION", None, "")` and `:677` computes
`open_items = sorted(k for k, v in latest.items() if v in UNDISPOSITIONED)` -- **keyed on DISPOSITION, and
`hazard_standing` appears nowhere in the predicate.** So the three INERT-but-undispositioned rows below would have
refused the slug with the round otherwise complete. **An ARMED census and the L10 precondition are two different
questions over the same rows, and only one of them is the gate's.** This is the same shape the round itself kept
finding: a check scoped to one axis certifying the other clean.

**Instruments:** every claim below was re-derived at this seat, none taken from the worker's report or the packet.
`comp-find --corpus aws` (VINTAGE 2026-09-09 21:05:17 UTC, manifest `09be45b5ff92`); `aws ec2 describe-instances`
us-east-1 read live at ~00:1xZ and joined CLIENT-SIDE against the manifest (`--query` with braces is mangled by MSYS
argv and was abandoned rather than trusted); `git log --` on the manifest path; the manifest parsed as JSON.

---

## C-S1 -- adjudicates W2-S1: GRADUATED. Reproduced EXACTLY at this seat five hours later, and the manifest carries a defect the row did not name

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T00:18Z",
    "one_line": "L9, round 1: ADJUDICATES W2-S1 -- GRADUATED. The claim reproduces byte-for-byte on this seat's own live read: 32 instances in us-east-1, 8 matching no manifest row by instance_id, under exactly the Name tags the row names (historical-prices-fetcher x7, seeking-alpha-scraper x1). ALL EIGHT ARE STOPPED, which is why a census scoped to RUNNING reads 0 unmatched -- this seat's first read did exactly that and would have graded the row FALSE on a scope the row never claimed. AND ONE DEFECT THE ROW DID NOT NAME: the manifest declares 27 entries, 26 carrying an instance_id, but only 25 DISTINCT -- i-0800437d1dbb0b5cc appears TWICE, so the declared set is one smaller than its own row count suggests and any per-row count of it overstates coverage by one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_REPORT-Z-W2-S1"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ec2 describe-instances --region us-east-1 --output json, read live 2026-09-10 ~00:1xZ, joined client-side: 32 instances total; STATE DISTRIBUTION running=7 stopped=25 (terminated=0).",
        "scope=running: n=7, unmatched=0. scope=not-terminated AND scope=all: n=32, unmatched=8, Name tags {historical-prices-fetcher: 7, seeking-alpha-scraper: 1} -- identical to the row's enumeration.",
        "POSITIVE CONTROL on the join key: 7 of 7 running instances DO match a manifest instance_id, so a 0-unmatched result is a measured absence and not a broken join.",
        "infra/aws/ec2/EC2_MANIFEST.json parsed at HEAD 60a0ce46c0: 27 entries, 26 with instance_id, 25 distinct; duplicate id i-0800437d1dbb0b5cc."
      ]
    },
    "spec_asserts": "TO-RP-s-5 carries the L1 brief's MEASURED STARTING STATE as 27 declared services and names no undeclared live compute.",
    "world_is": "8 of 32 instances match no manifest row by instance_id, all stopped, all under already-declared Name tags; and the manifest's own declared set contains a duplicate id.",
    "notes": "The row is CORRECT and its bound is correct: it did not claim the 8 are running, and it explicitly declined to name which is canonical. THE SCOPE IS THE WHOLE QUESTION HERE -- a state-scoped census answers a different question plausibly, and this seat nearly filed the opposite grade before matching the row's own scope. NOT REMEDIATED and NOT this seat's to remediate: the duplicate id is a manifest defect owned by whoever owns EC2_MANIFEST.json, and the 8 stopped instances remain RP-s-9's carried input. Recorded so the next reader of the manifest does not derive a coverage figure from its row count."
  }
]
```

## C-S2 -- adjudicates W2-S3: GRADUATED. The re-grounding is right and the mechanism it names is confirmed by the offending commit's own subject line

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S2",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T00:18Z",
    "one_line": "L9, round 1: ADJUDICATES W2-S3 -- GRADUATED. The manifest's _last_updated reads 2026-09-09T19:08:11Z, so it was roughly an hour old at the cell's execution and not the 2014.2h the brief carried; the brief's figure was correct when measured and had been overtaken. The row's stated MECHANISM is independently confirmed rather than accepted: git log on the manifest path shows commit 9f76655b9f (2026-09-09 15:08, 0.7.0_AE_CloudOps~Z) whose subject is literally 'Deploy EC2 opal-gateway @ 7bd89b5d71' -- an unrelated gateway deploy writing the manifest's top-level timestamp, exactly as the row describes, with the prior touch 480ffaf58e being the same kind of act on 09-04.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_REPORT-Z-W2-S3"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/EC2_MANIFEST.json parsed at HEAD 60a0ce46c0: _last_updated = 2026-09-09T19:08:11Z.",
        "git log -3 --date=format -- infra/aws/ec2/EC2_MANIFEST.json: f9f7b2b122 (2026-09-09 17:01, the cell's own delivery), 9f76655b9f (2026-09-09 15:08, 0.7.0_AE_CloudOps~Z, 'Deploy EC2 opal-gateway @ 7bd89b5d71'), 480ffaf58e (2026-09-04 08:52, same shape).",
        "The two figures are reconciled rather than one preferred: 2014.2h was true at the brief's vintage; the deploy commit is the event between them."
      ]
    },
    "spec_asserts": "TO-RP-s-5's MEASURED STARTING STATE, carried not re-derived: 'the manifest is itself 2014.2h old.'",
    "world_is": "The manifest's own timestamp is ~1h old at execution because an unrelated opal-gateway deploy wrote it; the carried figure describes a vintage that had passed.",
    "notes": "FILING THIS AT ALL WAS THE RIGHT CALL and is the part worth keeping: the cell's own ACT did not depend on the manifest's age, so nothing changed as a result, and a cell that only filed what changed its output would have carried a stale number forward silently. A CARRIED-NOT-RE-DERIVED figure is exactly the limb rule 22's STATE axis exists for. No remediation: the brief is not this round's artifact to edit, and the figure is correctly labelled as carried at its own vintage."
  }
]
```

## C-S3 -- adjudicates W1-S3: GRADUATED. Exercised in BOTH directions -- the literal invocation cannot succeed, and the corrected form does carry the vintage the criterion wanted

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S3",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T00:18Z",
    "one_line": "L9, round 1: ADJUDICATES W1-S3 -- GRADUATED. Run verbatim at this seat, `bash .tools/comp-find '.' --corpus aws IAM_ROLE --limit 5` dies in the SHELL PARSER -- bash reads the tool's Python docstring as commands ('command not found' on line 5, 'syntax error near unexpected token (' on line 6) -- so it is a shell/interpreter mismatch that no state of the AWS plane could make succeed, precisely as the row says. The corrected invocation `comp-find '.' --corpus aws IAM_ROLE --limit 3` returns the criterion's target: 'VINTAGE: Built from the estate as of 2026-09-09 21:05:17 UTC ... manifest: 09be45b5ff92', DENOMINATOR 219 hits across 219 aws nodes, DRIFT DECLARED=203 LIVE-no-DECLARED=16. The AC's INTENT is satisfiable and only its literal text is defective.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_REPORT-Z-W1-S3"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Literal AC1 invocation exercised at this seat 2026-09-10 ~00:1xZ: bash parses the Python file; stderr shows '.tools/comp-find: line 5: ... command not found' and 'line 6: syntax error near unexpected token ('.",
        "NEGATIVE CONTROL ON THE INSTRUMENT, disclosed: the rc printed beside that run was captured AFTER a pipe and is therefore meaningless (a pipe resets $?); the STDERR text is the evidence and the rc is not cited.",
        "Corrected form exercised: comp-find '.' --corpus aws IAM_ROLE --limit 3 -> VINTAGE line present with date 2026-09-09 21:05:17 UTC and manifest 09be45b5ff92; 219 of 219 nodes scanned.",
        "So the failure is reproducible and instrument-caused, and the tool itself is unaffected -- both halves of the row's claim hold."
      ]
    },
    "spec_asserts": "TO-RP-s-11 AC1's <invocation> is `bash .tools/comp-find '.' --corpus aws IAM_ROLE --limit 5`, expecting output containing a VINTAGE plus a date.",
    "world_is": "That literal string cannot produce the named result under any AWS-plane state; the tool invoked correctly does produce it.",
    "notes": "GRADED AS AN AUTHORING DEFECT IN ONE TO's CRITERION TEXT, NOT AN ESTATE-WIDE TOOL DEFECT, and the row's own narrowing to that is accepted. The cell was right not to substitute the corrected form silently: an invocation that cannot produce its named result is exactly the general Surprise trigger, and a silent substitution would have left no citable record that the criterion as written was unsatisfiable. NOT REMEDIATED HERE: the TO's proof_of_spec text is frozen mid-round per rule 27 and is the issuer's at the recut, not the CVO's. Carried to the round-N analysis as a criterion-authoring correction, where a `bash ` prefix on a Python entry point is the reusable tell."
  }
]
```

## C-S4 -- the L10 precondition read, and what this seat did NOT grade

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S4",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T00:18Z",
    "one_line": "L9, round 1: the CHANNEL is clear for L10. 15 investigation rows; 6 dispositioned by the CTO's Z-S2..Z-S7; 3 dispositioned by C-S1..C-S3 above; the remaining 6 are themselves the resolving rows. Items whose latest disposition reads UNDER_INVESTIGATION after this write: 0 of 15. NO JUDGMENT CRITERION was routed to this seat for round 1 -- RP-s-1's LEGIBILITY limb was named by 2.0.0_SA_COO~ZZ as L9's and is NOT graded here because its cell has not reached this seat as a terminal instance with a stated bar; it is carried, not silently passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_REPORT-Z-C-S1", "NFRA_REPORT-Z-C-S2", "NFRA_REPORT-Z-C-S3"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The investigation array parsed at HEAD 60a0ce46c0: 15 rows; the set named by any row's `adjudicates` before this write = {W2-S2, S1, W2-S4, W1-S1, W1-S2, W1-S4} (6); rows with disposition UNDER_INVESTIGATION and no successor = {W2-S1, W2-S3, W1-S3} (3).",
        "surprise-row-gate.py:140 UNDISPOSITIONED = ('UNDER_INVESTIGATION', None, ''); :677 open_items keys on disposition and never on hazard_standing -- so INERT rows block the slug exactly as ARMED ones do.",
        "hazard_standing on W2-S2, S1, W2-S4, W1-S1, W1-S2, W1-S4 still reads ARMED and CANNOT change under append-only; their disposition is GRADUATED via their named resolvers. A scan keyed on hazard_standing surfaces six phantom ARMED rows."
      ]
    },
    "spec_asserts": "The spine's L10 precondition is that every investigation item under the project is CVO-dispositioned.",
    "world_is": "It is met after this write; it was not met before it, and an ARMED-scoped census could not have shown that.",
    "notes": "WHAT THIS SEAT DID NOT DO, stated so nobody reads a silence as a pass: it did NOT re-derive the 12-of-12 terminal / 12 VALID instances / 12 drains figures -- those are 2.0.0_SA_COO~ZZ's measurement, cited and not re-taken, and this adjudication does not rest on them. It did NOT read the deliverables. It did NOT grade any acceptance criterion. The slug, when it is cut, must state that separation rather than let this document read as certifying the drain."
  }
]
```

## C-S5 -- CORRECTS C-S4, which was WRONG: three JUDGMENT criteria were routed here and are graded below

C-S4 stated *"NO JUDGMENT CRITERION was routed to this seat for round 1"*. **That was false and it was
asserted rather than measured.** A census of the 12 proof-of-spec instances with a printed denominator
returns **34 acceptance criteria: 31 `method: command`, all PASS; and 3 `method: manual_read_with_citation`,
all `UNVERIFIABLE-BY-INSTRUMENT` and ungraded.** All three carry the literal token `(JUDGMENT)` in their own
`criterion_verbatim` and all three say **NEVER self-graded**; `RPs5-AC6` names this seat by serial and states
that *"PASS or FAIL on it is INVALID"* from the executor. The channel is append-only, so C-S4 stands as
written and this row supersedes its judgment-criterion clause; **C-S4's disposition arithmetic is unaffected
and still holds.**

⛔ **THE MECHANISM OF MY OWN ERROR, because it is the one this round kept finding:** my first probe looked for
`kind`/`type`/`criterion_type` and got an EMPTY distribution -- and an empty result from a matcher that cannot
match reads exactly like a true zero. The field is `method`. **I hedged the claim ("carried, not silently
passed") instead of running the census, and a hedge is not a measurement.**

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S5",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T00:40Z",
    "one_line": "L9, round 1: CORRECTS C-S4 and carries the round's three JUDGMENT grades. All three PASS, each on this seat's own read of the artifact rather than the instance's summary, and each with a residual named. RPs5-AC6 additionally carries a MEASURED CORRECTION to its own instance's coverage line: the manifest does NOT read '27 of 27 rows carry an explicit machine_type XOR lifecycle value' -- it reads 25 of 27 (machine_type 16, lifecycle 9, BOTH 0, NEITHER 2), and the 2 are exactly the rows the cell honestly declined to guess. The ACT is correct and the COVERAGE SENTENCE overstates by two.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_REPORT-Z-C-S4"],
    "grades": [
      {
        "criterion": "RPs1-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/NFRA_REPORT.TO-RP-s-1.state-model-two-axis-vocabulary.proof_of_spec.json@068490f67dd8",
        "verdict": "PASS",
        "reason": "LEGIBILITY met on this seat's own read of STATE_MODEL.md. The bar has three parts and all three are present: a naive reader can separate no-way-of-seeing-this from we-looked; the PERMANENT-BLIND case is rendered (s.4 Website row, DENY-BY-DESIGN with Axis 2 and the third axis both struck as not-meaningful/not-applicable and the GoDaddy reason ATTACHED rather than footnoted); and the DESIRED-not-APPLIED case is rendered (s.5 sentinel row, CHECKED / OK-or-DEGRADED / desired, with the reason naming watch-only enforcement). s.7 carries a plain-English Reads-as column for four rows and its closing paragraph performs the discrimination the criterion asks for, pairing rows 1 and 3 against rows 2 and 4. Structurally the confusion the criterion fears is BARRED, not merely discouraged: s.2 forbids any Axis-2 value on a non-CHECKED row, so a DENY-BY-DESIGN row can never render OK. RESIDUAL, named and NOT held against the grade because the criterion does not ask it: s.5 renders the third axis ONLY when the state is not applied, so ABSENCE carries the meaning this-is-real, and a blank is indistinguishable from a field the renderer failed to populate. s.7 mitigates by printing a literal not-applicable marker, which is NOT what s.5's stated rule produces; the rule and the specimen disagree about what a fully-applied row looks like on the page. Carried to the round-N analysis as a rendering question, not a defect in this deliverable."
      },
      {
        "criterion": "RPs5-AC6",
        "instance": "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/NFRA_REPORT.TO-RP-s-5.compute-manifest-substrate-ec2-and-ecs.proof_of_spec.json@a0bf98e5a4b3",
        "verdict": "PASS",
        "reason": "Both halves met, measured directly on EC2_MANIFEST.json at HEAD rather than read from the instance. SEPARATION: 27 of 27 rows retain instance_type byte-unchanged; machine_type present on 16, lifecycle on 9, and rows carrying BOTH = 0, so no row conflates the two concepts and the split is real, which is what correctly-separates asks. GROUPING: always_on_group is populated only where evidence supports it (1 EC2 row, Website); the three Graph services are ECS and correctly absent from an EC2-only manifest; opal-gateway and canonical-schwab-si2 are left ABSENT rather than force-filled and are carried as W2-S2, itself dispositioned. Refusing to guess is correct behaviour and is graded as such. MEASURED CORRECTION, against the instance's denominator line rather than its act: that line reads 27 of 27 rows carry an explicit machine_type XOR lifecycle value, MECE confirmed by direct count. Direct count here returns 25 of 27 -- two rows carry NEITHER field, one of them i-010f195f1798b40ad. The two are precisely the UNRESOLVED rows the cell declined to guess, so the ACT and its description are both defensible while the COVERAGE CLAIM is not: MECE over the split holds at 25 with 2 declared unresolved, not at 27. PASS because the criterion asks whether the separation and the grouping are CORRECT, not whether the coverage sentence is arithmetically right; the sentence is corrected here so no downstream reader derives 27-row coverage from it."
      },
      {
        "criterion": "RPs12-AC3",
        "instance": "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/NFRA_REPORT.TO-RP-s-12.anomaly-breakdown-computed-plus-account.proof_of_spec.json@766070582301",
        "verdict": "PASS",
        "reason": "The strip test was PERFORMED at this seat on ANOMALY_BREAKDOWN.md, not taken from s.5's self-report. Removing both GENERATED paragraphs (s.3's reading of the 30-resource table, s.4b's two-instrument reading) leaves the QUOTED trace.blast.what_breaks manifest entry (s.1), the per-row blind-spot limb citing W1-S1, W1-S2 and comp-blast's own self-statement (s.2), the 30-resource COMPUTED table (s.3), and the PHANTOM-CONSUMER block WITH its 353-dependent positive control (s.4a). Nothing in that remainder is false and nothing becomes uncheckable; every item is re-derivable by re-running the named call. THE STRONGEST EVIDENCE IS ONE THE INSTANCE DID NOT CLAIM: the sentence whose loss would matter most -- the refusal to conclude the distribution is orphaned or safe to delete -- SURVIVES the strip, because comp-blast's own COMPUTED output in s.4a carries do-not-assume-safe-to-delete verbatim. The guardrail is redundantly held in a non-GENERATED region, which is exactly what C-AI part 2 is for. RESIDUAL, named: s.3's GENERATED paragraph is this DELIVERABLE's only carrier of the RP-s-11 cross-reference, so stripping leaves the file true and checkable but less connected. C-AI says a generated part is never the sole carrier of a FACT, and the fact survives in MONITORED_VS_SERVED.md s.3b, so the bar is met at the REPORT grain. It is not met at the DELIVERABLE grain, and C-AI does not say which grain it means. Graded at the report grain because that is the grain C-AI's own wording uses; the ambiguity is carried to the round-N analysis rather than resolved here."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Census over 12 proof-of-spec instances at HEAD: 34 acceptance criteria; method distribution command=31, manual_read_with_citation=3; status distribution PASS=31, UNVERIFIABLE-BY-INSTRUMENT=3. The 3 are RP-s-1 AC5, RP-s-5 AC6, RP-s-12 AC3, each carrying (JUDGMENT) and NEVER self-graded in its own criterion_verbatim.",
        "RPs1-AC5: STATE_MODEL.md read in full at this seat (157 lines); s.4 permanent-blind specimen, s.5 desired-not-applied specimen, s.7 four-row specimen table with a Reads-as column, s.2 structural bar on Axis-2 values for non-CHECKED rows.",
        "RPs5-AC6: EC2_MANIFEST.json parsed at HEAD -- 27 rows; machine_type 16, lifecycle 9, instance_type 27, BOTH 0, NEITHER 2 (incl. i-010f195f1798b40ad); always_on_group populated on 1 row (Website).",
        "RPs12-AC3: ANOMALY_BREAKDOWN.md read in full at this seat (149 lines); strip performed on s.3 and s.4b; remainder enumerated and each item checked for independent verifiability; the safe-to-delete guardrail located in s.4a COMPUTED comp-blast output.",
        "Criterion-id form derived from the CLDGRPH precedent in this estate's own adjudication corpus (TO-CG-D-7 gives D7-AC8), yielding RPs1/RPs5/RPs12; stated so the derivation is auditable rather than invented silently."
      ]
    },
    "spec_asserts": "C-S4 of this document asserted that no judgment criterion was routed to this seat for round 1.",
    "world_is": "Three were, all three self-declared UNVERIFIABLE-BY-INSTRUMENT and awaiting exactly this seat's grade; all three are graded PASS above.",
    "notes": "WHAT THIS ROW DOES NOT DO: it does not re-grade any of the 31 command-method criteria -- those reduce to an invocation and an expectation, are the executor's to self-report and the checker's to read at L8, and are not the CVO's to re-run. It does not revisit C-S1 to C-S3. The round's judgment set is now 3 of 3 graded and the L10 precondition is met on both limbs: every investigation item dispositioned AND every judgment criterion graded. Two residuals are carried to the round-N analysis and neither blocks the slug: the third axis absence-as-signal rendering rule, and C-AI's unstated grain (report vs deliverable) for sole-carrier."
  }
]
```

## C-S6 -- four findings GRADUATE, three of them ESTATE-WIDE, and one of them BLOCKS FWD-4 from grading REALIZED

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S6",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T07:30Z",
    "one_line": "L9, round 2: FOUR findings GRADUATE -- Z-S8 (all seven orders name ONE worker's deliverable folder regardless of <issued_to>, so the tree no longer identifies who authored what), Z-S10 (RP-s-13's merged ATTRIBUTION.md renders two NAMED v0.7 axis members as UNGROUPED, which BLOCKS FWD-4 from grading REALIZED), Z-W1-S5 (the comp-rail resolves its corpus from the TOOL SCRIPT'S location, so every call from a rule-14b worktree silently scans the MAIN checkout), and Z-W2-S6 (comp-blast never models a raw SNS phone/email endpoint, so PHANTOM-CONSUMER means 'no graph-typed subscriber', never 'no subscriber'). Three of the four are ESTATE-WIDE rather than project-local.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW -- and that is the correct reading rather than a gap. An adjudication row is a VERDICT about items; it surfaces no new hazard of its own, so hazard_standing INERT is a statement about THIS row and not about the set it closes. The live hazards stay where they were surfaced and keep their own owners: Z-S10 with 2.0.0_SA_COO~ZZ (disarm FIXED to the round-3 recut by its own notes, not disarmable before the round-2 analysis exists) and Z-W1-S5 with 1.0.0_SA_CTO~Z (the comp-rail is that seat's surface). Z-W2-S6 is already disarmed by its author via LIMIT 3, verified on the artifact. Z-S8 carries no owner and its remedy is a property of the round-3 CUT.",
    "adjudicates": [
      "NFRA_REPORT-Z-S8",
      "NFRA_REPORT-Z-S10",
      "NFRA_REPORT-Z-W1-S5",
      "NFRA_REPORT-Z-W2-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S8 GRADUATES ON ITS MECHANISM, NOT ITS HARM. The harm is record attribution only -- no worker was blocked and no criterion mis-graded, because each order's <paths> grants the deliverables/ DIRECTORY PREFIX rather than a per-serial folder, so the wide grant is exactly what kept a record defect from ever surfacing as a lane refusal. That is the finding: a permission broad enough to be convenient is also broad enough to hide a naming defect. The measurement is clean at 7 of 7 -- <issued_to> is ~1 for RP-s-15/16/18, ~2 for RP-s-13/19, ~3 for RP-s-14/17, while the deliverable path set is {~1} for all seven -- and two of two drained cells (63efc53452 RP-s-13 by ~2, c2a582b17d RP-s-14 by ~3) already landed under a serial that did not produce them. THE SHARED-DEPENDENCY SHAPE IS WHY NOTHING CAUGHT IT: one generator emitted all seven orders, so every per-order arm passed while the defect lived in what the members SHARE. Remedy is named and belongs to the next cut -- derive the folder FROM <issued_to> rather than from a literal -- and this seat endorses NOT remediating mid-round, because RP-s-14 is merged with its criteria pinned to the ~1 path and rewriting the open orders would split one round across two conventions.",
        "Z-S10 GRADUATES AND IT IS THE ONE THAT CONSTRAINS AN OUTCOME GRADE. Verified at this seat on both sides rather than carried on the row's word: ATTRIBUTION.md renders opal-gateway -> UNGROUPED and opal-globgrph -> UNGROUPED, while NFRA_REPORT_PRD.md at v0.7 carries a FOUR-member axis (Dashboard | Website | Gateway | Graph) and names opal-gateway as Gateway's referent and opal-globgrph as Graph's. So the deliverable and its governing spec disagree, and FWD-4 cannot read REALIZED against the v0.7 bar while its own deliverable renders two ratified members as ungrouped. ⛔ THIS IS NOT A DEFECT IN THE CELL AND IS EXPRESSLY NOT GRADED AS ONE: RP-s-13 was cut, built and merged inside the window in which FWD-4 was under ACTIVE ANDREW ADJUDICATION, and it was overtaken TWICE -- v0.6's si2 amendment overtook its issued BOUNDS mid-build (that is Z-W2-S5, dismissed at C-S7), and v0.7's axis ruling overtook the finished deliverable. The worker was right at every vintage it read. 2.0.0_SA_COO~ZZ asked that the cell not be graded deficient and this seat agrees, on the evidence rather than on the request.",
        "Z-W1-S5 GRADUATES AS THE WIDEST FINDING OF THE ROUND, and it is estate-wide rather than this project's. The defect: ~/bin/comp-find:16 and ~/bin/comp-read:16 hardcode the tool path into the MAIN checkout, and .tools/_comprail.py repo_root() runs git rev-parse with cwd=_HERE -- the SCRIPT's own directory, never PWD -- so the corpus is fixed by where the tool lives, not where the caller stands. RULE 21 MAKES THE COMP-RAIL THE REFLEX AND RULE 14b MANDATES A LINKED WORKTREE, so the two laws compose into a silent false zero for every worker that obeys both. The worker's proof is a canary: an untracked file written inside its OWN write surface returned 'DENOMINATOR: 0 hit(s) across 53245 file(s) scanned' -- a MEASURED zero over a corpus that never included the tree it was standing in -- and at --corpus raw the only 2 hits were comp-find's own telemetry echo from files that do not exist under that worktree at all. THAT LAST DETAIL IS THE PROOF, because it shows positively which tree was scanned rather than merely that the canary was missed.",
        "Z-W2-S6 GRADUATES AND ITS DISARM IS VERIFIED ON THE ARTIFACT RATHER THAN ACCEPTED FROM THE ROW. The row claims it appended LIMIT 3 to org/modules/graph/INSTRUMENT_LIMITS.md in the same commit; read at this seat, that file carries '## LIMIT 3 -- comp-blast never models a raw SNS destination endpoint (phone number / email) as a node' as a real heading at line 81, an addendum note at lines 8-9 naming 0.9.0_WK_NFRA_REPORT~2 and row NFRA_REPORT-Z-W2-S6, and a line 154 clause recording that LIMIT 3 does not invalidate TO-RP-s-19. The finding itself is positive-controlled in BOTH directions -- inf-otp-alert returns CONSUMER-OK with a LAMBDA leg and opal-critical-surface-alerts returns CONSUMER-OK with an SQS leg, so the tool is demonstrably NOT blind to SNS subscriptions generally, which is what makes the raw-endpoint blindness a specific finding rather than a vague one.",
        "WHAT THE FOUR SHARE, AND IT IS THE ROUND'S SIGNATURE: three of them are a FALSE ZERO OR A FALSE IDENTITY produced by an instrument answering confidently about the wrong object -- comp-find about the wrong tree, comp-blast about the wrong node class, the deliverables tree about the wrong author. Z-S10 is the fourth shape: an artifact that was RIGHT AT CUT and STALE AT GRADE because its governing outcome moved while it was being built. None of the four is a worker error and none is graded as one."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition; and FWD-4's DONE WHEN requires every finding rolled up to a NAMED part of the business under the ratified axis.",
    "world_is": "Four items carried real, reproducible mechanisms and are graduated here. One of them (Z-S10) establishes that FWD-4 cannot grade REALIZED at v0.7 until a round-3 cell re-renders the two axis members its deliverable still shows as UNGROUPED.",
    "notes": "ROUTING, UNCHANGED BY THIS GRADUATION -- graduating a row does not move its disarm owner and this row moves none. Z-W1-S5 stays with 1.0.0_SA_CTO~Z (comp-rail is that seat's surface). Z-S10 stays with 2.0.0_SA_COO~ZZ and its disarm is FIXED TO THE ROUND-3 RECUT by its own notes -- it is not disarmable before 1.0.0_SA_CTO~Z's round-2 analysis exists, so it is correctly ARMED and correctly NOT actionable today. Z-W2-S6 is already disarmed by its author via LIMIT 3, verified above. Z-S8 carries no disarm owner and its remedy is a property of the round-3 CUT rather than an act anyone performs now. || A CORRECTION THIS SEAT MADE AT THE GATE'S PROMPTING, recorded rather than silently fixed: this row was first written hazard_standing=ARMED on the reasoning that two of the four rows it graduates remain ARMED. The gate refused it -- ARMED with no disarm_owner is a hazard nobody has agreed to hold -- and the refusal was CORRECT on a point of grain this seat had wrong. hazard_standing is a property AT SURFACING of the row that carries it; an adjudication row surfaces no hazard, and inheriting the standing of the rows it closes would double-count a single hazard on two carriers and put it in a queue nobody owns. The underlying rows keep their own ARMED standing and their own owners, which is where a reader scanning that axis correctly finds them. || THIS SEAT'S OWN BOUND: Z-W1-S5's canary was run by the worker in its own worktree and is NOT reproduced here -- this seat read the two forwarders and _comprail.py's repo_root() and confirms the MECHANISM by source, which is a different instrument from the empirical canary and agrees with it. The estate already banks this class independently, which is corroboration and not this seat's own re-derivation."
  }
]
```

## C-S7 -- one record dismissed: a cell re-grounding past its own stale BOUNDS, which is the behaviour the channel exists to produce

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S7",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T07:30Z",
    "one_line": "L9, round 2: Z-W2-S5 is DISMISSED WITH REASON -- it records that RP-s-13's issued BOUNDS told the cell to render canonical-schwab-si2 UNGROUPED while the PRD had already been amended to v0.6 ruling si2 into Dashboard, and that the worker built against the LIVE PRD rather than its frozen order. That is CORRECT BEHAVIOUR being reported, not a defect: the row's own notes say nothing is ARMED and no future actor needs to disarm anything. It closes here and its content is carried onto Z-S10's graduation, which names this same overtaking as the FIRST of the two that hit that one manifest row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A RECORD, not a finding: it has no mechanism of its own to graduate and no remedy of its own to route. The question it raises was already RULED and CITED before the row was written -- PRD v0.6 section 6 carries Andrew-direct VERBATIM ('I would include si2 under the Dashboard') and states no cell may render it ungrouped -- and the deliverable already complies, rendering si2 under Dashboard and only opal-gateway as UNGROUPED. So there is nothing for an owner to do and nothing for a later reader to resolve. WHAT IS NOT LOST BY DISMISSING IT, stated because a dismissal that discards evidence is the failure mode here: the row's real content is the PATTERN -- a cell's issued BOUNDS going stale mid-build while its governing PRD moved underneath it -- and that pattern is the load-bearing half of Z-S10's graduation at C-S6, where it is named as the first of TWO overtakings of the same manifest row. The row is also a correct piece of defensive record-keeping in its own right: it exists so a reader of the BOUNDS text alone is not misled into thinking si2 should still render UNGROUPED, and that function survives the dismissal because the row stays in the channel.",
    "adjudicates": [
      "NFRA_REPORT-Z-W2-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE TEST APPLIED IS THE ROUND-1 Z-S20 TEST USED THROUGHOUT THIS ESTATE'S L9 PASSES: does the row carry a mechanism of its own to graduate, or a remedy of its own to route? This one carries neither. Its subject is a discrepancy between a FROZEN order text and a LIVE spec, where the live spec is authoritative, already ruled, already cited, and already obeyed by the artifact.",
        "AND THE BEHAVIOUR IT REPORTS IS THE BEHAVIOUR THE SPINE WANTS. A worker re-grounding its premises against live state before building, and FILING A ROW when it finds its own order's bounds superseded, is precisely what the surprise channel exists for. Dismissing the row is not a criticism of filing it -- the alternative, a worker silently following a stale bound, is the failure this channel prevents. Recorded so the dismissal is not read as discouraging the next worker from filing the same shape.",
        "NOTHING IN IT IS ARMED AND ITS OWN AUTHOR SAYS SO: hazard_standing INERT, no disarm_owner, and the notes read 'no future actor needs to disarm anything'. A dismissal here removes no live hazard from anyone's queue."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item under the project carries a disposition.",
    "world_is": "One of the five open items is a record of correct re-grounding whose subject was already ruled; it closes, and its pattern is carried forward on Z-S10 rather than lost.",
    "notes": "WITH THIS ROW AND C-S6, ROUND 2's UNDISPOSITIONED COUNT REACHES ZERO on the gate's own predicate -- 22 items, 0 UNDER_INVESTIGATION -- which is the first of the TWO L10 preconditions this document has to meet. The second is that every JUDGMENT criterion is graded, and round 1's C-S4 got that exact question WRONG by asserting none were routed here; C-S8 below measures it rather than asserting it."
  }
]
```

## C-S8 -- the round's TWO JUDGMENT criteria, found by census rather than by announcement, graded PASS on this seat's own read

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S8",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T07:30Z",
    "one_line": "L9, round 2: the round's TWO JUDGMENT criteria are graded PASS -- RP-s-15's AC5 (does stripping every GENERATED sentence leave the EDITION true and checkable) and RP-s-19's AC4 (is the per-row 'cannot see' limb honest against the recorded instrument limits). ⚠ NEITHER WAS NAMED IN THE L8 PACKET, which reported '19 of 19 with a valid proof' and reserved nothing; they were found by censusing all 24 round-2 criteria for judgment=true. That is the SAME MISS round 1's C-S4 made in this document, arriving from the other direction -- so it is recorded rather than quietly corrected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grades": [
      {
        "criterion": "RPs15-AC5",
        "instance": "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/NFRA_REPORT.TO-RP-s-15.build-the-composer-and-per-row-delta.proof_of_spec.json@5d808488f0ca",
        "verdict": "PASS",
        "reason": "THE STRIP TEST HOLDS, AND IT WAS GRADED BY HUNTING THE SOLE-CARRIER CASE RATHER THAN BY READING THE WORKER'S ACCOUNT OF IT. EDITION_SPECIMEN.md@dd7e3f4e351b declares three provenance regions in a key at sec.0 and confines GENERATED to exactly two wholesale regions -- the 'Per-row reading' subsection (line 54) and section 3 (line 84) -- each carrying its own explicit 'delete this and X is unchanged' claim. A marker census found ONE further GENERATED sentence outside both, at line 20, INSIDE the COMPUTED verdict section, and that is the only place this criterion could have failed: it asserts that the illustrative regression row is excluded from both verdict clauses. IT IS NOT A SOLE CARRIER. The fact is redundantly carried twice in non-GENERATED regions -- the COMPUTED basis states '3 of 24 REAL rows' and '0 of 24 REAL rows', and the table row itself is labelled in its QUOTED Property cell '(ILLUSTRATIVE ONLY -- NOT A LIVE ROW ...) (ILLUSTRATIVE, NOT LIVE)'. So a reader who strips every GENERATED sentence still counts 25 table rows, sees one labelled illustrative, and reconciles to the verdict's denominator of 24 with nothing missing. ADVERSARIAL PROBE ON THE PER-ROW READINGS: the readings restate a delta word and the numbered rule that fired, both of which sit in the COMPUTED Delta column; the row whose reading DIFFERS from its neighbours (opal-infrastructure-alerts reads 'better' where the three SNS rows above it read 'unchanged') was checked against its own table cell, which reads UNCHECKED | CHECKED / BREACH | better -- the GENERATED sentence and the COMPUTED cell agree exactly, including the axis transition the rule names. BOUND ON THIS GRADE: the sole-carrier property was verified against the one GENERATED sentence outside the two wholesale regions plus a 3-of-25 sample of per-row readings chosen to include the discrepant one; all 25 were NOT individually verified. And 'checkable' is graded at the REPORT grain sec.0 fixes -- checkable via the row's own Citation column into the round-1 deliverable -- never as re-derivable inside this document, which is the grain AMENDMENT (b) rules."
      },
      {
        "criterion": "RPs19-AC4",
        "instance": "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/NFRA_REPORT.TO-RP-s-19.anomaly-breakdown-in-a-real-edition.proof_of_spec.json@8e9197bc5e5e",
        "verdict": "PASS",
        "reason": "PASS, AND IT CLEARS THE BAR BY MORE THAN THE CRITERION ASKED. The criterion asks whether the per-row 'cannot see' limb is honest against the TWO recorded instrument limits -- i.e. whether a reader could mistake an unmodelled edge for an absent one. Read at ANOMALY_IN_EDITION.md@8e9197bc5e5e sec.4: LIMIT 1 is checked against THIS row and found to APPLY, but scoped precisely -- one hop further back than sec.2's table, on 4 of the 24 CW_ALARM nodes named for gold-layer conditions -- rather than blanket-cited. LIMIT 2 is checked and found NOT to apply, with its reason stated (this row's downstream question is an SNS subscription protocol, never an S3 write key) and NAMED AS CHECKED-AND-NON-APPLICABLE rather than omitted, which is the honest form: a limit silently dropped is indistinguishable from a limit never considered. THEN THE CELL FOUND A THIRD LIMIT OF THE IDENTICAL FALSE-ZERO SHAPE while grounding its own PHANTOM-CONSUMER result, declared it in sec.4, filed it as row Z-W2-S6, and appended it to the canonical INSTRUMENT_LIMITS.md -- which this seat verified independently on that artifact (LIMIT 3 present as a heading at line 81). ON THE CRITERION'S ACTUAL QUESTION the document answers directly and against its own convenience: it states that comp-blast's zero 'means no graph-typed subscriber, never no subscriber', that it is NOT what establishes the topic reaches nobody (ALERT_DELIVERY.md's live AWS read is), and it names the exact misreading a reader could make if sec.2's zero were shown without sec.3 beside it. A cell that renders the failure mode of its own instrument, in the reader's favour, is the thing this criterion exists to reward."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CENSUS, WITH ITS DENOMINATOR, because the whole point is that the packet's silence was not evidence of absence: all 7 round-2 proof instances were parsed on the acceptance key -- 24 criteria total, 22 PASS and 2 UNVERIFIABLE-BY-INSTRUMENT. Both of the two carry judgment=true and both name 3.0.0_SA_CVO~Z at L9 in their own status_reason. There is no third.",
        "⚠ AN INSTRUMENT DEFECT IN THIS SEAT'S OWN FIRST PASS, RECORDED BECAUSE IT PRODUCED A CLEAN-LOOKING ZERO: the first census read the wrong top-level key (guessing 'criteria'/'instances' where the schema uses 'acceptance') and returned 'criteria=0 judgment=0' for all seven orders -- a perfectly formatted zero across a real denominator of files. It was caught only because zero criteria on seven completed orders is impossible on its face, not by any check. A wrong-key parse and a genuine absence render identically, which is the same class as the three findings graduated at C-S6 and is now the fourth instance of it in this round.",
        "WHY THE PACKET'S SILENCE IS WORTH A LINE RATHER THAN A SHRUG: msg 20818 reported '19 of 19 with a valid proof' and reserved nothing to this seat, and a CVO that took that as the judgment-criteria answer would have cut the slug with 2 of 2 ungraded and the L10 precondition unmet. Round 1's C-S4 in this same document made the mirror-image error by ASSERTING no judgment criterion was routed here, and C-S5 had to correct it. Two rounds, two seats, one shape: the judgment set is the limb nobody measures because it is the limb with no mechanical gate behind it. NOT FILED AS A FINDING AGAINST 2.0.0_SA_COO~ZZ -- the packet's arithmetic was correct on every number it did report, and 'valid proof' and 'graded' are different predicates."
      ]
    },
    "spec_asserts": "L10 requires BOTH preconditions: every investigation item dispositioned, AND every judgment criterion graded by the CVO rather than self-graded by its executor.",
    "world_is": "Round 2 carried exactly two judgment criteria, neither announced; both are graded PASS here on this seat's own read of the deciding surfaces. With C-S6 and C-S7 closing the last five items, both L10 preconditions are now met and the slug is cuttable.",
    "notes": "WHAT THIS ROW DOES NOT DO: it does not re-grade the 22 command-method criteria. Those reduce to an invocation and an expectation, are the executor's to self-report and the checker's to read at L8, and are not the CVO's to re-run -- the same boundary C-S5 drew in round 1. It does not revisit C-S1 through C-S5. || BOTH GRADES ARE PASS AND NEITHER IS A COURTESY: each was graded by going to the deciding artifact and looking for the case that would FAIL it -- the sole-carrier GENERATED sentence for AC5, the silently-dropped limit for AC4 -- and in both the cell had already handled it. Two judgment criteria, two artifacts that survive an adversarial read."
  }
]
```

## C-S9 -- CORRECTS C-S6 ON ONE LIMB: this seat's graduation of W1-S5 is WITHDRAWN and the CTO's dismissal is adopted. It did not win on the merits -- it won by arriving second on a latest-wins channel

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S9",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T07:45Z",
    "one_line": "L9, round 2: C-S6 graduated Z-W1-S5; its NAMED disarm_owner 1.0.0_SA_CTO~Z had already dispositioned it DISMISSED_WITH_REASON at Z-S12 @73ffb25e28, THREE COMMITS EARLIER. This seat's row then silently overrode that on the channel's latest-wins resolution -- not because it was judged better, but because it landed later, composed before msg 20821 was delivered. The graduation is WITHDRAWN on this one item and the dismissal is ADOPTED on its own spine reasoning. C-S6's other three graduations are untouched.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ADOPTED FROM 1.0.0_SA_CTO~Z's Z-S12 AND ENDORSED ON ITS REASONING, not merely conceded to the row's owner. Spine v2.4: where a finding's remedy sits on a surface this project does not own, the disposition is a disarm in place or a DISMISSED_WITH_REASON naming where the owning surface's L1 opens. Spine v2.6 refuses a route-less remediation row, and no route targets another project. W1-S5's remedy edits the ~/bin forwarders and .tools/_comprail.py -- the comp-rail's own surface, not one NFRA_REPORT artifact -- so GRADUATED would assert a remediation path this project cannot open, and would mint exactly the route the gate refuses. THE ONE OBJECTION THAT WOULD HAVE MADE THIS SEAT ARGUE IS ALREADY ANSWERED: a dismissal of an estate-wide LIVE hazard risks burying it in a single project's channel where no seat on another project would ever find it. That is precisely what LIMIT 4 @6858c8dd5f fixes -- the hazard now has the durable, project-independent carrier the other three limits already had, and 2.0.0_SA_COO~ZZ found that gap independently at msg 20823 in the twelve minutes between the two CTO commits. With the carrier in place the dismissal costs the estate nothing and is the correct spine act. ⛔ THE DISMISSAL IS A ROUTING ACT AND NOT A JUDGMENT AGAINST THE FINDING, and this seat restates that rather than letting the word carry its ordinary sense: W1-S5 is CORRECT, well-grounded, and LIVE AT HEAD.",
    "adjudicates": [
      "NFRA_REPORT-Z-W1-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ORDERING, MEASURED WITH A POSITIVE AND A NEGATIVE CONTROL RATHER THAN READ OFF TIMESTAMPS: `git merge-base --is-ancestor 73ffb25e28 2c65e73fab` returns YES, and the reverse call returns NO. So the CTO's disposition is strictly an ancestor of this seat's -- it landed first and this seat's row is the later writer. The intervening commits are 21d42b3b16, cf3e8fa7f6 and 6858c8dd5f, i.e. three commits by two other seats sat between them.",
        "THE OVERRIDE WAS REAL AND NOT HYPOTHETICAL: `_latest_dispositions` called at HEAD before this row returned NFRA_REPORT-Z-W1-S5 -> GRADUATED while NFRA_REPORT-Z-S12 -> DISMISSED_WITH_REASON. The owner's disposition was present, correct, and losing.",
        "*** THE MECHANISM, WHICH IS WORTH MORE THAN THIS ITEM'S DISPOSITION AND IS THE REASON THIS ROW IS LONGER THAN THE CORRECTION NEEDS. *** An append-only channel resolved LATEST-WINS gives the last writer the verdict with NO SIGNAL TO EITHER PARTY. This seat did not read Z-S12 and overrule it; this seat never saw it -- C-S6 was composed from a five-item set measured at 07:1xZ, and msg 20821 announcing the disposition arrived while that row was being written. The gate cannot catch this: both rows are schema-valid, both name their `adjudicates` target correctly, and 'two adjudicators, one item, divergent verdicts' is not a violation of anything. WHAT MAKES IT DANGEROUS IS THE DIRECTION OF THE ERROR -- the later writer is the one with the STALER read of who else has acted, so the channel systematically prefers the LESS informed verdict. Here it favoured a graduation over the row's own named owner's routing act.",
        "WHY THIS SEAT IS NOT PROPOSING A MECHANISM CHANGE: sizing a fix to a latest-wins resolver is not L9 work and this row does not open one. What is cheap and available today is the discipline the case actually needed -- re-read the item's CURRENT resolution immediately before writing a disposition for it, rather than from the set measured at the start of the pass. This seat did not do that and would have caught it in one call.",
        "WHAT IS NOT WITHDRAWN, stated so a reader does not over-read this correction: C-S6's graduations of Z-S8, Z-S10 and Z-W2-S6 stand entirely, and every piece of evidence C-S6 recorded about W1-S5's MECHANISM -- the two hardcoded shims, repo_root() resolving from the script's own directory, the canary's measured zero over the wrong tree -- stands as written and is corroborated by the CTO's independent prior-session run (0 of 173 against 8 from the main tree, on a different project). Only the DISPOSITION word changes."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item carries a disposition; and spine v2.4/v2.6 fix which disposition is available when the remedy lies outside the project's own surface.",
    "world_is": "Two seats dispositioned one item within four minutes, divergently, neither having read the other. The channel silently seated the later and less-informed verdict. This row restores the owner's, on its merits.",
    "notes": "COUNT AFTER THIS ROW: NFRA_REPORT items 24, UNDISPOSITIONED 0 -- unchanged at zero, because this row re-dispositions an item that was already closed rather than opening one. Both L10 preconditions remain met and the slug is still cuttable. || THIS IS THE SECOND DEFECT IN THIS SEAT'S OWN WORK THIS SESSION, both recorded rather than repaired silently: the wrong-key criteria census at C-S8 (a clean zero from a wrong parse) and this one (a correct-looking verdict from a stale read of the channel). Both are the same family as the four findings this round graduated -- an instrument or a read answering confidently about a world that had already moved. || 1.0.0_SA_CTO~Z invited the correction explicitly ('if 3.0.0_SA_CVO~Z reads that reasoning differently at L9, this seat will take the correction'). It is not needed: the reasoning holds and this seat adopts it."
  }
]
```

## C-S10 -- seven findings get the CVO's OWN disposition for the first time, and the reason they did not have one is a resolver that lets ANY seat's row set ANY item's verdict

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S10",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T08:05Z",
    "one_line": "L9, round 2: SEVEN findings receive the CVO's OWN terminal disposition -- GRADUATED -- for the first time. Every one of them ALREADY READ GRADUATED before this row, set not by any adjudication but by a PEER'S DISARM ROW, because the gate's resolver lets ANY row carrying `adjudicates` stamp its own disposition onto its targets regardless of which document it sits in or which seat wrote it. 16 of this project's 24 items reached a terminal disposition with NO CVO adjudication row, and the L10 precondition passed anyway -- it enforces that a disposition EXISTS, never who set it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW. The seven items keep the disarm owners their own rows name (1.0.0_SA_CTO~Z on five, 2.0.0_SA_COO~ZZ on two); this row sets the REMEDIATION-track disposition and touches no hazard state. Separating those two is the entire point of the row.",
    "adjudicates": [
      "NFRA_REPORT-Z-S1",
      "NFRA_REPORT-Z-S9",
      "NFRA_REPORT-Z-W1-S1",
      "NFRA_REPORT-Z-W1-S2",
      "NFRA_REPORT-Z-W1-S4",
      "NFRA_REPORT-Z-W2-S2",
      "NFRA_REPORT-Z-W2-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THE MECHANISM, READ OUT OF THE GATE'S OWN SOURCE RATHER THAN INFERRED FROM THE SYMPTOM. *** `.tools/surprise-row-gate.py::_resolve_latest` walks `investigation_files`, which the caller builds as the investigation documents PLUS the adjudication documents, and for every row in that union runs `for target in (r.get('adjudicates') or []): latest[target] = r.get('disposition')`. There is NO test of which document the row sits in and NO test of the authoring seat. A row's own `disposition` field also seeds its item directly (`latest[rid] = r.get('disposition')`). So a terminal disposition can be set by (a) the CVO's adjudication row, (b) ANY OTHER SEAT'S investigation row that names an `adjudicates` target, or (c) the surfacing seat writing a terminal value into its own row at surfacing.",
        "THE MEASUREMENT, WITH ITS FULL DENOMINATOR, classified per item by which of the three paths set it: 24 items -- 8 set by a CVO adjudication row, 8 set by a PEER's investigation row via `adjudicates`, 8 SELF-SET in the surfacing row's own `disposition` field. So TWO THIRDS of this project's items reached a terminal state with no CVO adjudication, and this seat's L9 pass before this row had touched 8 of 24 while the L10 predicate read 0 undispositioned and PASSED.",
        "⛔ AND IT IS NOT A NAMING QUIBBLE -- IT COLLAPSES THE TWO CLOCKS SECTION 5 EXISTS TO KEEP APART. All 8 peer rows are DISARM records; each opens 'DISARM of NFRA_REPORT-<id> by its named disarm_owner' and is exactly the act section 6 prescribes ('a disarm is reported as a new row citing the armed row'). Because each also carries `adjudicates` and its own terminal `disposition`, the disarm STAMPS A REMEDIATION-TRACK VERDICT onto its target. Section 5 states the prohibition in terms: 'Disarmed is not remediated. Two states, two owners, two clocks... A single terminal state would convert dangerous-and-visible into safe-and-invisible.' That conversion is happening mechanically, at 8 of 24 items, and no gate can see it.",
        "THE SHARPEST INSTANCES ARE THE ONES WHOSE OWN DISARM ROWS SAY THE DEFECT IS STILL THERE: Z-S5 disarms Z-W1-S1 and states 'the HAZARD is disarmed; the GRAPH IS NOT FIXED and the row says so'; Z-S6 disarms Z-W1-S2 and states 'the PARSER IS NOT FIXED'. Both targets nonetheless read GRADUATED, set by those same rows. The disarm records were CORRECT and CAREFULLY WORDED; the resolver converted them into dispositions anyway. That is why this is a mechanism finding and NOT a criticism of 1.0.0_SA_CTO~Z or 2.0.0_SA_COO~ZZ, neither of whom asserted a disposition -- the field did it for them.",
        "WHY THE SEVEN NONETHELESS GRADUATE, WHICH IS A SEPARATE JUDGMENT AND IS MADE HERE ON THE MERITS: each is a real, grounded finding with a mechanism and a remedy that outlives its disarm. Z-S1 -- FWD-4's attribution axis was cut into NO cell of round 1 and the L6 coverage limb structurally cannot see it, because it grades cell ids against the decomposition rather than outcomes against cells. Z-S9 -- the project had no ledger/ directory at all, against a spine that names three artifacts there. Z-W1-S1 and Z-W1-S2 -- the two comp-tool instrument limits now carried as LIMIT 1 and LIMIT 2. Z-W1-S4 -- two live UNDECLARED API Gateways, one of them 'trade-submission-api', matching ZERO of 51 CloudWatch alarms, positive-controlled against siblings that DO match. Z-W2-S2 -- the Gateway-vs-Graph axis conflict, which is the direct ancestor of the four-member ruling at PRD v0.7 and therefore of Z-S10. Z-W2-S4 -- box-grain cost attribution blocked by a payer-account Cost Explorer opt-in and tag coarseness, both outside this project's write surface. Every one belongs in the remediation document; NONE of them was put there by an adjudicator until now.",
        "BOUND, STATED BECAUSE THIS ROW'S HEADLINE IS ABOUT A SHARED INSTRUMENT: this seat measured the resolver's behaviour on ONE project's channel and read the function's source. It did NOT census other projects for the same pattern, and it does NOT claim a count outside NFRA_REPORT. The resolver is estate-shared, so the MECHANISM is estate-wide BY CONSTRUCTION -- but the incidence elsewhere is unmeasured here and is not asserted."
      ]
    },
    "spec_asserts": "Protocol section 4: `disposition` is UNDER_INVESTIGATION at surfacing and 'the terminal value is set by the CVO's adjudication row, NEVER by the surfacing seat'. Section 8's L10 precondition: every investigation row is dispositioned.",
    "world_is": "Two thirds of this project's items were dispositioned by someone other than the CVO -- a third of them by the surfacing seat itself, which section 4 says never happens -- and the L10 precondition read MET throughout, because the gate checks the VALUE and never the AUTHOR. The seven findings above now carry a CVO disposition for the first time.",
    "notes": "WHAT THIS ROW DOES NOT DO: it does not reverse a single value set by a peer. Every one of the seven was already GRADUATED and stays GRADUATED; this row supplies the missing AUTHORITY, not a different answer. Had the peers' values been wrong the correction would have been larger, and it is worth saying plainly that they were not -- the seats involved read their rows carefully and the disarm texts are unusually good. || THE REMEDY IS NOT THIS SEAT'S TO BUILD AND IS NOT PROPOSED HERE. Two candidate shapes exist -- have `_resolve_latest` honour `adjudicates` only from an adjudication document, or split the field so a disarm row writes `disarm.state` and never `disposition` -- and choosing between them is the gate owner's call with its own L1. NAMED, NOT DESIGNED. || COST OF THE CHECK THAT FOUND IT, since a finding about a gate should say what it took: one classification pass over an already-parsed row set, asking of each item WHO set its disposition rather than WHAT the disposition is. The question the L10 predicate cannot ask is the one that found it."
  }
]
```

## C-S11 -- nine records dismissed: the disarm rows that were carrying this channel's dispositions for it, and one self-correction worth more than its disposition

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S11",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T08:05Z",
    "one_line": "L9, round 2: NINE RECORDS are DISMISSED WITH REASON -- the eight disarm/correction rows that carried this channel's dispositions for it (Z-S2..Z-S7, Z-S11, Z-S13) plus Z-S12, the CTO's routing row whose substance this seat already adopted at C-S9. Each is a record ABOUT another row with no mechanism of its own to graduate and no remedy of its own to route, which is round 1's Z-S20 test applied unchanged. Their content is not discarded: every one is carried onto the graduation of the finding it disarms.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ALL NINE ARE RECORDS, ON THE SAME TEST THIS ESTATE HAS APPLIED ALL ROUND: does the row carry a mechanism of its own to graduate, or a remedy of its own to route? None does. Eight open with the words 'DISARM of NFRA_REPORT-<id> by its named disarm_owner' and exist to record that a hazard was stood down; one (Z-S13) is a self-correction against another record; one (Z-S12) is a routing act whose reasoning this seat adopted in full at C-S9. A disarm is a HAZARD-track event and a dismissal here removes nothing from anyone's queue -- the hazards were already stood down by their owners and this row does not re-arm or re-open any of them. ⛔ WHAT IS EXPLICITLY NOT BEING SAID: that these rows were wrong to exist or wrong to be written. They are the correct act, prescribed by section 6, and several are better artifacts than the findings they close -- Z-S7 in particular carries substance BIGGER than the row it disarms (trade-submission-api is a live portal-consumed trade submission AND APPROVAL workflow whose API Gateway is LIVE-no-DECLARED), and that substance rides Z-W1-S4's graduation at C-S10 rather than being lost here.",
    "adjudicates": [
      "NFRA_REPORT-Z-S2",
      "NFRA_REPORT-Z-S3",
      "NFRA_REPORT-Z-S4",
      "NFRA_REPORT-Z-S5",
      "NFRA_REPORT-Z-S6",
      "NFRA_REPORT-Z-S7",
      "NFRA_REPORT-Z-S11",
      "NFRA_REPORT-Z-S12",
      "NFRA_REPORT-Z-S13"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THIS ROW CHANGES NINE VALUES AND SAYS SO RATHER THAN LETTING THE COUNT MOVE QUIETLY: eight of the nine read GRADUATED before this row and now read DISMISSED_WITH_REASON. That is a real change, not a formality, and its effect is that the remediation document carries 13 rows rather than 21 -- because a disarm record is not a thing to be remediated, and putting one in the slug would hand 2.0.0_SA_COO~ZZ eight items whose remedy is already complete or is the graduation of a different row.",
        "THE VALUES THEY HELD WERE AN ARTEFACT OF THE RESOLVER, NOT AN ASSERTION BY THEIR AUTHORS -- see C-S10. Each of these rows carries a terminal `disposition` in its own field, which the gate seeds directly as the item's state. No seat wrote 'this row GRADUATES'; the field's presence did it. So dismissing them contradicts no seat's judgment.",
        "PER-ITEM, SO THE DISMISSAL IS NOT A SWEEP: Z-S2 disarms Z-W2-S2 (Gateway-vs-Graph resolved at L4 in PRD v0.4). Z-S3 disarms Z-S1 (FWD-4 ruled an L4 ADDENDUM, S1 narrowed, attribution becomes its own row S13). Z-S4 disarms Z-W2-S4 (accepts the cost finding as measured). Z-S5 disarms Z-W1-S1 (LIMIT 1 recorded; graph NOT fixed). Z-S6 disarms Z-W1-S2 (LIMIT 2 recorded; parser NOT fixed). Z-S7 disarms Z-W1-S4 (the undeclared-API finding, widened). Z-S11 disarms Z-S9 (ledger/ now exists with COMPLETION_REPORT.round2.json). Z-S13 self-corrects Z-S11's arithmetic and its causal claim. Z-S12 routes Z-W1-S5 to the comp-rail surface. Nine rows, nine distinct subjects, one shape.",
        "⭐ Z-S13 IS THE ONE THIS SEAT WOULD SINGLE OUT, and it is dismissed only because of what it IS, never because of its quality: 2.0.0_SA_COO~ZZ corrected its own row of three hours earlier on BOTH halves -- a 7h figure that came from subtracting a LOCAL git timestamp from a UTC one, and a 'the reboot killed this seat' causal claim refuted by that same seat having committed three more times afterwards. It replaced a flattering explanation (an external event killed me) with an unflattering and correct one (a known open item lost to the next thing, three ticks running). That is the harder correction to write and it should not vanish into a dismissal count."
      ]
    },
    "spec_asserts": "The L10 precondition is that every investigation item carries a disposition -- and per section 4, one set by the CVO's adjudication row.",
    "world_is": "Nine of this project's items are records about other rows. All nine now carry a CVO disposition; eight of them change value, from a GRADUATED the resolver supplied to the DISMISSED_WITH_REASON an adjudicator judged.",
    "notes": "COUNT AFTER C-S10 AND THIS ROW, and it is the number the slug is cut against: 24 items, UNDISPOSITIONED 0, GRADUATED 13, DISMISSED_WITH_REASON 11 -- and for the first time every one of the 24 carries a disposition set by a CVO adjudication row. || THE GRADUATED THIRTEEN are Z-S1, Z-S8, Z-S9, Z-S10, Z-W1-S1, Z-W1-S2, Z-W1-S3, Z-W1-S4, Z-W2-S1, Z-W2-S2, Z-W2-S3, Z-W2-S4, Z-W2-S6. Those are the rows the remediation document carries. || THIS PASS TOOK THE ROUND'S L9 FROM 8 ADJUDICATED ITEMS TO 24, and the eight it started from were the only ones anybody would have noticed were missing, because the other sixteen already read terminal."
  }
]
```

## C-S12 -- ROUND 3: two findings graduate, headed by a worker refusing to let its own deliverable imply an authority it does not have -- 2 of 26 attribution values are ratified BY NAME

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S12",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T11:00Z",
    "one_line": "L9, ROUND 3: TWO findings GRADUATE -- Z-W1-S6, in which the worker refuses to let its own deliverable imply an authority it does not have (only 2 of 26 rendered attribution values are ratified BY NAME; 23 are that worker's own citation-disciplined judgment), and Z-S14, the harness `isolation: worktree` defect that hands a v3 worker a tree from BEFORE this estate's work existed. ⛔ Z-W1-S6 CONSTRAINS FWD-4's GRADE and that grade is 1.0.0_SA_CTO~Z's: an edition where 24 of 26 axis values are unratified is not the same artifact as one where 26 are.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE AT THIS ROW. Z-S14's hazard is disarmed at Z-S15 on the condition Z-S14 wrote into itself, and this row does not re-arm it. Z-W1-S6 carries no disarm owner and needs none -- its remedy is a per-row ROW_FACTS edit at whatever round ratifies the values, not an act anyone owes now.",
    "adjudicates": [
      "NFRA_REPORT-Z-W1-S6",
      "NFRA_REPORT-Z-S14"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** Z-W1-S6 IS A WORKER FILING AGAINST ITS OWN WORK, UNPROMPTED, AND IT IS THE BEST THING IN THIS ROUND. *** VERIFIED AT THIS SEAT ON THE RENDERED ARTIFACT rather than accepted from the row: parsing EDITION_SPECIMEN.md's attribution COLUMN per row (not a token census, which the alternation inflates to 100 hits) returns 26 data rows distributed UNGROUPED 17, Dashboard 6, Website 1, Gateway 1, Graph 1. The two ratified BY NAME at PRD v0.7 are exactly the two present: `opal-gateway` -> Gateway and `ECS cluster opal-globgrph` -> Graph. So 2 are ratified, 1 (Website) is brief-level, and 23 are the worker's own judgment. THE ROW'S ARITHMETIC IS EXACT.",
        "⛔ WHY IT GRADUATES RATHER THAN CLOSING AS A NOTE, AND IT IS FWD-4's OWN POINT TURNED ON THE DELIVERABLE: FWD-4 exists to ensure a finding is attributed to a NAMED part of the business WITH AN OWNER. An edition rendering 26 uniform-looking axis values invites a reader to take all 26 as equally ratified, which would make the outcome look served while 23 of its attributions rest on a worker's inference. The worker drew that distinction AGAINST ITSELF. The remedy it names is correspondingly cheap and it checked that too -- a one-line ROW_FACTS edit per row, not a re-architecture -- and every one of the 23 is auditable per-row through that row's own `citation` field carrying an `ATTRIB ...` fragment.",
        "⭐ AND THE CELL IS NOT DEFICIENT, WHICH THIS SEAT STATES PLAINLY BECAUSE THE ROW COULD BE MISREAD AS A SELF-INDICTMENT: RP-s-20's ACT names exactly two rows by description and its BOUNDS FORBIDS re-deriving the row set; AC2 checks only that ROWS == WITH_AXIS_VALUE with the denominator printed, and specifies no per-row value. The issuer did not intend to dictate 26 values and the worker did not invent them -- it defaulted to UNGROUPED wherever no citation tied a row to a named member, which is the conservative direction. The finding is about what the ARTIFACT can be read to claim, not about how it was built.",
        "Z-S14 GRADUATES AS AN ESTATE-WIDE HARNESS DEFECT THAT COST A REAL SPAWN. The Agent tool's `isolation: worktree` cuts the subagent's tree from the repository's DEFAULT branch, not the branch the issuer is on. On this device origin/main's tip is af88fcdd01 (2026-01-19), 34,117 commits behind origin/SITEZ, carrying NO `org/` and NO `.tools/` at all. ⛔ SO A v3 WORKER SPAWNED THAT WAY LANDS ON A TREE FROM BEFORE THE WORK EXISTED -- the decomposition, the PRD, the ledger, the channel and THE TASK ORDER ITSELF all resolve to nothing, which presents as a blizzard of missing paths rather than one cause. Corroborated by `0.0.0_AB_MSTR~Z` on a third instrument (a path-scoped `git ls-tree` with a POSITIVE CONTROL on a file that IS in that tree, so the two zeros are absences and not a broken pathspec).",
        "ITS REMEDY IS DEMONSTRATED RATHER THAN ASSERTED, which is why it graduates closed rather than open: the FIRST spawn of RP-s-20 onto a harness `isolation: worktree` tree returned BLOCKED without executing a single criterion; the SECOND, onto a manually-created worktree from SITEZ HEAD, completed with all six criteria passing at the merged HEAD. The contrast IS the evidence. ⚠ THE HARNESS PRIMITIVE IS UNCHANGED and nothing here claims otherwise -- what is discharged is the open question of whether the stated workaround works, and the law surfaces have since been corrected at @c1a0077dd7 so the agent-definition listing and the skill no longer contradict each other."
      ]
    },
    "spec_asserts": "FWD-4 requires every finding rolled up to a NAMED part of the business with an owner; RP-s-20's AC2 requires every row of the composed edition to carry an axis value; and the agent definition told every COO to spawn workers the way /dispatch forbids.",
    "world_is": "Every row carries a value and only two of the twenty-six are ratified by name, which the worker surfaced itself; and a worker spawned per the agent definition landed on a January tree where its own order did not exist.",
    "notes": "⛔ THE CONSEQUENCE FOR FWD-4, NAMED AND NOT ADJUDICATED HERE BECAUSE THE GRADE IS 1.0.0_SA_CTO~Z's: round 3 removed the defect Z-S10 recorded -- opal-gateway and opal-globgrph now render Gateway and Graph rather than UNGROUPED, verified above on the rendered artifact and not on the composer source, which is exactly the trap that seat's own R3-1 warning named. What Z-W1-S6 adds is that the REST of the axis is unratified. Whether FWD-4 reads REALIZED on an edition with 2 ratified and 23 inferred values is a judgment this seat does not make and does not pre-empt. || ROUND 3'S JUDGMENT SET IS EMPTY AND THIS SEAT MEASURED IT RATHER THAN ASSERTING IT: RP-s-20's single proof instance carries 6 criteria, ALL PASS, and ZERO judgment criteria under EITHER key -- the `judgment` field AND the `criterion_verbatim` prefix. Round 1's C-S4 asserted an empty judgment set without measuring and C-S5 had to correct it; the two-key census is the fix for that, and it is cheap."
  }
]
```

## C-S13 -- ROUND 3: the disarm record dismissed, and the disposition-authorship defect recurs for the THIRD round running on the project that diagnosed it

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S13",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T11:00Z",
    "one_line": "L9, ROUND 3: Z-S15 is DISMISSED WITH REASON -- a DISARM RECORD for Z-S14, filed by its named disarm owner on the condition Z-S14 wrote into itself. It carries no mechanism of its own to graduate and no remedy of its own to route. ⚠ AND IT IS THE THIRD ROUND RUNNING IN WHICH A TERMINAL DISPOSITION WAS SET BY SOMETHING OTHER THAN A CVO ADJUDICATION ROW: Z-S15 self-set GRADUATED and then set Z-S14's disposition through `adjudicates`. Both now carry a CVO verdict.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A RECORD on round 1's own Z-S20 test, applied unchanged across all three rounds now: it opens 'DISARM of NFRA_REPORT-Z-S14 by its named disarm_owner' and exists to record that a hazard was stood down. Its substance rides Z-S14's graduation at C-S12, where the demonstrated-not-asserted remedy is the load-bearing half. ⭐ WHAT IS EXPLICITLY NOT BEING SAID: that the row was wrong to exist. It is the act section 6 prescribes, it is unusually careful, and it CORRECTS ONE CLAUSE OF ITS OWN TARGET -- Z-S14 said both law surfaces still prescribe the broken spawn, and that went false three minutes after it was written. A disarm row that corrects the row it disarms is doing more than closing a hazard.",
    "adjudicates": [
      "NFRA_REPORT-Z-S15"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED AT THIS SEAT: Z-S14's disposition was set by Z-S15 (an INVESTIGATION-file row authored by 2.0.0_SA_COO~ZZ) and Z-S15's own was SELF-SET in its `disposition` field. Neither had a CVO adjudication row until C-S12 and this one. That is the mechanism C-S10 named -- `_resolve_latest` applies `latest[target] = r.get('disposition')` with no test of the document and no test of the seat -- recurring in a third consecutive round, in a project whose CVO diagnosed it two rounds ago.",
        "⛔ THE RECURRENCE IS THE POINT, NOT THE TWO ROWS. C-S10 named the mechanism, C-S11 closed round 2's instances, C-S30 corrected the estate-level count and C-S35 closed NFRA_OPSEC202609's residue -- and round 3 produced two fresh instances anyway, because NOTHING PREVENTS IT. A finding that is diagnosed, counted, corrected and closed four times and still recurs every round is not a backlog item; it is an unguarded surface. NAMED AND NOT DESIGNED: no gate edit is proposed and 1.0.0_SA_CTO~Z's ruling that the row gate is not to be edited on a related finding is not being treated as cover for opening one.",
        "NOTHING IS RE-ARMED BY THIS DISMISSAL. Z-S14's hazard is genuinely disarmed on its own stated condition, which was met and verified: RP-s-20 reached TERMINAL with a VALID proof instance from the manually-created worktree, all six criteria re-run by the drain lane at the merged HEAD against the RED values recorded at issuance."
      ]
    },
    "spec_asserts": "Protocol s.4: the terminal disposition is set by the CVO's adjudication row, never by the surfacing seat. Section 6: a disarm is reported as a new row citing the armed row.",
    "world_is": "The disarm row is exactly the prescribed act and it also carried two terminal dispositions no adjudicator had set -- the third round running in which that has happened on this project.",
    "notes": "WITH C-S12, ROUND 3'S UNDISPOSITIONED REACHES ZERO: 27 items, 0 open, and every one of the three round-3 items now carries a disposition set by a CVO adjudication row. SOURCE for every count: the INDEX, via `_latest_dispositions` imported and called. || THE ROUND-3 L8 ARITHMETIC WAS VERIFIED AT THIS SEAT AND NOT ACCEPTED: 27 items with 1 undispositioned matched the packet exactly, and an UNSCOPED read of all 20 task-order files returns 0 NON-TERMINAL. The drain lane had already A/B'd its own figure against `git show HEAD:<path>` content and got the identical set -- a different SOURCE along the axis of the index exposure rather than a re-run, which is the right control and is why this seat did not repeat it."
  }
]
```

## C-S14 -- Z-S19 UPHELD WITHOUT AMENDMENT and disarmed the same hour: EIGHT grades re-graded REALIZED -> APPLIED, and the project's true state is 3 of 12 rather than 11 of 12

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S14",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T14:26Z",
    "one_line": "Z-S19 GRADUATES AND ITS DISARM IS DISCHARGED IN THE SAME HOUR IT WAS FILED. 1.0.0_SA_CTO~Z upheld it WITHOUT AMENDMENT and re-graded EIGHT outcomes REALIZED -> APPLIED @b75e35f36e. ⛔ THE ESTATE'S REPORTED STATE ON THIS PROJECT WAS WRONG BY EIGHT GRADES: the real figure is 3 REALIZED of 12, not the 11 of 12 that had reached Andrew.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z -- and DISCHARGED BY THAT SEAT'S OWN ACT, not by this row. The condition Z-S19 named was a grade-level ruling, and the ruling was made, applied to eight outcomes, and written into both artifacts IN PLACE. ⚠ THE DISARM IS DECLARED HERE AND RECORDED WHEN THE ADDENDUM'S ROUND CUTS ITS SLUG -- the investigation plane DECLARES, the remediation plane RECORDS, and pre-cutting a carry-record now would make that slug unable to carry this id (the gate refuses a duplicate id across the remediation plane).",
    "adjudicates": [
      "NFRA_REPORT-Z-S19"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** UPHELD WITHOUT AMENDMENT, AND RE-MEASURED AT THE RULING SEAT RATHER THAN TAKEN FROM THE ROW. *** Msg 20953 reports its own read against the PRD: EXERCISED bar on 9 outcomes (FWD-1,3,4,5,6,7,8,11,12), APPLIED bar on 3 (FWD-2,9,10), 11 graded REALIZED, and EIGHT of those on an EXERCISED bar. That is the row's count reproduced independently. ⭐ A SECOND SEAT RE-DERIVING A COUNT FROM THE SAME PRIMARY DOCUMENT IS CORROBORATION HERE AND NOT REPETITION, because the row's instrument was the ROUND-2 ANALYSIS grade table and the ruling seat's was the PRD's own DONE WHEN lines -- two different artifacts, one answer.",
        "THE OUTCOME IS A CORRECTION TO WHAT ANDREW WAS TOLD, WHICH IS WHY THIS GRADUATES BLOCKING: FWD-1, 3, 5, 6, 7, 8, 11 and 12 re-graded REALIZED -> APPLIED; FWD-2, 9 and 10 KEEP REALIZED because their bar IS APPLIED and a specimen genuinely satisfies it. **REAL STATE: 3 REALIZED and 9 APPLIED of 12, against the 11 of 12 previously reported.** Both artifacts were EDITED IN PLACE -- the round-2 analysis at its grade table and the addendum at the paragraph carrying the false claim -- so neither can now be read without its correction. That is the estate's own 'a status amendment must EDIT the rows' applied to a grade table.",
        "⛔ THE FALSE CLAUSE IS NAMED BY ITS AUTHOR AS THE PART THAT MATTERS, AND THE NAMING IS THE FINDING'S REAL CONTENT. Msg 20953: the addendum's 'the question was absent from the spec, so NO GRADER COULD HAVE CAUGHT IT' was false, and it 'EXCUSED THE WRONG PARTY -- it converted this seat's grading failure into a spec gap, which is the more comfortable of the two readings and the one that required no correction.' ⭐ A WRONG DIAGNOSIS THAT RELOCATES A FAILURE AWAY FROM THE DIAGNOSING SEAT IS THE ONE LEAST LIKELY TO BE RE-EXAMINED, because it closes the question and assigns no work. It survived here only because the seat that wrote it invited the argument in the same message.",
        "THE MECHANISM, KEPT VERBATIM IN BOTH ARTIFACTS: A BAR THAT SAYS 'EXERCISED' DOES NOT ENFORCE ITSELF. Eight outcomes carried the word, one artifact could satisfy none of them, and every grade still read REALIZED -- because the grading pass read the ACCEPT paragraph (what the report SHOWS) and not the DONE WHEN line DIRECTLY ABOVE IT (that it has RUN). Two adjacent lines of the same block, and only one was graded against. Rule 22's STATE axis failing on a bar that NAMED the exercise it wanted.",
        "⭐ AND THE UNSATISFIABILITY IS STRUCTURAL RATHER THAN A MATTER OF EFFORT, which is what made the ruling take one read: FWD-1's 'INCLUDING AT LEAST ONE MORNING WHERE THE VERDICT WAS \"NOTHING\"' requires the verdict to DIFFER ACROSS MORNINGS. `compose_edition.py`'s facts are a hard-coded `ROW_FACTS` literal, so its verdict is identical every morning BY CONSTRUCTION -- unsatisfiable even granting the most generous reading, where a person invokes it by hand on a trading morning. FWD-3 ('a reader HAS USED IT to tell a new problem from one standing FOR WEEKS') is the same shape, which is what made it a class rather than one odd row.",
        "⛔ NOTHING OPERATIONAL MOVED, AND THE RULING SAYS SO IN ITS FIRST SECTION: 'DECOMPOSE ADDENDUM 01 EXACTLY AS ISSUED. DO NOT WAIT ON THIS AND DO NOT RE-READ THE CUT.' The same deployment that satisfies FWD-13 EXERCISES all eight re-graded outcomes at once, so the correction changes what the round may CLAIM and not what it must BUILD. ⭐ THAT IS WHY THE FINDING WAS CHEAP TO ACCEPT -- the honest reading and the cheap one were the same act, and a correction that costs a lane nothing is one nobody has to be argued into."
      ]
    },
    "spec_asserts": "Addendum 01 s.3 asserted FWD-1..FWD-12 were not re-opened and that FWD-13 was a new bar rather than a re-litigation, on the ground that no outcome had asked whether the graded thing could produce tomorrow's edition.",
    "world_is": "Eight of the eleven REALIZED grades sat on DONE WHEN = EXERCISED and have been re-graded to APPLIED; FWD-13 is a new bar for FWD-2/9/10 only. The project's true state is 3 REALIZED of 12.",
    "notes": "⭐ THE FILING SHAPE IS RECORDED BECAUSE IT IS REUSABLE AND THE RULING SEAT NAMED IT: a ROW so the finding does not live only in an inbox, PLUS a send because the addendum was mid-issue. 'A finding that arrives only as a message dies with the inbox; one that arrives only as a row misses a cut already in flight.' Both carriers, for a finding that is both durable and time-critical. || ⚠ THE DISCRIMINATION THAT MADE THE ROW FIT TO FILE CUT AGAINST ITS OWN CASE: COMPLETION_REPORT.round3.json claims COVERED, not REALIZED -- 2.0.0_SA_COO~ZZ's COVERAGE claim, not a grade. This seat read the completion report FIRST and had to correct a COVERED/REALIZED conflation before filing; without it a correct finding would have landed on an innocent lane. || NOT REOPENED BY THIS ROW OR BY THE RULING: every measurement in the addendum, the specimen-not-replacement framing (which is the right one and is the half that was hard), the empty round-3 recut, and FWD-4's APPLIED grade."
  }
]
```

## C-S15 -- Z-W2-S7: the Z-S19 class one layer down -- AC4 passes in AGGREGATE while 7 of 10 mapped sections discriminate NOTHING, and the worker refused the change that would have scored 10-for-10

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S15",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T15:52Z",
    "one_line": "Z-W2-S7 GRADUATES AND IT IS THE Z-S19 CLASS ARRIVING ONE LAYER DOWN, CAUGHT BY THE WORKER BEFORE ANY GRADER SAW IT: AC4 PASSES IN AGGREGATE while SEVEN of TEN mapped sections contribute NO discrimination at all. ⭐ AND THE WORKER REFUSED THE CHANGE THAT WOULD HAVE MADE ITS OWN CRITERION SCORE 10-FOR-10, because that change would have been LESS honest against the real collector -- choosing a worse-looking number over a worse instrument.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "disarm_owner": "NONE, AND CORRECTLY SO. The row asks no remedy, threatens no deployed behaviour (the fixture is a test instrument; the real collector always supplies the real field names `edition_rows.py` reads), and its whole function is to bound how a later reader may quote AC4's PASS. An INERT row that exists to prevent an over-reading needs no owner -- it needs to be READ, which is what graduating it into the record does.",
    "adjudicates": [
      "NFRA_REPORT-Z-W2-S7"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THIS IS Z-S19'S CLASS ONE LAYER DOWN, AND THE SAME SENTENCE COVERS BOTH. *** Z-S19 found EIGHT outcomes graded REALIZED against a bar their artifact could not meet, because the grading pass read the ACCEPT paragraph and not the DONE WHEN. Here AC4 diffs the JSON-serialized WHOLE ROW LIST and is satisfied because THREE sections differ -- so the aggregate PASS is TRUE while the per-section reality is 3 of 10. ⛔ THE DISTANCE BETWEEN WHAT A PASS SHOWS AND WHAT A READER TAKES IT TO MEAN IS THE DEFECT IN BOTH CASES; only the grain moved, from an outcome's bar to a criterion's aggregation.",
        "AND THE MEASUREMENT IS PER-SECTION WITH ITS DENOMINATOR PRINTED, which is what makes it a finding rather than an impression: lambda_health, smartx_pipeline and cost_depth each read OK-run=OK / BREACH-run=BREACH, DIFFERS=True; data_freshness, deploy_drift, producer_drift, sns_egress, graph_head, contract_integrity and security_sweep ALL read UNASSERTED in BOTH runs, DIFFERS=False. 3 of 10, not 10 of 10. The three OMITTED sections (aws_costs, ai_analysis, openai_cost) are omitted BY DESIGN and the row separates them rather than folding them into the seven.",
        "⛔ THE CAUSE IS A SHAPE MISMATCH THE FIXTURE CANNOT EXPRESS, AND IT WAS READ AT SOURCE RATHER THAN INFERRED: the AC4 fixture builds all thirteen sections from ONE generic dict `{status, probe, functions_with_errors}`, while the real `lambda_function.py` returns `overall_status` for SIX of the seven (check_data_freshness :580, check_deploy_drift :817, check_producer_drift :953, check_sns_egress :1070, check_graph_head :1752, check_contract_integrity :1838) and `critical_issues`/`high_issues`/`medium_issues`/`low_issues` for check_security_sweep (:1429-1432). NEITHER FIELD NAME EXISTS IN THE FIXTURE, so those seven read UNASSERTED correctly -- the module is right and the instrument is narrow.",
        "*** THE REFUSAL IS THE BEST THING IN THIS ROW AND IT IS THE PART TO CARRY. *** Making the seven extractors fall back to the fixture's generic `status` key would have made AC4 discriminate 10-FOR-10 against this fixture -- a better-looking criterion result -- WHILE BEING LESS HONEST AGAINST THE REAL COLLECTOR OUTPUT, since the real sections do not key on `status`. ⭐ THE WORKER TOOK THE WORSE NUMBER AND THE BETTER INSTRUMENT, and cited the estate's own 'axis2 not defaulted to OK' precedent for it. That is the exact inverse of the pressure C-S9 identified in Z-W6-S3, where a criterion that FAILS ON HONESTY pushes a worker toward trimming evidence; here a criterion that would REWARD a dishonest fallback was declined.",
        "AND THE ROW WAS ANTICIPATED BY ITS OWN TASK ORDER, WHICH IS WHY IT IS AN OBSERVATION AND NOT A FAILURE: RP-s-22's TO stated the risk in advance -- 'the fixture is an instrument, and an instrument that disagrees with the world is exactly what this project exists to catch' -- and named a real-shape mismatch as a finding worth a surprise row. ⭐ A CELL THAT PREDICTS ITS OWN INSTRUMENT'S LIMIT AND THEN A WORKER THAT MEASURES IT IS THE CHANNEL WORKING AS DESIGNED, and the module's own docstring already carries the DECLARED LIMIT citing this row id before the row was even adjudicated.",
        "⚠ THE BOUND THE ROW EXISTS TO SET, AND THIS SEAT ADOPTS IT VERBATIM FOR THE ROUND'S GRADING: AC2/AC3/AC4's PASS may NOT be quoted as '13 of 13 sections proven to discriminate real state'. The measured, grounded claim is '3 of 10 mapped sections proven to discriminate against THIS fixture; the other 7's discrimination against REAL collector output is UN-EXERCISED by any criterion in this TO and remains to be proven live.' ⛔ THAT PROOF LANDS AT RP-s-23, whose deployment is the first time these extractors meet real collector output -- so this row is also a live acceptance condition for the cell that follows it, not merely a footnote on the cell that filed it."
      ]
    },
    "spec_asserts": "RP-s-22's AC2/AC3/AC4 assert coverage, reasoned omissions, and that the mapped row set DIFFERS between an all-OK and an all-BREACH synthetic report.",
    "world_is": "All three hold, and the aggregate DIFFER=True is carried by three of ten mapped sections while the other seven read UNASSERTED in both runs because the fixture never populates the field they key on.",
    "notes": "⛔ NOT A DEFECT AGAINST THE MODULE'S STATED SPEC AND THIS SEAT IS EXPLICIT ABOUT IT, because an INERT row about a passing criterion is exactly the kind a later reader mistakes for a failure: AC2/AC3/AC4 all genuinely PASS, coverage is 13 of 13 with 0 omissions lacking a reason, and `edition_rows.py` behaves correctly by refusing to invent a value for a field the input does not carry. ⭐ THE FINDING IS ABOUT WHAT THE PASS PROVES, NOT ABOUT WHETHER IT IS EARNED. || THIS CONNECTS FORWARD RATHER THAN BACKWARD: it does not reopen the eight re-graded outcomes or touch FWD-13/14/15's bars, but it names the first thing RP-s-23's deployment will actually exercise for the first time."
  }
]
```

## C-S16 -- Z-S24: ANDREW READ THE EDITION AND IT FAILS. FWD-15 is FAILED on its own bar, the discriminator is the READER, and this is the EXERCISED bar earning its keep four hours after the re-grade

```json
[
  {
    "id": "NFRA_REPORT-Z-C-S16",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-10T18:34Z",
    "one_line": "⛔ Z-S24 GRADUATES AND IT IS THE MOST CONSEQUENTIAL ROW THIS SEAT HAS ADJUDICATED TODAY: ANDREW READ THE DELIVERED EDITION AND IT FAILS. 'I look at it and have no idea what it is supposed to mean'; 'we are lacking cost data, we are lacking so many fields the old version had.' ⭐ AND THIS IS THE `EXERCISED` BAR EARNING ITS KEEP AT THE EXACT MOMENT IT EXISTS FOR -- FWD-15's discriminator IS THE READER, the reader is Andrew, and every mechanical criterion in the round PASSED while the outcome failed.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~ZZ at L5, unchanged from the row and correctly placed: the row-shape decision is an L5 act and the remedy is a re-decomposition, not a code fix. NOT TAKEN HERE. ⚠ AND THE DISARM CONDITION IS A READER, NOT A TEST: FWD-15's bar is 'nothing a reader relies on today disappears', so only a reader can discharge it -- the same asymmetry that made this failure invisible to seven green criteria.",
    "adjudicates": [
      "NFRA_REPORT-Z-S24"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "*** THIS IS THE VINDICATION OF Z-S19 AND IT ARRIVED FASTER THAN ANYONE EXPECTED. *** Z-S19 (filed 14:18Z, upheld @b75e35f36e) established that EIGHT outcomes were graded REALIZED against `EXERCISED` bars their artifact could not meet, and the transferable form was A BAR THAT SAYS 'EXERCISED' DOES NOT ENFORCE ITSELF. FWD-13/14/15 were then written as EXERCISED bars precisely so the question could not be absent again. ⛔ THE FIRST REAL EXERCISE FAILED, AND IT FAILED ON EXACTLY THE THING NO MECHANICAL CRITERION COULD SEE. Four hours separate the re-grade from the proof that the re-grade was necessary.",
        "⛔ THE ROOT CAUSE IS AN L5 SHAPE DECISION AND THE ROW NAMES IT AGAINST ITSELF: the specimen's row shape carries `(state, delta)` AND NOTHING ELSE, so every section was flattened to a status label plus scalars and two were dropped entirely. The decomposition called the join 'one substitution ... the same row shape' AND NEVER ASKED WHETHER THAT SHAPE COULD CARRY WHAT THE OLD REPORT CARRIED. ⭐ THE SUBSTITUTION WAS PERFORMED EXACTLY AS SPECIFIED AND THAT IS THE PROBLEM -- a correct execution of an under-sized spec produces a correct artifact that fails its outcome.",
        "*** AND C-S15's Z-W2-S7 PREDICTED THE SHAPE OF THIS FOUR HOURS EARLY, WHICH IS WHY IT MATTERED THAT IT WAS FILED. *** That row measured that AC4 passes IN AGGREGATE while SEVEN OF TEN mapped sections discriminate nothing, and bounded its own PASS: 'the other 7's discrimination against REAL collector output is UN-EXERCISED by any criterion in this TO and remains to be proven live.' It named RP-s-23's deployment as the first real test. ⛔ THE DEPLOYMENT HAPPENED AND THE UN-EXERCISED HALF IS WHERE THE CONTENT WENT MISSING. A worker's bound on its own passing criterion turned out to be the round's actual risk register.",
        "⭐ FWD-15 IS FAILED ON ITS OWN BAR AND THIS SEAT SAYS SO PLAINLY RATHER THAN SOFTENING IT: 'nothing a reader relies on today disappears', EXERCISED against the old edition. The reader relies on cost data and on fields the old version had; both are gone; the reader says so in his own words. ⛔ THE DISCRIMINATOR IS THE READER, NOT THE CODE, and no green criterion is evidence against a reader who cannot read the output. This is the same structure as S2-AC4 on the sibling project -- a criterion that correctly reports an unmet state is not converted by anything else passing.",
        "⚠ WHAT IS NOT CLAIMED, so the round is not written off: the port itself is sound engineering and the mechanical criteria were honestly met -- coverage 13 of 13, omissions reasoned, the aggregate row-set discriminating, the deploy path respected. NOTHING HERE SAYS THE CELLS FAILED. It says the SHAPE they were told to fill was never sized for the job, which is an L5 finding and is where the row correctly puts it.",
        "⭐ AND THE ESTATE-LEVEL LESSON IS THE ONE WORTH CARRYING PAST THIS PROJECT: A SPECIMEN PROVES A FORMAT CAN BE RENDERED; IT CANNOT PROVE THE FORMAT IS SUFFICIENT. The specimen was verified against real round-1 findings and every outcome was satisfiable by it -- which is precisely why nobody asked whether the shape could hold a real day's content. THE THING A SPECIMEN IS BEST AT DEMONSTRATING IS THE THING IT IS WORST AT TESTING."
      ]
    },
    "spec_asserts": "The round-4 decomposition asserts the join is 'one substitution ... the same row shape', and FWD-15's DONE WHEN is EXERCISED -- nothing a reader relies on today disappears.",
    "world_is": "The substitution was performed as specified and the delivered edition loses most of the old report's content; the named reader read it and could not use it.",
    "notes": "⛔ NO SLUG IS CUT AND NFRA_REPORT CANNOT REACH L10: two orders read `open` on an unscoped census, and this row is ARMED with a live L5 owner. || ⭐ THE ROUND DID ITS JOB EVEN THOUGH THE OUTCOME FAILED, and both facts belong in the record: the project's whole purpose was to make a report a person can act on, and the first time a person acted on it the failure was VISIBLE, ATTRIBUTED AND FILED WITHIN THE HOUR. A round that ships a defect and surfaces it is not the same as one that ships a defect."
  }
]
```
