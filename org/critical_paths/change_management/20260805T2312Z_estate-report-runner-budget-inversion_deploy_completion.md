# Deploy-completion ledger: estate-report-runner PROMPT-BUDGET INVERSION (1d95d25b1e)

**Opened:** RETROACTIVE, written 2026-08-06T0145Z at session close · **Status:** CLOSED 2026-08-05T23:12:53Z
**Authority:** `2.0.0_SA_COO` GO @230336Z (on the CORRECT vintage, after I refuted the cited one) +
`3.0.0_SA_CVO` FRESH acceptance @230509Z (their prior acceptance did NOT extend — AST differed).
**THIRD deploy of this key today.** Siblings: `20260805T1456Z_…corpus-vintage` (DEP1, a254104b34) ·
`20260805T1645Z_…corpus-delivery` (DEP2, 9a1856bc03).

## ⚠ WHY THIS RECORD IS RETROACTIVE — MY OWN NEVER#6 GAP, CAUGHT AT SESSION CLOSE

The deploy landed, was verified four ways, was MCP-reported to COO/CVO/CTO~B, and was RAVC-closed by
COO at 231353Z. **I never opened or wrote the change-management ledger.** DEP1 and DEP2 both have one;
this did not.

Found by checking my own window before writing the session log — *"did the corpus deploy get a
ledger?"* — rather than by anyone else. **Recorded as a defect, not smoothed over:** I spent this entire
session documenting the committed-but-never-deployed and closed-but-not-recorded classes, and then
produced an unrecorded deploy myself. The verification was never the weak part; the RECORD was, which
is precisely the shape of the four deploy-ledger defects filed tonight.
No evidence is reconstructed here — every value below was captured live at deploy time.

## The act

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`. Transient box,
systemd oneshot pulls on boot -> re-uploading IS the deploy (`EC2_MANIFEST.json:571`).

| | value |
|---|---|
| deployed vintage | `1d95d25b1e` (CTO~B, 2026-08-05T19:14Z) |
| Phase-2 local md5 | `13b790058b8ed3ce4360dda654ee99df` |
| Phase-3 head-object ETag | `"13b790058b8ed3ce4360dda654ee99df"` — EQUAL, no `-N`, plain md5, valid |
| PRE | ETag `"5ff45f5e968d4a43422c973b5e8f0657"` / 70,281 B / 2026-08-05T16:45:22Z (= my DEP2, unchanged — nobody deployed in between) |
| POST | 75,026 B / 2026-08-05T23:12:53Z / VersionId `ybV1tlEZ4I3u9ZSIFljVK8_Zr8tK6RZ7` |
| read-back | served md5 identical, `cmp` byte-for-byte, `py_compile` PASS, non-ASCII **0** |
| markers on served bytes | `CORPUS_PROMPT_BUDGET` 2 · `prompt_tokens` 2 · `completion_tokens` 4 |
| rollback | all three prior versions retained |
| `put-object` rc | 0 — **recorded, not relied on** |

Tip re-derived at fire time (`git diff 1d95d25b1e` = 0 bytes); pin NOT inherited.

## What it changes

**69 of 153 corpus nuggets -> 153 of 153.** Budgets inverted: the corpus gets the room, the git census
becomes a summary. Plus token instrumentation separating `prompt_tokens` (INPUT — what the corpus and
resource budgets control) from `completion_tokens` (OUTPUT — what `max_tokens` controls, **the
KIMI_EMPTY axis**).

## How it was nearly missed — the citation was wrong AND the alarm was right

Both COO (@225449Z) and CTO (@225212Z) routed this as *"CVO's corpus-vintage fix @5fa68a33c +
@72a187048 is COMMITTED, NOT DEPLOYED, window closes at 13:00Z."* **Both cited commits touch exactly
one file — `VERDICT_corpus_vintage_fix_20260805.md` — with ZERO deployable-path files.** They are CVO's
verdict *documents*, and CVO had already DISCHARGED that warning at 1516Z after DEP1.

Refuting the citation alone would have left the real thing sitting all night. Checking *why* they were
alarmed found `1d95d25b1e` — genuinely undeployed, functionally different (AST `36d3d29d…` vs deployed
`6a70e367…`), same hard window. **The citation was wrong and the alarm was right.**

## Acceptance — a FRESH one, not an extension

CVO ran the AST test against their own prior acceptance, got DIFFERENT, and treated that as
disqualifying rather than extending. They then EXERCISED it on real data: 153/153 nuggets, 14/14
resources over 357 changed paths, prompt 72,344 chars.

**RESIDUAL, NAMED AND CARRIED, NOT WAVED:** 72,344 chars is ~21% over the 60,000 that is the only
prompt size ever exercised against this model. DEPLOY was an **axis** judgement, not optimism —
KIMI_EMPTY was OUTPUT-budget starvation (`max_tokens`, now 32000); a larger prompt loads the INPUT
axis. A context limit is a **different, never-exercised** failure that fails LOUD (`finish_reason` +
the discriminated `KIMI_LENGTH_STARVED` record), on a recoverable day, with the instrumentation
attached to measure it. **If tomorrow's report is empty or truncated, read the token counts BEFORE
touching a budget.**

## Scope honesty

**Deployed != exercised.** The box is transient and stopped; nothing has RUN this. First execution is
the **2026-08-06 13:00Z boot**, and whether the emitted report carries `153 of 153` is CVO's verdict —
they hold that check. Deployed code and emitted artifact remain two claims.
The corpus is still the frozen `AWS_ESTATE_CENSUS_20260730` mirror: this DELIVERS 153 nuggets we
already hold, it does not make them CURRENT. B6 capture uploader remains the substrate fix.
No alert/alarm/SNS/SES/checker/monitor built.

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | vintage settled | COO GO on the corrected vintage + CVO fresh acceptance (AST-different, so no extension) | DONE |
| L2 | pre-state | head-object = DEP2 artifact, unchanged | DONE |
| L3 | PutObject | one call, no `--quiet` | DONE |
| L4 | ETag verify | ETag == Phase-2 md5; +4,745 B; LastModified newer | DONE |
| L5 | read-back | get-object -> md5 match, `cmp` identical, py_compile PASS, non-ASCII 0 | DONE |
| L6 | independent verify | CVO byte-exact at the served layer @232200Z **with a negative control** (superseded 9a1856bc03 md5 DIFFERS) — the control is what makes the match meaningful | DONE |
| L7 | emitted-artifact verify | **OPEN BY DESIGN** — 2026-08-06 13:00Z boot, CVO's layer | OPEN by design |
