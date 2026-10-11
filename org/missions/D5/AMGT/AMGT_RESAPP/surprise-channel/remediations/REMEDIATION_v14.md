# AMGT_RESAPP -- surprise channel, REMEDIATION v14 -- RECONCILIATION of every graduated item carried without a row

Author: 3.0.0_SA_CVO~Z. Round: v80 (round 67). Fabric: site-z. Recorded: 2026-10-05T01:1xZ. **Reader:** `1.0.0_SA_CTO~Z`.

**What it reconciles.** `.tools/surprise-row-gate.py` named 146 GRADUATED items with no remediation row, and `comp-surprise` read 153
ARMED (ADJUDICATION_v80 section L10). This file carries one row per item, plus round 67's Z-S346: **147 rows.**

**Result:** 125 REMEDIATED (36 of them ARMED items now DISARMED, each `at` the UTC commit time of the fixing commit) and 22 OPEN, of which
7 are still ARMED: Z-W42-S5, Z-W88-S1, Z-S230, Z-S242, Z-W117-S5, Z-W2-S3, Z-S238.

**Method.** The items were split into six batches and drafted by read-only subagents of this seat. Each verdict rests on one of:
- a fixing commit confirmed as an ancestor of HEAD;
- a path:line at HEAD;
- a task order's LAST `<status>`;
- a superseding row.

This seat validated all 147 rows against `remediation_row.schema.json` (0 errors). It re-examined two calls:
- `Z-S296`: its amendment's order was withdrawn. The closure has since shipped and serves, which this seat read live.
- `Z-S229`: see below.

**Named for owners, not acted on here:**
- **`Z-S230` stays ARMED.** A credential was committed. The code fix landed (@ab796d0520), but no scrub was ruled (@dbb9fedb27), and
  this seat found no evidence the credential was rotated. That is the owner's and the CTO's call.
- **Ledger contradiction on `leadpanel-price-producer-schedule`.** The `.md` record reads CLOSED (20260924T111024Z). The tracked
  `.open_deploys/leadpanel-price-producer-schedule.json` reads OPEN, with L3/L4 unproven and last RED 2026-10-04T22:27Z. The scheduled
  price fire does write daily (newest axis 2026-10-02, written 2026-10-04T11:05Z). Per NEVER-2, its author `0.0.3_BG_BBGTerminal`
  measures the artifact and closes it SUPERSEDED.

**Calls the drafters flagged and this seat accepted:**
- No-act-owed closures rest on a named ruling or completion (Z-W38-S1, Z-W39-S4, Z-S273, Z-S260, W146-S1).
- Disarm times use the code or deploy commit as each row states.
- Owners default to `2.0.0_SA_COO~Z` where the row named no serial.

**OPEN rows (22):** Z-S341, Z-W173-S3, Z-W37-S2, Z-W42-S5, Z-W88-S1, Z-S218, Z-S230, Z-S242, Z-S343, Z-W173-S4, Z-W212-S2, Z-W45-S1, Z-S283, Z-W117-S5, Z-W2-S3, Z-W45-S2, Z-S220, Z-S238, Z-S221, Z-S278, Z-W40-S1, Z-S228.

```json
[
  {
    "id": "AMGT_RESAPP-W130-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The naming-gate (LGIC_ENFORCE DEC-6, ENFORCE mode live) REFUSEs the AMGT-rl-1 fixtures file: its captured API-response DATA carries real production S3-key-shaped literal strings the gate's registry has no pattern for, so the byte-identical copy the cell requires at portal/src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json cannot be committed as written.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W130-S1",
      "portal 513bb3c5 (ancestor of the pinned gitlink ec65c5d6): the contract-check fixtures land under __harness__/tests/, the naming gate's exempt class",
      "portal ec65c5d6:src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json is tracked at the workspace HEAD gitlink",
      "adjudications/ADJUDICATION_v55.md:132 (6841a976e4): gate reads 1 seen, PASS 0 graded; same bytes at a non-exempt path read REFUSE 48 graded"
    ],
    "remedy": "Fixtures relocated under __harness__/tests/ (portal 513bb3c5), where the naming gate's fixture exemption applies; the file is tracked at HEAD.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W150-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-rn-5 AC1's issued <expect> pattern ('served carries N of N landed top-level keys; missing: none; _served provenance ... -> OK; exit=0') does not match the shape the named checker (round39/checks/rn-5.AC1.py) actually prints ('landed top-level keys: N; served carries N of them; missing: ...') -- a real invoke against the deployed function, otherwise satisfying AC1's substance (7 of 7 keys carried, provenance complete, rc=0), still fails proof-of-spec-check.py's literal expect-match gate.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W150-S1",
      "c89e9febdf (ancestor of HEAD): issuer amends rn-5 AC1 expect to quote checks/rn-5.AC1.py's real line shape",
      "task-orders/AMGT_RESAPP.TO-AMGT-rn-5.fwd-30-on-the-served-plane.md:49 expect now reads 'landed top-level keys: N; served carries N of them; missing: none'; last status complete"
    ],
    "remedy": "The issuer rewrote AC1's expect to the checker's printed shape at c89e9febdf; rn-5 is complete.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S194",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "2 of the 3 VALIDATION names serve NO management to a manager, under a label that is false for the stored object: scoped_amgt.read_management serves management_status ABSENT / absent_because ZERO_OFFICERS / officer_count 0 whenever roster_status != RESOLVED (scoped_amgt.py:2519-2533), and CSL_AU_Equity stores 14 officers and 6861_JP_Equity 1 officer (roster_status UNRESOLVED-SOURCE, officers from the Bloomberg fallback rk-47 wrote). The served page says the roster has zero officers when the object carries 14.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S194",
      "3a7afd3316 (ancestor of HEAD, AMGT-rk-77): read_management serves the Bloomberg fallback roster, labelled",
      "lib/research/api/scoped_amgt.py:3711-3727 at HEAD: ZERO_OFFICERS only when officers is empty; :3784-3795 a non-RESOLVED roster with officers names ROSTER_UNRESOLVED_NO_FALLBACK, never ZERO_OFFICERS",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-77.serve-fallback-roster.md last status complete; TO-AMGT-rk-78.render-fallback-roster-reason.md last status complete"
    ],
    "remedy": "rk-77 partitions management by officer count first and serves the fallback roster with roster_source; rk-78 renders it on the page.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T19:13Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S216",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "After AMGT-rk-94 the PRINT route renders for all 5 model-block names, but it runs 15-17 s WARM against the Lambda's 29 s timeout, and invocations have hit the full 29,000 ms and been cut off: a manager's print can time out and return nothing. The 29 s ceiling is effectively fixed by the HTTP API's integration limit, so the fix is render time, not the timeout.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S216",
      "88f8589245 (ancestor of HEAD, rk-97 apply): memory 512 -> 1769 on opal-amgt-scoped-api, timeout stays 29",
      "infra/aws/terraform/harvest/scoped-amgt-api.tf:376 at HEAD: memory_size = 1769",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-97.print-latency.md last status complete",
      "adjudications/ADJUDICATION_v26.md:52: 11 cold starts since the apply, 0 timeouts, max 10.3 s, read from the function's own logs"
    ],
    "remedy": "rk-97 raised the function to 1769 MB; the print route's cold starts read 0 timeouts on the function's own logs.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-22T10:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S223",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py has 1 FAILING test at HEAD 96cc4dae9d -- pre-existing, not caused by round 28.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S223",
      "54995eb25f (ancestor of HEAD, AMGT-rk-115): a FIXED content pin restores the stale discriminator (Z-S223)",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-115.research-tests-cleanup.md last status complete",
      "adjudications/ADJUDICATION_v33.md:45: the files read 11 passed together; Z-S222, Z-S223 and Z-S224 read REMEDIATED"
    ],
    "remedy": "rk-115 repaired the failing raw-pair latest-stamp test with a fixed content pin; the suite reads green.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S229",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The PRICE ranking axis is 12 days stale (newest 2026-09-10) while the chatter axis is current, so the Lead Panel's price lists would be stale the moment the page renders.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S229",
      "8d235eadb1 (ancestor of HEAD): adds the isolated price leg to the scheduled daily pull",
      "integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:352-353 at HEAD: :price_leg runs price_axis_pull.py",
      "DynamoDB opal-harvest-security-metrics scan 2026-10-04 (read-only, 2255 of 2255 items, no LastEvaluatedKey): 56 TRENDING_PRICE partitions, newest axis date 2026-10-02 (last trading day before Sunday 10-04), written 20261004T110521Z"
    ],
    "remedy": "The daily price leg rides the scheduled pull and the served price axis reads the last trading day (scheduled write 2026-10-04T11:05Z). Its ledger entry is contradictory (the .md reads CLOSED, the tracked .open_deploys json reads OPEN with L3/L4 unproven); that is named for its author, not closed here.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S241",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The incomplete-teardown CLASS census is CLEAN on site-z (0 untracked .tf across 77 terraform dirs / 477 tracked .tf) -- and running it shows the ruled verify-after can be CHEAPER and WIDER than 'an ls per teardown': `git status --porcelain -uall` is a git command that READS THE FILESYSTEM and would have caught this hazard.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S241",
      "row carries disposition GRADUATED and records a clean census (0 untracked .tf across 77 dirs / 477 tracked .tf) with a planted positive control"
    ],
    "remedy": "No act owed: the row records a controlled clean census and a cheaper verify-after; it asserts no live defect.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S251",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "rm-1 re-keyed the MEASUREMENT and left the CONCEALMENT intact: at least ELEVEN places in portal/ still assert the retired identity `--bg-band == #0A1733`, including Panel.tsx:8/:47 (the exact docstring that misled the round-37 grader) and index.css:88/:94 (the SAME FILE in which the token was re-pointed). R-65's ruling named the stale comments as part of the blast radius; the instrument was fixed and the comments were not, so the trap that cost round 37 is still armed for the next reader who does the right thing and reads the owning component to learn what a band is.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S251",
      "portal 02e04083 (ancestor of pinned gitlink ec65c5d6, AMGT-rn-3): retire the retired-identity prose; workspace drain 2906e31cc4 (ancestor of HEAD) moves the gitlink",
      "portal ec65c5d6: 0A1733 has 0 hits in src/index.css, src/ui/components/panels/Panel.tsx, scripts/ui-smoke.mjs, PrintExportAction.tsx (git grep rc=1); positive control bg-band 12 and 6 hits in index.css and Panel.tsx",
      "task-orders/AMGT_RESAPP.TO-AMGT-rn-3.the-retired-identity-prose-and-c13.md last status complete",
      "adjudications/ADJUDICATION_v55.md:131: the row's own query returns 10 hits across 1137 files, all allow-listed; none of the named sites remains"
    ],
    "remedy": "rn-3 removed the stale #0A1733 band assertions and the hardcoded scrim (portal 02e04083, drained at 2906e31cc4).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T18:54Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S258",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-Z-S253, -Z-S254 (ARMED) and -Z-S256. rm-7 deployed and all three legs proved: CodeSha256 moved, the pdf default is DELTA=0 on the content-stream comparand with a live negative control, and format=rich serves text/markdown while format=xml refuses 400. Each row's remedy was executed by a NAMED act and each is recorded separately below, because the three did not move together.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S258",
      "row is a disarm carrier for Z-S253, Z-S254 and Z-S256, each disarm recorded on its own evidence line",
      "adjudications/ADJUDICATION_v48.md:26: Z-S258 GRADUATED, terminal already as a carrier"
    ],
    "remedy": "No act owed: the row is a disarm carrier recording rm-7's executed remedies for three other rows.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S264",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ADJUDICATION CARRIER, batch 2 of the R-78 sweep, INHERITED: nineteen rows from rounds 1-9 (2026-09-11 to 09-13) whose disarm_owner is the predecessor lane 2.0.0_SA_COO~ZZZ -- a serial no longer seated on this project, so the rows have named an owner who could not act since round 13 (the stale-owner class /mstr-spawn 1d names). This project's issuer takes them as inherited, on its own read of each, and adjudicates the ones resolved in the world; each remedy is on its own evidence line. Nothing on any target row is edited.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264",
      "row is an adjudication carrier (R-78 sweep batch 2) for nineteen inherited rows; disposition GRADUATED; nothing on a target row edited"
    ],
    "remedy": "No act owed: the row is an adjudication carrier recording per-row remedies of inherited rows.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S273",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The CTO's three-valued Peers P/E ruling (@0d568cdf51) rests on row Z-S270, which says the Peers P/E reads BEST_PE_RATIO and that Deere, Eaton and Union Pacific can never fill. On the served Peers tab after ro-7's act C, P/E is the reciprocal of each member's earnings yield, and all 12 of 12 members carry a figure, those three included.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S273",
      "479eee52ff (ancestor of HEAD): the CTO vacates the three-valued Peers P/E ruling the row disputed",
      "f574a21ac1 (ancestor of HEAD): row Z-S275 folds Z-S270 and Z-S273 as the round-40 L10 ruled"
    ],
    "remedy": "No act owed: the ruling the row challenged was vacated at 479eee52ff and the row folded by Z-S275.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S281",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The rich export's Model Cases line CONTRADICTS ITSELF -- it reads 'Upside / Base / Downside cases: SERVED -- the payload carries no case block' while the served route carries a full base block -- because `_model_cases_markdown` reads only `cases`/`status`/`reason` and NEVER reads `base`, `upside` or `downside`, so a SERVED block with no `reason` key falls through to a DEFAULT absent-reason. Boeing's served base of -18.03 therefore never reaches the export at all.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S281",
      "164eec0d8c (ancestor of HEAD, AMGT-rr-2): the export's Model Cases block reads each case",
      "lib/research/print/render_pack.py:786 at HEAD: docstring names Z-S281 as the top-level-only read it replaces",
      "task-orders/AMGT_RESAPP.TO-AMGT-rr-2.the-model-cases-shown-and-exported.md last status complete",
      "adjudications/ADJUDICATION_v53.md:24 (56aca7662b): GRADUATED, rr-2 fixed exactly this, verified three ways"
    ],
    "remedy": "rr-2 wrote the SERVED branch so the export reads the per-case base/upside/downside objects.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S289",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CORRECTING MY OWN ROUND-44 CLAIM: the packet's 'served over 95 of 95, OK 95' rested on a harness OK predicate that never tested absDiff.missing; on the same capture 86 of 95 names drop one page absence (the posture line). Row Z-S268 was graduated on that claim.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S289",
      "0e5ba2303e (ancestor of HEAD, AMGT-tt-1): the export carries both page forms of an ABSENT posture line and the verdict counts a dropped one",
      "portal ec65c5d6:src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs:610 OK predicate requires absDiff.missing.length === 0",
      "task-orders TO-AMGT-tt-1 and TO-AMGT-tt-2 last status complete",
      "2b3f58e826 (ancestor of HEAD): round-45 close run served 95 of 95 OK, absences missing=0 on 95 of 95; ADJUDICATION_v55.md:129"
    ],
    "remedy": "tt-1 made the OK predicate test missing absences and tt-2 served the fix; the close run reads 0 missing on 95 of 95.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S296",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "vv-4 REFUSED before the upload on three limb hits. The real one: the dossier closure this act newly packages carries lib/research/corpus/extract.py, whose MODULE SCOPE imports fitz, openpyxl and lxml, none packaged -- and both halves admit that closure only on the condition it carries no fitz/pymupdf. The other two are a two-line helper and a closure hop the halves' file list does not spell out.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S296",
      "aeee38480a (ancestor of HEAD): COO AMENDMENT 2 rules the three closure hits, extract.py admitted as shipped-inert with a runtime no-fitz clause",
      "task-orders/AMGT_RESAPP.TO-AMGT-vv-4.the-redeploy.md last status withdrawn (rolled back on an unrelated grant line)",
      "adjudications/ADJUDICATION_v57.md:35 (556a5a37f8): GRADUATED, ruled in AMENDMENT 2 with the CTO's concurrence",
      "the closure has since shipped and serves: opal-amgt-scoped-api CodeSha256 2rFeF57l (AMGT_CORPUS al-5, 2026-10-04T22:42Z) answers 200 on the timeline, chatter, ledger and peers routes (3.0.0_SA_CVO~Z probe, 2026-10-05)"
    ],
    "remedy": "The issuer ruled the closure hits in AMENDMENT 2 with the CTO's concurrence; vv-4 then rolled back and was withdrawn.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-29T07:57Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S305",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "FWD-30's no-regression arm (round47/checks/vv-4.AC2.sh) read at round-48 close: EXPORT-COMPARE OK on 62 of 96 (NOT_OK 33, CAPTURE_FAILED 1), against 95 of 95 at round 45's close. Every NOT_OK is ABSENCES only (figures, cites and cases equal on all 95), and the differing lines sit on the posture/call, company-description and thesis-driver absences -- sections the page changed today in DSGN_AMGTV1 rounds 3-4, and none that round 47/48 changed on the export side.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S305",
      "33ed750433 (ancestor of HEAD): ADJUDICATION_v58 section 2 controlled run at the round-45 page reads absences and figures equal on 95 of 95; the 33 NOT_OK are the page's rewording",
      "task-orders/AMGT_RESAPP.TO-AMGT-xx-1.fwd30-grader-keys-on-data-attributes.md last status complete"
    ],
    "remedy": "Attribution settled by the controlled run (v58): the deploy did not regress; the one-writer question is carried by Z-S297.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S325",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AC1's served limb cannot pass for ANY subject: the deployed opal-amgt-scoped-api has no /posture route at all. GET /api/scoped/amgt/security/<K>/posture returns 404 {'refused': true, 'reason': 'no /api/scoped/amgt route for GET ...'} on 3 of 3 keys this act overwrote AND 3 of 3 keys it never touched, while /thesis on the SAME function returns 200. So ae-1's 24 BAD lines are ONE cause, and that cause is not the act.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S325",
      "3bab99e4ae (ancestor of HEAD): carrier row Z-S326 disarms Z-S325; AMENDMENT 2 re-points AC1's served limb to the overlay's posture carrier",
      "task-orders/AMGT_RESAPP.TO-AMGT-ae-1.posture-batch-over-the-held-names.md last status complete",
      "adjudications/ADJUDICATION_v67.md:46 (2d8bf2518a): disarm verified, live /posture 404, overlay serves posture 200"
    ],
    "remedy": "AC1's served limb was re-pointed from the non-route to the overlay's posture field (Z-S326); ae-1 closed exit=0.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-01T06:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S341",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seating check (.tools/to-decomp-ref-lint.py, gate2) counts a WITHDRAWN task order as OPEN: TERMINAL_STATUS lacks WITHDRAWN, and an unknown status is open by design. At the round-65 issuance it announced that 0.7.0_AE_CloudOps~A holds 2 open AMGT_HARVST orders; both read <status>withdrawn</status> as their only tag.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S341",
      "7fbc36a5eb (ancestor of HEAD): the row filed",
      ".tools/to-decomp-ref-lint.py:80-81 at HEAD: TERMINAL_STATUS is still COMPLETE, CLOSED, SUPERSEDED, CANCELLED, DONE, CLOSED-SUPERSEDED; WITHDRAWN absent"
    ],
    "remedy": "Still live: the lint owner (1.0.0_SA_CTO) has not ruled WITHDRAWN terminal or added it to TERMINAL_STATUS.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-r-1's bound reads the FYE month from 'Bloomberg's fiscal-period fields the CRO mapped' -- but no such field is mapped; FISCAL_YEAR_END is BAD_FLD/INVALID_FIELD and no alternative was tested. The fix instead reads the true period end from WHICH DATE a fundamentals-bearing row itself carries (already on the record, no lookup field needed).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W1-S5",
      "integrations/bloomberg/research/fye_join.py:109 at HEAD: period_end = _parse(date) read off each fundamentals-bearing row, no FISCAL_YEAR_END field"
    ],
    "remedy": "No act owed: the bound is met through the row date carrier; the row corrects the spec's named field.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W159-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Worker's own read of row Z-W159-S1 after AMENDMENT 1 (issuer): the two harness limits named there are fixed IN THE INSTRUMENT (pageAbsences' {1,300} cap removed; the Model-sheet <td> parser now spans a nested CheckFaceBadge span), never by bending the export to them (_page_absence_cap removed). One further, previously-masked class closed on the same pass: CRNCY reaches the page ONLY as the price Stat tile's own prefix, so it is withheld from the header table whenever PX_LAST carries no figure. rq-1.AC1.sh now reads 'local rebuild over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0', exit=0. Filed UNDER_INVESTIGATION per A-1/LGIC_ENFORCE-C-S24 -- adjudicating S1 and any GRADUATED transfer are the CVO's at L9, not this worker's to declare.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W159-S2",
      "86e0683292 (ancestor of HEAD): AMGT-rq-1 amendment 1, 89 of 89 OK, the instrument fixed in the instrument",
      "task-orders/AMGT_RESAPP.TO-AMGT-rq-1.the-export-says-absent-the-way-the-page-does.md last status complete",
      "adjudications/ADJUDICATION_v52.md:24 (55d659db8c): GRADUATED as the carrier"
    ],
    "remedy": "No act owed: the row reports the worker's own instrument fix, landed at 86e0683292 and adjudicated in v52.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W173-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A SERVED case's VALUE and currency ride no data attribute, so CASES keys a served case on (name, SERVED, formula) and an absent one on (name, ABSENT, served reason).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W173-S3",
      "portal ec65c5d6 (pinned gitlink): no data-model-case-value or data-model-case-currency attribute anywhere under src; ModelTab.tsx:261 mentions data-model-case-formula only in a comment"
    ],
    "remedy": "Still open: the value and currency attributes asked of DSGN_AMGTV1 were never added; whether the case line still exists needs a re-read.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-W197-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-af-1 AC1 cannot reach exit=0 in the sparse worktree: 3 tests in test_print_format_rich.py error on a missing portal fixture (portal/ is a gitlink the cone does not populate); all other tests pass.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W197-S1",
      "e03b0a0b1c (ancestor of HEAD): row Z-S327 resolves W197-S1/W198-S1; AC1 graded on the full tree, 342 passed, exit=0",
      "task-orders/AMGT_RESAPP.TO-AMGT-af-1.the-monthly-chatter-route.md last status complete",
      "adjudications/ADJUDICATION_v68.md:47: GRADUATED, resolved by Z-S327 (the cone)"
    ],
    "remedy": "The issuer graded AC1 on a full tree with portal populated (Z-S327); af-1 is complete.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W212-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The one display-name rule strips share-class codes but does not re-case: a name served from the model-block fallback stays all-caps (pinned by test_model_block_names 'HERMES INTERNATIONAL'), so 'not all-caps' holds only where the classifications table or crosswalk holds a cased name.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W212-S1",
      "d72eed67f7 (ancestor of HEAD, AMGT-ao-1): every served display name in title case, at the producer seam",
      "lib/research/api/tests/test_model_block_names.py:44 at HEAD asserts display_name == 'Hermes International' while name keeps 'HERMES INTERNATIONAL'",
      "task-orders TO-AMGT-ao-1.display-name-title-case.md and TO-AMGT-ao-2.the-code-redeploy.md last status complete",
      "26bea252e9 (ancestor of HEAD): ao-2 closed, c17 YES, 0 of 94 / 0 of 95 all-caps on the deployed function"
    ],
    "remedy": "ao-1 re-cases every served display name at the producer and ao-2 deployed it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W37-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AC6's mandated census (AMGT-rk-33, C-PRODUCTION-HOME): after this cell's fixes, 50 lines across 25 production .py files still name a worker's deliverables folder ('0.9.0_WK_AMGT_RESAPP~<n>') by literal or path segment; the three PRD-named instances (model_block_pull.py's field-map/pull-log, build_universe.py's SEC cache, peers/universe.py's candidate-universe cache) are ABSENT from this list -- this row is the CLASS'S RESIDUE, not edited by this order.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W37-S2",
      "git grep -c -F '0.9.0_WK_AMGT_RESAPP~' at HEAD ff24d30809 over lib/ integrations/ infra/ *.py excluding tests: 49 lines across 25 files",
      "adjudications/ADJUDICATION_v14.md:288 (C-S329): remedy named, holder 1.0.0_SA_CTO~Z"
    ],
    "remedy": "Still live: production files still name a worker deliverables folder; no cell moved them beside their producers.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W42-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "After every code fix in rows S3/S4, the ONE live sample this order's remaining budget could afford still measures below two of AC3/AC4's own literal numeric bars: 'blocks per citation min/median/max' reads 1/1/2, not the named 1/1/1, and VERBATIM-CHARS reads 57 of 67 (85.1%), below the named >= 0.90 -- both traced to genuine content properties of THIS filing, not a further code defect.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W42-S5",
      "adjudications/ADJUDICATION_v14.md:431 (C-S335): class anchor; the CTO ruled the remedy a process habit, not a gate",
      "adjudications/ADJUDICATION_v26.md:76: further criterion-bar defects dismissed onto W42-S5 in round 24"
    ],
    "remedy": "Open: the remedy is a cutting habit with no mechanism, and later rounds still dismiss new instances onto this row.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_LEDGER.json@4c3f3fcb2e: its object is a criterion or instruction in a terminal order (a filings order, status complete: below-bar live sample traced to the filing's own content); no open order carries it (the task-orders folder holds only ll-1..ll-4 and two cancelled/staged orders non-terminal) and the lesson is a cut-time"
      }
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-09T20:19:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W88-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The SERP primitive's own record shape carries no per-page tag, so `harvest_serp`'s per-row `page_bronze_key` (order item 5e) cannot be derived exactly for a multi-page fetch; this cell attributes every row to the LAST page's bronze key.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W88-S1",
      "lib/research/harvest/bright_data_serp.py:128-132 at HEAD: every row still takes the last page's bronze key; no refusal of max_pages > 1",
      "harvest_serp has no non-test caller at HEAD (git grep lists only lib/research/harvest/tests/test_bright_data_serp.py)",
      "adjudications/ADJUDICATION_v24.md:106 (C-S372): remedy owed by the wiring cell, max_pages=1 or refuse"
    ],
    "remedy": "Open: no wiring cell exists and the writer still accepts max_pages > 1 silently; dormant, not disarmed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-09T20:19:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W137-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT-rl-8's LeadPanel.tsx now imports PanelFooter (from '@/ui/components/panels') and Segmented (from '@/ui/components/Controls'); tabs.harness.cjs (another cell's, __harness__/tabs.harness.cjs, read-only under this cell's <paths>) sources the real LeadPanel.tsx through its own narrower stub map and has no case for either specifier, so it now throws MODULE_NOT_FOUND before any of its own checks run.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W137-S1",
      "portal 1267a67e (2026-09-24T09:32Z, ancestor of HEAD's portal gitlink ec65c5d6): tabs.harness.cjs stubs extended -- PanelFooter (panels), Segmented (Controls)",
      "ca52fa60c1 (ancestor of HEAD): rl-8 closed complete, 'W137-S1 resolved by the harness stub extension (portal 1267a67e)'",
      "993b8234b9 (ancestor of HEAD): row Z-S266 adjudicates W137-S1 as fixed",
      "portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:85 PanelFooter stub and :117 '@/ui/components/Controls' case at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rl-8.lead-panel-controls-and-footer.md last <status> complete"
    ],
    "remedy": "Remediated: the issuer extended tabs.harness.cjs's stub map with PanelFooter and the Controls specifier at the rl-8 drain, so the harness loads the merged LeadPanel again.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T09:32Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W152-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-ro-1 item 1's 'the page's description ABSENT line carried verbatim when the page carries it' cannot be fully closed inside this cell's <paths>: the header's OWN description object (overlay.description, HeaderBrief.tsx's 'Description: ...' line, computed by scoped_amgt.py's description resolver) is a SEPARATE structure from thesis_bundle.drafted_sections[company_description] that build_rich_text already reads, and the ONE caller that could pass it (_print_pack in lib/research/api/scoped_amgt.py) is not in this cell's <paths>. build_rich_text now accepts an OPTIONAL, additive `description` param that renders it verbatim when supplied, but nothing wires it in yet -- with only the existing thesis_bundle-derived path in play, the fixture used by AC1/AC2/AC4 never exercises an ABSENT description (BA_US_Equity's overlay.description.status is SERVED, and its text is byte-identical to thesis.drafted_sections[company_description].sentences[0].text), so AC1/AC2/AC4 pass either way and the gap is not mechanically visible on this fixture.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W152-S1",
      "f3de463222 (ancestor of HEAD): drain-join wires scoped_amgt._print_pack description= and build_rich_text adds the header's Description line (row Z-S271)",
      "lib/research/api/scoped_amgt.py:5919 description=read_description(resolved_key, identity=identity, model_block=block) at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v50.md:22 GRADUATED, wired at f3de463222",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ro-1.the-export-adds-nothing.md last <status> complete"
    ],
    "remedy": "Remediated: _print_pack now passes description=read_description(...) to build_rich_text, which writes the header's description line beside the drafted section.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S197",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Now MANAGER-VISIBLE after AMGT-rk-77: Keyence's served roster_reason reads 'the persisted None filing doc-1defdb68a7ffd3b7 carries an EMPTY officer section (no item label): the item was not cut from the primary document' -- roster.py:944-947 formats source_object.get('form') with %s, and a non-EDGAR doc- source object carries form None, so the literal 'None' and an internal id reach the page. Before rk-77 this text sat behind a withheld block; rk-78 renders roster_reason verbatim beside the fallback.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S197",
      "a71d2ff8b2 (ancestor of HEAD): AMGT-rk-79 jp-president-and-readable-roster-reason lands",
      "5912b7d107 (ancestor of HEAD): row Z-S204 disarm record -- 6861's and CSL's stored roster_reason read as sentences with no 'None'",
      "lib/research/management/roster.py:294-307 _filing_label returns '{form} filing', a family label or 'filing' -- never a literal None -- at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-79.jp-president-and-readable-roster-reason.md last <status> complete"
    ],
    "remedy": "Remediated: rk-79 replaced the %s format of a None form with a filing-label rule that never emits a literal None, and the stored roster reasons were re-read clean.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S218",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The print route runs a pypdf text extraction on EVERY print but returns only the PDF -- the extracted text is discarded -- costing roughly 10-15% of the print's time (0.22-0.40 s locally). Dead work on the served path.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S218",
      "lib/research/print/render_pack.py:342-346 build_pack runs pypdf.PdfReader(...).extract_text() and writes txt_path on every call at HEAD",
      "lib/research/api/scoped_amgt.py:5933 _print_pack takes 'pdf_path, _ = build_pack(...)' and returns the PDF only at HEAD",
      "git log --all --grep=Z-S218 returns 0 commits"
    ],
    "remedy": "Still live: build_pack extracts the PDF text with pypdf on every print and _print_pack discards it; the removal (after a caller census) has not been cut.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S224",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "integrations/bloomberg/research/tests cannot be collected as a DIRECTORY: two test files import render_pack.load_model_block, which no longer exists, so pytest errors at collection.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S224",
      "54995eb25f (ancestor of HEAD): rk-115 test-rot cleanup -- a test-local helper reaches the current served overlay consumer (Z-S224)",
      "integrations/bloomberg/research/tests/test_consumer_wiring.py:44 and test_unresolved_overlay_renders_marked.py:69 define the test-local load_model_block at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v33.md:45 Z-S222, Z-S223 and Z-S224 read REMEDIATED",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-115.research-tests-cleanup.md last <status> complete"
    ],
    "remedy": "Remediated: rk-115 gave both test files a test-local load_model_block helper, so the bloomberg research tests directory collects again.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S230",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W116-S2's containment MEASURED, and it moves the class: the Bloomberg terminal USERNAME is not merely printable, it is ALREADY COMMITTED -- present in 4 TRACKED artifacts in credential context, the oldest 2026-08-14, i.e. an INCIDENT and not only an EXPOSURE. Remedied in code the same turn; the ROTATION decision is Andrew's and is carded, not assumed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S230",
      "ab796d0520 (ancestor of HEAD): fingerprint hashes BOTH limbs -- the code (exposure) limb only",
      "dbb9fedb27 (ancestor of HEAD): CTO ruling -- no history scrub; rotate later, not this session; row STAYS ARMED",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v35.md:163,170 code limb closed, four tracked artifacts remain, Z-S230 stays ARMED until both limbs close",
      "no commit found evidencing a Bloomberg terminal credential rotation (git log --all -i --grep=rotat since 2026-09-22)"
    ],
    "remedy": "Code limb closed at ab796d0520; the four tracked artifacts stay (no scrub, ruled at dbb9fedb27) and the credential rotation is deferred and not evidenced, so the row stays ARMED.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_054xZ_ALL_RECS_APPROVED_CTOZ_THREE_CARRIED_CARDS.md@08618af88b ruling 3: the password is not rotated; only the username is in the 4 tracked files"
      }
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-10-07T05:48:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S242",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "CORRECTS the R-12 amendment's one excluded false hit: etf-classifications.tf is NOT '3.0.0_SA_CVO~Z's live work' -- it is BYTE-IDENTICAL to HEAD in all 15 worktrees that hold it, and `git status` calls it MODIFIED in one and CLEAN in fourteen on IDENTICAL CONTENT, because the verdict comes from git's stat cache and not from the file.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S242",
      "git show HEAD:infra/aws/terraform/yang-pipeline/etf-classifications.tf = 2815 bytes with 82 CR bytes; git check-attr reads eol: lf, text: set",
      "git log -- infra/aws/terraform/yang-pipeline/etf-classifications.tf lists only 39810307ce, so no normalisation commit exists",
      "7c4d12648f (ancestor of HEAD): ruling R-12 scoped accepts the mechanism and widens the class to 46 files"
    ],
    "remedy": "Still live: the committed blob of etf-classifications.tf still carries CRLF against its eol=lf attribute; the LF re-commit has not landed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-10-09T20:19:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S252",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-Z-S248 (the PY_AWS assignment sat inside the SEND leg, so the pull-failed/DAPI-up path invoked an EMPTY interpreter on both landing legs). The named disarm owner -- this seat, which authored the 2026-09-04 leg-isolation fix the defect sat inside -- hoisted the single assignment above the RC branch under a NEVER-2 ledger entry opened BEFORE the edit. The one assignment now sits at :143, above the `if \"%DAPI_OK%\"==\"1\" goto :etf_leg` branch at :156, so every path into :etf_leg carries it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S252",
      "2e38c030f4 (ancestor of HEAD): PY_AWS assignment hoisted above the RC branch, ledger CLOSED",
      "integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:143 set PY_AWS precedes the :156 DAPI_OK goto :etf_leg branch at HEAD"
    ],
    "remedy": "No act owed: the row is the disarm carrier for Z-S248, and the hoist it records is at HEAD.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S259",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-Z-W5-S2 and AMGT_RESAPP-Z-S44, the two ARMED rows naming 3.0.0_SA_CVO~Z as disarm_owner: BOTH were resolved on 2026-09-11 and 2026-09-13 and have read ARMED ever since. And the census that found them understates resolution by an order of magnitude -- R-78's heuristic reads only LATER ROWS IN THE SAME FILE, while disposition is recorded in the sibling adjudications/ and remediations/ artifacts BY DESIGN: joining across them takes 180 ARMED from 103 uncited to 10.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S259",
      "e04ae3fe6c (ancestor of HEAD): files Z-S259 as the disarm carrier for Z-W5-S2 and Z-S44",
      "17e4d99e0e (ancestor of HEAD): row Z-S260 self-corrects the sibling-artifact join as nearly vacuous; the two disarms stand"
    ],
    "remedy": "No act owed: the row is a disarm carrier recording that Z-W5-S2 and Z-S44 were already resolved; its census claim was qualified by the author's own row Z-S260.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S265",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The Peers tab's 'P/E (trailing)' and 'P/E (NTM)' columns render values that are WRONG BY A FACTOR OF 100 -- 12 of 12 members implausible as a P/E as shown, 0 of 12 implausible at x100 -- and the estate's own producer map states the relation as 'RECIPROCAL: P/E = 1 / ey' while that reciprocal has no locatable implementation in either the portal or the peers library.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S265",
      "4258d3dc8f (2026-09-24T19:23Z, ancestor of HEAD): drain of AMGT-rn-2 -- P/E units, P/E in [0.5,200] on 24 of 24",
      "lib/research/peers/csc.py:105 and :229-230 carry transform 'reciprocal' and units at HEAD",
      "bf49596fec: ADJUDICATION_v49 verifies Z-S265 fixed at exactly 100x",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v54.md:27 GRADUATED -- remedied round 39 rn-2",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rn-2.the-pe-units.md last <status> complete"
    ],
    "remedy": "Remediated: rn-2 made the producer state transform and units and the consumer apply them, putting P/E in band on 24 of 24.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T19:23Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S275",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ADJUDICATION CARRIER for Z-S270 and Z-S273, whose disposition the round-40 L10 @fa03858417 resolved differently from ADJUDICATION_v50 -- and a MEASURED correction to that L10's ordering claim: the vacatur landed 4.6 minutes AFTER the slug, not twenty minutes before it. The substantive criticism stands and is accepted in full; only the sequence is wrong.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S275",
      "f574a21ac1 (ancestor of HEAD): files Z-S275 folding Z-S270 and Z-S273 as the round-40 L10 ruled"
    ],
    "remedy": "No act owed: the row is an adjudication carrier that applies the round-40 L10 dispositions and corrects a sequence claim.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S282",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Disarm-owner read of AMGT_RESAPP-Z-S279: the served base case now REFUSES by name on 6 of the 7 implausible names and serves a plausible base on the seventh -- AMGT_CORPUS round 5 re-derived the 89 blocks under CRPS-g-1's guarded rule (ledger 20260925T1952Z, CLOSED 20:06Z), and the deployed function serves the blocks as written.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S282",
      "eaf143941f (ancestor of HEAD): files Z-S282 -- the guarded re-derive refuses 6 of the 7 bad base cases by name",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v53.md:25 GRADUATED as the disarm-owner read"
    ],
    "remedy": "No act owed: the row is the disarm-owner read of Z-S279, recording that AMGT_CORPUS round 5 already disarmed it on the served plane.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S290",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM ACT for AMGT_RESAPP-Z-W163-S1 (disarm_owner this seat): no open round-45 order touches the portal, and the issuer's order template no longer tells a worker to move the portal gitlink; the issuer moves it only after the portal commit is PUBLISHED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S290",
      "2128056916 (ancestor of HEAD): round-46 issuance of uu-2, uu-3, uu-4",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-uu-2.the-harness-loads-the-timeline-mount.md:44 and AMGT_RESAPP.TO-AMGT-uu-3.the-base-case-on-the-adjusted-basis.md:56 read 'Do not commit the portal gitlink' at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v56.md:102 Z-W163-S1 GRADUATED, Z-S290 graduates with it"
    ],
    "remedy": "Remediated: the round-46 order template carries 'Do not commit the portal gitlink' on every portal-touching order.",
    "owner": "2.0.0_SA_COO",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S297",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "vv-4 AC2 reads 84 of 95 AFTER the apply, but a controlled experiment holding the DEPLOYED CODE IDENTICAL and moving only the portal shows the cause is page-side: at f1a90a9b the page yields cit_page=0 on 11 names where 8fa7abde yields cit_page=N, and cit_rich is byte-identical in both arms. The halves' rollback trigger does not fire on this act, and there is currently NO portal vintage at which AC2 can pass.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S297",
      "59f82c8e17 (2026-09-29T10:54Z, ancestor of HEAD): DSGN AV-r-3 parity harness keys on data; closes AMGT_RESAPP Z-S297",
      "1dfd5c0970 (ancestor of HEAD): round-48 analysis names FWD-30's one grader, sweep.py keyed on page data attributes",
      "bda9ce9e80 (ancestor of HEAD): ADJUDICATION_v59 -- xx-1 AC3 re-run YES, Z-S297 graduates",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-xx-1.fwd30-grader-keys-on-data-attributes.md last <status> complete; AMGT-vv-4 last <status> withdrawn"
    ],
    "remedy": "Remediated: FWD-30 has one grader keyed on the page's data attributes, so a page wording change no longer breaks export parity.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-29T10:54Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S311",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-zz-8 AC2 CANNOT PASS BY THE SPECIFIED ACT: the served /thesis `thesis_driver` rides on the D-1 DRAFTING_SERVED document (scoped_amgt.py:1876), NOT on filings/v1/<key>/<accession>.analysis.json. The ASML rewrite landed correctly (3 of 3 points now spanned) and the served chart is still ABSENT, because rewriting the filings object does not regenerate the document the chart's driver is read from. zz-6's AC1 could not see this: it handed thesis_driver_chart the re-verified driver IN PROCESS and never exercised the join.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S311",
      "274240b782 (ancestor of HEAD): zz-8 closed complete on the CTO's AC2-only rollback waiver",
      "108fb01895 (ancestor of HEAD): ADJUDICATION_v62 -- /thesis for ASML serves thesis_driver_chart SERVED, source filing",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v62.md:13-15 and :54 Z-S312/Z-S311 GRADUATED",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-zz-8.the-one-build.md last <status> complete"
    ],
    "remedy": "Remediated: ASML's thesis_driver_chart is SERVED from the filing on the deployed build, so the round-51 carried unmet is met.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S326",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM ACT for AMGT_RESAPP-Z-S325 (disarm_owner this seat): no scoped-API route is missing -- posture is served as the `posture` field of /security/{key}/overlay; the defect was the issuer's check, now amended (AMENDMENT 2) and re-run against the deployed function: exit=0, YES. Also answers Z-S324 for the L8 read.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S326",
      "cff509cdd2 (ancestor of HEAD): ae-1 AC1 PASS under the issuer's amendment, NEVER-2 entry CLOSED",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v67.md:46-47 Z-S325 disarmed by Z-S326, verified (/posture 404, overlay posture 200)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ae-1.posture-batch-over-the-held-names.md last <status> complete"
    ],
    "remedy": "No act owed: the row is the disarm act for Z-S325 (the issuer's amended check), verified at L8.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S343",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Collecting lib/research/harvest/test_am1_marker_once.py or test_al2_content_key.py in the same pytest run as lib/research/management/tests fails 10 test_ceo_search.py tests (TestClassifySerpAttempt, TestSerpBrightdataRecords); each passes alone, and management alone is 142 passed. The interaction predates fc5a0bf42d: it reproduces with the 9a8cbd2c97 versions of finbert_sentiment.py, publication_gold.py and test_am1_marker_once.py.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S343",
      "bf072c57a2 (2026-10-03T19:41Z): files rows Z-S342/Z-S343",
      "git log -- lib/research/harvest/test_am1_marker_once.py test_al2_content_key.py management/tests/test_ceo_search.py shows nothing after fc5a0bf42d (2026-10-03T18:38Z), which predates the row",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v78.md:50 GRADUATED as pre-existing and an enrichment item"
    ],
    "remedy": "Still live: the collection interaction was graduated as a pre-existing enrichment item and no commit has fixed it since it was filed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W116-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "integrations/bloomberg/auth/bbg_credentials.py --check prints the Bloomberg terminal USERNAME in cleartext (user='<value>') inside its own 'CREDENTIAL: OK' fingerprint line, contradicting its own module docstring's promise that --check prints 'a FINGERPRINT (lengths + a sha256 head), never the value ... without ever displaying it.'",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W116-S2",
      "ab796d0520 (2026-09-22T20:27Z, ancestor of HEAD): fix(bbg_credentials.fingerprint) hashes BOTH limbs, surfaced by row Z-W116-S2",
      "integrations/bloomberg/auth/bbg_credentials.py:84-102 fingerprint returns user_len and user_sha256 at HEAD",
      "the already-committed incident limb is carried separately by row Z-S230"
    ],
    "remedy": "Remediated: fingerprint() now prints the username as length plus a sha256 head, the same treatment as the password.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-22T20:27Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W163-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT-tt-1's TO instructs 'the outer commit, including the portal gitlink', but the gitlink-publication-check hook (ADOPTED TODAY 2026-09-26 by 3.0.0_SA_CVO~Z, .tools/git-hooks/gitlink-publication-check.sh) BLOCKS an outer commit naming an unpublished portal commit, and the worker standing rule is 'never push'. I could not do both.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W163-S1",
      "2128056916 (2026-09-28T22:00Z, ancestor of HEAD): round-46 issuance carries the corrected template",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-uu-2.the-harness-loads-the-timeline-mount.md:44 'Do not commit the portal gitlink' at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v56.md:26 GRADUATED -- the round-46 template is changed"
    ],
    "remedy": "Remediated: the issuer's order template no longer names the gitlink as the worker's act, and the issuer moves it only after the portal commit is published.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-28T22:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W173-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The thesis-driver chart's absence has no shared key: the page's data-driver-chart-reason is the served reason, the export's 'The chart: ABSENT -- the thesis driver is \"<series>\"' names the series; and the export states it on an UNDRAFTED thesis (AMD) whose page renders no chart element. Not graded.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W173-S4",
      "portal ae1be3c8 (ancestor of HEAD's portal gitlink): AV-u-5 adds data-driver-chart-series beside data-driver-chart-reason (ThesisDriverChart.tsx:75-78)",
      "lib/research/print/render_pack.py:857-863 _thesis_driver_chart_markdown emits 'The chart: ABSENT' whenever the chart is not SERVED, with no drafted-thesis check, at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round49.md:30 routes the no-attribute facts to DSGN; the undrafted-thesis limb is not ruled",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v60.md:67 graduates Z-W173-S1..S4 on the value plants only"
    ],
    "remedy": "Partly addressed: AV-u-5 added data-driver-chart-series, but the export still prints the chart-ABSENT line for an undrafted thesis whose page renders no chart, and no ruling settles that limb.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W198-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "AC1 cannot exit 0 in a sparse worker worktree: test_print_format_rich.py needs portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json, and portal is a gitlink (160000) the worktree does not check out -- 3 errors, identical before and after af-2's edit.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W198-S1",
      "e03b0a0b1c (ancestor of HEAD): af-1/af-2/af-3 closed, AC1 graded on the full tree (342 passed, exit 0) per Z-S327",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v68.md:47 Z-W197-S1/Z-W198-S1 GRADUATED, resolved by Z-S327",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-af-2.served-t1-fallback-breakout-and-percent.md last <status> complete"
    ],
    "remedy": "Remediated: the sparse-cone fix (row Z-S327) let af-1 and af-2 AC1 grade on the full tree, 342 passed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W212-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Gold article_security_mention holds no url column, so the overlay feed items now serve url null; the feed moved from P-1 pool bodies (which carried a url) to the day view's gold source.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W212-S2",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round64.md:29 'Not cut this round' -- adding the url is a HARVST gold rebuild",
      "504827836c (ancestor of HEAD): round-64 analysis commit",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v77.md:45 GRADUATED as enrichment, a url source is a round-65 item; none of ROUND_ANALYSIS.round65-67 mentions url"
    ],
    "remedy": "Still live: the overlay feed serves url null because gold article_security_mention has no url column; the round-64 analysis did not cut it, since it needs a HARVST gold rebuild.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-W38-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The face's section 3 names the AMGT-rk-34 rollback as 're-derive with the pre-act map bytes, NO S3 delete', but the actual signed never-widen pair (both halves) names the rollback as delete_object of the new stamp -- the two documents disagree about the one thing section 3 says 'the pair' states.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W38-S1",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~38/AMGT_RESAPP.TO-AMGT-rk-34.unit-map-every-name.proof_of_spec.json:158 rollback not needed, 33 of 33 derived",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-34.unit-map-every-name.md last <status> complete",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v14.md:484 the class is ratified as CTO round-14 doctrine note 2"
    ],
    "remedy": "No act owed: rk-34 completed with every derive successful and no rollback, so the face-versus-pair rollback disagreement governs no pending act.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W45-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "4 of 12 served management objects (BABA, BA, COST, HD -- all dated 2026-09-15, the pilot-name batch) carry ceo_public_profile.status=ABSENT, query SET, and absence_class NULL even though their own basis text describes exactly the CANNOT_SAY case ('the SERP returned N url(s) and none on <domain> -- ABSENT is the honest result, never confused with NOTHING_FOUND'); AMGT-rk-43's field-only reading (built BY SUBTRACTION over status/query/absence_class/basis, never a parsed sentence) correctly refuses to guess and reads these as UNREADABLE_OBJECT, not the order's own asserted SEARCHED_LINKS_UNREADABLE.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W45-S1",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round17.md:51 W45-S1 held by Andrew's standing 'no fleet re-runs until validated'",
      "org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md:4136 W45-S1 is held",
      "no later commit names an absence_class backfill of BABA/BA/COST/HD (git log -i --grep=absence_class since 2026-09-17)"
    ],
    "remedy": "Still owed: the producer re-run that would populate absence_class on the 4 pilot objects was held under Andrew's no-fleet-rerun word, and no later backfill is evidenced.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-W9-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "16 of 89 folders in AMGT-s-12's universe.json carry bloomberg_ticker.value == 'AAPL US' with status MEASURED even though their folder names name distinct companies -- an identity-layer data-quality anomaly this cell's ticker selection had to route around.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W9-S1",
      "628b975b49 (ancestor of HEAD): s-12 amendment -- shared-template-placeholder fix downgrades a MEASURED ticker two or more folders share",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json at HEAD: ticker_status_partition MEASURED 32, zero 'AAPL US' values MEASURED, the 16 listed under shared_ticker_placeholders_downgraded",
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v1.md:34 C-S1 -- the 16-way identity collapse is REAL and ALREADY REMEDIATED, 32 MEASURED of 32 distinct",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root.md last <status> complete"
    ],
    "remedy": "Remediated: the s-12 shared-template-placeholder fix downgrades any MEASURED ticker shared across folders, so 'AAPL US' is no longer MEASURED for the 16 folders.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W140-S2",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AC3's literal invocation chains `ui-contract-check.mjs --scope body --states list ... && ui-class-census.mjs ...` -- but 'list' carries pre-existing, out-of-this-cell's-scope predicate FAILs (weights [300,500,600], radii [\"8px\"]) at EVERY scope, per Bound 2's own instruction to leave them standing rather than fix them, so ui-contract-check.mjs always exits 1 on this state and the `&&` never reaches the census command.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W140-S2",
      "d3f1d8620e (ancestor of HEAD, 2026-09-24T14:08Z) adds row AMGT_RESAPP-Z-S250, the disarm carrier for W140-S2, and flips rm-1 complete",
      "task-orders/AMGT_RESAPP.TO-AMGT-rm-1.the-instrument-rekeyed.md last <status> complete",
      "adjudications/ADJUDICATION_v48.md:27 (24d6af9249) GRADUATED W140-S2 via Z-S250, verified at the artifact"
    ],
    "remedy": "Remedied by the issuer's disarm carrier Z-S250: the issuer read the census unchained (FILES 31 TOTAL 0) and corroborated the scope pairs, and rm-1 closed terminal on that read.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W165-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Re-running two still-OPEN rows' own claims today (AMGT-tt-4's measurement cell) finds both defects APPEAR RESOLVED in the world, though neither carries a disarm carrier: Z-S236's deployed no-span reader now serves 0 no-span sentences across the same 12 documents (was 179), and Z-S251's eleven-plus stale #0A1733 prose sites are gone from a repeat of the row's own comp-find query (only the row's own allow-listed 10 remain).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W165-S1",
      "6841a976e4 (ancestor of HEAD) ADJUDICATION_v55: Z-S236 re-measured 12 of 12 SERVED, 0 no-span; Z-S251 query re-run 10 hits, all allow-listed",
      "adjudications/ADJUDICATION_v55.md:47 W165-S1 GRADUATED (it asked for this seat's read, given above)"
    ],
    "remedy": "No act owed: the row asked for a CVO read of two re-measurements, and ADJUDICATION_v55 gave that read and graduated Z-S236, Z-S251 and this row.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S201",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Exec Management tab prints the CEO line with a DOUBLE full stop on every NOT_SEARCHED name ('... so the CEO web search was not run..'): AMGT-rk-75's approved table sentences end in a period and the tab appends another after the reason. Also seen: the panel subtitle 'Officers from the filing, with tenure against the pool' is false on a Bloomberg-fallback roster (CSL, 6861).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S201",
      "portal f22e369c (ancestor of portal gitlink ec65c5d6 at HEAD) fix(ExecManagementTab, AMGT-rk-80): one period on the CEO line, subtitle names the Bloomberg fallback",
      "portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx:165 endSentence() used at :188/:195/:211; :428-431 subtitle switches on roster_source BLOOMBERG_FALLBACK",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-80.exec-tab-text-fixes.md last <status> complete"
    ],
    "remedy": "Remedied by AMGT-rk-80: the CEO line ends in one period and the subtitle names the Bloomberg fallback.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S219",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The SA forecast-fallback identity check compares our company name against SA's attributes.name, which is the TICKER; the company name is attributes.companyName. BA is wrongly refused; COST and BABA pass only by substring.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S219",
      "63a11651f2 (ancestor of HEAD) code(AMGT-rk-111): SA forecast-fallback identity check prefers attributes.companyName (Z-S219)",
      "integrations/bloomberg/research/sa_forecast_fallback.py:240 sa_name = sa_attrs.get(\"companyName\") or sa_attrs.get(\"name\")",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-111.sa-identity-company-name.md last <status> complete",
      "adjudications/ADJUDICATION_v31.md:45 (9c5beff60d) reads Z-S219 remedied on the CVO's own probe"
    ],
    "remedy": "Remedied by AMGT-rk-111: the SA identity check now prefers attributes.companyName over the ticker-shaped attributes.name.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S225",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "rk-114's test_no_enrich_rows_byte_identical builds with the PINNED (pre-rk-114) crosswalk module but the LIVE registrations.json, so rk-113's ENRICH row now makes the pinned module raise its collision refusal: the identity suite reads 1 failed, 66 passed on the merged tree, where it read 67 passed in each worker's own worktree.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S225",
      "c2a76629e2 (ancestor of HEAD) fix(AMGT_RESAPP-rk-120): Z-S225's pinned-module arm tests the property not the repo's state",
      "lib/research/identity/tests/test_crosswalk_enrich_coverage.py:306-308 no_enrich_regs filters mode ENRICH before the pinned build",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-120.identity-cleanup-and-schema-gate.md last <status> complete"
    ],
    "remedy": "Remedied by AMGT-rk-120: the byte-identity arm builds the pinned side from registrations with ENRICH rows filtered out, so it tests the property and not the repo's state.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S236",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Deployed AMGT thesis reader serves 179 no-span sentences among 389 aggregate sentences across the full current 12-document drafting population.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S236",
      "6841a976e4 (ancestor of HEAD, 2026-09-28T21:04Z) ADJUDICATION_v55: Z-S236 GRADUATED on the CVO's own measure_served.py run, 12 of 12 SERVED, 0 no-span, 401 control fired",
      "lib/research/api/scoped_amgt.py:2475 and :2500-2504 held_no_span_at_read / held_no_span_on_object at HEAD",
      "2e9c087db4 (ancestor of HEAD) close(AMGT-ad-2): 179 no-span sentences held on 12 stored D-1 documents"
    ],
    "remedy": "Remedied: the deployed reader holds no-span sentences at read, and the CVO's independent re-run of measure_served.py read 0 no-span of 210 on 12 of 12 documents; ad-2 later held the 179 on the stored objects.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-28T21:04Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S244",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RESOLVES AMGT_RESAPP-W130-S1 at the drain: the round-37 contract-check fixtures land under portal/src/pages/SecurityAnalysis/__harness__/tests/, the naming gate's own exemption class for fixture data (naming-gate.py:1421-1423), and ui-contract-check.mjs's default --fixtures path follows; sha256 4ad01d45...8aa0e21 unchanged. Also corrects that row's fabric (reads laptop; the seat, worktree and gate run were site-z). FIRST APPEND LOST: this row was appended at ~07:14Z and overwritten by 75659fe11a's rewrite of the shared file before it committed -- the append-only race, from the other side.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S244",
      "a0ca844eeb (ancestor of HEAD) adds row Z-S244; merge 5c2af33d86 (ancestor of HEAD) carries portal 513bb3c5 (ancestor of portal HEAD)",
      "portal/scripts/ui-contract-check.mjs:77 default --fixtures src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json; the file exists at HEAD",
      "task-orders/AMGT_RESAPP.TO-AMGT-rl-1.the-instrument.md last <status> complete"
    ],
    "remedy": "No act owed: the row is itself the resolution of W130-S1, executed in-round when the fixtures moved under __harness__/tests/.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S253",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "rm-7's apply cannot move the function's code: the Lambda's source_code_hash is read from the S3 ARTIFACT OBJECT, that object still carries the PRE-rm-4 bytes, and NO CELL IN THE ROUND OWNS THE BUILD+UPLOAD that sits between rm-4's merge and rm-7's apply -- rm-4 'does not deploy' and rm-7 'changes no code', so the precondition is an uncovered member of the decomposition.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S253",
      "35038a7459 (ancestor of HEAD) deploy(rm-7 LANDED + ledger CLOSED + Z-S258 disarms Z-S253/254/256): artifact uploaded, apply 1 changed, CodeSha256 y5bJBQsP...",
      "task-orders/AMGT_RESAPP.TO-AMGT-rm-7.the-deploy-leg.md last <status> complete",
      "adjudications/ADJUDICATION_v48.md:30 (24d6af9249) Z-S253 GRADUATED via Z-S258, by execution"
    ],
    "remedy": "Remedied by execution under Z-S258: issuer amendment 2 added the artifact upload to rm-7, the apply moved CodeSha256, and rm-7 closed complete.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S260",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SELF-CORRECTION to this seat's own row filed 40 minutes ago: the sibling-artifact join is very nearly VACUOUS as a resolution signal, not merely caveated. 161 of 181 ARMED rows (89 percent) appear in an ADJUDICATION because the L8 compile enumerates a round's rows BY CONSTRUCTION -- so 'appears in a sibling' is near-universal and carries almost no information about resolution. Separately, the prefix-substring hazard is REAL and its incident count here is measured at ZERO.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S260",
      "17e4d99e0e (ancestor of HEAD) adds row Z-S260, disposition GRADUATED; its notes state NOTHING HERE ASKS ANY SEAT FOR AN ACT"
    ],
    "remedy": "No act owed: a self-correction record that asks no seat for an act; the structured resolves field of R-81 is the remedy it names.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S266",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ADJUDICATION CARRIER for two round-37 rows naming 2.0.0_SA_COO~Z that still read UNDER_INVESTIGATION on `_latest_dispositions()` because round 37's adjudication predates the rl-9 drain that resolved them: AMGT_RESAPP-Z-S247 (the MODEL state's identity line at ratio 1.48 on the band, lowContrastChars 37) and AMGT_RESAPP-W137-S1 (tabs.harness.cjs throwing MODULE_NOT_FOUND on LeadPanel's new PanelFooter and Segmented imports). Both fixed by 0.9.0_WK_AMGT_RESAPP~138 on AMGT-rl-9 and re-measured by the issuer today.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S266",
      "993b8234b9 (ancestor of HEAD) adds row Z-S266, disposition GRADUATED, adjudicates Z-S247 and W137-S1",
      "portal c2b51a46 (ancestor of portal HEAD); portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:85 PanelFooter stub and :121 Segmented stub at HEAD"
    ],
    "remedy": "No act owed: an adjudication carrier recording that the rl-9 drain fixed Z-S247 and W137-S1; both fixes hold at HEAD.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S276",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Disarm-owner read of AMGT_RESAPP-Z-W158-S1: the scoped API's 16 AMGT routes use a single-segment {security_key} template (0 greedy), so a key sent with a raw '/' (BP/_LN_Equity, NG/_LN_Equity) matches no route; whether an encoded %2F reaches the function, and how the page's request builder encodes the key, is UNMEASURED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S276",
      "130c3be101 (ancestor of HEAD) drain(AMGT-an-6): the encoded key reaches every per-security route",
      "bf4b04b120 (ancestor of HEAD, 2026-10-03T01:40Z) close(NEVER-2, AMGT-an-7): redeploy; c14 BP-SLASH-_LN_Equity reaches overlay/thesis/peers/coverage 4 of 4",
      "lib/research/api/scoped_amgt.py:916-927 _route_security_key unquotes and decodes the slash-safe form; portal/src/api/endpoints/amgt-lead-panel.ts:136 encodeURIComponent(securityKey)",
      "adjudications/ADJUDICATION_v77.md:19 (e8ee439150) encoded key BP%2F_LN_Equity answers 200 on thesis, peers, overlay and timeline (4 of 4)",
      "task-orders AMGT-an-6 and AMGT-an-7 last <status> complete"
    ],
    "remedy": "Remedied by AMGT-an-6 (the route decodes a percent-encoded or slash-safe key) and its an-7 redeploy; the CVO read BP%2F_LN_Equity, the form the page's encodeURIComponent sends, answering 200 on 4 of 4 routes.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-03T01:40Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S283",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TWO DISTINCT 'R-21's exist in this estate and a bare 'R-21' does not disambiguate them: the ratified register rcg/rulings/RULINGS.jsonl holds an R-0021 that RESOLVES cleanly and is a COORDINATION ruling about spawning a CTO seat, while the vendor grant every AMGT order cites is a separate Andrew-direct R-21 @b390c36444 that lives only in the message record.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S283",
      "adjudications/ADJUDICATION_v53.md:26 (56aca7662b) GRADUATED with remedy: cite Andrew-direct R-21 WITH @b390c36444",
      "task-orders/AMGT_RESAPP.TO-AMGT-yy-5.the-one-build.md:16 bare '(R-21, scripted)' with no commit at HEAD; xx-3:87 does carry @b390c36444",
      "rcg/rulings/RULINGS.jsonl:22 R-0021 still the 2026-08-03 coordination ruling (file last changed d4ab5453dd, 2026-08-06)"
    ],
    "remedy": "Open: the citation fix is applied unevenly (yy-3 says Andrew-direct R-21 with no commit, yy-5 says bare R-21) and RULINGS.jsonl still holds only the coordination R-0021; the CTO owes the citation rule or a renumbering.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md@4a89bef967 section E: rcg cited R-00NN, PRD-local cited PRD R-NN"
      }
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S292",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT_HARVST's LOCAL-only portal commit 92a25762 mounts TimelinePanel in HeaderBrief.tsx; RESAPP's exportCompare.harness.cjs loads HeaderBrief and cannot resolve TimelinePanel's '@/api/api-client' alias, so every FWD-30 export-compare on a tree carrying 92a25762 reads CAPTURE_FAILED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S292",
      "65461f9916 (ancestor of HEAD) drain(round 46 uu-2 + uu-3): harness loads the timeline mount (portal 9125df0b, ancestor of portal HEAD)",
      "portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs:125-130 TimelinePanel stub at HEAD",
      "task-orders/AMGT_RESAPP.TO-AMGT-uu-2.the-harness-loads-the-timeline-mount.md last <status> complete",
      "adjudications/ADJUDICATION_v56.md:30 (4be12a2f1a) Z-S292 GRADUATED, uu-2 AC1 4 of 4"
    ],
    "remedy": "Remedied by AMGT-uu-2: exportCompare.harness.cjs stubs TimelinePanel, and the harness loads the timeline mount on 4 of 4 sets.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S298",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The vv-4 pool-prefix grant is APPLIED but cannot be COMMITTED: the naming gate refuses 'amgt/harvest/gold/research-dossier/' in ENFORCE mode as NEW and OUT-OF-PATTERN, wanting research_dossier -- a form that holds ZERO objects. DESIRED and APPLIED now disagree on that one line, and the remedy is a registry row outside this order's paths.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S298",
      "e1e4ae43d4 (CTO verdict) and 1c410c5936 (ancestor of HEAD, 2026-09-29T10:03Z) rollback(AMGT-vv-4): vv-4 ROLLED BACK, entry CLOSED",
      "adjudications/ADJUDICATION_v57.md:19 (556a5a37f8) simulate_principal_policy reads research-dossier implicitDeny, chatter_event allowed",
      "26113dbc97 (ancestor of HEAD) feat(AMGT-ww-1): grant the CANONICAL research_dossier/ prefix, committed before the apply",
      "infra/aws/terraform/harvest/scoped-amgt-api.tf:226 \"amgt/harvest/gold/research_dossier/\" at HEAD; task-orders AMGT-ww-1 last <status> complete"
    ],
    "remedy": "Disarmed by rolling vv-4 back on the CTO decision so that DESIRED equals APPLIED; remedied by ww-1, which committed and applied the canonical research_dossier/ grant.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-29T10:03Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S312",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer attribution for AMGT_RESAPP-Z-S311: zz-8 AC2's false premise was the issuer's cut -- zz-6's AC1 handed thesis_driver_chart the re-verified driver in process and the zz-8 COO half predicted a SERVED chart from it, neither exercising the join to the D-1 drafting document the served /thesis reads.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S312",
      "adjudications/ADJUDICATION_v62.md:13 and :93 (108fb01895, ancestor of HEAD) /api/scoped/amgt/security/ASML_NA_Equity/thesis 200, thesis_driver_chart SERVED, source filing",
      "adjudications/ADJUDICATION_v62.md:54 Z-S312/Z-S311 GRADUATED"
    ],
    "remedy": "Remedied in round 52: the D-1 drafting regeneration landed, and the served /thesis route returns thesis_driver_chart SERVED from the filing for ASML on the deployed build.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S328",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM ACT for AMGT_RESAPP-Z-W200-S1 (disarm_owner this seat): the BA 'no research pack' sentence is page text (portal reasonWords.ts:33 rewrites the served class-A reason); the presentation writer DSGN_AMGTV1 (2.0.0_SA_COO~D, CONTRACT s.0) takes it as round-16 order DSGN_AMGTV1.TO-AV-g-5.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S328",
      "71b7aef709 (ancestor of HEAD) adds row Z-S329, correcting Z-S328 (COO~D msg 27627)",
      "adjudications/ADJUDICATION_v69.md:42-43 (7277aabc16) Z-W200-S1 GRADUATED, disarmed by Z-S328 as corrected by Z-S329"
    ],
    "remedy": "Superseded by Z-S329: Z-W200-S1 was disarmed by DSGN's issuer wording ruling, not by AV-g-5, and ADJUDICATION_v69 graduated both rows.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S344",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r64_served.py c10 now carries an expectation that r66_served.py c22 contradicts on the same deployed bytes: c10's C2 clauses require the 90- and 365-day price windows to serve 0 rows and 'not produced yet', while c22 requires them to serve 94 and 95 rows. After ap-3 landed the generations and ap-4 shipped the reader, c10 reads SERVED: NO with exactly 4 FAIL lines, all of them those clauses. The ap-4 order and COO half both scope c10 to its 30-day clauses, so nothing was mis-graded here -- but any later round that runs c10 unscoped reads NO on a healthy function.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S344",
      "6e1852e03f (ancestor of HEAD) check(round 66): r64_served c10 retires its 90/365 clauses; disarms row Z-S344",
      "deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py:114-117 SKIP C2 90/365 retired, graded by r66_served c22 (row Z-S344)",
      "adjudications/ADJUDICATION_v79.md:53 (ff7c1e5c7b) Z-S344 disarmed by its owner @6e1852e03f"
    ],
    "remedy": "Remedied by the owner: r64_served c10 retired its 90/365 'not produced yet' clauses, and r66_served c22 grades those windows.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W117-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AC0's literal invocation includes `python integrations/bloomberg/auth/dapi_check.py`, which sends a REAL, live SPX Index/PX_LAST ReferenceDataRequest every time it runs (confirmed by reading the script: it opens a session and sends a genuine ReferenceDataRequest, not a cached/idempotent check) -- re-running it this session, as the literal criterion demands, would spend a SECOND SPX probe against a cell whose own COO/CTO halves size the WHOLE CELL at exactly 2 requests total and name 'more than the sized requests are spent'/'quota above the 2 stated requests' as an explicit ROLLBACK TRIGGER. The predecessor already spent request 1 of 2 on this exact probe (recorded in .scratch/r117/ac0_out.txt, 'DAPI: UP', ~16:23 local this session's continuation).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W117-S5",
      "adjudications/ADJUDICATION_v35.md:83-91 (c79b5c10fe) GRADUATED W117-S5 with the rule: a criterion that fires egress inside a BASELINE step is refused at the cut",
      "git grep over .tools org/ref .claude docs for the baseline-egress refusal returns 0 hits; .tools/to-pipeline-gate.py has no dapi_check or baseline-egress limb"
    ],
    "remedy": "Open: ADJUDICATION_v35 ruled the cut-time refusal of egress in a baseline step as prose practice only; no AC0 skip-if-spent clause, per-session sizing or gate limb was found, so the issuer still owes one.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-09T20:19:00Z"
    },
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_LEDGER.json@4c3f3fcb2e: its object is AC0 of a complete order (dapi_check.py baseline sent a live Bloomberg request each run); Bloomberg pulls now go only through the queue (CLAUDE.md law) and the double-spend issue is recorded resolved at 8555ce7e12; no open order carries AC0"
      }
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W171-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "AC2 (api-suite.sh) cannot run in the sparse-cone worktree: 268 of the suite's tests error at collection/setup with FileNotFoundError on infra/logic/registry/systems.json, a path outside the cone (lib, integrations, .tools, org, docs, rcg), so the criterion's '308 passed' is unreachable here.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W171-S1",
      "adjudications/ADJUDICATION_v58.md:54 (33ed750433, ancestor of HEAD) the CVO's run of round48/checks/api-suite.sh on the full tree: 323 passed, exit=0"
    ],
    "remedy": "Remedied by the remedy the row named: api-suite.sh was run on the full tree, which carries infra/logic/registry, and read 323 passed with exit 0.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W173-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "At 2026-09-29T22:01Z the served FWD-30 grade on the attribute key is 95 of 96 identified names; the one NOT_OK is 6501_JP_Equity, whose identity now RESOLVES (so it is graded, not 'unidentified') while the deployed print route REFUSES it, leaving the export side a 173-byte refusal body.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W173-S5",
      "adjudications/ADJUDICATION_v60.md:68 (eaa8419bce, ancestor of HEAD) Z-W173-S5 GRADUATED: the block landed, FWD-30 reads 96 of 96 identified"
    ],
    "remedy": "Remedied: Hitachi's model block landed (AMGT_CORPUS v20), and FWD-30 reads 96 of 96 identified names.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AC5's `grep -r` over infra/aws/terraform/research/ transiently counted a byte-coincidence match inside a gitignored `terraform init` provider-plugin binary as a loopback violation, reading '1' instead of '0' until the ephemeral `.terraform/` cache was removed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S3",
      "adjudications/ADJUDICATION_v1.md C-S3 (d98b82113b) GRADUATED W2-S3 with W2-S4/W1-S3/W1-S4 and routed it to the comp-tool rail owner 1.0.0_SA_CTO~Z",
      "remediations/REMEDIATION_v1.md C-S3 row remedy 'exclude the ephemeral floor by construction', state OPEN",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (inheriting issuer) reads W2-S3 cleared once the cache was removed and rd-2 complete: that clears the instance, not the recurrence",
      ".tools/_comprail.py:340-341 EPHEMERAL_DIRS has no .terraform at HEAD, and comp-find's default corpus all includes gitignored files"
    ],
    "remedy": "Open: the ephemeral floor is still not excluded by construction; .terraform is absent from the comp-find floor, so a gitignored provider binary is still searched, and the rail owner's REMEDIATION_v1 remedy stays unbuilt.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-W214-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "After the projection cut, the largest remaining cold stages of BA /timeline/day are the identity resolution (~0.85-0.93 s) and the 2.6 MB mention snapshot GET (~0.55-0.8 s locally); neither is in this cell.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W214-S2",
      "adjudications/ADJUDICATION_v77.md:45 (e8ee439150, ancestor of HEAD) Z-W214-S2 GRADUATED (Z-C-S451) as enrichment",
      "bf4b04b120 (ancestor of HEAD) close(AMGT-an-7): c15 3 of 3 cold at 1.9-2.3 s against a 5 s bound"
    ],
    "remedy": "No act owed: a cold-stage timing measurement graduated as enrichment input (Z-C-S451); the cold read now passes its bound.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W38-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "raw/bloomberg/<key>/<stamp>/ can carry a stamp folder holding ONLY an identity.json (no refdata.json/histdata.json) for a key whose Bloomberg raw has never landed -- measured on all three validation names -- so a stamp folder existing is not evidence raw landed, and model_block_pull.py's own _latest_stamp (used unmodified by its stage_derive) would crash NoSuchKey rather than report absence if pointed at one of these keys.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W38-S5",
      "06296daccd (ancestor of HEAD) build(AMGT-rk-70): _latest_stamp requires both refdata.json and histdata.json, raising NoRawStampError",
      "integrations/bloomberg/research/model_block_pull.py:714-719 qualifying = _stamps_with_raw_pair(...); raise NoRawStampError at HEAD",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-70.latest-stamp-requires-raw-pair.md last <status> complete"
    ],
    "remedy": "Remedied by AMGT-rk-70: model_block_pull._latest_stamp now requires a refdata+histdata pair and raises NoRawStampError rather than NoSuchKey.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W45-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "This worker's assigned worktree needed THREE undocumented environment repairs before the order's own named deploy mechanism would run: (1) portal/node_modules was a MALFORMED Windows junction (fsutil reparsepoint query showed a doubled substitute name 'C:\\C:\\Users\\...', confirmed via native fsutil, not a bash artifact) so `./node_modules/.bin/tsc` was absent -- repaired via the order's own authorized bun-install exception; (2) the portal worktree's git HEAD was DETACHED (not on a named branch, unlike sibling worker portal worktrees which all carry one) so the portal commit this order made was reachable via no ref but this worktree's own HEAD until a branch was created after the fact; (3) infra/aws/terraform/harvest had never been through `terraform init` in this worktree, and even after init, the FIRST plan attempt failed because .build/chatter-axis-producer.zip (an UNRELATED resource's build artifact, built by lambda_src/build_zip.py) did not exist, so no plan -- targeted or otherwise -- could render at all until that unrelated zip was built once.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W45-S2",
      "adjudications/ADJUDICATION_v14.md:383 (913a02de36) lists the id; git log --all --grep=W45-S2 finds only the filing d5977aeee6 and AMGT_HARVST's unrelated id of the same suffix"
    ],
    "remedy": "Open: no commit or order shows the three provisioning repairs (junction check, portal worktree on a named branch, pre-warmed terraform init and build zip) in the worker spawn path.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md@fb9ca91ad5 section E: a worker does not deploy"
      }
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S346",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "aq-5's code leg is LANDED and aq-2's window tone is still not served: the deployed role cannot read the chatter_window prefix, so 95 of 95 rows on /lead-panel/timeseries/collected/chatter serve tone_reason 'the window table could not be read (AccessDenied)'. AC2's expectation (mismatches 0) is unmet at mismatches 74, so the halves' rollback trigger has fired on its literal terms -- but the rollback cannot cure it (the base read the same 74) and would revert c23, c25 and c26, all three of which now PASS. Rollback NOT taken; the disposition is the issuer's.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S346",
      "768731795b (ancestor of HEAD) grant(AMGT-aq-5 leg 3 / AMGT-aq-6): chatter_window read prefix LANDED, unreadable 95 -> 0, mismatches 74 -> 0",
      "389089e765 (ancestor of HEAD, 2026-10-04T23:41Z) adds row Z-S347, the disarm record for Z-S346",
      "infra/aws/terraform/harvest/scoped-amgt-api.tf:251 \"amgt/harvest/gold/chatter_window/\" at HEAD; task-orders AMGT-aq-5 last <status> complete",
      "adjudications/ADJUDICATION_v80.md:77 (69ce44def1) Z-S346 disarmed in fact"
    ],
    "remedy": "Remedied by the aq-5 leg 3 grant of the chatter_window read prefix; Z-S347 records the disarm, and the CVO's probe reads tone served.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-04T23:41Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W141-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AC3's literal invocation calls ui-measure.mjs with a --route flag, but only ui-smoke.mjs's missing --route flag was named in the task order's WHAT YOU BUILD text (item 3: \"If ui-smoke.mjs takes no --route flag, add the smallest one to it ... and say so\"); ui-measure.mjs took no --route flag either (positional args[0] only) and would have silently mis-parsed '--port' as the route.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W141-S1",
      "562fe050e2 (ancestor of HEAD): rm-2 drain merged worker ~141 with the additive --route flag on both scripts",
      "portal/scripts/ui-measure.mjs:692 at portal HEAD ec65c5d6 (= the CLOUD gitlink): route reads --route when present, else args[0]",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rm-2.the-free-chrome.md last <status>complete</status>",
      "adjudications/ADJUDICATION_v48.md:29 GRADUATED -- INERT, additive flag already applied"
    ],
    "remedy": "No act owed: the in-lane additive --route fix landed with rm-2 and is present at HEAD.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S176",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The round-14 acceptance sweep silently omits AMGT-rk-58's five criteria: _order_criteria scopes to the FIRST <proof_of_spec> span in the document, and rk-58's first such span is a PROSE mention whose captured body is the literal '...', so the real block is never read -- the five criteria are not UNVERIFIABLE, they are absent from the sweep and from its denominator.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S176",
      "01727c89bf (ancestor of HEAD): rk-69 line-anchors _PROOF_BLOCK_RE on both the open and close <proof_of_spec> tags",
      ".tools/surprise-row-gate.py:1307 at HEAD: _PROOF_BLOCK_RE is line-anchored (re.M | re.S), so a prose mention no longer captures the block",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-69.acceptance-sweep-anchored-proof-block.md last <status>complete</status>"
    ],
    "remedy": "Fixed by rk-69: the criterion parser anchors the proof block to line start, the narrowest remedy the row named.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T16:22Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S202",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "CAT_US_Equity, a VALIDATION name, serves ONE officer (Derek Owens, Chief Legal Officer) as its whole RESOLVED roster -- so it reads NO_CEO_ON_ROSTER and has no CEO on the page -- because its 10-K's Item 10 says 'Information required by this Item appears in Item 1D of this Form 10-K' and the roster parser does not follow that cross-reference: it parsed Item 10's 27,766 chars of incorporation-by-reference text and caught one stray officer.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S202",
      "a13b0fc140 (ancestor of HEAD): rk-79 drain -- CAT served INCOMPLETE-NO-CEO with a readable Item 1D reason",
      "63d4adf6d1 (ancestor of HEAD): row Z-S206 disarms Z-S202 -- no-CEO census reads 0 of 15, never RESOLVED with no CEO",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-79.jp-president-and-readable-roster-reason.md last <status>complete</status>",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S206 dismissal_reason: the false-complete condition no longer holds for CAT or any of the 15 names"
    ],
    "remedy": "Disarmed by rk-79 and row Z-S206: the roster is no longer served false-complete; a full CAT roster from Item 1D stays a named follow-on.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T21:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S220",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SERP freshness reads bright-data/harvest/bronze/serp/security_key=<k>/ but the SERP writer writes serp/date=<d>/<qsha>-p<n>.json, so freshness can never find a SERP object; SERP keys carry no security key at all.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S220",
      "lib/research/freshness/build_view.py:181-182 at HEAD: latest_bright_data_serp_stamp still lists the serp prefix plus a security_key partition",
      "lib/research/harvest/bright_data_serp.py:6-8 at HEAD: the writer still partitions date=YYYY-MM-DD/<request hash>",
      "adjudications/ADJUDICATION_v30.md:61: Z-S220 resolves with the key design; no landed act found on CLOUD"
    ],
    "remedy": "Still live at HEAD: reader and writer use different partitions; owed the key design (writer adds the security key, or freshness reads a key-to-query index).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-S226",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The CDN has NO cache behavior for /api/scoped/amgt/*, so every Security Analysis request falls to the SPA origin and returns 200 text/html (index.html); the page parses HTML as JSON and renders empty panels. Andrew reported the page blank at ~18:2xZ.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S226",
      "8c038da7e7 (ancestor of HEAD): rk-123 appends one ordered_cache_behavior for /api/scoped/amgt/* at the API origin",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-123.amgt-edge-behavior-apply.md last <status>complete</status>",
      "c69c4866ce (ancestor of HEAD): row Z-S261 is the disarm carrier; live re-measure 401 application/json on every AMGT path, with controls",
      "adjudications/ADJUDICATION_v35.md:39: Z-S226 is remediated (rk-123, verified live)"
    ],
    "remedy": "Fixed by the rk-122/rk-123 CDN behavior for /api/scoped/amgt/*, applied under a closed ledger and re-measured live.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-22T20:53Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S238",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "opal-amgt-scoped-api returned 28 unhandled 500s in the 09-19..09-23 window, 500s that NO instrument in this estate can attribute to a route or a firm -- and the same blindness is what bounds every future incident reconstruction on this surface.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S238",
      "infra/aws/lambda/research/scoped_amgt_api/lambda_function.py:60-64 at HEAD: the error line still carries only request_id, type and detail -- no route, security_key or firm",
      "git log --grep=Z-S238 on CLOUD: only the filing commit 39cd826599; no remedy commit",
      "adjudications/ADJUDICATION_v75.md:33: GRADUATED (Z-C-S447) -- still an observability gap; not re-measured"
    ],
    "remedy": "Still live at HEAD: owed one structured per-request log line (route_key, security_key, edge-injected firm id) from the scoped API writer.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md@fb9ca91ad5 section E: not cut; returns as a new row when an outcome needs it"
      }
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-06T22:04:38Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S247",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AT THE rl-6 DRAIN the six-state contract check read the MODEL state lowContrastChars PASS -> 37: the identity line (\"BA US\", \"identity\", \"crosswalk/v1\", \"@ 2026-09-24\") renders navy ink rgb(22,51,114) on the band ground rgb(10,23,51), ratio 1.48, because ModelTab.tsx places IdentityLine (rl-2's component, ink unset so it follows its ground) ON THE BAND rather than inside its white panel. Routed to AMGT-rl-9, the one cell admitted to every src/pages/SecurityAnalysis/** file, whose criterion is the six-state PASS.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S247",
      "6fdce83b63 (ancestor of HEAD): rl-9 drain -- ModelTab.tsx IdentityLine moved off the band",
      "0cf98a11f5 (ancestor of HEAD): row Z-S249, the issuer disarm carrier for Z-S247",
      "993b8234b9 (ancestor of HEAD): row Z-S266 adjudicates Z-S247 -- model lowContrastChars PASS at portal 5e339ffd",
      "adjudications/ADJUDICATION_v47.md:48: lowContrastChars 0 measured across all six states (37 -> 0)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rl-9.designed-states-and-the-reassert.md last <status>complete</status>"
    ],
    "remedy": "Fixed by rl-9: the identity line sits inside its white panel and the model state reads lowContrastChars 0.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T12:04Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S254",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The served print PDF is NOT byte-deterministic -- it carries a render-time /CreationDate -- so rm-7's AC2/L2 ('body sha256 EQUAL to the BEFORE sha; a different sha is the ROLLBACK trigger') can NEVER pass, and following it literally would ROLL BACK a correct deploy. R-57's 'verified DELTA=0 on every existing response' does not hold on the raw-byte plane it is stated on.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S254",
      "35038a7459 (ancestor of HEAD): rm-7 landed, ledger closed, row Z-S258 disarms Z-S253/Z-S254/Z-S256",
      "4f93bbf428 (ancestor of HEAD): ruling R-76 amends R-57 so DELTA=0 names its comparand",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S258: AC2 graded on the content-stream comparand, pdf default DELTA=0",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rm-7.the-deploy-leg.md last <status>complete</status>"
    ],
    "remedy": "Disarmed: rm-7 AC2 was re-cut to a CreationDate-free comparand and the deploy passed on it without a false rollback.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T16:02Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S261",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-Z-S226 (the CDN had no behavior for /api/scoped/amgt/*, so every Security Analysis request fell to the SPA origin and returned 200 text/html). CLOSED IN THE WORLD ON 2026-09-22 by rk-122 (terraform 8c038da7e7, cloudfront-distribution.tf +36) and rk-123 (the apply), ledger 20260922T2058Z_amgt-rk123-edge-behavior closed 21:26Z -- TWO HOURS FORTY-ONE MINUTES AFTER THE ROW WAS FILED AT 18:45Z. It sat ARMED for two days with no carrier, which is R-78's class in its sharpest instance: disarmed in the world, open in its field, and nothing in the row able to say so. Carried on the EXISTING `adjudicates` field, not on the new one R-81 proposed: that field already exists in investigation_item.schema.json with a gate limb propagating disposition, and R-81 proposed a duplicate without checking the build ladder's first rung.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S261",
      "c69c4866ce (ancestor of HEAD): files row Z-S261 as the disarm carrier for Z-S226",
      "8c038da7e7 (ancestor of HEAD): the rk-123 behavior the row records"
    ],
    "remedy": "No act owed: a disarm-carrier record for Z-S226, whose fix landed with rk-123.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S268",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "FWD-30 is NOT met on the served plane, and its round-38 REALIZED grade rested on an instrument that cannot see half its DONE WHEN. (1) SERVED: the page, rendered from the deployed function's own responses, discloses 'ABSENT: no description header scalar [CIE_DES, CIE_DES_BULK] ... and no served D-1 company_description sentence ...'; the served format=rich body never mentions a description at all -- 4 of 5 page absences covered verbatim (landed plane: 5 of 5). (2) BOTH PLANES: the rich export carries 17 figures the page does not show, 10 of them the IS_DIV_PER_SHR fiscal series 2016-2025 that the page REFUSES as SIGN-UNRESOLVED, printed in the export as values with an UNRESOLVED label. FWD-30's DONE WHEN reads 'with NOTHING in the export that is not on the page'; exportCompare.harness.cjs computes the extras and never grades them.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S268",
      "996b260d42 (ancestor of HEAD): tt-2 redeploy landed, ledger entry closed",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-tt-1.the-export-carries-every-page-absence.md last <status>complete</status>",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-tt-2.the-redeploy.md last <status>complete</status>",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rq-1.the-export-says-absent-the-way-the-page-does.md last <status>complete</status> (figure extras, round 42)",
      "adjudications/ADJUDICATION_v55.md:129: round45 close-run served.tsv OK 95 of 95, abs_missing/fig_missing/cit_missing 0 on all 95"
    ],
    "remedy": "Fixed by rq-1 (extras) and tt-1/tt-2 (absences plus the verdict predicate), verified 95 of 95 on the served plane.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-27T00:29Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S277",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served plane moved under round 42: after AMGT_CORPUS round 4 re-pulled the model blocks, FWD-30's served comparison reads 0 of 89 OK (round 41: 5 of 89), 89 of 89 pages now carry figures (round 41: 31), and figure extras appear on 88 names -- a data change, not a code change.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S277",
      "adjudications/ADJUDICATION_v52.md:22: GRADUATED -- a recorded vintage",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rq-1.the-export-says-absent-the-way-the-page-does.md last <status>complete</status> (89 of 89 at the same vintage, v52:131)"
    ],
    "remedy": "No act owed: a record that the served FWD-30 grade moved with AMGT_CORPUS data; rq-1 was cut against that vintage.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S284",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "rr-3's AC2 grades a LIVE population that GREW under it -- 94 folders at the cut, 95 at the run -- and the new member 'AIA Group' has no minted canonical identity, so the sweep records CAPTURE_FAILED 1 and the criterion fails on a name the deployed code never touched.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S284",
      "lib/research/identity/registrations.json:1696 at HEAD: folder AIA Group carries a canonical identity (1299_HK_Equity, ADJUDICATION_v53.md:148)",
      "b71972db23 (ancestor of HEAD): rr-3 AC2 passes under amendment 1 pinned population, entry closed",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rr-3.the-redeploy.md last <status>complete</status>"
    ],
    "remedy": "Resolved: AIA Group has a minted identity and rr-3 closed on a pinned population.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S293",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The team's 'served-and-cited' cases are the SECTION HEADINGS: over all 95 live-library dossiers, 34 of 34 non-absent base/upside/downside values read exactly 'Base Case' / 'Upside Case' / 'Downside Case' at locator 0, and 0 carry content -- so FWD-12 limb 3's data half is NOT met and round-46 cell 5 (render the team's cited cases) has nothing to render.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S293",
      "fd44f203a6 (ancestor of HEAD): AMGT_CORPUS round 9 dossier rewrite landed 95 of 95, every served case its own columns of the team scenario table",
      "lib/research/corpus/dossier.py:766-773 at HEAD: cases are filled from _read_case_table via _case_table_field, not the section heading",
      "adjudications/ADJUDICATION_v56.md:104: Z-S293 GRADUATED (cases served by case, AMGT_CORPUS ADJUDICATION_v12)"
    ],
    "remedy": "Fixed in AMGT_CORPUS round 9: the dossier serves each team case from its scenario table.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S299",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CORRECTING MY OWN VERDICT on Z-S298 (self-drive tick 24, msg 26550): I said the grant's literal 's3://opal-data-harvest/amgt/harvest/gold/research-dossier/' was 'carried at HEAD' and so minted nothing, citing lib/research/corpus/tests/test_backlog.py:217. The naming gate's _carried_at_head excludes */tests/* by design (naming-gate.py:791-812, LD-0611-ARM-01), and dossier.py carries only the table name, not the address. By the gate's own definition, the literal IS new. The gate-edit branch of my verdict was built on a carrier the gate does not count; its else-branch (roll back) is the right one, and 1.0.0_SA_CTO~Z took it (e1e4ae43d4).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S299",
      "a910bf58a5 (ancestor of HEAD): files the correction row",
      "e1e4ae43d4 (ancestor of HEAD): the CTO executed the verdict else-branch (roll back)",
      "adjudications/ADJUDICATION_v57.md:34: GRADUATED, rollback verified on the APPLIED plane"
    ],
    "remedy": "No act owed: a correction record; the rollback it endorses was executed at e1e4ae43d4.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S314",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Correction of AMGT_RESAPP-Z-S313's standing (CTO msg 27014 condition 2): a D-1 regeneration that drops served sentences is a DEFECT, not an accepted limit -- carried to round 53 as its own cell. ARMED: any live --rebuild-pool run would regress served /thesis sentences until it is fixed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S314",
      "cd70547173 (ancestor of HEAD): ac-2 amendment 1 files row Z-S316, re-classifying Z-S314 per CTO msg 27185",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S316: the dropped sentences are the verbatim gate HOLD working as designed",
      "adjudications/ADJUDICATION_v64.md:8: GRADUATED, superseded by Z-S316; 0 of 208 scheduled tasks invoke --rebuild-pool",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ac-2.regeneration-keeps-served-sentences.md last <status>complete</status>"
    ],
    "remedy": "Superseded by Z-S316 (CTO msg 27185): not a defect, and a live rebuild runs only under a signed pair.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-30T14:09Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S329",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CORRECTS AMGT_RESAPP-Z-S328: Z-W200-S1 is disarmed by a DSGN issuer RULING, not by order AV-g-5 (which does not change the Thesis pillars wording). 'research pack' is DSGN's designed worded form of the served 'class A report'; since DSGN AV-f-5 the Exec sentence agrees with it, so the page faces no longer contradict.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S329",
      "71b7aef709 (ancestor of HEAD): files the correction row",
      "adjudications/ADJUDICATION_v69.md:43: Z-S328, Z-S329 GRADUATED as the disarm carrier and its correction"
    ],
    "remedy": "No act owed: a correction record of the Z-W200-S1 disarm basis; served text needs no change.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer's disarm read of AMGT_RESAPP-Z-W3-S5 (ARMED, disarm_owner this seat): the root .gitignore:47 `lib/` blanket did NOT bite round 2 -- all five round-2 cells' new lib/research/ files landed via safe-commit.sh's `git add -f` and are VALID at HEAD (fec90bfb4f); the residual is only a plain-git verifier undercount, routed to the CVO's round-2 L9.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S4",
      "b750649397 (ancestor of HEAD): drops the stock blanket lib/ rule from the root .gitignore",
      ".gitignore:47-48 at HEAD: the blanket lib/ is recorded as removed; no lib/ ignore line remains"
    ],
    "remedy": "No act owed: a disarm-read record; its residual (the blanket lib/ ignore) was removed at b750649397.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W126-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": ".owned-paths.yaml's static `paths:` table has ZERO entries covering `.scratch/` anywhere (0 of 282 keys), so `owned-paths-validate.py --check-agent` refuses EVERY `.scratch/r126/*` path this order's own <paths> block grants at HEAD -- the dynamic `worker_grant` (task-order-paths) limb that exists exactly to admit such a path is never reached, because `_cmd_check_agent` returns UNDEFINED as soon as `resolve_lane()` finds no STATIC lane, before `check_agent()` (which alone consults `worker_grant`) is ever called.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W126-S3",
      "6bc980ad5d (ancestor of HEAD): owned-paths-validate lets a worker task-order grant reach an UNMAPPED path",
      ".tools/owned-paths-validate.py:428-430 at HEAD: when resolve_lane returns None, _owns_task_order_paths is consulted before UNDEFINED"
    ],
    "remedy": "Fixed at 6bc980ad5d: the check-agent CLI consults the worker grant for unmapped paths such as .scratch/.",
    "owner": "1.0.0_SA_CTO",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-25T05:05Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W171-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Follow-up to AMGT_RESAPP-Z-W171-S1: the issuer widened the cone to infra/logic (ruling by 2.0.0_SA_COO~Z, this session), which removes S1's cause (registry now present; the commit gate's naming limb can read it). AC2 still cannot pass in this cone: 'exit=1, 5 failed, 287 passed, 23 errors', every failure a FileNotFoundError on a path outside the cone (infra/aws/terraform/harvest/scoped-amgt-api.tf x5; portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json x23).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W171-S2",
      "adjudications/ADJUDICATION_v58.md:54: api-suite.sh on the full tree reads 323 passed, exit=0",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ww-2.list-rows-carry-the-served-name-and-classification.md last <status>complete</status>"
    ],
    "remedy": "No act owed: an instrument absence in the sparse cone; the full-tree run passes 323 of 323.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W175-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-xx-3: the walked INTU officer section points to Item 1 of its OWN 10-K, not the proxy, and the proxy names only NAMED executive officers (5), so the proxy gain is the NEO list; the pointer population is 2 of 96.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W175-S1",
      "58a7b5b7d1 (ancestor of HEAD): yy-3 persists the proxy officers with officer_set/label passed through",
      "lib/research/management/proxy_officers.py:286 at HEAD: OFFICER_SET = named_executive_officers",
      "adjudications/ADJUDICATION_v60.md:73: GRADUATED, named_executive_officers is served"
    ],
    "remedy": "Resolved: the proxy list is served under the named_executive_officers label, not as the full roster.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "This cell's own task text and battery-findings note both name the landed SA tickers as BABA/RTX/+1 (sa_ids MEASURED for BABA 137271, RTX, +1); the live store and the merged sa_ids.json both show BABA/BA/COST instead -- no RTX object exists anywhere under raw/seekingalpha/.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S5",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S5 world_is: the worker ran AC1-AC4 against the real landed set BABA/BA/COST"
    ],
    "remedy": "No act owed: a cell-text ticker mismatch; the cell measured the real landed set.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W218-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 90/365 route read made test_rolling_windows.py's price qualified-wait test reach the live DynamoDB table; its shared fixture now stubs the pointer read (one added line, inside lib/research/api/).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W218-S1",
      "db56406c8e (ancestor of HEAD): ap-2 proof VALID with the one-line fixture stub",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ap-2.price-history-build.md last <status>complete</status>",
      "adjudications/ADJUDICATION_v79.md:52: DISMISSED_WITH_REASON, a fixture stub inside the cell"
    ],
    "remedy": "No act owed: an in-cell test fixture stub, recorded and dismissed with reason.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W39-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An Edit-tool call given a bare 'C:\\Users\\Opal Bloomberg\\Desktop\\ajb_workspace\\...' path (rather than the worktree's 'C:\\tmp\\wk-amgt-14-39\\...' path) landed the FIRST HEADER_FIELDS edit for this order in the SHARED main workspace tree instead of this worker's isolated worktree -- caught on the very next command (git status --short showed the worktree file clean while the main tree showed the diff) and reverted with git checkout -- <path> before any further work.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W39-S4",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W39-S4: the mis-targeted edit was reverted on the next command; no commit from the wrong tree",
      "adjudications/ADJUDICATION_v14.md:398: W39-S4 recorded as reverted by the worker"
    ],
    "remedy": "No act owed: a reverted near-miss; a cross-worktree guard would be a new gate nobody ordered.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W54-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "crosswalk.load_crosswalk() resolves the pool's crosswalk/v1/ prefix by sorted(keys)[-1] with NO pinning -- a new vintage (crosswalk/v1/2026-09-19.json) landed live in the pool DURING this MEASURE-only cell's own execution window and silently changed the answer to the SAME unmodified invocation from population 33 (vintage 2026-09-15.json, this order's own stated figure) to population 36, mid-session, with zero code change on either side.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W54-S2",
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S326: remedy is the key-shape filter; CTO ruled newest-wins stays with the resolved key recorded",
      "0164b134ac (ancestor of HEAD): rk-68 crosswalk pool-vintage key-shape filter",
      "lib/research/identity/crosswalk.py:72 and :1176 at HEAD: CROSSWALK_KEY_RE refuses any non-dated key before sorted(keys)[-1] at :1182",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-68.crosswalk-key-shape-filter.md last <status>complete</status>"
    ],
    "remedy": "Fixed per ruling: rk-68 refuses non-dated keys loudly; newest-dated-wins is the ruled policy.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T15:38Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W144-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "PanelFooter.tsx's `content` prop is typed `string` (no ReactNode escape hatch), and its content-side wrapper carries `flex-shrink-0` whenever `leftContent` is truthy -- the likely actual mechanism behind ADJUDICATION_v47 s.2.4's mid-word clip, though not a literal truncate/nowrap/overflow-hidden class name, so it does not match the face's own trigger text verbatim.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W144-S1",
      "portal 4aa49151 (ancestor of portal HEAD ec65c5d6): rm-2 removes flex-shrink-0 from the PanelFooter content wrapper, min-w-0 on both wrappers",
      "8b95f42d33 (ancestor of HEAD): rm-2 closed complete; row Z-S257 disarms W144-S1",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S257 (GRADUATED disarm carrier, clippedTextBlocks 0 in both scopes at DEV 5e339ffd)",
      "portal/src/ui/components/panels/PanelFooter.tsx:104 and :106 at HEAD: both wrappers carry min-w-0, no flex-shrink-0",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rm-2.the-free-chrome.md last status complete"
    ],
    "remedy": "Disarmed by Z-S257: rm-2 dropped flex-shrink-0 and put min-w-0 on both PanelFooter flex wrappers, so the clip mechanism is gone for every caller.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T15:13Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S177",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W40-S2 and W46-S2 compose into a latent SERVING defect neither row states alone: objects ACCUMULATE per security_key with no supersession (W40-S2) and roster.load_source_object() picks sorted(keys)[-1] where 'U'(85) beats every digit (W46-S2), so a key holding a stale UNRESOLVED-SOURCE placeholder will SHADOW a later digit-leading EDGAR accession. Measured against the store: 0 keys serve a placeholder today; 177 of 193 hold ONLY a placeholder and would shadow their own next resolution.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S177",
      "7e28fcb73d (ancestor of HEAD, rk-46): accession-first pick in roster.load_source_object",
      "5c7735af76 (ancestor of HEAD): row Z-S179 disarms Z-S177",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S179 and #AMGT_RESAPP-Z-S262 (both name Z-S177 resolved)",
      "lib/research/management/roster.py:1065-1081 at HEAD: pick_source_key class order accession > doc- > other",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-65.accession-ranking-rule-both-readers.md last status complete"
    ],
    "remedy": "Disarmed by Z-S179 (rk-46 accession-first pick) and closed by rule in rk-65: pick_source_key ranks EDGAR over doc- over placeholders regardless of ASCII order.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T04:10Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S209",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GATE 5 resolves a command's target repo from `git -C <p>` / `cd <p> &&` with a no-whitespace pattern, so on this box (path contains a space) the /prod-deploy push from a quoted absolute worktree path is judged against the WRONG repo and a DT's PROD push is DENIED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S209",
      "472dc71296 (ancestor of HEAD, rk-95): never-rules-gate GATE 5 parses a quoted git -C / cd argument whole",
      "a57bd0a068: round-23 packet, rk-95 drained @fc2d043bf8 with negative controls still DENY",
      ".tools/hooks/never-rules-gate.sh:286-312 at HEAD: quoted and drive-letter paths resolve REPO whole",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-95.gate5-quoted-path-parser.md last status complete"
    ],
    "remedy": "rk-95 fixed GATE 5 to parse a quoted git -C / cd path whole and treat a Windows drive path as absolute; shared-branch push denial kept.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S221",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "detect_language returns 'en' whenever ASCII letters are over half of all letters, so German, French, Italian and every Latin-alphabet language read as English and are never translated, with no warning; the API also drops text_translated from every drafted sentence.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S221",
      "0de2c26e82 (ancestor of HEAD, rk-107): Latin-alphabet stopword detection in detect_language",
      "lib/research/filings/document.py:393-433 at HEAD: ascii-majority branch runs the stopword test (Z-S221)",
      "ADJUDICATION_v31.md:31: CVO probe reads de/fr/it/en correctly",
      "git grep -i translat over lib/research/api/ at HEAD: 0 hits; positive control lib/research/filings/drafting_build.py carries text_translated (2 hits)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-107.language-latin-and-cs386.md last status complete"
    ],
    "remedy": "Detection limb fixed by rk-107 (de/fr/it detected); the API limb is still live: the scoped API serves no text_translated on drafted sentences, so a cell must carry it to the route.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S227",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "0 of 5 Security Analysis tabs carry an isError branch: each gates its body on {!isLoading && data && ...}, so a FAILED read renders a titled panel with an empty body -- indistinguishable from 'no data for this name'. This is what made Z-S226 silent.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S227",
      "portal c2b51a46 (ancestor of portal HEAD, rl-9): Thesis, Exec, Posture and Model tabs gain an isError branch",
      "portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:247, ExecManagementTab.tsx:437, PostureTab.tsx:665, ModelTab.tsx:955, PeersTab.tsx:257 at HEAD: isError branch per tab",
      "portal/src/api/api-client.ts:176-181 at HEAD: a non-JSON 200 body rejects in response.json(), which reaches the query's isError"
    ],
    "remedy": "rl-9 added an isError branch to the tabs; all five Security Analysis tabs now render a named failure distinct from an absent object.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-24T11:35Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S239",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CORRECTION AND DISARM of AMGT_RESAPP-Z-S238's first limb: the unhandled 500s are HISTORICAL, not live -- all three error classes stopped BEFORE the no-span cutover and there have been ZERO since it. S238's attribution-blindness limb is UNAFFECTED and stays ARMED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S239",
      "3e33937f78 (ancestor of HEAD): row Z-S239 filed, the 500s historical with zero since the cutover",
      "S238's attribution limb is carried on its own row, not this one"
    ],
    "remedy": "No act owed: a correction-and-disarm record of Z-S238's first limb; the remedy (no runtime lib.opal_naming import) had already shipped.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S249",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-Z-S247 (model state lowContrastChars 37 on the identity line over the band): rl-9 (0.9.0_WK_AMGT_RESAPP~138) moved ModelTab.tsx's IdentityLine off the band (portal c2b51a46, merged into DEV at 65a41a1f, drained @6fdce83b63) and the issuer read BOTH the worker's contract-check-final/model.json and its own drain-time contract-check-after-rl-9/model.json at lowContrastChars 0 -- the disarm condition Z-S247 named, met on two instruments.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S249",
      "portal c2b51a46 (ancestor of portal HEAD, rl-9): ModelTab IdentityLine moved off the band",
      "6fdce83b63 (ancestor of HEAD): rl-9 drained"
    ],
    "remedy": "No act owed: a disarm carrier for Z-S247; rl-9 moved the IdentityLine off the band and lowContrastChars reads 0 on six of six states.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S256",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "rm-7's build REFUSES on a precondition no cell owns either: the generated module lib/research/api/_harvest_prefixes.py drifts from fresh lib.opal_naming output because an UNRELATED IRPT registry commit moved the registry hash. The only drifting content is the provenance stamp -- all four prefix constants are byte-identical -- and that file is lane BASE_EXEC, outside rm-7's <paths>, so this lane cannot regenerate it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S256",
      "19a22f2f51 (ancestor of HEAD): issuer restamp of lib/research/api/_harvest_prefixes.py from fresh lib.opal_naming output",
      "35038a7459 (ancestor of HEAD): rm-7 landed, row Z-S258 disarms Z-S253/S254/S256",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S258",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rm-7.the-deploy-leg.md last status complete"
    ],
    "remedy": "The owner regenerated _harvest_prefixes.py at 19a22f2f51, the build passed and rm-7 deployed; disarmed by Z-S258.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S262",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER, batch 1 of the R-78 sweep on this serial: fourteen rows naming 2.0.0_SA_COO~Z as disarm owner whose remedy landed in the world between 2026-09-13 and today and which have read ARMED ever since because nothing cited them (R-78). Each is resolved on its own evidence line below; nothing on any target row is edited (R-81 (iv)). Per R-81's interim discipline this row names ONLY the ids it resolves, listed in `notes` as full ids (R-81's `resolves` field is refused by the schema at HEAD, additionalProperties false, so the ids are carried where the R-78 heuristic reads them), and no other.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S262",
      "25152295cf (ancestor of HEAD): row Z-S262 filed",
      "cbeba32072 (ancestor of HEAD): row Z-S263 folds Z-S262's fourteen ids through adjudicates"
    ],
    "remedy": "No act owed: a disarm carrier that records fourteen resolved rows, each on its own evidence line.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S270",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S269's deliberately-unclaimed WHY is now MEASURED: the deployed Peers P/E columns read BEST_PE_RATIO, a FY1-FY3 FORECAST mnemonic, and the forecast mnemonics are absent from most served model blocks -- so the P/E gap is a FORECAST-COVERAGE gap in the DATA, not a stale artifact and not a rendering defect. AMGT_CORPUS's FWD-12 pull closes it for the peer members INSIDE the 89-key set and CANNOT close it for the ones outside, which on the observed rows is 3 of 5.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S270",
      "479eee52ff (ancestor of HEAD): CTO vacates the ruling; the Peers P/E is not BEST_PE_RATIO and the three members carry figures",
      "fa03858417 (ancestor of HEAD): round-40 L10 rules Z-S270 SUPERSEDED",
      "f574a21ac1 (ancestor of HEAD): row Z-S275 adjudicates Z-S270 and Z-S273",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S275"
    ],
    "remedy": "Superseded: the CTO vacated the three-valued P/E ruling (479eee52ff) and the round-40 L10 (fa03858417) ruled Z-S270 SUPERSEDED, folded by Z-S275.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S278",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "overlay.chatter and overlay.price are BARE NULLS on 89 of 89 served overlays, while description, feed and posture on the same payload each carry a status and reason on 89 of 89 -- a null that says nothing about why (defect named by 1.0.0_SA_CTO~Z, msg 25884, @74ed138afa).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S278",
      "e77106d93b (ancestor of HEAD): row Z-S278 filed",
      "lib/research/api/scoped_amgt.py:2918-2919 at HEAD: chatter and price are by_axis.get(...), None with no status or reason",
      "a88531512b (ancestor of HEAD, af-2): overlay axis reads carry absent_reason when not SERVED"
    ],
    "remedy": "Still bare nulls at HEAD: overlay chatter and price are by_axis.get() and serve None when absent; af-2 put absent_reason on axis_reads, but no ruling names that as this row's remedy.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S285",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The LIVE research library grew to 95 during round 43: 'AIA Group' was added after the cut and has no canonical identity (harvester_key security-a49e6fe67bebe3a9), so it has no page, no Model block and no export -- rr-3's served sweep over the live library held on it (0.7.0_AE_CloudOps~A).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S285",
      "64d3cad229 (ancestor of HEAD): row Z-S286 corrects Z-S285",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S286",
      "lib/research/identity/registrations.json:1696-1699 at HEAD: folder AIA Group, security_key 1299_HK_Equity"
    ],
    "remedy": "Corrected by Z-S286: AIA Group has a canonical identity (1299_HK_Equity) and a Model block.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S294",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round45/checks/tt-1.AC2.sh (the planted control 'THE VERDICT COUNTS A DROPPED ABSENCE') passes on ANY harness rc=1, so on a tree where the harness crashes (Z-S292) it reads 'YES on 2 of 2' with empty ABSENCES/EXPORT-COMPARE fields -- a control that passes on a blind instrument.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S294",
      "37a81870ac (ancestor of HEAD): uu-2 proof, AC2 2 of 2 controls fire",
      "65461f9916 (ancestor of HEAD): uu-2 drained, issuer re-ran",
      "ADJUDICATION_v56.md:104: Z-S294 GRADUATED on uu-2 AC2",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-uu-2.the-harness-loads-the-timeline-mount.md last status complete"
    ],
    "remedy": "uu-2 AC2 tightened the control to require missing=1 and EXPORT-COMPARE NOT OK on both exports; it fires by token 2 of 2.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer's read of AMGT_RESAPP-Z-W7-S3 (ARMED, disarm_owner this seat): the 16-of-48 AAPL US collapse in universe.json is REAL (re-measured 48 MEASURED / 33 distinct / one value on 16 folders), the ISSUANCE cut no unscoped pass over the identity layer's members, and the order is REOPENED with AC7 rather than left to round 2 -- four consumers hang off the root inside this round.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S3",
      "71b5b760db (ancestor of HEAD): row Z-S3 filed",
      "628b975b49 (ancestor of HEAD): s-12 shared-template-placeholder fix",
      "s-12 AC7 invocation at HEAD: MEASURED 32, distinct 32, shared 0",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root.md last status complete"
    ],
    "remedy": "The s-12 reopen this row records landed: AC7 added and universe.json regenerated with the template ticker read as UNRESOLVED.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S318",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "AC3 CANNOT PASS BY THE SPECIFIED ACT: ac_3_served.py --what bpng compares WHOLE served bodies before and after an act whose entire purpose is to MOVE THE READ PATH, and the body reports that path in its object_key / report_key / extract_key provenance fields. The data is unchanged; only the provenance strings moved.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S318",
      "f3f0e2167b (ancestor of HEAD): issuer accepts ac-3, row Z-S320 rules Z-S318",
      "e1e6603ee5 (ancestor of HEAD): ac-3 closed, 4 of 4 under AMENDMENT 2",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S320",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ac-3.the-slash-key-window.md last status complete"
    ],
    "remedy": "Ruled by Z-S320: AMENDMENT 2 re-scoped AC3 to rewrite read paths inside *_read only; 6 of 6 equal with a failing plant, ac-3 accepted.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S331",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served monthly chatter route (FWD-32, live since 08:20:58Z) names 63 of 95 covered rows; the other 32 serve the raw security key as display_name (e.g. 9433_JP_Equity), which DSGN prints as served on the bubble face.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S331",
      "74dc498d65 (ancestor of HEAD): ah-1 name fix as a direct act in the round-58 issuance",
      "7884f01689 (ancestor of HEAD): ah-2 accepted, name fix live, 0 of 95 raw keys",
      "ADJUDICATION_v70.md:39: Z-S331 GRADUATED, 0 of 95 on the deployed function",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ah-2.the-name-fix-redeploy.md last status complete"
    ],
    "remedy": "Round 58 shipped the name fix: 0 of 95 bubble rows serve the raw key on the deployed function.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-s-12's universe.json carries a measurement defect: 16 of its 48 MEASURED bloomberg_ticker values -- unrelated folders from AstraZeneca to Total Energies, including the CRO's own control folder 'SAP GY' -- all read the identical string 'AAPL US'.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W1-S1",
      "628b975b49 (ancestor of HEAD): s-12 whole-population pass downgrades a shared MEASURED ticker",
      "s-12 AC7 invocation at HEAD over deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json: MEASURED 32, distinct 32, shared 0",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S3",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root.md last status complete"
    ],
    "remedy": "s-12 was reopened with AC7 and regenerated; no two covered names share a MEASURED ticker.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W158-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "2 of 89 coverage-list identities resolve to a security_key carrying a literal '/' (folder 'BP PLC' -> 'BP/_LN_Equity', folder 'National Grid NG LN' -> 'NG/_LN_Equity'); a direct lambda:Invoke tolerated it (200 on all 5 routes) but that bypasses API Gateway's own path-segment matcher, so whether a real HTTP hit to /security/{key}/* resolves the same way is UNMEASURED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W158-S1",
      "f9245a8404 (ancestor of HEAD, an-6): per-security route accepts the encoded key (_route_security_key)",
      "lib/research/api/scoped_amgt.py:916 at HEAD: def _route_security_key",
      "3e7d3ab309 (ancestor of HEAD): round-64 real run on deployed KQSA62c3 reads c14 YES (encoded key resolves on overlay/thesis/peers/coverage)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-an-6.repairs.md last status complete"
    ],
    "remedy": "an-6 made the per-security route accept the encoded key (BP-SLASH-_LN_Equity) and resolve it to BP/_LN_Equity; read live on the deployed function.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-02T22:58Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W173-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The page carries NO data attribute for a figure's VALUE or for the identity line (sector, country, currency), so FWD-30's page reader keys FIGURES on line + year (HEADER mnemonic, FISCAL mnemonic + year) and the three identity mnemonics are dropped from the export side.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W173-S1",
      "60d2315e1f (ancestor of HEAD, yy-1): FWD-30's grader compares values, not only fact identities",
      "portal ae1be3c8 (AV-u-5): seven FWD-30 data attributes incl. Identity",
      "portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx:408-410 at HEAD: data-identity-sector/country/currency",
      "ADJUDICATION_v60.md:67: Z-W173-S1..S4 GRADUATED, value plants caught on both sides",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-yy-1.fwd30-grader-compares-values.md last status complete"
    ],
    "remedy": "yy-1 made the grader compare values and AV-u-5 added identity attributes; the CVO's value plants are caught on page and export.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W176-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT-yy-1: on 6 of 96 names the export states a header figure's unit as UNRESOLVED (\"does not discriminate absolute vs millions\") while the page prints a scaled magnitude (JPY 24.15T), so the value grade compares those figures' DIGITS but cannot compare their SCALE.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W176-S1",
      "0982a0767d (ancestor of HEAD): AMGT_CORPUS round 22 unit apply",
      "ADJUDICATION_v61.md:62: Z-W176-S1 GRADUATED, digits compared scale unchecked = 0, 0 differing on each of the six"
    ],
    "remedy": "AMGT_CORPUS's unit apply resolved the six units; the post-deploy sweep reads scale unchecked 0 (was 6).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-30T05:21Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W200-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "BA's Thesis sentence \"no research pack for this security\" is written by the PAGE: reasonInWords (portal/src/pages/SecurityAnalysis/reasonWords.ts:33) rewrites the served dossier text \"no class A report for this security\" to \"research pack\" for ResearchTeamPillars (tabs/ThesisTab.tsx:117-130); no served string says \"no research pack\".",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W200-S1",
      "71b7aef709 (ancestor of HEAD): row Z-S329 corrects Z-S328, disarm by the DSGN ruling",
      "a4d23b89bf (ancestor of HEAD): row Z-S328",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S329",
      "ADJUDICATION_v69.md:42: Z-W200-S1 GRADUATED, disarmed by Z-S328 as corrected by Z-S329"
    ],
    "remedy": "Disarmed by DSGN's issuer wording ruling via Z-S329: 'research pack' is the designed form of 'class A report', and AV-f-5 aligned the Exec sentence.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-01T07:55Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-s-4's cell text names which securities the reader should key items by only implicitly (via AMGT-s-12's identity layer); this worker reused AMGT-s-b4's own run_manifest.json ticker selection (BABA_US, BA_US, COST_US) rather than deriving an independent set.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W3-S3",
      "2f86c643b1 (ancestor of HEAD): s-4 L7 commit filing the row"
    ],
    "remedy": "No act owed: records a worker's grounded choice of a sibling cell's selection; the order closed on it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W40-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Bloomberg's own COMPANY_WEB_ADDRESS for CSL ('www.csl.com.au') resets the TCP connection on every GET this worker tried (default urllib, a curl-style UA, and fetch.py's SEC User-Agent, all timed out or RemoteDisconnected) while DNS resolves fine -- the ONE entity-tied seed step 4 has for CSL is unreachable from this box, so AC3 REFUSES rather than reaching investors.csl.com (the host the validation report itself names as the eventual winner).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W40-S1",
      "ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S330: GRADUATED, holder 1.0.0_SA_CTO~Z to rule",
      "git log --grep=CSL and --grep=C-S330: no ruling or resolving commit found"
    ],
    "remedy": "A ruling is still owed (Z-C-S330 holder 1.0.0_SA_CTO~Z): another egress path, a second sanctioned seed, or CSL UNRESOLVED by design; no commit records one.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "This order's own worker-face launch prompt dictated a proof-of-spec filename shorter than .tools/to-pipeline-gate.py's complete-flip discovery glob requires, so the correctly-produced instance was invisible to the gate until renamed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W7-S2",
      "e9d19be279 (ancestor of HEAD): check_complete_flip reads the instance the order's <proof_of_spec> block names",
      ".tools/to-pipeline-gate.py:961-965 at HEAD: self-test, a tag-named to_id instance is the candidate",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-an-6.repairs.md:73: issuance dictates the full-stem proof_of_spec.json name"
    ],
    "remedy": "Fixed both ways: the gate reads the instance the order's own proof_of_spec block names, and issuances now dictate the full-stem filename.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-W146-S1",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The nested portal repo carries no .tools/safe-commit.sh of its own, and this worker committed rn-1's PanelHeader.tsx fix (0f7db9bd) with plain `git commit` rather than through the parent's .tools/safe-commit.sh (whose gates -- risk-reflex, naming-gate, to-pipeline-gate -- were therefore not exercised on this commit), before noticing that AMGT_RESAPP~141's own proof_of_spec.json documents invoking `../.tools/safe-commit.sh` from inside portal/ for the same kind of commit.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-W146-S1",
      "9be94c9af4 (ancestor of HEAD): the worker commit that filed the row and moved the portal gitlink to 0f7db9bd",
      "portal 0f7db9bd is an ancestor of portal HEAD (merge-base --is-ancestor read)",
      "db7bea0ef0 (ancestor of HEAD): the rn-1 drain; round-39 packet a83660d367 lists W146-S1 INERT with no follow-on act",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rn-1.the-size-10-residue.md last <status> complete",
      "adjudications/ADJUDICATION_v49.md:124 row AMGT_RESAPP-Z-C-S417 adjudicates W146-S1 GRADUATED"
    ],
    "remedy": "No act owed: the portal commit 0f7db9bd carries correct content and was accepted as-is at the round-39 drain with no follow-on gate run, and the row was graduated by AMGT_RESAPP-Z-C-S417.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S192",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The rk-48 direct act wrote OUTSIDE what both signed chain E halves covered, and this seat's own COO half is the defect: (1) two NEW raw objects, raw/bloomberg/CSL_AU_Equity/20260921T162530Z/exec_officers.json and raw/bloomberg/6861_JP_Equity/20260921T162534Z/exec_officers.json, written by enrich's Bloomberg fallback re-pull -- the half's BLAST RADIUS named only the 3 dated management keys and its writer census counted writers OF those keys, never the act's own full write set; (2) ceo_public_profile CHANGED on all 3 keys (absence_class NOTHING_FOUND -> CANNOT_SAY, basis rewritten), where the half's expected outcome said 'ceo_public_profile unchanged' and 'nothing rewritten' for a NOT_SEARCHED name.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S192",
      "1ed2e24638 (ancestor of HEAD): CTO half of the rk-48 as-landed pair",
      "0b71e7f5ab (ancestor of HEAD): COO half RETAIN; reading NOT_SEARCHED 3/3 unchanged on pre-act and as-landed versions; Z-S192 keep-rationale withdrawn by its author; pair complete",
      "5f10ddf969 (ancestor of HEAD): round-18 analysis rules R19-A a re-projection of 3 conditional puts with no Bloomberg/raw writes (the Z-S192 class avoided)",
      "adjudications/ADJUDICATION_v17.md:113 names Z-S192"
    ],
    "remedy": "The rk-48 as-landed pair was completed RETAIN (CTO half 1ed2e24638, COO half 0b71e7f5ab) and the round-19 re-projection R19-A was ruled with no Bloomberg or raw writes, so the out-of-radius write class is closed for this act.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S215",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The PRINT route (/api/scoped/amgt/security/{key}/print) serves a 500 for ALL THREE VALIDATION NAMES -- CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity -- while BA and COST return 200. Cause, reproduced box-side on SITEZ code WITHOUT M3 (@a74268ba4d): lib/research/print/render_pack.py:264 `for fy in sorted(by_fy.keys())` raises TypeError ('<' not supported between int and str) because those names' model-block figures carry MIXED fiscal-year types -- historical years as str ('2016'..'2025') and forecast years as int (2026, 2027). NOT caused by M3 (rk-92): it reproduces on pre-M3 code; found by this seat's own 13-route census at M3's drain.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S215",
      "5357068676 (ancestor of HEAD): adds _fiscal_year_sort_key and str-keyed grouping in render_pack.py",
      "lib/research/print/render_pack.py:308 and :968 at HEAD: sorted(by_fy, key=_fiscal_year_sort_key)",
      "f16e253426 (ancestor of HEAD): redeploy of opal-amgt-scoped-api with the fix, deploy ledger opened and closed",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.md last <status> complete",
      "a57bd0a068: round-23 packet reports /print 200 on all 5 names"
    ],
    "remedy": "rk-94 sorts fiscal years on a normalised key and the adapter was redeployed, so the print route renders for all five model-block names.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-22T08:32Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S222",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "integrations/bloomberg/research/tests/test_fye_join.py has 3 FAILING tests at HEAD 96cc4dae9d, each reaching for an S3 bucket that no longer exists -- pre-existing, not caused by round 28.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S222",
      "54995eb25f (ancestor of HEAD): rk-115 test-rot cleanup, fixtures replace a retired-bucket S3 read (Z-S222)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-115.research-tests-cleanup.md last <status> complete",
      "21a2fcaf93 (ancestor of HEAD): ADJUDICATION_v33 reads Z-S222/S223/S224 REMEDIATED, files 11 passed (adjudications/ADJUDICATION_v33.md:45)"
    ],
    "remedy": "rk-115 replaced the retired-bucket S3 read in test_fye_join.py with fixtures, and the CVO re-measured the suite passing.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S228",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "There is NO name search: the page's search box passes the raw string into the URL as a security key and the server does an exact lookup, so 'Lenovo' can never match. The folder name 'Lenovo 992 HK' is not indexed; only its sha256 digest is.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S228",
      "portal ec65c5d6 (the HEAD gitlink) src/pages/SecurityAnalysis/components/LeadPanel.tsx:444-449: handleSearchSubmit passes searchInput.trim() straight to onSelectSecurity",
      "portal ec65c5d6 LeadPanel.tsx:491: placeholder \"Search any ticker\"",
      "git log --grep=Z-S228 returns only the filing (9ca923f2dc) and the round-30/31 analysis and issuance (28ab7ce9fd, f441a2ea76), none a fix",
      "adjudications/ADJUDICATION_v35.md:97 carries it to the addendum page contract and AMGT_CORPUS backlog; no landed remedy found"
    ],
    "remedy": "Still live: no name-resolution route or client-side filter exists at HEAD; the page search passes the raw string as a security key, and no commit or ruling records the name-search contract the row was carried to.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S240",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RUNS the discriminator AMGT_RESAPP-Z-S237 named and recorded as 'nobody has run it': NO portal commit is stranded. All 6 unreachable commits are deliberate trials or git stashes. S237's own hazard is NOT disarmed by this -- only its unmeasured sub-question is closed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S240",
      "row disposition GRADUATED at filing; disarm_owner text: NO ACT IS OWED"
    ],
    "remedy": "No act owed: the row reports a clean discriminator run (6 of 6 unreachable portal commits are trials or stashes) and asks for nothing; S237 is not disarmed by it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S250",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-W140-S2 (rm-1's AC3 invocation chained the body-control check and the page census with `&&`, so the census line could never print while any graded predicate failed -- the issuer's face defect, not the worker's): the issuer read the census in the worker's tree (FILES 31 TOTAL 0; the src diff against the base is the fixture HTML alone) and corroborated the scope pairs on the shared portal after the merge (stripContainers list 2 -> 3, identityAccents 1 -> 3, body over main). The order is terminal with AC1/AC2 PASS and AC3 satisfied on the issuer's read.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S250",
      "adjudications/ADJUDICATION_v48.md:23 Z-S250 terminal (carrier for W140-S2)",
      "adjudications/ADJUDICATION_v48.md:27 W140-S2 GRADUATED via Z-S250, verified at the artifact"
    ],
    "remedy": "No act owed: the row is the disarm carrier for AMGT_RESAPP-W140-S2 and records the issuer census read that satisfied rm-1 AC3.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S257",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM CARRIER for AMGT_RESAPP-W144-S1 (rm-5's row: PanelFooter.tsx imposes flex-shrink-0 on its content wrapper when leftContent is truthy, producing the same mid-word clip the face named without any truncate/nowrap class firing): rm-2, the row's named owner, dropped flex-shrink-0 and put min-w-0 on both the leftContent and content flex wrappers (portal 4aa49151, DEV 5e339ffd); clippedTextBlocks reads 0 on all six states in BOTH scopes after (rm-6's 24 of 24 at ffef75aa, the issuer's contract-check-after-rm-2/ at 5e339ffd). The mechanism the row named is gone from the component; the ancestor-aware detector it also exposed is carried as rm-6's C13 bullet 5.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S257",
      "portal ec65c5d6 (the HEAD gitlink) src/ui/components/panels/PanelFooter.tsx:104 and :106: min-w-0 on both wrappers, no flex-shrink-0",
      "adjudications/ADJUDICATION_v48.md:28 W144-S1 GRADUATED via Z-S257, confirmed in the six-state grid"
    ],
    "remedy": "No act owed: the row is the disarm carrier for AMGT_RESAPP-W144-S1; rm-2 dropped flex-shrink-0 and put min-w-0 on both PanelFooter wrappers.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S263",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ADJUDICATION CARRIER for the fourteen rows AMGT_RESAPP-Z-S262 resolved on evidence: Z-S262 carried the ids in prose because R-81's `resolves` was refused by the schema, and R-81a (@c69c4866ce) withdrew that field for the one the schema already has -- `adjudicates`, which gate (iii)'s second limb propagates as the named items' latest disposition. This row names the same fourteen through that field and adds no new finding; its evidence is Z-S262's, line for line.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S263",
      "row disposition GRADUATED at filing; adjudicates 14 rows, nothing on any target row edited"
    ],
    "remedy": "No act owed: the row is an adjudication carrier that re-files Z-S262 resolutions through the adjudicates field and adds no new finding.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S271",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The ro-1 x ro-3 drain-join's 17/17 EXPORT-COMPARE OK was measured on the LANDED FIXTURE; on the SERVED plane the same harness reads 16 of 17, because the export echoes the thesis payload's description_verdict_reason verbatim while the PAGE composes a longer reason that joins the model-block header-scalar clause to it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S271",
      "f3de463222 (ancestor of HEAD): drain-join adds the header description line to the rich export (row Z-S271)",
      "lib/research/print/render_pack.py:540 def _header_description_lines and :964 its call site citing Z-S271, at HEAD",
      "6f7e5ed7ca (ancestor of HEAD): ADJUDICATION_v50 GRADUATED, ro-7.AC2 reads absences 17 of 17, extras 0 (adjudications/ADJUDICATION_v50.md:23)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ro-7.the-served-acts.md last <status> complete"
    ],
    "remedy": "The ro-1 x ro-3 drain-join made the rich export write the header description line the page composes, and ro-7 AC2 then read absences 17 of 17 on the served plane.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S280",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the LIVE population the served export reads 89 of 94 OK after rq-2; the 5 NOT_OK are exactly the names added since the snapshot (AMD, GOOGL, LLY, PWR, UNH), none with a landed model block, and for each the print route REFUSES ('no printable pack') while the page shows 16 absence lines -- the export has no path for a name without a model block.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S280",
      "e835017d16 (ancestor of HEAD): rr-1 close, the five no-block names carry a Model block, AC1 5 of 5, AC2 5 of 5",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rr-1.the-five-no-block-names.md last <status> complete",
      "adjudications/ADJUDICATION_v52.md:125 adjudicates Z-S280 GRADUATED"
    ],
    "remedy": "rr-1 landed a Model block for each of the five no-block names, so the export has a block to render for them.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S288",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CORRECTING MY OWN ADJUDICATION_v54 @b7151b3093, same day: I wrote that 'no single served value was observed traversing both surfaces'. That is TOO STRONG. FWD-30's parity comparison reads the export AND the page across 95 names and 285 cases on the LIVE served plane, which IS that observation at population scale. My bound was accurate about the RENDER -- whose fixture predates the currency change -- and I generalised a bound on ONE instrument into a bound on the round's whole evidence set. The AC4 verdict does not move.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S288",
      "adjudications/ADJUDICATION_v55.md:46 Z-S288 GRADUATED (this seat's own correction)",
      "row notes: needs no act beyond the correction being on the record"
    ],
    "remedy": "No act owed: the row is the CVO correcting one over-broad sentence in ADJUDICATION_v54, and the correction is on the record.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S295",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "uu-4's closure diff HITS stop limbs 1 and 3 and the redeploy was REFUSED before the upload: both never-widen halves measured their delta from scoped_amgt.py @78f11f5a02, but the DEPLOYED artifact is OLDER than that commit (its scoped_amgt.py is f3de463222), so the apply would also have shipped AMGT_HARVST's timeline mount -- 2 files and 9 scoped_amgt constructs neither half names.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S295",
      "c524129644 (ancestor of HEAD): the first attempt refused at the closure diff before any upload",
      "658475977c and e21c04c433 (ancestors of HEAD): AMENDMENTS 1 and 2, one combined act with HVST-a-2",
      "f92bc63665 (ancestor of HEAD): CTO re-sign",
      "0d54b880cf (ancestor of HEAD): the combined act LANDED, 5 of 5 criteria PASS, entry CLOSED",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-uu-4.the-redeploy.md last <status> complete (flip 474516b751)",
      "4be12a2f1a: ADJUDICATION_v56 GRADUATED Z-S295 (adjudications/ADJUDICATION_v56.md:27)"
    ],
    "remedy": "The halves were re-signed to name the AMGT_HARVST timeline mount and uu-4 landed inside one combined scoped-API act with HVST-a-2, so the apply shipped only a delta both pairs cover.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-29T02:17Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S303",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "ww-1 AC2 exits 1 on ONE arm only: 1 of 96 research-library folders, 'Hitachi 6501 JP', resolves to a harvester_key but to NO security_key, so AC2 counts it a read failure and its 'failed 0' clause cannot be met. The failure is produced ENTIRELY IN THE LOCAL HARNESS before any Lambda call (vv-4.AC3.py:39-40 invokes the deployed route only `if key`), so neither the ww-1 artifact nor its two grants can cause it or cure it. Every substantive AC2 arm passes at full strength: formula as ruled 70 of 70, team_cases as the dossier holds them 95 of 95 names, 102 cases SERVED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S303",
      "d2c6b4d354 (ancestor of HEAD): AMENDMENT 1 to ww-1 AC2",
      "4a5eeb4458 (ancestor of HEAD): AC2 RULED MET, leg V1 and the entry CLOSED",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ww-1.the-redeploy-on-the-canonical-prefix.md last <status> complete",
      "33ed750433: ADJUDICATION_v58 GRADUATED Z-S303 (adjudications/ADJUDICATION_v58.md:53)"
    ],
    "remedy": "The issuer amended ww-1 AC2 so the one never-invoked no-identity arm is not a rollback trigger, and AC2 was ruled met with the NEVER-2 entry closed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S319",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "build-and-upload-scoped-amgt.sh's upload leg CORRUPTS the artifact's content-sha256 metadata whenever the base64 sha begins with a forward slash: MSYS path conversion rewrites the --metadata argument to the Git installation root plus the rest, and modules/yang-lambda reads that metadata AS source_code_hash.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S319",
      "71f1cafcab (ancestor of HEAD): ad-3 drain, upload_verified.sh sourced by all four build scripts",
      "infra/aws/terraform/harvest/upload_verified.sh:16 MSYS_NO_PATHCONV=1 on the cp; :22-25 read-back exits 3 on a content-sha256 or length mismatch, at HEAD",
      "infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh:736, build-and-upload.sh:29, build-and-upload-print-deps-layer.sh:73, build-and-upload-chatter-axis.sh:34 source upload_verified.sh at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ad-3.one-verified-upload.md last <status> complete",
      "d1743ceccc: ADJUDICATION_v66 Z-S319 GRADUATED (disarmed) (adjudications/ADJUDICATION_v66.md:54)"
    ],
    "remedy": "ad-3 added one verified upload helper with no path conversion on the metadata and a read-back that refuses a mismatch, sourced by all four harvest build scripts.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-30T18:30Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S332",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ai-2's CTO condition 3 names 'a 200 on /security/<key>/overlay' as the proof that a price bar OPENS its security -- but a FABRICATED key (ZZZZ_XX_Equity) also returns 200, so the status code cannot tell a covered key from an impossible one. The sound discriminator is a field the COO half already names: identity_status (MEASURED vs UNRESOLVED).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S332",
      "10b667f446 (ancestor of HEAD): am-5, an unknown key answers 404",
      "eb6cfa6a3e (ancestor of HEAD): the am-5 drain",
      "lib/research/api/scoped_amgt.py:5763-5782 at HEAD: identity UNRESOLVED and not a covered key raises AdapterError 404 (comment cites Z-S332)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-am-5.round-60-carried-items.md last <status> complete"
    ],
    "remedy": "am-5 made the per-security arm answer 404 for a key that is not in the crosswalk, not a landed block and not a covered name, so a status code now discriminates.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "This worktree's .gitmodules is EMPTY, so the portal/ gitlink (pinned at 5907cbca98eb091124e38a32debefa355c1d4376) cannot be initialized here at all; the F10 precedent DESIGN_SPEC.md this cell's task text names as READ material was read instead from the shared main workspace checkout, which itself carries a DIFFERENT portal commit (30ca034bbaa4b9d2864d3acce826e3c2fa59be0a) that also does not contain the pinned commit.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W1-S4",
      "3730474e77:.gitmodules is the empty blob e69de29b (the condition the row measured)",
      "69288c8ca0 (ancestor of HEAD): .gitmodules maps portal and opal_ai",
      ".gitmodules:5-7 at HEAD: [submodule \"portal\"] path = portal, url set"
    ],
    "remedy": "The root .gitmodules, empty at the worker base 3730474e77, now maps the portal submodule, so a worktree can initialise the pinned portal gitlink.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W159-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AC1 cannot reach 89 of 89 OK: 25 names' remaining FIGURES-extra is the exportCompare harness's OWN pageFigures() regex failing to parse a <td data-model-cell> that carries a nested CheckFaceBadge <span> for any non-PASS verdict, so a genuinely page-shown figure reads absent to the instrument -- not a render_pack.py defect, and the harness is outside this cell's <paths>.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W159-S1",
      "f50bd03775 (ancestor of HEAD): rq-1 amendment 1 grants exportCompare.harness.cjs",
      "86e0683292 (ancestor of HEAD): 89 of 89 OK, the instrument fixed in the instrument (portal gitlink moved)",
      "portal ec65c5d6 (the HEAD gitlink) src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs:260: td regex <td([^>]*)>([\\s\\S]*?)</td> admits nested tags",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rq-1.the-export-says-absent-the-way-the-page-does.md last <status> complete",
      "adjudications/ADJUDICATION_v52.md:23 Z-W159-S1 GRADUATED, closed by amendment 1"
    ],
    "remedy": "rq-1 amendment 1 granted the harness and the worker fixed pageFigures() to read every td including one with a nested badge span, and AC1 reached 89 of 89 OK.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-25T17:12Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W173-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three absences state their served REASON only in visible words (peers absent column, description absence, posture no-call), so ABSENCES keys them on identity alone: (PEERS_COLUMN, column), (DESCRIPTION, ABSENT), (POSTURE_NO_CALL).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W173-S2",
      "portal ae1be3c8 (ancestor of the HEAD gitlink ec65c5d6): AV-u-5 seven FWD-30 data attributes on Header, Peers, Posture",
      "portal ec65c5d6 src/pages/SecurityAnalysis/tabs/PeersTab.tsx:231 data-absent-column-reason",
      "portal ec65c5d6 src/pages/SecurityAnalysis/components/HeaderBrief.tsx:66 data-header-description-reason",
      "portal ec65c5d6 src/pages/SecurityAnalysis/tabs/PostureTab.tsx:411-413 data-posture-verdict with data-posture-reason"
    ],
    "remedy": "DSGN AV-u-5 put the served reason on a data attribute for all three absences, so each key can carry its reason.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W191-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT-ac-2's premise fails: the 8 ASML_NA_Equity sentences a rebuild drops (company_description 5, investment_thesis 1, risks 2) were served under the pre-HOLD vacuous rule with quoted_spans [] and no verbatim run in the excerpt, so they genuinely fail today's gate -- a ruling, not a build; nothing was changed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W191-S1",
      "cd70547173 (ancestor of HEAD): ac-2 AMENDMENT 1 per CTO msg 27185, AC1 re-scoped to span-carrying stored sentences",
      "f336e07550 (ancestor of HEAD): AC1 PASS under AMENDMENT 1, flip complete",
      "8b56a93755 (ancestor of HEAD): drain records Z-W191-S1 resolved by CTO msg 27185 / Z-S316",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ac-2.regeneration-keeps-served-sentences.md last <status> complete",
      "adjudications/ADJUDICATION_v63.md:57 Z-W191-S1 GRADUATED"
    ],
    "remedy": "The CTO ruled the HOLD working as designed (msg 27185, row Z-S316) and the issuer re-scoped ac-2 AC1 to span-carrying stored sentences, which pass 2 of 2.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-30T14:09Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W208-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PAGE-SIDE (DSGN lane, not edited): portal LeadPanel.tsx holds three universes in one component -- the price ranking (94 names), the monthly collected chatter (95 covered names) and the chatter ranking (1 name, read only to join starred names); the one served universe it should read is the covered universe, which /lead-panel/timeseries/collected/chatter already serves. No served route serves more than one universe now.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W208-S1",
      "org/missions/D13/DSGN/DSGN_AMGTV1/task-orders/DSGN_AMGTV1.TO-AV-zh-1.one-served-universe-per-face.md last <status> complete",
      "0090fba789 (ancestor of HEAD): AV-zh-1 complete",
      "4aed6b5ae8 (ancestor of HEAD): AV-zh-1 drain, each Lead Panel face reads one served universe",
      "a427b2ef70: DSGN round 30 issuance names Z-W208-S1"
    ],
    "remedy": "DSGN_AMGTV1 AV-zh-1 collapsed each Lead Panel face to one served universe (the chatter-ranking read dropped, the starred join taken from the collected rows).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The repo's own top-level .gitignore line 47 ('lib/', Python-boilerplate) blankets the ENTIRE lib/ tree, including the already-tracked lib/research/checkface/ this cell writes to -- a brand-new file there (markers.py) is invisible to plain `git status`/`git add` and would be silently dropped unless force-added.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W3-S5",
      "b750649397 (ancestor of HEAD): fix(.gitignore) drops the stock blanket lib/",
      ".gitignore:47-48 at HEAD: comment records the blanket lib/ removed 2026-09-11; no bare lib/ line remains (lib64/ at :51 only)"
    ],
    "remedy": "The blanket lib/ ignore was removed from the root .gitignore, so a new file under lib/research/ is visible to plain git status and git add.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T09:28Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W42-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Live PASS 1 (opus-5) did not follow the language rule as originally worded/positioned: it wrote finding SENTENCES in ENGLISH with only a handful of quoted TERMS left in Japanese (0 of 66 served items in the filing's own script), even though the prompt explicitly said 'write every finding in the filing's own language.' Fixed by moving the rule to the FIRST bullet of RULES and rewording it to name the failure mode directly.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W42-S4",
      "2e388452dd (ancestor of HEAD): language rule moved first and reworded",
      "lib/research/filings/analyze.py:227 CRITICAL language bullet and :80 PROMPT_VERSION rj6-two-pass/3, at HEAD",
      "row evidence: VERBATIM-CHARS rose from 0 of 66 to 57 of 67 on the live re-run"
    ],
    "remedy": "The language rule moved to the first RULES bullet, marked CRITICAL, with PROMPT_VERSION bumped; zh/ko re-verification stays with any future cell that runs those languages.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W85-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "lib/opal_data_harvest/ has no lib/__init__.py, so a test file UNDER that package (relative import) and any OTHER caller using the absolute `lib.opal_data_harvest.X` path load the SAME source as TWO SEPARATE module objects -- a monkeypatch on one is invisible to code reached through the other.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W85-S1",
      "739eb5f288 (ancestor of HEAD): round-21 analysis, W85-S1 disarmed for this project by a cutting rule",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round21.md:29-33 at HEAD: the cutting rule text",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-88.bright-data-serp-writer.md:144 and rk-94..rk-110 orders carry the qualified-import rule and identity arm",
      "lib/__init__.py absent at HEAD (git ls-files empty); pytest.ini sets no import mode"
    ],
    "remedy": "The CTO ruled a cutting rule binding from round 22 (qualified lib.<pkg>.<mod> imports plus an identity arm in every order), one of the two remedies ADJUDICATION_v23 named; lib/__init__.py is still absent repo-wide.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-21T23:29Z"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
