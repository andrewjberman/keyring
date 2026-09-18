# Andrew-direct ~17:1xZ 2026-09-18 -- Exec Management: both cards YES

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, answering section 2 of
`BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md` (@`36ed77f347`), as put to him:

1. *"When there's no filing, should Bloomberg's executive list fill the table?"* -- recommended: yes, clearly labelled
   as coming from Bloomberg, with tenure left blank and the reason stated.
2. *"Should LinkedIn profile lookups (Lusha, a paid service at 2 credits a company) be part of setting up a new
   security?"* -- recommended: decide after the three-name validation reports.

## Verbatim

> 1.) Yes. 2.) Yes they should.

## Reading, narrow

1. **Card 1 -- YES, in the form recommended.** When the filing yields no roster, Bloomberg's `COMPANY_EXEC_OFFICERS`
   (names and titles) fills the officer table, labelled as Bloomberg's, with role start, tenure and the pool comparison
   ABSENT and the reason stated. It changes contract C-EXEC-MANAGEMENT's ratified text, so it lands as a PRD change
   `1.0.0_SA_CTO~Z` writes and the CVO signs, not as a field add.
2. **Card 2 -- YES, and ahead of the recommended timing.** Lusha profile links are a step of instantiating a new
   security. He chose not to wait for the validation.
3. **Not covered by either answer, and put back to him as a question:** (a) the CEO-profile web search, the OTHER billed
   half of enrichment (Bright Data SERP), which was not in card 2; (b) whether the three-name validation now running
   should exercise Lusha on its names. The validation's recorded scope excludes both, and stays that way until he says
   otherwise.
4. Nothing here authorizes a fleet run; his "no run until validated end to end" stands.

## Addendum ~17:2xZ -- the CEO search, answered and redesigned

Asked whether his yes covered the CEO-profile web search (Bright Data), and whether the running validation should do
the Lusha lookups. Verbatim:

> We should also do that, search the CEO's name with Bright Data SERP, and have an agent go through it and
> pull/organize the relevant results.

**Reading, narrow:**
1. **The CEO search is part of instantiation, and its design changes.** It becomes a Bright Data SERP search on the
   CEO's NAME, not today's single query scoped to the company's own IR domain, followed by an agent (a model step)
   that goes through the results and pulls and organizes the relevant ones. This replaces contract C-EXEC-MANAGEMENT's
   "ONE targeted SERP query on the company's own IR domain ... capped at one page" (`enrich.py:13-15`), so it joins
   the same amendment as cards 1 and 2.
2. **The CEO only**, as he said; other officers are not widened into it.
3. **Whether the running three-name validation should call Lusha or Bright Data now is NOT answered by this.** Its
   recorded scope still excludes both.

## Addendum ~18:4xZ -- an exploration subagent for the CEO step

Verbatim, quoting back this seat's summary of the CEO step: *"Also set up another subagent to go explore how this would
be properly implemented"*.

**Reading, narrow:** one subagent of this seat, on Opus as for the validation, explores and writes up how the CEO step
(Exec Management brief s.9) should be implemented, with a scratch prototype. Covered, for that exploration only: up to
10 Bright Data SERP queries through the estate's existing zone and key; fetching the public pages those return; model
calls for the curation prototype under a US$5 cap; three sample CEOs. **Not covered:** Lusha; any S3 write; any repo
code change or commit; any schedule; storing any contact data.
