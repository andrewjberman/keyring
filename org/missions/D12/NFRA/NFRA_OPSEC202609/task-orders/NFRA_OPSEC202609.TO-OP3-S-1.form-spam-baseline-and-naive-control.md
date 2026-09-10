# TO NFRA_OPSEC202609.TO-OP3-S-1 -- FWD-19: MEASURE THE FORM-SPAM BASELINE **BEFORE** ANY CONTROL IS ARMED, then put a NO-GODADDY control in COUNT and read the same window again (OP3-s-1, FWD-19)

<to_id>NFRA_OPSEC202609.TO-OP3-S-1</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.9.0_WK_NFRA_OPSEC202609~1</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged</status>

**ISSUER'S NOTE ON `S1-AC4`, ADDED BY `2.0.0_SA_COO~Z` 2026-09-10 ~12:4xZ. THE ORDER STAYS NON-TERMINAL AND THE FAIL IS THIS FACE'S DEFECT, NOT THE EXECUTION'S.**

`S1-AC4`'s expectation read: *"the response shows refusal or challenge, AND the entry does NOT appear in the entry store."* The worker graded it FAIL by output and was right to: the scripted probe returned **HTTP 200 with confirmation text byte-identical to a genuine success**, and the entry DID appear -- as **entry 22, status=spam, zero notifications**.

⛔ **TWO DEFECTS IN ONE CRITERION, BOTH THE ISSUER'S:**
1. **IT IS COMPOUND.** It conjoins a wire-level clause and a store-level clause with AND. Spine v3 L6: *"a criterion that conjoins clauses is refused at the cut."* It should have been split and was not. The L6 gate did not catch it because the v3 shape carries `<expect>` as free text and nothing parses it for conjunction.
2. **IT WAS WRITTEN AGAINST A CONTROL C-19 FORBIDS.** "The response shows refusal or challenge" is an EDGE/WAF shape -- refuse at the wire. C-19 forecloses the edge entirely (AWS WAF cannot attach to a bare EC2; both candidate edges need a GoDaddy record change). The only control available is on-box and form-level, and a honeypot **accepts and flags by design**. So the criterion demanded a behaviour the only permitted control cannot produce -- a criterion a correct build cannot satisfy, the same class as `S3-AC6` in this issuance.

⭐ **AND THE WORKER DECLINED THE WRONG FIX, CORRECTLY.** It could have forced a PASS by hardening `honeypotAction` to abort or destroy. It did not, citing **C-17**: a control that refuses a real advisor enquiry is a VIOLATION of FWD-19, not a side effect. It left `honeypotAction` at the core default `spam` -- the least-refusing mode the platform offers -- and left the criterion FAILING rather than bend the estate to the face. That is the right trade and the reason this note exists instead of a quiet re-run.

**WHAT THE EVIDENCE ACTUALLY SHOWS, for `3.0.0_SA_CVO~Z` at L9:** the scripted submission was classified **spam** and generated **zero notifications**, so it did not reach a human; the real-visitor probe (`S1-AC5`, PASS) came through as **entry 23, status=active, all 7 fields unaltered, 2 notifications fired** exactly as every legitimate entry does. Both halves of FWD-19's DONE WHEN are demonstrated on the store side; only the criterion's wire-level wording is unmet. **This face does not grade that -- `S1-AC7` is the judgment criterion and its oracle is the CVO.**

`S1-AC7` is RECORDED, not graded, and the worker bounded it against itself: before 0.217 automated/day over 36.82 days; after 0 organic over ~32 minutes, with the note that the window is **UNDERPOWERED** -- the baseline rate predicts only ~0.0048 expected arrivals in a window that short. A zero there is not evidence of an effect, and the worker said so rather than claiming one.

**Directive:** D12 · **Fabric:** site-z · **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14** (FWD-19; bounds **C-17**, **C-18**, **C-19**) · **Decomp cell:** `OP3-s-1` (round-3 rectangle v0.3.0) · **Round:** 3.

---

## THE CELL

FWD-19, ratified by Andrew at v0.14: *"Automated submissions and scraping against the marketing site are refused or challenged, and a real visitor is never stopped."*

**DONE WHEN (EXERCISED):** a scripted submission to the contact form refused or challenged **without a human acting**; a real submission by a person in a browser succeeding **unchanged in the same window**; and the volume of automated submissions reaching the entry store measured **before and after**.

**ACCEPT (Andrew's own calibration, v0.14):** the **NAIVE MAJORITY** of automated fillouts stop arriving, real advisor enquiries still arrive, and someone can say **by how much** it changed. *"Naive majority is fine for now."* ⭐ **A SOPHISTICATED BOT STILL GETTING THROUGH IS NOT A FAILURE OF THIS OUTCOME.** Do not gold-plate; do not widen.

This is the only outcome on this project that came from a user-visible complaint -- Andrew: *"We get a lot of bullshit form fillouts that are surely programmatic from bots."*

## THE ORDER OF ACTS IS THE WHOLE RISK

⛔ **THE BASELINE CENSUS IS ACT ONE AND IT ARMS NOTHING.** C-18: *"THE BEFORE-MEASUREMENT MUST BE TAKEN BEFORE ANY CONTROL IS ARMED OR IT IS UNOBTAINABLE."* If any control is armed first, FWD-19 becomes **ungradeable** and the round is wasted on it. There is no recovery -- the before-state cannot be reconstructed after the fact.

## BOUNDS -- all three from PRD 7.6, all three refusal-shaped

- **C-17 COUNT-FIRST.** The control enters **COUNT**, never BLOCK or CHALLENGE, on day one. *A control that refuses a real advisor enquiry is a **VIOLATION** of FWD-19, not a side effect of it.* The contact form asks for Firm and AUM; a silently-eaten enquiry from a prospective advisor costs more than the spam it prevents, **and it is invisible -- nobody reports the message they never knew was sent.** Violated by: any rule in BLOCK/CHALLENGE on day one; a graduation without soak evidence; a control with no measured false-positive read.
- **C-18 VOLUME-GRADED.** Graded on submission volume before/after, **never on the control's existence**. A face proving only that a rule is attached has satisfied itself and not the outcome. Violated by: arming before the baseline; grading on configuration; an after-read on a **different window or denominator** than the before-read.
- **C-19 NO-GODADDY.** The control set is bounded to what is achievable **without a DNS change at GoDaddy**. ⛔ **THE EDGE HALF IS UNBUILDABLE, NOT DEFERRED:** AWS WAF cannot attach to a bare EC2; both candidate edges (CloudFront, ALB) need the record repointed at GoDaddy; Route53 is no better because moving the zone changes the nameservers there. **SPEND NO TIME ON THE APEX, ON DNS, OR ON AN EDGE.** Measured 2026-09-09: apex and `www` both resolve to EC2 Elastic IP `18.208.18.213`; `server: LiteSpeed`, no CloudFront marker.

## GROUNDING YOU ARE GIVEN (re-ground it in phase 1; STOP and file a row on any difference)

- The origin box carries the site and its own access logs. Instance **`i-0152e3fe2599fa630`** appears in `TO-OP-S-13`'s proof instances as that surface; **an SSM document `opal-website-edge-protection` exists**. ⚠ **THIS SEAT DID NOT VERIFY SSM REACHABILITY OR THE LOG PATH** -- establishing both is phase-1 grounding, and if either is unreachable that is a `BLOCKING` row, not a reconstruction.
- The census is a **RE-RUN, NOT A NEW BUILD**: the same instrument censused **620,837 request lines** on this box over window **30/Jul-04/Sep** for `TO-OP-S-13`.
- ⛔ **A TRAP THAT ALREADY COST THIS PROJECT ONCE, on this exact log:** on WordPress a **FAILED login returns 200** (the form re-renders) and a **SUCCESS returns 302**. "200 means success" is exactly backwards here. If your discriminator uses status codes, say which way you read them.

## DELIVERABLE

1. **The BASELINE CENSUS ARTIFACT**, written before any control exists, at `../deliverables/0.9.0_WK_NFRA_OPSEC202609~1/OP3-s-1.baseline.json`. It names its **window**, its **denominator**, and its **automated/human discriminator**, over BOTH surfaces C-18 names: the **Gravity Forms entry store** and the **origin access logs**.
2. **The control, in COUNT**, chosen from what needs no GoDaddy change (form-level anti-automation on the box). State what it is and why it is inside C-19.
3. **The AFTER-READ**, same window length, same denominator definition, same discriminator, at `../deliverables/0.9.0_WK_NFRA_OPSEC202609~1/OP3-s-1.after.json`.
4. **A real-visitor check** in the same window: a submission made as a person in a browser, succeeding unchanged.
5. **The proof-of-spec instance**, VALID before the `complete` flip.

## ACCEPTANCE -- criterion ids minted at cut, ONE CLAUSE EACH

<criterion id="S1-AC1" cell_refs="OP3-s-1"><invocation>`python -c "import json;d=json.load(open('org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~1/OP3-s-1.baseline.json'));print(sorted(d.keys()))"`</invocation><expect>the printed list contains `window`, `denominator` and `discriminator`, each with a non-empty value.</expect></criterion> `S1-AC1` -- THE BASELINE EXISTS AND NAMES ITS THREE FIELDS.

<criterion id="S1-AC2" cell_refs="OP3-s-1"><invocation>`git log --diff-filter=A --format=%aI -- org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~1/OP3-s-1.baseline.json` compared against the control's own arming timestamp as recorded in the proof instance.</invocation><expect>the baseline's add-timestamp is strictly EARLIER than the arming timestamp.</expect></criterion> `S1-AC2` -- THE BASELINE PREDATES THE CONTROL.

<criterion id="S1-AC3" cell_refs="OP3-s-1"><invocation>the control's own configuration read back from the applied plane, pasted.</invocation><expect>its action/mode reads COUNT (or the platform's equivalent non-refusing mode), and no rule reads BLOCK or CHALLENGE.</expect></criterion> `S1-AC3` -- THE CONTROL IS IN COUNT, NOT BLOCK OR CHALLENGE.

<criterion id="S1-AC4" cell_refs="OP3-s-1"><invocation>the scripted submission, with its request and the observed response pasted.</invocation><expect>the response shows refusal or challenge, and the entry does NOT appear in the entry store.</expect></criterion> `S1-AC4` -- A SCRIPTED SUBMISSION IS REFUSED OR CHALLENGED WITH NO HUMAN ACTING.

<criterion id="S1-AC5" cell_refs="OP3-s-1"><invocation>the browser submission, with the entry-store record for it pasted.</invocation><expect>the entry is present and its fields are unaltered.</expect></criterion> `S1-AC5` -- A REAL SUBMISSION IN A BROWSER SUCCEEDS UNCHANGED IN THE SAME WINDOW.

<criterion id="S1-AC6" cell_refs="OP3-s-1"><invocation>`python -c "import json;a=json.load(open('.../OP3-s-1.baseline.json'));b=json.load(open('.../OP3-s-1.after.json'));print(a['denominator']==b['denominator'], a['discriminator']==b['discriminator'])"` with the paths expanded.</invocation><expect>both comparisons print `True`.</expect></criterion> `S1-AC6` -- THE AFTER-READ USES THE SAME WINDOW LENGTH, DENOMINATOR AND DISCRIMINATOR AS THE BASELINE.

<criterion id="S1-AC7" cell_refs="OP3-s-1" judgment="true"/> `S1-AC7` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9, NOT SELF-GRADED.** Whether the observed before/after change constitutes the NAIVE MAJORITY of automated fillouts no longer arriving, with real enquiries still arriving. **Record the two numbers and the delta and offer NO verdict.**

<expected_criteria>S1-AC1, S1-AC2, S1-AC3, S1-AC4, S1-AC5, S1-AC6, S1-AC7</expected_criteria>

<paths>
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP3-S-1.form-spam-baseline-and-naive-control.md
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~1/
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_OPSEC202609/prd/NFRA_OPSEC202609_PRD.md
org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3.md</decomp_doc> (v0.3.0), cell `OP3-s-1`.
<owned_cells>OP3-s-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN -- the alert/monitor moratorium (G-15) BINDS and this cell is INSIDE it only insofar as FWD-19 is a ratified outcome; **this cell builds no alarm, no notification and no monitor** -- it builds an anti-automation control on a form and measures volume. No new recipient, channel or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM identity policy is authored and no principal is created.
comp-adversary: RUN -- the issuer's grounding above is pinned to `TO-OP-S-13`'s proof instances and PRD v0.14; the assignee re-takes both in phase 1 and STOPS on any difference.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S1-AC1` .. `S1-AC7`. The worker fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~1/NFRA_OPSEC202609.TO-OP3-S-1.form-spam-baseline-and-naive-control.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S1-AC1,S1-AC2,S1-AC3,S1-AC4,S1-AC5,S1-AC6,S1-AC7"` BEFORE the `complete` flip. **`S1-AC7` IS A JUDGMENT CRITERION: record the output, never a verdict.** ⭐ **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S1-AC2`** -- if the baseline does not predate the arming, the outcome is ungradeable and nothing else in this face would show it. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any write">Confirm the worktree carries the tree this order names: `test -d org && test -d .tools`. Then re-ground the box handle, the access-log path and the Gravity Forms entry store. A surface you cannot reach is a `BLOCKING` row and a STOP, never a reconstruction.</phase>
  <phase id="2" when="first act">The baseline census. Nothing is armed until its artifact exists.</phase>
  <phase id="3" when="after the soak window">The after-read on the same window length, denominator and discriminator; then the proof instance.</phase>
</compiler_tools_mandate>

⛔ **RUN EVERY COMP-TOOL BY ITS EXPLICIT `.tools/` PATH, NEVER THE BARE NAME.** The bare name is a `~/bin` shim hardcoded to the MAIN checkout, so from your worktree it censuses the WRONG TREE and returns a confident denominator over it. A denominator near 55,000 means the bare name was used and that census is VOID (`org/modules/graph/INSTRUMENT_LIMITS.md` LIMIT 4 / 4a).
