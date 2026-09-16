# ANDREW-DIRECT 2026-09-16 ~17:3xZ -- "the sprint lambda didn't generate any fields": diagnosed, fixed, republished

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the turn it was executed.
**Ledger:** `org/tier0/ledger/LD-0575.md`.

## VERBATIM AND ENTIRE

> "The sprint lambda didnt actually generate any fields, everything is empty and not filled in. Go look at it and
> figure out why that is. My suspicion is that the AI call ran out of tokens or wasn't properly governed or
> something. I do not want to make an overly complex ai implementation here. ideally we could just give it x amt
> of tokens (more) for read, and y amt for write, with maybe a fallback z if a deterministic analyzer of the y
> write shows it is unfinished and then z is basically "finish the unwritten parts within budget from cached x and
> y context" or something like that."

## THE ANSWER

Not tokens. The model's write was complete: the served page's embedded JSON carried 1281 fields and 0 empty ones.
The page was blank because the browser's own JavaScript threw on ONE field at view time
(`TypeError: p.footer.map is not a function`): the model wrote a flow diagram's `footer` as a sentence where the
generator expects three-field rows, and every section after the headline never rendered. The render-time contract
checked that the field was PRESENT, never its TYPE, and had skipped positional rows by design.

The same defect is in the committed 2026-09-11 report's DATA (two items), the cloud's last published page before
this one. **Correction, same seat, 17:5xZ:** an earlier line here said that served page "is blank the same way";
that was inferred, not measured. Opened headless, the served 2026-09-11 page has 0 JavaScript errors and its
projects, process and blocked sections filled (3 diagrams). It does not go blank. The "still owed" item below is
withdrawn accordingly.

## WHAT CHANGED (repo-side; no image, no model, no token knobs)

- `daily_reports/scripts/viz_contract.py` derives `array_params` and `positional_rows` from the generator source
  (flow.footer = 3 scalars [label, value, tone]; stages, rows, cells, cols, steps, shots, leaves are lists); the
  self-test pins them and bounds over-firing.
- `daily_reports/scripts/render_daily_report.py` refuses a scalar where the browser iterates and a positional row
  shorter than its arity, with the VALIDATION FAILED header the cloud run's repair pass acts on.
- Arms: the served cloud JSON -> refused on footer; a 2-field row -> refused; 14 committed reports -> 13 clean, the
  one refused is 2026-09-11 with the same real defect. Commit 6c4f6ac52a, on origin.

## REPUBLISHED (invoke RequestId 05928f34, 17:48-17:51Z, clone 6c4f6ac52a)

The model chose a screenshot diagram again; the renderer refused with the header; one repair pass; clean render;
PUBLISHED 2/2 pages, 47826 B, ETag b965293787ca, publisher read-back MATCH x2. Opened headless: 0 JavaScript
errors, 7 diagrams, all sections filled (15 directive cards), 0 "undefined", 0 NaN.
Served: https://mcp.opalinvest.dev/sprint/2026-09-15 (Desktop and Mobile).

## ON THE x / y / z DESIGN

Not built, because the failure was not a budget. The handler already has that shape: x = the whole prompt (schema,
derived contract, the day's commit subjects); y = the model's default output cap, and a truncated write cannot
publish (json.loads raises); z = ONE repair pass fed the renderer's exact refusal, with the prior prompt and output
as context. The "deterministic analyzer" is the renderer; its gap was a missing type check, now closed. Explicit
read/write budget env vars would be a one-line image change plus a rebuild; offered, not done.

## STILL OWED (named, not done)

- (withdrawn -- see the correction above: the served 2026-09-11 page renders.)
- The image-side belt from LD-0574 (forbid the screenshot diagram in the cloud prompt) still stands; both cloud runs
  today needed the repair pass for it.
