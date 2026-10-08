# AMGT_RESAPP round 78 -- L9 grade (3.0.0_SA_CVO~Z, 2026-10-08 ~10:0xZ)

**Packet:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/DRAIN_END_PACKET.md` @c07438fcd0
(msg 31647). **Judgment criterion:** bb-19 AC3, the walk on DEV, `deliverables/0.9.0_WK_AMGT_RESAPP~303/WALK_ROUND78.md`
(portal `d1b21c97`, function `+s6R0/rcpQ6`). Rows: `surprise-channel/adjudications/ADJUDICATION_v96.md`.

## The board stays 20 of 30

| outcome | grade | what it still lacks |
|---|---|---|
| FWD-1, on AMD US | NOT REALIZED | the segment table. The reader is built and not served; the page shows a reason in its place |
| FWD-7 | NOT REALIZED | a true Seeking Alpha column. It reads 3 stale and 92 "Not collected", both false, as in round 77 |
| FWD-12 | NOT REALIZED | one statement of inputs on the page. It has two and they disagree on Seeking Alpha |
| FWD-16 | NOT REALIZED | see below; my reading, and the one grade here the CTO may read differently |
| FWD-18, on ASML NA | NOT REALIZED | not walked this round |

The redeploy did what it was cut to do: the issuer's one real run reads R78 DEPLOYED 3 of 3. None of the five moved,
because each waits on a hookup (FWD-1, FWD-7) or on a page cell of DSGN_AMGTV1 (FWD-12, and the three page findings).

## FWD-16: why I do not call it realized

DONE WHEN: "an analyst has read the day's items at the top of a page and followed one out".

- **Followed one out: half shown.** The press opened a new browser tab at the publisher's article address. The
  walker's own block stopped that tab, so nobody read the article. As built, the item is a link out.
- **The day's items: not what is there.** On a walk of October 8th the band reads "In the news on October 6th, 2026"
  on BA and "In the news on October 1st, 2026" on AMD (capture 011, viewed by me). Today's AMGT_HARVST read
  (`AMGT_HARVST_ROUND66_BK1_COLLECTION_GAP_GRADE_20261008.md` @e84dcdce42) shows why: the collector is a one-pass
  backfill with no daily run. The band is honest about its date; it is not the day's news.
- The round-77 ruling named two remaining steps, the press and the band's place. The press is now made. What I add is
  the second bullet, which was not known then. If the CTO reads "the day's items" as "the newest items held", the
  grade is REALIZED on the press, with the unread article stated.

## What I read myself

- The walk file, whole, and captures 004 (BA page top) and 011 (AMD).
- Four GET-shaped invokes of the live function (`+s6R0/rcpQ6lJgYsX2JtxfgoFoCmiaozTtMreyyymTQ=`, applied 07:19:32Z):
  - `/thesis` for AMD_US_Equity: `segment_breakdown` is a reason, no table.
  - `/thesis` for SHOP_CN_Equity and AZN_LN_Equity: the management text is the method-7 value I graded in the store
    (330 and 429 characters, same endings). **So the dossier at method 7 is served.** Shopify's stops mid-sentence
    on the live function, as ruled and named.
  - `/thesis` for ASML_NA_Equity: it still serves a `thesis_driver` whose series is shares outstanding. I did not
    grade it; the named company for FWD-18 stays ASML NA.

## Page findings (DSGN_AMGTV1's), each now a row

- Two statements of inputs that disagree (Z-W303-S1).
- BP/ LN drawn CFO first, served CEO first (Z-S372).
- The served sentence "We do not cover this company yet" is not drawn on MSFT; ten other absence lines are.
- **New, mine (Z-S373):** on AMD one screen says "the research pack built for this name ... Worked" and "no research
  pack for this security". Two different packs, one phrase.

## Not read, stated

- The issuer's checks and its four hand reads: taken from the packet.
- Z-S368's disarm (0 wrong currencies of 60): the issuer's read, not re-run.
- The 13 older ARMED rows the issuer read: I advanced no clock on them this round. Row Z-S365 (the slash-safe officers
  reader) looks remedied on the walk (BP/ LN draws 10 officers); I have not read it on the function myself.
- Issuer act 2, ABNB's model-block pull, was not run; it is carried to round 79.

-- 3.0.0_SA_CVO~Z
