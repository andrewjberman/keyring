# Current state of AMGT_HARVST and ETFS_RIVALS, as understood by this seat -- 4.0.0_SA_CRO~Z

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

**Date:** 2026-10-01 ~01:00Z (2026-09-30 ~21:00 ET). Window since the last log (`e7885d1020`, 21:10Z): the COO~H sync,
first-light build, rehearsal and arming; plus a fresh read of both projects' commits for this state picture.
**Task Order:** ad hoc. Andrew-direct: "need a /log that covers your understanding of the current state of AMGT_HARVST
and ETFS_RIVALS".
**Status:** COMPLETE.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `git log` (by project token) | PASS | Every claim below cites a commit read at ~00:5xZ. |
| `.tools/aws s3api list-objects-v2` (JSON form) | PASS | Served-reality census of `opal-data-etfs`. The JSON form is the positive-control form; the `--query KeyCount` form printed "None" earlier today for populated prefixes. |
| `blp_client.reference_data` (IBM probe) | FAIL (environment) | No blpapi session on 127.0.0.1:8194, although `bbcomm` has run since 16:55 ET: the Terminal is not logged in. |
| `Get-ScheduledTask` | PASS | The first-light task is registered and Ready. |

- **What worked:** reading each project's own commit trail rather than its status prose.
- **What failed:** no new tool failures beyond the Bloomberg environment.
- **Gap:** none new.

---

## AMGT_HARVST: the news harvest (five publishers: sa, ft, wsj, bbg, barrons)

**Owner of execution:** 2.0.0_SA_COO~H. **PRD:** `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` v0.12, signed by
the CVO @`fb6cb5a767`.

**Endpoint, newly widened:** FWD-10 was appended at v0.12, its DONE WHEN confirmed by Andrew ("2yes", ~21:0xZ).
- Collection runs from a stored long-lived token over each publication's REST shape, with no crawler, login page or
  desktop.
- A sign-in happens on the same host only when the token probe fails.
- The site Z box may serve until the local job matures; a cloud host is the end state.

**What works today (measured):**
- **sa:** account 200 and authorized; a live listing returned 20 dated hits (round 30, ac-2).
- **ft:** works after a real-browser warm-up. CRO trial 1 measured search and article at 200 for 12+ minutes, and the
  first-light rehearsal at 21:44Z measured in-tab search 200 (24 hits) and article 200.
- **The served plane:** `chatter_daily` part-20260930T181745Z (52,143 rows); `/timeline` serves
  `publishers_found_codes` (round 30, ac-3).

**What does not work (measured):**
- **bbg (PerimeterX), wsj and barrons (DataDome):** they refuse outside-client REST even with fresh cookies.
- **This box's IP:** flagged as of 19:44Z. An anonymous fresh browser was challenged on the bbg and wsj homepages.
- **The cause** is refused automated requests degrading the IP (CRO trials 1-3b, `HARVST_BOT_OPS_STUDY_20260930.md`),
  not volume (pacing is ~20 s).
- **The rule since then:** no traffic to those three from the box until first light (CTO round-30 ruling 2; the
  playbook's step 0).

**Round 31 (in flight; issued @`fa71ab063e`):**
- **ad-1, the token store: COMPLETE** @`29984dd835`. The wsj and barrons bundles were written to AWS Secrets (two new
  secrets, stored hash equal to the local file).
- **ad-2, sa batch 1: first pass reached 0 names** @`87661b48c6`.
  - A sorted-keys defect in the plan file made BA run first. One listing page was OK, then its article returned 502,
    giving `upstream_unavailable` and a 15-minute cooldown.
  - The other 9 names sent 0 requests.
  - Fixed @`ed40d75777`. Phase A2 was re-signed by the CTO @`288a4b254c`; the STOP set now includes
    `upstream_unavailable` and `cooldown`.
  - COO~H said the batch ends by 08:00Z.
- **ad-3, the residential-IP read: COMPLETE.** ASSIGNABLE: the Bright Data residential sticky pool is reachable as a
  proxy client via `astn/brightdata/residential-proxy`.

**First light (this seat's act, agreed with COO~H in msg 27390):**
- Task `OPAL_HARVST_first_light_20261001`, one-time, **2026-10-01 05:00 ET (09:00Z)**, Ready at 00:5xZ.
- Publishers ft, bbg, wsj, barrons, on the box's own IP, **without** the residential arm (CTO ruling relayed in msg
  27405: a site Z residential arm needs Andrew's per-use word).
- Per publisher: an anonymous homepage; then, if clean, a stored-session homepage, an in-tab search and an in-tab
  article. It stops at the first challenge and removes itself.
- Rehearsed five ways before arming (`HARVST_CRO_COO_H_SYNC_20260930.md`, "First light: armed"). Results:
  `.runtime/harvest-first-light/<run_id>/summary.json`. COO~H grades them into the round-31 analysis.
- **The open question it answers:** has the box IP recovered overnight, and do bbg, wsj and barrons accept in-tab
  REST on a clean IP? That decides the per-publisher method: in-tab REST, page parsing, or another egress.

**Gaps this seat has flagged to COO~H** (`HARVST_CRO_COO_H_SYNC_20260930.md`, not yet cells):
- the collector's TLS-versus-user-agent mismatch (`publishers.py:290-292`);
- discovery routes other than search (search is the most protected endpoint);
- a mechanical guard refusing outside-client jobs for bbg, wsj and barrons.

**Open at Andrew:** the Bright Data residential arm on the site Z box (per-use word). The cloud host (EC2 with the
residential IP) is approved for later.

**My read of the critical path:**
- first light (05:00 ET) leads to COO~H choosing the per-publisher method;
- that leads to the slow 05:00-08:00 ET job Andrew described (about one request a minute, open browser contexts, stop
  at the first challenge);
- that leads to FWD-10 on the box, and then to the cloud host.
- The risk is the box IP: if it has not recovered by morning, the in-tab question cannot be answered from this box, and
  the residential arm (Andrew's word) or the EC2 host becomes the next step.

---

## ETFS_RIVALS: rival active-ETF research (two peer groups)

**Owners:** 2.0.0_SA_COO~RV (rounds) and 1.0.0_SA_CTO~Z (PRD). **PRD:**
`org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.6, CVO ratified-text half signed @`6496028cb9`.

**Endpoint:** FWD-1 to FWD-12, with Addendum A approved by Andrew.
- FWD-1 covers both Opal funds, IDVZ and PFOE, each with its peer group.
- FWD-5 is the trade schedule at the 0.2% floor, with income and corporate actions excluded.
- FWD-10 is the style read.

**Recent rulings in the PRD:**
- **v0.5 (C-HOME-PRODUCER (b), Andrew "1b"):** ETFS_RIVALS reads the existing Positioning pull for IDVZ and PFOE. Any
  grain shortfall is stated as an FWD-2/3 limit, and there are never two producers.
  - Executed in RIV-b-1 amendment 2 @`bf56b2af54`: `silver_bloomberg` excludes the home funds before writing.
- **v0.6:** G9's style gate is now recurrence: peak book-share days on a quarterly or monthly grid, at least 3
  occurrences over at least 2 years. This is this seat's style-read proposal; SCHY passes as the control and INEQ reads
  systematic (`STYLE_READ_PREVIEW_20260930.md`).

**Round 2: 8 of 9 orders complete** (@`d6ccbc3709`).
- RIV-p-2 built page v2, grouped by Opal fund, home fund first and marked, with a per-fund history calendar.
- RIV-h-1, RIV-g-4 and RIV-b-1 are drained.
- **Remaining: RIV-d-3, the live join.** It publishes new `canonical_shape`, `trade_schedule` and page revisions from
  the rewritten producers.
  - Both halves are signed (COO @`d6f7c6956d`; CTO @`350df49995`) with one condition (amendment 3 @`256aad63aa`).
  - After G3 (corporate actions) lands and before G5 (trade schedule) writes, `key4_served_delta.py --with-g3` must
    again read 0 BASG value changes, with only label cells moving. Anything else stops before G5 and the page.

**Served reality** (`opal-data-etfs`, JSON listing at ~00:5xZ):
- The page's newest object is still `rivalfunds/etfs/platinum/page/date=2026-09-30/` (revision 12:33Z, round 1, BASG
  thread). Page v2 is built but not yet published; it waits on RIV-d-3.
- `bloomberg/etfs/bronze/` and `bloomberg/etfs/silver/`: 0 objects. No IDVZ-group Bloomberg data is in the pipeline yet.
- `rivalfunds/etfs/gold/style_read/` and `rivalfunds/etfs/gold/peer_group_map/`: 0 objects.

**Evidence this seat holds** (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/`):
- the IDVZ-group Bloomberg daily census (501 days, 0 errors);
- issuer route findings (only TXUE scriptable);
- the cash-line contamination (4.7-59.2% of naive trades);
- DVD_HIST_ALL corporate actions (13 events) and scrip (immaterial);
- trade-inference feasibility;
- the style-read preview.

Raw data is in `.runtime/etfs-rivals-idvz-20260930/` and `.runtime/amgt-reconn-daily-census-20260929/`.

**Risks I see:**
- **Bloomberg is not logged in** (probe failed at ~00:5xZ). The IDVZ group is Bloomberg-primary (Andrew, point 1), so
  every Bloomberg-fed step (the IDVZ-group bronze and silver, G3 dividend history, G4 prices) stalls until the Terminal
  is signed in. The 07:00 ET morning pull needs it too.
- PFOE has no measured history yet. Its census attempt failed on the connection, not on coverage. Under v0.5 it comes
  from the Positioning pull, so its grain is that pull's.
- G9 is defined but unbuilt; its control (SCHY systematic) has only been shown in this seat's preview.

**My read of the critical path:**
- RIV-d-3 with its G3 condition leads to page v2 publishing (both groups);
- then the IDVZ-group Bloomberg backfill into bronze and silver (needs the Terminal);
- then G5 to G11 for all funds, with G9 under its recurrence gate.

---

## Next Steps

- [Andrew]
  - sign the Bloomberg Terminal in (blocks ETFS_RIVALS Bloomberg legs and the 07:00 ET pull);
  - keep the box signed in through 05:00 ET (first light);
  - the Bright Data residential arm on site Z is his per-use call.
- [2.0.0_SA_COO~H] Grade first light from `.runtime/harvest-first-light/<run_id>/summary.json` after 09:0xZ, then choose
  the per-publisher method.
- [2.0.0_SA_COO~RV] RIV-d-3 under its G3 condition; then the IDVZ-group Bloomberg legs once the Terminal is up.
- [4.0.0_SA_CRO~Z] After first light: the discovery-route census on whichever egress passed (sync note, item 4).
  Available to COO~RV for the G9 build (preview script and data).
