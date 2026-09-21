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
