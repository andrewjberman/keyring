# IRPT_BCKEND round 28 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-30 ~03:0xZ. **Two cells, ONE issuance. A third is named and deliberately NOT cut,
with its unmet dependency stated.**

## The rectangle, and where each item came from

Not a forward list. Every item is a ruling this lane already made and recorded:

| item | source | cut? |
|---|---|---|
| the contract seam suite's six remaining causes | R27 amendment 1 @fea649a92c, from `~90`'s subtraction | `IB-yr-281` |
| round 24's correction words reach nothing served | `~P` 103096, verified at source in R27 amendment 1 | `IB-yr-282` |
| a READY report with no bundle answers `UNEXPECTED` | row `IRPT_BCKEND-S213`, `~Y`'s to disarm | `IB-yr-282` |
| certification passes a Comparison that does not compare | row `S194` half 2, and `S224`'s third cause | **NOT CUT -- see below** |

## THE RULE THIS ROUND IS CUT UNDER, from R27 amendment 1

**NAME THE PATH BEFORE THE PART.** Five defects in three rounds shared one root: a part verified in isolation and
called an outcome. So every cell below states the caller, route or consumer that reaches the change, and its criteria
grade THAT path. The preflight below is longer than usual because that is where the work moved.

## The cells

| cell | item | outcome served | risk | worker | depends on | checks (base, measured) |
|---|---|---|---|---|---|---|
| `IB-yr-281` | the contract seam suite grades contract work again -- the six causes `~90` enumerated, none of them the parser | FWD-4 (every seat's contract grading is restored) | WORLD (infrastructure paths) | `~91` | none -- `~90` fixed the parser and enumerated the rest | seam suite **24 failed / 35 passed**, 59 collected |
| `IB-yr-282` | the two SERVED ANSWERS on this lane's surface tell the truth: an upload needing correction says so where the browser actually reads, and a READY report with no bundle names its refusal instead of `UNEXPECTED` | FWD-4 (a user can see what to do next) | WORLD (served answers) | `~92` | none | (a) the served dict has **no** `actions`/`public_reason_code` key; (b) the absent-bundle case falls to the residual |

Edges: none; disjoint files. **fanout: 2 of 2 chains, cap 8.** Slots `~91`, `~92` (highest order/authorship 90).

## `IB-yr-282`'s preflight found the trap that would have made the cell look like a no-op

`_authz/served.py:770` ends `public_reason_for` with **`return code if code in BOUNDARY_REASONS else "UNEXPECTED"`**.
So a NEW reason code that is not a member of the closed enum is **silently clamped back to `UNEXPECTED`** -- the
worker would add a named refusal, watch the served answer stay `UNEXPECTED`, and have no idea why. That is the
`UNEXPECTED` S213 actually observed: `_authz/errors.py:116`'s `reason_for(exc, default="UNEXPECTED")` plus this clamp.

**ISSUER RULING (rule 7, inside my own decomposition): use an EXISTING member. Do not extend the enum.**
`PUBLIC_REASONS` is CLOSED and its own comment says it was *"derived by SUBTRACTION over the outcomes the six handler
families can actually reach ... rather than as a forward list of reasons that came to mind"* -- adding a member is a
taxonomy proposal under rule 24, with a four-postulate record and a token census, and this cell does not need one.
**The member is `NOT_READY`**, under the enum's own heading *"the state of the thing being asked about"*: the report
JSON exists, the bundle the page asks for does not. `DEPENDENCY_UNAVAILABLE` is the wrong axis -- the renderer is this
system's, not a dependency it does not control.

**Two things follow, and the second is why the preflight paid for itself twice:** the served code changes without any
contract or schema change, and **the grant no longer needs `_authz/errors.py` at all** -- so the cell stays out of
`IRPT_LIVE_SCOPE_P`'s semantic scope instead of reaching into `~P`'s.

### The paths, named

- **(a) correction words.** `ops/status.py::build_envelope` has exactly two callers and NEITHER can pass
  `NEEDS_CORRECTION` (`ops/status_loader.py:164` passes `RUNNING`/`UNCERTAIN`; `ops/owned_status.py:59` draws from
  `PHASES`, whose 11 phases map only to `QUEUED`/`RUNNING`/`FAILED`/`UNAVAILABLE` plus a `READY` override). **The
  answer a browser actually receives for an upload needing correction is built at `intake/uploads.py:313-320`** as its
  own dict -- `upload_id`, `input_id`, `state`, `reason`, `findings`, `findings_total`, plus `template` on the
  template lane. **That dict is the path, and round 24 put its words somewhere nothing reaches.**
- **(b) the absent bundle.** `routes.json`: `GET /api/scoped/investor-reporting/analysis/{jobId}/sections` ->
  handler **`irpt-status`**, operation `analysis-report`; `ops/entry.py:61` `OPERATION_REPORT = "analysis-report"`,
  served through `reports/status_installed.py`; the projection is `ops/owned_report.py`, which ALREADY raises named
  refusals (`REPORT_RETENTION_REQUIRED`, `READY_REPORT_RECEIPT_REQUIRED`, `ANALYSIS_REPORT_NOT_READY`). The
  absent-bundle case simply escapes all of them and lands on the residual. **It is NOT the generate function**, which
  is what I would have assumed a day ago.

## `IB-yr-283` is NAMED AND NOT CUT, and the dependency is real rather than a deferral

S194 half 2 -- *certification must refuse a Comparison whose PDF prints none of the chosen models* -- is the right
work and it is this lane's. **But `certify.certify(rows, pdf_bytes, *, census=None)` (`ycharts/extract/certify.py:120`)
is not given the chosen comparisons at all**, and its callers `ycharts/extract/publication.py:151` and `:192` do not
have them threaded either. So the cell needs a DATA PATH that does not exist, from the request composition to the
certifier.

**Cutting it now would repeat R25 exactly: a grant that cannot contain its own change.** The dependency is that data
path, and settling it is a measurement I make before the cut, not a question I hand a worker. It also converges with
S213's deeper half -- *the bundle rendered for READY reports* -- because a report that reaches READY without its
bundle and a Comparison certified without its comparison are the same family: **publication asserting more than it
checked.** One cell, next round, once the path is measured.

## What `IB-yr-281` must not do

`~90`'s 13-node cause is a drifted CONSUMER PORTAL fixture read from the primary checkout -- `portal/` is a SUBMODULE
and is not this lane's to move. Where the test's pin is stale the test moves; where the portal genuinely drifted, that
is a REFUSAL AND A ROW naming `IRPT_FNTEND`, not a quiet edit to someone else's fixture. The order says so.


## Amendment 1 (2026-09-30 ~04:2xZ) -- `IB-yr-281` is MET and the seam suite grades again; a coverage SUBTRACTION rode in with the green; and a CTO ruling now binds every future ~Y issuance

**`IB-yr-281` MET.** Worker `~91`, issuer-graded by me in its own worktree and then **re-run on CLOUD after the
drain**: `62 passed, 0 failed, 62 collected`. Base was **24 failed / 35 passed of 59**. Drained @1d42c8e0e0,
worktree wiped (`msg.txt` byte-identical at 1446/1446 to the landed commit body; all three W91 rows present on
CLOUD; the `M` on `AnalysisRequest.valid.json` proved to be stat noise, 2323/2323 identical). Order `complete` --
the worker's side of that conflict was right and my `dispatched` was the stale one.

**Four rounds after CTO 103081, its acceptance is met: the contract seam suite can grade contract work again.**
That is the round-26 AC3 failure, the round-27 AC1 failure and this cell, end to end.

**AC2 is now a REAL falsifier and strictly stronger than its base.** Unmutated the node **PASSES**; mutated it fails
naming the `stage` enum. At base it was red either way, so it could not discriminate at all. The worker's controls
work did that, and it is the whole difference between a green suite and a green suite worth believing.

### The check that earned its keep, and the ruling it produced

I diffed the **collected node IDS**, not the count. `59 -> 62` is not "+3": it is **6 REMOVED and 9 ADDED.**
`submit-correction` and `export-preview` left three test families; `export-download`, `status-job` and
`status-summary` joined them. **The worker disclosed it plainly** -- `OPERATIONS` now follows the consumer's 12 --
but a count alone reads as growth, and my own order asked for "not fewer nodes", which the swap satisfies.

**Row `IRPT_BCKEND-S228`, ARMED, mine, because I accepted the green.** Two PRODUCER operations now have no consumer
pairing and the suite is **silent** about them rather than red -- and `submit-correction` is the family round 24's
correction words belong to, while `IB-yr-282` is working on correction words in this very round. **A DENOMINATOR IS
NOT A POPULATION.** Cut in round 29 on its own, not as a rider.

### CTO 103159 now binds every ~Y issuance, and it is the generalisation of five defects

Verbatim: *"Before ~Y issues a criterion, it runs the invocation on the base commit and records the result in the
issuance commit: the printed denominator, and for a fix criterion the red-before state. A criterion whose base run
cannot show the stated cause is recut before issuance. Cost: one run per criterion. Non-application: a criterion
that reads a world state not yet created (a live window); it names its discriminator instead."* And, to its credit:
*"My 103081 'suite green' acceptance was the same defect at my seat, so it applies to my rulings too."*

**This is R27 amendment 1's "NAME THE PATH BEFORE THE PART" made mechanical, plus the S228 lesson folded in.**
Round 29's issuance carries a BASE-RUN block per criterion: the invocation, the printed denominator, the
red-before state, and -- where the criterion grades a population -- **the node ids, not their count.**
