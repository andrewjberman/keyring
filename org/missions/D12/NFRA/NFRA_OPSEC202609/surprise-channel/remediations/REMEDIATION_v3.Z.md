# NFRA_OPSEC202609 -- surprise channel, REMEDIATION v3 (site Z) -- THE ROUND-3 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 3, 2026-09-10 ~20:4xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, BOTH LIMBS, SOURCE = `comp-surprise --project NFRA_OPSEC202609` (JSON view, `_doc==INVESTIGATION`
rows only, disposition read via each row's `_latest` field -- the tool's own latest-carrier fold, cross-checked
against a direct parse of `INVESTIGATION_v1.md`'s and `ADJUDICATION_v1.md`'s fenced JSON blocks for the count
and for the open-item id set, which agree)**:

```
190 items | UNDISPOSITIONED 0 | GRADUATED 126 | DISMISSED_WITH_REASON 64
1 of 1 JUDGMENT criteria graded (S1-AC7 PASS at C-S37 @9cae36a5f0, 2026-09-10T13:45Z)
Task orders: 35 of 35 terminal (32 complete / 2 cancelled / 1 superseded), independent full-pair
  <status>-tag read of every file under task-orders/, not the gate's first-match regex -- TO-OP3A-S-1,
  the project's last non-terminal order, closed via re-seat ~4 -> ~6 (@1f87188985) and a clean deploy+
  commit by the re-seated worker (@1d187e8673.., @1d103b4651, @ea5d79c9c1).
CONTROL: the same call on NFRA_IAMROLES202609 returns 38 items / 0 open / 31 armed -- the census fires
         on a second project and returns a DIFFERENT number, so OPSEC's 0 is a measurement, not a stuck
         cache or a first-project default.
```

**WHAT THIS DOCUMENT CARRIES.** Round 2's slug (`REMEDIATION_v2.Z.md`) carried 99 rows (94 graduated by round 2's
own adjudications + 5 carried from round 1). Since then this project accumulated 27 MORE graduated items across
rounds 3 and 3A (S169-S178, W1-S1..S5, W2-S1, W3-S1, W4-S1, W5-S1..S4) and 5 of those 27 were themselves the
ADJUDICATION-track grade/correction rows that graduate nothing new on their own (C-S41/C-S43/C-S44/C-S45/C-S46 --
excluded from THIS document's row count for the same reason C-S1..C-S40 are excluded from round 2's: an
adjudication row is not itself a hazard needing a remedy). **This document carries the 22 investigation-plane rows
that are GRADUATED and were NOT YET carried by any prior remediation document** -- computed as the set difference
(GRADUATED ids) MINUS (ids already present as an `id` in `REMEDIATION_v1.Z.md` + `REMEDIATION_v2.Z.md`), verified
by direct enumeration against both files, denominator 104 already-carried ids, 22 uncarried.

**HOW `remedy`, `owner` AND `disarm` WERE DERIVED, stated so none is over-read, following round 2's own stated
method exactly.** `remedy` is carried **verbatim from each row's own `notes` field** where the row stated one;
three rows (`Z-W1-S1`, `Z-W1-S4`, `Z-W1-S5`) stated neither `notes` nor `disarm_owner` and are marked as such
rather than backfilled. `owner` is the lane named by the row's own `disarm_owner`, defaulting to
`2.0.0_SA_COO~Z` (this project's issuer) where a row names none. **`disarm.state` is `ARMED` for 14 of the 22
by default (nothing here is claimed disarmed without a specific, cited exercise) and `DISARMED` for 8, each with
its own confirming citation in the row's `disarm.note`** -- this departs from round 2's blanket-`ARMED`
convention because this round's own record already contains the confirming exercises for these 8 (a re-seated
worker's clean deploy for `Z-W5-S2`/`Z-W5-S3`, a successor's write under a widened grant for `Z-W4-S1`, this
seat's own L9 judgment grade for `Z-S169`, a live SNS read for `Z-S173`, the order that was finally cut for
`Z-S174`, a self-correction where nothing was ever live for `Z-S176`, and an independently-reverified-already-live
guard for `Z-W3-S1`) -- carrying a known disarm forward as still-ARMED would be a less accurate record, not a
more conservative one.

**AUDITED GATE OVERRIDE, disclosed here and not only in the commit,** matching round 2's own disclosure: as on
`NFRA_REPORT`, `_coordinate_violations` refuses a NEW row carrying `W<n>` from a non-worker committer while
protocol s.5 requires the remediation id to EQUAL the graduated id. This slug only ever CARRIES ids already
minted by their originating rows; it mints none.

**What this document is NOT.** It routes nothing and names no limb. Every `remedy` above is a RECOMMENDATION
to its named `owner`, not an instruction; the recut, the L4/L6 acts, and the coverage read are the reader's.
The CVO's engagement with this round ends here.

---

```json
[
  {
    "id": "NFRA_OPSEC202609-Z-S169",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TWO OF THE TWENTY CRITERIA IN ROUND 3'S ISSUANCE ARE UNSATISFIABLE BY A CORRECT BUILD, AND BOTH ARE THIS SEAT'S. S1-AC4 expects 'the response shows refusal or challenge, and the entry does NOT appear in the entry store' -- the first clause is an EDGE/WAF shape (refuse at the wire) and C-19, quoted VERBATIM on the same face 24 lines away, declares the edge half UNBUILDABLE-not-deferred; the only permitted control is on-box and form-level, and a honeypot ACCEPTS AND FLAGS BY DESIGN, so neither clause can hold (the scripted probe returned HTTP 200 with confirmation text byte-identical to a genuine success, and the entry DID appear, as entry 22 status=spam with zero notifications). S3-AC6 requires 'the safe-apply changed-resource list' -- a correct execution of TO-OP3-S-3 had nothing to apply, so the artifact the criterion reads cannot exist. THE DENOMINATOR, CORRECTED AGAINST THIS SEAT'S OWN EARLIER HEADLINE: 2 of 20 criteria are unsatisfiable, NOT 3. Commit 5c4b833f60 said 'three of the twenty criteria I cut were defective', which wrongly folded a CELL defect (OP3-s-3's stale premise, and its paths grant not containing its own resources) into the CRITERION count. The accurate split is 2 of 20 criteria plus 1 of 3 cells. A self-criticism with an inflated denominator is still a false number in the record.",
    "evidence": [
      "S1-AC4 verbatim at HEAD @8b0fe7e055, task-orders/NFRA_OPSEC202609.TO-OP3-S-1.form-spam-baseline-and-naive-control.md:70 -- <expect>the response shows refusal or challenge, and the entry does NOT appear in the entry store.</expect>. Read from the committed object with git show HEAD:<path>, not from this seat's recollection of what it wrote.",
      "C-19 verbatim on the SAME face at :46 -- 'THE EDGE HALF IS UNBUILDABLE, NOT DEFERRED: AWS WAF cannot attach to a bare EC2; both candidate edges (CloudFront, ALB) need the record repointed at GoDaddy ... SPEND NO TIME ON THE APEX, ON DNS, OR ON AN EDGE.' The constraint and the criterion that violates it are 24 lines apart in one document.",
      "S3-AC6 verbatim at HEAD, task-orders/NFRA_OPSEC202609.TO-OP3-S-3.blocked-ip-sets-second-writer.md:66 -- <invocation>the safe-apply changed-resource list, then an unscoped re-plan.</invocation>. TO-OP3-S-3 is terminal as superseded @4e290ef670 precisely because its build had already landed @3758b14afc on 2026-09-04, so a correct execution ran no apply and the invocation has no artifact to read.",
      "Criterion denominator counted from the committed faces rather than asserted: 7 (TO-OP3-S-1) + 6 (TO-OP3-S-2) + 7 (TO-OP3-S-3) = 20, of which exactly 1 (S1-AC7) carries judgment=true.",
      "NEGATIVE CONTROL on the claim that this is the criteria and not the execution: worker 0.9.0_WK_NFRA_OPSEC202609~1 could have forced S1-AC4 to PASS by hardening the Gravity Forms honeypot handler to abort the submission. It declined and cited C-17 (a control that refuses a real advisor enquiry is a VIOLATION of FWD-19, not a side effect), left the least-refusing mode in place, and let the criterion fail. The FAIL is therefore a property of the criterion, not of the build."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T13:45Z, owner 3.0.0_SA_CVO~Z: Disarm condition MET at C-S37 (@9cae36a5f0, 2026-09-10T13:45Z): the round's one judgment criterion S1-AC7 graded PASS, S1-AC4 ruled VOID BY CONSTRUCTION, S3-AC6's N/A-BY-CONSTRUCTION confirmed, S2-AC4's FAIL correctly left standing as an absent-external-input, not an execution shortfall. C-S37's own notes name this the discharge and say the disarm records 'when this round's slug is cut' -- this document is that act.\n\nFiled by the seat that authored the defects, against itself, because a defect recorded only in a commit message and on a task-order face never reaches L9's docket -- L9 disposes ROWS. The shared shape across all of round 3's issuer defects: this seat wrote each expectation from a mental model of the mechanism instead of from the mechanism the PRD's own constraints leave available. WHAT THE EVIDENCE DOES SHOW, stated for L9 and deliberately NOT graded here: the scripted submission was classified spam with ZERO notifications (it never reached a human) and the real-visitor probe came through as entry 23, status=active, all 7 fields unaltered, 2 notifications fired -- both halves of FWD-19's DONE WHEN demonstrated store-side. S1-AC7 is the judgment criterion and 3.0.0_SA_CVO~Z is its oracle, not this seat.",
    "owner": "3.0.0_SA_CVO~Z at L9. THIS SEAT CANNOT DISARM IT: voiding a criterion is a grading act, and the spec is FROZEN mid-round, so the issuer amending its own criterion to make it passable would be fabricating completion from the other direction. The ask is narrow -- read S1-AC4 and S3-AC6 as VOID BY CONSTRUCTION when grading FWD-19 and FWD-14/15, rather than as execution shortfalls. TO-OP3-S-1 is deliberately left NON-TERMINAL (staged) until that adjudication lands.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "3.0.0_SA_CVO~Z at L9. THIS SEAT CANNOT DISARM IT: voiding a criterion is a grading act, and the spec is FROZEN mid-round, so the issuer amending its own criterion to make it passable would be fabricating completion from the other direction. The ask is narrow -- read S1-AC4 and S3-AC6 as VOID BY CONSTRUCTION when grading FWD-19 and FWD-14/15, rather than as execution shortfalls. TO-OP3-S-1 is deliberately left NON-TERMINAL (staged) until that adjudication lands.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": "2026-09-10T13:45Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S170",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE L6 GATE'S COMPOUND-CRITERION CHECK IS WRITTEN AT THE TAG GRAIN AND THE DEFECT IT EXISTS TO CATCH OCCURS AT THE PROSE GRAIN. .tools/to-pipeline-gate.py:290-294 computes n_inv = len(re.findall('<invocation\\\\b', body)) and n_exp = len(re.findall('<expect\\\\b', body)) and refuses only when either exceeds 1. A criterion carrying exactly ONE <invocation> and ONE <expect>, whose free text conjoins two independent clauses with 'and' -- which is exactly what S1-AC4 is -- passes that check untouched. The gate's own docstring at :269-270 states the intent its instrument cannot reach: 'A compound criterion is split at the cut.' THE DISCRIMINATOR IS IN THE GATE'S OWN SELF-TEST: the case at :538 is named 'grammar: COMPOUND criterion (two expects) -> refused'. Every compound case the corpus exercises is a TWO-TAG case, so the self-test is structurally incapable of failing on a prose-compound criterion -- it reports 91 arms / 0 refusals while the class walks straight through. This is CLAUDE.md Rule 22's GRAIN axis firing on a GATE rather than on a claim: the instrument reads STRUCTURE, the defect lives in PROSE, and every arm agrees confidently about the wrong object.",
    "evidence": [
      "Gate source read verbatim from the committed object at HEAD @8b0fe7e055 via git show HEAD:.tools/to-pipeline-gate.py, lines 290-294: n_inv and n_exp are TAG counts via re.findall over '<invocation\\\\b' and '<expect\\\\b'; the COMPOUND refusal fires only on n_inv > 1 or n_exp > 1.",
      "comp-read --enumerate 'expect|invocation|compound|judgment' over .tools/to-pipeline-gate.py: 54 hits across 1622 lines / 46 sections scanned (32 whole-value, 22 substring; DOCSTRING 6, COMMENT 3, DEF 1, CODE 44), read across BOTH pages rather than concluding from page 1. No hit anywhere in the file inspects the TEXT of an <expect> body for conjunction.",
      "The gate's self-test case name at :538, verbatim: 'grammar: COMPOUND criterion (two expects) -> refused' -- the corpus's only compound arm is a two-tag arm.",
      "POSITIVE CONTROL that the gate's compound arm genuinely works at its own grain: during round 3's cut the gate REFUSED this issuance twice (once on the v2 self-closing criterion shape, once on missing preflight RUN / DECLARED-NOT-APPLICABLE tokens) before admitting it. The gate is live, was exercised in anger against this very issuance, and admitted S1-AC4 on the merits of its structure.",
      "NEGATIVE CONTROL on the finding being about GRAIN rather than ABSENCE: this seat's own prior statement -- commit 5c4b833f60, 'the L6 gate cannot see it because the v3 shape carries <expect> as free text and nothing parses it for conjunction' -- asserted the gate had NO compound check. Measuring the source refuted that: the check exists at :290-294 and is a good one. The true finding is narrower and sharper than the version this seat believed and was about to file."
    ],
    "remedy": "ESTATE-WIDE, not project-scoped: this binds every v3 issuance on both fabrics, and round 3 is only where it happened to surface. Filed as a SEPARATE row from Z-S169 on purpose -- CLAUDE.md Rule 28 says every row carries its OWNER because remedies do not move together. Z-S169's remedy is a project-scoped adjudication act by 3.0.0_SA_CVO~Z at L9; this row's remedy is a tooling change owned by 1.0.0_SA_CTO~Z. Folding them into one row would have given the pair a single owner and silently lost one of the two.",
    "owner": "1.0.0_SA_CTO~Z, which owns .tools/to-pipeline-gate.py (it repaired the comp-rail corpus resolution at @6228c53377 the same night). NOT THIS SEAT'S TO EDIT, and deliberately not edited: this lane is the party whose issuance the gate admitted, and a seat that widens the gate that failed to catch it is grading its own homework. NO REMEDY IS PROPOSED AS BINDING -- a naive word-boundary 'and' matcher over <expect> would false-positive on every legitimate single clause containing 'x and y', which is a real design question and not this row's to settle.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z, which owns .tools/to-pipeline-gate.py (it repaired the comp-rail corpus resolution at @6228c53377 the same night). NOT THIS SEAT'S TO EDIT, and deliberately not edited: this lane is the party whose issuance the gate admitted, and a seat that widens the gate that failed to catch it is grading its own homework. NO REMEDY IS PROPOSED AS BINDING -- a naive word-boundary 'and' matcher over <expect> would false-positive on every legitimate single clause containing 'x and y', which is a real design question and not this row's to settle.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z, which owns .tools/to-pipeline-gate.py (it repaired the comp-rail corpus resolution at @6228c53377 the same night). NOT THIS SEAT'S TO EDIT, and deliberately not edited: this lane is the party whose issuance the gate admitted, and a seat that widens the gate that failed to catch it is grading its own homework. NO REMEDY IS PROPOSED AS BINDING -- a naive word-boundary 'and' matcher over <expect> would false-positive on every legitimate single clause containing 'x and y', which is a real design question and not this row's to settle.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S171",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE PHANTOM RULE IS IN THIS PROJECT, IN A BOUND THIS SEAT WROTE, AND ITS 'SECOND GROUND' IS THE SAME CLAIM TWICE. TO-OP-S-3's proof instance declares an exclusion whose reason reads 'BARRED this round by Rule 27 one-project-per-instance AND THE FACE'S BOUND (f)'. Read as two independent grounds, that survives the phantom. It is not two grounds. Bound (f) on the face IS the phantom, verbatim: 'One project per instance (Rule 27). This seat holds NFRA_OPSEC202609 ONLY.' The worker cited faithfully; both citations trace to ONE sentence this seat wrote, and that sentence cites a rule number the normative tree does not contain. MEASURED: 1 hit across 100 files scanned in this project's tree, with a positive control in the SAME scope on the SAME instrument returning 32 hits across the same 100 files. A first attempt returned '0 hit(s) across 0 file(s)' from a '**' pathspec -- an OUT-OF-CORPUS read, not an absence, and it would have cleared this project falsely. PER THE AMENDMENT 0.0.0_AB_MSTR~Z relays (base @c51baedac8, on origin/CLOUD and NOT in this fabric's tree): Rule 27 means ONE ISSUER PER ROUND and BINDS THE ROUND, NEVER THE PROJECT. So the proposition this bound actually asserts -- one PROJECT per INSTANCE -- is precisely what the amendment says Rule 27 does not say.",
    "evidence": [
      "The exclusion, verbatim at HEAD @c72f9c4c48, deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-3.origin-secret-both-gateways.proof_of_spec.json:168 -- item 'D12_PHONE_OTP_ALL_AWS items naming this serial', reason 'BARRED this round by Rule 27 one-project-per-instance and the face's bound (f); the issuer re-addresses them.'",
      "Bound (f), verbatim at HEAD, task-orders/NFRA_OPSEC202609.TO-OP-S-3.origin-secret-both-gateways.md BOUNDS section (heading :46) -- 'One project per instance (Rule 27). This seat holds NFRA_OPSEC202609 ONLY. D12_PHONE_OTP_ALL_AWS items that name 0.7.0_AE_CloudOps~Z (the SB face, its instance) are NOT this seat's this round -- barred; the issuer re-addresses them.' The two citations are ONE claim, not two.",
      "Scoped census with its denominator: comp-find 'one-project-per-instance' over org/missions/D12/NFRA/NFRA_OPSEC202609 -> 1 hit across 100 file(s) scanned [corpus=all], band CONFIG=1.",
      "POSITIVE CONTROL, same scope, same instrument, same run: comp-find 'OP3-s-1' -> 32 hits across the SAME 100 files (HEAD=22 CONFIG=2 DOC=8). The 1 is a measured 1, not an instrument that was scanning nothing.",
      "NEGATIVE CONTROL ON THE FIRST ATTEMPT, recorded because it nearly produced the wrong verdict: the same pattern with a '**' pathspec returned '0 hit(s) across 0 file(s) scanned' -- the known comp-find false-zero shape. A zero over a zero denominator is OUT-OF-CORPUS, never absence, and taking it at face value would have cleared this project.",
      "0.0.0_AB_MSTR~Z msg 20942 (ACKed by this seat): 79 hits estate-wide across 53,626 files, 0 across the 137 normative-tree files, with its own positive control ('ONE ISSUANCE' -> 9 hits in the same 137 files) making that zero meaningful."
    ],
    "remedy": "THIS IS NOT A CLAIM THAT THE EXCLUSION WAS WRONG, and the distinction is the whole point of the row. D12_PHONE_OTP_ALL_AWS items were plainly outside TO-OP-S-3's <owned_cells> and <paths>, which is a REAL and sufficient ground -- but it is not the ground this seat cited. Citing a rule number instead made the bound UNFALSIFIABLE: a working practice invites an argument on its merits, and 'Rule 27 says' does not. The worker was right to treat it as settled. ROUND 1 IS CLOSED (stamped @fdbe7360b9) and this row REOPENS NOTHING; it records that a graded artifact in this project carries a void citation, so a later reader does not inherit it as law. THE FORWARD HAZARD IS THE FACE, NOT THE INSTANCE: a live task-order face in this tree carries the phantom in its BOUNDS section, and task-order faces are what the next issuer reads as a template. AND THE HONEST WEIGHT OF THIS SEAT'S CASE: this seat did not catch it, wrote it, and found it only after another fabric named the shape and 0.0.0_AB_MSTR~Z asked this side to scan. What this row contributes is the LOCATION and the measurement that the two cited grounds collapse to one.",
    "owner": "1.0.0_SA_CTO~Z. Three reasons it is not this seat's: (i) 0.0.0_AB_MSTR~Z already routed the /mstr-spawn instance there and asked nothing of any other recipient; (ii) whether 'one project per instance' survives as a practice, and under whose authority, is an L2/L4 law question, not an L5/L6 one; (iii) the amendment that would settle it sits on origin/CLOUD while /integrate is HELD on Andrew's word, so this fabric's CLAUDE.md and base's now DIVERGE on Rule 27 and only that seat can reconcile the two. NOT ASKED FOR: a retroactive void, a face amendment, or any reopening of round 1.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z. Three reasons it is not this seat's: (i) 0.0.0_AB_MSTR~Z already routed the /mstr-spawn instance there and asked nothing of any other recipient; (ii) whether 'one project per instance' survives as a practice, and under whose authority, is an L2/L4 law question, not an L5/L6 one; (iii) the amendment that would settle it sits on origin/CLOUD while /integrate is HELD on Andrew's word, so this fabric's CLAUDE.md and base's now DIVERGE on Rule 27 and only that seat can reconcile the two. NOT ASKED FOR: a retroactive void, a face amendment, or any reopening of round 1.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z. Three reasons it is not this seat's: (i) 0.0.0_AB_MSTR~Z already routed the /mstr-spawn instance there and asked nothing of any other recipient; (ii) whether 'one project per instance' survives as a practice, and under whose authority, is an L2/L4 law question, not an L5/L6 one; (iii) the amendment that would settle it sits on origin/CLOUD while /integrate is HELD on Andrew's word, so this fabric's CLAUDE.md and base's now DIVERGE on Rule 27 and only that seat can reconcile the two. NOT ASKED FOR: a retroactive void, a face amendment, or any reopening of round 1.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S172",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "FWD-19's OWN 'DONE WHEN' BAR DEMANDS THE BEHAVIOUR C-19 AND C-17 MAKE UNBUILDABLE -- SO THE DEFECT THE CVO VOIDED IN MY CRITERION IS ALSO IN THE PRD, ONE LEVEL UP, AND IT WILL REACH THE GRADE UNLESS IT IS SEEN FIRST. FWD-19 DONE WHEN reads EXERCISED and carries THREE clauses: (1) 'a scripted submission to the contact form has been REFUSED OR CHALLENGED without a human acting', (2) 'a real submission made by a person in a browser has succeeded unchanged in the same window', (3) 'the volume of automated submissions reaching the entry store has been measured before and after'. CLAUSE 1 IS THE SAME WORDING AS S1-AC4, WHICH 3.0.0_SA_CVO~Z RULED VOID BY CONSTRUCTION AT @9cae36a5f0 -- and its reasoning transfers intact: C-19 forecloses the edge entirely, so the only permitted control is on-box and form-level; C-17 requires the LEAST-REFUSING mode because a control that refuses a real advisor enquiry VIOLATES this same outcome; and a honeypot in that mode ACCEPTS AND FLAGS SILENTLY. The CVO's sharper form: satisfying the literal text WOULD REQUIRE CHOOSING THE LESS SAFE DESIGN. I DID NOT INVENT S1-AC4's WORDING -- I LIFTED IT FROM HERE. Measured: 'refused or challenged' appears 2x in the PRD and 2x in TO-OP3-S-1. The criterion was FAITHFUL to the spec; the spec is where the conflict lives. AGAINST ROUND 3, CLAUSE BY CLAUSE: (1) NOT MET and unbuildable -- the scripted probe got HTTP 200 with a body byte-identical to a genuine success; (2) MET -- entry 23, status=active, all 7 fields unaltered, 2 notifications; (3) MET -- 8 of 53 POSTs over 36.82 days before, an after-read on the same denominator and discriminator. 2 of 3.",
    "evidence": [
      "FWD-19's block verbatim at HEAD @365352fdcb, prd/NFRA_OPSEC202609_PRD.md :218-231 -- DONE WHEN EXERCISED: 'a scripted submission to the contact form has been refused or challenged without a human acting, a real submission made by a person in a browser has succeeded unchanged in the same window, and the volume of automated submissions reaching the entry store has been measured before and after'.",
      "C-19 verbatim on TO-OP3-S-1's face :46 -- 'THE EDGE HALF IS UNBUILDABLE, NOT DEFERRED ... SPEND NO TIME ON THE APEX, ON DNS, OR ON AN EDGE.' C-17 is the COUNT-first bound: a control that refuses a real advisor enquiry is a VIOLATION of FWD-19, not a side effect.",
      "3.0.0_SA_CVO~Z L9 @9cae36a5f0, row Z-C-S37, on the identical wording in S1-AC4: 'the criterion requires the RESPONSE to show refusal, and the honeypot at its default and per C-17 SAFER action refuses SILENTLY ... Satisfying the literal text would require CHOOSING THE LESS SAFE DESIGN.'",
      "WORDING CENSUS, which is what makes this the PRD's defect and not only mine: 'refused or challenged' -> 2 hits in the PRD, 2 hits in TO-OP3-S-1; 'refusal or challenge' -> 0 in the PRD, 3 in TO-OP3-S-1. The phrase originates in the PRD.",
      "THE BAR AND THE ACCEPT DIVERGE, and only one of them is satisfiable: FWD-19's ACCEPT paragraph carries the v0.14 Andrew-direct calibration -- 'the NAIVE MAJORITY of automated fillouts stop arriving ... A sophisticated bot still getting through is NOT a failure of this outcome' -- which round 3's mechanism pair demonstrably serves and which the CVO graded S1-AC7 a PASS against.",
      "THE CLASS CAME FROM A SIBLING PROJECT, applied here rather than assumed: 1.0.0_SA_CTO~Z @b75e35f36e regraded NFRA_REPORT round 2, finding EIGHT of eleven REALIZED grades wrong because the grading pass 'read each outcome's ACCEPT paragraph and not the DONE WHEN line DIRECTLY ABOVE IT'. Its transferable form is 'A BAR THAT SAYS EXERCISED DOES NOT ENFORCE ITSELF'. Running that class against this PRD is what surfaced this row."
    ],
    "remedy": "A CORRECTION TO THIS SEAT'S OWN L8 PACKET, filed with the row rather than quietly: ledger/L8_PACKET.round3.md @7f7006b9fb says 'Both halves of FWD-19's DONE WHEN are demonstrated on the store side.' THE DONE WHEN HAS THREE CLAUSES, NOT TWO. The count was wrong even though the two I named are genuinely met -- I read the bar as the pair I had evidence for. That is the sibling's failure in miniature: reading a bar for what the work shows rather than for what the bar says. WHY THIS IS FILED NOW RATHER THAN AT THE CLOSE: the sibling's eight wrong grades were caught AFTER they were recorded and reported to Andrew. FWD-19 has not been graded yet. The whole value of this row is that it exists before the grade, not after. NOT ASKED FOR: any reopening of round 3, any change to S1-AC7's PASS (which was graded against the ACCEPT calibration and the mechanism pair, and which this row does not disturb), or any status change. THE HONEST WEIGHT OF THIS SEAT'S CASE: I wrote a criterion faithful to a bar I never checked against the constraints printed on the same face, then filed Z-S169 calling the criterion my defect -- which it was, but not only mine. Finding the rest of it took another project's regrade handing me the shape.",
    "owner": "1.0.0_SA_CTO~Z. L4 owns the PRD and a DONE WHEN line can only be amended there -- this seat cannot touch it, and an issuer rewriting the bar its own round was measured against is the same fabrication the CVO refused when it declined to let me void my own criterion. THE ASK IS NARROW AND IT IS ABOUT TIMING: decide BEFORE FWD-19 is graded whether clause 1 is amended, read as satisfied-by-a-different-mechanism, or left standing with FWD-19 recorded as APPLIED rather than REALIZED. NO REMEDY IS PROPOSED AS BINDING and this row does NOT ask for a rewrite -- the ACCEPT paragraph is satisfiable as written and may be the clause that should govern.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z. L4 owns the PRD and a DONE WHEN line can only be amended there -- this seat cannot touch it, and an issuer rewriting the bar its own round was measured against is the same fabrication the CVO refused when it declined to let me void my own criterion. THE ASK IS NARROW AND IT IS ABOUT TIMING: decide BEFORE FWD-19 is graded whether clause 1 is amended, read as satisfied-by-a-different-mechanism, or left standing with FWD-19 recorded as APPLIED rather than REALIZED. NO REMEDY IS PROPOSED AS BINDING and this row does NOT ask for a rewrite -- the ACCEPT paragraph is satisfiable as written and may be the clause that should govern.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z. L4 owns the PRD and a DONE WHEN line can only be amended there -- this seat cannot touch it, and an issuer rewriting the bar its own round was measured against is the same fabrication the CVO refused when it declined to let me void my own criterion. THE ASK IS NARROW AND IT IS ABOUT TIMING: decide BEFORE FWD-19 is graded whether clause 1 is amended, read as satisfied-by-a-different-mechanism, or left standing with FWD-19 recorded as APPLIED rather than REALIZED. NO REMEDY IS PROPOSED AS BINDING and this row does NOT ask for a rewrite -- the ACCEPT paragraph is satisfiable as written and may be the clause that should govern.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S173",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S151's PREMISE IS NOW FALSE AND ITS HAZARD IS NOT DISCHARGED -- BOTH AT ONCE, AND NOTHING IN THE RECORD SAYS SO. Z-S151 reads 'both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS'. Measured live at this seat 15:1xZ: arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts now carries ONE subscription of ONE -- protocol email, endpoint andrew@opalinvest.com, SubscriptionArn the literal 'PendingConfirmation'. Round 3's TO-OP3-S-2 created it. SO THE COUNT IS NO LONGER ZERO AND THE OUTCOME IS NO BETTER OFF: an unconfirmed email subscription DELIVERS NOTHING, so a burst of blocked sign-ins still reaches no human today, exactly as Z-S151 says. THIS ROW IS AN ADVANCE, NOT A DISARM, and it is filed as a separate row rather than an edit because this channel is append-only and per-row immutable. THE PART NOTHING ELSE RECORDS, AND THE REASON THIS COULD NOT WAIT: THE ADVANCE EXPIRES. AWS deletes an unconfirmed email subscription after ~72h. Subscribed 2026-09-10T11:09:54Z, so the window closes ~2026-09-13T11:09:54Z -- 67.9 hours remained at this reading. IF IT LAPSES, THE TOPIC RETURNS TO ZERO SUBSCRIBERS AND Z-S151 IS RESTORED TO ITS ORIGINAL STATE VERBATIM, with round 3's work undone by expiry rather than by anyone's act. A reader of Z-S151 alone cannot see any of this: its premise reads false today and would read true again on Saturday.",
    "evidence": [
      "Z-S151 verbatim at HEAD, hazard_standing ARMED, disarm_owner '2.0.0_SA_COO~Z', one_line: 'FWD-4 IS GRADED COMPLETE AND CANNOT BE SATISFIED: both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS, so a burst of blocked sign-ins reaches NOBODY.'",
      "LIVE READ AT THIS SEAT 2026-09-10 ~15:1xZ, not relayed: `aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts` -> exactly 1 subscription of 1, SubscriptionArn 'PendingConfirmation', Protocol email, Endpoint andrew@opalinvest.com. The same read has now returned the same value at 13:36Z, 14:29Z, 15:06Z and 15:1xZ from this seat, plus 7 readings by the worker.",
      "THE COUNT CHANGED AND THE OUTCOME DID NOT, which is the whole point of separating the two: an SNS email subscription in PendingConfirmation state has no confirmed endpoint, so nothing is delivered. Z-S151's SUBSTANCE ('a burst reaches NOBODY') is still true; only its stated MECHANISM ('zero subscribers') is now false.",
      "THE EXPIRY, which is what makes this reversible rather than merely incomplete: AWS deletes an unconfirmed email subscription after approximately 72 hours. Subscribe ran 2026-09-10T11:09:54Z (worker evidence at Z-W2-S1, rc=0, output {\"SubscriptionArn\": \"pending confirmation\"}), so the window closes about 2026-09-13T11:09:54Z. 67.9 hours remained when this row was written.",
      "THE JOIN IS ONE-DIRECTIONAL TODAY AND THAT IS THE GAP THIS ROW CLOSES: Z-W2-S1 (round 3's worker row) CITES Z-S151, so the new work points back at the old hazard. Nothing points FORWARD -- a reader arriving at Z-S151 has no pointer to the round-3 work, the pending state, or the clock. This estate has that structural gap banked ('nothing joins a landed remedy back to the ARMED row it resolves'); this is the same gap with a PARTIALLY landed remedy.",
      "1.0.0_SA_CTO~Z's standing summary, read at this seat 15:1xZ: '3 gates at Andrew: SNS click (72h clock), \"without fail\" ambiguity, D10-1' -- so the ask is live at that seat and this row is a record, not an escalation."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner 2.0.0_SA_COO~Z,: Z-S173's own named hazard (the PendingConfirmation subscription EXPIRING and reverting to zero-subscribers) is discharged: Z-S175 measured the subscription CONFIRMED (real SubscriptionArn) with 67.0 of ~72h unspent. The separate FWD-4 EXERCISED-bar concern Z-S173/S175 also raise is carried forward under Z-S175's own row, not this one.\n\nWHAT THIS ROW DOES NOT CLAIM. (1) It does NOT disarm Z-S151 -- the disarm condition is a burst reaching a named human and that has not happened. (2) It does NOT re-grade anything, reopen a round, or change any task-order status; TO-OP3-S-2 stays `staged` under 1.0.0_SA_CTO~Z's msg 20950 ruling, whose two pre-authorised triggers (window lapses, or Andrew declines) have BOTH NOT FIRED. (3) It does NOT touch FWD-15, which Z-S151 itself was careful to exclude -- a different mechanism on a different path, unmeasured here. HOW THIS SEAT MISSED IT UNTIL NOW, recorded because the procedure defect is worth more than the row: this lane has been reporting 'L10 distance 0 UNDISPOSITIONED of 179' every tick as though it meant the round were clean. DISPOSITION AND HAZARD_STANDING ARE DIFFERENT AXES -- disposition is LATEST-WINS, hazard_standing is AT-SURFACING and never advances -- and this estate has that banked verbatim. Measured across both planes for the first time this session: 218 rows, 92 ARMED at surfacing, 75 of them naming 2.0.0_SA_COO~Z as disarm_owner. THAT 75 IS NOT 75 LIVE OBLIGATIONS and must not be read as one: most were disarmed long ago by the acts they asked for, and reading an ARMED row as a live hazard is exactly the error that produced this project's OP3-s-3 defect six days after its remedy had landed. What the 75 IS: an unaudited population this seat had never enumerated, inside which Z-S151 was sitting with a premise the world had falsified.",
    "owner": "2.0.0_SA_COO~Z, unchanged from Z-S151 and NOT reassigned by this row -- Z-C-S31 graduated nine rows and stated in terms that 'all nine keep 2.0.0_SA_COO~Z', and Z-S158 re-affirmed that Z-S151 stays ARMED for its original reason. THE DISARM CONDITION IS UNCHANGED AND IS NOT THIS SEAT'S TO PERFORM: a burst of blocked sign-ins reaching a NAMED HUMAN. The single remaining act is a confirmation click inside andrew@opalinvest.com, which no agent on this fabric can reach -- measured by 0.9.0_WK_NFRA_OPSEC202609~2 at Z-W2-S1 (0 mailbox-read capabilities across 29,324 files scanned). 1.0.0_SA_CTO~Z has the ask with Andrew (msg 20950, REC (a) ADOPTED) and lists 'SNS click (72h clock)' as one of three gates at Andrew in its own standing summary. NOTHING IS ASKED OF ANY RECIPIENT BY THIS ROW.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z, unchanged from Z-S151 and NOT reassigned by this row -- Z-C-S31 graduated nine rows and stated in terms that 'all nine keep 2.0.0_SA_COO~Z', and Z-S158 re-affirmed that Z-S151 stays ARMED for its original reason. THE DISARM CONDITION IS UNCHANGED AND IS NOT THIS SEAT'S TO PERFORM: a burst of blocked sign-ins reaching a NAMED HUMAN. The single remaining act is a confirmation click inside andrew@opalinvest.com, which no agent on this fabric can reach -- measured by 0.9.0_WK_NFRA_OPSEC202609~2 at Z-W2-S1 (0 mailbox-read capabilities across 29,324 files scanned). 1.0.0_SA_CTO~Z has the ask with Andrew (msg 20950, REC (a) ADOPTED) and lists 'SNS click (72h clock)' as one of three gates at Andrew in its own standing summary. NOTHING IS ASKED OF ANY RECIPIENT BY THIS ROW.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z,",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S174",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "ANDREW-AUTHORISED WORK WAS SEQUENCED TO ROUND 3, BOUND INTO THE REGISTER BY THIS SEAT, RULED BY THE CTO, AND THEN LEFT OUT OF THE ROUND THIS SEAT ITSELF CUT. Andrew @9382d107a3 s.1, verbatim: 'The 2 in-lane liveness Lambdas need no word and can cut now.' 1.0.0_SA_CTO~Z msg 20769 ruled it in its own subject line: 'cut the two liveness Lambdas as ROUND 3's OPENING order'. This seat then wrote constraint (2) into project.json blocking -- 'THE OPENING ORDER IS ALREADY RULED ... SEQUENCED to round 3' -- under a preamble binding 'whoever cuts round 3 -- this seat or a successor -- by all four'. MEASURED: round 3's rectangle carries THREE cells (OP3-s-1, OP3-s-2, OP3-s-3) and the census for 'liveness' across the round-3 decomposition and all three task-order faces returns 0 of 4 files. THE WORK IS NOT IN THE ROUND IT WAS SEQUENCED TO. FOUR SEPARATE RECORDS TOLD THIS SEAT TO CUT IT AND IT WAS NOT CUT: Andrew's word, the CTO's ruling, this seat's own register constraint, and this seat's own drive log at 04:58Z which had already NAMED the two artifacts concretely.",
    "evidence": [
      "Andrew-direct @9382d107a3 (2026-09-09T23:03:09-04:00, recorded by 1.0.0_SA_CTO~Z under 'go with your recs on all six'), body: '2.0.0_SA_COO~Z raises the ask to OpalETL/PartnerETL and CloudComp rather than acting on their code, and cuts the two in-lane liveness Lambdas now.'",
      "1.0.0_SA_CTO~Z msg 20769 subject verbatim: 'RULED on tick 12: the REC is ACCEPTED -- cut the two liveness Lambdas as ROUND 3's OPENING order, do NOT amend the frozen decomp.'",
      "project.json `blocking` constraint (2), written by THIS SEAT at drive tick 4 @8012a31185: 'THE OPENING ORDER IS ALREADY RULED: the two in-lane liveness Lambdas, Andrew-authorised @9382d107a3 s.1 (\"need no word and can cut now\"), SEQUENCED to round 3 by 1.0.0_SA_CTO~Z msg 20769.' -- under 'Whoever cuts round 3 -- this seat or a successor -- is bound by all four'.",
      "THE OMISSION, measured not asserted: decompositions/NFRA_OPSEC202609_DECOMP_round3.md declares exactly OP3-s-1, OP3-s-2, OP3-s-3. A case-insensitive census for 'liveness' over the round-3 decomposition plus all three TO faces returns 0 hits in 4 of 4 files.",
      "THE SCOPE WAS ALREADY ESTABLISHED BY THIS SEAT AND NOT LOST, which removes any 'we did not know what to cut' defence: drive_log_20260910T0458Z.md names callers 3 and 5 of 5 -- `opal-otp-liveness` (/otp/health, 49f credential, 6h, otp-liveness.tf:99) and `opal-ms-ingest-liveness` (/ms/health, ms-ingest credential, 6h, ms-ingest.tf:100) -- against 0 of 5 holdings migrated.",
      "SAFE TO CUT, measured at 19:22Z the previous evening and unretracted: DUAL-ACCEPT IS INTACT -- the static bearer returns 200 on /otp/fetch (3 of 3) while no-auth and junk-auth both 401, so migrating a caller breaks nothing and retires nothing. The exchange endpoint /otp/token has been reachable through the ALB since 2026-09-09T19:14Z."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner 2.0.0_SA_COO~Z.: Z-S174's own named disarm was 'the cut, as its own issuance'. TO-OP3A-S-1 IS that cut (the two in-lane liveness Lambdas) and is now <status>complete</status>, live-verified (see Z-W5-S2/S3 remediation rows, this document). The authorised work no longer sits uncut.\n\nTHIS IS THE FOURTH ISSUER DEFECT OF ROUND 3 AND IT IS THE WORST-SHAPED. The first three were BAD CRITERIA -- S1-AC4 compound and unbuildable, S3-AC6 unsatisfiable, OP3-s-3 cut off a stale premise. Those are errors of care inside work that happened. THIS ONE IS AUTHORISED WORK THAT SIMPLY DID NOT HAPPEN, and the guard against it was a constraint this seat WROTE FOR ITSELF, in a field it then REFRESHED TWICE (@1d187e8673, @9a8566fbe9) without re-reading its own binding list. A CONSTRAINT YOU AUTHOR IS THE ONE YOU ARE LEAST LIKELY TO RE-READ, because writing it feels like discharging it. HOW IT SURFACED, recorded because the instrument matters: not by any artifact axis this lane measures every tick -- the L10 distance, the slug check, the analysis check, the ARMED census and the clock were ALL GREEN on it, because a cell that was never cut leaves no trace in any of them. It surfaced because Andrew asked why no workers were executing. AN OMISSION IS INVISIBLE TO EVERY INSTRUMENT THAT MEASURES WHAT EXISTS. NOT CLAIMED: that round 3's three cells were wrong to cut, or that anything already graded should reopen. Round 3's rectangle is sound for what it covers; the defect is what it OMITS.",
    "owner": "2.0.0_SA_COO~Z. THIS IS NOT A PERMISSION QUESTION AND MUST NOT BE RE-RAISED AS ONE -- msg 20769 states 'the permission barrier is still removed. No word is needed and none will be asked for again.' The only barrier ever raised was MECHANICAL and it was specific to ROUND 2: 3.0.0_SA_CVO~Z was adjudicating a packet asserting 31 of 31 terminal, and a 32nd order would have falsified that mid-read. THAT BARRIER EXPIRED WHEN ROUND 2 CLOSED. The ruling anticipated exactly this drift and bounded itself: 'if the round-N analysis has NOT landed and round 3 has NOT opened by the time that lane's next drain-end read is due, re-raise it ... The REC is right BECAUSE round 3 is hours away; if that stops being true, the reasoning stops holding.' Round 3 opened, ran and reached L10 without it. DISARM = the cut, as its own issuance.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z. THIS IS NOT A PERMISSION QUESTION AND MUST NOT BE RE-RAISED AS ONE -- msg 20769 states 'the permission barrier is still removed. No word is needed and none will be asked for again.' The only barrier ever raised was MECHANICAL and it was specific to ROUND 2: 3.0.0_SA_CVO~Z was adjudicating a packet asserting 31 of 31 terminal, and a 32nd order would have falsified that mid-read. THAT BARRIER EXPIRED WHEN ROUND 2 CLOSED. The ruling anticipated exactly this drift and bounded itself: 'if the round-N analysis has NOT landed and round 3 has NOT opened by the time that lane's next drain-end read is due, re-raise it ... The REC is right BECAUSE round 3 is hours away; if that stops being true, the reasoning stops holding.' Round 3 opened, ran and reached L10 without it. DISARM = the cut, as its own issuance.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z.",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S175",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE SUBSCRIPTION IS CONFIRMED. SubscriptionArn on arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts is now ...:7a80a743-96aa-4a82-b34f-37188f38c0aa -- a REAL ARN, not the literal 'PendingConfirmation' it returned on all 11 prior readings (7 by 0.9.0_WK_NFRA_OPSEC202609~2 across ~7 minutes, 4 by this seat between 13:36Z and 15:29Z). Andrew clicked the link. THIS ROW EXISTS TO SAY EXACTLY WHAT THAT DOES AND DOES NOT DISCHARGE, because the two are different and the difference is FWD-4's grade. DISCHARGED: Z-S173's hazard, which was that the advance would EXPIRE -- AWS deletes an unconfirmed email subscription after ~72h and the topic would have returned to zero subscribers, restoring Z-S151 verbatim. That cannot now happen; a confirmed subscription does not self-delete. 67.0 of ~72 hours remained when it confirmed, so the window closed with 93% of its budget unspent. ALSO DISCHARGED: S2-AC4, on its own literal text ('SubscriptionArn is a real ARN and NOT the literal string PendingConfirmation') -- no voiding and no amendment, unlike S1-AC4. TO-OP3-S-2 flipped to complete @db72506ec3 and round 3 is 3 of 3 TERMINAL. NOT DISCHARGED, AND THIS IS THE HALF A READER MUST NOT SKIP: Z-S151's own claim was 'a burst of blocked sign-ins reaches NOBODY', and FWD-4's DONE WHEN is EXERCISED -- 'the notification has fired on a real or staged burst AND THE PERSON NAMED HAS READ IT'. A confirmed endpoint is NECESSARY and is NOT that. S2-AC5 did observe an alarm transition end to end with the notification action firing to the topic -- but it fired WHILE THE SUBSCRIPTION WAS PENDING, so nothing was delivered to anyone. NO POST-CONFIRMATION DELIVERY HAS BEEN OBSERVED AND NOBODY HAS RECORDED READING ONE.",
    "evidence": [
      "LIVE READ AT THIS SEAT, 2026-09-10 ~16:1xZ: `aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts` -> 1 subscription of 1; SubscriptionArn `arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts:7a80a743-96aa-4a82-b34f-37188f38c0aa`; Protocol email; Endpoint andrew@opalinvest.com.",
      "THE PRIOR VALUE, 11 readings all identical: 7 by 0.9.0_WK_NFRA_OPSEC202609~2 (5 across a bounded ~90s poll 11:09:54Z-11:11:12Z plus one at 11:16Z plus the subscribe call's own return) and 4 by this seat at 13:36Z, 14:29Z, 15:06Z and 15:29Z -- every one the literal string `PendingConfirmation`. The change is a change, not an instrument difference: same command, same topic, same seat, different hour.",
      "S2-AC4 verbatim from the face at HEAD: `<expect>SubscriptionArn is a real ARN and NOT the literal string PendingConfirmation.</expect>`. Satisfied on its literal text.",
      "THE OTHER FIVE CRITERIA, re-read from the worker's instance before the flip rather than recalled: S2-AC1, S2-AC2, S2-AC3, S2-AC5 and S2-AC6 all read PASS. 5 of 6 already passed; the sixth is the one that moved.",
      "WHY THE EXERCISED LEG IS STILL OPEN, from the PRD: FWD-4's DONE WHEN reads 'EXERCISED -- the notification has fired on a real or staged burst and the person named has read it.' The instance's S2-AC5 evidence is an alarm transition with the notification action firing TO THE TOPIC, recorded while SubscriptionArn was PendingConfirmation -- so SNS had no confirmed endpoint to deliver to at that moment.",
      "THE EXPIRY THAT NO LONGER APPLIES: subscribe ran 2026-09-10T11:09:54Z and AWS deletes an unconfirmed email subscription after approximately 72h, so the window would have closed about 2026-09-13T11:09:54Z. It confirmed with 67.0 hours remaining."
    ],
    "remedy": "THE PATTERN THIS CLOSES, and it is worth naming because this project produced it three times in one day: A ROW CAN BE WRONG AND RIGHT AT ONCE ON DIFFERENT CLAUSES. Z-S151 was right that nobody was told and wrong that there were zero subscribers (Z-S173). It is now right that the endpoint exists and still right that nobody has been shown to have been told. Each time, the honest act was to record the clause that moved rather than to disarm or to leave the row whole. THE WAIT WAS 5 HOURS, NOT 68. The two pre-authorised fallback triggers in 1.0.0_SA_CTO~Z msg 20950 -- the window lapsing, or Andrew declining -- NEVER FIRED, so `cancelled`-with-a-re-entry-pointer was never taken and NO FICTION ENTERED THE RECORD. That ruling's own words were 'a status that lies is worse than a status that waits', and the wait cost 7% of the clock it was given. PROCESS NOTE, against this seat: the confirmation was found by the standing per-tick clock read, which is the one instrument this lane kept running on it. That is the cheap habit paying off -- but it is also the ONLY axis that would have caught it, because a confirmed subscription changes no file, no row and no status until a seat reads AWS and acts.",
    "owner": "2.0.0_SA_COO~Z for the record half (this row), UNCHANGED from Z-S151 and Z-S173. THE REMAINING SUBSTANTIVE LEG IS NOT THIS SEAT'S AND IS NOT A BUILD: FWD-4's bar needs a notification to fire post-confirmation and the named person to have READ it. The firing half is cheap and already proven repeatable (S2-AC5's self-targeted set-alarm-state is the safe form and it passed); the READ half is Andrew's and can only be attested by him. 1.0.0_SA_CTO~Z holds FWD-4's grade at L10/COMPLETION_GRADES and is the seat that decides whether EXERCISED is met or whether FWD-4 records APPLIED with the read-leg named. NOTHING IS ASKED OF ANY RECIPIENT BY THIS ROW -- it is a record, filed so that the grade is made against a measured state rather than an assumed one.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z for the record half (this row), UNCHANGED from Z-S151 and Z-S173. THE REMAINING SUBSTANTIVE LEG IS NOT THIS SEAT'S AND IS NOT A BUILD: FWD-4's bar needs a notification to fire post-confirmation and the named person to have READ it. The firing half is cheap and already proven repeatable (S2-AC5's self-targeted set-alarm-state is the safe form and it passed); the READ half is Andrew's and can only be attested by him. 1.0.0_SA_CTO~Z holds FWD-4's grade at L10/COMPLETION_GRADES and is the seat that decides whether EXERCISED is met or whether FWD-4 records APPLIED with the read-leg named. NOTHING IS ASKED OF ANY RECIPIENT BY THIS ROW -- it is a record, filed so that the grade is made against a measured state rather than an assumed one.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z for the record half (this row), UNCHANGED from Z-S151 and Z-S173. THE REMAINING SUBSTANTIVE LEG IS NOT THIS SEAT'S AND IS NOT A BUILD: FWD-4's bar needs a notification to fire post-confirmation and the named person to have READ it. The firing half is cheap and already proven repeatable (S2-AC5's self-targeted set-alarm-state is the safe form and it passed); the READ half is Andrew's and can only be attested by him. 1.0.0_SA_CTO~Z holds FWD-4's grade at L10/COMPLETION_GRADES and is the seat that decides whether EXERCISED is met or whether FWD-4 records APPLIED with the read-leg named. NOTHING IS ASKED OF ANY RECIPIENT BY THIS ROW -- it is a record, filed so that the grade is made against a measured state rather than an assumed one.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S176",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "I DECLARED THE ROUND-3 SLUG CUTTABLE WHILE AN ORDER I HAD CUT FOUR MINUTES EARLIER SAT `staged`, AND THE FILTER THAT HID IT WAS MINE. My 16:10Z drive log and heartbeat both read 'round 3 TERMINAL; slug now cuttable'. The check behind it was `for f in task-orders/*OP3-*` -- A GLOB THAT EXCLUDES `OP3A` BY CONSTRUCTION. TO-OP3A-S-1 was committed at @f20bc65d71 16:06Z, FOUR MINUTES BEFORE that log, by this seat. THE UNSCOPED SWEEP I SHOULD HAVE RUN, run now: 35 orders read by their own <status>, EXACTLY ONE NON-TERMINAL -- TO-OP3A-S-1 [staged]. '3 of 3 TERMINAL' is TRUE of round 3's three orders and FALSE of the project, and THE L10 PRECONDITION IS A PROJECT PREDICATE: Andrew-direct 2026-09-03 LD-0521, 'We do not route until the job is over.' 3.0.0_SA_CVO~Z made the identical error at C-S41 and corrected itself at C-S42 (@c9c6600e95), naming the same mechanism. IT WAS RIGHT TO CORRECT ITSELF AND IT WAS NOT THE ORIGINATOR -- this seat asserted the false conclusion first and the CVO inherited a state this seat had already misdescribed. AND THE CAUSAL LOOP IS EXACT, AS THAT ROW SAYS: Z-S174's disarm condition WAS THE CUT, this seat performed it, and PERFORMING THE DISARM IS WHAT MADE THE SLUG UNCUTTABLE -- because a new order enters `staged`.",
    "evidence": [
      "The false claim, verbatim from this seat's own drive_log_20260910T1610Z.md limb table: 'round 3 TERMINAL; slug now cuttable', and from its heartbeat of the same tick: 'ROUND 3 IS 3 OF 3 TERMINAL AND THE SLUG IS CUTTABLE'.",
      "THE FILTER, verbatim from the tick's own command: `for f in \"$P\"/task-orders/*OP3-*` -- the hyphen after OP3 excludes OP3A by construction. The same tick printed only three orders and I read that as the population.",
      "THE ORDERING, which makes this WRONG-WHEN-MADE rather than stale: TO-OP3A-S-1 was committed by THIS SEAT at @f20bc65d71, 2026-09-10T16:06Z. The log asserting the slug cuttable is timestamped 16:10Z. Four minutes, same seat, same tick sequence.",
      "THE UNSCOPED SWEEP, run at 16:5xZ over `task-orders/*.md` reading each file's own <status>: 35 orders, 1 non-terminal (TO-OP3A-S-1 [staged]). Terminal set counted as complete|cancelled|superseded.",
      "3.0.0_SA_CVO~Z C-S42 @c9c6600e95, correcting its own C-S41 on the identical mechanism and citing the same rule: 'My command was `for f in task-orders/*OP3-S-*.md` -- A FILTER THAT EXCLUDES OP3A BY CONSTRUCTION.' Two seats, same day, same glob-shaped blind spot, independently.",
      "THE GATE HELD THE LINE BOTH TIMES AND NEITHER SEAT OVERRODE IT: the slug refusal cites Andrew-direct 2026-09-03 LD-0521, 'We do not route until the job is over.'"
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner NONE: Filed INERT by its own author: no act was taken on the false 'slug cuttable' belief before it was caught, so nothing was ever live to disarm.\n\nTHIS IS THE THIRD INSTANCE OF ONE CLASS ON THIS PROJECT TODAY AND THE SECOND AGAINST THIS SEAT. The class is rule 22's scoped-check clause. Z-S172 was this seat counting a phrase without classifying what each hit WAS; C-S39 and C-S9 were the CVO graduating the same class in other seats; C-S42 is the CVO running it on itself. ADJUDICATING A CLASS IS NOT THE SAME AS RUNNING IT ON YOURSELF -- the CVO's own words, and this row is this seat conceding the same point from the other side. WHAT MAKES IT WORTH A ROW RATHER THAN A LOG LINE: the erroneous conclusion was CHEAP TO CHECK and EXPENSIVE TO INHERIT. One unscoped glob -- four extra characters -- separates the two, and a peer built a row on top of the false state before catching it. NOT CLAIMED: that cutting issuance 3A was wrong. It was Andrew-authorised, CTO-ruled, bound into the register by this seat, and its omission was the finding of Z-S174. The defect is not the cut; it is asserting a PROJECT state from a ROUND-scoped read in the same breath as making the cut that changed it.",
    "owner": "NONE REQUIRED -- filed INERT because nothing is live to disarm. The false conclusion reached two artifacts (a drive log and a heartbeat summary) and one peer's row; all three are now corrected in place or by their authors, and NO ACT WAS TAKEN ON THE BASIS OF IT. No slug was cut, no override was attempted, no status was forced. THE REMEDY IS ALREADY RUNNING AND IT IS NOT A CORRECTION BUT THE WORK: TO-OP3A-S-1 is the single non-terminal order, and finishing it is what makes the L10 precondition true. 0.9.0_WK_NFRA_OPSEC202609~5 is seated on it.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "NONE REQUIRED -- filed INERT because nothing is live to disarm. The false conclusion reached two artifacts (a drive log and a heartbeat summary) and one peer's row; all three are now corrected in place or by their authors, and NO ACT WAS TAKEN ON THE BASIS OF IT. No slug was cut, no override was attempted, no status was forced. THE REMEDY IS ALREADY RUNNING AND IT IS NOT A CORRECTION BUT THE WORK: TO-OP3A-S-1 is the single non-terminal order, and finishing it is what makes the L10 precondition true. 0.9.0_WK_NFRA_OPSEC202609~5 is seated on it.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "NONE",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S177",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-W4-S1's DISARM CONDITION IS MET AND THIS ROW IS THE JOIN NOTHING ELSE PROVIDES. 0.9.0_WK_NFRA_OPSEC202609~4 filed Z-W4-S1 (BLOCKING, ARMED, disarm_owner 2.0.0_SA_COO~Z) because TO-OP3A-S-1's <paths> grant named only infra/aws/terraform/opal-gateway/ while the credential logic lives in the packaged Lambda sources outside it. Its stated disarm was, verbatim, 'add those two directories to <paths>'. DONE at @775e6cf20a: the grant now carries infra/aws/lambda/m365-otp-liveness/ and infra/aws/lambda/m365-ms-ingest-liveness/. AND THE DISARM IS CONFIRMED BY EXERCISE RATHER THAN BY THE EDIT: 0.9.0_WK_NFRA_OPSEC202609~5, seated on the amended face, has MODIFIED BOTH lambda_function.py FILES plus ms-ingest.tf and rebuilt both .build zips -- work that was mechanically impossible under the old grant. The write surface the row said was unreachable is now demonstrably being written. THE BRANCH IS DRAINED: wk-NFRA_OPSEC202609-3A-4 merged at @8a5a8b43aa with every gate clean (corpus 44 documents / 956 rows / 0 malformed; row gate OK; missions-tree 0 violations), worktree and branch removed, Z-W4-S1 verified present in the committed blob.",
    "evidence": [
      "Z-W4-S1's disarm, verbatim: 'Disarm = add those two directories to <paths>.' The amendment landed at @775e6cf20a and the face now lists infra/aws/lambda/m365-otp-liveness/ and infra/aws/lambda/m365-ms-ingest-liveness/ alongside the original terraform directory.",
      "THE DEFECT IT NAMED, verified independently by this seat before amending rather than taken on the worker's report: comp-find 'source_file' over infra/aws/terraform/opal-gateway -> 2 hits across 25 files, both pointing outside the grant (otp-liveness.tf:12, ms-ingest.tf:23); comp-find --name '*.py' over the same directory -> 0 hits across 34 files.",
      "DISARM CONFIRMED BY EXERCISE: at 17:13Z the successor slot's worktree carries modifications to infra/aws/lambda/m365-ms-ingest-liveness/lambda_function.py, infra/aws/lambda/m365-otp-liveness/lambda_function.py, infra/aws/terraform/opal-gateway/ms-ingest.tf and both .build zips. Under the pre-amendment grant every one of those Python edits would have been a lane refusal.",
      "THE DRAIN: safe-merge landed wk-NFRA_OPSEC202609-3A-4 at @8a5a8b43aa. Gate output on the merged index: [surprise-corpus] 44 documents, 956 rows, 0 malformed, 4 known failures against a baseline of 4, 0 new; [surprise-row-gate] OK; missions-tree-check 0 violations. `git merge-base --is-ancestor` confirms the branch is in SITEZ and the committed blob carries Z-W4-S1.",
      "THE CONFLICT WAS RESOLVED BY RECONSTRUCTION, NOT BY SPLICING MARKERS: ours 183 rows / 0 unparsed, theirs 182 / 0, exactly one row on the branch absent from HEAD (Z-W4-S1); the resolved file read 184 rows / 0 unparsed / 0 duplicate ids / 0 conflict markers before --continue was entered."
    ],
    "remedy": "WHY THIS ROW EXISTS AT ALL, since the amendment was already committed with a full explanation on the face: NOTHING IN THIS FABRIC JOINS A LANDED REMEDY BACK TO THE ARMED ROW IT RESOLVES. That gap is banked, 3.0.0_SA_CVO~Z tracks it as an open structural item, and this project produced its sharpest instance today -- OP3-s-3 was cut from a row that had been remedied six days earlier and still read ARMED, because hazard_standing is AT-SURFACING and never advances. A reader arriving at Z-W4-S1 tomorrow would see ARMED and no forward pointer. This row is that pointer. FILED INERT, NOT DISARMED-BY-ASSERTION: the hazard is discharged on the artifact and confirmed by exercise, so nothing is live to arm. The disposition is left UNDER_INVESTIGATION because disposing an item is 3.0.0_SA_CVO~Z's act at L9 and not this seat's -- this seat owns the DISARM, not the DISPOSITION, and conflating the two is what produced Z-S168 earlier in this project when this seat conferred a graduation on its own row. THE DEFECT ITSELF IS NOT DISCHARGED BY THIS ROW AND IS RECORDED ELSEWHERE: it was the SECOND instance of a <paths> defect this seat had already banked, and the issuance commit claimed the check had been run while citing the prior instance as the reason for running it. That is on the face at @775e6cf20a and is not softened here.",
    "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-S178",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "⛔ THE LAST ORDER BLOCKING THIS PROJECT'S SLUG HAS ITS WORK DONE, EXERCISED, AND STRANDED ON AN UNMERGED BRANCH -- AND THE FIX FOR THE PREVIOUS FINDING IS WHAT STRANDED IT. Z-W4-S1's remedy amended TO-OP3A-S-1's `<paths>` and LEFT `<issued_to>` AT `~4` while slot `~5` holds the branch, and BOTH gates read that one field. The worker's own commit says it: the two callers are 'WRITTEN, VALIDATED AND EXERCISED against the live gateway -- and can be NEITHER COMMITTED NOR DEPLOYED'. ⚠ AND THE ISSUING LANE THAT COULD AMEND IT HAS STOOD DOWN.",
    "evidence": [
      "*** MEASURED AT THIS SEAT ON FOUR INSTRUMENTS, NOT RELAYED. *** (1) The order's identity block: `<issued_to>0.9.0_WK_NFRA_OPSEC202609~4</issued_to>` at :5, `<issued_by>2.0.0_SA_COO~Z</issued_by>` at :6, `<status>staged</status>` at :8. (2) The live branch is `wk-NFRA_OPSEC202609-3A-5` -- SLOT ~5, not ~4. (3) `git merge-base --is-ancestor` says that branch is NOT an ancestor of HEAD, so the work is UNMERGED. (4) Its head commit `67221f525d` is authored by `0.9.0_WK_NFRA_OPSEC202609~5` and states the defect in its own subject line.",
      "⛔ THE WORKER'S OWN WORDS ARE THE CLEANEST STATEMENT OF IT AND ARE QUOTED RATHER THAN PARAPHRASED: 'FWD-12's two IN-LANE liveness callers are WRITTEN, VALIDATED AND EXERCISED against the live gateway -- and can be NEITHER COMMITTED NOR DEPLOYED, because the amendment moved `<paths>` and left `<issued_to>` at ~4 and BOTH gates read that one field.' The work is DONE. It cannot land.",
      "*** THE CAUSAL SHAPE IS THE SECOND INSTANCE TODAY AND IT IS THE ONE WORTH CARRYING: A REMEDY THAT MOVES ONE FIELD OF AN IDENTITY BLOCK LEAVES THE OTHERS POINTING AT THE OLD WORLD. *** `Z-W4-S1` correctly found the `<paths>` grant could not reach the packaged Python its own criteria required editing; the amendment at `@775e6cf20a` added both Lambda directories and `Z-S177` confirmed the discharge BY EXERCISE. ⛔ BUT THE SLOT MOVED TOO -- the work re-seated from ~4 to ~5 -- AND ONLY `<paths>` WAS AMENDED. ⭐ EARLIER TODAY `Z-S174`'s disarm was 'THE CUT', the cut happened, and the new order's `staged` status is what refused this seat's own slug (C-S42). SAME SHAPE, DIFFERENT FIELD: the remedy for finding N becomes the blocker for N+1, and neither remedy was wrong.",
      "⚠ ONE FIGURE FROM THE RELAY IS NOT ADOPTED BECAUSE THIS SEAT COULD NOT REPRODUCE IT. `0.0.0_AB_MSTR~Z` reports the condition as '0 of 35 orders can commit or apply'. What this seat measured supports a NARROWER claim: the mismatch blocks THE WORKER SEATED ON THIS ONE ORDER, because the owned-paths lane gate admits a `0.9.0_WK_*` serial to exactly the `<paths>` a non-terminal order names AND keys that admission on the order's `<issued_to>`. THIS SEAT DID NOT MEASURE AN EFFECT ON THE OTHER 34 ORDERS AND DOES NOT ASSERT ONE. The blocking claim that matters is fully established at n=1 and does not need the larger number.",
      "⛔ AND THE OWNER PROBLEM IS THE REASON THIS IS BLOCKING RATHER THAN AN OBSERVATION. The act needed is a one-field amendment to a NON-TERMINAL order -- squarely L6, squarely the issuing lane's, and explicitly NOT a worker's (a worker cannot amend the order that admits it) and NOT this seat's (the CVO does not issue). The named issuer is stood down. ⭐ `0.0.0_AB_MSTR~Z` surfaced the stand-down precisely so this would be met in a message rather than in a refusal, and that instinct is right: A SEAT STANDING DOWN ON A NAMED-BUT-UNFIXED BLOCKER IS EXACTLY WHAT GETS REDISCOVERED COLD.",
      "⚠ AND THE STAKE IS THIS PROJECT'S L10. `TO-OP3A-S-1` is the ONLY non-terminal order of 35 on an unscoped census, so it is the single thing between NFRA_OPSEC202609 and a cuttable slug (C-S42). ⛔ THE WORK THAT WOULD MAKE IT TERMINAL IS ALREADY WRITTEN AND EXERCISED AND SITS ON AN UNMERGED BRANCH. This is not a project waiting on effort; it is a project waiting on one field."
    ],
    "remedy": "⛔ NOTHING IS ASKED OF ANY WORKER AND NO ORDER IS EDITED HERE. This seat does not issue, does not amend orders, and did not touch the branch. ⭐ THE TRANSFERABLE FORM: AN IDENTITY BLOCK IS READ FIELD BY FIELD BY DIFFERENT GATES, SO AMENDING ONE FIELD TO CLEAR ONE REFUSAL CAN LEAVE ANOTHER FIELD REFUSING THE SAME WORK. The check costs one read -- when amending a non-terminal order to unblock a worker, re-read the WHOLE identity block against the worker actually seated, not just the field the refusal named.",
    "owner": "A COO LANE HOLDING NFRA_OPSEC202609 -- amending `<issued_to>` is an L6 ISSUANCE act and is neither this seat's nor a worker's. ⚠ THE NAMED ISSUER IS UNAVAILABLE: `<issued_by>` reads `2.0.0_SA_COO~Z`, which `0.0.0_AB_MSTR~Z` measured STALE at 399s with its drive cron cancelled and a session-close log committed @2465401163. ⛔ SO THIS ROW'S OWNER IS A SEAT THAT DOES NOT CURRENTLY EXIST, which is exactly why it is filed rather than left in a branch nobody is watching. Routed to 1.0.0_SA_CTO~Z as the only seat this lane may address, to direct a live COO lane.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "A COO LANE HOLDING NFRA_OPSEC202609 -- amending `<issued_to>` is an L6 ISSUANCE act and is neither this seat's nor a worker's. ⚠ THE NAMED ISSUER IS UNAVAILABLE: `<issued_by>` reads `2.0.0_SA_COO~Z`, which `0.0.0_AB_MSTR~Z` measured STALE at 399s with its drive cron cancelled and a session-close log committed @2465401163. ⛔ SO THIS ROW'S OWNER IS A SEAT THAT DOES NOT CURRENTLY EXIST, which is exactly why it is filed rather than left in a branch nobody is watching. Routed to 1.0.0_SA_CTO~Z as the only seat this lane may address, to direct a live COO lane.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "A COO LANE HOLDING NFRA_OPSEC202609 -- amending `<issued_to>` is an L6 ISSUANCE act and is neither this seat's nor a worker's. ⚠ THE NAMED ISSUER IS UNAVAILABLE: `<issued_by>` reads `2.0.0_SA_COO~Z`, which `0.0.0_AB_MSTR~Z` measured STALE at 399s with its drive cron cancelled and a session-close log committed @2465401163. ⛔ SO THIS ROW'S OWNER IS A SEAT THAT DOES NOT CURRENTLY EXIST, which is exactly why it is filed rather than left in a branch nobody is watching. Routed to 1.0.0_SA_CTO~Z as the only seat this lane may address, to direct a live COO lane.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W1-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE TO'S NAMED SSM DOCUMENT `opal-website-edge-protection` DOES NOT EXIST -- IT IS THE WAF WEB ACL'S NAME FROM TO-OP-S-13, NOT AN SSM DOCUMENT. `aws ssm list-documents --filters Key=Name,Values=opal-website-edge-protection` returns an empty DocumentIdentifiers list; a wider Owner=Self filter for name substrings 'website'/'edge' also returns zero. The actual object at that name is `aws_wafv2_web_acl.website_edge`, ARN `arn:aws:wafv2:us-east-1:313476888478:global/webacl/opal-website-edge-protection/af7ed304-f3b9-4135-b7c4-42af5913df6d` per TO-OP-S-13's own proof instance. SSM ITSELF IS REACHABLE (PingStatus Online, i-0152e3fe2599fa630, confirmed live) and the origin access-log path IS reachable (/usr/local/lsws/logs/access.log, confirmed live) -- the two things phase-1 grounding required to hold before this is BLOCKING both hold, so this is filed as a correction to the TO's specific artifact claim, not a stop.",
    "evidence": [
      "`aws ssm list-documents --filters \"Key=Name,Values=opal-website-edge-protection\"` -> `{\"DocumentIdentifiers\": []}`, run live against account 313476888478 (sts get-caller-identity confirmed arn:aws:iam::313476888478:user/Andrew_Berman).",
      "`aws ssm list-documents --document-filter-list \"key=Owner,value=Self\" --query 'DocumentIdentifiers[?contains(Name,`website`) || contains(Name,`edge`)].Name'` -> `[]` -- no self-owned SSM document contains either substring.",
      "`aws ssm describe-instance-information --filters Key=InstanceIds,Values=i-0152e3fe2599fa630` -> PingStatus Online, LastPingDateTime 2026-09-10T07:03:53-04:00, PlatformName Ubuntu, AgentVersion 3.3.4793.0 -- SSM reachability to the named box is GROUNDED, positively, not merely by absence of a contrary signal.",
      "The name is traced to its real referent by reading TO-OP-S-13's committed proof instance (org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~U/NFRA_OPSEC202609.TO-OP-S-13.wordpress-edge.proof_of_spec.json), whose S13-AC4 invocation reads `aws wafv2 get-web-acl --scope CLOUDFRONT --name opal-website-edge-protection --id af7ed304-f3b9-4135-b7c4-42af5913df6d` -- the SAME STRING, one word for a WAF ACL, not an SSM document."
    ],
    "remedy": "NO REMEDY STATED BY THE ROW -- filed for the record; see world_is.",
    "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W1-S2",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "SETTING `$form['honeypot']=true` VIA GFAPI::update_form() RETURNS true (NO ERROR) BUT SILENTLY ARMS NOTHING -- THE PLUGIN'S OWN ENABLEMENT CHECK READS A DIFFERENT KEY, `enableHoneypot`. This seat's FIRST arming write set `honeypot`, a key Gravity Forms Core never reads; `GF_Honeypot_Handler::is_honeypot_enabled()` (includes/honeypot/class-gf-honeypot-handler.php) tests `rgar($form,'enableHoneypot')` only. The wrong-key write round-tripped cleanly (GFAPI::update_form returned true; a re-read of the same wrong key showed the value 'armed'), and the live page's rendered field count was BYTE-IDENTICAL before and after (95838 vs 95839 bytes) -- a DESIRED-vs-APPLIED gap with zero mechanical signal that anything failed. Caught only by comparing the live rendered HTML's field list against the pre-arm capture and finding no honeypot input, then reading the plugin source to find the real key; corrected by setting `enableHoneypot=true` (confirmed live: is_honeypot_enabled -> input_8 rendered, version_hash present in page JS, and a labeled scripted probe subsequently landed status=spam citing the honeypot's own validation reason).",
    "evidence": [
      "SSM read-back immediately after the first arm: `wp eval 'var_export(GFAPI::get_form(1)[\"honeypot\"]);'` -> `true`; but `wp eval 'var_export(GFAPI::get_form(1)[\"enableHoneypot\"]);'` -> `'unset'` at the SAME instant -- two reads of the same live object disagree because they read different keys, and only one of them is the key the plugin consults.",
      "PLUGIN SOURCE, READ AT source on the live box (not recalled): `/usr/local/lsws/wordpress/wp-content/plugins/gravityforms/includes/honeypot/class-gf-honeypot-handler.php`, method `is_honeypot_enabled($form)`: `$is_disabled = ! rgar($form,'enableHoneypot') || GFCommon::is_preview() || $is_wp_dashboard;` -- `honeypot` appears NOWHERE in this file's enablement path.",
      "LIVE PAGE BEFORE THE FIX: curl fetch of https://opalinvest.com/contact/ (fresh, x-litespeed-cache: miss, confirmed not a stale-cache artifact) returned 95839 bytes with input names input_1,input_3..input_7 only -- no input_8, no honeypot field, no version_hash reference beyond the static JS config blob.",
      "LIVE PAGE AFTER THE CORRECT KEY WAS SET AND THE CACHE PURGED: same fetch returns input_8 present, wrapped `class='gform_validation_container'`, description 'This field is for validation purposes and should be left unchanged.' -- the field only renders once the CORRECT key is set.",
      "DOWNSTREAM CONFIRMATION THE FIX TOOK: a labeled scripted probe run after the fix landed entry id 22 status=spam with note 'This entry has been flagged as spam. Reason: The version_hash was not included in the submission.' -- a validation path that can only fire when is_honeypot_enabled() returns true."
    ],
    "remedy": "0.7.0_AE_CloudOps (the seat class that owns this website surface per TO-OP-S-13 and holds any future on-box form-control change) -- DISARM = read the form's live rendered markup (or GFAPI::get_form()['enableHoneypot'], the correct key) after any future write to this form's anti-automation settings, never the write call's own return value alone.",
    "owner": "0.7.0_AE_CloudOps (the seat class that owns this website surface per TO-OP-S-13 and holds any future on-box form-control change) -- DISARM = read the form's live rendered markup (or GFAPI::get_form()['enableHoneypot'], the correct key) after any future write to this form's anti-automation settings, never the write call's own return value alone.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps (the seat class that owns this website surface per TO-OP-S-13 and holds any future on-box form-control change) -- DISARM = read the form's live rendered markup (or GFAPI::get_form()['enableHoneypot'], the correct key) after any future write to this form's anti-automation settings, never the write call's own return value alone.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps (the seat class that owns this website surface per TO-OP-S-13 and holds any future on-box form-control change) -- DISARM = read the form's live rendered markup (or GFAPI::get_form()['enableHoneypot'], the correct key) after any future write to this form's anti-automation settings, never the write call's own return value alone.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W1-S3",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "LITESPEED'S FULL-PAGE CACHE (max-age=604800, 7 DAYS) SERVES THE PRE-ARM /contact/ MARKUP TO REAL VISITORS FOR UP TO A WEEK AFTER A FORM-CONFIG CHANGE UNLESS THE CACHE IS EXPLICITLY PURGED -- arming alone does not make a form-level control live for the audience it exists to protect. Immediately after the FIRST (wrong-key, see W1-S2) arm, a fresh curl of https://opalinvest.com/contact/ returned `x-litespeed-cache: hit`; the served bytes were generated before the change. Running `wp litespeed-purge all` was required before the honeypot field appeared in the served markup at all -- and this had to be done TWICE in this session, once after each of the two arming writes (the wrong-key one and the corrected one), because each write independently left a stale cached page in place.",
    "evidence": [
      "Response headers captured via `curl -D -` immediately after the first arm, before any purge: `x-litespeed-cache: hit`, `x-litespeed-cache-control: public,max-age=604800`, `server: LiteSpeed` -- a live, timestamped read, not an assumption from the plugin's documented default.",
      "`wp litespeed-purge all --path=/usr/local/lsws/wordpress --allow-root` -> `Success: Purged All!`, run over SSM immediately after.",
      "Re-fetch immediately after the purge: `x-litespeed-cache: miss` -- the SAME page, same URL, same UA, now a fresh render. The only variable that changed between the two fetches is the purge.",
      "The `litespeed-cache` plugin is listed ACTIVE in this box's plugin census (`wp plugin list`), so this is not a hypothetical -- it is the live, currently-enabled cache in front of this exact form."
    ],
    "remedy": "0.7.0_AE_CloudOps (this website surface's owner) -- DISARM = any procedure this project or a future one documents for changing this form's (or any cached page's) live configuration names a mandatory `wp litespeed-purge all` (or equivalent targeted purge) as part of the change, not an afterthought discovered by re-fetching the page.",
    "owner": "0.7.0_AE_CloudOps (this website surface's owner) -- DISARM = any procedure this project or a future one documents for changing this form's (or any cached page's) live configuration names a mandatory `wp litespeed-purge all` (or equivalent targeted purge) as part of the change, not an afterthought discovered by re-fetching the page.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps (this website surface's owner) -- DISARM = any procedure this project or a future one documents for changing this form's (or any cached page's) live configuration names a mandatory `wp litespeed-purge all` (or equivalent targeted purge) as part of the change, not an afterthought discovered by re-fetching the page.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps (this website surface's owner) -- DISARM = any procedure this project or a future one documents for changing this form's (or any cached page's) live configuration names a mandatory `wp litespeed-purge all` (or equivalent targeted purge) as part of the change, not an afterthought discovered by re-fetching the page.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W1-S4",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE HONEYPOT'S `version_hash` CHECK IS DEFEATABLE BY A NON-JS SCRIPT: THE HASH IS A STATIC CONSTANT EMBEDDED IN THE PAGE'S INITIAL JS CONFIG BLOB, NOT COMPUTED PER-SESSION. `gform_theme_config` on the live page carries a literal `\"honeypot\":{\"version_hash\":\"3306833645cc55ebae51b15fd27abcd8\"}` -- a plain regex over the raw HTML extracts it with no JS engine required, and this seat used exactly that extraction to build the S1-AC5 real-visitor-equivalent probe. FWD-19's own ACCEPT line states a sophisticated bot still getting through is NOT a failure of this outcome, so this is filed as an OBSERVATION for the record, not a defect to fix -- gold-plating a fix here is explicitly out of scope.",
    "evidence": [
      "Raw curl fetch (no JS execution) of https://opalinvest.com/contact/, grep for `version_hash`: two hits, both the literal string `\"version_hash\":\"3306833645cc55ebae51b15fd27abcd8\"` inside the `gform_theme_config` JS variable -- present verbatim in the server-rendered HTML.",
      "This exact extracted value was used, unmodified, in this seat's S1-AC5 python probe (`.scratch/real_visitor_probe.py`) and the submission it produced landed status=active -- proving the value is sufficient on its own to pass `is_valid_version_hash()` with no JS execution.",
      "Plugin source (`class-gf-honeypot-handler.php`, `is_valid_version_hash()`) confirms the check is `in_array($hash, [wp_hash(GFForms::$version), wp_hash($previous_db_version)])` -- a function of the INSTALLED PLUGIN VERSION only, constant across every visitor and every session until the plugin is upgraded."
    ],
    "remedy": "NO REMEDY STATED BY THE ROW -- filed for the record; see world_is.",
    "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W1-S5",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "MEASURED AUTOMATED VOLUME ON /contact/ IS LOW, NOT HIGH: 8 OF 53 POSTs (15.1%) OVER 36.82 DAYS CARRY THIS SEAT'S MEASURED BOT DISCRIMINATOR -- ROUGHLY ONE TEMPLATED-UA SUBMISSION EVERY 4.6 DAYS, NOT 'A LOT'. FWD-19's own SOURCE line is Andrew-direct: 'We get a lot of bullshit form fillouts that are surely programmatic from bots.' The baseline census this TO commissioned (committed @6c4b8b8994) measured, over the full window the origin's own log retention allows (2026-08-04T15:31:44Z through 2026-09-10T11:19:02Z), 53 total POSTs to /contact/, of which 8 carry a quoted-UA or self-declared-bot signature (cross-checked 8-for-8 against the Gravity Forms entry store at matching IP+timestamp) and 18 total created a stored entry (8 automated, 10 human-like). This does not contradict Andrew's complaint -- 'a lot' is a subjective bar and this seat offers no verdict on it -- but the MAGNITUDE is recorded plainly because S1-AC7's judgment (whether the naive majority stops arriving) is graded against whatever bar the CVO reads into 'a lot', and a small base rate also means a short after-window (see the after-read's own window-length note) is even less likely to show a legible signal either way.",
    "evidence": [
      "`grep -c 'POST /contact/'` across all 16 retained access.log* files on i-0152e3fe2599fa630 (36.82-day window) -> 53, cross-verified by a full line-by-line dump matching the count exactly (no truncation).",
      "wp-cli `wp db query` against wp_gf_entry for form_id=1, date_created in the same window -> 18 rows; 8 of 18 carry a quoted-UA or explicit bot-token user_agent (ids 4,5,7,11,15,18,20,21), matching the 8 log-side hits by (ip, date) exactly, 8-for-8.",
      "All-time GF entry count (since the form's first-ever row, 2026-07-16, wider than the log-retention-bounded window) is 21, of which 10 are automated-flagged -- the same order of magnitude, ruling out the possibility that the log-bounded window happened to catch an unusually quiet stretch."
    ],
    "remedy": "NO REMEDY STATED BY THE ROW -- filed for the record; see world_is.",
    "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W2-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S2-AC4 COULD NOT BE MADE TO PASS BY THIS WORKER: NO AGENT ON THIS FABRIC HOLDS MAILBOX-READ ACCESS TO andrew@opalinvest.com, AND SNS EMAIL CONFIRMATION IS DELIVERED ONLY THROUGH THAT INBOX. `aws sns subscribe` to `arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts` (protocol email, endpoint andrew@opalinvest.com) returned `SubscriptionArn: \"pending confirmation\"`; `list-subscriptions-by-topic` read `PendingConfirmation` on every poll across ~7 minutes (5 polls at t+0..90s, one more after the S2-AC5/AC6 work). The confirmation link AWS sends exists only inside that mailbox; no comp-tool, AWS API, or credential in this repo (checked: 0 mailbox-read hits across the estate) can retrieve its Token in-band.",
    "evidence": [
      "`aws sns subscribe --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --protocol email --notification-endpoint andrew@opalinvest.com` -> rc=0, output `{\"SubscriptionArn\": \"pending confirmation\"}`.",
      "`aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts` run 5x over a bounded ~90s poll (2026-09-10T11:09:54Z..11:11:12Z) then once more at 11:16Z (~7 min after subscribe): every read shows exactly one subscription, protocol email, endpoint andrew@opalinvest.com, SubscriptionArn literally the string `PendingConfirmation` -- never a real ARN.",
      "`.tools/comp-find 'imap|gmail_api|mail\\.google\\.com|read_inbox|inbox_reader' --corpus all` -> DENOMINATOR 137 hits across 29324 files scanned, 0 of which are a mailbox-read capability (all are unrelated library/AST matches -- pygments IMAP lexer tokens, `as_completed`/`imap_unordered` iterator names). `.tools/comp-find 'ConfirmSubscription|confirm-subscription|PendingConfirmation' --corpus all` -> 75 hits, all either this TO's own text, alarm-reachability/critical-surface CHECKS that read `PendingConfirmation` as a failure state, or Terraform comments about the same expiry -- no site carries a token-retrieval or inbox-read path.",
      "This worker's tool set for the whole session is Bash/Read/Edit/Write/Glob/Grep (no email/MCP-inbox tool was offered), and the task order's own standing law states 'You cannot message anyone' -- so even relaying a request to Andrew to click the link is out of this turn's reach; the row is the only channel available."
    ],
    "remedy": "andrew@opalinvest.com (open the SNS confirmation email AWS already sent to that address and click the confirm link -- or extract its Token and run `aws sns confirm-subscription --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --token <token>`), or any future seat given mailbox-read access to that address. LEFT ALONE past SNS's ~3-day PendingConfirmation auto-expiry (org/modules/graph/critical-alarm-egress.yaml:8), the subscription is deleted and the alarms return to firing into a void, which is Z-S151's exact condition. Not this worker's to build: no messaging capability and no inbox-read tool is in this worker's write surface or capability set, and building one is new notification infrastructure the moratorium and this TO both forbid.",
    "owner": "andrew@opalinvest.com (open the SNS confirmation email AWS already sent to that address and click the confirm link -- or extract its Token and run `aws sns confirm-subscription --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --token <token>`), or any future seat given mailbox-read access to that address. LEFT ALONE past SNS's ~3-day PendingConfirmation auto-expiry (org/modules/graph/critical-alarm-egress.yaml:8), the subscription is deleted and the alarms return to firing into a void, which is Z-S151's exact condition. Not this worker's to build: no messaging capability and no inbox-read tool is in this worker's write surface or capability set, and building one is new notification infrastructure the moratorium and this TO both forbid.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "andrew@opalinvest.com (open the SNS confirmation email AWS already sent to that address and click the confirm link -- or extract its Token and run `aws sns confirm-subscription --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --token <token>`), or any future seat given mailbox-read access to that address. LEFT ALONE past SNS's ~3-day PendingConfirmation auto-expiry (org/modules/graph/critical-alarm-egress.yaml:8), the subscription is deleted and the alarms return to firing into a void, which is Z-S151's exact condition. Not this worker's to build: no messaging capability and no inbox-read tool is in this worker's write surface or capability set, and building one is new notification infrastructure the moratorium and this TO both forbid.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "andrew@opalinvest.com (open the SNS confirmation email AWS already sent to that address and click the confirm link -- or extract its Token and run `aws sns confirm-subscription --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --token <token>`), or any future seat given mailbox-read access to that address. LEFT ALONE past SNS's ~3-day PendingConfirmation auto-expiry (org/modules/graph/critical-alarm-egress.yaml:8), the subscription is deleted and the alarms return to firing into a void, which is Z-S151's exact condition. Not this worker's to build: no messaging capability and no inbox-read tool is in this worker's write surface or capability set, and building one is new notification infrastructure the moratorium and this TO both forbid.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W3-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THIS TO'S PREMISE IS STALE: THE LIFECYCLE-GUARD REMEDY Z-S136 CALLED FOR IS ALREADY COMMITTED AND LIVE-EFFECTIVE, five days before this TO's cut, via a DIFFERENT TO (TO-OP-S-15-19, commit 3758b14afc). All four sets now declare addresses=[] AND lifecycle{ignore_changes=[addresses]}, and a live test today (test address survives an unscoped plan) confirms the guard works. Separately, even had it not: this order's <paths> grants only infra/aws/terraform/opsec/ for terraform, which holds ONLY data-source references for the reconciler -- the actual resource declarations live in opal-gateway/waf.tf and portal-auth/waf-cloudfront.tf, neither granted.",
    "evidence": [
      "DECLARED STATE, ALL FOUR, RE-READ INDEPENDENTLY OF Z-S136 PER THIS TO'S OWN PREFLIGHT BOUND: opal_blocked_ips_regional_v4 (infra/aws/terraform/opal-gateway/waf.tf:259-298, addresses=[] at :264, lifecycle{ignore_changes=[addresses]} at :294-296), opal_blocked_ips_regional_v6 (waf.tf:300-339, addresses=[] at :305, lifecycle at :335-337), opal_blocked_ips_cloudfront_v4 (infra/aws/terraform/portal-auth/waf-cloudfront.tf:337-385, addresses=[] at :348, lifecycle at :378-380), opal_blocked_ips_cloudfront_v6 (waf-cloudfront.tf:387-427ish, addresses=[] at :392, lifecycle at :422-424). Denominator 4 of 4, matching Z-S136's count but NOT its shape: Z-S136 measured NO lifecycle block on any of the four; this read finds one on all four.",
      "AUTHORSHIP AND VINTAGE OF THE GUARD: git log -1 on both files returns commit 3758b14afc, author 0.7.0_AE_CloudOps~T, message 'opsec(NFRA_OPSEC202609.TO-OP-S-15-19, 0.7.0_AE_CloudOps~T): S15-AC5 -- STOP TERRAFORM BEING A SECOND WRITER OF THE BLOCKED-IP SETS. lifecycle ignore_changes = [addresses] on ALL FOUR sets across BOTH roots, proven against a POPULATED set', dated Fri Sep 4 00:46:06 2026 -0400 -- five days before this TO's 2026-09-10 issued_date. The commit's own body: 'FOUR OF FOUR, ACROSS TWO ROOTS ... All four carried addresses = []. All four now carry the lifecycle block' and 'PROVEN AGAINST A POPULATED SET ... AFTER the fix: portal-auth unscoped plan mentions 203.0.113.42 ZERO times'.",
      "LIVE READ TODAY (S3-AC2), BEFORE ANY TEST ACTION: aws wafv2 get-ip-set on all four returns Addresses:[] on every one -- opal-blocked-ips-regional (f073f448-eb85-4d23-9306-0cadf4573331), opal-blocked-ips-regional-ipv6 (85f90377-7cba-45dd-baca-397310d61f8e), opal-blocked-ips-cloudfront (b2e008a6-40d9-4d07-bef5-1caa8b682bb3), opal-blocked-ips-cloudfront-ipv6 (eb1a0caa-60a0-492e-a685-e5456cea8b7d). Declared and live AGREE (both empty) on all four -- S3-AC3's comparison.",
      "THE GUARD DEMONSTRATED LIVE, NOT REASONED ABOUT (S3-AC4): aws wafv2 update-ip-set added 192.0.2.55/32 (RFC 5737 TEST-NET-1) to opal-blocked-ips-regional; a subsequent unscoped terraform plan on opal-gateway ('Plan: 0 to add, 2 to change, 0 to destroy') shows only a description diff on both regional sets -- addresses is among the '7 unchanged attributes hidden' and 192.0.2.55/32 does not appear anywhere in the plan output. IDENTICAL diff shape to the plan taken immediately BEFORE the test address was added. The address was then removed (update-ip-set with an empty list) and a final get-ip-set confirms Addresses:[] again, matching the before-state exactly (S3-AC5). Full session recorded in the closed deploy-ledger entry org/critical_paths/change_management/20260910T1135Z_opsec-op3s3-blocked-ip-second-writer-verify_deploy_completion.md.",
      "THE <paths> MISMATCH, INDEPENDENT OF WHETHER A FIX WAS STILL NEEDED: this TO's <paths> names infra/aws/terraform/opsec/ as its only terraform grant. That module carries ZERO resource \"aws_wafv2_ip_set\" blocks -- comp-find 'resource \"aws_wafv2_ip_set\"' infra/aws/terraform returns exactly 4 hits, all in opal-gateway/waf.tf and portal-auth/waf-cloudfront.tf, none in opsec/. opsec/reconciler-lambda.tf:57-64 and opsec/iam_reconciler_and_cli.tf:60-87 hold only data \"aws_wafv2_ip_set\" READ references for the OP-s-15 reconciler Lambda's environment variables. Had the guard genuinely been missing, this order could not have applied its own remedy inside its granted write surface.",
      "THIS BOUNDARY WAS ALREADY NAMED ON Z-S136 ITSELF: that row's disarm_owner reads '2.0.0_SA_COO~Z (route to TO-OP-S-4-18 / the reconciler's cell: add lifecycle ignore_changes on addresses to all four sets; NOT this face's to edit)', and its notes cite 2.0.0_SA_COO~Z's own scope ruling (msg 20180): 'a rotation-blocker face is not an authorisation to restructure a root'. Z-S137 (subordinate row, same date) independently measured the SAME remedy shape effective in a worktree copy, but explicitly declined to assert it as committed because it was transient and uncommitted at that time -- the remedy this row finds committed is the same shape, landed five days later by TO-OP-S-15-19."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner 2.0.0_SA_COO~Z: The premise was stale at filing: the lifecycle guard this row worried about was already committed and live five days before this TO issued (TO-OP-S-15-19 @3758b14afc), independently re-verified live by this row's own author. Nothing needed building.\n\nWHY THIS IS FILED AS ONE ROW AND NOT TWO: the premise-staleness and the <paths> mismatch are one story -- the order was cut against Z-S136's vintage, which predates TO-OP-S-15-19's fix, and had it NOT predated it, this order could not have discharged its own deliverable inside its own write grant. Both halves are stated so a reader does not conclude from the second alone that the fix was simply misrouted; it was not routed at all, because it was already done. || WHAT THIS ROW DOES NOT DO: it does not dispute that Z-S136 was GROUNDED and correctly GRADUATED at the time it was written (2026-09-04, before the fix landed) -- the row was true of its vintage. It does not choose any address, block anything beyond the one TEST-NET-1 address added and removed under this same session's ledger, and does not touch opal-gateway/waf.tf or portal-auth/waf-cloudfront.tf (neither is in this order's <paths>; both remain byte-identical to HEAD across this session). || THE VERIFICATION VALUE KEPT DESPITE THE STALE PREMISE: S3-AC4 is 'the control that must be able to fail' per this order's own framing, and it was run for real against live AWS with a live terraform plan rather than reasoned about -- the fact that it PASSED is itself the answer to the question TO-OP-S-15-19's own commit left open ('NOT APPLIED -- the COO's BAR on portal-auth stands until lifted'): whatever that bar's current status, the guard is demonstrably active on THIS plane (terraform plan against current source) as of 2026-09-10T11:37Z, independent of any prior apply history for the lifecycle block itself, because ignore_changes is evaluated fresh at plan time from source, not from state history.",
    "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z (issuer default -- row named no disarm_owner)",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W4-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE ORDER'S <paths> WRITE GRANT CANNOT REACH THE ARTIFACT ITS OWN CRITERIA REQUIRE EDITING. S3A-AC4 and S3A-AC5 demand 'the diff of otp-liveness.tf AND ANY SOURCE FILE IT PACKAGES', but the two callers' credential logic lives entirely in the packaged Python, and the packaged Python is outside the grant. MEASURED: otp-liveness.tf:12 packages ../../lambda/m365-otp-liveness/lambda_function.py and ms-ingest.tf:23 packages ../../lambda/m365-ms-ingest-liveness/lambda_function.py (2 of 2 source_file references in the module); a --name '*.py' census over the granted directory returns 0 hits across 28 files scanned. The <paths> block names infra/aws/terraform/opal-gateway/ and does NOT name infra/aws/lambda/. Per .owned-paths.yaml:45-47 a 0.9.0_WK_* serial 'is admitted to exactly the <paths> a NON-TERMINAL task order ... names at HEAD ... A path the order does not name is a lane refusal' -- so the constraint is MECHANICAL, not merely textual. The .tf files carry only the env vars (URL + secret id); NOTHING in the .tf plane decides which credential is presented. The migration is a 3-to-5 line edit to each lambda_function.py, and this worker may not make it. SECOND LIMB OF THE SAME BLOCK: S3A-AC6/AC7 expect 'the log shows which credential path it took' -- neither running function emits any such line (deployed bytes verified byte-identical to the repo sources, sha256 fd13b490...c70f / 8f2b0aca...6000), so satisfying that clause is ALSO a lambda_function.py edit. NOT CLAIMED: that a terraform-only workaround is impossible in principle -- a second copy of the source under the granted directory, or archive_file inline content, would technically work; both were REFUSED here because they orphan the canonical source at infra/aws/lambda/ and stand up a duplicate source path, which is the exact shape CLAUDE.md s.5 vetoes ('NEVER stand up a shadow/build-alongside pipeline, duplicate output path').",
    "evidence": [
      "TO-OP3A-S-1 <paths> block at f20bc65d71, verbatim, 5 entries: infra/aws/terraform/opal-gateway/ ; the task-order file itself ; deliverables/0.9.0_WK_NFRA_OPSEC202609~4/ ; surprise-channel/investigations/INVESTIGATION_v1.md ; org/critical_paths/change_management/ . infra/aws/lambda/ appears in NONE of them.",
      "infra/aws/terraform/opal-gateway/otp-liveness.tf:12 @f20bc65d71: source_file = \"${path.module}/../../lambda/m365-otp-liveness/lambda_function.py\" -- and ms-ingest.tf:23: source_file = \"${path.module}/../../lambda/m365-ms-ingest-liveness/lambda_function.py\". comp-find 'source_file' over the granted directory: DENOMINATOR 2 hit(s) across 22 file(s), and both point outside the grant.",
      "comp-find --name '*.py' -- infra/aws/terraform/opal-gateway : 0 hit(s) across 28 file(s) scanned [corpus=all]. There is no Python inside the write grant to edit.",
      ".owned-paths.yaml:45-47 @f20bc65d71, serial_glob \"0.9.0_WK_*\", note verbatim: 'a worker serial 0.9.0_WK_<CODE>~<n> is admitted to exactly the <paths> a NON-TERMINAL task order under <CODE>, issued_to that serial, names at HEAD ... A path the order does not name is a lane refusal'.",
      "THE CODE IS WHAT DECIDES THE CREDENTIAL, measured on the DEPLOYED bytes not the repo alone: aws lambda get-function -> Code.Location -> downloaded zip (1996 B / 1697 B, single entry lambda_function.py); deployed sha256 fd13b4905476d692752a277cae109c2721288ba9d7469adb9a0cc0c29d73c70f (3947 B) == repo infra/aws/lambda/m365-otp-liveness/lambda_function.py, and 8f2b0aca27da50324b981dcc439999c1032406b5768935492c5030cbea046000 (3301 B) == repo m365-ms-ingest-liveness. Both running bodies build urllib.request.Request(HEALTH_URL, headers={'Authorization': f'Bearer {bearer}'}) where bearer is the Secrets-Manager static value -- the exchange endpoint is never called.",
      "NEITHER function prints a credential-path line: the only print( in either body is the SES-skip except-handler. The AC6/AC7 clause 'the log shows which credential path it took' is unsatisfiable without a source edit, and the manual invocations confirm it -- both returned {\"ok\": true, \"detail\": \"status=200\"} with log tails containing only START/END/REPORT."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner 2.0.0_SA_COO~Z: Disarm condition (add both Lambda source directories to <paths>) MET @775e6cf20a and CONFIRMED BY EXERCISE per the project's own Z-S177 row: the successor slot wrote both lambda_function.py files under the widened grant, which was mechanically impossible before the amendment.\n\nWHAT THIS WORKER DID ESTABLISH BEFORE HITTING THE WALL, so the successor does not re-measure it. (1) DUAL-ACCEPT RE-MEASURED TODAY, not inherited: static bearer -> GET /otp/health = 200 {\"ok\":true} at 2026-09-10T16:13:51Z, with no-auth 401 and junk-auth 401 as separate invocations, so the 200 discriminates. (2) THE EXCHANGE CONTRACT, READ FROM THE ENDPOINT RATHER THAN ASSUMED, and it is NOT a Microsoft OIDC 302: GET /otp/token = 405 Method Not Allowed, server: uvicorn, allow: POST. POST /otp/token no-auth = 401 www-authenticate: Bearer; POST with the static bearer = 200 application/json cache-control: no-store, body {capability_token, token_type:\"Bearer\", expires_in:300, aud:\"gw:otp\"}. The capability_token is an RS256 JWT, kid ac4c49e6c8bec6d4, claims iss=https://mcp.opalinvest.dev sub=49f aud=gw:otp typ=capability exp=iat+300, and presenting it to GET /otp/health returns 200 {\"ok\":true}. /ms/token is the identical shape with sub=ms aud=gw:ms. CROSS-AUDIENCE CONTROL: the gw:ms capability token presented to /otp/health returns 401, so audience binding is enforced and the 200s are not 'any JWT passes'. (3) THE PREFLIGHT'S UNMEASURED IAM ITEM IS NOW MEASURED and needs NO change: simulate-principal-policy, one --resource-arns per call -- opal-otp-liveness-role x secretsmanager:GetSecretValue x the 49f secret ARN = allowed; opal-ms-ingest-liveness-role x its own secret ARN = allowed; NEGATIVE CONTROL as a separate invocation, opal-otp-liveness-role x the MS secret ARN = implicitDeny, so the simulator discriminates. The exchange path reads the SAME secret it reads today (the static bearer is what is presented AT /otp/token), so the existing least-privilege grant already reaches it. NOT CLAIMED: that no OTHER IAM action is needed -- only GetSecretValue on the existing secret was simulated, and the exchange adds no AWS API call. (4) NOTHING WAS RETIRED OR REVOKED and no alarm/monitor/notification was created. (5) BOUND ON THE INVOCATIONS: both manual invokes ran against a gateway measured healthy seconds earlier, so neither could fire the SNS/SES alert path; that was checked BEFORE invoking, not inferred after.",
    "owner": "2.0.0_SA_COO~Z. DISARM = re-cut TO-OP3A-S-1 (or issue its successor) with infra/aws/lambda/m365-otp-liveness/ and infra/aws/lambda/m365-ms-ingest-liveness/ ADDED to the <paths> block. This is a WRITE-GRANT question only and must not be re-raised as a permission or scope question: Andrew authorised the migration at @9382d107a3 s.1, the CTO ruled it at msg 20769, and the order's own criteria already name the packaged source as the artifact to diff -- the grant is simply narrower than the criteria it must serve. NOTHING ELSE ABOUT THIS ORDER IS BLOCKED: the safety re-grounding (AC1/AC2/AC3) is complete and green, the exchange contract is READ and works end to end, and the IAM question the preflight left UNMEASURED is now MEASURED as sufficient with no change needed -- a successor worker with the wider grant starts at the code edit.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z. DISARM = re-cut TO-OP3A-S-1 (or issue its successor) with infra/aws/lambda/m365-otp-liveness/ and infra/aws/lambda/m365-ms-ingest-liveness/ ADDED to the <paths> block. This is a WRITE-GRANT question only and must not be re-raised as a permission or scope question: Andrew authorised the migration at @9382d107a3 s.1, the CTO ruled it at msg 20769, and the order's own criteria already name the packaged source as the artifact to diff -- the grant is simply narrower than the criteria it must serve. NOTHING ELSE ABOUT THIS ORDER IS BLOCKED: the safety re-grounding (AC1/AC2/AC3) is complete and green, the exchange contract is READ and works end to end, and the IAM question the preflight left UNMEASURED is now MEASURED as sufficient with no change needed -- a successor worker with the wider grant starts at the code edit.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W5-S1",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE SHARED TERRAFORM ROOT THIS ORDER MUST APPLY WAS ALREADY DIRTY, AND NOT WITH MY WORK. A baseline `terraform plan` of infra/aws/terraform/opal-gateway, taken BEFORE any edit of mine, returned `Plan: 0 to add, 2 to change, 0 to destroy` -- two `aws_wafv2_ip_set` resources (opal_blocked_ips_regional_v4 and _v6) each acquiring a `description` that is declared in waf.tf and ABSENT on the live set. Those resources are `0.7.0_AE_CloudOps`'s (waf.tf @37c4bde812 TO-OP-S-4-18, @3758b14afc TO-OP-S-15-19), not this order's. My task order says `safe-apply only` and says nothing about scoping, so the literal reading -- apply the root -- would have SILENTLY LANDED ANOTHER LANE'S PENDING CHANGE under this order's ledger entry and this order's serial. I scoped my apply with `-target=aws_lambda_function.otp_liveness -target=aws_lambda_function.ms_ingest_liveness`, which plans exactly `0 to add, 2 to change, 0 to destroy` over my two functions and excludes both IP sets. THE GENERAL SHAPE, which is what makes this worth a row rather than a footnote: a DESIRED-not-APPLIED change parked in a shared Terraform root is invisible to everyone until someone else's unrelated apply carries it, and the carrier's ledger entry, commit author and audit trail all name the WRONG LANE. NOT CLAIMED: that the two descriptions are wrong, harmful, or that anyone erred in leaving them -- a description-only delta on a WAF IP set is close to harmless in itself. What is claimed is that the ROOT IS A SHARED MUTABLE SURFACE WITH NO PER-LANE PARTITION, and that an untargeted apply by any lane is the delivery mechanism.",
    "evidence": [
      "BASELINE PLAN, taken in this worktree at HEAD c9c6600e95 with NO edit of mine present, between my 17:01:32Z and 17:12:15Z live reads: `terraform -chdir=infra/aws/terraform/opal-gateway plan -input=false -lock=false -no-color` -> rc 0, `Plan: 0 to add, 2 to change, 0 to destroy.` (line 133 of 140 in the captured output).",
      "THE TWO RESOURCES, verbatim from that plan: `# aws_wafv2_ip_set.opal_blocked_ips_regional_v4 will be updated in-place` with `+ description = \"NFRA_OPSEC202609 C-2: addresses blocked at the ALB. Written ONLY by the OP-s-15 reconciler from opal-suspicious-addresses, never by hand.\"`, and `# aws_wafv2_ip_set.opal_blocked_ips_regional_v6 will be updated in-place` with `+ description = \"NFRA_OPSEC202609 C-2: IPv6 sibling of opal-blocked-ips-regional. ...\"`. The `+` on a `~ update in-place` is the tell: the attribute is declared in the repo and absent live.",
      "OWNERSHIP, read from history rather than assumed: `git log -3 -- infra/aws/terraform/opal-gateway/waf.tf` -> 3758b14afc `0.7.0_AE_CloudOps~T` 2026-09-04 (TO-OP-S-15-19, lifecycle ignore_changes on all four sets), 37c4bde812 `0.7.0_AE_CloudOps~S` 2026-09-03 (TO-OP-S-4-18, the two regional sets created EMPTY), a7312b946b `0.7.0_AE_CloudOps` 2026-08-14. The resource name resolves to exactly 1 file under the granted directory (waf.tf).",
      "MY SCOPED PLAN, the remedy, run immediately after: same command plus `-target=aws_lambda_function.otp_liveness -target=aws_lambda_function.ms_ingest_liveness` -> rc 0, `Plan: 0 to add, 2 to change, 0 to destroy`, the two changed resources being `aws_lambda_function.ms_ingest_liveness` and `aws_lambda_function.otp_liveness`, with `Warning: Resource targeting is in effect`. Neither IP set appears.",
      "THE TASK ORDER'S TEXT, quoted so the gap is legible: `**safe-apply only, never bare terraform apply.** A deploy-ledger entry under org/critical_paths/change_management/ is OPENED before any apply and CLOSED at completion.` There is no scoping clause, and `<paths>` grants the whole `infra/aws/terraform/opal-gateway/` directory -- which is a WRITE grant over waf.tf as well."
    ],
    "remedy": "WHY I RAN A BASELINE PLAN AT ALL, since nothing told me to: an apply is directory-grained while a task order is cell-grained, and those two grains only coincide when the directory happens to be clean. That is a property of the WORLD at apply time, not of the order -- so it is measurable, and measuring it costs one plan. THIS ROW IS ABOUT WHAT THE MEMBERS SHARE. Per-cell verification cannot see it: every cell in this root can be individually correct while the ROOT they share is dirty, and each cell's own apply is the thing that delivers the others' drift. CONSEQUENCE THIS ORDER ADDS, stated against myself rather than left for someone to find: my own commit puts a THIRD pending in-place change into this same root (the two Lambda functions), because the deploy leg of this order was blocked by a separate gate refusal -- see Z-W5-S2. After this commit an untargeted apply of `infra/aws/terraform/opal-gateway` lands FOUR resource changes across THREE lanes' work. That is recorded in the deploy-ledger entry `20260910T1714Z_opsec-op3a-s1-liveness-exchange-migration_deploy_completion.md`, which is OPEN and says so.",
    "owner": "0.7.0_AE_CloudOps owns the two resources and waf.tf, and is the only lane that can say whether the pending descriptions should be applied or reverted. 2.0.0_SA_COO~Z routes it, being this project's issuer and the seat that cuts orders into this root. NOTHING IS ASKED OF THIS WORKER'S ORDER: I disarmed my own instance by targeting, and the residual -- the next untargeted apply of this root by anyone -- is not mine to fix and I did not touch waf.tf.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps owns the two resources and waf.tf, and is the only lane that can say whether the pending descriptions should be applied or reverted. 2.0.0_SA_COO~Z routes it, being this project's issuer and the seat that cuts orders into this root. NOTHING IS ASKED OF THIS WORKER'S ORDER: I disarmed my own instance by targeting, and the residual -- the next untargeted apply of this root by anyone -- is not mine to fix and I did not touch waf.tf.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps owns the two resources and waf.tf, and is the only lane that can say whether the pending descriptions should be applied or reverted. 2.0.0_SA_COO~Z routes it, being this project's issuer and the seat that cuts orders into this root. NOTHING IS ASKED OF THIS WORKER'S ORDER: I disarmed my own instance by targeting, and the residual -- the next untargeted apply of this root by anyone -- is not mine to fix and I did not touch waf.tf.",
      "at": null
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W5-S2",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE ORDER'S AMENDMENT WIDENED `<paths>` BUT NEVER MOVED `<issued_to>`, AND THAT IS A HARD MECHANICAL BLOCK ON THE ONE ACT THE ORDER EXISTS TO PERFORM. TO-OP3A-S-1 was amended @775e6cf20a to grant the two Lambda source directories after `~4` was blocked by the narrow grant; `<issued_to>` still reads `0.9.0_WK_NFRA_OPSEC202609~4`. `.tools/safe-apply.sh` runs `.tools/halt-gate-check.sh` first, and that gate admits a spine-v3 worker ONLY while a NON-TERMINAL task order under <CODE> at HEAD is `issued_to` it (halt-gate-check.sh:141-180, `halt_gate_worker_issuer`). Census, unscoped: `issued_to 0.9.0_WK_NFRA_OPSEC202609~5` = 0 of 35 task orders under this project at HEAD. So `safe-apply` refuses this seat rc=3, verbatim `HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed) / Resolved serial: 0.9.0_WK_NFRA_OPSEC202609~5`. THE REFUSAL IS CORRECT AND I DID NOT OVERRIDE IT. The gate scans the worker's ISSUER's inbox for [STOP] messages; a worker with no order has no issuer to scan, and admitting it means deploying blind to a STOP. The rc=3 identity branch carries no override by design. I could have made myself admissible by editing one line of the task order -- `<issued_to>` is inside my own `<paths>` grant -- and that is precisely manufacturing my own admission past a safety gate, and an issuer act rather than a worker's. So S3A-AC4 and S3A-AC5 (declaration-plane) are met and S3A-AC6, S3A-AC7 and S3A-AC8 (deploy-plane) are NOT, and I am saying so rather than reaching for the edit. NOTHING LANDED: both functions read their pre-deploy CodeSha256 and LastModified at 17:23:16Z with neither new env var present, so NEVER-2 is not engaged.",
    "evidence": [
      "THE FIELD AT HEAD: `git show HEAD:org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP3A-S-1.in-lane-liveness-caller-migration.md | grep -m1 -oE '<issued_to>[^<]*</issued_to>'` -> `<issued_to>0.9.0_WK_NFRA_OPSEC202609~4</issued_to>` at c9c6600e95.",
      "THE CENSUS WITH ITS DENOMINATOR, taken over every task order the gate itself globs (`git ls-files -- org/missions/D*/*/NFRA_OPSEC202609/task-orders/*.md`), reading `<issued_to>` from `git show HEAD:<p>` on each: `issued_to ~5: 0 of 35 task orders`. Not a page, not a first-hit stop -- all 35 read.",
      "THE REFUSAL, verbatim and reproduced twice. First run 17:17:39Z: `HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)` (no session serial file in a fresh worktree). After writing `org/mcp/sessions/<session-id>.serial` = `0.9.0_WK_NFRA_OPSEC202609~5` exactly as that banner instructs: `HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed) ... Resolved serial: 0.9.0_WK_NFRA_OPSEC202609~5 ... a spine-v3 worker (0.9.0_WK_<CODE>~<n>) is admitted only while a NON-TERMINAL task order under <CODE> at HEAD is issued_to it.` APPLY_RC=3 both times.",
      "THE GATE'S MECHANISM, read at source rather than inferred from the banner: halt-gate-check.sh `halt_gate_worker_issuer` extracts `<issued_to>` from each task order at HEAD, `[ \"$issued_to\" = \"$serial\" ] || continue`, skips terminal statuses, and prints `<issued_by>`; `halt_gate_validate_serial` routes any `0.9.0_WK_*~[0-9]*` serial through it and returns 1 on no match. The header comment states the intent: `Its STOPs are its ISSUER's: a worker has no inbox by design (spine v3 L7), so the gate scans the inbox of the issuer that order names ... Fail-closed: no such order, no admission.`",
      "NO SANCTIONED OVERRIDE EXISTS FOR THIS BRANCH, read from source and DELIBERATELY NOT EXERCISED: `HALT_OVERRIDE` appears at halt-gate-check.sh:415, inside the STOP-message branch that is only reached after identity resolves; `HALT_ACK` at :438 answers the routine-unacked exit-1 path. The exit-code contract at :31 is `0 pass | 1 routine-unacked | 2 stop-block | 3 no-serial`, and the banner says in terms `Do NOT override this`. I did not run safe-apply with HALT_OVERRIDE set: a test whose failure mode is performing the deploy I had just declined to authorise myself for is not a safe test, and reading the branch structure answers the question without that risk.",
      "NOTHING LANDED, measured on the LIVE plane AFTER the refusal at 17:23:16Z: `opal-otp-liveness` CodeSha256 `hot3riLNhAoNfPYJhQPI/z/TW5Cd4BjfaQ73Q5oZbMU=` LastModified `2026-08-15T02:32:24.425+0000`, `OTP_TOKEN_URL` absent; `opal-ms-ingest-liveness` CodeSha256 `eJivS8spnzrkj5eCovTF5BWU22kclsEMabGOrQYQ6UI=` LastModified `2026-08-15T02:32:30.583+0000`, `MS_TOKEN_URL` absent. Byte-identical to the values read at 16:5xZ before any edit. Terraform was never invoked; the gate exits before the `exec`.",
      "THE WORK ITSELF IS DONE AND VALIDATED, so the block is on the DEPLOY leg only: both `lambda_function.py` patched (py_compile clean), both `.tf` patched (`terraform validate` Success, `terraform fmt -check` rc 0), and BOTH PATCHED HANDLERS EXERCISED LOCALLY AGAINST THE LIVE GATEWAY with `_alert` hard-stubbed to abort rather than publish -> `{\"ok\": true, \"cred_path\": \"exchange\", \"detail\": \"status=200\"}` on each at 17:12:15Z."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner 2.0.0_SA_COO~Z: Disarm condition (move <issued_to> to the executing slot) MET @1f87188985 (re-seat ~4 -> ~6, the WHOLE identity block) and CONFIRMED BY EXERCISE: slot ~6 committed and deployed the migration clean (deploy-ledger 20260910T1714Z entry, CodeSha256 matching the targeted plan on both functions).\n\nTHIS IS THE SAME AMENDMENT, HALF-APPLIED -- and the shape is one this order has already produced once. `~4` was blocked because `<paths>` named a directory containing none of the code the criteria describe. `~5` is blocked because `<issued_to>` names a serial that is not executing. Both are IDENTITY-OR-GRANT FIELDS that a criterion never reads, so nothing in the acceptance set can fail on them: they surface only when a WRITE or a DEPLOY is attempted, which is after every cheap criterion has already passed and the order looks nearly done. THE INSTRUMENT POINT, offered because it is cheap and general: the amendment was verified against the DEFECT it was fixing (`comp-find 'source_file'`, `comp-find --name '*.py'` -- both correct, both run) and not against the ACT it was enabling. A grant that reaches the code is necessary and is not sufficient; the seat must also be admissible to the tools the order names. Running the order's mandated invocation once, under the new serial, would have caught it in about ten seconds -- which is the same lesson the amendment itself already records, one field over. NOT CLAIMED: that the gate should change, that workers should be admitted more loosely, or that anything about the halt-gate design is wrong. It refused correctly and its refusal is the reason this is a row and not a silent blind deploy. NOT CLAIMED EITHER: that the migration is wrong or risky -- it is written, validated, and exercised end-to-end against the live gateway from this workstation; only the last mile, applying it to the two functions, is unperformed. ONE FURTHER ITEM, recorded here rather than as its own row because it is the same block one step earlier: `safe-apply` also refused on first run with `IDENTITY UNRESOLVED` because a freshly-created worktree has no `org/mcp/sessions/<session>.serial`. That path is gitignored (.gitignore:423) and `HALT_GATE_REPO_ROOT` resolves to the worktree root, so writing it is worktree-local runtime state and not a repo edit or a lane question -- but it IS a precondition of the order's mandated verb that no task order face states, and every worker cut into a fresh worktree will meet it.",
    "owner": "2.0.0_SA_COO~Z -- this order's own `<issued_by>`, the author of the @775e6cf20a amendment, and the only seat that can re-issue. THE DISARM IS ONE LINE: set `<issued_to>` to the serial of the slot that is actually executing, and commit it, exactly as the `<paths>` half of the same amendment was committed. It is the SAME AMENDMENT that is half-applied, not a new decision. ARMED because it recurs by construction: every re-slotting of a worker order that moves `<paths>` and not `<issued_to>` re-arms it, and the block only surfaces at the deploy step, after all the cheap criteria have already passed.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z -- this order's own `<issued_by>`, the author of the @775e6cf20a amendment, and the only seat that can re-issue. THE DISARM IS ONE LINE: set `<issued_to>` to the serial of the slot that is actually executing, and commit it, exactly as the `<paths>` half of the same amendment was committed. It is the SAME AMENDMENT that is half-applied, not a new decision. ARMED because it recurs by construction: every re-slotting of a worker order that moves `<paths>` and not `<issued_to>` re-arms it, and the block only surfaces at the deploy step, after all the cheap criteria have already passed.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W5-S3",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE SAME `<issued_to>` DEFECT ALSO BLOCKS THE COMMIT, NOT ONLY THE DEPLOY -- AND THIS IS STRICTLY WORSE THAN Z-W5-S2 RECORDED. Z-W5-S2 was written believing the cost was the last mile: code committed, deploy blocked. It is not. `.tools/safe-commit.sh` REFUSED rc=1 with SIX owned-paths lane violations, one per `infra/` path, each reading verbatim: `agent=0.9.0_WK_NFRA_OPSEC202609~5 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block (ADHC_OWNPTH.005: the order is the grant; a missing path is a cut defect, never an override)`. The lane gate resolves a worker's write grant through the SAME `<issued_to>` field the halt gate resolves admission through, so ONE stale field disables BOTH the write and the deploy. The `<paths>` block DOES name these directories -- the @775e6cf20a amendment added them -- but the gate can never read that grant for a serial no order is issued to. THE ORDER'S OWN AMENDMENT IS THEREFORE UNREACHABLE BY THE SEAT IT WAS WRITTEN FOR. Split by plane, measured: 6 of 9 dispatched paths REFUSED (2 lambda_function.py, 2 .tf, 2 .build zips, all under infra/), 3 of 9 ADMITTED (the deploy-ledger entry, this channel file, and the proof-of-spec instance -- all under org/, whose lanes do not key on the task order). So the record of the defect can land and the work it describes cannot. I DID NOT USE `GIT_COMMIT_AUTHOR_OVERRIDE`, which CLAUDE.md 14a names as the audited escape for a lane refusal: a `<paths>` entry the gate cannot reach is a cut defect and a BLOCKING row, never an override, and overriding here would have written six files into a lane on the strength of my own say-so. THE CODE IS NOT LOST: it is intact and unstaged in worktree C:/tmp/wk-opsec-3a-5 on branch wk-NFRA_OPSEC202609-3A-5, and a git-format patch of all four text files is committed to this order's deliverables folder as a RECORD (sha256 a5bf2999bcbf7c11..., 8003 bytes, 140 lines) so that the work survives the worktree.",
    "evidence": [
      "THE REFUSAL, verbatim from `.tools/safe-commit.sh --author \"0.9.0_WK_NFRA_OPSEC202609~5 <...>\" -F <msgfile> -- <9 paths>`: `ERROR: owned-paths lane violation(s) detected (block mode):` then six `VIOLATION:` lines, one each for infra/aws/lambda/m365-ms-ingest-liveness/lambda_function.py, infra/aws/lambda/m365-otp-liveness/lambda_function.py, infra/aws/terraform/opal-gateway/.build/m365-ms-ingest-liveness.zip, infra/aws/terraform/opal-gateway/.build/m365-otp-liveness.zip, infra/aws/terraform/opal-gateway/ms-ingest.tf, infra/aws/terraform/opal-gateway/otp-liveness.tf -- each `lane=CLOUD_OPS_OR_ETL ... agent=0.9.0_WK_NFRA_OPSEC202609~5 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block`. Then `ERROR: safe-commit did NOT commit (rc=1).`",
      "THE COMMIT DID NOT HAPPEN, asked of the REPOSITORY rather than read off the tool's stdout (the refusal text says in terms not to grep itself): `git status --porcelain` after the refusal shows the six infra paths still as worktree modifications and no new commit on the branch; branch tip unchanged at c9c6600e95 until the org-only commit that carries this row.",
      "THE GRANT EXISTS IN THE DOCUMENT AND IS UNREADABLE TO THE GATE: the task order's `<paths>` block at HEAD names `infra/aws/terraform/opal-gateway/`, `infra/aws/lambda/m365-otp-liveness/` and `infra/aws/lambda/m365-ms-ingest-liveness/` -- the amendment @775e6cf20a added the last two precisely so a worker could reach them. The gate's refusal text names the missing precondition as the ORDER, not the path: `no NON-TERMINAL task order at HEAD issued_to this serial NAMES this path`. Both conjuncts are required and the first fails.",
      "ONE FIELD, TWO GATES -- the shared dependency, which is the part a per-gate check cannot see: `.tools/halt-gate-check.sh` (`halt_gate_worker_issuer`) and the owned-paths lane gate invoked by `.tools/safe-commit.sh` (ADHC_OWNPTH.005) BOTH resolve a `0.9.0_WK_*` serial by finding a non-terminal task order at HEAD whose `<issued_to>` equals it. Neither can be satisfied without the other, and one commit fixes both.",
      "THE PLANE SPLIT, with its denominator, measured on the same single invocation: 9 dispatched paths; 6 REFUSED, all under `infra/`; 3 ADMITTED, all under `org/` (org/critical_paths/change_management/..., org/missions/.../surprise-channel/investigations/INVESTIGATION_v1.md, org/missions/.../deliverables/0.9.0_WK_NFRA_OPSEC202609~5/...proof_of_spec.json). Every other gate in the same run PASSED before this one: commit-gate `All checks passed!`, to-pipeline-gate OK, surprise-corpus OK `4 known, 0 new, 0 resolved`, surprise-row-gate `2 new row(s) of 184 total checked (182 pre-existing, NOT re-graded)`.",
      "THE WORK IS INTACT AND RECOVERABLE, stated so the block is not read as data loss: the four edited text files remain as unstaged modifications in C:/tmp/wk-opsec-3a-5 on branch wk-NFRA_OPSEC202609-3A-5, and `git diff` over them is committed to this order's deliverables folder as OP3A-s-1.exchange-migration.WORKTREE-ONLY.patch (sha256 a5bf2999bcbf7c1125eecd83ed28f0bbb41734786ba8e18b8ec6d9be0c9d8c24, 8003 bytes, 140 lines). IT IS A RECORD, NOT A SOURCE: nothing reads it, no terraform references it, it stands up no duplicate source path, and it is applied back onto the four canonical paths with `git apply` by whoever is admitted."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-10T20:35Z, owner 2.0.0_SA_COO~Z: Same disarm as Z-W5-S2 (one field, both gates) and confirmed by the same exercise: slot ~6's commit landed all six previously-refused infra/ paths.\n\nWHAT I GOT WRONG IN MY OWN PREVIOUS ROW, recorded because it is the more useful half: Z-W5-S2 measured the halt gate, found the cause, and then ASSUMED THE BLAST RADIUS -- it said the declaration-plane criteria were satisfiable and satisfied, on the strength of having run the diff, py_compile, terraform validate and a live exercise. All of those were true and none of them is a COMMIT. I verified the work and inferred that landing it would follow, which is the same rung-skip the row was about. The correction cost one command. A ROOT CAUSE IS NOT A BLAST RADIUS: I identified the stale field correctly and then scoped its consequence to the gate I happened to be standing in front of, when the field is read by at least two independent gates and I had not asked which. The general form: when a defect is in a SHARED INPUT, enumerate the consumers before stating what it costs -- checking the consumer in front of you certifies nothing about the others, and they all agree about the same wrong thing. NOT CLAIMED: that the owned-paths gate is wrong. It is right, it fails closed, and its refusal text names the true precondition precisely (`the order is the grant; a missing path is a cut defect, never an override`). NOT CLAIMED EITHER: that the migration is unsound -- it is written, py_compile-clean, terraform-validate-clean, terraform-fmt-clean and exercised end to end against the LIVE gateway from this workstation, returning {\"ok\": true, \"cred_path\": \"exchange\", \"detail\": \"status=200\"} on both callers at 17:12:15Z. What is unperformed is landing it, on both planes, for one missing line.",
    "owner": "2.0.0_SA_COO~Z -- unchanged from Z-W5-S2, because it is the SAME one-line disarm: set `<issued_to>` on TO-OP3A-S-1 to the serial of the slot actually executing, and commit it. That single edit releases BOTH gates at once, since both read the same field. ARMED and NOT merely BLOCKING: left alone, the committed record of this order will state that a migration was written while the migration itself exists only as an unstaged worktree change and a patch file, and a reader of the repo alone would find the two `.tf` files and both `lambda_function.py` unchanged. FILED SEPARATELY FROM Z-W5-S2 RATHER THAN AMENDING IT, per the append-only contract: S2 is accurate about what it measured and its scope claim -- that the block is the deploy leg -- is too narrow. This row is the correction, not a restatement.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z -- unchanged from Z-W5-S2, because it is the SAME one-line disarm: set `<issued_to>` on TO-OP3A-S-1 to the serial of the slot actually executing, and commit it. That single edit releases BOTH gates at once, since both read the same field. ARMED and NOT merely BLOCKING: left alone, the committed record of this order will state that a migration was written while the migration itself exists only as an unstaged worktree change and a patch file, and a reader of the repo alone would find the two `.tf` files and both `lambda_function.py` unchanged. FILED SEPARATELY FROM Z-W5-S2 RATHER THAN AMENDING IT, per the append-only contract: S2 is accurate about what it measured and its scope claim -- that the block is the deploy leg -- is too narrow. This row is the correction, not a restatement.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-10T20:35Z"
    }
  },
  {
    "id": "NFRA_OPSEC202609-Z-W5-S4",
    "project": "NFRA_OPSEC202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE PROOF-OF-SPEC CONTRACT HAS NO REPRESENTATION FOR AN ARTIFACT THAT WAS PRODUCED BUT REFUSED, SO A BLOCKED WORKER'S CENTRAL DELIVERABLE MUST LEAVE `artifacts_produced` ALTOGETHER. `proof-of-spec-check.py` accepts exactly two shapes for a repo artifact's `commit_or_etag`: the literal `PENDING-THIS-COMMIT`, which it then VERIFIES is STAGED in this commit, or a 7-40 character hex commit-ish. My four migrated files are neither -- they are written, py_compile-clean, terraform-validate-clean, exercised end-to-end against the live gateway, and REFUSED by the owned-paths lane gate (Z-W5-S3), so no commit carries them and they will not ride this one. I tried `UNCOMMITTED-LANE-GATE-REFUSED` and the checker refused it four times, verbatim: `carries commit_or_etag 'UNCOMMITTED-LANE-GATE-REFUSED', which is neither PENDING-THIS-COMMIT nor a 7-40 hex commit-ish for a repo artifact`. BOTH PERMITTED ENCODINGS ARE FALSE STATEMENTS HERE -- `PENDING-THIS-COMMIT` asserts the file rides this commit, and a hex pin asserts a commit that does not exist -- so the only schema-VALID move is to DELETE the artifact rows and describe the files in prose under `declared_exclusions`. THE CONSEQUENCE IS THE PART THAT MATTERS: an instance can now be VALID, rc=0, with the deliverable it exists to prove ABSENT from its own artifact list. `deployed_state` already carries a three-value axis for how far an artifact got (DEPLOYED-VERIFIED / COMMITTED-NOT-DEPLOY-SCOPE / STAGED-AWAITING-GATE) and every one of them presupposes the commit succeeded; the gap is one rung EARLIER than the axis begins. NOT CLAIMED: that the checker is wrong to refuse an unrecognised string -- fail-closed on an unknown value is correct, and a free-text escape hatch would rot to unpopulated. What is claimed is that the DOMAIN is not covered: a produced-and-refused artifact is a real state of the world with no member.",
    "evidence": [
      "THE REFUSAL, verbatim, 4 of 4 infra artifact rows, from `python .tools/proof-of-spec-check.py <instance> S3A-AC1,...,S3A-AC9` run from inside this worktree: `VIOLATION: artifact-resolution: 'infra/aws/lambda/m365-otp-liveness/lambda_function.py' carries commit_or_etag 'UNCOMMITTED-LANE-GATE-REFUSED', which is neither PENDING-THIS-COMMIT nor a 7-40 hex commit-ish for a repo artifact` -- and the identical line for m365-ms-ingest-liveness/lambda_function.py, opal-gateway/otp-liveness.tf and opal-gateway/ms-ingest.tf. INVALID (rc=1).",
      "THE PRIOR ATTEMPT, which is the other half of the box: with those same four rows carrying `PENDING-THIS-COMMIT` but NOT staged, the checker refused them the other way -- `is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and NOT staged -- it will not ride this commit; pin the row to the commit that carried it (CCX class)`. So the two permitted encodings fail in opposite directions on the same true state, which is what makes it a gap rather than a mistake of mine.",
      "THE SCHEMA'S OWN AXIS, read at org/standards/PROOF_OF_SPEC.schema.json: `deployed_state` enumerates DEPLOYED-VERIFIED, COMMITTED-NOT-DEPLOY-SCOPE and STAGED-AWAITING-GATE, described as `an atomic commit is NOT an atomic deploy; state which`. All three sit at or past a successful commit. `commit_or_etag` is `type: string, minLength: 6` at the schema level -- the two-shape restriction is the CHECKER's, not the schema's, so schema-validity and checker-validity disagree about this field.",
      "THE RESOLUTION I TOOK, so the record is not silently short: the four artifact rows were REMOVED from artifacts_produced and a `declared_exclusions` entry naming all four paths was added in their place, citing this row. The work itself is carried by three other surfaces in the same instance -- the committed patch record OP3A-s-1.exchange-migration.WORKTREE-ONLY.patch (artifact_covered_by S3A-AC4, S3A-AC5), the full diffs pasted verbatim in S3A-AC4 and S3A-AC5 output_evidence, and the exclusion naming the blocked commit. After the removal the checker reads VALID.",
      "THE DENOMINATOR OF THE DAMAGE, measured on this instance: artifacts_produced went from 7 rows to 3, and 4 of 4 removed rows are the order's actual subject (both packaged sources and both terraform declarations). The 3 that remain are the deploy-ledger entry, the surprise channel and the patch record -- every one of them a RECORD OF THE WORK rather than the work."
    ],
    "remedy": "WHY THIS IS THE THIRD ROW OF THE SAME SHAPE TODAY AND I AM NAMING THE SHAPE RATHER THAN JUST THE INSTANCE: Z-W5-S2 and Z-W5-S3 are both a FIELD THAT DOES NOT DESCRIBE THE WORLD (`<issued_to>` naming a slot that is not executing); this one is a FIELD WITH NO VALUE FOR THE WORLD. Both end the same way -- the artifact reads clean and the truth lives in prose a gate cannot check. THE HONEST BOUND ON THIS ROW: I hit this because I was blocked, which is rare, and I have NOT measured how often it bites. I did not census prior instances for artifacts_produced rows that should exist and do not, and I am not claiming a pattern beyond this one instance -- an omission is invisible to a census of what exists, which is the same instrument problem the project's own Z-S174 records. NOT PROPOSED: a new enum value. A value-enum proposal arrives with its four-postulate record and a word-boundary token census (Rule 24 / R-0006), this worker's order grants neither the schema nor the checker, and the seat that owns them may well prefer that a blocked artifact simply not be claimed as produced -- which is a defensible reading of `artifacts_produced` and would make this row a documentation item rather than a schema one.",
    "owner": "1.0.0_SA_CTO~Z, as the seat that holds the proof-of-spec schema and checker surface (org/standards/PROOF_OF_SPEC.schema.json + .tools/proof-of-spec-check.py). ARMED, and the hazard is a READING hazard rather than a mechanical one: nothing breaks, but a future reader of a VALID instance sees an artifact list that omits the work, and the omission is invisible in exactly the way an omission always is -- there is no row to notice missing. NOTHING IS ASKED OF THIS ORDER OR ITS ISSUER. I did not edit the schema or the checker; both are outside this order's `<paths>`, and a worker widening its order to fix a neighbouring surface is the defect this row would otherwise become.",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z, as the seat that holds the proof-of-spec schema and checker surface (org/standards/PROOF_OF_SPEC.schema.json + .tools/proof-of-spec-check.py). ARMED, and the hazard is a READING hazard rather than a mechanical one: nothing breaks, but a future reader of a VALID instance sees an artifact list that omits the work, and the omission is invisible in exactly the way an omission always is -- there is no row to notice missing. NOTHING IS ASKED OF THIS ORDER OR ITS ISSUER. I did not edit the schema or the checker; both are outside this order's `<paths>`, and a worker widening its order to fix a neighbouring surface is the defect this row would otherwise become.",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z, as the seat that holds the proof-of-spec schema and checker surface (org/standards/PROOF_OF_SPEC.schema.json + .tools/proof-of-spec-check.py). ARMED, and the hazard is a READING hazard rather than a mechanical one: nothing breaks, but a future reader of a VALID instance sees an artifact list that omits the work, and the omission is invisible in exactly the way an omission always is -- there is no row to notice missing. NOTHING IS ASKED OF THIS ORDER OR ITS ISSUER. I did not edit the schema or the checker; both are outside this order's `<paths>`, and a worker widening its order to fix a neighbouring surface is the defect this row would otherwise become.",
      "at": null
    }
  }
]
```
