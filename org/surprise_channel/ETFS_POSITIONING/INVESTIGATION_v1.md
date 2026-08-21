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
    "third instance today of the same mechanism: a correct artifact committed locally while the seat needing it reads the remote"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.0.0_AB_MSTR",
  "notes": "Routed same-turn by COO before I saw it. DISARM = the integrator push. REMEDIATION is a different state with a different clock: the fresh seat's spec-at-pickup actually reading the amended TO. The spawn brief is the only live delivery surface during the push window, which is why COO sent the three load-bearing lines for it -- the brief is load-bearing, not redundant."
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
 }
]
```
