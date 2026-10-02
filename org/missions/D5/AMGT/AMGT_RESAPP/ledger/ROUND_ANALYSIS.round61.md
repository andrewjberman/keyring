# AMGT_RESAPP -- ROUND 61 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~09:4xZ

**Input:** CVO~Z slug msg 28369, `surprise-channel/adjudications/ADJUDICATION_v73.md` @beea21d735 (precondition MET; all 8 rows past v72
dismissed). CVO~Z read the deployed `opal-amgt-scoped-api` itself (CodeSha256 `E+FAZF0f...`, 07:45:38Z). **Round 61 is CLOSED.**

## 1. WHAT THE ROUND DELIVERED (served, PROD included; no portal promote needed)

DSGN round-21 analysis section 3B, cells B1-B5, each landed under its never-widen pair:

| cell | what | served read (CVO~Z) | pair |
|---|---|---|---|
| B1 | a company name on every price row | 94 of 94 named | ak-2, CTO half @02d032ee67 |
| B2 | plain served reasons (Lusha, registry) | 0 code-shaped peers reasons | ak-6 act (A), @af95b2f1c0 |
| B3 | M-1 officer parse | VLO officers carry full titles and no ages | ak-6 act (A) |
| B4 | posture basis claims in words | 0 of 12 status tokens | ak-6 act (A) |
| B5 | CEO public-profile basis in words | the basis reads in words | ak-6 act (C), @b49f4d2db3, re-signed @bbbda2e848 |

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **No RESAPP round 62 before Andrew's demo read** (13:00Z). Round-60 ruling 1's hold resumes: COO~Z cuts only on a served-field defect that a DSGN or Andrew walk surfaces. | the served faces are fixed on PROD |
| 2 | **B2's residual system vocabulary in the peers reasons is the page's to word,** per the DSGN round-23 analysis ruling 1 (FWD-16 reasons in reader words, page-side, one clause per registry reason class). No RESAPP cell. | the page maps reason classes to clauses |
| 3 | **After the demo, round 62's list is round-60 ruling 3's carried items:** `Z-S332` (an unknown key answers 200, not 404); the dead legacy inputs on the chatter path; collapsing the page universes to one; removing the duplicate dossier prefix's reads. Plus the `ceo_profile_reading` new-failure-prefix line that ak-3 added and that rides the next scoped-API redeploy. | carried, not on the demo thread |
| 4 | **The future-dated `surfaced_at` stamps** (6 of 8 rows read 12:00Z-13:10Z at a 09:33Z compile): the issuer's workers write the time a row is surfaced. `surprise-row-gate` now WARNs on such a stamp (@a19b3df852). | v73 ask |

## ADDENDUM 2026-10-02 ~10:4xZ -- DEMO RISK: BA `/timeline/day` times out on every call since 10:14Z (CVO~Z msg 28406, DSGN v23 row Z-C-S29 @355e85e46d; disarm owner this seat)

**Read by this seat:**
- `opal-amgt-scoped-api`: MemorySize **1769 MB** (about 1 vCPU), Timeout 29 s, CodeSha256 `E+FAZF0f...` (07:45:38Z). There has been no
  deploy since.
- The day route (`scoped_amgt.py:4702-4724`) reads the gold `article_security_mention` snapshot. It then calls
  `publication_gold._latest_articles_for_keys`, which reads each involved publisher's whole latest silver (bbg 85 MB, wsj 76 MB, per
  CVO~Z) to fetch headlines.
- CloudWatch per CVO~Z: 0 timeouts in 694 invocations from 05Z to 09Z, then the first at 10:14:25Z.
- The silver grows all day while the HARVST collectors run, so the cold read crossed 29 s. Each timeout kills the sandbox, and
  the warm cache never forms.

**Ruling 5 -- this is round-60 ruling 1's exception (a served-route defect on the demo path). `2.0.0_SA_COO~Z` owns it; ONE issuance
or direct acts; due by 12:15Z, before the 13:00Z demo.**

| track | act | criteria shape | class |
|---|---|---|---|
| A (now) | **Raise the function's memory to 3538 MB (2 vCPU)** via Terraform `safe-apply`, with the NEVER-2 entry opened and closed. If 3 cold direct invokes of BA `timeline/day/2026-09-08` do not all finish under 20 s at 3538, go to 10240 MB and measure again. | 3 of 3 cold invokes under 20 s, measured with the sandbox recycled (`update-function-configuration` resets it). A served value equal to the pre-incident value on one control day (a day that answered before 10Z) | config only; no served value moves, so no never-widen pair. Rollback: the memory back to 1769 |
| B (if A misses 20 s, else post-demo) | **The day route never dies on the read.** `_timeline_silver_articles` runs under a deadline (about 20 s). On the deadline the route serves the day's mentions with `headline: null` and a plain reason, instead of a sandbox kill. | a planted slow silver read returns 200 with mentions and the reason, not a timeout; normal days are unchanged | code; this moves served output only on the timeout path, so it carries the never-widen pair |
| C (post-demo, round 62) | **The day route stops reading whole-publisher silver:** headline and `published_precision` ride the gold mention row, or a per-day article index does | cold BA day read under 5 s at 1769 MB | HARVST producer + RESAPP reader |

`2.0.0_SA_COO~H`: the collectors keep running, and nothing here holds them. Track C's design input is yours.

**Ruling 5a (~11:0xZ, on CVO~Z msg 28411, DSGN v24 @09dc9ccf15) -- track B is now the demo guard, not a fallback.**
- **Track A as read by CVO~Z:** 10240 MB (the Lambda maximum) since 10:55:16Z. 15 of 15 concurrent BA day invokes answered 200,
  with 0 timeouts. 9 were cold, at 12.4-20.0 s handler time; 7 of 9 were under 20 s and 2 sat at it. **The hazard is disarmed in
  fact, but the margin is about 9 s to the 29 s gateway, and it shrinks as the collectors grow silver.** Memory has no headroom
  left.
- **Ruling:** `2.0.0_SA_COO~Z` lands **track B** before the demo.
  - `_timeline_silver_articles` runs under an **18 s** deadline measured from handler start. That leaves room for a cold init
    inside the 29 s gateway.
  - On the deadline, the route serves the day's mentions with `headline: null` and one plain reason ("headlines are still
    loading for this day"), as a 200.
  - It carries the never-widen pair: served output changes only on the deadline path.
  - Criteria:
    1. a planted slow silver read returns 200 with the mentions and the reason;
    2. two control days' bodies are byte-equal to their pre-act bodies;
    3. 3 cold BA day invokes answer 200.
- **Freeze:** if track B is not deployed AND graded by **12:30Z**, it does not deploy before the demo. Track A stands alone, and B
  lands after the 13:00Z read. No deploy to this function between 12:30Z and the end of Andrew's demo read.
- **The collectors keep running** (HARVST, "we do not accept any defeat"). This seat does not pause collection to protect a read
  path.
