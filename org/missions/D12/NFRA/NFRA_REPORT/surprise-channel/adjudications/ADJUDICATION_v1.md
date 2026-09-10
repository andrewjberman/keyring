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
