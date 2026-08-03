# Site Z (~Z lane) — MDLP_MONPUB: W1 hold, W4 root cause + corrected pkl, Bloomberg login diagnostic

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

**Agent:** `0.0.0_AB_MSTR~Z` (site Z / Opal Bloomberg box) · **Window:** 2026-08-03T15:02Z -> 16:10Z
*(Base folder, lane in title, per the flat-vs-nested rule. Prior session died ~13:40Z in the machine
hang Andrew power-cycled; this session reconstructed from base MSTR's agentbus catch-up package.)*

---

## Current State (zero-context handoff)

**Startup:** registered PID 21872; inbox Monitor `bfse58770` + agentbus consumer `bl525dpms` both
TaskOutput-confirmed running; repo ff-only `215a7c369 -> 2733bfcef`; `/govern` cron re-armed
`37 * * * *` (job `90893664`, NFRA_VELOCITY scope, XXX.md Step 1b-F row is the carrier); A.3 PATH
92/94 + exercise PASS; audit-archive invoker = the known 12 site-Z device-keying findings, fails
closed, baseline untouched.

**The incident (MDLP_MONPUB), state as of 16:10Z:**

1. **W1 as ordered was WRONG and is HELD.** The "known-good 07-30 output" premise rested on
   execution success; the actual 07-30 build (S3 version `JTV0rndkN387Qf5UhKe3zAMu1p0V08Ak`) carries
   a garbage ST MODEL row (1D +2.22, 1Y -13.64, YTD -6.29, vol 20.79-27.79). Confirmed by direct
   artifact read. W1 fired anyway at 15:05:47Z (`20260803_w1republish-150535`, FAILED) and the
   corrupted 0730 pkl pair was re-uploaded to `uploads/` at 15:14:06Z; my stop-class message landed,
   base MSTR relayed, DS held the manifest write and deleted the re-uploads. Serve stayed at 07-27
   (correct-but-stale) throughout — verified live repeatedly, last at ~15:45Z.
   The 13:27Z 07-27 rerun (`0d669fd1`) was Andrew's DELIBERATE rollback, not an accidental silent
   regression — ~F's mechanism findings all stand, but the incident narrative inverts.

2. **W4 root cause, source-confirmed, both defects:**
   - **0731 dups:** notebook cell 16 appends a one-day DAILY snapshot onto MONTHLY frames; on a
     month-end as-of (07-31) it duplicates the final row. Census (denominators): price_monthly 60
     dup rows of 30,250 (30 series x2, value-identical); return_monthly 168 of 29,079 (84 x2, NOT
     value-identical — daily row is NaN in valuation fields and carries a 1-DAY return); return_daily
     0 of 111,266. Yang's own guard (`and end_date != df.date.max()`) landed in the live notebook at
     13:08Z — fixes future runs, not the uploaded artifact. June-end pkls have 0 dups (append block
     likely added in July).
   - **0730 wrong instrument:** the pkl's `.ST Index` series is a different instrument's full
     request-window history (1449 rows from 2021-01-04, price ~1.9, its 07-30 return +2.216187 ==
     the published +2.22). Same code+window from THIS box returns the correct 676-row series
     (live-probed). Terminal-side resolution defect on the machine that pulled Friday — per-login
     CIX resolution or transient redefinition; discriminating test needs Yang's login.

3. **Corrected pkl PRODUCED, VERIFIED, STAGED (Andrew-direct option b):**
   `s3://opal-data-portal-v2/data-refresh/staging/mdlp-monpub-w4/data 20260731 v1.pkl`,
   VersionId `gvUZKeEiOrVJfvYfR07KBeF0lNof1.jM`, single-part PUT so ETag == md5
   `2a4703465c00f76ce71094db5ae522c0`, sha256 `6cd028605149ef65...def0` (full value in the bus
   message + deliverable script header). Source proven byte-identical to the S3 upload the
   executions read (local md5 == S3 ETag `961a1f5a30f964471e766965a07c2f6a`). Dedup semantics:
   price_monthly lossless (identity asserted per pair); return_monthly keeps the field-bearing
   monthly row WHOLE (a naive `.last()` would keep the NaN-heavy daily row). Verification: the
   exact `build_rfr_daily` reindex precondition passes for all 81 series; ST digit-identical to
   0727 on shared dates and to the live terminal (07-31 close 112.503).

4. **Interval content gate (Andrew's ask): PASS.** Replicated the Lambda's period methodology
   (windows :445-519, compound :525, vol :534, inception 2024-04-30); CONTROL reproduces the served
   07-27 ST row to 2dp on all 10 periods. Corrected-0731 vs served-0727: every interval within
   +/-0.29pp (YTD 1.60 vs 1.62, 1Y 3.59 vs 3.50, SI 4.47 vs 4.50; vols 2.1-3.3); the four new
   trading days compound to -0.01pct. Dashboard-plausible everywhere the portal displays.

5. **Bloomberg diagnostic (Yang/Andrew, live Teams thread):** this box's login is NOT blocked at
   any tested size — probe (2-sec), medium (AAPL 2y daily), and the full 84-ticker production pull
   (Alyssa's successful 08:03 run). Yang's login got `-4003 LIMIT/REVIEW "Access pending review
   [nid:52865]"` on the same code+request → block is login-scoped. Excel-path BDH is
   UNTESTABLE-HEADLESS (bxlafct.exe never spawns under COM automation; `#N/A Requesting Data...`
   is an automation artifact, not a deny). Active login here: the box's own seat (terminal live,
   logged in; profile UUIDs ever used here: 32265165 recent, 33343590 older; UUID->name not
   resolvable from the API side).

**Remaining promote gates (all laptop-side):** W2 deploy (commit `05dcbe7651`, DT), DS re-hash of
the staged object, CTO GO. My producer-source position: sitez path clean (evidenced), Yang-side
`.ST` resolution is the open item and is with Yang/Andrew.

**Corrections to my own record this window (Andrew challenge):** "sitez terminal NOT affected" was
overclaimed at the time it was sent — it was probe-class evidence only. Corrected in-channel; the
full-size evidence (Alyssa's 08:03 pull) arrived later and now grounds the claim properly. The
Friday-pull machine attribution remains INFERRED (YangLiu kernel path evidence dates only today's
interactive session; this box's `blppersist2.db` shows Friday 17:15 local terminal activity too).

---

## MCP / bus traffic (significant only)

~12 bus messages handled. Inbound: catch-up package (`085968b0`), 3 ACKs from base MSTR, DS
option-a pick (`d2926245`, superseded), Yang diagnostic relay (`2961ccc5`), Andrew option-b +
interval ask (`6e78de50`), DS staging key (`9f4129de`). Outbound: package ACK (`8a52a458`), W1 HOLD
(`e3f2babf`), stop-class W1-in-flight (`1fcad744`), W4 root-cause report (`0b50c446`), corrected-pkl
ready (`1141f61e`), Yang diagnostic results (`33f59211`), staged-upload + interval report
(`b9912943`). All inbound ACKed in-turn per Rule 22b.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` (A.3 exercise) | PASS | forwarder ran (banner produced), 92/94 resolve bare |
| owned-paths hook | PASS | install idempotent no-op |
| audit-archive-invoker (A.2) | WARN (expected) | 12 device-keying findings, fails closed on site Z by design; no re-baseline |
| rail-checked raw greps (x3) | OK | non-estate Bloomberg local profile/logs — no comp-tool models terminal login identity |

No `comp-estate`/`comp-pipescript`/`comp-iam` runs: the window was artifact/content forensics on
non-estate local files (OneDrive pkls, notebook, Bloomberg profile) plus operational AWS reads
(s3 get/head/put, stepfunctions list — off-rail); the one estate-source read (the Lambda's period
methodology) was a targeted Read at the path ~F's committed log already cited. No infra/code change
was made from this seat. **Gap noted:** no comp-tool models S3 object-version content diffs — the
load-bearing instrument of the W1 refutation was raw versioned `get-object` + python, denominators
printed.

## Blockers

None of mine. Open at others, evidence-cited: **[0.2.0_DS_PortfolioAnalytics]** staged-object
re-hash + promote after W2; **[0.2.0_DT_PortfolioAnalytics]** W2 deploy `05dcbe7651`;
**[1.0.0_SA_CTO]** GO + whether a formal producer-trace deliverable is wanted; **[Yang/Andrew]**
nid:52865 review with Bloomberg rep + the `.ST` pull test on Yang's login.

## Next Steps

- **[0.0.0_AB_MSTR~Z]** Respond to bus events; `/govern` fires at :37; formal trace doc if CTO asks.
- **[0.0.0_AB_MSTR (base)]** Relay of interval report to Andrew/CTO; W1 TO amendment at CTO.
- Deliverables committed alongside this log: `deliverables/MDLP_MONPUB_W4/dedup_0731.py` (the exact
  transformation that produced the staged object) + `interval_compare.py` (the content-gate check).
