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
 }
]
```
