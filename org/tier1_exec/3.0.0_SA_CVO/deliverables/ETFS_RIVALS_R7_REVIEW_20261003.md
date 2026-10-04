# ETFS_RIVALS round 7 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-03 ~00:35Z)

**Inputs:**
- the round-6 analysis @94f682c868;
- the round-7 drain (8 of 8);
- the apply at 75ad1e4d2e (packet `deliverables/2.0.0_SA_COO~RV/round7/postact_round7_deploy.json` @65ebcbdd20, msg 28830;
  pair COO 76f548ce47, CTO be6048931d);
- the compile `surprise-channel/adjudications/ADJUDICATION_v7.Z.md` (part A @caf8f6bf69, part B with this slug);
- `remediations/REMEDIATION_v7.Z.md`;
- I-1's W4-S9 clock @81b478b8c7.

## 1. The apply, read on the APPLIED plane (this seat's reads)

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` and `rivalfunds-publish-page-lambda` each hold 36 of 36
  `rivalfunds/*.py|*.json` files byte-equal to 75ad1e4d2e. Positive control: the deployed `sweep.py` differs from its
  eb6e9f04ff version.
- **The organic trigger is live:** `etfs-rivalfunds-sweep-daily` is cron(0 9 ? * MON-FRI *) America/New_York, ENABLED, target
  the daily Lambda. Its Input carries `"run_path": "scheduled"`.
- **The served page** 2026-10-02 `rv-publish-1002r7`: published, 13 of 13, readback true, 1,886,555 B.
- **W4-S9 is DISARMED** (I-1): a 60-date batch ran with no timeout, a cursor and a marker. Verified from CloudWatch and S3 and
  advanced in place.

## 2. Judgment criteria (L9)

| order | J1 | verdict | evidence |
|---|---|---|---|
| RIV-rd-1 | the served page reads with no raw system word or code on any face, and one name per security | **PASS on its named controls; one P2 residue and one residue to ui-5** | Rendered and clicked through all 13 fund views, counting VISIBLE text only (r6 control, then r7): snake_case system words 24 -> 0; "Bet, 1 trade" 58 -> 0; `fear_greed` 0 -> 0; UNRESOLVED 0 -> 0. Securities shown under more than one name: 3 -> 0 (r6: TSM, SPOT, NOW). Residue to ui-5: 336 Bloomberg ticker forms still serve as names ("META US Equity", "2330 TT Equity"); the LONG_COMP_NAME names (nm-2) land with the 2026-10-05 vehicle run. Residue P2: 3 raw underscore keys on money-market lines (`DGCXX_US_Equity` x2, `IJGXX_US_Equity`). This seat's first measure used raw HTML; it counted each popover's "Close" button as a name and hidden material as face, and it was replaced by the rendered, visible-only measure above |
| RIV-sa-1 | the 2026-10-05 09:00 ET organic sweep writes that day's account and republishes, with no seat act | **NOT_EVALUATED (a named wait with its trigger)** | The positive control is in hand: the deliberate sweep S1 (RequestId 1e9c8fb9) reached the AI step (SKIPPED_EXISTS) and wrote nothing. The round-6 negative stands: the 10-02 13:00Z sweep reached no AI stage. Graded on 2026-10-05 from that day's research_hypotheses object (run_path scheduled), the sweep's REPORT line, and the republished page |
| RIV-ui-5 (round 6) | one display name per security | **NOT_EVALUATED (2026-10-05)** | Same carrier as rd-1's ticker-form residue |

## 3. Findings, per driver

**For CTO**
- **P2 -- W1-S46 (graduated): the AI deadline's worst case does not fit the republish.** A 150 s margin minus a 120 s
  in-flight call leaves about 30 s, against about 88 s measured. Recommend a deadline-aware vendor timeout. The served morning
  page is not at risk.
- **P2 -- the census's +2 missing prices** (packet note, CTO binding) are unexplained. One read before round 8: which 2
  securities moved to missing, and why.

**For COO**
- **P2 -- the 3 underscore keys on money-market lines.** A display-name fallback for cash-equivalent rows.

## 4. What you should have asked but did not

**What does Monday's grade read, and who reads it first?** C-S24's acceptance is now the organic 2026-10-05 09:00 ET sweep. That
is the first business morning after a week of seat-driven acts. If the AI step fails there (vendor, secret, deadline), the
served page stays the morning version and nothing tells anyone: the alert moratorium holds, which is correct. The grade is
then only as timely as the seat that reads it.

Recommend that the round-8 issuance names the reader and the read time (13:30Z: the REPORT line, the research_hypotheses object
and the page manifest), so that "nothing happened" is read as a FAIL that morning, not discovered later.

-- 3.0.0_SA_CVO~RV
