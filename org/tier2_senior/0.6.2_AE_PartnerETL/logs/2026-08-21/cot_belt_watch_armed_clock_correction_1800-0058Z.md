# COT G4/G4b acceptance armed + the clock correction that four seats were holding

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**serial:** 0.6.2_AE_PartnerETL (PID 23176; inbox Monitor bb5aiy7je, belt Monitor bgx6dde2b)
**window:** 2026-08-20 1800Z -> 2026-08-21 0058Z (crosses UTC midnight; continues
`logs/2026-08-20/cot_supervised_g1_g4_bronze_legs_1722-1800Z.md`)
**TO:** COT_SUPERVISED.G1-G7 (bronze legs G1/G4 + the G4b handoff half)

## Current State

**Both bronze legs remain DELIVERED (unchanged this window); what changed is that their
ACCEPTANCE is now correctly dated, instrumented, and armed.**

**THE CORRECTION THAT DOMINATES THIS WINDOW -- MINE.** Andrew instructed *"verify tonight's run
and close when it fires"*, and going to verify is what made me read the schedule I had been
asserting all day. **There is no ~02:00Z cot run.** The chain is `cron(30 7 * * ? *)`
America/New_York = **11:30Z** (Andrew-direct 2026-08-14, MDPF_TRGALN 3 row 4); the `cron(0 2)Z`
Rule I was reasoning from was **DELETED in that same change** (`eventbridge.tf:43-45`). Read at
BOTH planes -- DESIRED `schedule-et.tf:90`; APPLIED `aws scheduler get-schedule
cot-bd-session-daily-et` -> State **ENABLED**, same expression; `comp-trigger` corroborating.
**So the G4/G4b acceptance fire is FRIDAY 2026-08-21 11:30Z.** I had carried the stale anchor
into four messages; CTO (63716) and COO (63713) inherited it FROM MY REPORTS and corrected
their own boards -- four seats, one unverified fact, propagated by citation, broken only by
being told to go look.

**THE CONSEQUENCE THAT MATTERS MORE THAN THE CORRECTION:** today's fire ran **11:31Z, SIX HOURS
BEFORE** my 17:50Z template amendment, so today's 19-column extract is **NOT a G4 failure**.
Had anyone checked "tonight" and found 19 columns, the natural conclusion would have been that
the amendment failed. **A wrong clock does not merely delay a verification -- it FRAMES A
CORRECT ARTIFACT AS A DEFECT** (CTO's phrasing, adopted by COO into the R14 record).

**ARMED AND PREPPED FOR THE FIRE:**
- **Watch:** Monitor `bgx6dde2b`, persistent, on the exact key
  `s3://opal-data-cot/forwardfill_v2/holdings/HOLDINGS_DAILY_2026-08-20.xlsx` -- **confirmed
  ABSENT**, so its appearance is an unambiguous oracle. Emits on **LANDING**, on **OVERDUE past
  13:00Z**, and on **non-404 poll errors** -- silence cannot read as success.
- **Instrument:** `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/COT_SUPERVISED/verify_g4_belt_acceptance.py`
  @`d4a86a84e1` -- 12 checks, every one on SERVED bytes, none reading config to assert behavior.
  **Pre-fire NEGATIVE CONTROL run 20:49Z: 8/12 PASS, failing exactly the four not-yet-true
  cells** -- the instrument can fail and fails in the right places. It also discriminates
  SCHEDULE-landed from HAND-landed on the landing window, which correctly failed G4b against my
  own 17:36Z G1 bootstrap (a file-presence check would have passed G4b on my own hand-run).
- **Baseline, MEASURED not quoted:** served `HOLDINGS_DAILY_2026-08-19.xlsx` = **19 cols /
  18,051 rows / zero supervised columns**. Expected tomorrow: **21 cols / 18,051 rows**.
- **The belt's real test is built in:** per-row `Holding Supervised` vs `Account Supervised`
  disagreement across all ~18k rows, denominator printed, any disagreement listed as a routable
  FINDING rather than a silent pass.

**G4b RUNTIME PREREQUISITES VERIFIED DEPLOYED, NOT MERELY COMMITTED** -- the highest-value catch
of the window. DS landed G4b @`f03ec88563` then went dark. **The repo is not the runtime:** the
SSM doc pulls the script from `s3://opal-data-cot/code/bronze/` at run time (`ssm.tf:121`) and
`load_template` reads the TEMPLATE from that same prefix. A committed-but-undeployed template
would have raised, failed the table, and **SUPPRESSED THE WHOLE CHAIN'S BRONZE SENTINEL** --
breaking tomorrow's entire bronze->silver advance, not just G4b. Verified live and clean:
`code/bronze/cot_bronze_ingest.py` 80,599 B @18:06:50Z (4 `account_attributes` occurrences +
SNAPSHOT_TABLES membership) and `code/bronze/templates/account_attributes.json` 1,225 B
@18:06:01Z. Both re-verified POST-MERGE at HEAD `8aa7120a09` -- local == S3 byte-for-byte,
line-ending-normalized so CRLF cannot manufacture a false differ.

## Blockers

**NONE.** One external gate, correctly dated: the **FRIDAY 2026-08-21 11:30Z** scheduled cot
chain fire. Not deferrable-by-choice -- the acceptance is DEFINED as the scheduled run's output
(an ad-hoc artifact is never production evidence). Session is being held for it per
Andrew-direct.

**One dependency stated honestly:** the belt watch is a session-scoped Monitor and dies with the
session. The verifier is committed and runs standalone, so a successor loses the notification,
not the capability.

## Next Steps

1. **[me, on the 11:30Z fire]** `python .../verify_g4_belt_acceptance.py` -> mint
   `COT_SUPERVISED_PROOF_OF_SPEC_062_20260820.json` (group bronze-G1-G4) -> validate
   `python .tools/proof-of-spec-check.py <instance> G1,G4,G4b` (comma-separated; validator
   confirmed working, and it warns that coverage is UNCHECKED without the expected set -- so the
   set is passed) -> **RAVC close to 2.0.0_SA_COO cc 1.0.0_SA_CTO**.
2. **[0.2.0_DS_PortfolioAnalytics]** G4b behavioral acceptance keys on the SAME fire (sentinel +
   silver consuming the prefix). Seat was DARK at 20:45Z; my clock correction to them is QUEUED,
   not delivered -- **they may still be holding the stale "tonight" clock on respawn.**
3. **[0.6.0 lane, routed via COO]** the `endpoints/README.md:59` doc fix (POST-updates claim is
   false at the wire; true verb is PUT with id in BODY, response carries no id, verify by fresh
   GET diff).
4. **[whoever draws DATA_BDINSURANCE W1]** the discriminating asOfDate test on the 4 Voya
   accounts ($26.0M, supervised, flat across the Q2 close). My seat holds the wire mechanics and
   can execute same-session if routed.

## MCP traffic

**~13 messages handled; 8 outbound acts.** Significant only:
- **OUT -- the clock correction** (63705/63706/63707, 3 recipients): both planes read, the old
  anchor's DELETION cited, baseline measured. CTO named it "the standard" and owned his share
  (63716); COO corrected its log + the R14 record and landed the Friday sequencing line
  confirming the two acceptance events are **seat-disjoint** (63713, 63723).
- **IN -- DATA_BDINSURANCE reframe** (63541/63551): Andrew narrowed it BACKEND-ONLY; CTO minted
  RESTATEMENT as a third value-change class and measured $41.6M of the current book already
  value-only. **OUT (63558-thread):** I surfaced that BD's **`Position Only`** flag (117 True in
  my G1 extract) is the vendor's OWN declaration of the no-timing-data class. **CTO adopted it
  as the PRIMARY `valuation_basis` anchor** on my cold-start argument, and the cross-tab it
  enabled found the 4 Voya accounts -- **90% nest by count, only ~37% by value.**
- **IN/OUT -- F-010 VARIANT** (63790 -> 63798/63799/63800): `-F` protects the invocation, not
  the message-file BUILD. Audited my 5 commits: **3x `<<'EOF'`, 2x single-quoted printf, zero
  unsafe forms.** Corroboration sent: `d4a86a84e1` carries a **real, succeeding** backticked
  command in the permanent record, which under a double-quoted heredoc would have executed and
  spliced JSON silently.
- **IN/OUT -- merge window** (63970 -> ACK, 63990 -> ACK): held commits, verified nothing
  staged, and **re-ran MSTR's own declared void-condition** post-merge for my acceptance pair.

## Files Modified

See commit message: `d4a86a84e1`. One new file (`verify_g4_belt_acceptance.py`) + the
`2026-08-20` log's clock-correction addendum.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-which | "when does the cot nightly pipeline fire and is its schedule enabled" | PASS -- routed to `comp-trigger` (top of 77, score 1.50); the routing was correct and I used the tool it named |
| comp-trigger | `comp-trigger cot-bd-session --days 3` | PASS -- 136 events-rules + 18 schedules scanned (denominator printed); scheduler ENABLED + both chain rules FIRED in window. Its own output correctly labels the TF hits "declared-ness ONLY -- a text hit cannot tell landed from planned" |
| aws scheduler get-schedule | live primitive, `# rail-checked` marker | PASS -- APPLIED state ENABLED; the layer `comp-trigger` structurally cannot supply (Rule 22a) |
| proof-of-spec-check | dry run on DS's instance | PASS -- VALID rc=0, 7 rows; confirmed the validator works and learned the arg convention BEFORE close time |
| comp-pipescript | NOT RUN -- deliberate | no gold script touched and no gold run triggered this window; the bronze deploy-currency question is answered by reading the DEPLOYED S3 bytes, which is what Rule 22a actually demands |

**What worked:** `comp-which` -> `comp-trigger` routed correctly on a plain-English schedule
question, and `comp-trigger` prints its denominator unprompted. **The two-stage discipline is
what caught the clock**: the comp-tool localized, the live primitive settled APPLIED truth.

**What failed:** nothing tool-side. The failure this window was MINE and pre-tool -- I asserted
a schedule for a full day without ever running either check, and three other seats inherited it.

**Gap found (recorded, not chased):** no comp-tool models `aws_scheduler_schedule` APPLIED state
-- `comp-trigger` covers dispatch forensics and reads TF for declared-ness, so an
EventBridge-Scheduler **enablement/expression** claim still requires the raw live primitive
behind a `# rail-checked` marker. Given that a stale schedule fact just propagated across four
seats, this is a coverage gap worth naming to CTO at cadence rather than a convenience issue.

## Note for a successor

`.comp-graph/.agent_context` read `SERIAL=3.0.0_SA_CVO~A` at 0058Z -- another seat overwrote the
shared last-writer-wins file, exactly as `org/XXX.md` warns. **It is not an identity source.**
My identity holds from `org/mcp/sessions/{session_id}.serial` + my armed inbox Monitor. Do not
resolve a serial from that file.
