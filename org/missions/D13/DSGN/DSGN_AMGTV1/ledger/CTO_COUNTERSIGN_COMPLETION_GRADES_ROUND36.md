# DSGN_AMGTV1 -- CTO countersign of the rounds 34-36 completion grades, with two rulings (1.0.0_SA_CTO~Z, 2026-10-05 ~03:4xZ)

**Input:** `2.0.0_SA_COO~D` msg 29460; `deliverables/2.0.0_SA_COO~D/round36/COMPLETION_GRADES.round36.json` @c706123ec2: 15 REALIZED, 6
NOT_REALIZED, 5 NOT_EVALUATED, 1 RETIRED. The grading walk ran on DEV `c66d08f3` (read-20261005T025451Z, 26/1/0; FWD-24 control PASS
on MSFT; FWD-20 instrument 76/0).

## Countersign

**COUNTERSIGNED as graded.** Each NOT_REALIZED row names its contrary and its artifact. The two rows that asked for a ruling are
ruled below, and neither changes a verdict.

## Ruling 1 -- FWD-4 against FWD-27 on a name whose payload lacks header figures (ROG SW: 3 of 7 tiles)

- **Both outcomes hold, and they do not conflict on the page.** FWD-27's "an unconnected field prints no line" is the page's correct
  behaviour: it never invents a figure or a placeholder tile. FWD-4's seven-figure row is a COMPLETENESS outcome, and it is met only
  when the payload carries the figures.
- **FWD-4 stays NOT_REALIZED, and the cure is the PRODUCER.** ROG SW's served figures carry no `PX_LAST`, beta, average volume or
  short interest. That gap is AMGT_RESAPP's overlay, so it is routed to RESAPP (`2.0.0_SA_COO~Z`, an addendum to the round-68
  analysis): every covered name's header payload carries the seven figures, or a served reason per missing figure. The DSGN page
  changes nothing.

## Ruling 2 -- FWD-7's scope (ASML passes; AMD and MSFT show no officers; 84 of 95 covered names have no management object)

- **The scope stands as written: "for every covered name".** It is not narrowed to names whose filings list officers. Narrowing an
  ENDPOINT outcome to what the producer delivers would be grading the producer's coverage as the target.
- **FWD-7 stays NOT_REALIZED, and the cure is the PRODUCER:** the F3 fallback chain (filing, then dossier, then Bloomberg) applied
  to the 84 names. That is RESAPP's exec-roster re-run, routed with ruling 1.
  - **Sources:** only those already worded. A leg that needs a vendor call no word of Andrew's names is listed for him as an ACT,
    never assumed.
  - **Grading:** each name either shows its officers with the source named, or shows the designed "no list published yet" sentence
    with the source chain it tried.
