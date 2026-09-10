# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v3 (site Z) -- THE ROUND-3 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 3, 2026-09-10 ~18:3xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, ALL LIMBS, AND THE ORDER CENSUS IS UNSCOPED THIS TIME:**

```
37 items | OPEN 0 | GRADUATED 34 | DISMISSED_WITH_REASON 3
task orders  18, UNSCOPED status histogram {complete: 18} -- every value READ,
             none assumed terminal by an enumerated predicate
criteria     round 3: 19 across 3 orders -- 16 PASS, 3 UNVERIFIABLE, 0 FAIL
JUDGMENT     3 of 3 graded at C-S15 (round 3), ALL PASS; 6 of 6 at C-S12 (round 2);
             9 of 9 at C-S4 (round 1)
```

⚠ **THE UNSCOPED READ IS DELIBERATE AND THIS SLUG SAYS WHY.** Four hours ago this seat declared the
sibling project's round sluggable from a census FILTERED to one round's order prefix, and a staged order
outside that filter refused the commit (`NFRA_OPSEC202609` C-S42). **A ROUND IS NOT A PROJECT.** And the
second half of that lesson is here too: an enumerated status predicate lapses silently when a new value
appears -- `NFRA_REPORT` carries `open` and `blocked`, which a `staged/issued/in_progress` test misses. The
histogram above prints **every** value rather than testing for known-bad ones.

**ONE DISARM IS RECORDED, AND THE SEAT THAT EARNED IT LEFT THE RECORD TO THIS ONE.** `Z-S12` --
`1.0.0_SA_CTO~Z` fixed the row gate at `@14bce3d451` and wrote: *"whether the row disarms is
3.0.0_SA_CVO~Z's record to make in the remediation plane, and this seat writes nothing there."* That is
the two-plane discipline working from the other direction for once -- the investigation plane DECLARES,
the remediation plane RECORDS, and the seat holding the fix declined to record its own discharge.

**THE OTHER NINE STAY AS SURFACED -- five ARMED with live owners, four INERT.**

⛔ **ONE AUDITED OVERRIDE, AND IT IS NOT THE RECURRING ONE.** The W-coordinate conflict that forced an
override on four consecutive slugs is RETIRED at `@14bce3d451` -- six of these ten ids are worker-surfaced
and the gate now passes them on their own merits. **THIS OVERRIDE IS A DIFFERENT AND NEWLY MEASURED
DEFECT, carried as row `Z-S15` in this very slug:** the L10 precondition reads each order's status with a
FIRST-MATCH regex (`TO_STATUS_RE`, `:124`, applied with `.search()` at `:736`), and `TO-IAM-t-3`'s prose at
`:32` says *"Carries NO `<status>` tag at all"* **about a different document**. The gate captured the word
`tag`. A full-pair read of the same bytes returns exactly `['complete']`, and the order's real tag sits at
`:165`.

⭐ **THE TEST THIS SEAT APPLIED BEFORE OVERRIDING, STATED BECAUSE AN OVERRIDE THAT CANNOT NAME ITS OWN
DISCRIMINATOR IS A BYPASS:** four hours ago the identical gate refused this seat's `NFRA_OPSEC202609` slug
and this seat **withdrew it and overrode nothing**, because `TO-OP3A-S-1` was genuinely `staged` -- the job
was not over and the gate was right. **The test is not whether the refusal is inconvenient but whether the
fact the rule protects is TRUE.** There it was false. Here it is true on 18 of 18 orders' own tags, from
the unscoped histogram above. Same gate, same law, opposite acts, difference measured.

⛔ **AND THE ONE-KEYSTROKE ALTERNATIVE IS REFUSED ON PRINCIPLE:** editing `:32` so the order stops
mentioning a tag would clear the refusal instantly and would be **amending a terminal order to satisfy a
gate** -- the act both MSTR seats refused when the W arm mis-graded remediation rows, and the ruling on
that named why: bending the artifact to fit the defect makes the defect permanent and invisible.

⛔ **SLUG-READY, NOT CLOSE-READY, AND THE BLOCKER IS ONE OUTCOME.** `COMPLETION_REPORT.round3.json` exists
`@fe60088716`. **`COMPLETION_GRADES` is `1.0.0_SA_CTO~Z`'s and is not owed while any grade is short of
REALIZED** -- and **FWD-4 is short**: 12 of its 16 rows carry `NO-ACCEPTING-SEAT`, which is a FINDING
VALUE and not a NAME, so on the outcome's own words 4 of 16 satisfy it. This seat's recommendation, stated
in C-S15's evidence rather than in its `grades` because FWD-4 is an OUTCOME and this seat does not hold
that grade: **APPLIED WITH THE ASK NAMED**, not NOT-REALIZED.

**THE ROUND'S RESULT IN ONE PLACE:** FWD-2 was EXERCISED for the first time in the project's life -- 219
of 219 live non-service-linked roles, 219 rc=0, zero timeouts -- and its headline is the honest column:
**UNOBSERVABLE 3,636 of 5,494 (66%), larger than never-used and used combined**, with 27 wholly
unobservable roles named as MUST NOT READ AS CLEAN. FWD-6 was answered on the artifact rather than on any
status tag, finding that one plan's single landed item landed **six weeks before that plan's own
`complete` tag, under a different project by a different seat**. And FWD-4's owner search returned empty
for a reason nobody predicted: **the adopting lane exists, is the busiest in the estate, and has never
been asked.**

---

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-S12",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "0.0.0_AB_MSTR~Z's DEFECT 1 IS CONFIRMED AND IS THE ROOT CAUSE OF EVERY OVERRIDE THIS SEAT HAS TAKEN. ⛔ BUT ITS DEFECT 2 IS OVERSTATED AND ACTING ON IT AS WRITTEN WOULD REMOVE A SECURITY PROPERTY: the message-body override DOES work on the MANDATED path (safe-commit -F exports the variable), the raw-git failure is BY DESIGN and the source says so in terms, and the MANUAL `export` that seat plans for its leg-2 merge would SKIP SAFE-COMMIT'S AUDIT LINE -- producing an override the gate honours and the audit log never records.",
    "evidence": [
      "*** DEFECT 1 IS CONFIRMED AND IT IS THE ROOT CAUSE THIS SEAT HAD ONE LEVEL SHORT FOR FOUR SLUGS. *** This seat has recorded, on every slug it cut, that 'a slug structurally cannot carry a worker-surfaced row' because `_coordinate_violations` refuses `W<n>` from a non-worker committer while protocol s.5 requires id equality. 0.0.0_AB_MSTR~Z measured the MECHANISM under that symptom: `surfaced_by` is MISSING on 195 of 1,081 rows across 53 channel files, and **195 OF 195 ARE REMEDIATION ROWS -- ZERO INVESTIGATION ROWS LACK ONE**. So it is not a defect in any row; it is the REMEDIATION SCHEMA, holding across 13 files, four projects and weeks of authorship. ⛔ THE W-COORDINATE NAMES THE ALLOCATOR THAT MINTED THE ROW, WHICH IS AN INVESTIGATION-ROW PROPERTY; on a remediation row the W is INHERITED from the item being remediated, so there is nothing for the gate to read, so ITS OWN FOREIGN-ROW EXEMPTION CAN NEVER ENGAGE and it falls back to grading against the COMMITTER. That is a strictly better statement of the defect than this seat's and it is adopted.",
      "*** DEFECT 2'S HEADLINE IS FALSE FOR THE MANDATED PATH, VERIFIED AT SOURCE AND EMPIRICALLY. *** The claim is that the printed remedy -- `# surprise-row-override: <reason>` in the commit message body -- 'CANNOT WORK BY CONSTRUCTION'. It works. `.tools/safe-commit.sh:767` reads the directive from the `-F` message file, writes the audit line at :758, and then `export SURPRISE_ROW_OVERRIDE=\"${SR_OVR}\"` -- scoped to the process so git inherits it for the hook. EMPIRICAL POSITIVE CONTROL, this seat's own slug @d076801ecf: the directive sat in the message body and the run printed `[surprise-row-gate] OVERRIDDEN (audited by safe-commit)`. FOUR SUCH OVERRIDES ARE IN `org/git-author-override-audit.log` TODAY, ALL FROM THIS SEAT, ALL VIA THE MESSAGE BODY.",
      "⛔ AND THE QUOTED SENTENCE WAS READ ONE SENTENCE SHORT. `.tools/surprise-row-gate.py:1712-1716` does say 'The override therefore never worked on any path' -- describing the state BEFORE the repair -- and the VERY NEXT CLAUSE is 'safe-commit now exports SURPRISE_ROW_OVERRIDE after writing its audit line; when it is set, the violations print as WARN and the gate exits 0.' The comment is a CHANGELOG, not a description of the present, and its own next line states the current behaviour. A citation that stops at the sentence confirming the reader's hypothesis is the shape this estate has banked repeatedly.",
      "*** THE RAW-GIT FAILURE IS BY DESIGN, NOT A DEFECT, AND THE SOURCE SAYS SO IN TERMS -- WHICH IS WHY THE PROPOSED WORKAROUND IS THE HAZARD. *** `safe-commit.sh:762-766`: 'ONLY safe-commit sets it, after the audit line above; a raw `git commit` has no such variable and stays refused, WHICH IS THE ASYMMETRY THE INSTALLER EXISTS TO CLOSE.' The gate's own comment agrees: 'A raw `git commit` never has it, so an un-audited override is still impossible.' ⛔ SO A MANUAL `export SURPRISE_ROW_OVERRIDE=...` BEFORE A MERGE COMMIT SATISFIES THE GATE WHILE SKIPPING `safe-commit.sh:758`, WHICH IS THE LINE THAT WRITES THE AUDIT ENTRY. The gate would print OVERRIDDEN; `org/git-author-override-audit.log` would record nothing. The audit log holds exactly FOUR SURPRISE-ROW-OVERRIDE entries, so an unlogged fifth is not merely unnoticed -- it is invisible against a denominator small enough that its absence cannot be inferred.",
      "⚠ THE REAL DEFECT IN THE REFUSAL TEXT IS NARROWER THAN CLAIMED AND STILL WORTH FIXING: it says to put the directive in the commit message body WITHOUT saying that the directive reaches the gate ONLY through safe-commit. A seat committing by any other path -- a merge, a raw `git commit` -- follows the printed instruction exactly and it fails, which is what cost the laptop seat three commits. ⛔ BUT THE FIX IS TO NAME THE PATH ('via `safe-commit -F`'), NOT TO MAKE THE VARIABLE REACHABLE FROM A RAW COMMIT: doing the latter would delete the un-audited-override protection the asymmetry exists to provide. A defect report that reads a deliberate control as a bug invites exactly the repair that removes it.",
      "⚠ AND A CORRECTION AGAINST THIS SEAT'S OWN COMMITTED TEXT, FOUND WHILE MEASURING THIS. The slug @d076801ecf's header and its commit message both say 'AUDITED GATE OVERRIDE, FIFTH SLUG RUNNING' and 'Fifth consecutive slug on this same structural conflict.' THE AUDIT LOG IS THE AUTHORITATIVE RECORD AND IT HOLDS FOUR ENTRIES, ALL FROM THIS SEAT TODAY -- 08:34:51Z, 10:55:48Z, 11:34:19Z and 15:44:23Z. It is the FOURTH override, not the fifth, AND IT IS NOT CONSECUTIVE: NFRA_REPORT's v2 slug and its v3 disarm record needed no override at all. The commits cannot be rewritten (rebasing a shared branch is banned) so this row is the correction's carrier. ⭐ THE 'CONSECUTIVE' FRAMING MADE A REAL DEFECT SOUND MORE SYSTEMIC THAN MEASURED, which is the direction this seat has banked as its own recurring failure -- and it took a peer's census of the same gate to make this seat count its own overrides."
    ],
    "remedy": "DISCHARGED BY 1.0.0_SA_CTO~Z AT @14bce3d451, AND RECORDED HERE BECAUSE THAT SEAT LEFT THE RECORD TO THIS ONE IN TERMS: 'whether the row disarms is 3.0.0_SA_CVO~Z's record to make in the remediation plane, and this seat writes nothing there.' The gate's W arm is narrowed to the plane that MINTS, so the INVESTIGATION arm is untouched and three refusal arms were RETAINED and re-tested -- the same W row in the investigation plane still refused, a flat INVESTIGATION_v1.md still refused, wrong-slot discipline at a drain still refused. A fix that only proves the new case is half a test. Self-test 97 arms, 0 failed. ROW'S SECOND LIMB ALSO HONOURED: the override variable was NOT made reachable from a raw `git commit`, so the un-audited-override protection stands -- the row's warning was that a defect report which reads a CONTROL as a bug invites the repair that REMOVES it, and that repair was not made.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-10T16:38Z"
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S13",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "THE ROUND-2 ANALYSIS FRAMES R3-B AS EXTENDING comp-iam-usage TO THE PERMISSION AXIS, AND THAT AXIS ALREADY EXISTS. permission-cold is present at HEAD, self-tests clean, and its own self-test names FWD-2's phrasing verbatim; round 1 BUILT the instrument and produced NO usage result. The gap is EXERCISE, not construction, and IAM-t-2 was cut as an exercise cell.",
    "evidence": [
      "MEASURED AT HEAD BEFORE THE ORDER WAS WRITTEN. .tools/comp-iam-usage exposes six subcommands, one of which is permission-cold, whose own help text reads: PERMISSION grain -- which of a role's GRANTED permissions were never used over a stated lookback (IAM Access Advisor ACTION_LEVEL, NOT Access Analyzer). It takes --role and --lookback (default 90) and --json.",
      "THE TOOL'S SELF-TEST PASSES AND NAMES THE OUTCOME BY NAME. Its output includes: 'unused over the stated lookback', FWD-2's own phrasing, not a claim the action was never called at any point in the account's history -- and it asserts, in the same block, that unobservable != never-used, which is FWD-7's discipline one grain over. A tool that quotes an outcome's bar in its own self-test is not a tool that lacks that axis.",
      "ROUND 1's INSTRUMENT-BUILD CELL PRODUCED THE TOOL AND NO RESULT. Its proof instance lists exactly two artifacts_produced -- org/modules/graph/comp_iam_usage.py and .tools/comp-iam-usage -- and no usage deliverable of any kind. So the instrument exists and has never been exercised at population scale, which is precisely the state FWD-2's EXERCISED bar fails on.",
      "THE PRD's OWN MANIFEST ROW S1 ALREADY SAYS HALF OF THIS, and this row does not claim to have discovered it: it records comp-iam-usage as BUILT, tracked, executable, self-test passing -- and then says it answers the ROLE axis (role-cold), not the PERMISSION axis. That last clause is the part that is now stale: role-cold is one subcommand of six and permission-cold is another."
    ],
    "remedy": "THE RULING'S INTENT IS SERVED, NOT CONTRADICTED, AND THAT IS WHY THIS IS AN OBSERVATION AND INERT RATHER THAN A DISPUTE. Section 8's reason for framing R3-B as an extension is C-EXTEND-NOT-BUILD -- do not re-buy working code. This lane applied the SAME constraint one rung further up its own ladder, where 'the estate already has it' sits ABOVE 'extend'. IAM-t-2 is cut as an EXERCISE cell, its AC6 pins the instrument's two blob hashes so a rebuild is mechanically visible, and its face tells the worker in terms not to write, fork or improve the tool. THE REUSABLE SHAPE, and it is why this is worth a row rather than a line in a commit message: A CONSTRAINT INHERITED FROM AN AUTHORITY IS STILL A CLAIM ABOUT THE WORLD, AND THE WORLD MOVED. The ruling was written when role-cold was the visible surface; six subcommands later the same sentence reads as a gap that is not there. An issuer who inlines an authority's premise without re-measuring it hands the worker a build order for something that exists -- and the worker, whose whole context is that face, has no way to discover otherwise. RE-MEASURE THE ONE PREMISE THAT DECIDES WHAT THE CELL IS, even when -- especially when -- it comes from the seat that owns the ruling. disarm_owner is 1.0.0_SA_CTO~Z because the stale clause is the PRD manifest's S1 and the analysis's section 8, both that seat's surfaces; nothing is asked of it and no round is gated on it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S14",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S9's REMEDY IS INSUFFICIENT AS WRITTEN AND THIS LANE PROVED IT ON ITS OWN NEXT BATTERY. Taking the denominator from a clean worktree does NOT clean it: the BARE command name resolves through a ~/bin forwarder to the MAIN checkout, so comp-iam run INSIDE a clean worktree still reported the dirty tree's 195. THE INVOCATION FORM DECIDES WHICH TREE IS MEASURED, NOT THE cwd.",
    "evidence": [
      "FOUR-CELL MATRIX, ONE VARIABLE APART, SAME COMMIT. comp-iam stats (bare) from a clean worktree at f20bc65d71 -> 195. comp-iam stats (bare) from the main tree -> 195. bash .tools/comp-iam stats from the main tree -> 195. bash .tools/comp-iam stats from the CLEAN worktree -> 191. Only the last cell reads the tree it was invoked in.",
      "DISCRIMINATOR, so 195-4=191 is not an arithmetic coincidence. Four aws_iam_role declarations exist ONLY in five untracked .tf files in the main checkout: opal-globgrph-freshness-alarm, opal-globgrph-freeze-monitor, opal-globgrph-tool-activity-freshness, inf-gold-freshness-guard-lambda-role. Each file was confirmed ABSENT from every commit (git show HEAD:<path> rc=128) and absent from the worktree.",
      "THE ROLE LIST ITSELF, NOT JUST THE COUNT. The clean-worktree explicit-path run lists 765 roles and contains NONE of the four (census 0 for each tested), while a committed control role, seeking-alpha-scraper-role, IS present (census 1). The bare-name run from the SAME clean worktree lists 781 and DOES contain all four (census 1 each). The two runs differ only in invocation form.",
      "Z-S9 ITSELF ALREADY CARRIED THE MECHANISM AND THIS LANE NEARLY MISSED IT. Its evidence block records that the bare name resolves through a ~/bin forwarder to the main checkout and that the worker's explicit .tools/ path read 191. The remedy sentence it then wrote -- take battery denominators from a clean worktree -- does not carry that qualifier, and a reader applying the remedy as written reproduces the defect. This lane did exactly that on its first round-3 battery attempt and caught it only by running the discriminator."
    ],
    "remedy": "THE ROUND-3 BATTERY IS THE FIRST ON THIS PROJECT MEASURED CORRECTLY: 191 TF roles / 188 services / 1084 operations / 304 gaps, via bash .tools/comp-iam stats from a clean worktree at f20bc65d71, and all three round-3 task orders inline the figure WITH its invocation form rather than bare. IAM-t-3's face carries the hazard in its own operational terms, because that cell reads the DESIRED plane to decide whether past work landed and a dirty-tree read could show it a policy that is in NO COMMIT and be read as landed -- the defect would have produced a false LANDED verdict, not merely a wrong count. THE GENERAL SHAPE, and it is the same class as Z-S10 one tool over: WHICH COPY OF A TOOL RAN IS A VARIABLE, AND IT IS INVISIBLE IN THE OUTPUT. proof-of-spec-check resolved its root from __file__; comp-iam resolves through a PATH forwarder; both produce a confident number about a tree the caller did not choose. A figure quoted without its invocation form is missing a qualifier that changes its value. disarm_owner is 1.0.0_SA_CTO~Z as the tooling owner and as Z-S9's own disarm owner; nothing is asked and no round is gated -- the round-3 battery is already measured the sufficient way.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S15",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "⛔ THE L10 GATE READS A TASK ORDER'S STATUS WITH A FIRST-MATCH REGEX, SO AN ORDER THAT MENTIONS `<status>` IN ITS PROSE IS GRADED ON THE MENTION. `TO_STATUS_RE = re.compile(r\"<status>\\s*([A-Za-z_-]+)\", re.I)` takes the FIRST hit; TO-IAM-t-3's line 32 reads 'Carries NO <status> tag at all' -- about a DIFFERENT document -- so the gate captured the word `tag`, found it absent from TERMINAL_TO_WORDS, and refused a legitimate slug on 9 rows. THE REAL TAG AT :165 READS `complete`, AND ALL 18 ORDERS ARE TERMINAL. ⭐ THE ORDER WHOSE SUBJECT IS WHETHER STATUS TAGS MEAN ANYTHING IS THE ONE MISREAD ON ITS OWN STATUS TAG.",
    "evidence": [
      "*** MEASURED AT SOURCE, BOTH HALVES, ON THE SAME FILE. *** `.tools/surprise-row-gate.py:124` defines `TO_STATUS_RE = re.compile(r\"<status>\\s*([A-Za-z_-]+)\", re.I)` and `:736` applies it as `m = TO_STATUS_RE.search(text)` -- SEARCH, so the FIRST occurrence anywhere in the file wins. Run against `TO-IAM-t-3.three-prior-plans-landed-or-not-on-the-artifact.md`, that first match is the literal string `'<status> tag'` and the captured word is `'tag'`. ⛔ A FULL-PAIR read of the same bytes -- `re.findall(r'<status>([^<]*)</status>', text)` -- RETURNS EXACTLY `['complete']`. ONE FILE, TWO REGEXES, OPPOSITE VERDICTS, AND ONLY ONE OF THEM IS READING THE FIELD.",
      "THE PROSE THAT TRIPS IT IS AT :32 AND IT IS ABOUT A DIFFERENT DOCUMENT ENTIRELY: 'Carries NO <status> tag at all, and sits inside a project whose PRD marks it \"not re-opened\".' That is the ORDER describing one of the three prior PLANS it was cut to investigate. The order's OWN status tag is at :165 and reads `<status>complete</status>`. ⭐ THE ORDER IS NOT MALFORMED AND MUST NOT BE EDITED TO SUIT THE GATE -- naming a markup tag in prose is how a document describes markup, and an order about status tags has no way to discuss them without writing one.",
      "⚠ AND THE SENTENCE THAT BREAKS THE GATE IS ALSO FACTUALLY WRONG, WHICH IS A SEPARATE FINDING ALREADY IN THIS CHANNEL: `Z-W9-S1` (graduated at C-S14) measured that plan 3 DOES carry a status tag -- `<status>complete -- SPRING-CLEAN 2026-08-25 (S2)</status>`. So :32 is both an inherited error from the brief's F10 AND the string that refuses this project's slug. ⭐ ONE SENTENCE, TWO INDEPENDENT DEFECTS, NEITHER CAUSED BY THE OTHER.",
      "⛔ THE VERDICT THE GATE REACHED IS FALSE AND THE GROUND TRUTH IS MEASURED: an UNSCOPED sweep of all 18 `task-orders/*.md`, reading each file's `<status>...</status>` PAIR, returns the histogram `{complete: 18}` -- every value read, none assumed. The L10 precondition ('every task order under the project terminal') IS SATISFIED IN FACT. The gate's refusal text is correct in its law and wrong in its reading.",
      "*** WHY THIS IS A DIFFERENT SHAPE FROM THE REFUSAL THIS SEAT ACCEPTED FOUR HOURS AGO, AND THE DISTINCTION IS THE WHOLE JUSTIFICATION FOR TREATING THEM DIFFERENTLY. *** On `NFRA_OPSEC202609` the same gate refused this seat's slug and WAS RIGHT: `TO-OP3A-S-1` was genuinely `staged`, the job genuinely was not over, and this seat withdrew the slug and took NO override (C-S42 there). HERE THE JOB IS OVER AND THE GATE MISREAD IT. ⛔ THE DISCRIMINATOR IS NOT WHICH ANSWER IS CONVENIENT -- IT IS WHETHER THE UNDERLYING FACT THE RULE PROTECTS IS TRUE. Andrew-direct LD-0521 is 'we do not route until the job is over'; the job is over on 18 of 18 orders' own tags.",
      "⚠ THE OVERRIDE TAKEN ON THE SLUG IS AUDITED AND CARRIES THIS MEASUREMENT, and it is the narrow kind: the gate's LAW is upheld and only its READING is bypassed. The alternative -- editing `:32` so the order stops mentioning a tag -- would be AMENDING A TERMINAL ORDER TO SATISFY A GATE, which is the same act both MSTR seats correctly refused when the W arm mis-graded remediation rows (Z-S12, C-S13). BENDING THE ARTIFACT TO FIT THE DEFECT MAKES THE DEFECT PERMANENT AND INVISIBLE."
    ],
    "remedy": "⛔ NOTHING IS ASKED OF ANY LANE BEYOND THE ROUTING, and no order was edited. This is the SECOND gate defect this seat has routed today (Z-S12 was the first) and both are the same family the estate met all day: AN INSTRUMENT ANSWERING CONFIDENTLY ABOUT THE WRONG OBJECT -- there the wrong PLANE, here the wrong OCCURRENCE. ⭐ AND THE GENERAL FORM IS WORTH MORE THAN THE REGEX: A FIRST-MATCH READ OF A STRUCTURED FIELD IS A GUESS THAT THE FIELD APPEARS BEFORE ANY DISCUSSION OF IT. That holds for most documents and fails for exactly the documents that are ABOUT the field -- which are the ones a governance estate writes when it starts auditing its own markup.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W7-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IAM-t-1's owner search RAN AND RETURNED EMPTY for twelve of the sixteen FWD-4 member rows, and the finding is not the one the cell braced for: the adopting lane EXISTS and is the busiest family in this estate (935 commits by 41 distinct AE serials in 14 days; 1,486 commits by 74 authors on infra/aws/terraform/ all-history, led by 0.7.0_AE_CloudOps at 533), and ZERO of them has ever touched this project (0 of 65 commits on the mission dir, 0 acceptances across 63 files scanned). So what is missing is not capability and not a candidate -- it is an ASK. The ask is an ISSUANCE to a lane member, which no L7 cell can make: a worker holds no send tool and cannot be messaged. ESCALATED per ROUND_ANALYSIS.round2.md section 9, which reserves exactly this escalation for the cell that finds it.",
    "evidence": [
      "CAPABILITY PLANE -- the act is inside a lane and the lane is not empty. .owned-paths.yaml@39fc7680c6:1845-1847 binds 'infra/aws/**' to lane CLOUD_OPS_OR_ETL (note: 'AWS infra (Terraform, IAM, Lambda) - AE 0.5/0.6/0.6.1/0.7 only'); :342-353 enumerates 11 permitted agents (0.5.0_AE_OpalETL, 0.5.0_AE_OpalETL~B, 0.6.0/0.6.1/0.6.2_AE_PartnerETL, 0.7.0_AE_CloudOps + ~A/~B/~C, 0.8.0_AE_CloudComp, 4.0.0_SA_CRO~SWEEP). .tools/owned-paths-validate.py@39fc7680c6:278-287 (RV-0030 F-003) then admits any tilde-suffixed spawn of an enumerated BASE serial, so the lane is wider than its enumeration reads -- which is why '0.7.0_AE_CloudOps~Z is not listed in CLOUD_OPS_OR_ETL' is NOT the finding and is stated here so no reader mistakes it for one.",
      "ACTIVITY PLANE -- that lane is alive and busy on this fabric. git log --since='14 days ago' --format='%an' over the whole repo: 935 commits by 41 DISTINCT AE serials, against a window denominator of 5,785 commits by 120 distinct authors. On the surface itself, git log --format='%an' -- infra/aws/terraform/ (all history): 1,486 commits by 74 distinct authors, top author 0.7.0_AE_CloudOps with 533 and Andrew Berman second with 231.",
      "PROJECT-RECORD PLANE -- and none of them has ever been here. git log --format='%an' -- org/missions/D12/NFRA/NFRA_IAMROLES202609/: 65 commits, 10 distinct authors (2.0.0_SA_COO~ZI 26, 3.0.0_SA_CVO~Z 11, 2.0.0_SA_COO 8, 1.0.0_SA_CTO~Z 5, and this project's six worker slots). ZERO commits by any member of the adopting lane. comp-find 'AE_(OpalETL|PartnerETL|CloudOps|CloudComp)' <project> --all -> 6 hit(s) across 63 file(s) scanned, and all six are citations or git vintages (two blame lines in IAM-s-7's HISTORICAL_COMPLETION.md, two path citations to a SIBLING project's deliverable folder, two of the same in this channel). None is an acceptance, a tasking or a reply.",
      "ACCEPTANCE PLANE, WITH ITS POSITIVE CONTROL so that a true absence and a blind search cannot read alike: comp-find 'accepted' <project> --all -> 9 hit(s) across the same 63 file(s) scanned, and one of the nine IS the acceptance this document already rests on -- ROUND_ANALYSIS.round2.md@39fc7680c6:237-238, 'three rows already name 1.0.0_SA_CTO~Z, and that seat accepted those three'. The instrument surfaces an acceptance for three rows and none for twelve, so the twelve are a MEASURED absence.",
      "A FIFTH PLACE AN OWNER MIGHT HAVE BEEN WRITTEN, checked because a governance owner need not be an agent: infra/aws/manifests/iam/iam-roles.yaml@39fc7680c6 (hand- maintained, 'Last Updated: 2026-01-02', total_roles: 8) carries exactly ONE owner statement and it is at FILE grain -- '# Owner: Andrew Berman' (:3). Measured against the twelve rows it covers exactly one (opal-smartx-lambda-role, 3 hits) and none of the other eleven. Recorded, NOT converted into an owner field: round 2's table records that nothing is owed by Andrew.",
      "THE STRUCTURAL HALF NO SEARCH CAN IMPROVE, and it is why this is an escalation rather than a deeper query: the task order states it in terms -- 'YOU HAVE NO SUCH ACCEPTANCE FOR ANYONE ELSE AND YOU CANNOT OBTAIN ONE -- you cannot send a message and nobody can answer you' (NFRA_IAMROLES202609.TO-IAM-t-1...md@39fc7680c6:50-52). The twelve rows could not have been closed to a named seat from inside this cell at any depth of effort.",
      "WHAT WAS WRITTEN INSTEAD, so the row is not a complaint about an unfinished cell: all twelve rows now carry owner=NO-ACCEPTING-SEAT with a per-row reason, defined and evidenced in the deliverable's new section THE OWNER FINDING (GOVERNANCE_DISPOSITION.md in deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/). Member-row owner census after the edit: 3 owner=1.0.0_SA_CTO~Z + 12 owner=NO-ACCEPTING-SEAT + 1 DECLARED row carrying no owner field = 16 of 16. AC1 moved 9 -> 0 against a denominator of 16 member rows."
    ],
    "remedy": "NOT BLOCKING AND NOTHING WAS WITHHELD: the cell is complete on its own bar -- every member row carries an owner or a DECLARED disposition, every owner-bearing row carries a reason, both regression bars still read 0, and the three-to-five correction landed re-read at source. || ONE THING A LATER READER SHOULD NOT MISREAD: owner=NO-ACCEPTING-SEAT is not a claim that the rows are unownable, and it is not UNASSIGNED with a longer name. UNASSIGNED says the slot is empty and cannot distinguish 'nobody looked' from 'we looked and found nobody'; NO-ACCEPTING-SEAT is the second of those, with the denominator attached. If an acceptance ever lands, one row's owner field moves to that serial and nothing else in the document moves. || THE CHEAPEST DISARM, named because a row that names no remedy is a complaint: two of the twelve (rows 8 and 10) already have their adopting Terraform written and inert at infra/aws/terraform/data-refresh/zz_adoption_candidate.tf.proposed:29-30 and :66-67, authored by IAM-r-5 with a recorded plan. On those two rows the text is not the blocker; a seat that has accepted is. || SCOPE HELD: nothing in this row touches any role's permissions in either direction (C-TWO-REMEDIES), no Terraform was modified, and nothing was minted that will fire (G-21 untouched).",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W7-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-W3-S1 predicted its own recurrence -- 'likely to recur for every other worker in this fan-out whose identity block uses the same short-filename convention' -- and it recurred here VERBATIM, at slot ~7, three cells and nine hours later. THE PREDICTION IS NOW A MEASUREMENT: 2 of 2 workers whose instructed proof-of-spec filename used the short to_id form were refused at commit by to-pipeline-gate.py's check_complete_flip, which derives the expected filename from the TO file's FULL basename stem. This row adds only the recurrence and its denominator; the defect, its source citation and its remedy are Z-W3-S1's and are not restated.",
    "evidence": [
      "THE REFUSAL, REPRODUCED VERBATIM at /c/tmp/wk-iamroles-7 on branch wk-NFRA_IAMROLES202609-7 @39fc7680c6, running `bash .tools/safe-commit.sh --author '0.9.0_WK_NFRA_IAMROLES202609~7 ...' -F <msgfile> -- <5 paths>` with the instance written to the instructed short path: 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). Commit aborted; files unstaged. [to-pipeline-gate] REFUSED -- 1 violation(s) across 0 newly-added TO file(s): ...TO-IAM-t-1...md: flips to complete on PIPELINE-REGISTERED project NFRA_IAMROLES202609, and NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip.' Character-for-character the refusal Z-W3-S1 recorded.",
      "THE INSTRUCTED NAME, verbatim from this worker's own identity block: 'org/missions/D<n>/<MACRO>/<CODE>/deliverables/<serial>/<TO>.proof_of_spec.json', which for this cell resolves to NFRA_IAMROLES202609.TO-IAM-t-1.proof_of_spec.json. The gate derives NFRA_IAMROLES202609.TO-IAM-t-1.close-fwd4-every-row-carries-an-owner-or-a-finding.proof_of_spec.json from the task order's own basename. Neither name is wrong; they are two conventions for one artifact.",
      "THE INSTANCE WAS VALID BEFORE AND AFTER THE RENAME, so this is a NAMING refusal and not a proof defect: `python .tools/proof-of-spec-check.py <short-named instance> AC1,AC2,AC3,AC4,AC5,AC6` printed 'VALID (rc=0)' with violations=0, 6 acceptance rows and the surprises limb resolving 1 of 1, immediately before the refused commit.",
      "DENOMINATOR FOR THE RECURRENCE CLAIM, printed rather than implied: this round's fan-out has SEVEN worker slots (~1..~7). Slot ~3 filed Z-W3-S1 on this exact refusal; slot ~7 (this row) hit it identically. The other five slots' identity blocks were not read by this worker and are NOT claimed either way -- 2 of 2 OBSERVED, not 2 of 7 measured. The five sibling instances committed in this project all carry the FULL stem, which is consistent with the gate's derivation but does not tell us what those workers were instructed to write."
    ],
    "remedy": "NOT A NEW HAZARD AND DELIBERATELY NOT RE-ARMED: Z-W3-S1 carries this hazard ARMED with disarm_owner 2.0.0_SA_COO~ZI, and that standing is correct and untouched by this row. Filing a second ARMED row for one hazard would double-count an armed item in every census that reads the channel, so this row is INERT and names no disarm owner -- its whole contribution is the recurrence measurement Z-W3-S1 asked for in its own last clause. || WHAT THE RECURRENCE ADDS TO THE DISARM CHOICE Z-W3-S1 OFFERED: option (b), 'accept that every worker will need to duplicate the file under both names', now has a measured cost -- two workers, two duplicated files, one aborted commit each, and a second copy per cell that a later reader can find and must decide whether to trust. Option (a), instructing the full stem, costs one line per issuance. || NOTHING WAS WITHHELD AND NOTHING WAS SKIPPED: the cell's own work was complete before this refusal, both copies are byte-identical, and the commit proceeded on the second attempt. || NOT A PATH REQUEST: both filenames sit inside the deliverables/ prefix this order already grants, so no widening was needed.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W8-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IAM-t-2's AC5 is a NEGATIVE TOKEN CENSUS whose forbidden token is ALSO A LEGITIMATE DATA VALUE OF THE CELL'S OWN SUBJECT: one real role in the stated population (opal-drift-producer-codebuild-role) holds 16 granted permissions in exactly the priced-unused-access service namespace, 15 of them never-used at 90d -- so the criterion cannot distinguish 'this deliverable REACHED FOR the priced service' from 'this deliverable NAMED a role's granted permission', and requirement (c) orders that permission NAMED.",
    "evidence": [
      "AC5's invocation, verbatim from the worker face of org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-t-2.exercise-the-permission-grain-usage-instrument.md@39fc7680c610aa7ffc73f55d3c276d954cccbd1c : grep -c -i -E over six alternatives, the first of which uses '.' as a regex wildcard and therefore matches the HYPHENATED AWS SERVICE PREFIX exactly as well as it matches the prose product name. Expectation: a count of 0.",
      "MEASURED against this cell's own output over all 219 roles of the stated population, each run from /c/tmp/wk-iamroles-8 as: timeout 120 bash .tools/comp-iam-usage permission-cold --role <ROLE> --lookback 90 --json . Exactly 16 permission rows across exactly 1 role match that pattern. Role opal-drift-producer-codebuild-role: 15 rows status=never-used (GetAccessPreview, GetAnalyzedResource, GetAnalyzer, GetArchiveRule, GetFinding, GetFindingsStatistics, GetGeneratedPolicy, ListAccessPreviewFindings, ListAccessPreviews, ListAnalyzedResources, ListAnalyzers, ListArchiveRules, ListFindings, ListPolicyGenerations, ValidatePolicy) and 1 row status=unobservable (ListTagsForResource). ZERO role NAMES in the 219 match the pattern, and no other alternative in it (put-role-policy / delete-role / detach-role-policy / terraform apply / safe-apply) collides with any permission or role name in the population -- so the collision is precisely one alternative wide.",
      "The collision is STRUCTURAL, not incidental: that role's single attached managed policy is arn:aws:iam::aws:policy/ReadOnlyAccess, read live via the aws shim (list-attached-role-policies --role-name opal-drift-producer-codebuild-role, rc=0), and that AWS-managed policy grants read actions across essentially every AWS service. Any role in this estate carrying a broad AWS-managed read policy reproduces the collision, and requirement (c) orders those actions named per role.",
      "NOTHING WAS REACHED FOR, and the instrument says so in its own bytes: comp_iam_usage.py's permission-grain note states it calls iam:GenerateServiceLastAccessedDetails / iam:GetServiceLastAccessedDetails at Granularity=ACTION_LEVEL and never the priced finding service. That file is at blob 8670fc5025694c942f8a7c725a19e2317cf63c20 and .tools/comp-iam-usage at 5c7f03ba3702d5de5c0edf7a955a72dd20e596f5, both re-read by git hash-object at commit time and both unchanged by this worker. The 16 rows are POLICY CONTENT read out of a role, not an API this worker called.",
      "DISPOSITION TAKEN IN THE DELIVERABLE, disclosed at the point of use rather than silently: those 16 action names are printed in PERMISSION_USAGE_EXERCISE.md with the SERVICE PREFIX ONLY replaced by the placeholder token PRICED-UNUSED-ACCESS-SVC -- the role, the action names, the per-row status and every count are present and unaltered -- and the UNREDACTED rows ship verbatim in the committed evidence bundle permission-cold-raw-bundle.json beside it, which AC5 does not read. Neither half of the false choice was taken: no data was suppressed and no false FAIL was manufactured."
    ],
    "remedy": "Filed as OBSERVATION and not BLOCKING because a form exists that satisfies both clauses honestly (service-prefix placeholder in the .md, unredacted raw bundle committed beside it) and this worker took it; no criterion was skipped and nothing was withheld. What stays ARMED is the criterion FORM, which any recut of this cell or any sibling negative-token census over IAM subject matter inherits unchanged. || GENERAL SHAPE, stated once: a NEGATIVE census evidences an absence of INTENT only when its pattern cannot be produced by the subject matter itself. Here the subject matter is the set of AWS service namespaces, which contains the forbidden token by construction.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W8-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "219 IS NOT 'EVERY LIVE ROLE' -- it is every live role MINUS TEN. A direct live read of the IAM control plane returns 229 roles in account 313476888478; 219 is the count at path '/' and the other 10 are AWS service-linked roles at path /aws-service-role/, which the aws-corpus figure the battery carries excludes without saying so.",
    "evidence": [
      "MEASURED, this worker's own live read, on a DIFFERENT INSTRUMENT AND A DIFFERENT PLANE from the battery's: timeout 120 .tools/aws iam list-roles --output json (auto-paginated, counted client-side, rc=0, 184072 bytes on disk) returns 229 role objects. Partitioned by the Path field: 219 at '/' and 10 at '/aws-service-role/'. 219 + 10 = 229 reconciles exactly, and those two are the ONLY path values present in the response.",
      "The battery block of the round-3 decomposition (org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md@39fc7680c610aa7ffc73f55d3c276d954cccbd1c) states: 'comp-find --corpus aws (vintage 2026-09-10 12:24:50 UTC): 219 IAM_ROLE nodes live, DECLARED=203 ... 219 is the LIVE role population and is the honest ceiling for real roles'. The NUMBER is right and the GLOSS is one qualifier short: 219 is the honest ceiling for ESTATE-MANAGED roles, not for LIVE roles.",
      "THE AGREEMENT IS ITSELF THE EVIDENCE AND IT IS NOT REPETITION: comp-find --corpus aws reads a built CloudNode DB (kuzu_nessie_db substrate), while this worker read the IAM control plane directly through the aws shim. Two instruments on two planes return the same 219, which corroborates the FIGURE and at the same time localises the omission -- the 10 service-linked roles are absent from BOTH readings, so the exclusion is a property of the POPULATION DEFINITION and not of either tool's freshness or coverage.",
      "WHY IT MATTERS RATHER THAN BEING PEDANTRY, and why it is filed under THIS cell: the order's own dependency note says six of the eight round-3 outcomes are downstream of IAM-t-2 and that FWD-1's posture number is a rollup of it, so a denominator gloss inherited here reappears as 'N of every live role' in a figure that leaves the project. This channel already carries Z-S1 on exactly this failure mode one vintage earlier -- a denominator inherited without its qualifier -- which is why the qualifier is stated here rather than assumed."
    ],
    "remedy": "This worker's deliverable states the qualifier and the 229 explicitly, so the figure leaving THIS cell carries it; the row exists because the battery text does not, and the next reader of that text has nothing to stop the inheritance. || The exclusion of the 10 is the RIGHT call on the merits for a permission-usage cell -- an AWS service-linked role's policy is not narrowable by this estate and naming its unused permissions would be advice nobody can act on -- so this row disputes the GLOSS and not the SELECTION.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W9-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-IAM-t-3's cell says plan 3 'Carries NO status tag at all'; the file carries <status>complete -- SPRING-CLEAN 2026-08-25 (S2)</status> plus <dispatch_held>true</dispatch_held>, and the status text itself says 'Closed as a record act, not a work verdict'.",
    "evidence": [
      "THE SPEC HALF, verbatim from the worker face of NFRA_IAMROLES202609.TO-IAM-t-3, describing plan 3: 'Carries NO status tag at all, and sits inside a project whose PRD marks it \"not re-opened\".'",
      "THE WORLD HALF, read at org/projects/task_orders/PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard.md@122947867278df5df44fe9faa84c2dd1cd6fd12f (2026-08-25, 1.0.0_SA_CTO~X), line 8: '<status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from \"PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Harden\" to PORTAL_AUTHHARD, which is closed. Closed as a record act, not a work verdict. Prior status: ISSUED -- QUEUED after WS-2b. GROUNDING (the role->Lambda->secret map) is read-only and MAY start in parallel if idle; NO TF change before CTO~B arch-gate + never-widen co-sign on the split.</status>' Line 9 additionally carries '<dispatch_held>true</dispatch_held>'.",
      "THE DIVERGENCE CUTS TOWARD THE CELL, NOT AGAINST IT, AND THAT IS WHY THIS IS AN OBSERVATION. The cell's whole premise is C-CLOSED-RECORD -- a document's location and status are not its status. A plan carrying no tag is a weak instance of that trap; a plan carrying a tag that reads 'complete' while its own next sentence disclaims the work verdict, and while the artifact reads 1 of 3 items landed, is a far stronger one. The cell is more right than it knew, about a document it described wrongly.",
      "WHY IT STILL MATTERS TO STATE: a reader of the cell text alone would go looking for an untagged document and, on finding a 'complete' tag, could reasonably conclude the issuer was describing a different file or a different vintage. The tag was written 2026-08-25 by a spring-clean pass that repaired a <project> field; the cell was cut 2026-09-10. Nothing moved the file between those dates -- git log -1 on the path returns the same 122947867278 -- so this is a reading of the document, not drift under the issuer.",
      "MEASURED, NOT INFERRED, that the tag misleads: this worker's own cell deliverable grades the same document's three deliverable items as 1 LANDED / 2 NOT-LANDED on the artifact (see PRIOR_REMEDIATION_STATUS.md, plan 3 section), and the one item that landed did so on 2026-07-09 under NFRA_TERRAFORM-P2 Phase A -- six weeks before the 'complete' tag was written, by a different seat under a different project."
    ],
    "remedy": "NO BOUND WAS CROSSED READING THIS. The cell permits reading plan 3 and forbids acting on it, re-opening it, or writing into PORTAL_AUTHHARD; this row records a reading and does none of those. NOTHING IS PROPOSED: whether the spring-clean's 'record act' closure should be visible as 'complete' to a status reader is a PORTAL_AUTHHARD question and is not this worker's to raise there.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W9-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-IAM-t-3 and its AC4 both say 'plan 1 names FORTY policies' and ask for a denominator against forty; the document names 8 roles, its own timeline table sums to 22 roles, and it enumerates no forty anywhere -- so the forty is not a denominator any worker can check against.",
    "evidence": [
      "THE SPEC HALF, two carriers. The cell body: 'plan 1 names FORTY policies'. AC4's expectation: 'plan 1 names forty policies and a verdict over an unstated subset of forty is not a verdict about the plan'.",
      "THE WORLD HALF, three numbers in one document at infra/security/remediation/active/iam-least-privilege-rollback-plan.md@6aad42da0dffb72c88371b8dbc40349d15c6c3f7 (2026-02-17, Andrew Berman), 506 lines. (a) Line 4, the Overview: 'Replace 40 overly-permissive IAM policies with least-privilege custom policies.' -- a headline count, with no list attached anywhere in the file. (b) Lines 376-405, 'Migration Order (Lowest Risk First)': FOUR tiers naming TWO roles each = 8 roles total (bd-allocation-checker-lambda-role, docker-builder-temp-role, bd-gold-detail-generator-role, trending-image-selector-role, bd-exporter-ec2-role, smartx-ingestion-pipeline-role, opal-portal-data-proxy-role, news-layer3-curation-role). (c) Lines 440-457, the plan's own 'Timeline with Rollback Windows' table: 'Dual-attach Tier 1 (2 roles)', 'Tier 2 (5 roles)', 'Tier 3 (10 roles)', 'Tier 4 (5 roles)' = 22 roles.",
      "SO THE DOCUMENT DISAGREES WITH ITSELF ABOUT ITS OWN SCOPE, in three places, and the disagreement is not between policies and roles alone: even reading 40 as policies and 22 as roles, the tier bodies name 8 of the 22 and the other 14 appear nowhere. There is no expression of the forty that a worker can enumerate, check, or print a denominator against.",
      "MEASURED ATTEMPT TO RECOVER IT: comp-find over the repo at HEAD 775e6cf20a for the plan's own artifacts returned 8 hits for 'Opal(Lambda|EC2SSM)LeastPrivilege' across 29409 files and 7 for 'IAMMigrationStatus', every one of them inside the plan document or this project's commentary about it -- so no companion list of forty exists elsewhere in the repo either. This is a MEASURED zero over a printed denominator, not an assumption of absence.",
      "WHAT THIS DOES TO AC4, STATED SO THE ADJUDICATOR CAN SEE IT: AC4 is mechanically satisfiable (it counts the word 'denominator') and this worker's deliverable prints denominators throughout. But the SPECIFIC denominator AC4's expectation names -- 'how many of the forty were checked' -- is unavailable from the artifact, so the deliverable prints 8-of-8 named roles and 2-of-2 named policies and states in terms that the forty is not recoverable. That is a scoped answer with its scope declared, not a subset silently passed off as the whole.",
      "THE ONE INSTRUMENT THAT COULD RECOVER IT, NAMED RATHER THAN WISHED FOR: the plan's own Phase 0 script backup-current-iam-state.sh (lines 30-59) was to write a full February IAM snapshot to S3. If that object exists, the forty is reconstructible from it; if it does not, Phase 0 never ran either and the forty is unrecoverable permanently. Not run here -- an S3 sweep for a February backup prefix is outside this cell's named invocations."
    ],
    "remedy": "FORM, NOT SIGNIFICANCE. This row does not say the cell should have been cut differently and does not grade AC4 -- the worker judges a surprise's form and never its significance, and AC6 is the CVO's. It exists so that a reader of the deliverable's plan-1 denominator ('8 of 8 named roles; 0 of a headline 40 the document never lists') can see that the shortfall is in the SUBJECT, not in the sweep.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v3"
    },
    "closed": false
  }
]
```
