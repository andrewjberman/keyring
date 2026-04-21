# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-04-21
**Task Orders:** MKOV_CLOUD.001.daily-cloud-fix (ad hoc, from Andrew)
**Branch:** CLOUD
**Input:** Andrew flagged Daily Cloud widget rendering only 2 keywords in this morning's 07:16 ET refresh.

---

## Summary

Root-caused a positive-feedback loop in `news-trending-analysis` Lambda that shrank the Daily Cloud from ~30-40 keywords to 5 over the last ~week, intermittently producing empty output. Fixed in code and reset the contaminated S3 config. Daily Cloud re-invoked and now has 39 keywords.

---

## Root Cause

`gpt_validate_keywords()` in `news_trending_analysis/lambda_function.py` used GPT-4o-mini to flag "junk" keywords. Every flagged keyword was **permanently appended** to `s3://opal-data-portal-v2/config/dynamic_stopwords.json`, and the next Lambda run pre-filtered against that accumulated list before GPT validation even ran.

Over ~3 months since introduction, the stopwords file grew from 0 to **1,207 entries**. Many were legitimate market topics swept up by GPT misfires: `fed chair`, `fed chair powell`, `earnings call`, `anthropic amazon deal`, `bitcoin etf filings`, `federal reserve announcements`, etc. (123 entries match obvious market terms by substring alone.)

Stacked on top: GPT-4o-mini occasionally tantrums. Trajectory of GPT filter rejections in the last 14 days:

| Date | GPT filter (in → out) |
|------|----------------------|
| 4/07 - 4/16 | Normal, 30-46 → 28-46 |
| **4/17 17:16** | **35 → 0** (empty Daily Cloud) |
| 4/18 - 4/20 | Degraded, 23-38 out |
| **4/21 07:16** | **42 → 5** (screenshot Andrew flagged) |

## Work Done

### 1. Code fix — Lambda guardrail + kill auto-learn (committed)

File: `infra/aws/lambda/news_trending_analysis/lambda_function.py`

- Added module constant `MAX_GPT_FILTER_RATIO = 0.30`.
- In `gpt_validate_keywords`, added a guardrail: if GPT flags > 30% of candidates as junk, log a warning and discard GPT's judgment for this run (return unfiltered list).
- Removed the `dynamic_stopwords.update(junk_keywords)` + `save_dynamic_stopwords(dynamic_stopwords)` auto-learn block.
- Kept `load_dynamic_stopwords()` / `save_dynamic_stopwords()` function definitions — pre-filter at line ~1455 still consumes S3 file, now manually curated.
- Updated docstring to reflect that filter is in-session only.

### 2. S3 stopwords file reset

- Archived prior state (1,207 entries, 29 KB) to `org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/dynamic_stopwords_archive_2026-04-21.json` for audit trail.
- Uploaded empty list to `s3://opal-data-portal-v2/config/dynamic_stopwords.json` with a `note` field documenting the reset.

### 3. Lambda re-invoke to regenerate today's output

- Invoked `news-trending-analysis` (StatusCode 200) with an empty payload.
- **Output: 39 keywords** (up from 5 this morning), 100 trending clusters, 7,366 articles scanned.
- A scheduled EventBridge run (at 08:41 ET, between my reset and my invoke) re-polluted the stopwords file to 13 entries because the deployed code still has the auto-learn loop. My re-invoke added 2 more, bringing it to 15. After DT deploys the fix, the file will stop growing; I'll reset once more post-deploy.

### 4. CloudFront invalidation

- Distribution `EVTSA9VEHNZVH` (domain `d2n2nzpeqf34ge.cloudfront.net`, origin `opal-data-portal-v2`), path `/api/general/sentiment/keyword-sentiments.json`.
- Invalidation ID: `ICAK7QECU4S8YD9P0YP1CDSYRC`, status `InProgress` at submission.

### 5. Curation of the pre-existing banned list (Andrew ad hoc)

After the initial reset to empty, Andrew asked to review the 1,207 archived banned phrases and unban the obvious market topics that should never have been filtered.

Three-way partition applied to the archived list:

- **UNBAN (781 legitimate market topics):** `anthropic amazon deal`, `chair jerome powell`, `fed chair powell`, `earnings preview`, `bank of america earnings`, `bitcoin etf filings`, `canva ai pivot`, `tim cook transition`, `starmer mandelson scandal`, `spirit airlines liquidation`, `super micro stock`, `baird lowers`, `blue owl`, `cef downgrades`, `davos switzerland`, `artemis ii mission`, `trump iran oil`, `drug cartel leader`, `stock analyst estimates`, `retail earnings forum`, `prediction market bill`, ~760 more.

- **KEEP BANNED (427 confirmed junk):** sports (NFL/NBA/MLB/NHL teams, recruits, tournaments, playoffs, ~250 entries), entertainment (oscars, grammys, bafta, kardashian, pokemon), lifestyle (affordable travel, aging in place, gift guides), fragments (`the end`, `as part`, `a bull`), news boilerplate (`bbc world service`, `further reading`, `news bulletin`).

Uploaded the curated 427-entry list to `s3://opal-data-portal-v2/config/dynamic_stopwords.json` replacing the prior contaminated 15-entry version. Curated file archived at `org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/dynamic_stopwords_curated_2026-04-21.json` for audit.

Summary:
- 2026-04-21 07:16 ET: 1,207 entries (auto-accumulated contamination)
- 2026-04-21 08:40 ET: 0 entries (reset)
- 2026-04-21 08:43 ET: 15 entries (re-polluted by scheduled run + my re-invoke; deployed code still has auto-learn)
- 2026-04-21 09:00 ET: **427 entries** (manually curated — confirmed sports/entertainment/lifestyle/fragments/boilerplate kept; 781 legitimate market topics + 8 of the 15 recent accumulation unbanned)

Partition logic lives in `.runtmp/partition_v3.py` (gitignored). Partition outputs in `.runtmp/partition_v3.json`.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Daily Cloud GPT filter fix + deploy steps | `docs/briefs/devops-brief-daily-cloud-gpt-filter-guardrail.md` | DT 0.1.0_DT_MarketIntelligence |

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/lambda/news_trending_analysis/lambda_function.py` | Added 30% GPT filter guardrail; removed auto-learn of dynamic stopwords. |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/dynamic_stopwords_archive_2026-04-21.json` | New — archive of the pre-reset 1,207-entry list. |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/dynamic_stopwords_curated_2026-04-21.json` | New — the 427-entry curated replacement. |
| `docs/briefs/devops-brief-daily-cloud-gpt-filter-guardrail.md` | New — deploy brief for DT. |

S3 writes (not git-tracked, but owned by this session):

| Key | Change |
|-----|--------|
| `s3://opal-data-portal-v2/config/dynamic_stopwords.json` | 1,207 entries → 0 (reset) → 15 (re-pollution) → **427** (curated). |
| `s3://opal-data-portal-v2/json/sentiment/keyword-sentiments.json` | Regenerated via Lambda re-invoke. 5 keywords → **39**. |
| CloudFront invalidation `ICAK7QECU4S8YD9P0YP1CDSYRC` on `/api/general/sentiment/keyword-sentiments.json` (distribution `EVTSA9VEHNZVH`). |

---

## Commits

| Hash | Author | Description |
|------|--------|-------------|
| `676aabe2` | 0.1.0_DS_MarketIntelligence | fix Daily Cloud GPT filter runaway (Lambda guardrail + kill auto-learn + brief + archive + initial log) |
| `b54c31fc` | 0.1.0_DS_MarketIntelligence | curate Daily Cloud banned-phrases list (427 curated entries replacing 1,207; 781 legitimate market topics unbanned) |

---

## Compiler Tools

| Tool | Command | Result | Notes |
|------|---------|--------|-------|
| comp-blast | `comp-blast news-trending-analysis` | 1 EventBridge trigger, Lambda itself. | No cross-domain Lambda dependencies; the real downstream (S3 artifact → portal TopicCloud) not in graph. |
| comp-pipescript | N/A | N/A | This is a Lambda change, not a gold script. |
| comp-routes | `comp-routes trace opal-portal-data-proxy` | No match. | Expected — proxy Lambda isn't in route registry; Daily Cloud loads via public `/api/general/sentiment/keyword-sentiments.json` directly from CloudFront → S3. |

---

## Evidence Pack

**CloudWatch log (today's broken run, request `58522ef9-fcd2-4e28-9d02-0f60c820cc55`):**

```
[+] BULLISH: smartfinancial earnings (+0.959)    [candidate, filtered out]
[+] BULLISH: bank of america earnings (+0.898)   [candidate, filtered out]
[+] BULLISH: anthropic amazon deal (+0.072)      [candidate, filtered out]
... 37 more legitimate topics flagged as "junk" by GPT ...
GPT: identified 37 junk keywords: {'netflix earnings downgrade', 'kevin warsh fed', ...}
   Reason: The keywords contain either meaningless fragments, boilerplate phrases, or are not relevant to financial topics.
OK: Saved 1207 dynamic stopwords to S3
Filtered: 42 -> 5 keywords
```

**14-day filter trajectory (CloudWatch `filter-log-events "Filtered"`):**

| Date (ET) | Filter in→out | Signal |
|-----------|---------------|--------|
| 4/07 – 4/16 | 30-46 → 28-46 | Normal |
| 4/17 07:16 | 46 → 21 | First degradation |
| **4/17 17:16** | **35 → 0** | **Empty word cloud** |
| 4/18 – 4/20 | 30-40 → 23-38 | Intermittent degradation |
| **4/21 07:16** | **42 → 5** | **Andrew's screenshot** |
| 4/21 08:43 (my re-invoke) | 41 → 39 | Normal after reset |

**Pre-reset contamination sample** (dynamic_stopwords.json, random 30 of 1,207):

`anthropic amazon deal`, `earnings call transcript`, `chair jerome powell`, `fed chair`, `federal reserve announcements`, `bitcoin etf filings`, `bank of america earnings`, `cftc crypto staffing`, `delta earnings report`, `ira contribution limits`, `trump crypto venture`, `reed hastings departure`, `tim cook transition`, `smartfinancial earnings`, `crypto regulation clarity`, `farage bitcoin probe`, `circle internet earnings`, `bitcoin price predictions`, `bitcoin rally iran ceasefire`, `saudi arabia liv golf` (legit junk — sports), `scottish football` (legit junk), `gavin newsom`, `masters week`, `timestamp updates`, `story here`, `interview with`, `secretary of`, `control`, `a fire`, `in venezuela`.

---

## Current State (end of session)

- **Daily Cloud data:** healthy. 39 keywords at `s3://opal-data-portal-v2/json/sentiment/keyword-sentiments.json`, generated 2026-04-21 08:43 ET. CloudFront invalidation submitted; portal picks up on next client refresh.
- **Dynamic stopwords file:** **427 curated entries** (sports + entertainment + lifestyle + fragments + boilerplate only). 781 legitimate market topics that had accumulated over 3 months were unbanned.
- **Code fix:** committed to CLOUD branch at `676aabe2`, awaiting DT push + deploy. Until then, the deployed Lambda's auto-learn loop is still live — the 427 count can drift up until DT lands the fix.
- **Diagnostic artifacts retained** in `.runtmp/` (gitignored): raw CloudWatch exports, partition scripts, before/after keyword JSONs. Safe to delete after DT deploy confirmed.

## Next Steps

1. [DevOps 0.1.0_DT_MarketIntelligence] Deploy per `docs/briefs/devops-brief-daily-cloud-gpt-filter-guardrail.md`. Target tag `news-v2.9.6`. After deploy, the dynamic stopwords file stops auto-growing; manual curation via direct S3 edit or a DS commit to the deliverables file.
2. [DS 0.1.0_DS_MarketIntelligence] Monitor the next 2-3 EventBridge runs (17:16 ET tonight, 07:16 ET tomorrow). Without the auto-learn loop, stopwords count should stay flat at 427. If it grows, deploy didn't land.
3. [RD 0.1.1_RD_MarketPerformance] Secondary fragility: `portal/src/components/market-performance/TopicCloud.tsx` visx Wordcloud drops long multi-word phrases when canvas is small. Even with 39 keywords today, some of the longest phrases may not render. Not urgent but worth a hardening pass.
