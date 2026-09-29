# AMGT_HARVST ROUND 12 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~03:3xZ
**Input:** `2.0.0_SA_COO~H`'s `round12/ROUND12_DRAIN_END_PACKET.md` @`fc46ad44fd` (read to EOF, 6,168 B), msg 26422.
**L7 RE-MEASURED not adopted:** `a-1`..`a-4`, `w-2`, `w-4`, `w-5` all `complete` on their LAST `<status>` tag at HEAD; exactly 2
criteria carry `judgment="true"` (`a-4` AC4, `w-2` AC4). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **88 items, 17 UNDER_INVESTIGATION**, which reproduces the packet's fold. **9 of the 17 gate the
slug** (class BLOCKING or ARMED).

### THE OUTCOME THIS ROUND EXISTS FOR -- READ ON THE APPLIED PLANE BY THIS SEAT

`apigatewayv2 get-routes` on `7k3ed8px20` now returns **18 AMGT route keys**, including `GET .../timeline` and
`GET .../timeline/day/{date}`, with `/thesis` present as the control. At round 11 this seat read 16 and 0. The close-run trace
shows the deployed function (`CtIvirv...`, 01:58:24Z) answering `/timeline` HTTP 200 for BA (2 events) and 992_HK (3 events).
The in-region timing is measured in `a-2`'s proof instance (Lambda REPORT duration; the day route at 8.85 s), not in the trace.

### DISPOSITIONS -- the 9 gating rows

| row | disposition | grounds |
|---|---|---|
| `Z-W31-S1` (ARMED: routes unmounted) | **GRADUATED** | 18 routes live, both timeline routes present (this seat's read, above) |
| `Z-S35` (ARMED: a mount alone cannot make the routes serve) | **GRADUATED** | The deployed function serves both routes with data (trace: HTTP 200, 2 and 3 events) |
| `Z-S36` + `Z-S39` (ARMED/BLOCKING: the role could not read, then could not LIST, harvest gold) | **GRADUATED** | The deployed function serves rows equal to the newest landed `chatter_event` (close run), which a role without GET and LIST could not do. ⚠ This seat did not read the IAM policy itself; the proof is the served read |
| `Z-S38` (BLOCKING: the pyarrow pin) | **GRADUATED** | The deployed function reads parquet gold and answers HTTP 200 |
| `Z-W35-S1` (BLOCKING: two pinned-16 tests turned red) | **GRADUATED** | Resolved by AMENDMENT 1 (`Z-W35-S2`, CLOUD @`15caf6ed3b`); the packet's api suite reads 256/256. ⚠ Not re-run here |
| `Z-W31-S2` (ARMED: day-route latency) | **GRADUATED** | In-region day route 8.85 s against a 29 s ceiling (`a-2` proof instance, Lambda REPORT duration). Round 11's 19.9 s was an off-box, in-process figure |
| `Z-W37-S3` (BLOCKING/INERT: a guard test ran the real Seeking Alpha re-authentication) | **GRADUATED** | The resume ran behind three guards, all PASS, under the CTO's ruling @`74e1eea534`. The spend is ledgered as an ESTIMATE-UPPER-BOUND; the incident stays on the record |
| `Z-S37` (ARMED: `safe-merge --continue` whitelists the conflicted index) | **CARRIED** | A tool fix proposed to the script's authoring lane; not landed |

**NON-GATING:** `Z-S34` GRADUATED with the rows it specified. `Z-W37-S4` (the HTTP 402 on the Seeking Alpha account check) is
CARRIED. **Its owner is the account holder, not a seat:** is the subscription active, and does the account show the 00:21Z
sign-in? `Z-W34-S1`, `Z-W35-S2`, `Z-W36-S1`, `Z-W37-S1`, `-S2` and `-S5` are CARRIED as INERT notes.

## 2. L9 -- `a-4` AC4: "does the lead name what the burst was about?"

This seat re-ran `ac4_does_the_lead_name_the_burst.py` against S3 (8 events, 263 mention rows, 120 silver headlines):

| event | stories (tier-A) | served lead | names the burst? |
|---|---|---|---|
| 992_HK 02-12 | 2 (1+1), one results day | Lenovo earnings beat | **YES** |
| 992_HK 05-22 | 3 (1+1+B), one results day + a market wrap | Q4 revenue beat | **YES** |
| 992_HK 08-13 | 2 (1+1), one results day | record revenue | **YES** |
| **BA 08-26** | 2 (1+1), **unrelated**: FAA Dreamliner inspections / Wisk vertiport | FAA inspections (a 1-1 tie) | **NO -- there is no single burst to name** |
| BA 09-08 | 3 (1 runway + **2 deliveries** + B) | **"Boeing Delivers 51 Jets in August"** | **YES -- round 11's miss is fixed** |
| COST 09-14 | 2 (1+1), same story | motor-oil price hike | **YES** |
| HD 08-18 | 2 (1+1), same results | results beat | **YES** |
| NVDA 06-01 | 3 (1+1+1), one story read as three | Nvidia AI PCs | **YES** (the under-merge does not reach the lead) |

**VERDICT: 7 of 8** (round 11: 6 of 8). The one miss is structural, not a lead choice. BA 08-26 is two unrelated stories that
share a day, and no lead can name "the burst".

⭐ **THE ONE LINK THAT FIXED BA 09-08 IS A MONTH NAME.** After `boeing` and `jet` were dropped as ubiquitous, the deliveries
pair links on exactly one shared token, **`august`**. The link is right here, because both are August-deliveries stories. But
a calendar word is shared by most same-month headlines, so the next multi-story day in any month can over-merge through it.
Round 13 should drop calendar tokens (month and day names) from the link vocabulary, as `boeing` and `jet` already are.

⚠ **"Only events with 3+ tier-A articles can change lead under the grouping"** (the script's own line): the plurality rule acts on
2 of 8 events here (BA 09-08, NVDA). The rule is thin because the data is thin, which is the packet's own carding.

**"Is a multi-story day one event?" -- the evidence the CTO asked for.** Of the 8, **6** hold tier-A stories about ONE company
event (a results day, one product push, one price action). **2** hold unrelated tier-A stories (BA 08-26; BA 09-08's runway story
beside deliveries). This seat's reading: **a day whose tier-A stories are about unrelated company events is not one event.**
Splitting it is the honest shape, and it would dissolve BA 08-26's tie rather than break it arbitrarily. The ruling is the CTO's.

## 3. L9 -- `w-2` AC4: UNGRADED -- NOT EXERCISED

`w2_ac4_output.txt`: **0 listing pages fetched**, so 0 `--new-only` skips. The first job hit the account-check error (HTTP 402);
the rest were cooldown-suppressed before reading `known_ids`. **A skip criterion with no skips is not a pass.** The capture never
reached the code path the criterion exists to test. It re-arms at the next capture that fetches a listing page.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 7 of 7. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 9 gating: 8 GRADUATED (7 rows as tabled, `Z-S36`+`Z-S39` counted as two), 1
   CARRIED with its owner and reason. **MET**
3. **Every judgment criterion graded** -- `a-4` AC4 graded 7 of 8; `w-2` AC4 UNGRADED by name as not exercised. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S30",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T03:35:00Z",
    "one_line": "L8/L9 round 12: the timeline serves on the deployed API for the first time -- 18 AMGT routes live incl. both timeline routes (this seat's get-routes read; 16 at round 11), HTTP 200 with data, day route 8.85 s in-region. Eight gating rows graduate on that. a-4 AC4: the lead names the burst on 7 of 8 (round 11: 6); BA 09-08 is fixed, but the only link that fixed it is the month token 'august'; BA 08-26 is two unrelated stories and no lead can name it. w-2 AC4 is UNGRADED: 0 listing pages, 0 skips.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST a-1, a-2, a-3, a-4, w-2, w-4, w-5 all read 'complete' on their LAST <status> tag at HEAD; judgment=\"true\" on a-4 AC4 and w-2 AC4.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') reads 88 items, 17 UNDER_INVESTIGATION; 9 are BLOCKING or ARMED: Z-W31-S1, Z-W31-S2, Z-S35, Z-W35-S1, Z-S36, Z-S37, Z-W37-S3, Z-S38, Z-S39.",
        "APPLIED plane: apigatewayv2 get-routes --api-id 7k3ed8px20 returns 18 route keys containing /api/scoped/amgt, including 'GET /api/scoped/amgt/security/{security_key}/timeline' and 'GET /api/scoped/amgt/security/{security_key}/timeline/day/{date}', and 1 ending /thesis as the control. This seat's round-11 read of the same API was 16 and 0.",
        "SERVED: round12/CLOSE_RUN_ROUND12_TRACE.txt reads deployed CodeSha256 CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM= (LastModified 2026-09-29T01:58:24Z), '/timeline (deployed) -> HTTP 200, 2 events' for BA_US_Equity and 'HTTP 200, 3 events' for 992_HK_Equity. The in-region timing is in deliverables/0.7.0_AE_CloudOps~A/AMGT_HARVST.TO-HVST-a-2...proof_of_spec.json (Lambda REPORT duration; the day route 8.85 s), not in the trace.",
        "GRADUATED: Z-W31-S1 (routes live), Z-S35 (the deployed function serves), Z-S36 + Z-S39 (a served read equal to the landed rows needs GET and LIST; this seat did not read the IAM policy itself), Z-S38 (the parquet read serves), Z-W35-S1 (AMENDMENT 1 @15caf6ed3b via Z-W35-S2; api suite 256/256 per the packet, not re-run here), Z-W31-S2 (8.85 s in-region against 29 s), Z-W37-S3 (three guards PASS under the CTO ruling @74e1eea534; spend ledgered as ESTIMATE-UPPER-BOUND), and Z-S34, the spec those rows executed. CARRIED: Z-S37 (tool fix not landed); Z-W37-S4 (HTTP 402, owner the account holder).",
        "L9 a-4 AC4, from this seat's own run of ac4_does_the_lead_name_the_burst.py against S3 (8 events, 263 mention rows, 120 silver headlines): YES on 992_HK 02-12, 05-22, 08-13, BA 09-08 (lead now 'Boeing Delivers 51 Jets in August, Lowest in Four Months', the 2-article deliveries story), COST 09-14, HD 08-18, NVDA 06-01; NO on BA 08-26 (a 1-1 tie of 'FAA Orders Inspections of Some Boeing Dreamliners for Gaps' and 'Boeing's Wisk breaks ground on California vertiport', unrelated). 7 of 8; round 11 read 6 of 8.",
        "THE LINK: the script prints for BA 09-08 'tier-A tokens dropped as ubiquitous: [boeing, jet]' and 'bbg:TL11A6T9NJ ~ sa:4640843: shared ... after drop=[august] -> LINKED'. The grouping's one decisive link is a month name.",
        "THE 'ONE EVENT?' EVIDENCE: 6 of 8 events hold tier-A stories about one company event; 2 hold unrelated tier-A stories (BA 08-26; BA 09-08's runway story beside deliveries). The script also prints that only events with 3+ tier-A articles can change lead under the grouping: 2 of 8 here.",
        "L9 w-2 AC4 UNGRADED: w2_ac4_output.txt reads 'sa listing pages fetched by the capture ... 0'; job 1 status account_or_harvester_unavailable (the 402), the others cooldown_suppressed before reading known_ids. No skip exists to grade."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W31-S1",
      "AMGT_HARVST-Z-W31-S2",
      "AMGT_HARVST-Z-S34",
      "AMGT_HARVST-Z-S35",
      "AMGT_HARVST-Z-S36",
      "AMGT_HARVST-Z-S38",
      "AMGT_HARVST-Z-S39",
      "AMGT_HARVST-Z-W35-S1",
      "AMGT_HARVST-Z-W37-S3"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @fc46ad44fd asserts 7 orders terminal and VALID, the timeline served on the deployed API with in-region timing inside 29 s, 8 rows' remedies exercised, a-4 AC4 presented with the lead rule carded as thin both ways, and w-2 AC4 with nothing to grade.",
    "world_is": "True as re-measured on the applied plane (18 routes, both timeline routes present) and against S3 (the AC4 run). The lead names the burst on 7 of 8. BA 09-08's fix rests on the single month token 'august'. BA 08-26 is two unrelated stories, not one burst. w-2 AC4 was never exercised.",
    "notes": "FOR THE ROUND-12 ANALYSIS, three items. (1) Drop calendar tokens (month and day names) from the story-link vocabulary, as 'boeing' and 'jet' already are; the one link that fixed BA 09-08 is 'august'. (2) On 'is a multi-story day one event?': this seat's reading of the evidence is NO where the tier-A stories are unrelated company events. Split them, which dissolves BA 08-26's tie instead of breaking it; the ruling is the CTO's. (3) Z-W37-S4 needs the ACCOUNT HOLDER: is the Seeking Alpha subscription active, and does the account show the 00:21Z sign-in? The worktree holding the only raw incident evidence (wk-hvst-r12-37/.scratch/auth/) is kept until that owner's word."
  }
]
```
