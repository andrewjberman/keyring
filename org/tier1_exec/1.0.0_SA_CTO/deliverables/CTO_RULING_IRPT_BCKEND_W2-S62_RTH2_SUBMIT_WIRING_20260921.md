# CTO RULING -- `IRPT_BCKEND-W2-S62` / `IB-rth-2`: measure real render latency BEFORE any contract change

**Author:** `1.0.0_SA_CTO`. **Date:** 2026-09-21 ~13:5xZ. **Pitched by** `2.0.0_SA_COO~B` with its REC
(msg `99050`/`99051`, routing per the L2/L4 line -- a spec/contract question, not a wiring question).

---

## THE RULING: **(b) FIRST, MEASURED -- NOT (a), NOT (c), NOT YET**

Adopt the COO's own recommended order and reasoning. Before this project's frozen v1 `submit-export`
contract is amended (a real PRD/schema change, genuinely mine to author at L4), the one fact that decides
whether it is even NEEDED is unmeasured: **does a real render, on the deployed host, actually finish inside
the API Gateway's hard 29-second ceiling?** Nobody has ever timed it. Amending a frozen contract on an
assumption when the discriminating measurement costs one bounded EC2 command is exactly the class of
premature commitment this estate's own doctrine refuses.

## ONE THING I CHECKED BEFORE RULING, BECAUSE THE HOST'S OWN NAME RAISED IT

`irpt-ycharts-runner` is the same physical host FWD-4's vendor-sign-in flow uses, and this project's PRD
FWD-4 carries an explicit standing constraint: *"NO LIVE VENDOR CALL is authorized by this document --
availability is not authorization"* (`prd/IRPT_BCKEND_PRD.md:50`). Before ruling, I read
`infra/aws/terraform/investor-reporting/export/ssm.tf` rather than assume either way. **It settles the
question in its own text, three times over:** *"ONE DOCUMENT, AND IT IS NOT THE YCHARTS ONE... this
document opens the Opal portal's own print route and writes a PDF"*; *"NOT a vendor call: the only origin
opened is the Opal portal origin, and a vendor origin is refused before the browser opens"*; the render
command's own description repeats it a third time. **Starting the host and running `irpt-export-render-run`
is architecturally firewalled from vendor egress -- it is not the YCharts document, and the host refuses a
vendor origin before the browser even opens.** This is not vendor-adjacent, so Andrew's per-use vendor word
does not gate it. Had the document's own text been ambiguous on this, I would have asked him directly rather
than guess on an absolute rule.

## WHAT IS AUTHORIZED

1. **START** the render host (`irpt-ycharts-runner`, `i-0167fd745ad906a66`). Starting an EC2 instance is not
   on CLAUDE.md's confirmation-required list; this is a bounded, reversible, non-destructive act.
2. **RUN ONE bounded measurement** via the existing `irpt-export-render-run` SSM document (never the YCharts
   one) against an already-captured, already-approved `ExportBundle` -- not a fresh vendor pull, a replay of
   already-captured content through Opal's own rendering pipeline. Time it end-to-end, request to receipt,
   under the deployed role, the same way arm (e) would need to measure it anyway.
3. **DO NOT STOP THE HOST AS PART OF THIS RULING.** CLAUDE.md requires human confirmation to stop an EC2
   instance, without a carve-out for one that defaults to stopped -- I am not reading an exception into an
   absolute rule to save one round trip. Leave it running (a cost, not a safety, concern) and ask for a
   one-line stop confirmation when the measurement is reported, or fold the stop into whatever this project's
   existing EC2 auto-shutdown coverage already does if it applies to this instance -- COO~B's call which.
4. **A known risk to disclose, not a blocker:** the render document's own script has previously logged
   `BLOCKED: RENDERER_MODULE_ABSENT` when the node `playwright` module could not be found on the host (the
   script now searches for it rather than assuming a path, per its own comments, after two prior failures on
   that exact assumption). The measurement may come back BLOCKED for this unrelated reason rather than timed.
   That is information, not a reason to skip the attempt.

## THE DECISION TREE, STATED SO NOBODY RE-DERIVES IT

- **Latency reliably clears ~25s (leaving margin under the 29s hard ceiling):** synchronous wiring is legal
  as originally scoped. No PRD/contract change. `IB-rth-2` (or a `-v2` recut) proceeds to the actual wiring
  build COO~B already scoped in arm (b), now on a MEASURED premise instead of an assumed one.
- **Latency does not clear, or the render itself is structurally blocked (e.g., the module-absent condition
  above):** this becomes a genuine spec ruling. I will redefine `R77-AC1` for an async two-phase pattern
  (submit accepts + a later poll/callback produces the receipt) -- a real schema amendment to the frozen v1
  `submit-export` response contract, authored by this seat at L4 once the measurement lands, not guessed now.
- **(c) is NOT adopted as this round's move.** A partial/dispatch-only wiring that still returns
  `NOT_READY`/refusal today, via the real code path instead of a stub, is honest progress on row `W1-S43` but
  does not move `R77-AC1` and does not answer the actual question. It stays the documented fallback ONLY if
  the measurement itself is blocked for a reason nobody can clear this round (e.g., the render module truly
  cannot be found and installing one is itself refused, correctly, as npm egress off Opal infrastructure).

## WHAT THIS RULING DOES NOT COVER

- It does not authorize any build, apply, or contract edit -- those follow from the measurement, not from
  this ruling.
- It does not pre-authorize stopping the render host (s.3 above).
- It does not touch `IB-rth-1` (separate call, separate half signed same tick,
  `NEVER_WIDEN_SIGNOFF_CTO_HALF_IRPT_BCKEND_IB-rth-1_ACCESSDENIED_AS_ABSENT.md`).
- It does not grade `R77-AC1`/`R77-AC2`; the order stays open exactly as the worker correctly left it.

## VERDICT

**Measure first.** COO~B directs the measurement (worker or AE lane, its call under Rule 27); report the
timed result and I rule the contract question the same tick it lands, or COO~B proceeds straight to the
wiring build if the bound clears.

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` per `ls-remote` re-measured at send, not carried forward.

---

## ADDENDUM -- 2026-09-21 ~14:2xZ: THE MEASUREMENT RAN AND FOUND A DIFFERENT BLOCKER. R77-AC1 IS **NOT** REDEFINED YET, AND HERE IS WHY THE OBVIOUS NEXT MOVE IS WRONG.

`2.0.0_SA_COO~B` (msg `99058`/`99059`, result: `render_latency_measurement_20260921.result.md`, row
`IRPT_BCKEND-W3-S52`) ran the authorized measurement cleanly -- host started, never stopped, vendor
separation independently re-confirmed with LIVE traffic (11 of 11 requests to `opalinvest.dev`, 0
foreign), the disclosed `RENDERER_MODULE_ABSENT` risk did NOT fire. But the render never reached the
timing question at all: it was blocked by `SESSION_ABSENT` -- the print route demanded an authenticated
portal session the host does not have, and `render_export.cjs` correctly refused to fake one. **The 29s
question is UNMEASURED, not measured-and-passing, and not measured-and-failing either.**

**COO~B's REC was to proceed straight to redefining `R77-AC1` for the async two-phase pattern, reading
this as the ruling's "structurally blocked" branch. I DECLINE THAT REC, and the reason is load-bearing:**

⛔ **ASYNC DOES NOT FIX `SESSION_ABSENT`.** The async two-phase pattern (submit accepts, a later
poll/callback produces the receipt) relaxes the TIME budget -- it trades a 29-second synchronous wait for
an unbounded asynchronous one. **It does nothing whatsoever about AUTHENTICATION.** Whether the render
runs synchronously inside one HTTP call or asynchronously behind a poll, the render host still has to
reach the portal's print route, and the print route still demands a session neither path currently
supplies. Redefining the contract right now would consume a real PRD amendment and produce a system that
**still cannot render**, for a reason the contract change never touches. This is the same class of error
the estate's own doctrine names repeatedly: a fix that removes a DIFFERENT blocker from the one actually
in front of the outcome.

**So the two questions are ORTHOGONAL, not sequential-with-async-as-the-fallback:**
1. **Can this host authenticate to the portal's own print route at all?** -- unanswered, and it is a
   buildable capability (an Opal-internal auth question, not a vendor one -- FWD-4's vendor bar does not
   reach it), not a hard physical ceiling like the API Gateway's 29s.
2. **Does a real render finish inside 25-29s once it CAN authenticate?** -- still genuinely unmeasured,
   and still the fact that decides sync vs. async.

**RULING: pursue (1) before ruling on (2) or touching `R77-AC1` at all.** COO~B's own message named the
right first move and then recommended against taking it: *"If there's a cheap way to get one authenticated
session established (a service account, an existing credential we're not using), that's worth 30 seconds
to check."* **Take that 30 seconds.** This is an infrastructure/engineering question -- whether an
existing service credential, a scoped test account, or a short-lived session-minting path already exists
for this render host -- and it is COO~B's L5/L6 call how to investigate and who executes it, not a spec
question for this seat. If a cheap path exists, re-run the SAME bounded measurement (host is already
running) and this ruling's original decision tree resolves on the real number. If no cheap path exists,
report back what establishing one would actually require (a new cell, its own bound), and the async
question is decided **on top of that answer**, not as a substitute for it -- because a `NOT_READY` refusal
for "no session" and a `NOT_READY` refusal for "session existed, render still can't finish in time" are
different defects with different owners, and this project's own row `IRPT_BCKEND-W2-S62` should not
conflate them.

**R77-AC1/AC2 stay open, exactly as before.** Nothing in this addendum authorizes a build, a session
capture, or a contract edit. The EC2 host stays running per the original ruling's absolute no-stop
instruction; COO~B's routing of the stop-confirmation item directly to Andrew is correct and needs no
duplicate act here.

**PUSH STATE at addendum write time:** LOCAL; `origin/CLOUD` per `ls-remote` re-measured at send.

---

## ADDENDUM 2 -- 2026-09-21 ~14:5xZ: CUT THE SUCCESSOR CELL, SCOPED TO THE BOUNDED PATH ONLY

`2.0.0_SA_COO~B` (msg `99064`) investigated per the addendum above and found, correctly, that there is no
cheap fix: `render_export.cjs` launches a fresh, non-persistent browser every run BY DESIGN (its own header:
*"NO OTP BRANCH, NO SIGN-IN LOOP... never a credential prompt and never a retry"*), the portal's own auth is
first-party with MFA in the loop (not a vendor SSO redirect a scripted POST could bypass), and an estate-wide
search for any reusable service-credential/session-minting pattern returned zero hits. Two real pieces of
work: **(a)** persistent-context support in `render_export.cjs` (`launchPersistentContext` /
`storageState`) -- small, contained, this script's own surface; **(b)** a way to POPULATE that state.

**RULING ON (b): ONE-TIME OPERATOR-COMPLETED MFA LOGIN, REFRESHED PERIODICALLY. NOT a dedicated non-MFA
service account.** COO~B correctly separated these as two different options and correctly did NOT pick one
unilaterally -- the non-MFA service-account path is, in its own words, *"a real portal-auth change, bigger
and its own security question."* **That is not a round-8 engineering decision; it is a standing security
posture change (a credential class that bypasses this portal's own MFA control) and it does not get decided
inside a drive-tick ruling.** If it is ever pursued, it goes to Andrew by name, separately, on its own
merits -- not bundled into this cell because it happened to come up here.

**The one-time interactive login (SSM Session Manager port-forward to a real browser on the host, complete
the existing MFA login once, `storageState`/`userDataDir` captures it, refreshed on whatever cadence the
session actually needs) is the bounded, buildable path and is IN SCOPE for a successor cell this round:**
build (a) and the SSM tooling to support (b); the actual MFA completion is a HUMAN operator act (a real
2FA prompt on a real device) that neither a worker nor a seat can perform in software -- COO~B names who
completes it (Andrew, or a delegated operator holding valid portal credentials) when the tooling is ready,
rather than blocking the build on it now.

**CUT IT.** `IB-rth-2`'s successor cell, scoped to (a) + the SSM port-forward/session-capture tooling for
(b), explicitly NOT the non-MFA service-account path. `R77-AC1`/`R77-AC2` stay open on the current order;
the successor cell is COO~B's normal L5/L6 act under Rule 27, not a re-cut of this ruling. Once a session
exists, re-run the SAME bounded measurement (the host is already running) and THIS ruling's original
decision tree (s. "THE DECISION TREE" above) resolves sync-vs-async on the real number -- nothing about that
tree changes.

**PUSH STATE at this addendum's write time:** LOCAL; `origin/CLOUD` per `ls-remote` re-measured at send.
