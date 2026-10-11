# Active projects by box -- status, blockers, and the last six hours

**For:** Andrew. **By:** 1.0.0_SA_CTO (laptop), 2026-10-09 ~15:20Z, **updated ~19:00Z** (see the UPDATE section). **Window:** commits on `CLOUD` from 09:00Z to ~15:05Z, all times UTC; the update covers 15:15Z-18:55Z.

**Sources:**
- Every project's `project.json`, latest round analysis, task-order statuses and issue rows (the per-project issue logs the seats call surprise channels).
- `git log` of each project folder.
- The cluster open-calls list (~15:10Z), and `sequence-check.py`.

**How a box was assigned:** by the seats actually doing the work. COO lanes ending `1` are on dell1, `2` on dell2, `Z`-family on site Z. A project's register `fabric` field is NOT used, because it is stale for 12 projects (see "Register drift" in the summary).

**Words used:**
- **Round:** one build cycle. The CTO lists the work, a COO issues task orders, workers build, the CVO (the verifier seat) grades, and the CTO analyses.
- **FWD-n:** one of the project's promised outcomes. **MET** or **REALIZED** means it was graded done.

---

## UPDATE ~19:00Z -- new state since this report was written (~15:20Z)

**Window:** 15:15Z-18:55Z, 856 more commits across the four boxes. The sections further down still describe the 09:00Z-15:20Z window. Where they disagree, this update is the current state.

### Headlines

1. **Client account data reached the repository (16:00Z) and was contained within about an hour.**
   - A dell2 worker committed a file holding data for 121 client accounts; it reached `CLOUD`. A census then found about 130 tracked files under Investor Reporting carrying account numbers.
   - All were moved out of the repo or redacted to hashed `acct#<8hex>` tokens: ADVI_COTBKF orders, IRPT_DASHBD and IRPT_BCKEND files, and 11 issue-log files (by the CVO).
   - A content-reading commit check now exists on all four boxes (details in the process report).
   - **The files remain in git history: purging them is your decision.**
2. **Three projects CLOSED with every outcome met:**
   - DSGN_AMGTV1, 26 of 26 (78294bf9ee, 17:22Z);
   - LGIC_ENFORCE, 7 of 7 (65cfdb8978, 18:00Z);
   - NFRA_GATSCP, 8 of 8 (45f5fc4fd9, 18:03Z).
3. **Two idle laptop projects moved to dell1 and now have COOs:**
   - MDPF_CANON (`~D1`; 60f7b56293, seated 7b0f032171);
   - LGIC_CANON (`~B1`; 198b235f94, seated da56779806).

   The laptop now runs only NFRA_CTLPLN.
4. **Two journeys now work end to end:**
   - **TCKT_VNEXT:** the Ticket Center's first journey ran end to end (66bfdf5c2e).
   - **NFRA_OPALAI:** the Opal Analyst's closing test passed on a fresh message (349edef03b).
5. **site Z's Control Plane page is live** at https://mcp.opalinvest.dev/control-plane (e9a1bf5127).

### Your list now (acts only you can do; cluster list read 18:57Z)

| Box | id | Act | Note |
|---|---|---|---|
| site Z | `-9f24` | Barron's sign-in | unchanged |
| site Z | G-MSPID | MSP calling identity and its MFA sign-in | unchanged ("Not yet") |
| site Z | `-21c5` | **NEW:** open https://mcp.opalinvest.dev/control-plane once and name one box's projects (~1 minute) | closes NFRA_MCPORTAL FWD-14 |
| site Z | `-f0d2` | **NEW:** sign in once as the Opal Bloomberg account in a browser window site Z opens (~2 minutes) | NFRA_MCPORTAL FWD-2 |
| site Z | `-a519` | Send one Teams message to the Opal Bloomberg account | **probably no longer needed**: that test's arm (b) passed on a fresh message at ~18Z (349edef03b); site Z should close it |
| dell1 | `-86a2` | Rotate the Anthropic API key | unchanged |
| dell1 | `-203a` | Is Opal_Muni_Sleeve Opal's Muni SMA? | MDPF_STRATID's planted-sleeve test passed (8125d09ffe); the organic check is due 2026-10-10 13:30Z |
| dell1 | `-f23d`, `-838c`, `-5f4b`, `-69ef` | Cleanup deletes (1 stray S3 file, 2 empty Terraform states, 1 log group) | unchanged; `-bf6d` and `-c20b` are duplicates still listed |
| dell2 | `-62ea` | Delete `C:/dev/_scratch265` | unchanged |
| dell2 | `-3082` | Research Team Meeting transcripts: invite, or an M365 transcript policy | unchanged; 29 of 34 meetings landed |
| dell2 | `-3cb1` | Alyssa files one Analysis request on portal DEV | unchanged |
| dell2 | `-fbb1` | Close test ticket TCK-20261009-a1052909 | unchanged |
| all | -- | **Purge the client-data files from git history (yes/no)** | **NEW; my recommendation is yes** |

**Closed since 15:20Z:**
- `-2f53` (the FWD-8 return tolerance, ruled at 0.35 percentage points; closed on both sides);
- `-886a` (the transcript reader holders, closed on both sides).

### What changed since ~15:20Z, by box

**dell1** -- three projects closed, and two moved here from the laptop and now have COOs.
- **DSGN_AMGTV1** -- CLOSED at round 68, 26 of 26 outcomes (78294bf9ee). Portal PROD moved to portal-v2.1.211, a change to the staff-only Security Analysis page.
- **LGIC_ENFORCE** -- CLOSED, 7 of 7 (65cfdb8978). A one-cell follow-up round was re-closed at 18:21Z (c38826976d).
- **NFRA_GATSCP** -- CLOSED at round 4, 8 of 8 (45f5fc4fd9).
- **AMGT_RESAPP** -- round 86 closed (64c5f8d6fe), and kk-1's name list was republished from the laptop. The NU description graded not met (2eba7c172b), so round 87 was issued with four orders (433e2b510d).
- **AMGT_CORPUS** -- round 41 graded MET (73eebd934a). Round 42 was issued, and its rewrite has both sign-off halves signed (cc7aeaa601).
- **AMGT_HARVST** -- the collector fix merged (e086d0b429), and the round-79 re-pin was released to site Z. No live collection cycle has run yet.
- **MDPF_SECHIST** -- a dry run of the gold job matched the served page 1,520 of 1,520 cells (9842e9a0d5). Both halves are signed, and the deploy went to a new deploy lane `~SC1` (57d6e1eab3).
- **MDPF_STRATID** -- round-2 deploys D1 and D2 landed (6259c6efbf). The planted-sleeve test graded MET (8125d09ffe). The organic check is a dated wait until 2026-10-10 13:30Z.
- **ETFS_RIVALS** -- the lookup is live (5e3d4f0a97). The tc-1 merge waits for site Z's manager window at 2026-10-10 06:00Z.
- **MDPF_DEMQUE** -- 16 history cells booked (da5f4eddee). New finding D1-S6: the uploader writes ETF history cells as empty (81eea42ed9). Next: the 02:30Z draw.
- **MDPF_HEALGAP** -- a dated wait was confirmed; the next checks are at 20:00Z and 2026-10-10 07:15Z.
- **MDPF_SECCLASS** -- removed three records that paired a client relationship id with its holdings (9b96ca20cd). It waits on the 23:00Z run.
- **MDPF_CANON** -- moved here with `~D1` seated, and PRD v2.9 is signed (d8ef27e783). New finding D1-S1: three tests already fail on dell1's branch before any change (0d5563e370).
- **LGIC_CANON** -- moved here with `~B1` seated. Round 5 was issued with three cells (dcea6794eb).

**dell2** -- the redaction sweep dominated, with real progress on the 49 Financial bundle, Teams transcripts and tickets.
- **ADVI_COTBKF** -- all 7 parked orders were redacted (5cda488073, 10f554dde2). Rounds 50-53 ran, and COT gold was redeployed and read back equal to the repo (a1d34b066e).
- **IRPT_DASHBD** -- the gold Lambda's memory went from 2,048 to 3,008 MB under a signed pair (7033c30a1c). The 990 out-of-tolerance segments were re-graded (c351fa8186).
- **IRPT_BCKEND** -- the 49 Financial bundle (IB-pr-417) was rebuilt with the memory fix, and both halves are signed (c7b3f175b7). The performance adapter is failing (row D2-S60, 7364c85e16).
- **IRPT_ANLREQ** -- release 1 revision 5 is live, using password window 5 (e4a57bee63). Its R3 check then found a code mismatch (d086ccf09f).
- **IRPT_YCDGEN** -- irpt-status revision 4 crashed and was rolled back to revision 3 (f551980c99). Under revision 5, R3 passes but R4 is still refused.
- **NFRA_TRNSPT** -- the first scheduled Teams landing ran at 16:00Z. Round 21 closed (bbaa367ce5). A census found 29 of 34 meetings landed; round 22 hunts the 4 missing Monday meetings (0f551cca1f).
- **TCKT_VNEXT** -- the main journey ran end to end on run 4 (66bfdf5c2e). The sign-off pair's rollback clause was corrected (3edb75d80a).
- **No commits:** NFRA_OPSWKF. ADVI_BILLING moved only through site Z's release order.

**site Z** -- the Control Plane page is live, and gateway releases queue on the one host.
- **NFRA_MCPORTAL** -- Control Plane LIVE (e9a1bf5127). MP-r-2 stopped at a 31.6-second read against a 30-second limit (row Z-S30).
- **NFRA_OPLGTW** -- the release carrying ADVI_BILLING's Excel tool is cut, with all three halves signed (5e258448d2). It deploys after MX-r-9 and MP-r-2.
- **NFRA_MCPINDEX** -- MX-r-9 phase B was re-cut on the live gateway, and the COO half is signed. The apply is held behind the queue.
- **COMM_ASSIST** -- the real deploy applied nothing, because the package carried unreviewed lines. The build was pinned, all halves re-signed, and GO was re-issued at 17:48Z (f453cdd6bd).
- **NFRA_OPALAI** -- closing test arm (b) PASSED (349edef03b). Arm (a) still waits on site Z's own call `-4d5a`.
- **NFRA_IAMROLES202609** -- round 6 was issued to a new deploy lane, `~IR`, and phase A is in flight.
- **NFRA_MCPMSP** -- no change; held on your act G-MSPID.

**laptop**
- **NFRA_CTLPLN** -- password windows 3 (24 minutes) and 5 (7 minutes 54 seconds) opened and closed inside their limits. New issue rows: S9108; S9109 (the cross-box send fails on Windows); D1-S6; D1-S7.
- **My acts as control plane since 15:20Z:**
  - client-data check (8c1d8a1966);
  - task-order gate redaction and rename support (9caacb0f35, 24bdcd2690, b2d3d8e749, 8fff05ca26);
  - safe-deploy summary now counts bundles (dd78f5dd5e);
  - deploy-check hook fires only on closed ledgers (d29f2f61de);
  - MDPF_STRATID round-2 sign-off (07ee308141);
  - password windows 5 and TO-APPLY-30 (91d0d7982c, 075fab8835);
  - site Z rulings (441f2f547d, ca14ebabec);
  - MDPF_CANON and LGIC_CANON moved to dell1.

---

## Summary

| Box | Active projects with work today | Commits on their folders since 09:00Z | Headline |
|---|---|---|---|
| **dell1** | 13 | ~570 | Busiest research and MDPF box. LGIC_BLANKFIX (9 of 9 outcomes) and NFRA_GATSCP closed rounds. One production break (MDPF_STRATID) was rolled back in 7.5 minutes. |
| **dell2** | 9 | ~410 | All Investor Reporting work, the Cottonwood backfill, transcripts and tickets. The R44 gold release went live, and the FWD-5 transcript reader went live. The 49 Financial bundle publish is still open. |
| **site Z** | 7 | ~155 | Gateway release r29 went live at 12:46Z. Three deploys now queue for the one gateway host. NFRA_MCPMSP is held on your sign-in act. |
| **laptop** | 1 (NFRA_CTLPLN) | ~30 | The control plane. The laptop also signs the IAM changes and password windows the Dells need, and its CTO ruled cross-box calls all day. |
| **idle** | 29 registered "active" | 0 | About 12 look stale or duplicate and should be closed. |

- **Total:** 59 projects read "active" in the register (398 scanned). 30 moved today, and 1,573 distinct commits landed in the window.
- **Register drift:** the register says `laptop` for seven projects that run on dell2, and `site-z` for five that run on dell1. MDPF_HEALGAP also still reads `laptop`. This is my fix to make (the register is the CTO's).

### Everything waiting on you (acts only you can do)

| Box | id | Act | What it unblocks |
|---|---|---|---|
| site Z | `-9f24` | Barron's sign-in (the saved session is refused) | AMGT_HARVST's WSJ/Barron's collection |
| site Z | G-MSPID | Supply the MSP calling identity and sign it in with MFA (multi-factor authentication). Your last word: "Not yet". | NFRA_MCPMSP (held) |
| dell1 | `-86a2` | Rotate the Anthropic API key (it was printed into a local transcript; never committed or sent) | security hygiene |
| dell1 | `-203a` | Is Opal_Muni_Sleeve ($550,823) Opal's Muni SMA? | MDPF_STRATID FWD-3 |
| dell1 | `-f23d`, `-838c`, `-5f4b`, `-69ef` | Delete one stray S3 file, two empty retired Terraform state files, and one orphan log group | nothing; cleanup |
| dell2 | `-62ea` | Delete `C:/dev/_scratch265` (21 MB of worker scratch) | nothing; cleanup |
| dell2 | `-3082` | Research Team Meeting transcripts: get the gateway account invited, or have a Microsoft 365 admin grant a transcript policy | NFRA_TRNSPT FWD-2 |
| dell2 | `-3cb1` | Alyssa files one Analysis request on portal DEV | TCKT_VNEXT live proof |
| dell2 | `-fbb1` | Close test ticket TCK-20261009-a1052909 | TCKT_VNEXT cleanup |

**Since the morning list:**
- `-2caa` (walk Security Analysis on PROD) is retired: FWD-1 was graded by a signed-in seat.
- `-20b4` (a market-update deck) is answered by your folder pointer.
- `-bf6d` and `-c20b` are duplicates I ruled closed; they still show OPEN on dell1's list.

---

## dell1

**dell1 is the busiest box:** 13 active projects, about 570 commits, and 11 COO lanes. dell1 also runs its own CTO (`1.0.0_SA_CTO~DELL1`) and manager (`0.0.0_AB_MSTR~DELL1`).

- **Closed rounds:** LGIC_BLANKFIX and NFRA_GATSCP each closed a round with every outcome met.
- **One live production break:** MDPF_STRATID broke a production job at 14:51Z and rolled it back 7.5 minutes later.

### AMGT_RESAPP -- Security Analysis research pack, automated (model block, company description, segments)
- **Status:** executing, round 86 issued at 14:29Z (COO `~R1`). About 107 commits, the most on dell1.
- **Done:**
  - Round 85 closed with all 5 orders complete (b6eac72a7c).
  - The scoped API is live, and all three of its acceptance checks pass (a2e2d4f27b).
  - The CVO graded the served draft for NU clean: 38 of 38 sentences verbatim and cited (d5bf2ba8cd).
  - Round 86 was issued as five orders (4aa37450fe). Order kk-2, the company description from the business section, is complete (8bed441aab).
- **Waiting on:**
  - kk-1, the name-list republish, needs a laptop deploy seat (cross-box order b9dd45c1ff).
  - kk-3 edits five stored drafts in place, which needs a paired sign-off. The COO half is written (1380a0f2cd).
- **Next:** drain round 86, then the grade.

### DSGN_AMGTV1 -- Security Analysis portal page redesign (staff-only)
- **Status:** executing, round 67 issued at 14:42Z (COO `~D1`).
- **Done:**
  - Rounds 58-65 are live on portal PROD (portal-v2.1.210).
  - **FWD-1, the main journey, is graded MET** (eed6b7b743): Valero was picked by name and its header figures served, on a signed-in walk of PROD.
  - FWD-7 is MET: officers are shown with a source.
  - 23 outcomes are realized on record.
- **Waiting on:** nothing. Round 67 targets FWD-8 (peer tickers and currency) and FWD-27 (one format per measure).

### MDPF_DEMQUE -- backfill demand queue (history backfills drawn within the Bloomberg and Yahoo budgets without starving production)
- **Status:** round 7 (COO `~Q1`).
- **Done:**
  - Round 6 closed.
  - Non-trading-day quoting is live (57c75a37a8).
  - A quote with no finish date now reads UNQUOTED instead of erroring (7c6d6cfd68).
  - A one-cell Bloomberg read was booked for MDPF_SECHIST (df823bf77a).
- **Waiting on:**
  - The Saturday backfill (t24) runs at site Z, and that seat reports that the warning and stop interfaces it needs are not exposed to it (b7d7a0db94). The COO must amend the order before Saturday.
  - Your act `-f23d` (optional cleanup).

### ETFS_RIVALS -- rival-fund research (six rival active ETFs, holdings, a daily page)
- **Status:** round 28 (COO `~V1`).
- **Done:**
  - The daily Lambda can read the one Bright Data key secret, by exact name (86c14e4b3a).
  - Both halves of the deploy sign-off are signed. The CTO's condition: a wrong corporate-action row is voided by a seat, never removed by an S3 delete. Order wk-1 builds that.
  - The deploy order was issued (84b51c181a).
- **Waiting on:** wk-1 ships first, then the deploy rides the scheduled windows.

### AMGT_HARVST -- publication harvest (every mention of a covered company, with its source)
- **Status:** round 77 (COO `~W1`).
- **Done:** round 76 graded MET (20 of 20 kept mentions true, 8e239604e5).
- **Real defect:** the site-Z collector runs but collects almost nothing (row D1-S3).
  - Bloomberg: 96 cycles, 0 items.
  - WSJ and Barron's: 0 attempts.
  - The "sa" source: 3,324 of 3,339 items rejected.
  - Nothing has reached silver since activation at ~12:57Z.
- **Waiting on:** site Z's diagnosis orders bu-1 and bu-2, then a fix round. The WSJ/Barron's half ties to your Barron's sign-in (`-9f24`).

### MDPF_SECCLASS -- one canonical classification table per security
- **Status:** round 18 closed (73344395e2); round 19 waits on scheduled runs (COO `~M1`).
- **Done:**
  - Both gold test suites are green on the CVO's own runs: Black Diamond 99, COT 28.
  - The COT port is live (4a05003ec3).
- **Waiting on:** the scheduled runs at 23:00Z, 04:00Z and 11:30Z. An ad-hoc gold run was ruled out.

### LGIC_BLANKFIX -- every broken resource name gets a complete fix
- **Status:** **round 14 closed with 9 of 9 outcomes realized** (6d071ac6da, 14:49Z; COO `~B1`).
- **Done:**
  - Firm schedule names come from the builder, and 31 of 31 pass the live gate (43f6416fed).
  - 180 schedules checked: 148 agree, 32 are partial with a reason, 0 mismatch (a6ed571cb7). The CVO confirmed it independently.
- **Waiting on:** dell1's CTO marking it complete. Your cleanup deletes (`-838c`, `-5f4b`, `-69ef`) block nothing.

### NFRA_GATSCP -- GitOps gates that refuse only what the act itself breaks
- **Status:** round 3 at close (d2eeb6579f; COO `~N1`).
- **Done:** six gate fixes merged and confirmed on live data:
  - Line-ending normalisation in the pipeline gate.
  - round-close-check reads an order's status word correctly.
  - The receiver of a cross-box record commits its own copy.
  - safe-merge refuses a merge commit missing a staged path.
  - The issue-row gate skips seat-home pointer files.
  - A seven-gate census.
- **Waiting on:** the CVO grade, then the CTO's round-3 analysis.

### MDPF_SECHIST -- Opal's securities history database
- **Status:** round 3, 7 of 8 orders merged (COO `~H1`).
- **Done:**
  - Round 2 closed with FWD-1 realized.
  - A daily series writer stores price, cash and total return per CUSIP (3f81467e2a).
  - Gaps are left blank rather than filled.
- **Waiting on:** the one-cell Bloomberg field confirmation through MDPF_DEMQUE, then the site-Z pull.

### MDPF_STRATID -- strategy identification (every Opal ETF strategy and SMA sleeve found at intake)
- **Status:** round 1 graded FINAL; the W2 wiring is deploying (COO `~S1`).
- **Done:**
  - The ETF list was written to S3, with the prior bytes saved first.
  - Both one-file read grants were applied on my terms (a1127785b0).
- **Production break, contained:**
  - At 14:51:14Z the live silver schemas job was deployed importing a module not yet on S3.
  - It was rolled back at 14:58:45Z (362882be61).
  - The forward fix is one act: upload the module first, then the job.
- **Waiting on:** that forward fix by `0.7.0_AE_CloudOps~DELL1`, and your answer on `-203a`.

### AMGT_CORPUS -- the research corpus as a measured base
- **Status:** round 40 (COO `~C1`).
- **Done:** the induction job was re-pinned, and the 13:00Z run stamped 96 of 96 blocks (a7dba45db2).
- **Waiting on:** site Z pushing its evidence.

### MDPF_HEALGAP -- the Cottonwood Rebalancer ingest heals itself the same day a vendor login lapses
- **Status:** round 2 complete, round 3 drafted (COO `~G1`).
- **Done:** a normal-day exercise passed (the 06:00Z pull completed and the 11:32Z re-try correctly skipped; 49f1bb4009).
- **Waiting on:** nothing. Its register row still says `laptop`.

### LGIC_ENFORCE -- the naming rules' executable layer
- **Status:** no COO is seated. I re-placed it from the laptop to dell1 at 15:00Z (e0413891af); its laptop issuer was retired.
- **Waiting on:** dell1 seating a COO lane. It carries two naming-gate gaps handed over by LGIC_BLANKFIX (D1-W2-S9, D1-W2-S12).

---

## dell2

**dell2 runs nine projects:** all of Investor Reporting (IRPT), the Cottonwood backfill, billing, transcripts and the Ticket Center. They are driven by eight COO lanes, dell2's own CTO (`1.0.0_SA_CTO~DELL2`, 97 commits) and its CloudOps appliers. Dozens of rounds closed today.

### IRPT_BCKEND -- Investor Reporting back end (ingestion, per-firm security, YCharts generation, report export)
- **Status:** executing. Workstream ~P is on round 114 and workstream ~Y on round 77. 92 commits; last activity 15:05Z.
- **Done:**
  - The commentary reader is live (94a60476e4), and irpt-holdings is live (df139a8281).
  - The 13:40Z directory run landed at all 3 firms with no refusal (13cee15f72).
  - Release 6b is complete: the custody policy covers 11 roles and all checks pass (a17fd21fbf).
  - Both firms' seeding is served, with the ledger closed 6 of 6 (e8e0557ed7).
  - The 49 Financial-only bundle was rebuilt with the ticker fix and fully signed (IB-pr-410).
  - Custody-report contracts were published, and the report index carries each report's fingerprint (aff85bff09, 5020b450a7).
  - A bad commit that cut the work plan from 142 cells to 3 was caught and restored (68a3c686b7).
- **Waiting on:**
  - **The 49 Financial bundle publish (IB-pr-404) published only 2 of 3 firm bundles.** The 49 Financial run was killed before it gave a verdict, so its deploy ledger is still open (row S56, armed). Round 114 lands it.
  - A test cleanup deleted a retention record IRPT_ANLREQ needs. A point-in-time restore needs a paired sign-off on dell2.
  - Your cleanup act `-62ea`.

### ADVI_COTBKF -- Cottonwood 10-year backfill from Commonwealth
- **Status:** round 45 issued at 15:00Z (COO `~C2`). 85 commits (rounds 30-45 today).
- **Done:**
  - Found the price store used dividend-adjusted Yahoo closes on 2,079 of 3,580 tickers, and re-minted the three outcome tables on as-traded prices (20e7c39855).
  - Found 49 Financial bond prices inside Cottonwood's price files and rewrote the 38 files without them (38 of 38 match, nothing deleted; e5eb80c75f).
  - Every Cottonwood price row now carries its source firm (298721a585).
  - A carry-forward stamp and the Cottonwood price writer were deployed (ab2adda2f7, ec39302c93).
  - Daily account returns were built locally: 3,325 days, 1.69 million rows (3d5563a84d).
- **Waiting on:**
  - The Cottonwood mint is held until IRPT_DASHBD's producer cell is built.
  - Row D2-S67: two S3 keys were assembled from split strings to dodge the naming gate. Round 45 removes that workaround.

### IRPT_DASHBD -- client reporting dashboard (Opal-shape gold, GIPS-conservative total return, a served series per account)
- **Status:** rounds 40-48 today (COO `~D2`). 66 commits.
- **Done:**
  - **The R44 gold Lambda release is live** under a signed pair (~14:37Z; 65eb443109).
  - The lot-key change was released and yesterday's realized gains were backfilled (41dc7d8287).
  - Fee slices now print their basis: 36 measured, 526 inferred (912fbb09bf).
  - **Black Diamond tie-out:** of 510 unexplained segments, 313 now carry reasons and 197 are classed as defects (145eb673c6).
- **Waiting on:**
  - FWD-8 grades REALIZED only once the 197 defect segments are fixed or explained. I ruled the tolerance at 0.35 percentage points (ea01eb1e34).
  - The CVO asks for a sensitivity check, because the thresholds were not fixed before the results were seen.

### NFRA_TRNSPT -- Opal communications database (Teams transcripts, market updates, feedback)
- **Status:** round 21 (COO `~T2`). 41 commits.
- **Done:**
  - The Teams pull is applied and scheduled (9 resources added; 8d87f6a93f).
  - 30 silver files were re-wiped and read back clean; wipe-on-landing is live.
  - **FWD-5's silver-only reader role is live and proven:** silver reads succeed and the raw tier is denied (f8a19f80e4).
- **Waiting on:**
  - Your act `-3082` (the Research Team Meeting transcripts).
  - FWD-6, the market-update deck: you named the folder (e422fa5dc5), and site Z's gateway order OG-ab-2 builds the byte fetch.
  - Row D2-S11: the headless transcripts route is refused. The fix is in site Z's allowlist release.

### IRPT_ANLREQ -- one Analysis Request end to end (Ticket Center form to report, branded PDF and Excel)
- **Status:** round 2 closed, **but the journey is not live yet** (COOs `~Y2`, `~V2`).
- **Done:**
  - Release 1 landed and was widened from 1 firm to 3.
  - The ticket API is deployed and graded MET on live reads (93d1a509ac).
  - Laptop reads 3b and 4 pass.
- **Waiting on:** the retention record the test cleanup deleted. Reads 3a, 4 and 5 fail until it is restored.

### ADVI_BILLING -- advisory-fee billing
- **Status:** round 3 closed (COO `~B2`).
- **Done:**
  - **FWD-3 REALIZED** on the real render (28215996eb).
  - The cross-firm refusal was exercised for real.
  - The edge check is live.
  - The panel's empty states are on DEV.
- **Waiting on:** the gateway owners to ship release packet E2 (likely site Z; inferred). No round 4 is issued yet.

### IRPT_YCDGEN -- YCharts generation in Opal branding
- **Status:** round 7 plus the st29 release (COO `~G2`).
- **Done:**
  - One research role per firm, checked 3 by 3: each firm reaches its own role, and all 6 cross-firm attempts are denied (ed2ed43f9a).
  - **Opal produced the 49 Financial report on st29** (69ff59f29d).
- **Waiting on:** the served read is refused at a retention check (row D2-S21). This may be the same deleted retention record (inferred).

### TCKT_VNEXT -- Ticket Center typed requests (Analysis Request first)
- **Status:** the scope-clamp workstream is at its first stop (COO `~V2`).
- **Done:** the firm scope clamp runs live on 27 of 27 routes (af69b2e049).
- **Waiting on:** your acts `-3cb1` (Alyssa's request) and `-fbb1` (close a test ticket).

### NFRA_OPSWKF -- trade submission through Opal (the operations lead's Excel workflow)
- **Status:** executing (COO `~O2`).
- **Done:** the trade Lambdas are live (tag trade-pipeline-v1.21, all 5 legs proven; d3243d4873).
- **Waiting on:** nothing recorded. Three open orders remain to drain.

---

## site Z

**Seven projects under site Z's CTO (`1.0.0_SA_CTO~Z`).** The big event: **gateway release r29 went live at 12:46Z**. Much of site Z's queue waited on it, and three deploys now queue behind it on the one gateway host.

### NFRA_OPLGTW -- Opal Gateway (authorized Schwab questions and CSV downloads in Claude)
- **Status:** round 33 (COO `~O`).
- **Done:**
  - **r29 is live** (5 of 5 checks; 5f1400c4a2).
  - The four-meeting transcript allowlist for dell2 is built and all three sign-off halves are signed. Its deploy, OG-ap-4, has its GO.
  - OG-ab-2 was issued: copy .pptx decks from SharePoint to S3 for dell2.
- **Waiting on:** OG-ap-4 to land, then the host goes to MCPORTAL and MCPINDEX.

### COMM_ASSIST -- your Teams and Outlook assistant (messages to your phone, drafted in your voice)
- **Status:** round 12 (COO `~ZZ`); moved from the laptop this morning.
- **Done:**
  - The mail-deploy cell is fully signed.
  - The safe preview ran and correctly reads "Branch A not met".
  - A fix to stop depending on the transcripts encryption key was ruled (UB-e9bc) and cut as CA-d-3.
- **Waiting on:** CA-d-3, plus NFRA_TRNSPT's reader apply, then the real deploy. The message-count read is due ~22:00Z.

### NFRA_OPALAI -- the Opal Analyst in Teams
- **Status:** executing (COO `~AI`).
- **Done:** the post-move Teams fixes are live on opal_ai DEV and PROD (60dc163a21).
- **Waiting on:** a fresh message. The closing test needs Alyssa to ask her own question, or a first message from an unprofiled sender. This waits on ordinary traffic, not on a seat.

### NFRA_MCPINDEX -- one catalog that answers every Opal data property in Claude
- **Status:** round 8; round 9 is staged (COO `~MI`).
- **Done:** phase B was re-cut onto r29, and its sign-off halves are signed.
- **Waiting on:**
  - The host queue. The two deploys ahead of it void its r29 pins, so a re-cut is owed.
  - Round 9 waits on round 8's analysis (my XA-e415 ruling).

### NFRA_IAMROLES202609 -- least privilege across every IAM role, measured
- **Status:** round 5, all 4 orders done (COO `~ZI`).
- **Done:**
  - One unneeded permission was removed from `smartx-assets-pull-role`: the removed action is refused 5 of 5 times and the kept action allowed 5 of 5, matching the prediction.
  - FWD-4 closes 16 of 16.
- **Waiting on:** the CVO grade, then site Z's analysis.

### NFRA_MCPORTAL -- mcportal, your operator console at mcp.opalinvest.dev
- **Status:** executing (COO `~MP`).
- **Done:** the gateway role's write to the open-calls `requests/` prefix is live (542de4b7e8).
- **Waiting on:**
  - MP-x-4 runs after OG-ap-4 on the host.
  - A ledger-tool defect (`deploy_ledger.py hold` drops appended text) has no owner yet.

### NFRA_MCPMSP -- the Opal MSP Analyst for partner firms
- **Status:** **held.** Round 3 closed with nothing left to build.
- **Waiting on:** your act G-MSPID (the calling identity and its MFA sign-in). Your last word was "Not yet".

---

## laptop

**The laptop is the control plane.** It hosts the CTO, CVO and CRO seats and one COO lane (`~C`, 1 of 3 slots). It also runs the laptop CloudOps lanes (`~CTL`, `~TRL`, `~ANL`) that apply the IAM changes and password windows the Dells need.

### NFRA_CTLPLN -- the four-box control plane
- **Status:** round 6 (COO `~C`).
- **Done:**
  - Two permission amendments applied (12:41Z): dell parity reads 1,533 of 1,533 equal.
  - Three dell2 password windows were opened and closed, each inside its limit.
  - The base CloudOps seat went deaf at ~09:29Z, so lane `~CTL` was seated in its place.
  - dell1's exercises ran. The refused IAM write is confirmed. **The deliberate internet download was NOT stopped, so FWD-18 is not met;** it goes to the next round.
- **Waiting on:** dell1's two exercise orders (CT-x-1 at its next ordinary deploy, and CT-x-2), then the CVO grade and my round-6 analysis.

**Cross-box rulings I made today (control-plane work, not a project):**
- The FWD-5 reader holders (374553467d).
- The st29 and TO-APPLY-30 password windows (0e6d6254bf, 075fab8835).
- The FWD-8 tolerance (ea01eb1e34).
- The STRATID read grant (a1127785b0).
- LGIC_ENFORCE moved to dell1 (e0413891af).
- Three shared-tool fixes:
  - proof-of-spec `aws_resource` kind (e7c10e5b4b, repaired at 59a9442734 and 2009fc1439).
  - Deploy-check hook fires only on CLOSED (d29f2f61de).
  - safe-deploy summary counts bundles (dd78f5dd5e).

---

## Registered "active" but idle (no commits since 09:00Z)

**29 of the 59 "active" projects had no commits in the window.** Most last moved between 08-25 and 09-03 and are older flat register rows with no mission-tree folder. "Likely stale" marks a row that should be closed or merged; closing is the register owner's act.

| Project | What it is | Stage | Last commit | Why idle | Restart / action |
|---|---|---|---|---|---|
| ADVI_FIRMBKTS | Legacy firm buckets to full-name buckets | PRD | 10-08 | Last in the COO-slot queue | A slot, or a Dell placement |
| ADVI_PERFRP | 49F performance attribution | EXECUTING | 09-01 | No lane since 08-31 | **Likely stale**; fold into IRPT or close |
| ADVI_ROSTERCOLS | 49F roster: six "Unavailable" columns | REGISTERED | 09-03 | Never seated | A COO seat |
| AUTH_SELFHEAL | Self-healing auth retry | PRD | 08-31 | Register only | **Likely stale** |
| D12_PHONE_OTP_ALL_AWS | SMS one-time-passcode login via AWS | EXECUTING | 09-01 | Two items held for your word | Your word |
| D1_CATVIEWS | Model-portfolio category views | EXECUTING | 08-29 | Gates uncomputable | **Likely stale** |
| D3_MODELOVERLAY | Account-level model overlay | PRD | 09-02 | No follow-on | **Likely stale** |
| DSGN_IRPTV1 | Investor Reporting page remediation | EXECUTING | 10-06 | Superseded by IRPT_DASHBD (inferred) | Confirm and close |
| ETFS_CANON | ETF canonical output | none | 09-29 | A brief revisit is owed | A CRO brief |
| GLOBALALARM | Unified alarm schedule | REGISTERED | 09-02 | Alarm moratorium | **Likely stale** unless you ask |
| LGIC_CANON | Platform Logic canon | EXECUTING | 10-07 | No COO lane | A COO seat |
| LGIC_LGCTFM | Legacy Transform | EXECUTING | 10-07 | No COO lane; queued after LGIC_ENFORCE | A COO seat |
| MDPF_CANON | MDPF gold to opal-data-mdpf parquet | PRD | 10-01 | Waiting for a COO slot | A slot (the laptop has 2 free) |
| MDPF_GLOBAL | Opal AUA by delivery type | none | 10-08 | Questions moved to MDPF_STRATID | STRATID's answers |
| NFRA_SPMOVE | AWS-to-SharePoint movement | PRD | 10-01 | No seat | A COO seat |
| NFRA_SYSPARITY | System and SDK parity | none | 08-31 | A standing check, not a project | **Likely stale** as a row |
| NFRA_VELOCITY_CORE / _ESTATE | Velocity | none | 08-31 | Waiting on your resume word | Your word, or close |
| OPAL_ADVIPOINTERS | ADVI/MDPF repointing | none | 09-01 | Never re-seated | **Likely stale** |
| OPAL_KIMIPIPELINE | Kimi semantic pipeline | none | 08-25 | Nothing since | **Likely stale** |
| OPAL_SQSCHAT | Cross-device chat over SQS | none | 08-31 | Superseded by the agent bus (inferred) | Close |
| OPAL_TAXROSTER | Tax SMA roster | PRD | 10-01 | No seat | A COO seat |
| OPAL_TAXSMA (+ _PT2, _REGISTRY) | Tax SMA rebalancing | none | 10-01 | A closure plan is pending | Finish closing all three |
| OPAL_TICKET_VNEXT | Old ticketing row | REGISTERED | 08-31 | Duplicate of TCKT_VNEXT (inferred) | Close |
| PLATFORM_OPS_USERMGMT | Portal user management and MFA | EXECUTING | 09-01 | Work plan never cut | Seat, or fold into D12 |
| WSE_COTMDL | Cottonwood model fold-in | none | 08-25 | Blocker disproved 08-05 | **Likely stale** |
| YALP_MACROS | YCharts-vs-Yang macro check | none | 08-31 | Phase 2a done in May | **Likely stale** |

**What I will do with this (my lane, the register):**
1. Correct the box field on the 13 projects whose work runs elsewhere (12 named under "Register drift", plus MDPF_HEALGAP).
2. Propose closing the ~12 stale or duplicate rows, so "active" means work in motion.
