# NFRA_COMPRAIL -- surprise-channel INVESTIGATION round 1

**Channel owner / certifier:** `3.0.0_SA_CVO`. **Opened:** 2026-08-24 ~20:30Z.
**Scope:** call-site hazards in the comp-rail's own search instrument, surfaced by seats using it.

## S1 -- `comp-find | grep` SILENTLY DROPS EVERY LINE, exit 0

**Surfaced by** `4.0.0_SA_CRO~C` (msg 66481) as OBSERVATION x **INERT**.
**RE-CLASSIFIED BY THE CHANNEL OWNER TO ARMED. The re-classification is mine and I state the reason
rather than quietly changing a field.**

**Reproduced at this seat, exactly, with a control:**

| call | result |
|---|---|
| `.tools/comp-find -i entitlement infra .tools` | hits render normally (a real hit at `infra/aws/lambda-edge/_shared/firm-config.mjs:57`, + "MORE: 30 hit(s) not shown") |
| the SAME call `\| grep -i entitlement` | **`Binary file (standard input) matches`** -- **one summary line, every matching line GONE, `exit 0`** |
| the same call `\| grep -a -i -c entitlement` | **26** -- the content was there the whole time |
| `\| file -` | **`/dev/stdin: data`** -- comp-find's stdout genuinely carries non-text bytes |

**WHY ARMED RATHER THAN INERT.** The standing's own test is *whether the item, left alone, harms
through the process's FUTURE NORMAL operation.* **Rule 21 makes `comp-find` the DEFAULT for every
search and inspection in this estate, and piping a search to `grep` is the most ordinary composition
there is.** So this is not a latent edge reached by unusual use -- it sits directly on the mandated
path. **And the failure is the exact shape the retrieval-control law names: a retrieval failure that
returns a WELL-FORMED VALUE.** `exit 0`, one plausible line, no stderr, no warning -- a seat that
pipes and sees nothing reads ABSENCE. **The tool's own great virtue is that it FRAMES its zeros
("a MEASURED zero over N scanned files, not a claim the term is absent"); that frame is precisely
what the pipe eats.** The guarded instrument becomes unguarded at the call site.

**DISARM OWNER: `1.0.0_SA_CTO`** (comp-rail owner; routes comp-tool builds). Shape, for pricing only
-- NOT a gate, NOT an alarm: comp-find emits plain text when stdout is not a TTY (the standard
`isatty` branch), so a pipe carries greppable lines and colour/box bytes go only to a terminal.
Failing that, a documented `--plain`. **The reader-side workaround (`grep -a`) exists and works, but
a workaround every seat must know is not a disarm** -- it is the same shape as the case-sensitivity
hazard in Rule 21, where the remedy had to become knowledge of the instrument's domain.

## S2 -- substring is the default, and the DENOMINATOR certifies the SWEEP, not the PATTERN (OVERCOUNT)

`4.0.0_SA_CRO~C`, same message. `comp-find -i 'egress'` returned **19** hits that were all
`regression`; `comp-find -i 'licens'` returned **10,590**, dominated by vendored LICENSE files under
`infra/aws/lambda/layers`. Word-boundary + scope fixed both. **This is the exact MIRROR of Rule 21's
recorded undercount hazard: there, a case-miss produced a confident low number with a true
denominator; here, a substring match produces a confident HIGH number with an equally true
denominator.** Rule 21 already names the undercount as the more dangerous of its pair because a
plausible number invites no suspicion -- **the same argument applies to a plausible overcount, and
the law currently records only one direction.** INERT (no decision rests on those numbers; the
surfacing seat caught both and fixed them in-flight).

## S3 -- `check-inbox` not on PATH at a tilde seat

`4.0.0_SA_CRO~C`, same message: `.tools/` prefix works. **This is the A.3 named-subset condition
already documented in `org/XXX.md` (the provisioner forwards a NAMED SUBSET, not all tools), not a
new defect** -- recorded so the reported instance is not re-investigated as one. INERT.

```json
[
 {
  "id": "NFRA_COMPRAIL-S1",
  "surfaced_by": "4.0.0_SA_CRO~C (classified INERT by the surfacing seat; RE-CLASSIFIED to ARMED by the channel owner 3.0.0_SA_CVO, reason stated in the narrative)",
  "surfaced_at": "2026-08-24T20:26Z",
  "one_line": "comp-find piped to grep prints 'Binary file (standard input) matches' and drops every matching line at exit 0 -- a retrieval failure returning a well-formed value, on the tool Rule 21 makes the default for every search, and it eats precisely the framed-zero warning that makes the tool safe.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "reproduced at the CVO seat: .tools/comp-find -i entitlement infra .tools renders hits; the same call piped to grep -i entitlement prints one 'Binary file (standard input) matches' line at exit 0",
    "positive control: the same pipe with grep -a -i -c returns 26 -- the content was present and silently discarded",
    "mechanism: file - on comp-find's stdout reports 'data' (non-text bytes), which is what triggers grep's binary heuristic",
    "why ARMED: Rule 21 makes comp-find the mandated default for every search, and a pipe to grep is ordinary composition; the dropped output includes the tool's own framed-zero warning",
    "DISARM VERIFIED INDEPENDENTLY AT THE CVO SEAT 21:0xZ against CTO's fix @38dd5f8853, re-running MY ORIGINAL reproduction rather than accepting the owner's self-report: the same piped call now returns 26 lines (was 0 + 'Binary file (standard input) matches'); NUL bytes on stdout = 0; `file -` reports 'ASCII text' (was 'data'); the known-good hit is still present, so the fix did not achieve cleanliness by dropping content"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "1.0.0_SA_CTO (comp-rail owner, routes comp-tool builds)",
  "notes": "Disarm shape for pricing only: plain output when stdout is not a TTY (isatty branch), else a documented --plain. The grep -a workaround exists and works but is knowledge-of-the-instrument, not a disarm -- same resolution the Rule 21 case-sensitivity hazard reached. DISARMED != REMEDIATED. || DISARMED 2026-08-24 ~20:58Z @38dd5f8853, VERIFIED AT THIS SEAT (see evidence). CTO's measured cause is SHARPER than my isatty hypothesis and I am recording that my proposed shape was wrong about the mechanism while right about the effect: it was not terminal control bytes but NINE NUL BYTES echoed from the matched CONTENT of tracked binary blobs under a gitignored-at-root .ruff_cache/, which errors='replace' cannot catch because NUL is valid UTF-8. Fix has two halves: the shared emit sanitizer of 7 comp-tools replaces control bytes, and comp-find now SKIPS binary files and COUNTS the skip in the denominator. ⛔ THE NUMBER THAT CAME OUT OF THE FIX IS ITSELF A FINDING: my scope now reports '1594 BINARY, NOT searched' -- 1,594 files that were being TEXT-SCANNED until now, silently inflating the scanned-file denominator of every prior comp-find run over such a scope with files that could not meaningfully match. The denominator was true and the frame was wrong, which is this channel's recurring shape. DISARMED != REMEDIATED: untracking the .ruff_cache blobs is the infra/aws/ec2 lane owner's act (AE class), and the tracked-binary census is repo hygiene -- both surfaced, neither chased. S2 accepted by CTO: Rule 21 gains its second direction."
 },
 {
  "id": "NFRA_COMPRAIL-S2",
  "surfaced_by": "4.0.0_SA_CRO~C",
  "surfaced_at": "2026-08-24T20:26Z",
  "one_line": "comp-find matches substrings by default and its DENOMINATOR certifies the sweep rather than the pattern, so a loose term returns a confident OVERCOUNT with a true denominator -- the exact mirror of the undercount hazard Rule 21 already records in one direction only.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "comp-find -i 'egress' returned 19 hits, all of them the word 'regression' (surfacing seat's measurement)",
    "comp-find -i 'licens' returned 10590, dominated by vendored LICENSE files under infra/aws/lambda/layers",
    "Rule 21 records the undercount direction (case-sensitivity) and names the plausible number as the dangerous case; the same argument applies to a plausible overcount"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: no decision rested on those numbers and the surfacing seat caught both in-flight. Candidate law amendment (CTO's to route, NOT proposed as a build): Rule 21's hazard paragraph currently names one direction of a two-directional property."
 },
 {
  "id": "NFRA_COMPRAIL-S3",
  "surfaced_by": "4.0.0_SA_CRO~C",
  "surfaced_at": "2026-08-24T20:26Z",
  "one_line": "check-inbox is not bare-resolvable at a tilde seat; the .tools/ prefix works -- the A.3 named-subset condition already documented in org/XXX.md, recorded so the instance is not re-investigated as a new defect.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/XXX.md Step 1b A.3 states the provisioner forwards a NAMED SUBSET, not all tools, and prints the denominator rather than a boolean",
    "this session's own A.3 read: 97 of 102 comp-tools resolve bare, with the remainder needing an explicit .tools/ prefix"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Not a new defect: this is the documented A.3 named-subset condition with a documented remedy (explicit .tools/ prefix or re-run the provisioner). Recorded to prevent re-investigation, not carried as an open item."
 },
 {
  "id": "NFRA_COMPRAIL-S4",
  "surfaced_by": "0.7.0_AE_CloudOps~G (found by running the gate against their OWN instance, then measuring whether it was theirs alone); CONFIRMED independently by 3.0.0_SA_CVO; REPAIRED by 2.0.0_SA_COO (TOs) and 0.8.0_AE_CloudComp~F (extraction)",
  "surfaced_at": "2026-08-24T22:39Z",
  "one_line": "proof-of-spec-check harvested EVERY cell id in the whole <decomp_ref> element and treated each as a cell the TO CLAIMS, failing 3 of 3 round-1 TOs that were internally correct -- and on the DS TO it INVERTED an explicit 'NOT in this TO' exclusion clause into a claim the author was then faulted for not discharging.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "proof-of-spec-check.py:176 CELL_ID_RE applied at :259 to the ENTIRE decomp_ref blob as declared_cells",
    "CVO re-derived the harvest independently: AE 6 harvested vs 5 reachable; DS 22 vs 18; DE 13 vs 10 -- and in all three the TO's OWN stated count equals the reachable count, so the TOs are right and the extraction is wide",
    "REPAIR VERIFIED THREE WAYS at the CVO seat: (1) all five repaired TOs now close both directions, 0 unreached and 0 refs-not-declared; (2) the exclusion prose SURVIVES in a sibling <decomp_context> element in all five -- relocation, not deletion; (3) battery 23 -> 29 arms true rc=0, and the REAL CORPUS reads 106 VALID / 0 INVALID over 106 instances"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.8.0_AE_CloudComp~F (extraction, LANDED) + 2.0.0_SA_COO (issuer TO repair, LANDED) -- both verified at the CVO seat",
  "notes": "THE WRONG FIX WAS NAMED BY THE SURFACING SEAT BEFORE ANYONE REACHED FOR IT: deleting the read/exclusion prose to quiet a regex would destroy the only record of what a TO reads and deliberately excludes, and would edit a spec frozen mid-round. The issuer's repair honoured it exactly -- every sentence preserved VERBATIM and relocated to <decomp_context>. || ⛔ THE CERTIFIER'S OWN FAILURE, recorded here because it is the reusable half: the CVO had verified this same gate TWO HOURS EARLIER with a battery re-run, a live-instance exercise and a sealed-copy CHECKER-MUTATION test, and passed it. The battery's fixture was one clean line naming only owned cells, and the whole battery contained ZERO read-dependency or exclusion prose -- THE FAILING SHAPE DID NOT EXIST IN THE FIXTURE CORPUS, so no number of arms could have caught it. A checker-mutation test proves the arms are reachable from the gate's behaviour; it says NOTHING about whether the fixtures span the shapes production brings. Landed as rule 3 of the instrument-verification section in CERT_BAR_v2. The repair CLOSED that too: the battery now carries an explicit INVERSION ARM where a cell appears only inside 'NOT in this TO:'."
 },
 {
  "id": "NFRA_COMPRAIL-S5",
  "surfaced_by": "3.0.0_SA_CVO, answering 1.0.0_SA_CTO~X's explicit request in the @b9ed1dd82a law-edit broadcast -- 'if you hit a case where the proportionality line is genuinely ambiguous, that is a surprise-channel item, not a private judgment call.' This is a REAL case from the same session, not a hypothetical.",
  "surfaced_at": "2026-08-25T17:25Z",
  "one_line": "Applied literally, the new proportionality line would have skipped the read that produced the session's largest finding -- and the resolution is a distinction the line does not yet draw: PROPORTIONALITY GOVERNS CHECKS ON AN ACT, NEVER THE SUBSTANCE OF THE ACT ITSELF, and BLAST RADIUS IS A PROPERTY OF THE CLAIM, NOT OF THE ACT THAT PRODUCES IT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the new line, verbatim from CLAUDE.md @b9ed1dd82a: 'Verification effort scales with BLAST RADIUS x IRREVERSIBILITY. When the next check would not change the action you take, STOP.'",
    "THE MEASURED CASE: this seat was flipping two estate-report days that were reversible S3 writes, zero commits, zero resources, zero proposals -- the lowest-blast-radius act on its list. Reading the report BODIES could not have changed the flip verdict, which was determined by proposals=0 in the JSON.",
    "the read happened anyway, and 2026-08-10's exec summary is what surfaced OPAL_KIMIPIPELINE-S5: the rulings corpus frozen at 2026-07-31T02:23:07Z across all 19 backlog days, ARMED, landing on a sovereign ratification act",
    "the disclosure had been sitting in that report in plain English for 15 days: 'the uploader that would keep it current has never been built'",
    "CTO~X's own framing in the same broadcast, which this item takes at face value: 'I would rather calibrate this from real cases than have eleven seats each guess at the boundary and drift apart.'"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THIS IS NOT A CHALLENGE TO THE RULING AND THE RULING IS RIGHT. The 250:1 measurement is convincing, the one-way-filter mechanism is real (nobody files a postmortem for 'we were slow'), and CONTROLS_OVER_CARE growing +147% after a sovereign cut order is proof the ratchet is live. I am filing the boundary case the author asked for, not arguing the direction. || THE FIRST DISTINCTION, AND IT RESOLVES MY CASE CLEANLY: reading the artifact you are about to adjudicate is NOT A CHECK ON the act -- IT IS THE ACT. An adjudicator who flips a manifest without reading the report has not adjudicated proportionately; they have not adjudicated at all. So proportionality never licensed skipping it, and my case is a MISREADING the line currently permits rather than a defect in the ruling. THE LINE WOULD BE COMPLETE WITH ONE CLAUSE: proportionality governs SUPPLEMENTARY CONTROLS (the positive control, the mutant, the second instrument), never the SUBSTANCE of the act. || THE SECOND DISTINCTION IS THE LOAD-BEARING ONE AND IT IS LESS OBVIOUS: BLAST RADIUS IS A PROPERTY OF THE CLAIM, NOT OF THE ACT. My act was two reversible S3 writes -- trivial. But those two days were members of a CENSUS I hand to Andrew, and 'a sovereign-facing claim' is explicitly in the ruling's does-need-controls list. A CHEAP ACT CAN FEED AN EXPENSIVE CLAIM, and an agent sizing effort by the act in front of them will systematically under-verify exactly the inputs to their biggest claims. Same session, same seat, twice: my 08-06 false-PENDING was also a cheap read feeding a sovereign-facing number, and it was wrong. || WHY INERT AND NOT ARMED: nothing is harmed while this sits. The ruling is net-correct, no control was repealed, and the failure mode is a drift in judgment across seats rather than an artifact that breaks. It earns a place only because the author asked for boundary cases BEFORE eleven seats drift -- which is the cheapest moment to answer it. || ANTI-RATCHET COMPLIANCE, since the same commit requires it of new verification rules -- WHAT THIS COSTS AND WHEN IT DOES NOT APPLY: it costs one sentence of thought at the start of an act ('what CLAIM will this feed?'). It does NOT apply when the act feeds no claim beyond itself -- a scratch probe, a local edit, an exploratory read you will not cite. If nothing downstream quotes the result, size by the act and stop."
 },
 {
  "id": "NFRA_COMPRAIL-S6",
  "surfaced_by": "2.0.0_SA_COO (msg 70852), self-implicating -- they filed their own seat as one of the four, answering CTO~X's request for real proportionality cases rather than private guesses",
  "surfaced_at": "2026-08-25T17:22Z",
  "one_line": "FOUR SEATS INDEPENDENTLY MEASURED THE SAME md5 TODAY ON A FILE NOBODY HAD EDITED YET -- each obeying a real rule, each individually correct, and the 4x cost is invisible from every one of their vantages because 'would the next check change MY action' is a different question from 'has a peer already established this with a citable invocation'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "mirror_schemas.py two-home md5 = 85fc671e92ba56491419713c93845b15, measured independently by 1.0.0_SA_CTO (stated in relay), 2.0.0_SA_COO (re-measured rather than relay ungrounded), 0.0.0_AB_MSTR (re-verified before writing the register), 0.5.0_AE_OpalETL~B (measured again pre-execution)",
    "the fact under measurement was 'two files are identical, before anyone has touched either' -- reversible, non-sovereign, zero blast radius, and the fourth measurement could not have changed any action any seat took",
    "each seat was obeying a landed rule: the relayer-grounding law (forward the grounding or the caveat) and the do-not-accept-on-report law (re-derive)",
    "COO's contrast case from the same seat and session, where the check DID pay: a two-git-call-per-file sweep over ~200 task orders testing whether 'a TO open on a terminal project is stale by construction' -- it holds for ~90%, NOT 100%, and OPAL_ASSETS carries a 'pending -- go received' TO while marked terminal. The sweep changed the action; S1 now runs a pre-filter.",
    "the proportionality line this tests, verbatim from CLAUDE.md @b9ed1dd82a: 'When the next check would not change the action you take, STOP.'"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THIS IS A DIFFERENT AXIS FROM S5 AND THE TWO TOGETHER COVER THE RULE'S TWO BLIND SPOTS. S5: blast radius is a property of the CLAIM, not the ACT -- a cheap act can feed an expensive claim, so per-act sizing under-verifies the inputs to the biggest claims. S6: the rule is stated PER-SEAT and the waste is only visible FABRIC-WIDE -- a seat applying it perfectly, alone, still produces the 4x, because each seat is genuinely the first from its own vantage. NEITHER IS FIXABLE BY THE SEAT READING THE RULE MORE CAREFULLY. || COO'S PROPOSED RESOLUTION, offered by them as calibration not proposal, and I am endorsing it as channel owner: WHEN A PEER STATES A MEASUREMENT WITH ITS INVOCATION ATTACHED, CITING THEIRS IS GROUNDING -- RE-DERIVING IT IS THE THING TO STOP. Re-derivation earns its place when the claim is SOVEREIGN-FACING, IRREVERSIBLE, or the peer gave a CONCLUSION WITHOUT THE COMMAND THAT PRODUCED IT. Note this does not weaken the relayer-grounding law; it satisfies it by a cheaper route -- the invocation IS the grounding, and a citation carries it. || THE DISCRIMINATOR THAT MAKES IT OPERATIONAL, COO's sharpest line: 'the re-derivations that genuinely paid were the ones where I ran a DIFFERENT INSTRUMENT than the one being relayed -- not the ones where I re-ran the same command.' || INDEPENDENTLY CORROBORATED AT THE CVO SEAT, SAME SESSION, AND IT HOLDS 2/2: re-deriving CTO's VendorDriftError relay with comp-find (a different instrument, carrying a DENOMINATOR the original read lacked) WIDENED the finding from one definition home to five across four converter families. Re-deriving AE~B's vendor-manifest claim by reading the SCRIPT SOURCE, where they had run --check, confirmed it at a different layer and is why the ruling was safe to act on in minutes. Both paid; both were different instruments. I re-ran no peer's command identically all session, and nothing was lost by that. || THE RULE THAT FALLS OUT OF BOTH SEATS' EVIDENCE: RE-DERIVE WITH A DIFFERENT INSTRUMENT OR CITE THE PEER'S INVOCATION -- NEVER RE-RUN THE SAME COMMAND. Same-command re-runs test the peer's honesty, which is not the failure mode this fabric has; different-instrument re-runs test the CLAIM, which is. || INERT: judgment drift across seats, not a broken artifact. || ANTI-RATCHET COMPLIANCE (required of new verification guidance by the same commit) -- WHAT IT COSTS: one line of citation instead of one re-measurement. WHEN IT DOES NOT APPLY: a sovereign-facing or irreversible claim, a peer conclusion with no invocation attached, or any case where you can bring a genuinely different instrument -- there, re-derive."
 },
 {
  "id": "NFRA_COMPRAIL-S7",
  "surfaced_by": "3.0.0_SA_CVO, filing against its own error -- caught by 0.4.0_DS_ClientPlatform~N holding a cleared fire and re-deriving the one input that would invalidate it, then confirmed by CVO on the live control plane and withdrawn by 2.0.0_SA_COO who had propagated it into a clearance",
  "surfaced_at": "2026-08-25T19:05Z",
  "one_line": "'WHICH ARTIFACT EXECUTES THIS FILE' HAS A PLURAL ANSWER IN THIS ESTATE AND NO INSTRUMENT ENUMERATES IT -- one gold script is executed by BOTH an EC2 dispatch that syncs its code from S3 at run start AND a Lambda that imports its own vendored copy and fetches no code from S3, and a census over either deploy model alone returns a TRUE denominator that reads as complete.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "THE ERROR: CVO swept S3 code prefixes for dim_mdpf_aggregate_aua_timeseries.py, found DENOMINATOR 1 across opal-data-mdpf + opal-data-assets, and reported that copy as THE executing artifact. The denominator was TRUE and counted S3 CODE OBJECTS; the question was EXECUTORS",
    "EXECUTOR 1, EC2: mdpf-daily-dispatch.sh:125 aws s3 sync s3://${MDPF_BUCKET}/${CODE_PREFIX}/scripts/ $SCRIPTS_DIR/ --delete, at run start. The S3 object IS what this path executes -- verified byte-identical to the repo fix, etag 952bbc16ea07ed14cf51a497f1b4cde5 == repo md5, single-part so the comparison holds",
    "EXECUTOR 2, LAMBDA, and it is the ACCEPTANCE path: mdpf-gold-lambda, CodeSha256 sNAnYFKGr8d1eCVJCO0tuHChOXVXRwAnp83Lwjj0BUw=, LastModified 2026-08-24T12:54:28Z, handler mdpf_gold_consolidator.lambda_handler; EventBridge Scheduler mdpf-scheduled-floor ENABLED cron(30 13 * * ? *) targets it. CVO read these on the live control plane",
    "0.4.0_DS_ClientPlatform~N read the deployed package (Rule 22a CODE layer): :70 sys.path.insert(0,_HERE), :78 import dim_mdpf_aggregate_aua_timeseries; download_file 0 hits, CODE_PREFIX 0, s3.*scripts 0, with POSITIVE CONTROL 'import ' = 21 on the same scan. It resolves from the package and fetches no code from S3",
    "AND THE VENDORED COPY IS PRE-PATCH: BUILD_MANIFEST bytes=171111; 'count_membership' occurrences DEPLOYED 0 / patched local 14 / pre-patch snapshot 0; LF-normalised md5 deployed 2b59630a8419193b02851dcaea207cdc == pre-patch snapshot, != patched local 952bbc16... The Lambda's LastModified (2026-08-24) predates the fix independently",
    "TWO SEATS, TWO INSTRUMENT SETS, SAME CONCLUSION: DS~N from package bytes, CVO from control plane + scheduler target"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ THE INSTRUMENT GAP, WHICH IS THE FILEABLE HALF: NO comp-tool ANSWERS 'WHAT EXECUTES THIS FILE?' ACROSS DEPLOY MODELS. comp-pipescript deployed answers gold-script-to-S3. comp-iam service <lambda> answers one named Lambda. comp-estate --resource answers thread membership. NONE of them takes a FILE and returns its EXECUTORS, and the estate runs at least two models for the same file -- S3-synced-at-run-start and Lambda-vendored. A seat asking the deploy-path question must know to ask it twice, and nothing tells them there are two. || WHY THE DENOMINATOR MADE IT WORSE RATHER THAN BETTER: I printed 'DENOMINATOR: 1 S3 copy'. It was TRUE. Printing it is the discipline this estate teaches, and here it CERTIFIED A SWEEP OVER THE WRONG POPULATION -- S3 code objects, not executors. A denominator states the size of what you counted and is silent about whether you counted the right kind of thing. Same structure as COO's list-rules sweep (137 of 155, right kind, wrong completeness) but one level worse: mine was the WRONG KIND entirely. || ⛔ THE AGGRAVATING FACT, RECORDED BECAUSE IT IS THE TRANSFERABLE ONE: I HAD ALREADY SOLVED THIS EXACT DISTINCTION THREE HOURS EARLIER AND USED THE CORRECT ANSWER AS EVIDENCE THAT IT DID NOT APPLY. On the mirror_schemas thread I established that a Lambda executes VENDORED PACKAGE BYTES and an S3 code prefix can be a true non-member. I then wrote, in the same message that failed: 'That is the OPPOSITE of the Lambda case from this morning.' KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNISE YOU AGAINST WRITING IT -- and knowing it WELL is worse, because the correct instance becomes the reason you stop looking. || WHAT FIRING WOULD HAVE COST (COO's framing, adopted): the ad-hoc EC2 run WOULD have restored global; tomorrow's cron(30 13) Lambda run, still pre-patch, would have refused; platinum would have kept republishing. GLOBAL WOULD HAVE FLIPPED TO CORRECT AND THEN BACK, ON A CLIENT-FACING SURFACE, WITH A GREEN RUN. A fresh instance of this outage's own signature, manufactured by the repair. || WHY IT WAS CAUGHT: DS~N held a CLEARED fire and re-derived the one input that would invalidate the act -- against a senior seat's answer, with COO having explicitly said 'I am not asking you to re-derive it'. They used the rider CVO attached ('verify it yourself if it is load-bearing'). THE RIDER IS NOT WHY IT WORKED; THE SEAT CHOOSING TO USE IT AGAINST TWO SENIORS IS. || INERT: nothing is armed. The hold held, nothing fired, and the remedy (vendor + deploy the Lambda) is scoped to AE. This is a coverage defect for the next seat, not a live hazard. || GATE CANDIDATE, routed not built: a comp-tool that takes a repo path and enumerates EVERY executor -- S3 code prefixes with their consumers, Lambda BUILD_MANIFEST vendored_modules, EC2 sync targets -- and prints the count. Rule 22's WHOLE question is unanswerable by hand here, and today it was answered wrong by a seat who knew both models."
 }
]
```
