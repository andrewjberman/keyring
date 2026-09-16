# Rising energy cost and rising yields were filed BULLISH -- the prompt was enforcing the wrong sign, not causing it -- 0.1.0_DS_MarketIntelligence

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), IMPLEMENT, VALIDATE

**Date:** 2026-09-16 (UTC; Andrew's direction landed 2026-09-15 local / ~02:0xZ 2026-09-16)
**Task Order:** ad-hoc / Andrew-direct -- news scanner analysis-layer direction defect
**Status:** COMPLETE (committed local; NOT deployed -- routing call open at Andrew)

---

## Objective

Andrew-direct: the news scanner paints "energy cost going up" and "yields increasing" as BULLISH.
Both are virtually always BEARISH -- energy up is supply push (war, sanctions, OPEC cuts), not
demand pull; yields up is a bond selloff (inflation concerns, loss of faith in the dollar). He
suspected "the sentiment scorers and GPT are seeing 'increasing' and getting the wrong idea" and
expected a surgical edit near the sports ban. Find the real cause and rectify it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find (aws corpus) | `comp-find 'news-layer3-curation' --corpus aws --limit 20` | PASS | 5 hits / 2529 aws nodes. Confirmed live `opal-news-layer3-curation` code_sha `bWvoG+WeKBa/...` == `d6913f1e9b` -- GRAIN proof the edited file IS the deployed bytes. Also surfaced the `semantic-news-layer3-curation` sibling + its CW alarm |
| comp-tool rail (hud) | 3 denials during the window | PASS (all correct) | see Gap found |
| .tools/commit-gate.sh | on the edited `.py` | PASS (after 1 real catch) | caught a dead `avg_sentiment` my own edit orphaned (ruff F841). A genuine defect, not gate noise |
| .tools/safe-commit.sh | `-F` msgfile, DS author line | PASS | `ed1a036b2b`; `[msg-verify] MATCH len=4416` |
| scratchpad `verify_macro.py` | py_compile + ASCII delta + 23 behavior cases | PASS | 0 failures; non-ASCII delta vs HEAD = 0 |
| native Grep / Glob / Read / sed | file census + targeted reads | PASS | single-file reads via `sed`, censuses via native Grep (both off-rail by carve-out) |

**What worked:** `comp-find --corpus aws` settled the GRAIN question in one call -- it printed the
live code_sha, which matched the hash my 2026-09-11 log recorded, proving I was editing deployed
bytes rather than a stale sibling. That is the check that would have been skipped on recollection,
and the repo holds TWO layer3 curation lambdas that a filename read alone cannot separate.
The commit gate earned its keep: it caught a variable my own edit had orphaned.

**What failed:** nothing returned a wrong answer this window.

**Gap found:** three, all real.
1. **`/watcher` and `/log` both hardcode `/c/Users/AndrewBerman/...`** as the anchor path. That is
   the OTHER device. On site Z the root is `/c/Users/Opal Bloomberg/Desktop/ajb_workspace`, and
   `cd`-ing to the skill's literal path fails. Measured, not inferred; both skills were run tonight.
2. **Memory `site-z-is-a-second-device` is STALE on the mount axis.** It asserts `/cygdrive/c` is
   the live mount and `/c` is ABSENT unless a `mount -f` is in effect. Measured tonight with both
   arms plus a negative control: `/c` DIR-EXISTS, `/cygdrive/c` ABSENT -- the exact inverse. The
   live peer watcher processes corroborate (`0.0.0_AB_MSTR~Z` streams run under `/c/...`). The
   memory's own instruction (measure, never copy a path out of a doc) is what caught it.
3. **comp-find rail denies a piped receiver even when the pipe is only truncating**
   (`| head -30`, `| sed -n '1,12p'`) because the receiver can erase the denominator. Correct
   behavior, and the native `--limit` is the answer -- but it cost two retries. Separately, the
   documented compound-call hazard hit once: a single Bash call chaining `sed` + a standalone
   `grep` was denied on the grep segment and **both** segments were lost.

---

## Work Completed

### 1. DIAGNOSE -- the defect is upstream of GPT, and the prompt was enforcing it

`infra/aws/lambda/news_layer3_curation/lambda_function.py` assigns direction **before GPT is ever
called**, from the sign of the mean FinBERT score (`prefilter_topics_by_finbert`, gated by
`BULLISH_FINBERT_MIN = 0.0` / `BEARISH_FINBERT_MAX = 0.0`). FinBERT scores the VERB: `surge`,
`climb`, `rising`, `increasing` are positive tokens in a generic financial-sentiment model, so
"oil prices surge" and "treasury yields climb" land in the **bullish pool**.

The curation prompt then makes the wrong sign unreachable by prompt, verbatim:

> "THE SORT IS GIVEN. FIND THE NARRATIVE THAT CARRIES IT. ... Do not re-file, re-rank or argue
> with the direction. It is given."

So GPT was being **ordered** to manufacture a bullish narrative for a bearish fact. Andrew's read
of the mechanism ("seeing 'increasing' and getting the wrong idea") is correct; the wrong idea was
locked in before the model saw the topic, and the prompt defended it.

**In-repo corroboration of the same class**, already recorded at the DIRECTION-CONSISTENCY GATE
note (`:215-231` @`d6913f1e9b`): topic "china oil demand" filed BULLISH on five articles scoring
-0.974/+0.874/+0.947/+0.950/-0.975 -> mean +0.164. The two articles actually about China's oil
demand said it was FALLING 8.9%. That note states the doctrine this fix applies: *"A prompt rule
alone is unenforced; the consuming half is the mechanism."*

### 2. IMPLEMENT -- one helper, read by every direction consumer

Added beside the crypto/sports ban constants (the area Andrew named):

- `_MACRO_INVERT_SUBJECT_RE` -- energy (oil, crude, brent, wti, opec, gasoline, natural gas,
  diesel, heating oil, energy costs, barrel) + rates (yield(s), treasury yields, 10-year, 2-year,
  30-year, borrowing costs, term premium, gilts, jgb, bund).
- `_MACRO_RISING_RE` -- rise/rising/surge/climb/jump/spike/soar/gain/increase/increasing/higher/
  record high/elevated/escalate etc.
- `_MACRO_EQUITY_EXEMPT_RE` -- stocks/shares/equities/etf/dividend yield/buyback. "energy stocks
  rally" is a real equity move, not a cost shock; "dividend yield" is not a bond selloff.
- `_macro_inverted_direction(topic)` -- returns `'bearish'` only when SUBJECT and MOTION appear in
  the **same text unit**. Keyword first, then the leading 3 headlines (the sports filter's shape).
  The same-unit requirement is deliberate: matching "oil" in a keyword against "rises" in an
  unrelated headline is precisely the loose-match failure the DIRECTION-CONSISTENCY note records.
- `_apply_macro_direction_override(topic)` -- stamps `effective_sentiment = -abs(finbert)`,
  `direction_override`, `direction_override_reason`. **`avg_sentiment` is left untouched** -- it is
  the measured FinBERT value and the stored record keeps it; the override carries its own claim and
  reason so a consumer can reject or audit it. Idempotent (prefilter and backfill both reach it).
- `_effective_sentiment(topic)` -- the single value every direction consumer now reads.

**Applied at all THREE consumers** -- a fix at one is not a fix:

| # | Site | Change | Why it had to be covered |
|---|------|--------|--------------------------|
| 1 | `prefilter_topics_by_finbert` pools | built on `_effective_sentiment`; override runs BEFORE composite scoring | ordering is load-bearing: run it AFTER scoring and the refiled topic ranks on its raw POSITIVE FinBERT at the BOTTOM of the bearish pool and is never selected -- the fix present but inert |
| 2 | `calculate_composite_score` | ranks on the corrected sign; None-guard still reads the RAW score | absence of FinBERT data must stay the skip condition; only the direction-bearing value moves |
| 3 | `add_backfill_topics` | mirrors the override | without it a topic dropped from the bullish pool RE-ENTERS as bullish via backfill -- exactly how crypto topics leaked back in before the ADHC_CRYPCT.001 hotfix in this same function |

Plus two narrative surfaces so the write-up matches the corrected file: a MACRO DIRECTION block in
the prompt's relevance section (beside the sports ban) and a per-topic `MACRO_INVERSION` marker in
`format_topic`, mirroring the existing `EARNINGS_TRANSCRIPT_CLUSTER` marker -- otherwise the model
is handed "FinBERT: +0.820" on a topic sitting in the bearish pool with no explanation.

### 3. VALIDATE -- 23 of 23, negative controls included

| Arm | N | Result |
|-----|---|--------|
| Positive (must refile bearish) | 11 | PASS -- oil/crude/brent/gasoline/natgas/treasury yields/10-year/bond yields/borrowing costs, incl. Andrew's exact phrasing "energy costs increasing", and one subject-in-keyword/motion-in-headline case |
| Negative controls (must NOT fire) | 10 | PASS -- falling arm untouched ("oil prices fall", "yields decline"), equity exemption ("energy stocks rally"), income exemption ("dividend yield rising"), unrelated subjects, motion-without-subject, subject-without-motion |
| Cross-text-unit guard | 1 | PASS -- "oil" keyword + "Nvidia shares rise" headline does NOT match |
| End-to-end pool move | 1 | PASS -- avg_sentiment +0.820 -> effective -0.820; OUT of bullish pool, INTO bearish; raw value preserved |
| Idempotency (prefilter+backfill) | 1 | PASS -- second application does not flip the sign back |

`py_compile` clean. `.tools/commit-gate.sh` clean. Non-ASCII delta vs HEAD: **0** (file carries 19
pre-existing non-ASCII lines, WARN-only; I added none).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix at pool assignment, NOT the prompt | The prompt explicitly orders GPT to keep the given sort. A prompt rule cannot reach a sign decided before the call -- and the file's own doctrine says the consuming half is the mechanism |
| Scope is ONE-DIRECTIONAL: rising only | Andrew asserted the RISING arm only. Falling energy/yields may be disinflation OR demand destruction, so the converse is NOT symmetric. CLAUDE.md: relay verbatim scope, never adjudicate wider or narrower. Flagged to him as an open call rather than assumed |
| `avg_sentiment` preserved; new `effective_sentiment` field | The raw FinBERT score is the measured value and the stored record must keep it. The override is a separate field carrying its own reason (A VALUE MUST CARRY ITS CLAIM) |
| Override BEFORE composite scoring | After scoring, a refiled topic sorts to the bottom of the bearish pool on its raw positive score and is never picked -- DESIRED-not-APPLIED |
| Equity/income exemption included | "energy stocks rally" and "dividend yield rising" would otherwise trip the subject regex and be wrongly refiled bearish |
| Did NOT deploy | `deploy.sh` uses `aws lambda update-function-code`, which CLAUDE.md bans outright (Terraform only). Landing this needs Andrew's routing call |
| Did NOT patch the `semantic-news-layer3-curation` sibling | It carries the same defect shape but writes `semantic-news-trending-daily`, not the portal's `opal-news-trending-daily`. Named as a CANDIDATE second surface, not a finding |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | Macro direction inversion: 3 regex lexicons + 3 helpers; applied at prefilter pools, composite scoring and backfill; prompt block + `format_topic` marker; removed the `avg_sentiment` local my edit orphaned | Yes -- `ed1a036b2b` (185 insertions, 10 deletions) |

---

## Briefs Written

None this window -- the ask was a surgical code fix on a live Lambda, not a hand-off spec. The
commit message carries the full rationale and evidence for the next reader.

---

## Blockers

None BLOCKED. The code work is COMPLETE and landed. Three items are OPEN CALLS AT ANDREW, not
blockers -- each is a decision that is his, and the work does not proceed correctly by assumption:

1. **Falling arm** -- deliberately not implemented (see Decisions). Needs his word.
2. **Deploy route** -- the repo's own `deploy.sh` path is banned by CLAUDE.md. Needs his routing call.
3. **`semantic-news-layer3-curation`** -- candidate second surface; needs his word to chase.

---

## Current State

`infra/aws/lambda/news_layer3_curation/lambda_function.py` at `ed1a036b2b` (branch SITEZ, LOCAL --
`origin/SITEZ` is `34575aaded`, ls-remote read 02:16:48Z; push is integrator-only) now refiles a
RISING energy-cost or RISING-yield topic from the bullish pool to the bearish pool BEFORE the GPT
curation call, via `_macro_inverted_direction()` / `_apply_macro_direction_override()` /
`_effective_sentiment()` defined next to `BULLISH_FINBERT_MIN`. Those three helpers are read at
`prefilter_topics_by_finbert` (pool construction), `calculate_composite_score` (ranking) and
`add_backfill_topics` (backfill re-entry). `avg_sentiment` is unchanged on the topic dict and the
DynamoDB record; the correction rides `effective_sentiment` + `direction_override` +
`direction_override_reason`. The prompt gained a MACRO DIRECTION block beside the sports ban, and
`format_topic` emits a `MACRO_INVERSION` marker on any overridden topic.
**The change is NOT deployed.** Live `opal-news-layer3-curation` still runs code_sha
`bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=` (== `d6913f1e9b`, comp-find `--corpus aws`, vintage
2026-09-16T00:55:21Z), i.e. the pre-fix bytes; it writes DynamoDB `opal-news-trending-daily`.
`deploy.sh` cannot be used as written -- it calls `aws lambda update-function-code`, banned by
CLAUDE.md (Terraform only).

---

## Next Steps

1. **[Andrew] Rule on the FALLING arm** -- should falling energy / falling yields be forced BULLISH?
   I did not assume the converse: falling oil is often demand destruction, which is bearish too.
2. **[Andrew] Rule on the deploy route** -- `deploy.sh` uses the banned
   `aws lambda update-function-code`. Either authorize that path explicitly for this Lambda, or
   route the code deploy through Terraform.
3. **[0.1.0_DS_MarketIntelligence] On his word, land the deploy and read the next scheduled run** --
   acceptance is a topic whose keyword carries rising energy or rising yields appearing in the
   BEARISH list with a cost-shock/selloff topline, plus a `WARN: MACRO INVERSION` line in the
   Lambda log naming the refiled keyword and its FinBERT score.
4. **[0.1.0_DS_MarketIntelligence] Confirm whether anything reads `semantic-news-trending-daily`** --
   the sibling Lambda is live in AWS with the same FinBERT-sign pooling defect (`:352-353`). If a
   consumer exists, it needs the same fix; if not, it is a retirement candidate.
5. **[0.0.0_AB_MSTR~Z] Carry `ed1a036b2b` when the site-Z push question clears** -- it is one file,
   no gitlink, no conflict surface.
6. **[0.1.0_DS_MarketIntelligence] Bank the site-Z mount correction to memory** -- the
   `site-z-is-a-second-device` entry has the `/c` vs `/cygdrive/c` axis inverted relative to
   tonight's measurement.
