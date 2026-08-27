# ANDREW-DIRECT 2026-08-27 ~05:0xZ — daily report: rigid template, structured JSON, daily_reports/ root, commit-kind under Rule 24

**Terminal:** 1.0.0_SA_CTO (laptop base), live design session on the /daily-sprint visual.
**Channel:** voice at this terminal. Operative words, VERBATIM (voice transcription):

> "for the headline card ... it's effectively a summary of the kind of day it was and either the
> biggest win or ... something that was demonstrative of the day ... it should be kind of a
> standalone feature. It should be like either the biggest win or like an amalgamation of some
> kind. I don't think it should just be a sprint item."

> "all of this should be rigidly templated. And when we create the slash daily dash sprint, the
> skill ... the skill should be designed with this visual shape explicitly in mind ... they know
> that they're looking for headline. They know that they're looking for the sprint items and
> associated who, what, where, why. ... they know that they're gonna be looking at that directives
> dot YAML to pull all the projects and like a little subtext summary ... they know that they need
> to get commits, and they need to tag them."

> "I think we may need a better mechanism or a more stable definition of the commit types. ...
> I don't know the difference between build and architecture. ... I would refer to rule twenty
> four from Claude dot MD. Those items should be mutually exclusive, collectively exhaustive,
> same state, same grain, same intent. We need to follow rules there."

> "all of this stuff should basically be delivered in the form of a structured JSON where that
> structured JSON is mapped explicitly to this visual shape. So we need to effectively create the
> infrastructure to do this. I don't know if it makes sense to have a root folder for daily
> underscore reports, and those JSONs and visual outputs are all saved there, and then all
> relevant scripts that the skill refers to are in there, and we kinda just group everything in
> there. That seems like it might be the best way to approach this."

## Executed same-turn (this session)

1. **`daily_reports/` root created** — schema/ templates/ scripts/ data/ out/ + README (the law).
2. **`schema/DAILY_REPORT.schema.json`** — the structured JSON contract, mapped 1:1 to the visual;
   headline is a standalone object (`kind`: biggest_win | amalgamation | day_summary), sprint items
   carry card (max 52 chars, fits-whole law) + WHO/WHAT/WHERE/WHY + viz type + 3 chips; team
   activity carries `claim: measured|inferred` on both cuts.
3. **`templates/daily_report_template.html`** — the V6 design frozen as the ONE rigid template,
   fully data-driven (`__DATA__` injection).
4. **`scripts/render_daily_report.py`** — validates (fails loud: card-length law, enum values,
   both team-activity cuts summing to the commit denominator) and renders to out/.
5. **`scripts/commit_census.py`** — measured by-kind census. **commit_kind enum re-derived under
   Rule 24:** axis = AUTHOR SEAT CLASS (mechanical, first-match on the author string), which
   dissolves the build-vs-architecture ambiguity he named — the four-postulate record is in
   `daily_reports/README.md`; enum is DRAFT pending word-boundary census + CVO routing before any
   consumer beyond this report builds on it. First run (2026-08-26): 423 commits, 28 workers,
   0 UNATTRIBUTED.
6. **First instance:** `data/DAILY_REPORT_2026-08-27.json` -> `out/DAILY_REPORT_2026-08-27.html`,
   rendered and verified in-browser.
7. **`.claude/skills/daily-sprint/SKILL.md` rewritten against the visual shape** — step 6 now
   census -> JSON -> validate/render (supersedes the 08-26 `render_sprint.py` step, retired); a
   "The visual shape" section tells any runner exactly what they are looking for.

## Standing laws this record carries

- The headline is a STANDALONE feature (kind of day + biggest win / amalgamation), never a
  sprint item.
- Card headlines fit whole — no ellipsis, ever (schema + renderer + template guard).
- WHO/WHERE touchpoints are B2B only (firms, platforms, dashboard pages) — never an individual
  investor or account.
- Team-activity values carry their claim; commit_kind is seat-class (declared proxy), Rule-24
  recorded, DRAFT until ratified.

Push state stated in the same-turn broadcast.

## Follow-up word, same terminal (~05:1xZ) — the owned-paths grant

The new `daily_reports/` root matched no path rule; safe-commit refused all 8 files UNDEFINED.
Per the org/sprints/** precedent (SoD: grantee does not self-land) the grant ask was queued to
0.0.0_AB_MSTR (dark at the time; inbox 20260827T051442Z). Surfaced to Andrew live. His word,
VERBATIM: **"you land it, cto should be the writer for this."**

Executed on that word: `daily_reports/**` -> lane `TIER0_TIER1_STARTUP_DOCS` (reused, not minted —
same runner population as org/sprints/**), landed by 1.0.0_SA_CTO with the SoD set-aside recorded
in the rule's own comment block; his word also names CTO the WRITER/OWNER of this surface
(template + schema = CTO design surface; daily data/out = that day's runner). MSTR follow-up sent
same turn resolving the queued ask.
