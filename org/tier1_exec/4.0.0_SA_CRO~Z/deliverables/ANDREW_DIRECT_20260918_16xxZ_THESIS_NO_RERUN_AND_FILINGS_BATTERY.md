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
5. Nothing here authorizes egress, a producer, a schedule or a model call. Building any battery step that calls
   outside Opal still needs his per-use word.
