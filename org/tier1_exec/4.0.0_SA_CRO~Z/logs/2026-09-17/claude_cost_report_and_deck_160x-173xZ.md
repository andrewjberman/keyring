# 4.0.0_SA_CRO~Z -- Andrew-direct: Claude cost-per-output report + slide deck, 16:0x-17:3xZ 2026-09-17

**archetype:** BUILD (SCRIBE)

## Objective

Andrew-direct ~16:0xZ at this terminal (record @`12fa905d41`, broadcast msgs 23543-23545): a markdown report and an
associated slide deck, built to the `deck_generation/` brand rules, showing the true cost per output of running Claude
and the data-sovereignty trade of a personal subscription with usage sharing turned off. Andrew supplied a long GPT
thread as context; it is saved verbatim beside the record and labelled SUPPLIED (unverified, no egress this session).

## Compiler Tools

| tool | result |
|---|---|
| `comp-find ... --limit` | the rail-compliant replacement for two denied searches (a glob grep and a comp-find piped to `head`) |
| Python stdlib reads | transcript JSONL, session-serial map and slide-library shapes; outside the comp-tool corpus or binary |
| `# rail-checked:` marker | one read-only census the rail misclassified as a repo search |
| raw `grep` | pipe receivers and single build-script lookups only |

## Work Completed

- `deliverables/CLAUDE_COST_REPORT_20260917/measure_claude_usage.py` (stdlib, pure ASCII): reprices the site-Z session
  transcripts at API list prices. Dedupe on (message id, request id, parent session); five price classes (input, cache
  write 5-minute, cache write 1-hour, cache read, output); seat attribution through `org/mcp/sessions/<id>.serial`;
  commits and completed task orders from git for per-output unit costs.
- `usage_summary.json` (generated 16:30:06Z): $8,329.75 over 30 days, 28,259 responses, 13.0B tokens; cache reads
  72%; per commit $1.72, per completed task order $44.54, per active day $297.
- `CLAUDE_COST_PER_OUTPUT_AND_DATA_SOVEREIGNTY_REPORT_20260917.md`: sections 1-11, every claim labelled MEASURED /
  REFERENCE / SUPPLIED / STATED.
- `deck_generation/prompts/claude-true-cost-per-output.deck.md`: 17 slides via `/deck-prompt`; renderer ran clean.
- `deck_generation/dev/scripts/claude_true_cost_build.py`: `/deck-gen` build. Final gate: 17 slides, 0 lint
  violations, 17/17 coverage. Output `deck_generation/output/Opal_True_Cost_of_Claude.pptx` (gitignored), copied to
  the Desktop, sha256 `a859c9fa0d60d095...` on both copies.
- Visual QA over PowerPoint COM renders, fixed and re-rendered until clean: footer overlaps (slides 9, 11, 13); slide 9
  heading wraps; slide 12 panel dead space (twice); slide 14 invented fulcrum label and unequal tray headings; cover tag
  wrap and an empty second tag bullet (now "September 2026"); slide 6 donut would have labelled dollars as $M (moved
  to a percent pie); slide 8 axis now in dollars; two typed double hyphens replaced.

## Decisions Made

- Narrow reading: two deliverables, not a canonical-flow project; no web fetch (the 2026-09-15 free-egress word
  @`dfa63b6d92` names that session only), so every SUPPLIED claim stays unverified and is labelled so.
- No Artifact published: publishing is egress off Opal infrastructure without a per-use word.
- `/deck-prompt` Pass 2 picker unavailable in an autonomous run: recommended variants accepted, disclosed in the
  prompt file's trailer.
- Left as-is: the Slide Library's footer logo is navy on the dark slides (2, 10, 16). It lives in the library layout
  every dark slide shares; changing it is an engine change outside this deck.
- Committed from a sparse linked worktree (Rule 14b): the shared tree holds a peer's open drain of
  `wk-amgt-13-26-fpA` (MERGE_HEAD `7aef98df54`, one conflicted path), which this seat did not touch.

- The deck prompt and build script sit in lane DECK, which does not list this seat; safe-commit refused them
  (block mode). They land in a SECOND commit under `GIT_COMMIT_AUTHOR_OVERRIDE=DECK`, audited, citing the
  Andrew-direct record @`12fa905d41` that sent this seat to `deck_generation/`. The report, script, summary and
  this log land first under the normal gate.

## Files Modified

- the five files above and this log, in two commits on branch `cro-z-claude-cost-20260917` (worktree
  `C:/tmp/cro-z-claude-cost`): seat-lane files first, the two DECK-lane files second
- memory: none new this segment

## Blockers

- Merge-back to SITEZ waits on the peer's open drain in the shared tree clearing.

## Current State

Report, measurement script, summary JSON, deck prompt and build script committed on the isolation branch; deck on the
Desktop. Inbox Monitor re-armed (task `bw48bm7ew`) after the 30-minute expiry.

## Next Steps

- Merge the branch back when the shared tree's MERGE_HEAD clears; then remove the worktree.
- Andrew's review of the report and deck.

---

## Second pass, 17:4x-18:2xZ -- rewritten for nontechnical managers, with the payments measured

Andrew-direct (record `ANDREW_DIRECT_20260917_174xZ_...`): the deck reads as if written for a technical audience and
must be spelled out for nontechnical managers; five Claude Max accounts at $200 are the real subscription cost; open
on what was paid against what the work costs at standard prices; include Anthropic's extra-usage charges, read from
the Ramp notices in andrew@opalinvest.com; "last 30 days are fine".

- Deck rebuilt 17 -> 23 slides, all copy rewritten in plain language: a basics slide, a six-term glossary, a
  subscription-vs-API explainer, a method slide, a plain-language data-sovereignty section and a data-journey flow.
  Gate: 23 slides, 0 lint violations, 23/23 coverage. Visual QA over COM renders, fixed and re-rendered until clean
  (cards into the footer bar on two slides, half-empty cards on four, a pie label collision, a 72/73 title mismatch).
- PAYMENTS MEASURED, not assumed: both site-Z gateway identities are `opalbloomberg@opalinvest.com` and the
  allowlist refuses `search_email`, so the mailbox scan was routed to `0.0.0_AB_MSTR~Z` (msgs 23551, 23552) and run
  by the main-fabric seat holding Andrew's mailbox identity. Result (msg 23553): three Anthropic payment notices in
  the window -- $10.04 on 08-26 (extra usage), $200.00 on 08-30, $200.00 on 09-06; $410.04 charged in-window, with
  four more $200 notices just before it. No gateway allowlist was widened and none was requested.
- "What we paid" is therefore $1,010: Andrew's stated five-account rate plus the measured $10.04. Multiple 8.2x,
  discount 88%. An open item is named in the report and on the slide: two of the five accounts show no renewal
  notice inside the window.
- Report rewritten to match: a plain-terms section 0, the payments table, the new per-unit figures, and the laptop
  measurement named as pending.
- Main-fabric token usage requested at 17:45:20Z; the laptop is running the same script and `0.0.0_AB_MSTR~Z` will
  relay. Not folded in yet, and the deck says so.

**Blocked, named:** the laptop's share of the 30 days; the two unexplained subscription renewals.
