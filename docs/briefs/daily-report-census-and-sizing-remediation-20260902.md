# The Daily Operating Report — CENSUS, SIZING AND ENUM REMEDIATION

**Author:** `0.0.0_AB_MSTR` · **UTC:** 2026-09-02
**Authority:** Andrew-direct 2026-09-02 at the MSTR terminal, four numbered items, verbatim:
*"1.) the output formatting as it pertains to automatically detecting/sizing for desktop versus
mobile readers. 2.) any tooling around image insertion. 3.) all references the script uses to tap
into the directives / commits / related substrate necessary for the output. 4.) logic on how
commits are attributed to directives"* — with the reasons given: last night's mobile render was
*"much smaller than usual rather than being large and readable"*; image insertion *"should be
streamlined … a reliable consistent function for this with rules"*; the substrate references
*"need to make sure that this is adequately robust and locked in"*; and the attribution logic
*"both to directives as well as to type of work needs to be reviewed and polished."*

**Rulings taken during the work:** `"Agreed (a)"` (commit_kind is work-type, from files) ·
`"I would have briefs go in a 'Planning' group. I would have logs go in an 'Audit' group."` ·
`"Yes etfs guardrail is a D8 project, not D4"` · `"Operator/decomp/ops dont need to be categories.
Also architecture should be folded into planning."`

**Ledger:** `LD-0504` · `LD-0505` · `LD-0506` · `LD-0507` · `LD-0508`.

---

## 1. VERDICT PER ITEM — the short version

| # | subject | verdict | status |
|---|---|---|---|
| 1 | mobile vs desktop sizing | **NOT the template and NOT generation variability.** One CSS cap in the photo grid disabled the wrap that would have stacked images on a phone | **FIXED** `aa3804301d` |
| 2 | image insertion tooling | The tool exists and is decent. It was **bypassed** — nothing enforces that a referenced shot came from it | **DIAGNOSED, NOT FIXED** |
| 3 | substrate references | **The directive register fed the report NOTHING**, and failed silently for as long as it has been a YAML mapping | **FIXED** `323f185e27` |
| 4 | attribution logic | Directive attribution had 54% unattributed; work-type attribution measured the **author's seat** while wearing work-type names | **FIXED** `323f185e27`, `c67a634b2d`, `87728e42cd`, `c9ea7b3b63` |

---

## 2. ITEM 1 — the page was innocent; the photos were not

**Both stated hypotheses were tested and cleared before anything was written**, because "everything
got smaller on a phone" has a classic cause — one overflowing element makes the browser shrink-to-fit
the whole document — and that cause would have pointed at entirely different code.

`Mobile_DAILY_REPORT_2026-09-01` (the complaint) vs `2026-08-31` (a night that read correctly), both
rendered headless at 390x844:

```
  <style> blocks                 88 lines each, diff CLEAN (byte-identical)
  .headline / .headsub / .sect   26px / 13px / 10.5px   -- IDENTICAL both nights
  document.scrollWidth           390 == viewport on BOTH -> NO zoom-out, NO overflow
  <img> count                    0 (08-31)  vs  3 (09-01)
```

The photos rendered `155x109`, `155x116` and `322x224` from `900`, `900` and `1440` px sources —
**17%, 17% and 22% of natural size.**

**Mechanism, `daily_reports/templates/_shared_viz.js` `screens()`:**

```
  flex: 1 1 260px;   max-width: n===1 ? '100%' : '48%'
```

`flex-basis: 260px` with `flex-wrap: wrap` means *"prefer 260px each, otherwise wrap."* The 48% cap
forces both figures **below** that basis, so they always fit on one line and **`flex-wrap` never
fires.** ⭐ **The cap did not merely shrink the photos — it disabled the one rule that would have
stacked them.** The fix is therefore a REMOVAL (`max-width:100%`), not a breakpoint: the correct
behaviour was already written and was being suppressed.

**Verified after, three cases:** 09-01 mobile — two shots `155px -> 322px`, one per row, no
overflow. 08-28 mobile — three shots, all 322px, one per row. 09-01 desktop 1280px — both figures
still share one row at 274px each.

⚠ **Residual, and it cannot be fixed by layout:** `etf_ownership_aug.png` is **1440x1000**, above
`capture_screens.py`'s own `MAX_W["desktop"] = 900`. At 322px a 1440px desktop UI is still 22%.
See item 2.

---

## 3. ITEM 2 — the tooling is fine; the bypass is the problem

`daily_reports/scripts/capture_screens.py` already does most of what was asked: headless capture
through the portal's own `ui-smoke.mjs`, `--from` to ingest an operator's own photo, downsizing to
`MAX_W = {"desktop": 900, "phone": 420}`, `--crop-height`, and a 400 KB/shot cap the renderer
enforces.

**Three gaps, none of them the tool's competence:**

1. **It was bypassed.** A 1440px shot is in `shots/2026-09-01/` — above the cap it would have been
   downsized to. **Nothing checks that a file named in the JSON came from the tool.**
2. **No single entry point.** The operator runs the script once per shot and then *hand-authors* the
   `viz.params.shots` block. The `frame` value is typed by hand and can silently disagree with how
   the image was actually captured.
3. **`--frame` does not reach the layout.** It picks chrome and the downsize cap only.
   `frame:"phone"` with two shots still got the 48% treatment.

**Recommended shape (NOT BUILT):** one function that takes the item and its shots, captures-or-
ingests, downsizes per frame, **writes the JSON viz block itself**, and **asserts the referenced
file is one it produced.** That closes the bypass and the hand-typed-frame drift together.

---

## 4. ITEM 3 — the register fed nothing, and it failed by going quiet

⛔ **THE SINGLE MOST CONSEQUENTIAL FINDING IN THIS PASS.**

`project_census.py` `load_membership()` read `org/missions/DIRECTIVES.yaml`, did
`list(rows.values())` — **discarding the mapping keys, which ARE the directive codes** — and then
skipped every row lacking a `code:` field, the identity it had just discarded.

**MEASURED: 0 of 13 rows carry a `code:` field.** The register contributed **zero** mappings. The
whole census ran on a PRD-path glob plus 9 hardcoded entries. Of the register's **37** declared
project->directive mappings, **20 were invisible** — including `ETFS_GUARDRAIL -> D8`, committed
that same morning.

⭐ **The failure mode is the lesson: an empty mapping degrades to "unattributed", never to an
error.** Editing `DIRECTIVES.yaml` appeared to work — the file changed, the commit landed, every
gate passed — and changed nothing downstream. **Nothing in the chain could fail, so nothing did.**

Two more in the same function:

- **`LIVE` was a hardcoded `range(12)`** = D0–D11 against a register carrying D0–**D12**. Proven in
  the wild: `org/projects/D12_PHONE_OTP_ALL_AWS.json` sat in the residual **with the directive token
  in its own filename**. A literal cannot track a register that grows.
- **The path arm of the project-code match was a bare substring** (`if code in f`) while the
  subject-line arm of the *same rule* was already `\b`-anchored. Two arms of one rule disagreed
  about what a match is.

**On the other two symptoms Andrew named:**

- **`undefined`** is not in the static HTML — 0 rendered-text occurrences across 8 files. It is
  produced at runtime because the schema declares `"params": {"type": "object"}` with **no per-type
  requirements**; the validator checks `viz.type` against an enum and never the params that type's
  generator reads. **NOT FIXED — see §7.**
- **Missing sections could not be reproduced.** All six committed days carry all nine top-level
  keys (`process` 12–13, `blocked` 2–7, `projects` 12–13), and 09-01's DOM rendered all five section
  headers. Either it predates this data directory or it is a runtime failure — and the unconstrained
  params above are the most likely cause, since they fail silently rather than failing the render.

---

## 5. ITEM 4 — two axes, both wrong, in different ways

### 5a. To directives — 54% of the day was reported as nothing

With the register dead plus `D0_PATHS` missing the estate's largest artifact classes
(`org/tier*_exec/`, `docs/briefs/`, `org/critical_paths/`, `org/audit/`), 09-01 read **158 of 293
commits (54%) UNATTRIBUTED.**

Andrew's ruling created two non-directive **work streams** — `PLANNING` (`docs/briefs/`) and `AUDIT`
(agent-home `logs/`, `drive_log*`), tested BEFORE the project-code match because *a log is a log
regardless of what it mentions.*

⚠ **The axis was renamed to WORK STREAM to keep the ruling Rule-24 legal.** `PLANNING`/`AUDIT`
beside `D0..D12` on an axis *called* "directive" mixes two grains — a directive and an activity
class — which is precisely the defect found in the other axis. Declaring the domain as work streams
makes every value one grain, MECE, residual named. They ship in an additive `by_stream` field
because `by_directive` rows are `[int, title, count]` through the schema, the renderer **and both
templates** (`PCOL[n%12]`); a string id there would break four consumers **silently at render
time**.

```
  2026-09-01, same day, same window, same 293 commits
                    BEFORE (@54e0058551)      AFTER
  UNATTRIBUTED      158  (54.0%)              26  (8.9%)
  D12                 0  (impossible)         61
  D2 / D4 / D0      101 / 5 / 27              103 / 6 / 27
  PLANNING            --                       9
  AUDIT               --                      71
```

**D12 was the second-largest stream of work that day and the report said it did not happen.**

### 5b. To type of work — the mix was a picture of who was awake

`commit_kind` matched the **author string** (`_DT_ -> FRONTEND`, `_SA_(CVO|CRO) -> VERIFICATION`)
while the enum was named for kinds of work. Rule 24 (iii): one axis wearing another's values.

```
  same 293 commits          SEAT-derived     FILE-derived
  VERIFICATION                    65               2
  DATA                            51              11
  BACKEND                         57              19
  ARCHITECTURE                    42               3
```

**Only two commits all day touched a test, battery, probe or certification path.** `VERIFICATION 65`
meant the CVO seat committed 65 times.

⛔ **A reader comparing a pre-2026-09-02 report to a later one is comparing two different
measurements that share a legend.** That warning is recorded in `daily_reports/README.md`, because
the legend is all a reader sees.

**The split was censused, not guessed.** A straight file-derivation put 57% into `COORDINATION`,
which would have replaced a flattering number with an uninformative one. Andrew's question —
*"Coordination is so heavy what accrues there exactly?"* — forced the subdirectory census that made
the split correct:

```
  agent-home deliverables/  102 touches  -> DELIVERABLES
  agent-home task_orders/    53          -> COORDINATION (dispatch, which is what the word means)
  org/critical_paths/        24          -> GOVERNANCE
  org/projects/ + org/tier0/ 30          -> GOVERNANCE
  agent-home drive_pairs/    14          -> COORDINATION
```

**The bucket was heavy because it held four different activities.** Splitting on a guess would have
produced plausible names over the wrong boundaries.

**Final enum — 10 values + a named residual**, after Andrew retired `OPERATOR`, `DECOMP` and `OPS`
and folded `ARCHITECTURE` into `PLANNING`. Retiring `OPERATOR` removed the enum's only
author-derived value, so `classify()` no longer reads the author at all and postulate (ii) holds
without exception.

```
  09-01: FRONTEND 3 · BACKEND 19 · DATA 11 · VERIFICATION 2 · PLANNING 14 · DELIVERABLES 82
         COORDINATION 44 · GOVERNANCE 29 · AUDIT 69 · TOOLING 17 · UNATTRIBUTED 3 (1.0%)
```

Two placements were **this seat's calls, not Andrew's**, and are marked as such in the README so
either reverses independently: `workflows/` -> PLANNING, `org/critical_paths/` -> GOVERNANCE.

---

## 6. ⛔ THE PATTERN THAT RECURRED — including against the seat writing this

Four instances of one class in a single afternoon. **Three of them were self-inflicted, by the seat
that had just documented the class.**

| # | instance | how it was caught |
|---|---|---|
| 1 | `if code in f` — bare substring in the project-code match | reading the source |
| 2 | `certification` — bare substring, matched inside a **session-log filename**, classifying a log as VERIFICATION. **Written an hour after fixing #1** | comparing the two axes' AUDIT counts and chasing a 2-commit delta instead of accepting it |
| 3 | `decision_type: correction` — an **invented value against a closed enum**, in the ledger entry recording #2, by the seat that spent the afternoon enforcing Rule 24 on someone else's taxonomy | the `mstr-ledger-check` gate |
| 4 | The first repair for #2 — hoisting agent-home rules above content rules — **was worse than the bug**: AUDIT 69 -> 85 while BACKEND, DATA, COORDINATION and TOOLING drained | re-measuring after the change |

⭐ **#4 is the one worth carrying.** The reorder's justification was a true sentence — *"an artifact
is typed by what it is, not what it mentions"* — and it would have shipped on the strength of that
sentence alone. **A one-file regression is repaired by anchoring one regex, not by reordering a
ladder that decides the answer for every multi-file commit in the estate.**

**And the tie-break beneath it was silently arbitrary:** `Counter.most_common` is insertion-ordered,
so a commit touching one deliverable and one log resolved to whichever path `git log` happened to
print first. Same commit, different listing, different answer, **and nothing in the output would
have shown it.** Ties now break on declared rule order, with AUDIT placed last because *a session
log is a byproduct of the work, not the work* — a placement worth 15 commits on one day.

**A fifth, of a different kind:** a `safe-commit` refusal was followed by a `git push` that moved
the branch ref — because the push carried **another agent's** local commit. The commit looked
landed and had not. Asking the repository (`git log -1 <hash>` plus a negative control) rather than
reading the tool's stdout is what caught it.

### RETRACTION on the record

This seat told Andrew **twice** that aligning the two axes' `AUDIT` counts was "one line." **It was
not.** Coverage was genuinely missing on the stream side (`drive_log*` at the agent-home root) and
that is fixed (58 -> 71). But the residual gap — **stream 71, kind 69** — is **structural**:
`project_census` tests its stream rules FIRST (a log must beat a code it mentions);
`commit_census` tests `AUDIT` LAST (a log must lose to the work it documents). **Both orderings are
correct for their own question, and forcing the numbers to match would break one of them.** The two
axes are not required to agree and the report must not imply they are.

---

## 7. WHAT REMAINS — ranked, none blocked

1. **Wire the renderer, schema and both templates to `by_stream`.** Planning and Audit are computed
   and committed but appear NOWHERE on the page. **Andrew's ruling is landed and invisible.**
2. **Per-type viz params in the schema**, so a missing param FAILS the render instead of printing
   `undefined` in the browser. Closes the last unaddressed half of item 3 and is the most likely
   cause of the missing sections that could not be reproduced.
3. **The single image-ingest function** with the provenance assertion — item 2, and what would have
   caught the 1440px bypass.
4. **Commit 09-01's JSON, shots and renders** — currently untracked. The day that prompted this has
   no committed record; it was published to S3 and never landed.

**Open at Andrew:** whether to re-publish 09-01 with the photo fix (rec: leave it — silently
changing what a shared link renders is worse than a bad night on the record); and **8 of the 26
work-stream residual commits are PRODUCT work** — `infra/aws` (3), `portal` (2), `data/etfs` (2),
`infra/system` (1) — with no directive claiming them, which is a register gap rather than process
leftovers. The other 18 are agent homes, `org/critical_paths/`, `org/tier0/`, `org/audit/` and
`docs/references/`.

⚠ **The residual figure moved twice while this brief was being written** — 27 -> 26, because the
`drive_log` coverage fix landed between the two readings, and the product-work count was **5 in an
earlier draft and is 8** because that draft counted only `infra/aws` and `data/etfs` and missed
`portal` and `infra/system`. **A number quoted from an earlier turn is not a measurement**; both
were re-derived against `@c9ea7b3b63` before this file was committed.

---

## 8. COMMITS

| commit | what |
|---|---|
| `323f185e27` | register key + `LIVE` from the register + word-bounded path match + `by_stream` (LD-0504) |
| `aa3804301d` | the `screens` mobile cap (LD-0505) |
| `c67a634b2d` | `commit_kind` file-derived + COORDINATION split + Rule-24 record rewritten (LD-0506) |
| `87728e42cd` | OPERATOR/DECOMP/OPS retired, ARCHITECTURE folded into PLANNING (LD-0507) |
| `c9ea7b3b63` | anchored `certification`, deterministic tie-break, stale carriers in the source file (LD-0508) |

All on `origin/CLOUD` (`git ls-remote` read; negative control on a bogus hash fails).
