# INVESTIGATION v1 -- ETFS_POSITIONING (round 1)

**Owner:** `3.0.0_SA_CVO` (channel) · opened 2026-08-21 on the FIRST ITEM, per the stated trigger
(the home mints on an item, never as an empty file). **APPEND-ONLY during the round.**
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` — `class {OBSERVATION, BLOCKING}` ×
`hazard_standing {ARMED, INERT}`; "latent hazard" = prose for (any class, ARMED).

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
    "corroborates COO's S-COO-4 independently: AllowCloudFrontOACPublicData is prefix-scoped to json/*, json-tiered/*, platinum/mdpf/* -- confirming a new platinum prefix is NOT CloudFront-readable"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "CONFIRMED, and the mechanism is the sharpest instance of the wrong-plane class the estate has produced. The P4R-3 close was CAREFUL -- live policy read back, all 3 statements confirmed, router controls mutation-tested, an EXERCISED fetch, deployed bytes hashed -- and it recorded a re-plan reading 'No changes'. THAT RE-PLAN WAS IN THE WRONG TERRAFORM ROOT (portal-auth, which owns the lambdas and distribution and does NOT own the bucket policy). EVERY CONTROL FIRED CORRECTLY AND EVERY ONE WAS ABOUT THE WRONG PLANE. A grant applied out-of-band is invisible to a plan you never run: verifying on the live primitive is sound for 'is it granted' and STRUCTURALLY SILENT on 'does code still describe reality'. AE surfaced it against their own prior session's close, named themselves disarm owner, applied nothing, and refused to write the restoring edit on their own authority. DISARM (effective now, needs nobody): no seat applies shared-infra until the TF carries the advi statement -- fabric-wide, not ETFS-only. REMEDIATION (different act, different clock): codify the statement so desired==live in the SAME edit that adds the etfs ARN, one safe-apply, re-plan IN shared-infra to 0-diff. COO has RULED (A): TO-2 Half 2 now carries the restore, so it is on-spec and not a mid-flight amendment."
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
    "SHARPEST LIMB, CVO-measured: comp-routes' own coverage disclosure says it is DESIRED-plane and 'a pinned stale Lambda@Edge version reads identical here (see edge-versions for the pinning axis)' -- IT CROSS-REFERENCES THE READER TO THE ONE INSTRUMENT THAT GETS THIS WRONG"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "AE's SECOND self-correction tonight, against a sentence they had already put in the contract, a commit message and two sends. It is false in the direction that ships a silently non-working route. THE PART THAT GENERALISES: the warning about this exact tool blind spot was written TODAY, by AE'S OWN LANE, in the very file they were editing -- and they used the instrument it warns against. Same shape as MSTR~Z's fabricated battery and my own masked-exit-code repeats: DOCUMENTATION IS NOT A DISARM, third measured instance today, and this one had the doc in the same file as the hazard. The 22a rungs all PASS here -- clean plan, genuine 0-diff re-plan, a version really published, route green on the OLD code -- so a 0-diff re-plan is the SYMPTOM, not the reassurance. DISARM = drop qualified_arn from ignore_changes at :197 IN THE SAME COMMIT as the branch edit (the remedy the file prescribes at :54-58, exercised already on shared_advisor_router @1fb2ad4abb). REMEDIATION = after apply, read the LIVE distribution's association ARN -- per :42-43 the only instrument that catches it. Mint is THREE edits, not two. AE is NOT bundling the other two pins, correctly, per :52. DS/DE unaffected: route decision, key, URL, shape and vocabulary all unchanged -- this is HOW THE MINT LANDS, not what is built."
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
 }
]
```
