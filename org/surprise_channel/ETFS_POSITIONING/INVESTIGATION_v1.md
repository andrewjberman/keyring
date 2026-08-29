# INVESTIGATION v1 -- ETFS_POSITIONING (round 1)

**Owner:** `3.0.0_SA_CVO` (channel) · opened 2026-08-21 on the FIRST ITEM, per the stated trigger
(the home mints on an item, never as an empty file). **APPEND-ONLY during the round.**
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` — `class {OBSERVATION, BLOCKING}` ×
`hazard_standing {ARMED, INERT}`; "latent hazard" = prose for (any class, ARMED).

⛔ **THIS IS THE LAPTOP FABRIC'S FILE. SITE Z KEEPS ITS OWN AT `INVESTIGATION_v1.Z.md` AND THE TWO
ARE NEVER MERGED.** This fabric's items are `ETFS_POSITIONING-S{n}`; site Z's are
`ETFS_POSITIONING-Z-S{n}`. **A bare `S3` in a message sent before 2026-08-21 21:08Z is read in the
SENDER's fabric** — for that hour the ids were genuinely ambiguous, and this line exists so nobody
re-litigates it. **The two files hold 14 DISTINCT findings, zero duplicated**: both certifiers
independently allocated `S1`–`S7` for entirely different hazards, because the id axis carried a
project coordinate and no fabric coordinate. Ruling `1.0.0_SA_CTO` 65860 (cross-fabric): resolve the
`ADD/ADD` by **RENAME, never by merge** — union-by-id would collapse 14 items into 7 *while looking
like it worked.*

## S2 — a control battery fabricated four results because the shell rewrote a flag into a path

**MSTR~Z self-reported it, and the report is the only reason anyone knows.** `cmd.exe /c` invoked
from Git Bash had MSYS convert the **`/c` FLAG into a path**; cmd opened an interactive shell and
returned 0; **baseline and both mutants all "passed" while the chain under test never executed.**
Their words: *"the negative control refusing to produce a 20 is the only reason I know."*
**ARMED, where it was filed INERT** — the trap exists on that box now and an ordinary act (a seat
typing the obvious `cmd.exe` invocation to check something) trips it and returns a confident green.
**The decisive argument against INERT is today's own lesson: this class is ALREADY in CLAUDE.md
with a named guard, and the harness hit it anyway. Documentation is not a disarm** — proven twice
today. **DISARM (MSTR~Z, their box):** route native invocations through the guard/shim pattern so
the trap cannot fire, rather than relying on remembering it.
*Second time today a green came from a harness that never ran the thing under test.*

## S1 — a complete landing sits in the PRODUCTION bbg prefix that cannot say whether it is production

**Filed by `1.0.0_SA_CTO` while grounding build inputs. Verified independently at this seat before
filing** (own `s3api` reads): `s3://opal-data-etfs/bbg/2026-08-20/` carries **7 objects, all
written 2026-08-21T14:22:18–19Z** — nine minutes after the L1 order was acked, and **hours before
the first SCHEDULED fire**. It is the **only** dated landing under `bbg/` (denominator: 1 of 1).
The manifest reads `as_of 2026-08-20` (correct BDay(-1)), `universe_count 109`, `objects_failed []`.

**THE MECHANISM, and it is why I am not classifying this the way it was filed: `run_class` IS
ABSENT FROM THE MANIFEST.** I enumerated its keys — `as_of, constituents, field_exceptions, funds,
generated_utc, history_window_end, history_window_start, objects_failed, objects_written,
prior_window_end, rows, universe_count`. **There is no field in which the artifact could declare
whether it was a manual QA run or a genuine first landing.** CTO named the two readings their own
order did not discriminate; the artifact cannot discriminate them either, and that is the point.

⚠ **CLASSIFIED ARMED, WHERE IT WAS FILED INERT — my act as channel owner, reasoning stated so it
can be overturned on the record rather than by preference.** The standing ad-hoc rule is that *an
ad-hoc run is never the production path and its artifacts are never production evidence.* The L3
producer cell is being designed **right now** to read `bbg/{date}/` as its production input. So if
this landing is a manual QA run written to the production prefix, **a production chain anchors on
ad-hoc evidence — and that happens through the NORMAL operation of the very cell COO is about to
cut, with everything already in place.** That is the ARMED test, met.
**IT IS NOT A CLAIM THE DATA IS WRONG** — every value I read is correct and consistent with a good
run. The hazard is provenance, not content, and provenance is exactly what the ad-hoc rule
protects.
**WHY THE ARMED CALL IS FREE HERE:** the disarm is already in flight — CTO asked MSTR~Z, via
agentbus, which run it was and to carry `run_class` in the manifest going forward. **ARMED costs
nothing when the disarm already has an owner and an act; INERT would cost the disarm obligation
attaching at all.** COO's own rule from this afternoon decided it for me: *an ARMED row filed as
INERT is the dangerous direction, because it waits for a future act that has already effectively
arrived.*
**DISARM (owner MSTR~Z, already asked):** name which run produced it, and carry `run_class` in the
manifest from here — a manifest field, not a spec change. **The durable half — that a production
artifact should be able to state its own run class — is a REMEDIATION for COO's round-1 producer
cell, not a mid-flight amendment.**

⛔ **RESOLVED 19:43:32Z — THE OWNER ANSWERED AND THE ARMED CALL WAS RIGHT.** MSTR~Z: these are
**AD-HOC STANDALONE RUNS** of `etf_daily_pull.py` from their terminal (three, ~10:17Z), **not a
scheduled fire**; the task has not fired since the ETF leg was appended (NextRun 08/22 07:00). So
reading (a). **The immediate arm is DEFUSED** — MSTR bridged it to CTO/COO before the producer cell
was cut on the premise, and CTO's *"the production input exists now"* decomp fact is **FALSE and
superseded.** **REMEDIATION STAYS OPEN and it is a different thing: the artifact still cannot
self-identify.** Seven correct-looking objects sit in the production prefix with no `run_class`, so
tomorrow's reader meets the same ambiguity without tonight's context.
*Recording one thing about the classification rule itself: I filed ARMED under uncertainty, on the
ground that the artifact could not declare its own class and a production cell was being designed
to read that prefix. The owner's answer confirmed it minutes later. **COO's "an ARMED row filed as
INERT is the dangerous direction" now has a measured instance** — filed INERT, the disarm
obligation would never have attached, and the premise was already travelling toward a cell.*

**DECOMP-RELEVANT FACT, CORRECTED — the critical path is NOT shortened:** L3 does **not** have a
production `bbg/{date}/` input today. `bbg-testpull/` remains the frozen QA reference (9 objects,
08:58Z). COO — the producer cell must state WHICH of the three prefixes it reads (scheduled landing / this ad-hoc output / the frozen QA reference) rather than inherit the ambiguity.

```json
[
 {
  "id": "ETFS_POSITIONING-S1",
  "surfaced_by": "1.0.0_SA_CTO",
  "surfaced_at": "2026-08-21T19:42Z",
  "one_line": "a complete 7-object landing sits in the PRODUCTION bbg/2026-08-20/ prefix, written hours before the first scheduled fire, and its manifest carries NO run_class field -- so the artifact cannot say whether it is a manual QA run or a genuine first landing",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "CVO independent s3api read: 7 objects under bbg/2026-08-20/, all LastModified 2026-08-21T14:22:18-19Z; the ONLY dated landing under bbg/ (denominator 1 of 1)",
    "CVO independent manifest key enumeration: run_class ABSENT -- the artifact has no field in which to declare its own run class; as_of 2026-08-20 correct, universe_count 109, objects_failed []",
    "CTO 65581: the L1 order did not discriminate manual-QA-to-production-prefix from first-genuine-landing (their own stated spec gap)",
    "standing ad-hoc rule: an ad-hoc run is never the production path and its artifacts are never production evidence",
    "RESOLVED 19:43:32Z by the disarm owner: MSTR~Z answered AD-HOC STANDALONE RUNS of etf_daily_pull.py from their terminal (three, ~10:17Z), NOT a scheduled fire; the task has not fired since the ETF leg was appended, NextRun 08/22 07:00. So reading (a) -- the ARMED classification is CONFIRMED by the owner's own answer, not merely defensible"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "notes": "CLASSIFIED ARMED WHERE FILED INERT, by the channel owner, on the record so it can be overturned by argument rather than preference. The L3 producer cell is being designed NOW to read bbg/{date}/ as production input; if this landing is ad-hoc, a production chain anchors on ad-hoc evidence through the normal operation of that cell, with everything already in place -- the ARMED test. NOT a claim the data is wrong: every value read is correct; the hazard is PROVENANCE. ARMED is free here because the disarm already has an owner and an act in flight (MSTR~Z: name the run, carry run_class forward); INERT would cost the disarm obligation attaching at all. REMEDIATION (COO round-1 producer cell, not a mid-flight amendment): a production artifact should be able to state its own run class. DECOMP FACT: L3 has a real bbg/{date}/ input today; bbg-testpull/ stays the frozen QA reference. || CONFIRMED ARMED AND PARTIALLY DISARMED, 19:44Z. The owner's answer resolves the ambiguity I filed on: these are AD-HOC artifacts sitting in the PRODUCTION prefix -- exactly the state the ad-hoc rule exists to prevent, and exactly why filing INERT would have been the dangerous direction. DISARM (immediate path) LANDED: MSTR bridged the answer to CTO/COO, killing the 'production input exists now' premise BEFORE the producer cell was cut on it -- CTO's decomp fact at 65582 is now FALSE and superseded. REMEDIATION OPEN, and it is a different thing: THE ARTIFACT ITSELF STILL CANNOT SELF-IDENTIFY. Seven correct-looking objects remain in the production prefix with no run_class, so a future reader -- including tomorrow's cell -- meets the same ambiguity with none of tonight's context. Remedy shape for COO's round-1 producer cell: carry run_class in the manifest, and rule what happens to these seven (mark, move, or declare-and-keep). bbg/{date}/ is now a THIRD thing distinct from both the scheduled landing and the frozen bbg-testpull/ QA reference; the cell should state which it reads rather than inherit the ambiguity. || TWO STATES ASSIGNED BY THE ISSUER (CTO 65640): DISARM = Amendment A1 to the L1 order (owner MSTR~Z, before 07:00 local) -- run_class in the manifest, prior-manifest resolution counts ONLY production manifests so a qa manifest can never be a continuity anchor, and the production pull script gets a REPO HOME (it is in neither repo nor S3 today). REMEDIATION = A1 landed AND the first production manifest read. Two clocks. NO S3 DELETE and nothing for Andrew tonight: the 7 ad-hoc objects STAY, marked by the ABSENCE of run_class (pre-amendment) and superseded by the first production manifest. DS's measurement changed the act -- a MOVE would have deleted the prior manifest and cold-started tomorrow's fire anyway."
 },
 {
  "id": "ETFS_POSITIONING-S2",
  "surfaced_by": "0.0.0_AB_MSTR~Z",
  "surfaced_at": "2026-08-21T19:43Z",
  "one_line": "a control battery on site Z FABRICATED four results: cmd.exe /c invoked from Git Bash had MSYS convert the /c FLAG into a path, cmd opened an interactive shell and returned 0, so baseline AND both mutants all passed while the chain under test never executed",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "MSTR~Z self-reported, via MSTR bridge 65590: first four L1-3 results fabricated; re-run clean and L1-3 genuinely closed",
    "their own words: 'the negative control refusing to produce a 20 is the only reason I know' -- the battery's PASSES were indistinguishable from real ones",
    "CLAUDE.md already carries this exact class (native-Windows parent handing argv to a POSIX-emulating child) with .tools/msys_argv_guard.py as the named remedy -- the class is documented and the harness still hit it",
    "second time today a green result was produced by a harness that never ran the thing under test (the portal tsc --noEmit false green being the first)"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "notes": "CLASSIFIED ARMED WHERE FILED INERT, consistent with the tsc precedent rather than as a reflex: the trap EXISTS NOW on that box, and a NORMAL act -- a seat typing the obvious cmd.exe invocation from Git Bash to check something -- trips it and returns a confident green. That is the same test that made the tsc false-green ARMED. THE DECISIVE POINT AGAINST INERT IS TODAY'S OWN LESSON: this class is ALREADY documented in CLAUDE.md with a named guard, and the harness hit it anyway -- documentation is not a disarm, proven twice today (COO reproduced the line-143 trap twenty minutes after reading the warning). DISARM (owner MSTR~Z, their box): route cmd/native invocations through the msys_argv_guard / shim pattern so the trap cannot fire there, rather than relying on remembering it. CONTRAST WITH S2 ON THE ADVIPOINTERS BOARD, which I filed INERT: there the bindings were correct and harm needed a FUTURE consumer wired wrong; here the trap is present and ordinary use trips it."
 },
 {
  "id": "ETFS_POSITIONING-S3",
  "surfaced_by": "0.7.0_AE_CloudOps",
  "surfaced_at": "2026-08-21T20:18Z",
  "one_line": "any terraform apply in infra/aws/terraform/shared-infra DELETES the live CloudFront read grant for platinum/advi/* and 403s the ADVI serving route that went live today, because aws_s3_bucket_policy is FULL-REPLACE and TF's desired document carries 2 statements while live carries 3",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "CVO INDEPENDENTLY CONFIRMED ON THE APPLIED PLANE, not accepted as a self-report: aws s3api get-bucket-policy on opal-data-portal-v2 returns 3 statements, third Sid=AllowAdvisorRouterOAIPlatinumAdvi scoped arn:aws:s3:::opal-data-portal-v2/platinum/advi/*",
    "TF desired state carries exactly 2 Sids (AllowCloudFrontOAI, AllowCloudFrontOACPublicData) at s3-portal-v2-import.tf -- so an apply writes a 2-statement document over a 3-statement live policy",
    "the advi Sid appears in ZERO code: comp-find -i returns 6 hits, ALL band=DOC (a ledger, AE's own message, the amended TO). No terraform resource manages it",
    "NEGATIVE CONTROL run: the same probe against opal-data-assets does not contain the Sid, so the instrument discriminates rather than matching anything",
    "AE's plan -target on the resource returned 'Plan: 0 to add, 1 to change, 0 to destroy' where the change is the statement REMOVAL",
    "corroborates COO's S-COO-4 independently: AllowCloudFrontOACPublicData is prefix-scoped to json/*, json-tiered/*, platinum/mdpf/* -- confirming a new platinum prefix is NOT CloudFront-readable",
    "REMEDIATION VERIFIED AT CVO'S SEAT 20:56Z, THREE LIMBS, none accepted as a self-report. (1) LIVE PLANE: get-bucket-policy returns 3 statements; AllowAdvisorRouterOAIPlatinumAdvi PRESENT and still scoped platinum/advi/*; AllowCloudFrontOACPublicData went 3 -> 4 resources, the added one being platinum/etfs/*. The apply that would have deleted the advi grant instead preserved it and added an ARN. (2) SOURCE PLANE: s3-portal-v2-import.tf now declares AllowAdvisorRouterOAIPlatinumAdvi at :176 and platinum/etfs/* at :137 -- DESIRED == LIVE, the out-of-band drift closed at its origin rather than papered over. (3) I INDEPENDENTLY VERIFIED AE'S *REFUSAL*, which is the rarer act: they declined to claim AC7 off an unauthenticated fetch on the ground that it 401s at the edge before the origin is touched and is therefore byte-identical whether the grant is intact or deleted. MEASURED MYSELF: the KNOWN-WORKING Models route and the ETF route BOTH return 401 unauthenticated -- the probe genuinely cannot distinguish a healthy /api/general/* route from a broken one. AE'S REFUSAL WAS CORRECT AND THEIR REASONING HOLDS UNDER TEST.",
    "⛔ CVO SELF-FILED AGAINST OWN SECOND, 21:00Z: WHEN I SECONDED THE FABRIC-WIDE FREEZE LIFT AT 20:56Z, THE FIX WAS LOCAL AND I DID NOT CHECK. My 'SOURCE PLANE' limb read the WORKING TREE copy of s3-portal-v2-import.tf. The remote still carried the hazardous two-statement document -- MSTR measured `git show origin/CLOUD:...| grep -c AllowAdvisorRouterOAIPlatinumAdvi` -> 0. So any seat cloning or pulling origin would have received the drifted TF AND a fabric-wide message saying the freeze was lifted, which is strictly worse than the freeze because the freeze was at least true. MSTR pushed and closed it BEFORE relaying, so no seat was ever exposed. NOW VERIFIED AT MY SEAT ON THE REMOTE: origin/CLOUD = 435d6d5aa6, 537b250716 contained, advi Sid on the remote copy = 1 (pre-push tip fd7a8732b9 = 0, so the probe discriminates and is not matching on anything)."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "CONFIRMED, and the mechanism is the sharpest instance of the wrong-plane class the estate has produced. The P4R-3 close was CAREFUL -- live policy read back, all 3 statements confirmed, router controls mutation-tested, an EXERCISED fetch, deployed bytes hashed -- and it recorded a re-plan reading 'No changes'. THAT RE-PLAN WAS IN THE WRONG TERRAFORM ROOT (portal-auth, which owns the lambdas and distribution and does NOT own the bucket policy). EVERY CONTROL FIRED CORRECTLY AND EVERY ONE WAS ABOUT THE WRONG PLANE. A grant applied out-of-band is invisible to a plan you never run: verifying on the live primitive is sound for 'is it granted' and STRUCTURALLY SILENT on 'does code still describe reality'. AE surfaced it against their own prior session's close, named themselves disarm owner, applied nothing, and refused to write the restoring edit on their own authority. DISARM (effective now, needs nobody): no seat applies shared-infra until the TF carries the advi statement -- fabric-wide, not ETFS-only. REMEDIATION (different act, different clock): codify the statement so desired==live in the SAME edit that adds the etfs ARN, one safe-apply, re-plan IN shared-infra to 0-diff. COO has RULED (A): TO-2 Half 2 now carries the restore, so it is on-spec and not a mid-flight amendment. || REMEDIATION 20:56Z: DISARMED AND REMEDIATED ON THE POLICY PLANE, verified three ways above. AC7 IS PARTIALLY DISCHARGED AND I AM NOT ROUNDING IT UP, matching AE's own framing: the authenticated ADVI GET through the auth path was NOT run, because the P4R-3 close scrubbed the key material and short-TTL tokens BY DESIGN and no minting method exists in-session. THE OPEN HALF IS NARROW AND I WILL STATE ITS SHAPE RATHER THAN ITS SIZE: the grant is verified present and byte-identical by direct policy read, and the auth path was not touched by this apply -- so the residual is that no single act has exercised grant+auth together end to end. WHAT MAKES THIS EXEMPLARY RATHER THAN A GAP: AE MEASURED THE CHEAP SUBSTITUTE, FOUND IT UNDISCRIMINATING, AND REJECTED IT INSTEAD OF BANKING IT. That is the wrong-plane class caught by its own author before it reached a certifier -- the first time tonight that happened without an external catch. || ⛔ THE DURABLE CLASS, MSTR'S AND IT IS NEW: THE REMEDIATION OF A FABRIC-WIDE HAZARD IS NOT FABRIC-WIDE UNTIL IT IS PUSHED -- a local fix plus a fabric-wide all-clear is strictly MORE dangerous than no all-clear. It generalises S4 one layer down and points at a hazard FENCE rather than a spec. NOBODY ACTED WRONGLY: AE cannot push (integrator gate) and said plainly the commit rides the next window; CTO and COO verified the remediation itself correctly. THE GAP IS STRUCTURAL -- under lanes-commit/integrators-push a disarm owner can COMPLETE a remediation and still be unable to make it real for anyone else, and THE LIFT MESSAGE TRAVELS FASTER THAN THE FIX. MY OWN PART, NAMED: I seconded the lift on a working-tree read, having spent the same evening authoring S4's ordering refinement about exactly this. THE PATTERN AT MY SEAT, THIRD INSTANCE TONIGHT: I VERIFY THE PLANE IN FRONT OF ME. The cert used an unexercised local join; this used a local file; both times the REMOTE was the question. Caught by MSTR, as the cert was caught by Andrew."
 },
 {
  "id": "ETFS_POSITIONING-S4",
  "surfaced_by": "2.0.0_SA_COO",
  "surfaced_at": "2026-08-21T20:11Z",
  "one_line": "COO's Amendment A+B commit sits on ZERO remote branches while the decomp and the three TOs are on origin/CLOUD, so a fresh seat pulling TO-1 from the remote reads the superseded single-stage producer shape and would build it correctly against a stale spec with nothing to tell them",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "COO measured with git branch -r --contains: cc7eca2da3 on zero remote branches; 308fcaea0d and 10f94e4f13 on origin/CLOUD",
    "Andrew closed the prior DS/DE seats for context health, so the seats that pick these up are FRESH and pull from origin",
    "third instance today of the same mechanism: a correct artifact committed locally while the seat needing it reads the remote",
    "REFINED 20:34Z by CVO (channel owner) after CTO 65756: the ARM is NARROWER than I filed it and the residual is an ORDERING one. CTO's closing fact -- only MSTR spawns seats, MSTR is dark, therefore NO fresh seat can appear to pull a stale TO, and the three live seats (DS/DE/AE) confirmed current content FROM DISK. So the hazard cannot fire while MSTR is away. BUT IT IS NOT UNCONDITIONALLY DEFUSED: MSTR's return re-enables BOTH the push (the disarm) and spawning (the trigger), and the binding need on return is DT for the promote leg. IF MSTR RETURNS AND SPAWNS DT BEFORE PUSHING, THE HAZARD FIRES IN EXACTLY THE WINDOW EVERYONE BELIEVES IT CLOSED -- a fresh seat pulling origin/CLOUD @53ed8605, which does not carry any of the 12 enumerated local commits including Amendment C and the rewritten s.6. SO THE DISARM CARRIES AN ORDER, NOT JUST AN ACT: PUSH FIRST, SPAWN SECOND. That ordering belongs in the reseat ask itself, because the moment of highest spawn pressure is the moment of return.",
    "DISARM VERIFIED AT CVO'S SEAT 20:43Z, NOT ACCEPTED AS A SELF-REPORT -- both limbs. PUSH: git fetch then per-commit containment; origin/CLOUD advanced 53ed8605 -> fd7a8732b9 and every sampled commit is contained (f7c719b56d s.6 rewrite, 6299ec7098 Amendment C, 8c7212ccf4 law widening, 59f2c95115 CVO cert, a5c3a2f282 CVO channel). My own S4 refinement fd7a8732b9 IS the remote tip. ORDERING -- the limb this row exists for, and the one a self-report cannot establish: read from org/mcp/agent-spawn-audit.log, NOT from MSTR's account of their own acts. MSTR's current session registers at 20:38:16.089Z (IDENTITY_GUARD_ACTIVE pid=22984, matching the PID they reported); the last SPAWN lines are 20:07:16Z (DS) and 20:07:36Z (DE), both from the PRIOR MSTR session before going dark; ZERO SPAWN entries after 20:38:16Z. PUSH BEFORE SPAWN HELD, MEASURED."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.0.0_AB_MSTR",
  "notes": "Routed same-turn by COO before I saw it. DISARM = the integrator push. REMEDIATION is a different state with a different clock: the fresh seat's spec-at-pickup actually reading the amended TO. The spawn brief is the only live delivery surface during the push window, which is why COO sent the three load-bearing lines for it -- the brief is load-bearing, not redundant. ORDERING REFINEMENT (CVO, 20:34Z): the disarm is not merely 'the push' but 'the push BEFORE the first spawn'. MSTR's return simultaneously restores the disarm capability and the trigger capability, and the reason MSTR is being reseated is to spawn DT -- so the natural first act on return is the one that arms this. Stated on the row rather than routed as a new escalation: CTO and COO have the reseat ask with Andrew and a third route would be noise, but an unstated ordering constraint is how a closed hazard reopens at the handoff. || CLOSED-HALF 20:43Z: DISARM CONFIRMED and the ORDERING RESIDUAL IS DISCHARGED -- verified on the remote and on the spawn-audit log rather than on MSTR's report, because the ordering claim is precisely the class where a seat's account of its own acts is the weakest available evidence. REMEDIATION REMAINS OPEN and the row does NOT close: remediation is a fresh seat's spec-at-pickup actually reading the amended TO, and no fresh seat has been spawned yet -- the two states have two clocks and only one has run. MSTR is carrying COO's three load-bearing lines in the spawn brief anyway, correctly noting the brief is now the REDUNDANT surface rather than the load-bearing one; a brief costs nothing and a stale pickup costs a rebuild."
 },
 {
  "id": "ETFS_POSITIONING-S5",
  "surfaced_by": "0.7.0_AE_CloudOps",
  "surfaced_at": "2026-08-21T20:11Z",
  "one_line": "mdpf_egress_publisher.tf:46-48 records a 2026-07-28 measurement of 2 statements scoped to CloudFront; live is 3 and OAC-scoped to exactly json/*, json-tiered/*, platinum/mdpf/*, so the header is 24 days stale on count and scope",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "AE measured live; CVO's independent policy read above reproduces the three prefixes exactly",
    "the zero-Denys half of the comment is still true, which is what makes the stale half credible"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "ARMED on COO's reasoning, which is a sharper standard than 'the comment is wrong' and I am adopting it: a seat inheriting that header concludes a new platinum prefix is CloudFront-readable -- IT IS NOT -- and the failure it produces is a MASKED HTML 403, because CF error rules dress JSON errors as HTML. So it does not merely mislead, it AIMS THE NEXT SEAT AT THE WRONG LAYER (routing bug rather than policy gap). Disarm is a comment correction, no apply."
 },
 {
  "id": "ETFS_POSITIONING-S6",
  "surfaced_by": "0.7.0_AE_CloudOps",
  "surfaced_at": "2026-08-21T20:25Z",
  "one_line": "public_data_router pins qualified_arn in ignore_changes, so applying the /api/general/etfs/ branch would publish a NEW edge version while CloudFront kept serving the OLD one -- the ETF URL 404s into the json/ fallback silently, with every rung of Rule 22a passing; and comp-routes edge-versions reports the pinned function as DYNAMIC [OK]",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "CVO source census reproduces AE exactly: ignore_changes = [qualified_arn, source_code_hash] at lambda-edge.tf:96 (auth_validator_edge), :151 (cache_control_injector), :197 (public_data_router) -- exactly THREE pinned; :244 and :294 carry source_code_hash only",
    "CVO RAN THE TOOL: comp-routes edge-versions prints 'DYNAMIC (5) -- these auto-update on terraform apply' and marks all five [OK], INCLUDING the three pinned ones. The misreport is live, not merely documented",
    "the tool reads the locals-block REFERENCE and cannot see the ignore_changes that defeats it (lambda-edge.tf:46)",
    "the file's own header at :36-37: 'Apply publishes a NEW Lambda version and CloudFront KEEPS SERVING THE OLD ONE'",
    "SHARPEST LIMB, CVO-measured: comp-routes' own coverage disclosure says it is DESIRED-plane and 'a pinned stale Lambda@Edge version reads identical here (see edge-versions for the pinning axis)' -- IT CROSS-REFERENCES THE READER TO THE ONE INSTRUMENT THAT GETS THIS WRONG",
    "DISARM+REMEDIATION VERIFIED AT CVO'S SEAT 21:20Z on the LIVE distribution -- the instrument lambda-edge.tf:42-43 calls 'the ONLY one that catches it'. EVTSA9VEHNZVH: public-data-router v7 on BOTH /api/general/* and /api/general/json-tiered/* origin-request. THE VERSION ADVANCED, which is exactly what the qualified_arn pin would have prevented. AE also proved the fix effective BEFORE the apply: the plan showed the distribution updating in-place with -/+ lambda_function_association pairs, and WITH THE PIN IN PLACE THAT RESOURCE PLANS AS NO-OP -- so the plan itself discriminated fixed from broken. MY FIRST QUERY WAS WRONG AND I CAUGHT IT BEFORE REPORTING: I read LambdaFunctionAssociations.Items[0] and got auth-validator-edge v18, a DIFFERENT function -- each behavior carries three associations by event type. Reporting that would have been a FALSE REFUTATION of a true claim. Fourth instance tonight of an instrument answering a question I did not ask, cleanly; the first one caught before it left my seat."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "AE's SECOND self-correction tonight, against a sentence they had already put in the contract, a commit message and two sends. It is false in the direction that ships a silently non-working route. THE PART THAT GENERALISES: the warning about this exact tool blind spot was written TODAY, by AE'S OWN LANE, in the very file they were editing -- and they used the instrument it warns against. Same shape as MSTR~Z's fabricated battery and my own masked-exit-code repeats: DOCUMENTATION IS NOT A DISARM, third measured instance today, and this one had the doc in the same file as the hazard. The 22a rungs all PASS here -- clean plan, genuine 0-diff re-plan, a version really published, route green on the OLD code -- so a 0-diff re-plan is the SYMPTOM, not the reassurance. DISARM = drop qualified_arn from ignore_changes at :197 IN THE SAME COMMIT as the branch edit (the remedy the file prescribes at :54-58, exercised already on shared_advisor_router @1fb2ad4abb). REMEDIATION = after apply, read the LIVE distribution's association ARN -- per :42-43 the only instrument that catches it. Mint is THREE edits, not two. AE is NOT bundling the other two pins, correctly, per :52. DS/DE unaffected: route decision, key, URL, shape and vocabulary all unchanged -- this is HOW THE MINT LANDS, not what is built. || S6 CLOSED 21:20Z: disarm (ignore_changes drop in the same commit) AND remediation (live association read after apply) both discharged, both verified here."
 },
 {
  "id": "ETFS_POSITIONING-S7",
  "surfaced_by": "0.0.0_AB_MSTR~Z",
  "surfaced_at": "2026-08-21T20:18Z",
  "one_line": "DIVZ and IDVZ have no constituent holdings anywhere in opal-data-etfs -- the declared universe is four funds and holdings exist for two (PFDE, PFOE) -- raised as a spec question about what the deliverable can CONTAIN",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "CVO SPOT-VERIFIED THE ABSENCE INDEPENDENTLY before reading CTO's call: silver/holdings/2026-08-20.parquet, 114 rows, fund_ticker = ['PFDE','PFOE'] only; POSITIVE CONTROL PFDE present, so the read discriminates",
    "CVO VERIFIED THE SECOND LIMB TOO -- that the SPEC ALREADY SAYS THIS: ETFS_POSITIONING_PRD.md:697-698 'TWO FULL BOOKS (PFDE/PFOE, constituent holdings) + TWO BOOK-LEVEL SHELLS (DIVZ/IDVZ ... no constituent rows), shells upgrading forward automatically'; :740 attributes the ship shape to Andrew (s.10.4); :761 'the page-ship cell does not wait on DIVZ/IDVZ rows'",
    "CTO's citation chain, deeper than mine: s.1 headline + two independent causes (the deployed TrueShares holdings arm is a NO-OP, source-confirmed on the deployed package; and the structural trust boundary -- filepoint administers PFDE/PFOE only, DIVZ/IDVZ sit on TrueShares/Polen)",
    "s.3.3 Andrew-ordered snapshot: 3 trees / 1,111 objects / 7,550 holding rows ALL-TIME, never a DIVZ or IDVZ constituent row; positive control PFDE = 5,920",
    "MSTR~Z's three traps are correct and already carried in s.10.1-10.3: a COUNT IS NOT A LIST (TOTAL_NUMBER_OF_HOLDINGS_IN_PORT returns DIVZ=30/IDVZ=46 and will not enumerate -- reads exactly like partial coverage and is not); ZERO NOT_AUTHORIZED so it is provably not an entitlement gap and cannot be bought out of; and the 73.4% dividend-yield field is 29 genuine non-dividend-payers, not a 27% hole"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "NOT A SURPRISE -- it is the PRD's own headline finding, measured three ways before stage 1, and the ship shape it implies is Andrew's own scope call. The spec already states what the deliverable CONTAINS. Nothing re-opens; no TO amendment. The 'unwired vs nonexistent' cell the reporter deliberately left open is also answered at source: NONEXISTENT via filepoint (trust boundary), while the TrueShares arm is the UNWIRED one whose wiring is the L2 design -- and L2 is the single cell gated on Andrew's egress word.",
  "disarm_owner": "n/a -- INERT, no disarm obligation attaches",
  "notes": "FILED AT CTO'S EXPLICIT REQUEST SO THE RECORD SHOWS THE QUESTION ARRIVED AND WAS ALREADY ANSWERED, RATHER THAN THAT IT WAS NEVER ASKED. That distinction is the whole value of the row: a future reader who re-derives this absence from the data -- and they will, because a 4-fund universe with 2-fund holdings looks exactly like a defect -- needs to find it already adjudicated with citations, not discover it fresh and re-escalate. MSTR~Z routed it correctly under Rule 27 (a spec question goes to the issuer, not the executing seat), stated its bounds properly with denominators and an enumerated tree, and explicitly declined to guess on the open cell. NONE OF THAT IS WASTED BY THE DISMISSAL -- an independent re-derivation of a PRD premise from the data side is corroboration, and the GICS tie-out that rode along (105/109, 4 gaps = the 4 fund rows, weighted rollup matching s.3.1 by an independent route) is a genuinely NEW input for TO-1's vocabulary act."
 },
 {
  "id": "ETFS_POSITIONING-S8",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T21:04Z",
  "one_line": "the comp-find census for the model-list membership fact is QUOTE-DELIMITED and structurally cannot match the same fact written as a bare object key, a fixed-length array, or a repeat(N) count -- true denominator 12, not 5",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE measured: six further in-plane sites plus one silent-drop filter were invisible to the quoted pattern",
    "DISARMED SAME TURN by DE: all 12 now derive from ONE declaration and the true denominator is printed in the AC1 row",
    "the original five were RIGHT -- the pattern's DOMAIN was too narrow, not its matches wrong"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DE_ClientPlatform",
  "notes": "DISARMED SAME TURN BY ITS OWN FINDER, and filed ARMED rather than INERT because DE is explicit that DISARMED IS NOT REMEDIATED: the pattern will read CLEAN on the next census while saying nothing about the three forms it cannot see. THIS IS CLAUDE.md RULE 21's UNDERCOUNT SHAPE, WHICH THE LAW ITSELF NAMES AS THE DANGEROUS HALF -- a zero invites suspicion, a plausible non-zero does not. 5 of 12 is exactly the plausible non-zero."
 },
 {
  "id": "ETFS_POSITIONING-S9",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T21:04Z",
  "one_line": "the LIVE Models artifact is served GZIPPED (ContentEncoding gzip, magic 1f8b, 8,111 B compressed / 73,522 B raw) while the ETF artifact CONTRACT states no Content-Encoding -- a producer MIRRORING the Models producer would naturally gzip, and gzip bytes without the header reach the browser as binary and fail JSON.parse",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE measured via s3api head-object on the live Models artifact",
    "plain JSON is a valid choice; the hazard is the MISMATCH between the template a producer would copy and the contract it must meet",
    "DS is the seat that would trip it and the Models producer is the obvious template"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "ROUTED, NOT CHASED -- DE flagged it to the contract owner rather than editing the contract or warning DS directly, which is correct conduct under a frozen spec. ONE LINE IN THE CONTRACT CLOSES IT. The hazard is precisely that the WRONG choice is the one a CAREFUL seat makes by following the best available example."
 },
 {
  "id": "ETFS_POSITIONING-S10",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T21:04Z",
  "one_line": "decomp ETFS-f-5 says 'the SIX DEF-band sites OUTSIDE the plane' and then ENUMERATES SEVEN",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE's live census agrees with the LIST, not the numeral: DEF=11 = 4 in-plane + 7 out-of-plane",
    "one component contributes two sites (:130 and :212), which is where the numeral slipped",
    "the LIST is what binds AC6 and the list is correct"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "n/a -- INERT, no disarm obligation attaches",
  "notes": "INERT and correctly so: the criterion is 'untouched', DE touched none, and nothing downstream reads the numeral to act on. DE's forward-looking note is why it is filed at all -- A ROUND-2 CLEANUP KEYED ON 'six' WOULD LEAVE ONE BEHIND. A wrong count beside a right list is harmless until someone trusts the count instead of reading the list."
 },
 {
  "id": "ETFS_POSITIONING-S11",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T21:04Z",
  "one_line": "the portal's ETF category constants are an input to the sub_asset_class vocabulary act and already contain all four fund tickers -- but as HOLDINGS INSIDE MODEL BOOKS, not as books; and the file's segment vocabulary is duration buckets",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE read it in-plane while executing TO-3",
    "the four tickers appearing in a role easy to conflate with the book role is the specific hazard",
    "the duration-bucket vocabulary IS the model vocabulary AE warned DS not to reuse for an ETF book of single securities"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "n/a -- INERT, no disarm obligation attaches",
  "notes": "Reported per COO's instruction and explicitly NOT coordinated by DE -- correct mid-round conduct. Filed because it is CONCRETE IN-PLANE CONFIRMATION of AE's two-grains warning rather than a new claim, and a confirmation reached independently on a second plane by a second seat is worth more than the original warning restated."
 },
 {
  "id": "ETFS_POSITIONING-S12",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T21:04Z",
  "one_line": "the holdings aggregate weighting treats a book with no AUM as zero in BOTH numerator and denominator, so the survivors still sum to exactly 1.0 -- an 'Aggregate' computed over a SUBSET is indistinguishable on screen from one computed over the whole set",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE measured it in-plane during TO-3; PRE-EXISTING, not introduced by this round",
    "no error, no empty state, no zero row -- a PLAUSIBLE WRONG NUMBER on a client-facing page",
    "DE left the behaviour UNCHANGED under the frozen spec, collapsed two verbatim copies into one helper, documented it at the site, and added a field exposing which books were dropped"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "UNASSIGNED -- routed to 2.0.0_SA_COO (TO issuer) same-turn for assignment; see notes",
  "notes": "THE SHARPEST ITEM IN DE'S SET AND THE ONE I WOULD PUT IN FRONT OF A HUMAN: it is CLIENT-FACING and it FAILS SILENTLY IN THE PLAUSIBLE DIRECTION. Renormalising over survivors means the number ALWAYS LOOKS RIGHT -- no missing row, no NaN, no empty state, nothing on screen that differs between an aggregate over all books and one over a subset. ARMED WITH NO DISARM OWNER, WHICH THIS SCHEMA REQUIRES: DE correctly declined to take remediation unilaterally under a frozen spec, so the ownership question is genuinely open and I am NOT assigning it myself -- routed to COO as TO issuer. WHAT DE DID DO IS THE RIGHT HALF: made the hazard VISIBLE without changing behaviour, converting an invisible failure into a detectable one with no off-spec write. DISARMED WOULD NOT EQUAL REMEDIATED HERE EITHER."
 },
 {
  "id": "ETFS_POSITIONING-S13",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T21:04Z",
  "one_line": "two pre-existing records: stray untracked directories in the portal tree, and a portal type declaring a returns period set that does not match the one the live artifact actually carries",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "(a) is the lingering-portal-CWD artifact TO-3's own placement note warns about -- not DE's, not touched, not committed",
    "(b) is pre-existing type-vs-live drift on the MODELS path, unrelated to this TO, untouched"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "n/a -- INERT, no disarm obligation attaches",
  "notes": "Filed as RECORDS rather than findings. (b) is the two-homes-diverged shape one layer up -- A TYPE AND A LIVE ARTIFACT DISAGREEING, WHERE THE TYPE READS AUTHORITATIVE AND IS STALE. Inert here because nothing in this round reads it, but it is exactly the class Rule 22a warns produces a clean verdict on the wrong plane."
 },
 {
  "id": "ETFS_POSITIONING-S14",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C (msg 66519); escalated by 3.0.0_SA_CVO 20:50Z as STRANDED/NEVER#6 -- CHARACTERISATION CORRECTED BY 0.0.0_AB_MSTR (66550) and accepted at this seat; the timing half and the ARMED standing CONFIRMED by them",
  "surfaced_at": "2026-08-24T20:42Z",
  "one_line": "A portal DEV->PROD promote merge (a239e4a9, v2.1.165) is PARKED AT THE LAST REVERSIBLE MOMENT and formally HELD-PENDING-SOVEREIGN in an on-origin deploy-completion ledger -- NOT stranded, NOT a NEVER#6 breach, DT left no mess. What IS new: the merge was parked ~13:0xZ against one question and Andrew's ~15:2xZ two-condition hold now governs its content, so its meaning changed after parking; and /prod-deploy Step 2 will SILENTLY DISCARD it on the next promote.",
  "class": "OBSERVATION",
  "hazard_standing": "DISARMED -- FALSIFIED BY EVENTS 2026-08-29T15:2xZ. THE DISARM ACT AS WRITTEN IS NOW IMPOSSIBLE TO PERFORM, not merely unnecessary: the owner row reads 'the disarm is MAKING THE CHOICE VISIBLE before the next promote runs', and THE NEXT PROMOTE RAN -- 0.0.0_AB_MSTR merged DEV->PROD v2.1.173 at 2026-08-29T06:00:59Z under Andrew's three panel edits -- so there is no longer a choice to make visible. TRUE WHEN WRITTEN 2026-08-24; overtaken by the world. Same class as D1_CATVIEWS-S8. || TWO INSTRUMENTS, AND THE FIRST COULD NOT ANSWER IT. ANCESTRY (2.0.0_SA_COO~Z): origin/PROD moved 8a96c916 -> fc3a4421, origin/DEV d43b88c5 -> 0e1c232d, merge-base --is-ancestor a239e4a9 PROD = FALSE. THAT ESTABLISHES ONLY THAT THE COMMIT IS ABSENT, NOT THAT THE WORK IS -- and CLAUDE.md Rule 22a says so in terms: a cherry-picked pin is resolved by CONTENT, NEVER by merge-base --is-ancestor. The ancestry instrument was the AVAILABLE one, not the PRESCRIBED one. CONTENT (3.0.0_SA_CVO~Z), 4 of the merge's 12 files by blob id at both refs: adviKeyRepoint.ts 0ae44992 IDENTICAL; etfAdapter.ts 7940a205->0867bd1d, bookSet.ts 94c96881->bb163b94, HoldingsTab.tsx 58c727cf->cd8f6020 DIFFER but are PRESENT. etfAdapter.ts and bookSet.ts were CREATED by that merge, so their existence at PROD tip is what proves the work reached PROD. NEGATIVE CONTROL package.json c17dea29 IDENTICAL at both refs, proving the instrument CAN report identity, so the DIFFERS are real differences and not an artifact. || THE ANSWER IS RE-MERGE, NOT ABANDONMENT: a239e4a9 is not an ancestor AND its content is in PROD -- both true, and only a content read separates them. || BOUNDS CARRIED, NOT DROPPED: 4 of 12 files compared, chosen as the two the merge CREATED plus two it heavily edited; THE OTHER 8 WERE NOT COMPARED. 'The work reached PROD' is ESTABLISHED; 'every TO-3 change is present in its v2.1.165 form' is NOT -- three of four evolved afterwards and nobody diffed what changed. A stronger claim needs a different measurement. || NOT A SOVEREIGN RULING: the push/park/roll-back call was placed above the CVO seat and likely Andrew's. IT IS NOT BEING TAKEN HERE -- IT WAS OVERTAKEN, and this records that rather than deciding it. Disarmed by 2.0.0_SA_COO~Z under D4 scope on 3.0.0_SA_CVO~Z's content measurement; 3.0.0_SA_CVO~Z explicitly declined to disarm, holding that supplying the MEASUREMENT is not taking the CALL. DISARMED != REMEDIATED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git -C portal ls-remote origin (REMOTE, not a local ref): refs/heads/PROD = 8a96c91654ed, refs/heads/DEV = d43b88c5124c",
    "local PROD = a239e4a9, a DEV->PROD merge commit 'merge DEV->PROD: v2.1.165 -- ETFS_POSITIONING TO-3 ... + OPAL_ADVIPOINTERS P4-REPOINT-49F', authored 2026-08-24T08:50:03-04:00 by Andrew Berman",
    "git -C portal branch -r --contains a239e4a9 -> EMPTY: the merge is on no remote branch, so CI never ran and PROD was never deployed",
    "local PROD is 14 ahead / 0 behind origin/PROD; local DEV == remote DEV (DEV is fine, only PROD is stranded)",
    "the ephemeral worktree .runtmp/portal-promote-20260824T124621Z is STILL REGISTERED at PROD a239e4a9 (workspace root .runtmp/, not portal/.runtmp/ -- correcting the surfacing seat's path); at least four promote worktrees from 08-04, 08-07 and today remain registered",
    "the timing: the merge (12:50Z) PREDATES Andrew's ~15:2xZ ruling that the ETF page promote is NOT YET on two conditions (CTO 66217, record @de481d0e06)",
    "⛔ CORRECTION, the evidence I never looked for: org/critical_paths/change_management/20260824T1241Z_etfs-positioning-prod-promote-v2-1-165_deploy_completion.md is ON origin/CLOUD (git cat-file -e verified at my seat, 156 lines, positive-controlled) and says verbatim 'STATE AS OF 2026-08-24T13:0xZ -- HELD-PENDING-SOVEREIGN', 'NOT COMPLETED. NOT ABORTED. NEITHER TERMINAL IS TRUE OF THIS ENTRY', with prod-push/ci/tag/pointer all HELD-PENDING-SOVEREIGN; COO adjudicated it KNOWN-HELD out of band because the tool REFUSED the state",
    "NEVER#6 does NOT bite: it binds a BEGUN deploy, and no production write occurred -- origin/PROD is still 8a96c916 and the merge is on zero remote branches. Parked at the last reversible moment is where DT deliberately put it"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "DT (portal promote lane) -- the disarm is making the CHOICE VISIBLE before the next promote runs, not performing it; the ruling on push / park / roll back is above the CVO seat and likely Andrew's, since his hold is what changed the merge's meaning",
  "notes": "⛔ MY CHARACTERISATION WAS WRONG AND THE CLASS IS MINE: every measurement I took reproduces at MSTR's seat, and I called a DISCLOSED, ADJUDICATED HOLD a stranded deploy and red-alert material. I verified the REPO plane exhaustively (ls-remote, branch -r --contains, worktree list, commit authorship) and never read the GOVERNANCE plane -- the deploy-completion ledger that NEVER#6 ITSELF NAMES as the mechanism. I cited the rule and did not look where the rule says the answer lives. Second wrong-plane instance at this seat today, and the first one (OPAL_KIMIPIPELINE-S1) was me correcting someone ELSE for exactly this shape. I came online 19:2xZ; DT closed ~13:5xZ; I was missing their disposition, not misreading the repo -- and 'I did not see it' is not a plane. WHAT SURVIVES, CONFIRMED BY MSTR AND NOT RETRACTED (post-catch maximal retraction destroys true findings): (1) THE TIMING FINDING IS NEW AND REAL -- the artifact was parked against one question and is now governed by Andrew's later two-condition hold it predates; the ledger's gate-ref still names the old question. MSTR is carrying that to Andrew. (2) THE ARMED STANDING IS RIGHT: /prod-deploy Step 2 re-asserts local PROD from origin, so the next promote silently discards a239e4a9 by default. DT disclosed it in the ledger, but A DISCLOSURE IS NOT A CONTROL -- it requires the next promoter to read it, and the failure mode is a seat running the sanctioned skill CORRECTLY and destroying a held artifact as a side effect. MSTR adopted my framing that the disarm is making the choice VISIBLE before the next promote runs, not performing it. DISPOSITION: push=NO (promotes content under a live conditional hold), discard=NO (destroys a merge nobody decided to lose); the live question is PARKED-UNTIL-STALE vs ROLLED BACK NOW, and it is Andrew's or CTO's. DT is closed; this is the first item for the next DT lane, with the ledger as its input."
 }
]
```
