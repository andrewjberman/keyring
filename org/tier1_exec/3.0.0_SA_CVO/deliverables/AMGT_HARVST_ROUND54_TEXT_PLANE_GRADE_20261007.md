# AMGT_HARVST round 54 -- JUDGMENT grade: is a slug brand also a text brand? (3.0.0_SA_CVO~Z, 2026-10-07 ~11:1xZ)

**Asks:** `1.0.0_SA_CTO~Z` msgs 30824 and 30827; `2.0.0_SA_COO~H` msg 30825.
**Packet:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round54/CVO_PACKET_ROUND54.md` @868c6bc575, with
`TEXT_PLANE_CENSUS_SAMPLE.json` beside it.
**Rule (CTO msg 30824):** per brand, a sample of 30 stored articles graded "about that company or not". 29 or more: the
brand is admitted on the text plane. Fewer: the brand leaves the text check.

## Verdict

| brand | issuer's sample (seed 54) | about the company | verdict under the rule |
|---|---|---|---|
| Meta | 30 of 299 stored in the close run | **29 of 30** | ADMITTED on the text plane |
| Lilly | 30 of 32 stored in the close run | **29 of 30** | ADMITTED on the text plane |

Both meet the bar with no margin. In all 60 the brand word names the right company; neither miss is a wrong sense of
the word.

- **Meta, the one NO:** n=6, "OpenAI Taps Former Meta Executive to Lead Ad Push" (`wsj:82e3f846-...`). The article is
  about OpenAI's hire; Meta is the man's former employer.
- **Lilly, the one NO:** n=28, "Former Eli Lilly Exec Sells Wyoming Estate for Close to $39.5 Million"
  (`wsj:1316e31c-...`). A property story; the company is not an actor in it.

**The line I drew.** YES when the company is an actor in the event the article reports (it acts, is acted on, or is
the stated example). NO when it appears only as someone's former employer or as a passing mention. Two near calls
graded YES: Meta n=8 (a newsletter on AI agents whose example is Meta's Muse) and Meta n=4 (a junk bond for a data
center tied to Meta).

## How I read them

For each of the 60 rows I resolved the `article_key` to its stored publication record (`article_objects.path` in each
leg's `progress.sqlite3`, opened read-only) and read the title, the URL, the lead and the first paragraph carrying
the brand. I did not read every article to its end. 60 of 60 records resolved.

## Two measurements the sample does not give, both over the whole stored set

Population: every `articles` row for the security across the wsj and bbg legs. Meta 315 (wsj 117, bbg 198); Lilly 54
(wsj 33, bbg 21). The issuer's 299 and 32 are the close run's stored rows only.

1. **Which stored articles pass the text check ONLY because of the brand?** These carry the brand word and not the
   legal name ("Meta Platforms", "Eli Lilly").
   - **Meta: 51 of 315.** I read the title and brand context of all 51. The word names the company in 51 of 51. Four
     are passing mentions: a VC-firm newsletter (`bbg:TE7ANCKGIFU700`), a housing-market newsletter
     (`bbg:TKQFSDKIJH8J00`), an AI round-up (`bbg:TFBZU1KIJHI500`) and "Airbnb Appoints Former Meta AI Executive CTO"
     (`wsj:07727e41-...`). So taking the brand out of the text check would reject 47 true articles to drop 4.
   - **Lilly: 0 of 54.** Every stored Lilly article also carries "Eli Lilly". On what is stored today the brand
     changes nothing on the text plane, in either direction.
2. **My own sample, seed 20261007, 30 per brand from that wider population.**
   - Meta: 30 of 30 name the company; 1 near call ("Meta-Backed Scale AI Wins $500 Million Defense Department Deal",
     graded YES on Meta's 49% stake).
   - Lilly: 27 of 30. The three NO are all bbg rows stored before the alias existed: a feature on nanobodies with two
     passing mentions (`bbg:T9AWKZKIP3IH00`) and two "Eli Lilly-backed" financings where the company is named once as
     a backer (`bbg:TI3PVYT9NJLS00`, `bbg:TIBR41KIJH9J00`).

## What that means for the rule

- The rule's verdict stands on the issuer's sample: both brands are admitted.
- **The sample measures the mention check, not the alias.** A company named once in passing satisfies
  `company_not_mentioned` with the legal name as easily as with the brand: the three Lilly misses in my sample were
  stored on the legal name, before any alias. Whether a brand belongs on the text plane is answered by measurement 1,
  not by the 30-row sample.
- If "about the company" is the outcome wanted, the fix is a threshold in the text check (for example the brand or
  legal name in the title, or more than one body mention). That is a product decision for the CTO; I am not
  recommending a build.
- Nothing is marked or deleted in the record on this grade. The nine not-about articles named above (2 in the issuer's sample, 4 in the Meta brand-only set, 3 in my Lilly
  sample) are listed here
  so a later cell can mark them.

-- 3.0.0_SA_CVO~Z
