# AMGT_HARVST -- ROUND 41 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-03 ~23:4xZ

**Input:** CVO slug msg 29069, `surprise-channel/adjudications/ADJUDICATION_v53.md` @716910082a (precondition MET). The authority is
Andrew's card 2 (~20:3xZ, "yes to all recommendations", @9fe6e6f111): FinBERT scoring over the stored articles, and the event
rebuild.

## 1. WHAT THE ROUND DELIVERED

- **an-1:** 13,224 articles FinBERT-scored, 11 no-text markers, 0 errors.
- **an-2, the tone rebuild,** under the pair COO @72f2c9be42 / CTO @8e0fed682a, is served. Mention 23,691 -> 31,042 rows, none gone or
  changed. CVO~Z read S3: every row's tone equals the scorer's own record for its content key (0 mismatch, 0 absent).
- **an-3, the event rebuild,** is served. Events went from 8 to 507 on 68 securities. Every event has 2 or more publishers, and every
  marker day opens. The 4 dropped ids were re-formed stories.
- **All post-act conditions of this seat's halves PASS** (COO~H msg 29066, @94c659696c).

## 2. GRADES

| FWD | grade | ground |
|---|---|---|
| **FWD-16** (FinBERT tone per article version, in gold) | **REALIZED** | CVO~Z's own S3 read of all 31,042 rows: 0 mismatch, 0 absent. |
| **FWD-6** (news events as spans on the timeline) | **REALIZED** | 507 served events, each with its lead headline and its articles. Every event is right on its own listing's page. |

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Z-C-S72:** 78 events are one company's story under two listings (BP 33, HSBC 14, ASML 13, Unilever 9, Roche 8, ICICI 1), about 429 distinct stories; `composite_figi` is null | **Not cut.** Recorded: the event count is per listing. | Every page is one listing, and each is correct on its own. No outcome counts distinct stories across listings. Grouping needs an identity source the estate does not hold (`composite_figi` null), and pulling one is a new vendor field no word of Andrew's names. |
| 2 | **FWD-17,** the window tone in gold (30/90/365, voters = non-neutral, tone over voters, null when 0 voters) | **Round 42's cell,** a new gold table (`chatter_window`), built through its builder under a never-widen pair. | Card 2 approved the scoring so that tone shows on DSGN and RESAPP ("Tone on DSGN/RESAPP shows 'not served yet' until they run"). FWD-17 is the step that turns the article scores into the window tone those pages read. |
| 3 | **AMD and VLO serve 0 events** (tier-A coverage from one publisher) | **The rule's answer, not a gap.** | RESAPP FWD-37 already says a name with no burst carries its earnings markers once pulled, and CORPUS aj-2 now pulls the dates. |

## 4. ENRICHMENT LIST (round 42, ONE issuance by `2.0.0_SA_COO~H`)

1. **FWD-17 `chatter_window`:** the build, its plant (an all-neutral name reads voters 0 and tone null, never 0.0), and its served
   write under a pair. RESAPP's chatter route then reads it (FWD-36's tone limb), as RESAPP's own cell.
2. **Nothing else.** Collection (STOP_FT, any relaunch) stays with Andrew: "We will discuss internally on how to proceed with further
   data collection after review."
