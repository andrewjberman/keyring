# Andrew-direct ~16:3xZ 2026-09-18 -- no re-run until validated end to end; filings are a per-security battery

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, answering the two cards in
`BRIEF_THESIS_CURRENT_TO_DESIRED_20260918.md` (@`9136ff9e73`): "May the filings batch run?" and "Where do the last
nine come from?".

## Verbatim

> I dont care about rerunning until the process is completely validated end to end and the product is basically done.
> We're not surfacing anything right now for users anyway so I dont care about rerunning if we may end up having to
> rerun again later. Regarding the last nine names, my position on this matter is that for every security, we
> basically have a battery on how to get its filings: If US 1.) Start with EDGAR, 2.) Try the BBG resolution, 3.) Try
> websearch maybe surfaced through an IR page. If International: 1.) I dont know but we need a plan. The premise
> behind this is that we will be adding things over time and the more important thing than establishing a pipeline
> itself is the process behind full "security analysis" backend instantiation for a new security.

And, a few minutes later, while the brief update was being written:

> It is worth considering that a translation functionality will be required in cases like these and that should be
> included in the spec/brief you create on Thesis.

## Reading, narrow

1. **"May the filings batch run?" -- answered NOT NOW.** No re-run of existing analyses and no fleet run until the
   process is validated end to end and the product is basically done. Stale analyses stay stale; that is accepted,
   because nothing is surfaced to users today. This does not forbid the runs that VALIDATION itself needs; it forbids
   re-running the fleet ahead of it. Whether an exemplar run for validation is inside that line is his to say, and is
   put back to him as a question, not assumed.
2. **"Where do the last nine come from?" -- reframed.** Not a source for nine names: a BATTERY every security goes
   through to find its filings. His US order is stated: EDGAR, then Bloomberg resolution, then web search via an IR
   page. The international order is his open ask: "we need a plan".
3. **The premise is the priority.** Securities will be added over time, so the deliverable that matters is the PROCESS
   for instantiating the full security-analysis backend for a NEW security -- ahead of any one pipeline.
4. **Translation is in scope for the Thesis spec.** A filing not in English is translated rather than excluded, and
   the Thesis brief carries the design (section 8.4 of `BRIEF_THESIS_CURRENT_TO_DESIRED_20260918.md`).
5. Nothing here authorizes egress, a producer, a schedule or a model call.

## Addendum ~16:5xZ -- the validation question, answered

Asked whether validating on three names not covered today (one US, one international with an English report, one
needing translation; a handful of model calls, not a fleet run) sits inside the "no re-run" line. Verbatim:

> sure set a subagent at opus model in this session to go pursue that, then you and I will proced to the next function,
> exec mgmt

**Reading, narrow:** the three-name validation is AUTHORIZED, run by an Opus subagent of this session. That covers,
per use and for these three names only: EDGAR reads through the estate's `fetch.py`; the `filings.xbrl.org` index and
one report download; web search; downloading each name's annual report from the issuer's own site or its regulator;
Bloomberg reference data; and the estate analyzer's model calls, under a stated spend cap. **It does NOT cover** Lusha
or Bright Data calls (billed vendors, not named; the management enrichment step is recorded as not exercised), any
write to the shared pool, crosswalk or universe (a new key there would change every other seat's census -- the
NVIDIA class), any scheduled-task change, or any repo code change. Building any battery step that calls
   outside Opal still needs his per-use word.
