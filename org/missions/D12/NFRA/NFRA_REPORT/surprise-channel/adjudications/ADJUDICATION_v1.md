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
