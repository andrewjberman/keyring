# AMGT_RESAPP -- L5 decomposition (COO) -- v1.8 (s.22 = round 14, 31 cells; s.21 = round 13; s.20 = round 12, amended s.20h + s.20i; s.18 = round 10; the header read v0.6 through v1.0 and is corrected here)

**Seat:** `2.0.0_SA_COO~ZZZ`, spawned by Andrew 2026-09-10 ~17:4xZ at the `1.0.0_SA_CTO~Z` terminal for this
project (seating brief msg 21003; `project.json` `seats.coo`). **Directive:** D5 Alternative Research.
**Fabric:** site-z. **Consumes:** PRD v0.3 section 4 SURFACE MANIFEST at
`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @f68818832b -- v0.3. The first landing
@c0b5636ea9 carried no fenced PRD_HEADER block, a numbered ENDPOINT heading the gate's whole-line match
cannot see, and ZERO outcome cards; measured by importing `.tools/to-pipeline-gate.py` and running
`_prd_conformance`, `_top_section` and `FWD_DEF_RE` on the file's bytes with the sibling PRD that passed L6
the same day as the positive control; handed back (msg 21037) and fixed by L4 within the hour. **At
@8019bf6433 the same three functions read True / 14 defined / 1 block / 0 complaints**, and at v0.3 @f68818832b
they read the same (header `prd_version: v0.3`, `status: RATIFIED`, 14 outcomes) on the committed blob.

**v0.2 OF THIS DECOMPOSITION IS AN L5 RE-ENTRY, NOT A RECUT.** L4 bumped the PRD to v0.3 (s.3a rewritten on
`4.0.0_SA_CRO~Z`'s SA auth investigation @b1656bbebc) and Andrew released the SA hold at this terminal
(@d09e26e1b1). MEASURED at this edit: no outcome moved (`FWD-1`..`FWD-14`), no manifest row moved (15), no
cell was added or removed (16). **What moved: the `AMGT-s-b4` row's act, state and bounds; section 5's
rounds (nine chains, all open); section 9's holds. Nothing else.** Rule 24 (iv) in section 2 says exactly
that release would move that cell and nothing else; this edit is the measurement of it.

**The rectangle is RECEIVED, not derived here.** L4 wrote the manifest; L5 mirrors it, re-grounds what it
can at its own vintage, adds the dependency edges, the placement axis and the battery. **This file does not
re-open the manifest's MECE.** It makes ONE structural cut of its own, on a sovereign word: manifest row S4
carries TWO cells, because Andrew held the task orders specific to Seeking Alpha backend design and said
*"proceed otherwise"* -- and the only way to hold exactly that is to give the SA backend its own cell
(section 1, section 9).

⛔ **ANDREW'S TWO WORDS THIS HOUR, BOTH RECORDED VERBATIM AND BOTH BINDING ON THIS FILE:**
- `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260910_184xZ_COOZZZ_SEEKING_ALPHA_IN_THE_TOS_VIRTUAL_ANALYST_REPORT_MODAL_AND_REST_API_VS_SCRAPING.md` @ee0eacab07 -- Seeking Alpha belongs in the task orders; the `virtual_analyst_report` modal; explore the authenticated REST API versus scraping; his credential is in AWS Secrets Manager. **Folded into the PRD at s.3a as `C-SA-NAMED-SOURCE`, `C-SA-ROUTE-COMPARISON`, `C-SA-PAYWALL-PRECONDITION-PARTLY-CLOSED` and `C-SA-VENDOR-WORD` @8019bf6433.**
- `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260910_185xZ_COOZZZ_HOLD_ON_SEEKING_ALPHA_BACKEND_TASK_ORDERS_PROCEED_OTHERWISE.md` @8c609decf7 -- *"Hold on the Task orders specific to Seeking Alpha backend design, i may provide updated information to this end before you cut those but proceed otherwise."* **RELEASED** by the third word below.
- `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260910_194xZ_COOZZZ_SEEKING_ALPHA_CASE_FIGURED_OUT_HOLD_RELEASED_AUTH_INVESTIGATION_IS_THE_REFERENCE_NO_PRD_RECUT.md` @d09e26e1b1 -- *"We have figured out the Seeking Alpha case"* / *"I think you can just review the brief here: ...AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md"* / *"Shouldnt need to recut the details on the PRD, it is right here, this is just what should be referenced for any TOs associated with SA news procural for this project."* The hold's release condition is met; the investigation @b1656bbebc is THE REFERENCE for every SA-procurement order.

---

## 1. The rectangle -- sixteen cells over fifteen manifest rows, `AMGT-s-<n>` mirroring `S<n>`

**INVARIANT THIS FILE COMMITS TO:** *every cell mirrors a manifest row, and every manifest row has at least
one cell.* ⛔ **IT IS NOT A BIJECTION AND IS NOT DECLARED AS ONE.** MEASURED AT THIS EDIT: 16 cells over 15
rows; every cell mirrors a row; 14 rows carry exactly one cell and **row S4 carries two** (`AMGT-s-4` and
`AMGT-s-b4`, the split section 9 explains). A later recut giving another row a second cell breaks nothing
here.

**CELL-ID CONFORMANCE, MEASURED not assumed** (`org/standards/DECOMP_CELL_ID_CONVENTION.md`): every id is
SHAPE 1 -- a project prefix, an axis of one lowercase letter, an optional letter, digits -- the form the
standard says to prefer for new decomps, so **no new regex branch is requested and neither of the standard's
two controls is owed.** Verified against the enforcer object itself (`.tools/proof-of-spec-check.py`
`CELL_ID_RE`, loaded and applied to these ids, not eyeballed): **16 of 16 match; 5 of 6 malformed controls
refused** (uppercase axis, lowercase prefix, underscores, a missing number, a four-letter axis). The one
control admitted -- a five-letter prefix -- is admitted by the regex's own unbounded prefix class and is not
an id this decomp mints. The run and its output are in this file's commit message.

⛔ **NO EXEMPLAR CELL ID FROM THE STANDARD OR FROM ANY SIBLING DECOMPOSITION IS WRITTEN IN THIS FILE, AND THAT
IS DELIBERATE.** The L6 coverage limb indexes every cell-shaped token in this document as a cell of this
decomposition; a sibling on this fabric quoted three exemplars and they became PHANTOM CELLS that refused
its own issuance. Siblings are cited here by PATH only.

**CELL STATUS VOCABULARY** -- ADOPTED, not authored: the closed set the sibling decomposition at
`org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md` @9e72041da5
section 2a records under Rule 24, restated at section 2a below because adopting a schema binds Rule 24 as
authoring one does:
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`.
- `NOT-EVALUATED` -- this decomp did not reach the cell. **No cell carries it at this cut**, and that is a
  MEASUREMENT (16 of 16 evaluated), not a vocabulary lacking the value.
- `OPEN` cuttable now · `IN-FLIGHT` a worker holds it · `HELD` blocked on a named owner · `COMPLETE` served
  and proven · `CLOSED` retired without being served, with its pointer.

| cell | row | outcome | act (the engine, and what binds it) | state | round | touches |
|---|---|---|---|---|---|---|
| `AMGT-s-1` | S1 | FWD-1 | THE MODEL BLOCK -- ~20 line items x 10 fiscal years + ~25 header scalars for a COVERED name, pulled from Bloomberg DAPI on this box by a BOX-SIDE job, raw vendor bytes landing in the version store BEFORE any derivation. Every mapped field carries a MEASURED unit and sign, re-measured per field on at least two securities beyond the one the brief mapped (a US name; an ADR). Fiscal year is the join key. Bloomberg's basis stated beside every number. | OPEN | 1 | DAPI 127.0.0.1:8194 -> S3 |
| `AMGT-s-2` | S2 | FWD-2 | THE ON-DEMAND PULL -- a ticker outside coverage, from the page. **FIRST deliverable: THE SEAM DESIGN** -- how a browser request served from AWS reaches a loopback-only DAPI on this device (section 1b: the estate has no precedent). **SECOND: the build on the approved design**, the page stating it is fetching now. Touches NEW securities, the binding cost axis. | OPEN (design) | 2 | API GW -> this box -> S3 |
| `AMGT-s-3` | S3 | FWD-3 | THE PROVENANCE FACE -- source, basis and vintage beside every figure, WIRED from the raw and derived records `AMGT-s-1` persists; never composed from a second read. | OPEN | 2 | portal |
| `AMGT-s-4` | S4 | FWD-4 | THE COVERAGE READER, NON-SA SOURCES -- the company's investor-relations channel located by SERP (the real domain is in `display_link`; `link` is an obfuscated redirect -- F11, re-measured first) and trusted publications per the allowlist `AMGT-s-15` owns; ranked by recency and frequency; each item admitted by the news rule `AMGT-s-11` states, PLUS one unscoped pass over the whole population per name. | OPEN | 2 | SERP zone -> S3 |
| `AMGT-s-b4` | S4 | FWD-4 | THE SEEKING ALPHA BACKEND -- the ETL that procures SA content for a ticker by the MEASURED route (`C-SA-NAMED-SOURCE` as amended at v0.3; the reference @b1656bbebc): `GET /api/v3/symbols/{ticker}` -> `sa_id`; `GET /api/v3/virtual_analysts/{sa_id}` (the report as JSON, carrying `createdAt` and `previousReportDate`); `GET /api/v3/symbols/{t}/analysis|news` -> `GET /api/v3/articles/{id}`. NO HTML parsing on the path. Rides the parked session through the residential proxy with the full browser-minted cookie jar AND a per-ticker `Referer` (`C-SA-SESSION-SHAPE`); a 200 with a 2-byte body is a FAILURE, a small-challenge 403 is a RE-HARVEST signal and never an auth failure; no POST through the proxy (`C-SA-NO-POST-THROUGH-PROXY`); the credential and the session are LOCATED in Secrets Manager at run time and no name is hardcoded. Raw JSON lands in the version store before any derivation. Tested ONCE on a stated small ticker set inside the exploration word; NOT scheduled and NOT served in production (`C-SA-VENDOR-WORD`); the comparison is DISCHARGED and not re-run (`C-SA-ROUTE-COMPARISON`); the five unmeasured limits are carried, not assumed (`C-SA-UNMEASURED`), and the terms question is Andrew's. The seven-Lambda archive estate is not this fetch path. | OPEN (released @d09e26e1b1) | 2 | SA API via residential proxy -> S3 |
| `AMGT-s-5` | S5 | FWD-5 | THE PRINT RENDERER -- Adam's artifact. **FIRST: THE DESIGN SPEC** for the Security Analysis page, in the form the F10 precedent gated (*"no .tsx files written until approved"*). **SECOND, HELD on that approval: the PDF-in-modal render** reproducing the template's four blocks (F1) so the printed output replaces the circulated document. | OPEN (spec); the .tsx phase HELD on approval | 3 | portal |
| `AMGT-s-6` | S6 | FWD-6 | THE VERSION STORE -- `opal-data-research`, MEASURED ABSENT at two vintages (section 1a), created by Terraform through `safe-apply` under a change-management entry opened BEFORE the act; snapshots ACCUMULATE, never overwrite; raw before derived. | OPEN | 1 | Terraform -> AWS |
| `AMGT-s-7` | S7 | FWD-7 | THE COVERAGE-FRESHNESS VIEW -- every covered name with its last-refreshed date, in one place a person OPENS. A view, never a monitor, alarm or scheduled checker. | OPEN | 2 | portal |
| `AMGT-s-8` | S8 | FWD-8 | THE PEER SET -- comparable to THIS company, or absent with a stated reason. RE-MEASURES F6 FIRST (48 of 54 carrying another company's set) on the SharePoint corpus through the Opal gateway, read-only; then a per-name rule PLUS one unscoped pass over the population -- the pass that would have caught a telecom set on 48 non-telecoms. | OPEN | 2 | SharePoint (read) -> S3 |
| `AMGT-s-9` | S9 | FWD-9 | THE DRAFTING FACE -- generated prose visibly MARKED, each sentence beside the evidence it was drawn from; the verbatim gate (an exact normalised substring of the fetched text, else rejected and regenerated) is machine-checked, never trusted. Proceeds on `AMGT-s-1` figures and `AMGT-s-4` evidence; SA evidence joins when `AMGT-s-b4` lands. | OPEN | 3 | portal + this box |
| `AMGT-s-10` | S10 | FWD-10 | THE CHECK FACE -- pass, fail or provisional per figure, on the page. A failure renders as a MARKED VALUE, never a blank, a zero or a row that vanished. | OPEN | 2 | portal |
| `AMGT-s-11` | S11 | FWD-10, FWD-3 | THE QUALIFICATION RULES -- one per class (a figure, a peer, an identity, a news or social item, a source, a generated sentence), each NAMING the input that makes it refuse and EXERCISING that input. **Each rule's cell PRODUCES the distribution its threshold is drawn from and states the threshold in its own deliverable** -- no threshold exists anywhere upstream and none is invented here. | OPEN | 1 | this box -> S3 |
| `AMGT-s-12` | S12 | FWD-13 | THE IDENTITY LAYER -- THE ROOT. Bloomberg ticker, SA symbol, IR domain, social account: four keys, the social one with no shared identifier. Two sources are never shown together until resolved; where they cannot be, the page SAYS SO. F6 re-measured as the failure instance. Resolves the SA-symbol KEY and binds nothing about the SA fetch path. | OPEN | 1 | this box -> S3 |
| `AMGT-s-13` | S13 | FWD-11 | THE SOCIAL FEED -- **MEASURE, THEN BUILD.** The first act EXERCISES the Bright Data datasets surface that nobody has: trigger one post-level dataset, observe a record, its cost, field schema, latency, freshness, and whether it can be queried by cashtag at all; the criterion is that MEASUREMENT. A feed follows only if the measurement admits one, under the social-item rule from `AMGT-s-11`, with the cashtag-native absence (F13) stated on the feed's own source line. | OPEN (measure) | 2 | Bright Data datasets API |
| `AMGT-s-14` | S14 | FWD-12 | THE INPUT LEDGER -- per input class: source, last run, outcome, and RE-RUN ALONE while the others stay. Every stage persists its own output. A single refresh under one timestamp is a violation. | OPEN | 2 | portal + S3 |
| `AMGT-s-15` | S15 | FWD-14 | THE LIST REGISTER -- the publisher allowlist and the company-to-social-account map, each with a NAMED OWNER and a rot signal a person reads. Not an alarm. | OPEN | 2 | this box -> S3 |

---

### 1a. Re-groundings performed at L5, at this lane's own vintage

PRD section 7: *"every F-numbered measurement is the CRO's, re-derived by nobody. This PRD carries them as
CITED, not as CONFIRMED, and a cell relying on one re-measures it first."* This lane re-grounded what a
decomposition can re-ground without spending a vendor call or doing a cell's work. **One premise held. One
substrate is DOWN at this vintage. Everything else stays CITED and is a cell's to re-measure.**

**`opal-data-research` (the `AMGT-s-6` premise) -- HOLDS, at a second vintage and a second instrument.**
```
  comp-find 'opal-data-research' --corpus aws
  VINTAGE      graph built 2026-09-10 12:24:50 UTC (stitch 03:01:17Z; manifest aebbd9cef8c4)
  DENOMINATOR  0 hit(s) across 2382 aws node(s) scanned  (S3 keys ARE modelled: S3Key band present elsewhere)
```
PART V measured it absent on the LIVE plane 13:30-16:00Z (a different instrument, a later vintage). Two
instruments, two vintages, one answer. `AMGT-s-6` creates it.

**The Seeking Alpha substrate (`AMGT-s-b4`) -- EXISTS, IS NOT THE FETCH PATH, AND THE FETCH PATH IS NOW MEASURED.**
At v0.2: `4.0.0_SA_CRO~Z` measured the route under Andrew's word (@b1656bbebc): authenticated REST with a browser-
harvested session parked in Secrets Manager (created 19:29Z, 65 cookies) returns 200 on every ticker and article tried
through the residential proxy; the modal page cannot work (JS-rendered); the cookieless unlocker cannot work. That
document is THE REFERENCE for the cell (Andrew's third word) and this lane does not restate its measurements here.
```
  comp-find 'seeking-alpha' --corpus aws   34 hit(s) / 2382 nodes, same vintage
  LAMBDA=7 (all LIVE-no-DECLARED)  EVENT_RULE=2  IAM_ROLE=1 (LIVE-no-DECLARED)  SECRET=1  DYNAMODB_TABLE=1
  EC2_INSTANCE=2  LOG_GROUP=11  S3Key=5  IAM_POLICY=2  INSTANCE_PROFILE=1  SECURITY_GROUP=1
```
The seven Lambdas and their two daily rules are the ARCHIVE PRODUCER brief PART II rules out as this
project's fetch path; the one SECRET is the credential Andrew named. The held cell inherits both facts.

⛔ **THE BLOOMBERG TERMINAL IS SIGNED OUT AT THIS VINTAGE (`AMGT-s-1`, `AMGT-s-2`).** `bloomberg_health`
at ~18:5xZ: `ok: false -- could not start blpapi session to 127.0.0.1:8194 (is the Terminal running +
logged in?)`. Brief PART VI measured `ok: true` at 13:30-16:00Z. **This is the sign-in playbook's most
common case (`integrations/bloomberg/READ_HERE.md` section 1), it is `0.0.3_BG_BBGTerminal`'s to repair
(two-phase, a 2-attempt budget, credentials only through the exec wrapper), and it is NOT a hold on L5** --
the decomposition calls nothing. It is a PRE-SPAWN CHECK at L6 for the `AMGT-s-1` slot (section 9), and a
worker's first act on that cell is `bloomberg_health`; on `ok: false` the worker does not sign in.
⚠ Health is necessary-not-sufficient (README section 3): `ok: true` is confirmed by a real reference read.

**The portal cache-key population (`AMGT-s-3`, `-5`, `-7`, `-9`, `-10`, `-14`).** `comp-cache map`:
118 of 118 `useQuery` call-sites captured across 415 of 415 source files -> **94 distinct keys in 44
files**; `collisions`: 17 shared keys, **0 type mismatches**. That is the population a new page's keys are
namespaced away from, re-checked by `comp-cache collisions` at each portal cell's commit.

**The request path (`AMGT-s-2`).** `comp-routes behaviors`: 28 CloudFront behaviors on the DESIRED plane;
every origin is S3 or API Gateway; the page itself rides the `/*` SPA default; the F10 precedent has its own
`/api/scoped/security-scanner/*` behavior. **No behavior reaches a desktop origin.** Section 1b.

**CITED, NOT RE-DERIVED HERE, and the cell that re-measures each first:** F4's units (`AMGT-s-1`; measured on
ONE security); F6's 48 of 54 (`AMGT-s-8`, `AMGT-s-12`; the SharePoint read is a cell's act); F12/F13
(`AMGT-s-13`; every Bright Data call is a vendor call this lane may not spend); F11 (`AMGT-s-4`).

---

### 1b. The seam is `AMGT-s-2`'s, not `AMGT-s-1`'s -- a plane note

PRD section 5 carries *"The desktop/cloud seam is crossed somehow"* as a precondition. Measured here:
`integrations/bloomberg/README.md` section 1 -- *"There is exactly one physical pipe, and it is loopback ...
DAPI binds 127.0.0.1 and nothing remote can reach it -- no VPN, peering, or security-group change. Something
running ON the Terminal box must make the blpapi call."* Section 5 lists **"Remote reach"** under what the
integration does NOT cover. The route inventory confirms no desktop origin exists.

⭐ **SO THE TWO BLOOMBERG CELLS SIT ON DIFFERENT SIDES OF THE SEAM, AND ONLY ONE NEEDS IT CROSSED.** A COVERED
name (`AMGT-s-1`) is served by the pattern the daily dashboard pull already runs in production: a job ON THE
BOX pulls, then publishes to S3, and the page reads the snapshot. Nothing crosses the seam inbound. An
UNCOVERED name typed into the page (`AMGT-s-2`) is a request that ORIGINATES in a browser served from AWS and
must reach the box -- that is the seam, and the estate has no precedent for it. **Hence `AMGT-s-2`'s first
deliverable is the design, not the build**, and `AMGT-s-1` is cut round 1 without waiting on it.

---

## 2. Four-postulate record (rule 24) for what this file ADOPTS and ADDS

Rule 24 binds any schema an agent authors **or ADOPTS**. This file adopts the PRD's manifest axes and the
sibling's cell-status vocabulary (2a); it adds the round axis (section 5) and the S4 split.

- **(i) MECE over a DECLARED domain.** Domain = the fourteen ratified outcomes `FWD-1`..`FWD-14`, reached
  through the fifteen manifest rows. Hunted in BOTH directions this file can hunt: **rows serving no cell:
  0 of 15; outcomes reached by no row: 0 of 14** (`FWD-10` is reached by S10 and S11, `FWD-3` by S3 and
  S11 -- the manifest's deliberate two-rows-one-outcome cases). **The S4 split is MECE over S4's own
  sources:** Seeking Alpha versus everything else, the boundary Andrew's hold draws, with no source in both
  cells and none in neither (IR channel, trusted publications -> `AMGT-s-4`; SA -> `AMGT-s-b4`).
- **(ii) SAME GRAIN.** Every cell is one ENGINE, the manifest's row grain. `AMGT-s-4` and `AMGT-s-b4` are two
  engines -- a reader and a fetch backend -- at the same grain as each other, not one nested in the other.
  `AMGT-s-2` and `AMGT-s-5` each carry two DELIVERABLES (a design, then a build) inside one engine; that is
  sequencing within a cell, not a second grain, and L6 cuts them as two criteria, never one compound one.
- **(iii) INTENT COHERENCE.** One axis per cell: what this engine must be able to answer. WHY a cell is
  bounded or held lives in section 2c and section 9, never as a cell state.
- **(iv) STATE COHERENCE -- which values one remedy does NOT move.** `AMGT-s-12` landing releases
  `AMGT-s-4`, `-8`, `-13`, `-15` (and the held `-b4`) from their root dependency; it does **not** move
  `AMGT-s-1`'s chain (`-2`, `-3`, `-5`, `-9`), `AMGT-s-6`'s (`-7`, `-14`) or `AMGT-s-11`'s (`-10`).
  **Andrew's release of the hold (@d09e26e1b1) MOVED `AMGT-s-b4` from HELD to OPEN and nothing else -- v0.2 of this file is the measurement: one row, one bounds line, the rounds, the holds.** The design-spec
  approval moves `AMGT-s-5`'s .tsx phase and nothing else. A repaired terminal sign-in moves the L6
  pre-spawn check on `AMGT-s-1`'s slot and no cell's state.
- **TOKEN CENSUS (word-boundary), owed with any value-enum proposal:** the only enum this file AUTHORS is the
  round axis (integers, section 5); the status vocabulary is adopted and its census is owed at L6 against the
  task-order and criteria corpus that does not exist yet, exactly as the sibling record states. **Recorded as
  a debt, not claimed.**

### 2a. Rule 24 record for the CELL STATUS vocabulary this file ADOPTS

Adopted verbatim from the sibling decomposition @9e72041da5 section 2a; restated so this file carries its
own record rather than a pointer:
- **(i) MECE over the declared domain** = every cell of this rectangle at any moment. The uncovered member
  the sibling hunted and found -- *"evaluated, and deliberately not cut this round"* -- is `CLOSED` **with
  its pointer**, not a seventh value.
- **(ii) SAME GRAIN** -- every value is a property of a CELL, none of a task order or a criterion.
- **(iii) INTENT COHERENCE** -- one axis: how far this cell has travelled. `HELD` is on that axis (not
  travelling, with a named owner); WHY it is held is section 9's, deliberately not a status value.
- **(iv) STATE COHERENCE.** Spawning a worker moves `OPEN -> IN-FLIGHT`; it does **not** move `HELD` (the
  named owner acts) and does **not** move `NOT-EVALUATED` (a re-decomposition, a COO act).
- **TOKEN CENSUS:** owed at L6, as above.

---

## 2b. BATTERY DISPOSITION PER LENS -- mandatory core, each RUN or DECLARED-NOT-APPLICABLE

**All three mandatory lenses were RUN. None is declared not-applicable.** Two COO-minimum lenses from
`org/XXX.md` (`comp-routes`, `comp-cache`) were also RUN; the third (`comp-blast`) is DECLARED-NOT-APPLICABLE
with its reason.

### `comp-schedule` -- RUN, COMPLETE at `--budget 500`. Denominators: C1=23 · C2=6 · C3=12 · C4=20 · C5=335

Scanned 5 of 5 carriers in 36.8 s (the default 90 s budget was NOT used: the sibling measured that it
returns a PREFIX and understated the armed set by 19). **`GATES ARMED: 25`. NONE is owned by this project.**
- `G-1`..`G-7` SENTINEL (C1): INF gold scripts, ETFS_GUARDRAIL schedule gates, black_diamond dispatch. Two
  carry DRIFT CANDIDATE flags, both other lanes'.
- `G-8`..`G-13` DEPLOY-LEDGER (C2): advi-insure, d12-sms, freshguard, opsec-s15. None this project's.
- `G-14`..`G-25` MORATORIA (C3, 12 standing NEVER clauses): **these bind every project including this one**,
  and seven bind specific cells here -- carried into section 2c.
- C4 (20 scope_guards) SEMI-DECIDABLE and C5 (335 `blocking` fields, 137 non-null prose) NOT-DECIDABLE -- a
  reading list, never gates.

### `comp-iam stats` -- RUN. Denominators: 195 TF roles · 188 services · 167 Lambda · 21 EC2 · 1084 operations · 304 gaps

Relevant here: **six services already carry `secretsmanager:GetSecretValue` as a GAP** (the keyword,
news-ingestion, news-trending, news-layer3, portal-data-proxy and volatility-fetcher services) -- the exact
shape `AMGT-s-b4`'s secret read will take when it is released, so that cell's IAM grant is a KNOWN gap
class, not a surprise. The SA role is LIVE-no-DECLARED (section 1a). **BLINDNESS STATED:** `comp-iam` emits
`wafv2:UNMODELED` and `UNMAPPED-METHOD`; its 304 is a floor on the DESIRED plane, not a population claim.
No cell is cut against the gap count.

### `comp-adversary` -- RUN on this file; declaration at section 7

### `comp-routes behaviors` -- RUN (COO minimum). 28 behaviors, DESIRED plane

Section 1a/1b: every origin S3 or API Gateway; the SPA default serves the page; no desktop origin; the seam
is a design deliverable at `AMGT-s-2`. A new backend API for this project needs its own behavior and
`auth-validator-edge`, and a `.tsx`-only page needs none.

### `comp-cache map` / `collisions` -- RUN (COO minimum). 118 sites / 94 keys / 44 files / 17 shared / 0 mismatches

Section 1a. Bound on every portal cell: keys namespaced under this page, `collisions` re-run at commit.

### `comp-blast` -- DECLARED-NOT-APPLICABLE at L5, with the reason

No cell deletes, renames or re-points an existing resource. `AMGT-s-6` CREATES a bucket; the blast radius of
a resource that does not yet exist is empty by construction. ⛔ `comp-blast` becomes OWED at `AMGT-s-6` the
moment its Terraform touches an existing bucket policy, role or distribution, and at `AMGT-s-2` if the seam
design adds a CloudFront behavior -- named at the cell, not run here against a change that does not exist.

### Non-core lenses -- DECLARED-NOT-APPLICABLE, with reasons

`comp-transform`, `comp-pipescript`: no cell touches a data prop, a gold script or a medallion tree. The
project writes to a new bucket outside `data/*/scripts/`.

---

## 2c. BOUNDS THE BATTERY ADDED TO CELLS -- carried here, and into the L6 cut

| cell | bound the battery added | lens |
|---|---|---|
| `AMGT-s-1`, `AMGT-s-2` | ⛔ **`integrations/bloomberg/READ_HERE.md` BINDS.** First act `bloomberg_health`; on `ok: false` the worker does NOT sign in (the 2-attempt budget is `0.0.3_BG_BBGTerminal`'s); credentials reach a process ONLY through `bbg_credentials.py --` and are never written anywhere; derived fields are CURRENT-DAY-ONLY with no backfill, so raw bytes land first; `data/bloomberg/` is never minted. **`G-24`:** `AMGT-s-2` touches NEW securities -- the manifest's own bound; the cell carries the word's question and does not spend it. | READ_HERE · comp-schedule C3 |
| `AMGT-s-2` | ⛔ **THE SEAM HAS NO PRECEDENT** (section 1b). The request path from API Gateway to a process on this box is a DESIGN deliverable with its own criterion, before any build; the daily pull's push shape and the README's planned local-terminating SSM tunnel are the nearest prior art and neither is the answer. **`G-21`:** whatever crosses the seam is derived, never hardcoded to this device. | comp-routes · README |
| `AMGT-s-b4` | **RELEASED @d09e26e1b1; THE REFERENCE IS @b1656bbebc (Andrew's third word).** PRD v0.3 s.3a binds in full: `C-SA-NAMED-SOURCE` (amended -- the API artifact, never the page: the page is JS-rendered and its HTML holds no content); `C-SA-ROUTE-COMPARISON` (DISCHARGED -- no cell re-runs it); `C-SA-SESSION-SHAPE` (harvest in a real browser, park, ride by REST through the residential proxy, re-harvest on the challenge signal; the jar carries the bot-protection cookies AND a per-ticker Referer; **a 200 with a 2-byte body is a failure**); `C-SA-NO-POST-THROUGH-PROXY` (the zone refuses every POST; a login never completes through it; reads only); `C-SA-UNMEASURED` (session lifetime, headless/Linux, MFA, rate limits, and the vendor's terms -- **the terms are Andrew's and no cell rules on them**); `C-SA-VENDOR-WORD` (L4's ruling: exploration and comparison AUTHORIZED, recurring or production use NOT -- the cell tests ONCE on a stated set and does not schedule or serve). The harvester `sa_harvest_session.py` and the fetcher `sa_rest_fetch.py` exist at the CRO's scripts folder: EXTEND, never rebuild (the build ladder). **`G-24`** is carried through `C-SA-VENDOR-WORD`. | PRD v0.3 s.3a · the reference @b1656bbebc · comp-schedule C3 |
| `AMGT-s-6` | ⛔ **`G-16` + `G-22` + `G-19`.** A change-management entry in `ledger/` BEFORE the apply, closed and committed BEFORE the grading reads; `safe-apply`, never bare `terraform apply`; no second output path beside the one bucket. `C-RAW-BEFORE-DERIVED`: the raw prefix exists before any derived one. | comp-schedule C3 |
| `AMGT-s-7`, `AMGT-s-15` | ⛔ **`G-20` (the alerting moratorium) IS ARMED.** A freshness VIEW a person opens and a rot SIGNAL a person reads are the bar; a schedule, an alarm, an SNS topic or an SES send would be the thing the moratorium forbids and would need Andrew's explicit word. | comp-schedule C3 |
| `AMGT-s-5`, `AMGT-s-3`, `-7`, `-9`, `-10`, `-14` | ⛔ **`C-DESIGN-SPEC-FIRST`:** `AMGT-s-5` owns the design spec and NO `.tsx` is written on any portal cell until it is approved -- the F10 precedent's own wording. **`G-21`:** no device-specific logic in `portal/`. Cache keys namespaced under the page; `comp-cache collisions` clean at commit. The page rides the `/*` SPA default. | comp-cache · comp-routes · comp-schedule C3 |
| `AMGT-s-8`, `AMGT-s-12` | **F6 RE-MEASURED FIRST**, on the corpus, with the denominator printed. `C-SHARED-DEFECT`: one unscoped pass over the population beside the per-name check. `C-IDENTITY-RESOLVED`: never two sources side by side until resolved. ⚠ Whether the stale set reaches the PRINTED packs is UNVERIFIED (PRD section 6) and no cell concludes it. | PRD · comp-adversary |
| `AMGT-s-11` | ⛔ **NO THRESHOLD EXISTS AND NONE IS INVENTED.** Each class's rule PRODUCES the distribution it is drawn against and states its threshold in the deliverable. `C-CHECK-MUST-REFUSE`: the refusing input is NAMED and RUN. A rule whose refusal case was reasoned rather than exercised has not been tested. | PRD |
| `AMGT-s-13` | ⛔ **`C-LISTING-NOT-CAPABILITY` + `G-24`.** The criterion is a MEASUREMENT; a criterion demanding a working feed from an unexercised catalogue is one a correct build cannot satisfy. The datasets API is a FOURTH SURFACE on the one credential, not a fourth zone. F13's cashtag-native absence is a required disclosure on the feed. | PRD · brief |
| every cell | Every F-number is CITED, not CONFIRMED: a cell relying on one re-measures it first and its criterion says so. **13 of 14 bars are EXERCISED: no cell claims one REALIZED on the strength of its own artifact; the `DONE WHEN` state line is graded, never the `ACCEPT` paragraph.** `G-14`: never a producer's self-report. `G-25`: the report of an act is never composed in the call that performed it. `C-NO-CONTACT`: no seat contacts Adam Muller. | PRD · comp-schedule C3 |

---

## 3. Placement axis

**Every cell EXECUTES on `site-z`** (`project.json` `fabric: site-z`; this lane is on SITEZ; workers are
subagents of this lane on this device). The axis is NOT degenerate at the level of what cells TOUCH, and the
table in section 1 carries it: DAPI on this box (`-1`, `-2`); AWS through Terraform (`-6`); portal source
(`-3`, `-5`, `-7`, `-9`, `-10`, `-14`); S3 (most); SharePoint through the Opal gateway, read-only (`-8`,
`-12`); the Bright Data datasets surface (`-13`, under `G-24`); Seeking Alpha (`-b4`, held). **The one
cross-plane request path -- browser to box -- is `AMGT-s-2`'s design deliverable (section 1b).**

⛔ **The manifest's `verb` column (`build` / `wire` / `measure, then build`) is a VERB, never a seat
assignment.** `2.0.0_SA_COO~ZZZ` seats workers at L6.

---

## 4. Dependency edges, keyed to OBSERVED completion, never to a status word

Read from the manifest's own `depends on` column. `AMGT-s-b4` inherits row S4's edge.

```
  AMGT-s-1   <- (none)          AMGT-s-11  <- (none)          <-- FOUR INDEPENDENT ROOTS
  AMGT-s-6   <- (none)          AMGT-s-12  <- (none)

  AMGT-s-2   <- AMGT-s-1
  AMGT-s-3   <- AMGT-s-1
  AMGT-s-5   <- AMGT-s-1, AMGT-s-3
  AMGT-s-9   <- AMGT-s-1, AMGT-s-4

  AMGT-s-4   <- AMGT-s-12
  AMGT-s-b4  <- AMGT-s-12          (released @d09e26e1b1; an ordinary edge now)
  AMGT-s-8   <- AMGT-s-12
  AMGT-s-15  <- AMGT-s-12
  AMGT-s-13  <- AMGT-s-11, AMGT-s-12

  AMGT-s-7   <- AMGT-s-6
  AMGT-s-14  <- AMGT-s-6

  AMGT-s-10  <- AMGT-s-11
```

⭐ **`AMGT-s-12` IS THE ROOT FOUR SURFACES HANG OFF AND IT IS NOT IN THE BRIEF'S OWN SURFACE LIST** (PRD
section 4). It is the direct remedy for the ONLY defect this project has measured in production. ⛔ **Cutting
`AMGT-s-4`, `-8` or `-13` before it lands rebuilds F6 on a new axis** -- that is a PRD bound, not a
suggestion, and the edges above encode it.

⚠ **`AMGT-s-9` DEPENDS ON `AMGT-s-4`, NOT ON `AMGT-s-b4`.** With S4 split, the drafting face proceeds on
IR-channel and publication evidence; Seeking Alpha evidence joins when the held cell lands. No cell was
re-sequenced around the hold; the hold removes one cell from round 2.

---

## 5. The arc as rounds

- **ROUND 1 (4 cells):** `AMGT-s-1` (the model block -- the head of the longest chain), `AMGT-s-6` (the
  store), `AMGT-s-11` (the rules -- what every check face reads), `AMGT-s-12` (identity -- the root).
- **ROUND 2 (10 cells, all OPEN):** on `-1`: `-2`, `-3`; on `-6`: `-7`, `-14`; on `-11`: `-10`; on `-12`: `-4`,
  `-8`, `-15`, `-b4`; on `-11`+`-12`: `-13`.
- **ROUND 3 (2 cells):** `AMGT-s-5` on `-1`+`-3`; `AMGT-s-9` on `-1`+`-4`.

⛔ **NINE CHAINS, ALL OPEN, AGAINST THE DEFAULT FAN-OUT CAP OF EIGHT.** A chain is a worker's queue -- a maximal
path with every cell in exactly one queue: `-1 -> -3 -> -5` · `-2` · `-12 -> -4 -> -9` · `-8` · `-15` · `-13` ·
`-6 -> -7 -> -14` · `-11 -> -10` · `-b4` (3+1+3+1+1+1+3+2+1 = 16, the partition closes). Four chains start at
issuance (the roots); five more start as their root lands. **The `fanout:` line in the L6 issuance commit is
DERIVED from these chains, never chosen: 8 of 9, cap 8** -- the natural deferral is `-15` (the list register: a
`build` with no dependants), which takes the first freed slot. This section is the INPUT to that derivation and
is not itself the fan-out.

⚠ **THE ROUNDS ARE A READING OF THE EDGES, NOT A SECOND SOURCE OF TRUTH.** If a cell lands early the next
round's cells become cuttable early; the edges govern, the round numbers describe.

---

## 6. `<preflight>` -- what this decomp actually ran, with denominators

| act | instrument | result |
|---|---|---|
| project located on both roots | `/canonical-flow` Step 1; `ls`, `cat project.json`, generated index | tree home; `fabric: site-z`; `dep_stage: PRD`; `decompositions: []` |
| tree/index/register validated | `.tools/missions-tree-index.py check` | **0 violations**; tree=8 projects, 8 valid; MACROS 5 of 5 RATIFIED |
| L4 conformance, by the gate's own functions | `to-pipeline-gate.py` `_prd_conformance`, `_top_section`, `FWD_DEF_RE` on the PRD's bytes, sibling PRD as control | @c0b5636ea9: False / 0 / 0 / 1 complaint -> handed back; **@8019bf6433: True / 14 / 1 / 0**; control True / 8 / 1 / 0; header `prd_version: v0.2`, `status: RATIFIED`, 14 outcomes. ⚠ `project.json` `prds[0].version` still reads v0.1 against the header's v0.2 -- a row/header drift, L4's, flagged in the L5 notify. |
| task orders | `.tools/to-check.py --all --project`; tree `task-orders/` | **0** (folder absent) |
| surprise channel | `comp-surprise --project` | **0 items, 0 rows** (53 files scanned, legacy root; tree channel not yet created) |
| unfinished edits / stash / worker branches | `git status --porcelain` on project paths; `git stash list`; `git branch --list` | **none / none / two branches, both other projects'** |
| brief read IN FULL from the working tree | `cat`, 337 lines / 22,244 bytes @19ce7d5b4d (v2) | Parts I-VII; III-B six classes; F1-F13; PART V |
| PRD read IN FULL at its path | `cat`, then the gate functions above | header + fourteen cards + the 16 constraints of s.3 and the four `C-SA-*` of s.3a + 15-row manifest |
| endpoint read IN FULL | `cat` @3bc8f5f2c4 | the fourteen bars, now transcribed into the PRD |
| cell ids vs the enforcer | `CELL_ID_RE` loaded from `.tools/proof-of-spec-check.py` | **16 of 16 match; 5 of 6 malformed controls refused** |
| lane admission | `.tools/owned-paths-validate.py` `check_agent`, lanes from `.owned-paths.yaml` | `decompositions/**` = `TREE_COO`: this lane **permitted**; CTO~Z, CVO~Z and a worker serial **refused** (3 of 3 negative controls) |
| Bloomberg substrate | `bloomberg_health` (MCP, read-only, no sign-in spent) | **`ok: false`** at ~18:5xZ -- section 1a |
| live-plane premises | `comp-find --corpus aws` (graph vintage 12:24:50Z) | `opal-data-research` 0 of 2382; `seeking-alpha` 34 of 2382 |
| **THE MANDATORY CORE BATTERY IS AT SECTION 2b** | | **comp-schedule, comp-iam, comp-adversary RUN; comp-routes, comp-cache RUN; comp-blast DNA with reason** |

---

## 7. comp-adversary declaration

Run ON this file; the declaration grid is in this file's commit message, not inlined, for the reason
section 1 gives: this document is indexed by the L6 coverage limb.

**What the author's evidence context WAS:** the PRD at @8019bf6433 read in full and graded by the gate's own
functions; the brief at @19ce7d5b4d read in full from the working tree; the endpoint at @3bc8f5f2c4 read in
full; the spine's L4/L5/section 3 read at HEAD; the tree contract; the cell-id convention; the Bloomberg
READ_HERE and README; the live AWS graph at 12:24:50Z; `bloomberg_health` live; `comp-schedule` to completion;
`comp-iam`, `comp-routes`, `comp-cache` run; all three of Andrew's words this hour, verbatim; PRD v0.3 s.3a read from the committed blob @f68818832b; the CRO's SA auth
investigation @b1656bbebc read in full.

**What it was NOT:** ⛔ this lane did not read the SharePoint corpus, the 54 workbooks, or any pack -- F1, F6
and the template facts are the brief's, cited. ⛔ It did not call Bright Data (every such call is a vendor
call under `G-24`); F12 and F13 are cited. ⛔ It did not exercise any Bloomberg field; F3, F4, F5 are cited. ⛔
It did not read the seven SA Lambdas' code, the CRO's seven supporting deliverables, or the directive PRD
(`D5_ALT_RESEARCH_PRD.md` -- reading the parent would import outcomes nobody wrote for this project). ⛔ The
`atom-decomp` package's full P0-P12 frontier and sealed-mutant certification were NOT run: the spine names
that harness as a self-check no seat waits on, the sibling that passed L6 today did not run it, and a
focused L5 records the omission as a boundary rather than a certification.

---

## 8. What this decomp REFUSES to assume

- **That F4's unit conventions generalise.** Measured on ONE security; `AMGT-s-1` re-measures on a US name
  and an ADR before any mapping is trusted.
- **That the stale peer set reaches the PRINTED packs.** Unverified (PRD section 6, brief PART VII); no cell
  concludes packs shipped wrong.
- **That any social dataset can be queried by cashtag.** Listed, never exercised; `AMGT-s-13` finds out.
- **That `bloomberg_health: true` means data flows.** Necessary, not sufficient; a reference read confirms.
- **That the seam has a precedent.** It does not (section 1b); `AMGT-s-2` designs it.
- **That the seven SA Lambdas are reusable.** An archive producer for a parked estate; the SA cell builds on the
  measured API route, not the archive -- and does not re-explore the modal, which is measured unworkable.
- **That the per-use egress word extends past the evaluation.** L4 ruled it as `C-SA-VENDOR-WORD`:
  exploration and comparison authorized, recurring or production use not; this file adopts that ruling as
  written, with its author, and adds nothing to it.
- **That the 16-and-15 is an invariant.** It is a measurement at this edit.
- **That any cell is buildable as written.** `AMGT-s-13` explicitly may deliver a measurement and no feed;
  `AMGT-s-2` may find the seam design needs Andrew's word on infrastructure before a build exists.

---

## 9. Holds, and whose they are

- **`AMGT-s-b4` WAS HELD by Andrew (@8c609decf7) and IS RELEASED (@d09e26e1b1).** Verbatim, the release: *"We have
  figured out the Seeking Alpha case"*, with the CRO's investigation @b1656bbebc named as THE REFERENCE for every
  SA-procurement order and *"Shouldnt need to recut the details on the PRD"*. The cell is `OPEN`, its order is cut
  in the one issuance like every other, and its slot spawns when `AMGT-s-12` lands. **No coverage exemption is
  needed and none is taken.**
  ⚠ **If his updated information bears on the IDENTITY of an SA symbol rather than the fetch route,
  `AMGT-s-12` becomes in-scope after all** -- named so it reads as his word widening, never as a defect
  in this cut (`1.0.0_SA_CTO~Z` msg 21044, confirming both readings).
- **`AMGT-s-5`'s .tsx phase is HELD on the design spec's approval** (`C-DESIGN-SPEC-FIRST`; the F10 precedent
  gated it in the same words). The spec is the cell's first deliverable and is OPEN.
- **`AMGT-s-1`'s slot has a PRE-SPAWN CHECK, not a hold:** `bloomberg_health` must read `ok: true` before the
  worker is spawned; at this vintage it reads `false` (section 1a). The repair is `0.0.3_BG_BBGTerminal`'s
  playbook, on this device, live. L6 checks; L5 does not wait.
- **`C-VENDOR-EGRESS` words are NOT held for `AMGT-s-2` (new securities), `AMGT-s-13` (a dataset trigger) or
  `AMGT-s-b4` (the API route).** Each cell carries the question in its criterion; none spends or assumes it.
- **NONE held by this lane, and none at Andrew.** Sixteen cells are `OPEN` (one, `AMGT-s-5`, with its .tsx phase
  held on the design spec's approval). Round 1 is cuttable now.
- **PUSH STATE: this lane's commits are LOCAL.** `0.0.0_AB_MSTR~Z` holds the push window.


---

## 10. ROUND 2 (RECUT) -- from the L10 round-1 analysis @4d31cf4caa (1.0.0_SA_CTO~Z)

**v0.3 IS AN L10 RECUT, NOT A NEW DECOMPOSITION.** Round 1 graded 0 of 14 REALIZED (a strong build:
16/16 terminal, valid instances, 24/0 channel, 13/16 judgment PASS) -- but 13 of 14 FWD bars are
EXERCISED (an analyst used a SERVED surface) and the surfaces are UNSERVED because every .tsx waits on
Andrew's DESIGN_SPEC approval (C-DESIGN-SPEC-FIRST), which measured EMPTY. So the exercise is
systematically unmet and the gap is EXERCISE, not a missing outcome -- coverage read: every FWD has a
cell, 0 uncovered, no PRD addendum. The round-1 cells (AMGT-s-1..15, AMGT-s-b4) are FROZEN and terminal;
this section ADDS the remediation cells the analysis's s.4 sends back. Nothing round-1 moves.

**THE TRUE CRITICAL PATH IS ANDREW'S, AND IT IS A ROUND-3 GATE, NOT THIS ROUND'S:** the DESIGN_SPEC
approval (moves 12 of 14 outcomes at once), plus four per-use/decision words (social vendor -- FWD-11;
drafting model -- FWD-9; peer-universe quota -- FWD-8; the two lists' owners -- FWD-14). The SURFACE
EXERCISE of every FWD is ROUND 3, expressly qualified per Rule 27 as the essential wait the analysis
s.4 names (a UI serving before its design is approved is the failure C-DESIGN-SPEC-FIRST exists to
prevent). This round is the MECHANICAL work that does NOT wait on the spec.

⛔ **DO NOT RE-CUT AMGT-s-b4** -- W9-S2 is disarmed by the completed re-run (18 objects / 3 tickers,
all six mechanical criteria PASS, drained @3be9d03962); its world-fact stands and the cell is terminal.

### 10a. The five round-2 cells -- ALL INDEPENDENT (fanout 5 of 5, cap 8, no deferral)

Each cell fixes ONE landed round-1 cell's named defect; none depends on another (AMGT-r-4 rides the SA
raw for tickers AMGT-s-b4 already resolved, so it does not wait on AMGT-r-12's coverage). Ids match
CELL_ID_RE (AMGT-r-<n>, verified against the enforcer's pattern).

| cell | fixes | FWD | the defect (analysis s.2) | the engine, and its bound |
|---|---|---|---|---|
| `AMGT-r-1` | `AMGT-s-1` / W1-S2 | FWD-1, FWD-3 | the fiscal-year join groups by the CALENDAR year of `date`, so a non-December filer's period-end fundamentals pair with a price ~9 months off (BABA, FYE 31 March: 100% of rows split). A served-correctness defect the mechanical AC4 could not see (a December-heavy sample passes). | THE FISCAL-YEAR JOIN, SERVED-CORRECT. Re-key the join to the ISSUER'S fiscal period so a period-end fundamental pairs with the price AT that period-end, never the calendar-year price. EXERCISE a CONTROL on BABA US Equity (FYE 31 March, ALREADY landed by AMGT-s-1 -- no new unique security, F2): the control FAILS under calendar-year grouping and PASSES under fiscal-period grouping (the difference arm). Home: `integrations/bloomberg/research/`. Bound: NO new unique security; the control MUST discriminate, not merely pass. |
| `AMGT-r-4` | `AMGT-s-4` | FWD-4 | s-4 AC7 was NOT_EVALUATED at grade time -- SA raw had 0 keys then; AMGT-s-b4 has since landed 18 objects / 3 tickers (BABA/RTX/+1). The reader was never exercised on real SA content. | THE SA COVERAGE RE-EXERCISE (RIDE, not re-write). Re-run the landed coverage reader over the SA raw AMGT-s-b4 landed under `raw/seekingalpha/`, so coverage_items carry real SA-class items keyed by the identity layer, ranked, admitted PROVISIONAL by the held-back item rule. AC: `sa_raw_keys_found` >= 3 (not 0), the F11 redirect trap still 0, the identity gate still refuses an UNRESOLVED-source attachment. Home: `lib/research/coverage/` + reads the store. Bound: NO new vendor call (reads LANDED raw); no HTML parse (C-SA-NAMED-SOURCE). |
| `AMGT-r-10` | `AMGT-s-10` | FWD-10 | s-10 AC6 FAIL: '12345 [PROVISIONAL]' skims as "a number, fine" -- the held-back verdict lives in the DATA and is absent in the READING, so an unchecked figure ships looking checked. | THE CHECK-FACE MARKER, IN THE READING. Add a machine-readable per-verdict MARKER (a colour token AND an icon name) to the check-face render and SPEC_SECTION_checkface.md, so PASS / REFUSE / PROVISIONAL are visually distinct and the later .tsx binds it -- land it BEFORE PROVISIONAL figures serve. AC: the render carries a distinct marker per verdict and a PROVISIONAL figure's marker != a PASS figure's, exercised on the fixture (the difference arm). Home: `lib/research/checkface/`. Bound: NO .tsx (C-DESIGN-SPEC-FIRST) -- the marker is a data+spec artifact the .tsx reads. |
| `AMGT-r-12` | `AMGT-s-12` | FWD-8, FWD-13 | after W7-S3's remediation the identity layer is 32 MEASURED / 32 distinct, with 57 UNRESOLVED residual (coverage, not a regression) -- four surfaces hang off it. | THE IDENTITY COVERAGE PASS. Resolve UNRESOLVED bloomberg_ticker cells WHERE A LEGITIMATE MEASURED SOURCE EXISTS (the SA sa_ids AMGT-s-b4 landed; a workbook cell that is NOT the shared template placeholder; a coverage-universe cross-reference) -- and SURFACE the folder-name fallback as an identity-layer DESIGN QUESTION for Andrew, do NOT code it. AC: MEASURED rises from 32 by the count legitimately resolvable, distinct still == MEASURED (no new shared value -- the AC7 unscoped pass still reads 0 shared), the residual UNRESOLVED count is printed with a per-name reason, and the folder-name-fallback trade-off is stated. Home: `lib/research/identity/`. Bound: NO folder-name fallback coded; NO new vendor call. |
| `AMGT-r-15` | `AMGT-s-15` | FWD-14 | s-15 AC6 FAIL: the official-vs-impostor test is a bare OR of three unequal checks, so an impostor beats the weakest (a copied "official account of <domain>" bio admits on check 3 alone). | THE IMPOSTOR AND-CLAUSE. Require check (3) (the bio/self-description) to CO-OCCUR with check (1) OR check (2) (the stronger signals) in the official-vs-impostor test in `social_accounts.json`'s schema and the rule. AC: the predicate REFUSES a fixture passing ONLY check 3 (the impostor) and ADMITS one passing check 3 AND (1 or 2) (the difference arm); the schema states the AND-clause. Home: `lib/research/lists/`. Bound: NO vendor call (the test is a rule); the owner stays UNASSIGNED (C-NO-CONTACT -- Andrew's). |

### 10b. Rule 24 record for what v0.3 ADDS (the five round-2 cells)

- **(i) MECE over the DECLARED domain = the analysis s.4's remediation set.** Written as a SUBTRACTION,
  not a recall: the analysis names FIVE mechanical items + the surface exercise (round 3) + do-not-recut
  s-b4. This section is exactly those five; the surface exercise is round 3 (Andrew's gate) and s-b4 is
  excluded by name. No sixth cell, no dropped item.
- **(ii) SAME GRAIN:** each is one cell fixing one landed cell's named defect.
- **(iii) INTENT COHERENCE:** one axis -- served-correctness / reading-not-data / real-content re-exercise
  / coverage / the AND-clause. No cell mixes remediation with new scope.
- **(iv) STATE COHERENCE -- what these cells do NOT move:** they fix the mechanical defects; they do NOT
  make any EXERCISED bar REALIZED. That needs the SERVED surface, which needs the .tsx, which needs
  Andrew's DESIGN_SPEC approval -- round 3. A round-2 cell landing complete does not close its FWD.

### 10c. Round-1 lessons absorbed into this cut (analysis s.5)

The round-1 cut carried defects every one of which a worker caught by RUNNING the criterion. This cut:
- Every criterion DISCRIMINATES -- a difference arm (fails one input, passes its twin), never an
  always-pass or always-fail; run the EXACT invocation against the world before handing it over.
- The proof-of-spec instance uses the FULL task-order stem filename (`<PROJECT>.TO-<cell>.<slug>.proof_of_spec.json`)
  -- the flip gate's discovery glob requires it (W7-S2 / W3-S2).
- A criterion names the instrument that can OBSERVE the artifact (W2-S2/W2-S4: comp-routes reads its own
  checkout; a bare comp-tool on a branch answers from the main checkout -- read the declared source directly).
- The write grant is live only while the order is NON-TERMINAL: the order is committed before the spawn,
  and the worker's flip rides in a commit whose parent still carries the order open (W7-S5).

### 10d. The round axis, updated

- **ROUND 2 (RECUT, 5 cells, all INDEPENDENT):** `AMGT-r-1`, `AMGT-r-4`, `AMGT-r-10`, `AMGT-r-12`,
  `AMGT-r-15`. Five chains of one; `fanout: 5 of 5, cap 8` (no deferral -- 5 < 8). Each spawns at issuance.
- **ROUND 3 (deferred on Andrew's gate):** the SURFACE EXERCISE of every FWD -- the .tsx that serves each
  surface, cut only after the DESIGN_SPEC approval and the four words land. NOT cut now.

**PREFLIGHT for the recut:** the mandatory core battery is NOT re-run -- v0.2's run (comp-schedule 25
armed none this project's; comp-iam 195/188/1084/304; comp-adversary 10/10) stands at its vintage and no
round-2 cell touches a new gate/IAM/adversary surface (all five are edits to landed modules against
landed data). The authority for the recut is the L10 analysis @4d31cf4caa (the CTO's one send), cited in
each round-2 order's authority chain. comp-blast DECLARED-NOT-APPLICABLE (no infra act; no served-output move).

**PUSH STATE: this amendment is LOCAL.** 0.0.0_AB_MSTR~Z holds the push window.

*(v0.3 amended 2026-09-11T05:30Z by 2.0.0_SA_COO~ZZZ -- the L10 recut from @4d31cf4caa; round-1 sections 1-9 unchanged.)*

## 11. ROUND 3 (v3, the corrective continuation; informally "round 2b") -- from the L10 round-2 analysis @c48576bf85 (1.0.0_SA_CTO~Z)

**CARRIER MAPPING (1.0.0_SA_CTO~Z ruling @21336).** The carrier numbers rounds by ISSUANCE SEQUENCE (integer / ^v[0-9]+$): round 1 (v1) the initial build, round 2 (v2) the r-* defect fixes, and THIS corrective continuation (the rb-* issuance @3f2189f28b) the THIRD issuance -- so it is CANONICAL ROUND 3 (v3). The CVO stamps L8/L9/L10 as r3 and cuts REMEDIATION_v3; any carrier artifact (this L5 decomp round field, the L6 issuance, each order's <round>) reads 3. The rb- CELL ids stay (cell ids are free-form; only the ROUND integer is constrained). The surface exercise (Andrew's DESIGN_SPEC-gated .tsx) is a LATER round (v4+), NOT pinned to 3.

**v0.4 IS AN L10 RECUT OF THE THREE FAILED ROUND-2 FIXES + TWO NEW r-1 SOURCE FINDINGS, NOT A NEW
DECOMPOSITION.** Round 2 was the defect-fix round for the five defects round 1 routed. The CTO's round-2
analysis @c48576bf85 (answering the CVO's slug REMEDIATION_v2 @b3acbcf3dd, drain 56c755b86a; artifacts
pinned 9a2e542c0b) graded 2 PASS / 3 FAIL, and the CVO's independent L8/L9 control surfaced 2 more source
findings on r-1. **0 of 14 FWDs newly REALIZED, unchanged -- every FWD still needs an EXERCISED served
surface and no .tsx exists.** This round is the pre-surface CORRECTNESS the surfaces will rest on; it
builds no surface. The round-1 and round-2 cells are FROZEN and terminal; this section ADDS the five
round-2b remediation cells the analysis s.2/s.3/s.5 sends back. Nothing prior moves.

**NONE OF THE FIVE IS DESIGN_SPEC-GATED** (analysis s.2/s.5): print-fixture / doc / logic / source
correctness, doable now without a .tsx and without Andrew's design approval. Only the SURFACE EXERCISE
(round 3) waits on him -- unchanged.

**C-S8 and C-S9 FOLD IN AS TEXT CORRECTIONS, not cells** (analysis s.3; both OBSERVATION/INERT, the WORK
is sound):
- **C-S8:** the r-1 order text implied a mapped `FISCAL_YEAR_END` reference field; that field is
  BAD_FLD/INVALID_FIELD and the join correctly uses the fundamentals ROW-DATE. Round-2b cells that touch
  the fiscal join name the measured row-date carrier, never a mapped reference field.
- **C-S9:** the SA exercise population is BABA/BA/COST (18 raw keys), NOT the order's BABA/RTX/+1. Any
  round-2b context that names the SA denominator uses the actual one.

### 11a. The five round-2b cells

M = FOUR dependency-independent chains: three single-cell chains (`AMGT-rb-10`, `AMGT-rb-12`, `AMGT-rb-15`,
DISJOINT write surfaces) + one two-cell chain (`AMGT-rb-1` -> `AMGT-rb-2`, both on
`integrations/bloomberg/research/`, serialized -- rb-2 wires the block rb-1 corrects and they share the
write surface). `fanout: 4 of 4, cap 8`. Ids match CELL_ID_RE (verified against the enforcer's pattern).

| cell | fixes | finding | FWD | the defect (analysis s.2/s.3; CVO evidence @b3acbcf3dd) | the engine, and its bound |
|---|---|---|---|---|---|
| `AMGT-rb-10` | `AMGT-r-10` | C-S12 (BLOCKING) | FWD-10 | the round-2 fix added a SECOND trailing text tag (`12345 [PROVISIONAL] [WARN]`) -- another plain suffix on the same NUMBER-FIRST presentation round 1 already rejected; render_print.py appends the icon as bracketed text and never renders a leading status or the colour_token; and the test compared DIFFERENT values (500 vs 12345), so string inequality never proved the marker made the difference. | THE CHECK-FACE SALIENT WARNING, IN THE READING. Make a PROVISIONAL/REFUSE figure visibly salient AT A GLANCE in the permitted print fixture (render_print.py, S5) -- a LEADING status marker (ASCII, from the closed contract green/OK, amber/WARN, red/BLOCKED) so the number is no longer the FIRST thing read, not a second trailing word. The difference-arm test renders the SAME number under PASS and under PROVISIONAL and shows the PROVISIONAL render is distinguished at the START. Regrade AC4 (CVO) before FWD-10 is treated realized. Home: `lib/research/checkface/`. Bound: NO .tsx (C-DESIGN-SPEC-FIRST); the marker contract is PRESERVED and carries into the approved design; NO non-ASCII (no glyph/emoji) -- a leading ASCII status token is the print-path "visual prominence". |
| `AMGT-rb-12` | `AMGT-r-12` | C-S13 (BLOCKING) | FWD-8, FWD-13 | the measured-source limb PASSED (34 distinct MEASURED); the DECISION NOTE failed -- `DESIGN_QUESTION_identity_fallback.md` twice promises "MEASURED-or-better 34 -> 49" while limiting ALL fallback values to INFERRED (categories that cannot share one denominator) and treats hypothetical renaming as a measured failure. | THE IDENTITY DECISION-NOTE CORRECTION (doc). Correct the note to "34 MEASURED + up to 15 INFERRED candidates" (never "49 MEASURED-or-better"); SEPARATE observed ambiguity (e.g. Nokia FH, a real trailing-token ambiguity in this corpus) from hypothetical renaming (e.g. a re-org rename -- not observed); NAME which downstream gate(s) still refuse INFERRED. Keep the fallback UNIMPLEMENTED pending Andrew. AC: a census over the doc finds NO "MEASURED-or-better ... 49" claim, the doc states 34 MEASURED + up-to-15 INFERRED, it names the INFERRED-refusing gate(s), and the measured count (34 distinct) is unchanged. Home: `lib/research/identity/` + deliverable. Bound: NO fallback coded (AC3 still refuses it in `*.py`); NO new vendor call; the 34 MEASURED are not re-litigated. |
| `AMGT-rb-15` | `AMGT-r-15` | C-S14 (BLOCKING) | FWD-14 | the advertised AND-clause executes as `check1 OR check2` and returns official immediately (the docstring's "AND any further evidence" is UNMET); the 8-case enumeration admits check2-alone and check1-alone; verification (check2) is an untyped boolean NOT bound to company identity, so a non-identity verification mark + a copied bio still passes. | THE IMPOSTOR PREDICATE, CORRECTED. Clarify the INTENDED truth table and the identity meaning of "verification"; make the CODE enforce the STATED contract (require the co-occurrence where intended -- resolve the docstring-vs-code contradiction in favour of the stated rule); bind check2 to COMPANY IDENTITY (a mark that does not attest the company's identity is not check2). Add NEGATIVE CONTROLS for (a) verification-without-further-evidence and (b) a mark that does not attest company identity. AC: the 8-case truth table matches the STATED contract with no admit the contract forbids; the two negative controls REFUSE where the old code admitted (the difference arm). Home: `lib/research/lists/`. Bound: ALL real handles stay UNRESOLVED; NO social/vendor call and NO owner assignment (C-NO-CONTACT; Andrew's per-use word, round 3). |
| `AMGT-rb-1` | `AMGT-r-1` / C-S15 | C-S15 (BLOCKING) | FWD-1, FWD-3 | `fye_join._nearest_price` falls back to the nearest point in EITHER direction when nothing is on-or-before, and `gap_days` uses `abs`, so a period_end 2025-12-31 with only a 2026-01-02 price returns that FUTURE price at gap_days 2 and passes the under-45-day check. A BOUNDED source defect -- 0 of 30 live served rows affected at this vintage. | THE FISCAL JOIN, DIRECTION-CORRECT. `_nearest_price` returns UNRESOLVED (None) when no on-or-before price exists (drop the either-direction FUTURE fallback); a price_date is NEVER after its period_end. Add a FUTURE-ONLY negative control (period_end 2025-12-31 + only a 2026-01-02 price -> UNRESOLVED, never gap 2) and a DIRECTION ASSERTION (price_date <= period_end on every resolved row). PRESERVE the passing 3-security sample and its exact pins (0 of 30 unaffected). Home: `integrations/bloomberg/research/`. Bound: the passing sample is not disturbed; C-S8 -- name the fundamentals ROW-DATE carrier, never a mapped FISCAL_YEAR_END field; NO new vendor call. |
| `AMGT-rb-2` | `AMGT-r-1` / C-S16 | C-S16 (OBSERVATION, re-cut as integration) | FWD-1, FWD-3 | `derive_fye_fixed.py` writes `derived/model_block_fye/`, a DISTINCT engine lane; the provenance/print consumers still read the original `model_block` lane (r-1 explicitly excluded replacing them), so the served analyst pack still reads the OLD calendar-year join. | THE FISCAL BLOCK, WIRED TO THE CONSUMER. NAME the provenance/print consumer path that reads `model_block` and TEST that the served pack reads the CORRECTED `model_block_fye` lane (its derived vintage) -- the smallest correct switch, never overwriting or aliasing `model_block` (STORE_CONTRACT rule 1). AC: a test names the consumer and shows it reads the corrected lane -- the difference arm: for BABA the OLD lane gives the calendar-year price, the corrected lane the fiscal-period price. DEPENDS ON rb-1 (wires the direction-corrected join). Home: `integrations/bloomberg/research/`. Bound: do NOT overwrite peer outputs; NO round-3 / .tsx; NO new vendor call. |

### 11b. Rule 24 record for what v0.4 ADDS (the five round-2b cells)

- **(i) MECE over the DECLARED domain = the analysis s.5's round-2b recut set.** SUBTRACTION, not recall:
  the analysis names the THREE failed fixes (r-10 salience C-S12, r-12 doc C-S13, r-15 predicate C-S14) +
  the TWO new r-1 source findings (C-S15 direction, C-S16 integration) = FIVE. C-S8/C-S9 are text
  corrections folded in (not cells); C-S10 is the CTO's to route to the repo owner (not a COO cell);
  round 3 is Andrew's. No sixth cell, no dropped item.
- **(ii) SAME GRAIN:** each is one cell fixing one named finding.
- **(iii) INTENT COHERENCE:** one axis -- reading-salience / doc-coherence / predicate-correctness /
  source-direction / consumer-integration. No cell mixes remediation with new scope.
- **(iv) STATE COHERENCE -- what these cells do NOT move:** they fix the pre-surface correctness; they do
  NOT make any EXERCISED bar REALIZED (that needs the served surface -> the .tsx -> Andrew's DESIGN_SPEC --
  round 3). rb-1 + rb-2 TOGETHER make the fiscal alignment LIVE in the served pack; alone, r-1's fix was
  correct on the sample but not the served figure. A round-2b cell landing complete does not close its FWD.

### 11c. Round-2 lessons absorbed into this cut

The round-2 cut carried three fixes that FAILED the CVO's judgment and two the CVO's own control caught.
This cut:
- **A difference arm must vary ONLY the thing under test.** r-10's round-2 test compared 500 vs 12345 --
  two different numbers, so string-inequality proved nothing about the marker. Every round-2b difference
  arm holds the value FIXED and varies only the verdict / direction / check.
- **A judgment fix must satisfy the JUDGMENT, not a mechanical proxy.** r-10 added a second text tag
  (mechanically "a marker") that did not achieve at-a-glance salience (the judgment). rb-10's AC names the
  SALIENCE property (leading status, value not first), not merely "a marker field present".
- **Advertised contract == executed code.** r-15's docstring said AND, the code did OR. rb-15 makes the
  8-case truth table the acceptance and asserts the code matches the STATED contract.
- **A benefit claim states ONE denominator's category.** r-12's note mixed MEASURED and INFERRED under one
  "34 -> 49" number. rb-12 keeps the two categories separate with their own counts.
- **A source fix is not live until a CONSUMER reads it.** r-1 corrected the join on a new lane nothing
  consumes. rb-2 tests the consumer path; rb-1 + rb-2 is the pair that makes it served.
- Carried from round 1: every criterion DISCRIMINATES; the proof instance uses the FULL task-order stem
  filename; a criterion names the instrument that OBSERVES the artifact; the write grant is read while the
  order is NON-TERMINAL.

### 11d. The round axis, updated

- **ROUND 1 (16 cells):** terminal, frozen.
- **ROUND 2 (5 cells):** terminal, frozen. 2 fixes LANDED (r-1, r-4), 3 FAILED + 2 new source findings ->
  round-2b.
- **ROUND 3 (v3, RECUT, 5 cells; informally 'round 2b'):** `AMGT-rb-10`, `AMGT-rb-12`, `AMGT-rb-15` (three independent chains of one)
  + `AMGT-rb-1` -> `AMGT-rb-2` (one two-cell chain, serialized). `fanout: 4 of 4, cap 8`. Four workers
  spawn at issuance; the fiscal worker runs rb-1 then rb-2.
- **ROUND 3 (deferred on Andrew's gate):** the SURFACE EXERCISE of every FWD -- the .tsx that serves each
  surface, cut only after the DESIGN_SPEC approval + the four words land. NOT cut now.

**PREFLIGHT for the round-2b recut:** the mandatory core battery is NOT re-run -- v0.2's run stands at its
vintage and no round-2b cell touches a new gate/IAM/adversary/vendor surface (all five are edits to landed
modules against landed data). The authority is the L10 round-2 analysis @c48576bf85 (the CTO's one send)
answering the CVO's slug REMEDIATION_v2 @b3acbcf3dd, cited in each order's authority chain. comp-blast
DECLARED-NOT-APPLICABLE (no infra act; no served-output move -- rb-2 tests a consumer READ, it does not
move a served key). L4-R: the PRD is GRANDFATHERED (predates the L4-R law commit f8337502a9) -- no new
sign-off cycle and no prd_version bump (this is a round-analysis answer, not a PRD addendum).

**PUSH STATE: this amendment is LOCAL.** 0.0.0_AB_MSTR~Z holds the push window.

*(v0.4 amended 2026-09-11 by 2.0.0_SA_COO~ZZZ -- the L10 round-2b recut from @c48576bf85; rounds 1-2
sections 1-10 unchanged.)*

## 12. ROUND 4 (v4) -- from the L10 round-3 analysis @38948db85c (1.0.0_SA_CTO~Z)

**v0.5 IS AN L10 RECUT closing the consumer-wiring so C-S16 closes, NOT a new decomposition.** Round 3
(the "rb-" corrective continuation, canonical v3 per the CTO carrier ruling @21336) graded 4 PASS / 1 FAIL:
rb-10 salience, rb-12 identity note, rb-15 impostor predicate, rb-1 fiscal direction all LANDED
(C-S12/C-S13/C-S14/C-S15 DISARMED/REMEDIATED). rb-2 (consumer-wiring, C-S16) FAILED -- a GOOD fail: the
consumer-wiring-as-its-own-AC (the CTO tick-2 generalization) caught that the overlay silently reverts to
the stale served price when the corrected fiscal row is UNRESOLVED (the rb-1 x rb-2 interaction). The CVO's
L8/L9 control surfaced two findings. **0 of 14 FWDs newly REALIZED -- the surfaces are still unserved.**
This section ADDS the two round-4 cells; rounds 1-3 are FROZEN and terminal. C-S16 stays OPEN until this holds.

**NONE IS DESIGN_SPEC-GATED** (analysis + slug): consumer-code / provenance correctness, doable now without
a .tsx. The surface exercise is a LATER round (v5+), still on Andrew's DESIGN_SPEC + the four words.

**RULING @21343 (1.0.0_SA_CTO~Z, folded in before rc-19 was worked).** rc-19 (C-S19) is fixed as an S11
QUALIFICATION RULE (class-level -- the "corrected-overlay unresolved" figure class in lib/research/rules/
figure.py -> S10 REFUSE/PROVISIONAL), NOT a bespoke fallback inside load_corrected_price_overlay (Rule 22:
fix what the members share; a bespoke fix is the next-consumer gap the CRO's holes-scan flagged). rc-19's
<paths> accordingly grant lib/research/rules/ + lib/research/checkface/. rc-20 (C-S20) stays its own fix,
framed as EXTENDING S3's provenance vintage/source handling, kept separate from rc-19.

### 12a. The two round-4 cells

M = ONE dependency chain: rc-19 -> rc-20, both editing the SAME consumer functions
(lib/research/provenance/render_print.py's `load_corrected_price_overlay`/`apply_corrected_price_overlay`/
`render_figure_line` and lib/research/print/render_pack.py's `load_model_block`), so serialized to one
worker. `fanout: 1 of 1, cap 8`. Ids match CELL_ID_RE; cell ids are free-form, the ROUND integer is 4.

| cell | fixes | finding | FWD | the defect (analysis @38948db85c; CVO evidence @13ae38f3f89b) | the engine, and its bound |
|---|---|---|---|---|---|
| `AMGT-rc-19` | `AMGT-rb-2` | C-S19 (BLOCKING) | FWD-1, FWD-3 | `load_corrected_price_overlay` keeps only rows whose price is not None, and `apply_corrected_price_overlay` `continue`s on a missing year -- so an UNRESOLVED corrected fiscal row (rb-1 now returns None for a future-only price) is DROPPED and the consumer silently keeps the OLD calendar price (BABA FY2025 146.58) UNMARKED, presented as trusted. Control: period_end 2025-03-31 with only a 2025-04-02 price -> corrected None -> loader {} -> render retains 146.58, no marker. | THE UNRESOLVED-ROW CONTRACT. Preserve explicit UNRESOLVED corrected rows; DISTINGUISH missing-lane/year (corrected lane absent for this year) from resolved data; MARK or REFUSE a fiscal price that has NO valid corrected evidence -- the calendar price may remain in source storage but NEVER silently regains trusted presentation. Test the NAMED consumer from a full corrected-join None output straight through to the RENDERED value. Home: `lib/research/provenance/`, `lib/research/print/`. Bound: STORE_CONTRACT rule 1 (original model_block byte-unchanged); NO new vendor call; the resolved 132.23 sample still renders correct. |
| `AMGT-rc-20` | `AMGT-rb-2` | C-S20 (OBSERVATION) | FWD-1, FWD-3 | `apply_corrected_price_overlay` replaces `fig.vintage` with the price OBSERVATION DATE (price_date) and drops the corrected artifact's derivation key (derived/model_block_fye/<sec>/<stamp>/model_block_fye.json); `render_figure_line` hardcodes "Bloomberg" and never emits `fig.source`. So observation date substitutes for vintage and the derivation identity is lost. | THE VINTAGE/DERIVATION IDENTITY. Carry OBSERVATION DATE and DERIVATION/LANDING IDENTITY as DISTINCT fields; retain the exact corrected artifact key (or an equivalent immutable pin) through the consumer and its provenance render; `render_figure_line` emits `fig.source`, never a hardcoded vendor. Add a test DISTINGUISHING two derived vintages that share one observation date. Home: `lib/research/provenance/`, `lib/research/print/`. DEPENDS ON rc-19 (same functions). Bound: within rb-2's own named-vintage acceptance; NO new vendor work; STORE_CONTRACT rule 1 holds. |

### 12b. Rule 24 record for what v0.5 ADDS (the two round-4 cells)

- **(i) MECE over the DECLARED domain = the analysis's round-4 recut set.** SUBTRACTION, not recall: the
  analysis routes exactly C-S19 (BLOCKING) + C-S20 (OBSERVATION) to close C-S16; the four round-3 PASSes are
  terminal, the surface exercise is a later round (Andrew's). No third cell, no dropped item.
- **(ii) SAME GRAIN:** each is one cell fixing one named consumer-wiring finding.
- **(iii) INTENT COHERENCE:** two distinct axes kept separate -- rc-19 unresolved-row SAFETY, rc-20
  vintage/derivation IDENTITY. Neither mixes the other's concern.
- **(iv) STATE COHERENCE -- what these do NOT move:** they close the consumer-wiring contract so the served
  pack reads the corrected join HONESTLY (unresolved marked, vintage distinct); they do NOT make an
  EXERCISED FWD REALIZED (that needs the served .tsx -- a later round). C-S16 closes when rc-19 + rc-20 land.

### 12c. Round-3 lessons absorbed into this cut

- **A consumer-wiring AC must exercise the UNRESOLVED path, not only the happy path.** rb-2's test proved the
  resolved BABA row reads 132.23, but never drove a None-corrected row through -- so a silent stale-price
  revert passed. rc-19's AC drives a FULL corrected-join None output straight to the rendered value.
- **An overlay that mutates a figure must not leave a stale value wearing a trusted face.** Marking/refusing
  an unresolved figure is the contract; silently keeping the old value is the C-S19 defect.
- **Observation date != vintage != derivation identity** -- three distinct provenance facts; collapsing any
  two loses auditability (C-S20). Carried from [[a-value-must-carry-its-claim]].
- Carried from prior rounds: every criterion DISCRIMINATES (a difference arm); the proof instance uses the
  FULL task-order stem filename; a criterion names the instrument that OBSERVES the artifact; an integration
  cell's <paths> names the CONSUMER's home (rc-19/rc-20 grant lib/research/print/ + lib/research/provenance/
  from the start -- the rb-2 cut-defect absorbed).

### 12d. The round axis, updated

- **ROUNDS 1-3:** terminal, frozen (v1 build; v2 defect fixes; v3 the rb- corrective continuation, 4 of 5
  landed).
- **ROUND 4 (v4, RECUT, 2 cells):** `AMGT-rc-19` -> `AMGT-rc-20`, one two-cell chain, one worker (slot ~1),
  serialized. `fanout: 1 of 1, cap 8`. rc-19 spawns at issuance; rc-20 handed after rc-19 lands.
- **SURFACE EXERCISE (v5+, deferred on Andrew's gate):** the .tsx that serves each FWD, cut only after the
  DESIGN_SPEC approval + the four words. NOT cut now, NOT pinned to a number.

**PREFLIGHT for the round-4 recut:** the mandatory core battery is NOT re-run -- v0.2's run stands and no
round-4 cell touches a new gate/IAM/adversary/vendor surface (both edit landed consumer modules against
landed data). The authority is the L10 round-3 analysis @38948db85c (the CTO's one send) answering the CVO's
slug REMEDIATION_v3 @13ae38f3f89b, cited in each order's authority chain. comp-blast DECLARED-NOT-APPLICABLE
(no infra act; the served pack's .tsx is not built, so no live served artifact moves -- but the consumer's
rendered figures change, flagged to the CVO for the L9 grade). L4-R: the PRD is GRANDFATHERED (predates the
law commit f8337502a9) -- no sign-off cycle, no prd_version bump.

**PUSH STATE: this amendment is LOCAL.** 0.0.0_AB_MSTR~Z holds the push window.

*(v0.5 amended 2026-09-11 by 2.0.0_SA_COO~ZZZ -- the L10 round-4 recut from @38948db85c; rounds 1-3 sections
1-11 unchanged.)*

---

## 13. ROUND 5 (v5) -- THE SURFACE ROUND, from the L10 round-4 analysis @959ba3e947 (`1.0.0_SA_CTO~Z`)

**v0.6 IS THE SURFACE CUT, AND IT IS THE FIRST ROUND OF THIS PROJECT WHOSE DECLARED DOMAIN IS NOT A REMEDY
SET.** Rounds 1-4 were pre-surface correctness work: round 4 graded 2 PASS / 0 FAIL, closed `C-S16` with
its children `C-S19`/`C-S20`, and is terminal at L10. **28 of 28 orders terminal, 0 open, 0 of 15 FWD
REALIZED** -- correct, because no surface is built and fourteen of the fifteen outcomes carry `EXERCISED`
bars that no build can close. This section ADDS the eight round-5 cells; sections 1-12 are FROZEN.

**THE DOMAIN IS ANDREW'S APPROVED SURFACE, NOT THIS LANE'S READING OF WHAT IS LEFT.** PRD s.3b
(ANDREW-DIRECT 2026-09-11 ~12:1xZ, "Recs approved") plus the S16 manifest row. `C-DESIGN-SPEC-FIRST` IS
LIFTED for this project, so `.tsx` is authorized in this round and the `AMGT-s-5` .tsx phase is released.

**HIS STATED ORDER IS A BOUND, NOT A SUGGESTION: "the box + both tables, TABLES FIRST."** The edges below
encode it; no cell may be re-sequenced ahead of it by a worker.

### 13a. What the L4-R gate said at this cut, because this round is the first to pass through it

`python .tools/prd-signoff.py status AMGT_RESAPP` -> **ADMITTED** at `@f0ff95cfac`; ratified-text SIGNED
`3.0.0_SA_CVO~Z` half `4eb997ed71ee`; brief SIGNED `4.0.0_SA_CRO~Z` half `26f942429c6a`.

BUT: **`ADMITTED` ALONE DID NOT AUTHORIZE THIS CUT AND MUST NOT AUTHORIZE THE NEXT ONE.** Row
`AMGT_RESAPP-Z-S6` (`1.0.0_SA_CTO~Z` @`65ab345826`) measured the gate printing "brief SIGNED current" while
the brief half's bytes had moved, because `prd_signoff_lib.evaluate()` falls back to `prd_version` equality
for any record carrying no `half_hash`. This lane therefore cut only after a SECOND, independent limb:
a `prd/signoff/4.0.0_SA_CRO*.json` record carrying a `half_hash` **equal to the brief half's CURRENT hash**
(`26f942429c6a`), found in the LANE file `4.0.0_SA_CRO~Z.json`. The BASE file `4.0.0_SA_CRO.json` is still
old-format and still returns MATCH=False -- a base-path-only check would have refused this cut.
WARN: **The general defect is NOT fixed and is NOT claimed fixed** (`prd_signoff_lib` untouched by anyone;
2 of this project's 3 signoff records are old-format; the estate-wide census is uncounted). The instance is
repaired BY ADDITION -- the defective carrier is still in the directory and would decide again if the lane
file were removed, renamed, or written under a different serial spelling.

### 13b. The eight round-5 cells

**M = TWO dependency-independent chains, MEASURED. `fanout: 2 of 2 chains, cap 8`** -- the two TABLE cells
are the only roots, they are the two chains' heads, and both spawn at issuance (his "TABLES FIRST").

| cell | row | outcome | act (the engine, and what binds it) | state | deps |
|---|---|---|---|---|---|
| `AMGT-rd-1` | S4, S13 | FWD-4, FWD-11 | **THE ARTICLE STORE.** NEW DynamoDB table `opal-amgt-articles`, shaped like `opal-news-articles` (title/source/url/published_at/sentiment) PLUS `ticker`/`security_key` (via S12) and `platform`. Terraform in `infra/aws/terraform/amgt-resapp/` via `safe-apply`, change-management entry OPENED BEFORE the act and closed before the grading read. **GENUINELY SEPARATE** from `opal-news-articles` (not that table with a filter) and from `opal-data-research`. MEASURED ABSENT on the live plane at this cut (row `Z-S5`: 0 hits across 2445 aws nodes) -- a genuine create, not an integration. | OPEN | -- (ROOT) |
| `AMGT-rd-2` | S16 | FWD-15 | **THE METRICS STORE.** NEW DynamoDB table `opal-amgt-security-metrics` holding PRE-COMPUTED per-ticker ranking rows, mirroring the proven `opal-news-articles` / `opal-news-trending-daily` split. Same Terraform module, same `safe-apply` + ledger discipline. MEASURED ABSENT at this cut. The Lead Panel READS it and never re-derives a ranking at render time (`C-SERVER-SIDE-RANKING`). | OPEN | -- (ROOT) |
| `AMGT-rd-3` | S16 | FWD-15 | **THE HARVESTER BOX + ITS OWN IAM ROLE.** NEW EC2 box in `infra/aws/terraform/amgt-resapp/` following the ASTN_WSJFT SHAPE (stopped-between-runs, SSM-woken) but with **AMGT_RESAPP's OWN IAM role** and write access to `opal-amgt-articles` -- **explicitly NOT the ASTN_WSJFT box and not its role.** ONE shared box for all four harvesters. Refresh MUST WAKE the stopped box (SSM / `inf-jwt-trigger` shape) or it silently no-ops -- the wake is part of the cell, not a follow-up. `comp-iam service` at Phase 1 and `comp-iam gaps` at Phase 2 (auto-rule 3; `iam.tf` changes). | OPEN | `rd-1` |
| `AMGT-rd-4` | S4, S13 | FWD-4, FWD-11 | **THE FOUR HARVESTERS** (Seeking Alpha, FT, Bloomberg, WSJ) writing per-ticker article content into `opal-amgt-articles`. Each admits an item by the news/social rule `AMGT-s-11` states, and resolves the platform's OWN identifier through S12 BEFORE dispatch (SA symbol-slug, Bloomberg `"TICKER US Equity"`, FT id) -- never a bare ticker. Raw vendor bytes land before derivation. | OPEN | `rd-3` |
| `AMGT-rd-5` | S16 | FWD-15 | **THE CHATTER AXIS WRITER.** A SCHEDULED PRODUCER computing the chatter ranking daily and writing pre-computed rows to `opal-amgt-security-metrics`. Axis = the committed chatter gate: 30-day window, 0-100 normalized, `TOP_N=10`. | OPEN | `rd-2` |
| `AMGT-rd-6` | S16 | FWD-15 | **THE PRICE AXIS ENGINE, BOX-SIDE.** The price ranking reads Bloomberg historical/intraday and therefore runs in the **BOX-SIDE puller shape** (the ETF-daily-pull shape), **NOT a Lambda calling Bloomberg** (`C-PRICE-RANKING-BOXSIDE`). 30-day window, matching chatter -- Andrew unified both to 30. Writes pre-computed rows to the same metrics table. **The BOX-SIDE host is the BLOOMBERG TERMINAL box (loopback DAPI, the ETF-daily-pull shape), NOT the new harvester EC2 box of `rd-3`** -- the harvester box hosts the four ARTICLE harvesters, which is a different machine and a different concern. | OPEN | `rd-2` |
| `AMGT-rd-7` | S16 | FWD-15 | **THE STARRED WATCHLIST.** SHARED ACROSS THE FIRM -- both PMs see the same starred names, keyed PER-FIRM, not per-user (`C-STARRED-PER-FIRM`, Andrew-ruled, reversible to per-user on his word). **Starring is a PURE MARKER:** it triggers NO refresh and queues NO harvester. Refresh is its own explicit action and the cell must prove the two are not wired together. | OPEN | `rd-2` |
| `AMGT-rd-8` | S16 | FWD-15 | **THE SURFACE ITSELF.** The `.tsx`: a persistent **Lead Panel** (universe discovery -- Trending/Breakout x Price/Chatter, List/Chart, Security overlay, Starred) above **three tabs: Thesis / Peers / Coverage**. **Print is a header export action**, not a tab. **The Model tab is CUT and its figures REHOMED** into Thesis and the Security overlay. Reads pre-computed rows from **`opal-harvest-security-metrics`** (RENAMED 2026-09-11 ~20:1xZ from `opal-amgt-security-metrics`, which is DROPPED -- 42 rows migrated and verified on FULL ITEM EQUALITY; env knob `HARVEST_METRICS_TABLE`); never re-derives a ranking at render time. | OPEN | `rd-5`, `rd-6`, `rd-7` |

### 13c. Rule 24 record for what v0.6 ADDS (the eight round-5 cells)

- **(i) MECE over the DECLARED domain, BY SUBTRACTION from a printed denominator -- not by recall.**
  ⚠ **AMENDED 2026-09-11 ~18:4xZ. THIS RECORD WAS TRUE AT EIGHT CELLS AND BECAME FALSE THE MOMENT `rd-3`
  AND `rd-4` WERE SUPERSEDED. It is repaired in the SAME commit as that supersede, deliberately: a
  subtraction record that is quietly falsified is WORSE than no record, because it still prints a clean
  remainder and every later reader trusts it.** The pre-amendment text mapped `C-HARVESTER-COMPUTE` to
  `rd-3` + `rd-4` and `C-VENDOR-WORD-HARVESTERS` to a bound on `rd-4`; both of those homes are gone.
  THE DOMAIN IS UNCHANGED -- the SIX named constraints of PRD s.3b plus the S16 manifest row. What changed
  is where two of them are SERVED. Subtracting what each cell covers:
  `C-AMGT-ARTICLES-STORE` -> `rd-1`; `C-SERVER-SIDE-RANKING` -> `rd-2` (the store) + `rd-5` (its writer);
  `C-PRICE-RANKING-BOXSIDE` -> `rd-6`; `C-STARRED-PER-FIRM` -> `rd-7`; the approved page shape + S16 ->
  `rd-8`. **THAT IS FIVE CONSTRAINTS OVER SIX CELLS.**
  ⛔ **THE REMAINING TWO ARE NOT UNCOVERED -- THEY ARE RE-HOMED OUTSIDE THIS ROUND, AND THE DIFFERENCE IS
  THE WHOLE POINT OF SAYING SO:**
  `C-HARVESTER-COMPUTE` -> **THE HARVEST ESTATE**, owned and executed by `4.0.0_SA_CRO~Z` per PRD v0.5
  @`5517e071e8` on Andrew's ~17:3xZ directive and his ~18:3xZ approval of the draw. It maps to NO round-5
  cell and must not be re-cut here.
  `C-VENDOR-WORD-HARVESTERS` -> re-homed onto the harvest estate's ACQUISITION surface **with all three
  limits intact** (the four named platforms; THIS project's harvesters only; not before the box stands).
  It was previously a time-scoped BOUND on `rd-4` and had no cell of its own, so superseding `rd-4` would
  have left it with NO CARRIER AT ALL -- found by `1.0.0_SA_CTO~Z` while verifying this very record, and it
  is the sharper half of this amendment. Andrew's "full egress and override authority" is authority to
  REALIZE THE ESTATE and is **NOT** a widening of `C-VENDOR-EGRESS`.
  **REMAINDER ZERO over the six constraints, now stated as FIVE SERVED IN-ROUND + TWO RE-HOMED, rather
  than as a single number that hides where the members went.**
- **(ii) SAME GRAIN:** each cell is one engine with one home. The two stores are separate cells because
  they are separate tables with separate consumers, not one "make the tables" cell.
- **(iii) INTENT COHERENCE:** one axis per cell. Storage (`rd-1`, `rd-2`), ranking production (`rd-5`,
  `rd-6`), marker state (`rd-7`), presentation (`rd-8`). ⚠ AMENDED: compute host (`rd-3`) and acquisition
  (`rd-4`) left this round with the harvest estate. The original separation of the BOX from the HARVESTERS
  that run on it stands as a design point and now applies inside that estate rather than here.
- **(iv) STATE COHERENCE -- what these do NOT move:** they build the surface, so for the first time an
  `EXERCISED` bar becomes REACHABLE -- but **REACHABLE IS NOT REALIZED.** No cell may grade its own FWD
  REALIZED on the strength of its own artifact; fourteen of fifteen outcomes need a PERSON to have used the
  thing, which is L9's to grade and never L7's. They do NOT close `FWD-9` (APPLIED, the drafting face) and
  do NOT touch rounds 1-4's landed correctness work.

### 13d. BOUNDS carried onto the round-5 cells

- **`C-VENDOR-WORD-HARVESTERS` -- RE-HOMED 2026-09-11 ~18:4xZ, AND THIS IS THE BOUND THAT ALMOST VANISHED.**
  ⚠ It had NO cell of its own: it was carried here as a time-scoped BOUND ON `rd-4`, deliberately, so the
  s.13c subtraction balanced visibly. **Superseding `rd-4` would therefore have left it with NO CARRIER AT
  ALL** -- found by `1.0.0_SA_CTO~Z` while verifying s.13c, and it is the sharper half of this amendment.
  IT IS NOW RE-HOMED onto the HARVEST ESTATE's acquisition surface per PRD v0.5 @`5517e071e8`, **with all
  three limits intact and none of them softened by the move:** the FOUR named platforms (Seeking Alpha, FT,
  Bloomberg, WSJ); **THIS project's harvesters only**; and **effective only once the box is stood up and
  ready to run -- NOT before.**
  ⛔ **ANDREW'S "FULL EGRESS AND OVERRIDE AUTHORITY" TO `4.0.0_SA_CRO~Z` IS AUTHORITY TO REALIZE THE ESTATE
  AND IS NOT A WIDENING OF `C-VENDOR-EGRESS`.** Written down rather than assumed, because a narrow
  time-scoped grant losing its carrier at the same moment another seat is handed broad-sounding egress
  language is exactly the shape in which it quietly becomes a blanket one, and nobody would see it happen.
  ⛔ **A PROXY VENDOR IS A SEPARATE, UNANSWERED QUESTION.** Extending Bright Data Web Unlocker from WSJ to
  the session harvesters is a NEW per-use call for Andrew -- never an inference from an EC2 IP proving
  unworkable against PerimeterX. `C-VENDOR-EGRESS` still binds every other vendor and every other use, and
  "availability is not authorization" is unchanged.
- **NO MONITOR, NO ALARM, NO FRESHNESS-CHECKER** (standing moratorium; `comp-schedule` carrier C3 counts 12
  standing NEVER clauses). `rd-5` and `rd-6` are SCHEDULED PRODUCERS, which is not only permitted but
  required ("production pipelines MUST be scheduled"); a producer that computes a ranking is not a monitor.
  STOP: neither cell may add an alert, an SNS topic, an SES send or a freshness checker on top of its output.
- **`opal-data-research` -- SUPERSEDED AND NOW LANDED. THE RENAME IS DONE: IT IS `opal-data-harvest`.**
  Andrew ruled at ~18:5xZ that harvest naming reaches this bucket ("better to have all of this stuff grouped
  by name right from the start"); `4.0.0_SA_CRO~Z` executed the migration and closed its ledger at
  ~20:1xZ -- 53 objects copied with the key grammar preserved and verified, the five live consumers flipped,
  the source dropped. THE EARLIER TEXT HERE SAID "about to move" AND THAT IS NOW THE STALE HALF; it is
  corrected rather than left, because a round-6 cutter reading a bound that says a resource is MOVING learns
  nothing about where it went.
  ⛔ **THE CURRENT NAMES, so no cell has to re-derive them** (`4.0.0_SA_CRO~Z`'s map, msg 21608):
  `opal-data-research` -> **`opal-data-harvest`**; `opal-amgt-articles` -> **`opal-harvest-articles`**;
  `opal-amgt-security-metrics` -> **`opal-harvest-security-metrics`**;
  `infra/aws/terraform/research/s3.tf` -> `infra/aws/terraform/harvest/s3.tf` (the old module is RETIRED, so
  a citation to it resolves to nothing). Env knobs: `HARVEST_BUCKET`, `HARVEST_ARTICLES_TABLE`,
  `HARVEST_METRICS_TABLE`.
  WHAT STILL HOLDS UNCHANGED: no cell of this project re-creates, re-declares or re-configures any of them,
  and none performs a migration -- those acts belong to the harvest estate.
  ⛔ **RE-MEASURED ON THE LIVE PLANE AT 2026-09-11 ~20:5xZ, AGAINST `opal-data-harvest` ITSELF** -- the
  earlier configuration line in this section was measured on `opal-data-research`, WHICH NO LONGER EXISTS,
  so it was a true statement about a dead object. Existence and access measured SEPARATELY, per the S5
  binding:
  IDENTITY `arn:aws:s3:::opal-data-harvest`, **us-east-1**, not an access-point alias.
  ACCESS **PROVEN, not assumed** -- `list-objects-v2` RETURNED KEYS, e.g.
  `derived/model_block/BABA_US_Equity/20260910T224432Z/model_block.json`; head-bucket rc=0 alone would
  have proved only that the NAME RESOLVES.
  ⭐ **AND THE TIMESTAMPED KEY GRAMMAR SURVIVED THE MIGRATION**, which is the property FWD-6's accumulate
  bar actually reads.
  CONFIGURATION: versioning **Enabled**; SSE **AES256**; **NO lifecycle** (`NoSuchLifecycleConfiguration`
  -- accumulation is not silently truncated); **NO bucket policy** (`NoSuchBucketPolicy` -- IAM-only).
  NEGATIVE CONTROL, so the reads are known to discriminate: `head-bucket opal-data-research` now returns
  **404 Not Found**. The instrument returns real data for one name and nothing for the other.
  EVERY DIMENSION MATCHES what this section asserted of the old bucket -- the migration preserved the
  configuration -- but it is now MEASURED rather than inherited.
  WHAT STILL HOLDS UNCHANGED: no round-5 cell re-creates, re-declares or re-configures it, and none of them
  performs the migration -- that act is the harvest estate's.
  Measured at the round-5 cut and still true of the source bucket: versioning **Enabled**, SSE AES256
  (SSE-C blocked), **no lifecycle**, **no bucket policy** (IAM-only), us-east-1, list access PROVEN by a
  successful `list-objects-v2`. Created by this project's own `AMGT-s-6` @`20260910T2059Z` via `safe-apply`.
  ⛔ **AND THE RENAME HAS CODE CONSUMERS, NOT ONLY DATA -- row `Z-S12`.** 12 DEF-band definitions of the
  bucket name across a printed denominator of 56,351 files; **ELEVEN are hardcoded literals with no env
  path** and six of those are LIVE round-1..4 modules. Exactly ONE is re-pointable by an environment
  variable. A cell of this round that reads a research-store path must expect the name to move under it,
  and `rd-5`'s producer is SCHEDULED daily -- so a rename landing between two fires breaks the next one at
  RUN time, not at apply time.
- **S12 RESOLVES EACH PLATFORM'S OWN IDENTIFIER BEFORE DISPATCH.** `rd-4` never dispatches on a bare ticker.
  This is the direct carry-forward of F6 (48 of 54 packs with a foreign peer set) -- **cutting an
  acquisition cell ahead of identity rebuilds that defect on a new axis.**
- **EVERY INFRA CELL: change-management entry OPENED BEFORE the act and CLOSED before the grading read;
  `safe-apply`, never bare `terraform apply`; no second output path beside the one table.**
- **NO NON-ASCII** in code, logs or AWS. Every F-number is CITED, not CONFIRMED -- a cell relying on one
  re-measures it first and its criterion says so.

### 13e. Round-4 lessons absorbed into this cut

- **A cut may not rest on a gate's green when a row says the gate lies.** 13a is this lesson applied to the
  cut itself: the two-limb precondition exists because `Z-S6` measured a false green THIS ROUND, and
  `to-pipeline-gate` LIMB 6 reads the same false green, so it could not have been the backstop.
- **An id is minted from a RE-READ, never from recall.** Row `Z-S7` was minted by this lane from "S5 mine,
  S6 the CTO's, so S7 next" and collided with `4.0.0_SA_CRO~Z`'s committed `Z-S7`. Re-enumerating at write
  time gives the lowest free id; recall does not. The same applies to cell ids in this table.
- **An uncommitted channel row is an ESTATE-WIDE OUTAGE, not a personal todo** -- the standing-corpus pass
  reads the WORKTREE and is fail-closed, so it blocked a peer's unrelated drain. The window between
  appending a row and committing it is a shared-resource window.
- **An invented schema field is a violation even when it looks harmless** (`additionalProperties: false`
  rejects the KEY, and no value satisfies it). Rule 24 binds a schema ADOPTED as hard as one authored.
- Carried from prior rounds: every criterion DISCRIMINATES; the proof instance uses the FULL task-order stem
  filename; a criterion names the instrument that OBSERVES the artifact; an integration cell's `<paths>`
  names the CONSUMER's home.

### 13f. The round axis, updated

- **ROUNDS 1-4:** terminal, frozen. 28 of 28 orders complete; round 4 CLOSED at L10 @`959ba3e947`.
- **ROUND 5 (v5, THE SURFACE ROUND) -- AMENDED 2026-09-11 ~18:4xZ: SIX cells, was EIGHT.**
  `rd-3` and `rd-4` are SUPERSEDED by the harvest estate (PRD v0.5 @`5517e071e8`); CHAIN A is therefore
  `rd-1` ALONE and terminal. The round did not lose coverage -- `C-HARVESTER-COMPUTE` and
  `C-VENDOR-WORD-HARVESTERS` are RE-HOMED, see 13c(i) and 13d.
  **AS ISSUED (the historical record, not the current shape):** roots `rd-1` and `rd-2` spawned at issuance
  (TABLES FIRST); CHAIN A was `rd-1` -> `rd-3` -> `rd-4`; CHAIN B `rd-2` -> {`rd-5`, `rd-6`, `rd-7`} ->
  `rd-8`; `fanout: 2 of 2 chains, cap 8`.
  **AS IT STANDS:** `rd-1`, `rd-2`, `rd-5`, `rd-6` terminal; `rd-7` in flight; `rd-8` last, converging
  `rd-5`/`rd-6`/`rd-7`.
  ⚠ **`rd-7` WAS RE-SLOTTED ~2 -> ~7 AND `rd-6` ~2 -> ~6, BOTH BY COMMITTED AMENDMENT BEFORE THEIR SPAWNS**
  (@`b67133bd80`, @`f3501860e8`). The queue positions were an ISSUER choice about worker slots, not edges in
  the dependency set; the edges are unchanged. The serial is part of the `<paths>` GRANT under RULING 1, so
  it moves in the FILE and never only in a spawn prompt.
- WARN: **THE ROUNDS ARE A READING OF THE EDGES, NOT A SECOND SOURCE OF TRUTH.** If a cell lands early the
  next becomes cuttable early; the edges govern, the round numbers describe.
- **AFTER ROUND 5:** `REALIZED` still requires a PERSON to have exercised each surface. Round 5 makes that
  reachable and does not achieve it; the project closes when every FWD grades REALIZED at L9.

**PREFLIGHT for the surface round -- the mandatory core battery WAS RE-RUN, and this is the first round
since v0.2 that could not carry the prior run forward:** round 4 declared it not-re-run because both cells
edited landed consumer modules; round 5 creates two DynamoDB tables, an EC2 box and a NEW IAM role, adds
server-side ranking routes and introduces new portal query keys, so every lens becomes applicable again.
- `comp-schedule --drift` -- RUN. 5 of 5 carriers scanned; REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20
  C5=334. 2 gates ARMED as drift candidates (`G-3` owner CTO, `G-7` owner POD4) -- **neither is this
  project's and neither blocks this cut.** C3's 12 standing NEVER clauses are the source of 13d's
  no-monitor bound.
- `comp-iam gaps` -- RUN. 836 call(s) verdicted across 96 mapped role(s); 12 missing, 291 deny-present, 1
  coverage-unknown, 2 resource-mismatch across 31 services. **No AMGT role exists yet**, which is the honest
  baseline for `rd-3` (the cell creates the first one). WARN -- COVERAGE LIMIT carried, not cleared: 630
  UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services NOT resource-checked, and 51 GRANTED-BROAD
  rows EXCLUDED rather than cleared -- a wildcard grant cannot be falsified by a resource check.
- `comp-cache collisions` -- RUN. 415 of 415 files scanned. Every existing collision is on another surface
  (market-performance, model-portfolio, partner-analytics, positioning); **no AMGT/research key exists**, so
  `rd-8` enters a clean namespace and its new keys must be checked at Phase 1 (auto-rule 2).
- `comp-routes behaviors` -- RUN. 27 behaviors; the auth-gated `/api/scoped/*` + `auth-validator-edge`
  viewer-request pattern is the precedent `rd-8`'s reads follow.
- `comp-blast` -- DECLARED-NOT-APPLICABLE AT THE CUT, with the reason: round 5 CREATES resources rather than
  modifying shared ones, and no live served artifact moves at L5. STOP: it becomes APPLICABLE inside
  `rd-8`, which edits the portal shell, and that cell carries it at Phase 1.
- `comp-adversary` -- RUN on this file; the declaration at section 7 stands and is extended by 13a's
  statement of what the gate could and could not tell this lane.

**AUTHORITY:** the L10 round-4 analysis @`959ba3e947` (the CTO's one send) answering the CVO's slug
`REMEDIATION_v4`@`b97837e7fe`, plus PRD s.3b (ANDREW-DIRECT 2026-09-11 ~12:1xZ) and the L4-R ADMITTED gate
at `@f0ff95cfac` with the second limb of 13a. Cited in each order's authority chain.

**PUSH STATE: this amendment is LOCAL.** `0.0.0_AB_MSTR~Z` holds the push window.

### 13g. AMENDMENT v0.6.1 -- `/dispatch --plan` caught a WRONG EDGE and a wrong fan-out, BEFORE any order was issued

**This amendment is legal because NO ORDER IS ISSUED AND NO WORKER IS SPAWNED.** Rule 27's freeze binds
the decomposition MID-ROUND; between L5 and L6 with an empty `task-orders/` set for this round, a
correction is still an L5 act. Issuing against a knowingly-wrong edge would have been the worse choice.

**WHAT `--plan` MEASURED:** under the skill's own definition of M ("two cells joined by an edge are one
chain"), the v0.6 edge set formed **ONE connected component, not four chains** -- so the stated
`fanout: 2 of 4` was wrong, and taken literally it implied N = M = 1 and one worker serializing all eight
cells, which contradicts Andrew's "TABLES FIRST".

**THE CAUSE WAS A SUBSTANTIVE ERROR, NOT AN ARITHMETIC ONE.** v0.6 gave `rd-6` (the price axis) a
dependency on `rd-3` (the harvester box). That edge is WRONG on the constraint's own words:
`C-PRICE-RANKING-BOXSIDE` names the **ETF-daily-pull shape**, which runs on the **Bloomberg TERMINAL
box** against a loopback-only DAPI -- the same seam `AMGT-s-2` exists to cross. The NEW EC2 box of `rd-3`
hosts the four ARTICLE harvesters. Two different machines, two different concerns; the edge conflated
"box-side" with "the box this round builds". Removing it yields **M = 2**, which is what the two
independent roots were always going to be.
WARN: the wrong edge would ALSO have mis-scoped `rd-6`'s worker face -- it would have named the harvester
box's home in `<paths>` and omitted the terminal box's, and under RULING 1 a path missing from the order
is a WALL, not a hint. So this was on its way to a blocked worker, not just a wrong number.

**THE GENERAL FINDING, worth more than this instance:** rounds 1-4 were either INDEPENDENT cells (round 2:
5 of 5) or a single PATH (round 4: 1 of 1), and for both shapes "connected components" and "worker queues"
give the same number. **Round 5 is this project's first CONVERGENT DAG** -- two roots meeting at `rd-8` --
and it is the first shape where the two readings diverge. A fan-out number copied forward in the shape of
earlier rounds is exactly where that divergence hides.

*(v0.6.1 amended 2026-09-11 by `2.0.0_SA_COO~ZZZ` before issuance -- one wrong edge removed, M re-measured
2, fan-out corrected. Sections 1-12 unchanged and FROZEN.)*

*(v0.6 cut 2026-09-11 by `2.0.0_SA_COO~ZZZ` -- the SURFACE round from @959ba3e947; sections 1-12 unchanged
and FROZEN.)*


## 14. ROUND 6 (v0.7) -- THE RECUT OF `AMGT-rd-8`, ONE CELL

**Cut 2026-09-11 ~22:2xZ by `2.0.0_SA_COO~ZZZ` on `1.0.0_SA_CTO~Z`'s L10 assessment (msg 21677).**
`AMGT-rd-8` was adjudicated FAIL on TWO criteria by `3.0.0_SA_CVO~Z` (`ADJUDICATION_v5.md`:
`AMGTrd8-AC4` FAIL, `AMGTrd8-AC2` FAIL). ⛔ **AN ADJUDICATED FAIL IS A CONCLUDED ATTEMPT WITH A
NEGATIVE VERDICT, NOT WORK IN FLIGHT** -- so L9 RELEASES the recut and `rd-8` does not wait for the
slug. `rd-8` flips to **`superseded`**, never `complete`: that word reads as success and this attempt
failed. The pointer is `AMGT-re-1`, the same shape `rd-3`/`rd-4` already carry @`64ce3b3c55`.

### 14a. The cell

| cell | rows | FWD | text | status | depends on |
|---|---|---|---|---|---|
| `AMGT-re-1` | S16 | FWD-15 | **THE SURFACE, RECUT.** Everything `AMGT-rd-8` was asked for, MINUS what it delivered, PLUS the four shape gaps L9 named and the two instruments it could not be graded on. Reads pre-computed rows from `opal-harvest-security-metrics`; never re-derives a ranking at render time. | OPEN | none -- `rd-5`, `rd-6`, `rd-7` are complete and drained |

### 14b. WHAT THE RECUT CARRIES, AS A SUBTRACTION FROM L9's OWN FAIL TEXT

⭐ **NOT re-derived from a summary.** `ADJUDICATION_v5.md`'s `AMGTrd8-AC4` reason names exactly what is
present and what is missing, and 14b is that text partitioned:

**ALREADY DELIVERED AT `e6057f26` AND NOT TO BE REBUILT** -- L9: *"the persistent panel, three tabs and
header Print location are present"*. The recut KEEPS them. 20 files / 2,067 insertions are on branch
`wk-amgt_resapp-5-8-portal` in the MAIN portal repo, anchored there by an explicit fetch before the
`rd-8` teardown (row `Z-S21`). **THE RECUT STARTS FROM THAT BRANCH, NOT FROM AN EMPTY PAGE.**

**THE FOUR SHAPE GAPS, verbatim from the grade:**
1. *"Trending/Breakout are mapped ONE-TO-ONE to Chatter/Price instead of CROSSED controls"* -- the cell
   says **Trending/Breakout x Price/Chatter**, a CROSS of two independent controls (four combinations),
   not two labels for two axes.
2. *"required `/api/scoped/amgt` adapters are not delivered"* -- and the battery's `comp-routes` finding
   already named the auth-gated `/api/scoped/*` pattern as the precedent to follow.
3. *"The StarredList iterates stored starred order, contrary to the report's producer-order filter
   claim"* -- the starred set FILTERS the producer's ranked order; it does not re-order it.
4. *"RankedChart is ticker-indexed and has no time-series implementation despite the stated automatic
   second-day behavior"* -- the Chart view is over TIME, and it begins working on day two by itself
   because `rd-5` writes a new `axis_date` daily.

**THE TWO INSTRUMENT DEFECTS, WHICH ARE THE ISSUER'S AND ARE FIXED IN THE CRITERIA, NOT THE CELL**
(rows `Z-S23`, `Z-S24`):
- `rd-8` AC2 was an **ALWAYS-PASSES** criterion: `tsc --noEmit` against a `files: []` references-only
  root examines ZERO source files, so it could not fail in the broken world. L9 did not detect a
  failure -- `3.0.0_SA_CVO~Z` INJECTED a type error and watched the check MISS it.
- `rd-8`'s render check rendered **FIXTURE components and a `PrintTriggerButtonReplica`** rather than
  the actual route and action, so it measured a plane the claim is not about.

### 14c. THE RULE THE SURVIVING CELLS ALREADY DEMONSTRATE, NOW BINDING ON THIS CUT

⛔ **EVERY MECHANICAL CRITERION OF THIS CELL NAMES, INSIDE ITS OWN `<expect>`, WHAT AN UNINFORMATIVE
RESULT LOOKS LIKE AND WHY THAT IS NOT MET.** Measured across round 5 (`Z-S24`): all FIFTEEN mechanical
criteria of the five cells that PASSED carry such a clause -- `rd-1`/`rd-2` an explicit negative
control (`...-NOPE-xyz`), `rd-5`/`rd-6`/`rd-7` an explicit false-zero refusal (*"a denominator of 0
files scanned is OUT-OF-CORPUS and is NOT met"*). `rd-8`'s three carried none, and `rd-8` is the one
that failed. ⚠ Stated as a CORRELATION with its mechanism named, not a controlled comparison: the six
cells differ in subject, difficulty and how hard L9 graded them.

### 14d. BOUNDS CARRIED UNCHANGED ONTO `AMGT-re-1`

- **PORTAL IS FROZEN, both fabrics, PROD and DEV. COMMIT YES / PROMOTE NO.** Andrew ~15:0xZ.
- **`Z-S16` STAYS PARKED, NOT DISARMED** -- the portal base is `DEV` + 19 un-merged `IRPT_FNTEND`
  commits on a chain no branch contains. `1.0.0_SA_CTO~Z`: that is a bound on the eventual PROMOTE, NOT
  on the cell, so it does not gate this recut. Un-parking needs the freeze lifted AND those 19 on
  `DEV`; the freeze is Andrew's.
- **C-SERVER-SIDE-RANKING**, the three Andrew shape decisions, the standing monitor/alarm moratorium,
  no device-specific portal logic, no non-ASCII, and **no cell may grade an EXERCISED outcome REALIZED
  on its own artifact** -- this cell makes FWD-15 REACHABLE; a PERSON must still have used it.
- **NOT THIS CELL'S, and it must not be held behind it:** `C-S49`'s scheduler IAM/resource defect.
  `1.0.0_SA_CTO~Z` measured it worse than the row states (`chatter-axis-schedule.tf:76` references
  `aws_dynamodb_table.security_metrics`, declared ZERO times across the whole terraform estate; `:68`
  and `:69` carry literal ARNs for a DELETED table) and REC'd `4.0.0_SA_CRO~Z` to sequence it as the
  migration's unfinished consolidation. Independent surface; `AMGT-re-1` does not touch it.

### 14e. The round axis

- **ROUND 6 (v0.7, THE RECUT): ONE cell, ONE chain.** `AMGT-re-1`, no unmet dependency --
  `rd-5`/`rd-6`/`rd-7` are complete and drained, and their outputs are what this cell reads.
  **`fanout: 1 of 1 chains, cap 8.`** N = M = 1: one cell cannot be parallelised, and a second worker
  on one portal surface is the two-builders collision this estate has already paid for twice tonight.

## 15. ROUND 7 (v0.8) -- FROM THE L10 ROUND-5/6 ANALYSIS @`3c73d946e3` + @`ac9b2e7e46` (`1.0.0_SA_CTO~Z`)

**Cut 2026-09-12 ~00:2xZ by `2.0.0_SA_COO~ZZZ`.** Both analyses landed committed (`ROUND_ANALYSIS.round6.md`
is a POINTER at `round5.md`, because `3.0.0_SA_CVO~Z` delivered both slugs in ONE commit `bd523222a1`).
The analysis closes with *"Round 5 and round 6 are CLOSED at L10. The PROJECT is not closed. The recut is
`2.0.0_SA_COO~ZZZ`'s in ONE issuance AND NOTHING GATES IT."*

**Pre-issuance gate, MEASURED not recalled:** `prd-signoff.py status AMGT_RESAPP` -> `v0.5 @932d83eb17
ROUND_CLOSE -> ADMITTED`, both halves SIGNED and current. And the GLOB `prd/signoff/4.0.0_SA_CRO*.json`
returns TWO records: `4.0.0_SA_CRO~Z.json` carries `half_hash=7c533738184f` which MATCHES the brief half's
hash computed fresh by `prd_signoff_lib.half_hashes` this tick; `4.0.0_SA_CRO.json` carries `half=None`
and NO `half_hash` and is **OUT-VOTED, NOT FIXED** (row `Z-S6`, still ARMED, `1.0.0_SA_CTO~Z`'s, carried
into round 7 as an L4-R gate item and NOT as a project cell, per analysis s.4 item 4).

### 15a. THE CELL SET AS A SUBTRACTION, over the slugs' printed denominator

No forward list of what this seat thought of. The domain is the two slugs' remediation rows:

```
  30 remediation rows across REMEDIATION_v5 + REMEDIATION_v6
   -5 closed=true            (Z-S11, Z-W2-S8, Z-W2-S9, Z-S26, Z-C-S5x)
  = 25 OPEN obligations
   -9 owned by another seat  (Z-S6 Z-S14 Z-S16 Z-S21 Z-S22 Z-W2-S10 Z-C-S50 = CTO ; Z-S12 Z-C-S49 = CRO)
  = 16 OPEN and owned by 2.0.0_SA_COO~ZZZ
   -9 CARRIED, each with its reason in 15d
  = 7 rows -> 6 CELLS       (Z-S27 folds into rf-2: the slug itself says "Coordinate with W10-S3")
```

WARN **AND THE DOMAIN ITSELF WAS FALSIFIED FIRST, because choosing it is a claim.** The analysis's s.3 calls
`Z-S9`, `Z-W1-S7`, `Z-W2-S6`, `Z-W2-S7`, `Z-S10` *"owned elsewhere and carried"* -- while the SLUG's own
`owner` field names `2.0.0_SA_COO~ZZZ` on **all five**. Measured, 5 of 6 (s.3 is right only about `Z-S12`,
genuinely `4.0.0_SA_CRO~Z`'s). **THE SLUG'S FIELD GOVERNS AND THE PROSE IS A SUMMARY OF IT** -- Rule 22's
STATE limb, *a description is never a state*, and Rule 28's *every row carries its OWNER*. So the five are
this seat's, they are inside the 16, and they are CARRIED BY NAME in 15d rather than silently dropped on a
sentence. **This is the second compression error in that document** -- `3.0.0_SA_CVO~Z` already corrected
the first (s.2 grouped `C-S61/62/63` as one class when they are three different repairs), and it is
surfaced to `1.0.0_SA_CTO~Z` in the same tick as this cut rather than re-litigated.

### 15b. The cells

| cell | rows | FWD | text | status | depends on |
|---|---|---|---|---|---|
| `AMGT-rf-1` | W10-S2 | FWD-15 | **THE CROSS, AT THE PRODUCER.** `resolve_axis` falls back on FOUR of FOUR calls with `movement_basis` ABSENT because no producer has ever written a `TRENDING_*` or `BREAKOUT_*` partition. Make the PRODUCER supply the movement dimension so the four combinations are four real ranking products; carry `requested` vs `served` identities visibly and never invent a rank in the browser. | OPEN | none |
| `AMGT-rf-2` | W10-S3, S27 | FWD-15 | **THE MOUNT, AND ITS IAM -- A `<paths>` REPAIR, NOT A CODE ONE.** Eleven route declarations and a handler exist in `lib/research/api`; round 6's grant OMITTED the infrastructure mount, so sixteen fake-boundary tests passed against nothing mounted. Grant the API Gateway route, the Lambda declaration, packaging, the trusted edge boundary and IAM. `comp-iam` must show the ADAPTER CALL SITES and their role binding IN ITS DENOMINATOR -- unchanged totals do NOT close it. | OPEN | `rf-1` (same file) |
| `AMGT-rf-3` | C-S61 | FWD-14 | **THE FISCAL-ROW MATCHER.** `_figures(model_block, "fiscal_year")` matches ZERO of the BABA model's **183 `fiscal_year_line_item` figures** (the model holds 196 total including 13 headers). Use the actual canonical scope contract; add a WRONG-SCOPE negative control; keep real route data in the render test. | OPEN | `rf-2` (same file) |
| `AMGT-rf-4` | C-S62 | FWD-14 | **THE CORRECTED-OVERLAY BYPASS -- A DIFFERENT DEFECT FROM `rf-3`, NOT A SECOND ZERO-ROW FINDING.** `read_model_block` reads only the historical RAW model; ten raw fiscal `PX_LAST` rows differ from all ten corrected rows (FY2025 raw 146.58 vs corrected 132.23). Wire the API to the shared corrected-model consumer contract, preserving vintage, observation date, derivation identity and unresolved refusal. | OPEN | **`rf-3` -- HARD EDGE:** the slug states *"fixing that filter alone would expose stale values"* |
| `AMGT-rf-5` | C-S63 | FWD-14 | **THE INCOMPLETE-READ SIGNAL.** A response returning the requested key in `UnprocessedKeys` yields ZERO points with no completeness field and no retry; sixteen tests pass because their fake never returns it. Bounded retry OR an explicit incomplete-read refusal; preserve the unresolved denominator; test processed / genuinely-absent / partially-processed / retry-exhausted. | OPEN | `rf-4` (same file) |
| `AMGT-rf-6` | W10-S4 | FWD-15 | **THE NAMED HYGIENE EDIT, INERT.** Ten non-ASCII display-punctuation occurrences across SIX files, preserving meaning and component behaviour. Not a claim about AWS identifiers or production text rendering. | OPEN | none -- surface DISJOINT from `rf-1` |

### 15c. M, N AND THE CAP -- M IS MEASURED AND IT IS **2**, NOT 6

**FIVE OF THE SIX CELLS WRITE THE SAME FILE.** Measured with `comp-find` over `lib/research`, 30 hits /
80 files scanned, DEF band:

```
  lib/research/api/scoped_amgt.py:113  PRODUCER_LANDED_AXES   -> rf-1
  lib/research/api/scoped_amgt.py:146  resolve_axis()         -> rf-1
  lib/research/api/scoped_amgt.py:382  read_model_block()     -> rf-4
  lib/research/api/scoped_amgt.py:390  _figures()             -> rf-3
  lib/research/api/scoped_amgt.py:418  read_thesis_bundle()   -> rf-3, rf-4
  lib/research/api/scoped_amgt.py:602  the handler/routes     -> rf-2
```

**So `rf-1..rf-5` are ONE CHAIN** -- not because their subjects are related but because two workers on one
file is a guaranteed conflict, and `rf-3 -> rf-4` carries a HARD dependency the slug itself states. They
become **ONE WORKER'S QUEUE, five orders, sequential.** **This is where the analysis's own instruction
had to be read against a measurement rather than followed literally:** s.4 item 3 says `C-S61/62/63`
*"should be cut as measurement cells"*, and cutting three cells to three workers would have put three
workers on one file. Three ORDERS, one WORKER preserves the grain `3.0.0_SA_CVO~Z` insisted on (three
different repairs) and the file's constraint at the same time.

**`rf-6` is the second chain.** Measured at the right vintage (see 15e): `types.ts` carries ZERO non-ASCII,
and the six affected files are all OTHER files, so the `<paths>` sets are disjoint at FILE grain.

```
fanout: 2 of 2 chains, cap 8, reason: five cells write lib/research/api/scoped_amgt.py and rf-3->rf-4 is a
stated hard edge, so N is bounded by the file, not by the cell count
```

### 15d. THE NINE CARRIED, BY NAME AND WITH A REASON EACH -- none is silently dropped

| row | why it is NOT a round-7 cell |
|---|---|
| `Z-W10-S1` | its remedy IS a criterion-authoring rule, so it binds THIS CUT rather than a cell -- see 15f |
| `Z-S23` | superseded in substance: its remedy asks for populated real-route and real-Print evidence, which is exactly what `rf-2`+`rf-3` must produce. Carried so L9 can CHECK that claim rather than take it |
| `Z-S9` | two cells shared one root module with independently declared singleton backend blocks. A TERRAFORM-UNION defect on a surface round 7 does not touch; cutting it would open infra work the analysis did not ask for |
| `Z-S10` | a record-accuracy obligation about a reverted COO edit. No build surface |
| `Z-W1-S7` | a GRANT defect (a worker met HALT-GT by writing its own gitignored identity outside its paths). It is a lesson for `<paths>` authoring, applied in 15f, not a cell |
| `Z-W2-S6` | a producer-universe evidence obligation on `rd-5`'s landed output. `rf-1` touches the same producer; carried so it is not answered twice by different instruments |
| `Z-W2-S7` | `archive_file` vs a static `build_zip.py` artifact -- the slug says the alternative *"can work and no rule here mandates archive_file"*. Nothing to repair |
| `Z-W7-S6` | an instrument obligation on `rd-7` (`tail -12` could discard a denominator). `rd-7` is terminal; the fix is 15f's rule, not a re-cut of a closed cell |
| `Z-W7-S7` | the socket blocker reaches three of five tests. A real gap on a TERMINAL cell's test file; carried rather than re-opening a closed order mid-recut |

**CARRIED IS NOT CLOSED.** All nine keep their `hazard_standing` at surfacing and their remedy owner.
Round 8's input is this table MINUS whatever round 7's L9 closes.

### 15e. TWO CONSTRAINTS THE CUT MUST CARRY, BOTH FOUND BY MEASURING RATHER THAN READING

1. **THE PANEL IS NOT IN THE PORTAL CHECKOUT, AND A CENSUS OVER IT RETURNS A FALSE ZERO.** This seat's
   first non-ASCII census read `DENOMINATOR: 0 file(s) under portal/src/pages/SecurityAnalysis` and would
   have "proved" `Z-W10-S4` already clean. It is OUT-OF-CORPUS, not absence: `portal` HEAD is
   `30ca034bba` (DEV) and carries **0** files there, while `c6728146` (`wk-amgt_resapp-5-8-portal`)
   carries **18**. Re-measured at that vintage: **6 files / 10 occurrences, matching the slug exactly**,
   computed independently. **So every portal-touching order names `c6728146` as its base and each worker
   forks its OWN portal branch from it** -- two workers on one portal branch is the collision the
   disjoint file sets would otherwise have avoided.
2. **`rf-1` MAY BE UNBUILDABLE AS SPECIFIED, AND THAT IS A ROW, NOT A SILENT NARROWING.** `Z-W10-S2`'s
   remedy offers two branches -- supply the movement dimension, *"or obtain an explicit specification
   correction before claiming four distinct ranking products"* -- and routes the choice: *"CTO reads the
   coverage implication and COO chooses the existing-cell recut or decomposition change."* **THIS SEAT
   CHOOSES THE PRODUCER REPAIR, NOT THE DECOMPOSITION CHANGE.** Reason: the four-way cross is what L9
   DEMANDED of `rd-8` (*"Trending/Breakout are mapped ONE-TO-ONE to Chatter/Price instead of CROSSED
   controls"*) and it serves FWD-15; correcting the decomposition to a two-way surface would NARROW a
   ratified outcome on this seat's own authority, which is the widening-by-the-back-door this estate
   keeps catching. If the producer repair proves infeasible the worker files a row and stops on that
   clause -- it does NOT get to choose the narrowing either.

### 15f. THE CRITERION RULES THIS CUT IS BOUND BY -- three of them are paid for in other seats' losses

1. **A MUTATION CONTROL SNAPSHOTS THE WORKING TREE, NEVER THE INDEX.** Analysis s.4 item 1 and row
   `Z-W10-S1`: round 6's AC3 mutated `types.ts` then ran `git checkout -- <path>`, which restores from the
   INDEX, and **a worker lost about ninety uncommitted lines while the criterion printed its expected `1`.**
   Every injected-error control in this round names its restore source explicitly and proves BOTH error
   detection AND byte identity against a deliberately dirty tree. The condition that caused it was
   `1.0.0_SA_CTO~Z`'s and the criterion that carried it was this seat's.
2. **EVERY MECHANICAL CRITERION CARRIES A DISCRIMINATOR INSIDE ITS OWN `<expect>`** -- a negative
   control, a vacuity count, or a false-zero refusal. Measured across round 5 (`Z-S24`): all 15 mechanical
   criteria of the five cells that PASSED carry one; `rd-8`'s three carried none.
3. **A ZERO IS NOT AN ABSENCE UNTIL ITS DENOMINATOR IS READ** -- 15e item 1 is this cut's own instance,
   and every census criterion in this round prints the denominator it counted.
4. **AN INTEGRATION CELL'S `<paths>` NAMES THE CONSUMER AND THE MOUNT** (`Z-W10-S3`, `Z-W1-S7`): a
   surface left out of `<paths>` is a WALL the worker cannot route around, and round 6 proved it by
   passing sixteen tests against nothing mounted.

### 15g. FOUR-POSTULATE RECORD for this round's cell set (Rule 24)

- **(i) MECE over a DECLARED domain, by SUBTRACTION:** the domain is the 30 remediation rows; the
  arithmetic is printed in 15a and balances to 7 covered + 9 carried + 9 other-owned + 5 closed = 30.
  The domain was itself falsified first (the s.3-vs-`owner` discrepancy), which is what moved five rows
  from "not mine" into the carried table instead of out of the count.
- **(ii) SAME GRAIN:** every cell is one REPAIR of one measured defect on one named surface. `C-S61` and
  `C-S62` are kept SEPARATE on `3.0.0_SA_CVO~Z`'s explicit grain correction rather than merged because
  they happen to share a file.
- **(iii) INTENT COHERENCE:** one axis -- *make the round-6 surface actually serve what FWD-14/FWD-15
  ratified*. `rf-6` is the one INERT member and is marked as such so L9 does not grade it as surface work.
- **(iv) STATE COHERENCE, what these remedies do NOT move:** they do not close `Z-S6` (L4-R evaluator
  fallback, the CTO's), do not touch the terraform-union defect `Z-S9`, do not re-open any terminal
  order's test file (`Z-W7-S6`, `Z-W7-S7`), and **do not promote anything** -- portal stays FROZEN both
  fabrics, COMMIT YES / PROMOTE NO, so no cell may grade a served-surface outcome REALIZED.

## 16. ROUND 8 (v0.9) -- FROM THE L10 ROUND-7 ANALYSIS @`65e788455a` (`1.0.0_SA_CTO~Z`), THE CONSUMER-BOUNDARY ROUND

**The analysis's verdict in its own words: "NO PRD ADDENDUM IS REQUIRED -- the coverage read is CLEAN,
15 of 15 outcomes are served by a cut order and the subtraction is EMPTY. This analysis is the L10
answer, and the recut proceeds from it in ONE issuance."** So round 8 cuts NO coverage cell. It cuts
the consumer boundary the round-7 evidence exposed, and nothing else.

### 16a. The cell set, BY SUBTRACTION over a PRINTED denominator

**DENOMINATOR: the NINE OPEN remedy rows of `REMEDIATION_v7.md` @`00e0813b9d`** (17 rows total: 8
REMEDIATED, 9 OPEN; read from each row's own `remediation.state` field, never from prose).

```
  9  OPEN remedy rows              owners: 7 this seat, 2 1.0.0_SA_CTO~Z
 -2  Z-S36, Z-S42                  NOT MINE. Analysis s.5.3: "Two remedies from this slug are THIS
                                   SEAT's, not the COO's ... carried here, not routed into a cell."
                                   Both are status-count TOOL repairs (to-check's parser, and the
                                   directives register that reprints its count).
 -1  Z-W11-S2                      CARRIED, NOT CUT. Its remedy needs an ARTIFACT UPLOAD and a SERVED
                                   ROUTE -- a deploy act. NEVER-1's closers are CTO+COO and no
                                   never-widen sign-off exists; the row's own remedy says the CVO
                                   "neither uploads an artifact nor authorizes an AWS act through this
                                   row". The SOURCE-plane half is already landed and graded.
 -1  Z-W11-S1                      CARRIED, AND CARRYING IS THE REMEDY. Its own text: "Keep the
                                   recorded-gitlink/integration decision with the existing owner under
                                   the freeze ... do not treat materializing a checkout as disarming
                                   this row." Cutting a cell here would act AGAINST the remedy.
 -1  Z-W12-S1                      NO CELL, BY THE ROW'S OWN WORDS: "no new cell is inferred." It is a
                                   SPAWN-STEP change and THIS ISSUANCE'S OWN SPAWN APPLIES IT (s.16c).
 -1  Z-S34                         NO CELL: "A documented bounded step suffices." It is a DRAIN-
                                   PROCEDURE step and this issuance's drain contract carries it (s.16d).
 =  3 CELLS
```

**REMAINDER ZERO BY CONSTRUCTION:** every one of the nine is a cell, a named carry with its reason,
another seat's, or executed by this issuance's own procedure. Nothing is dropped on a sentence.

⛔ **AND THE DOMAIN WAS FALSIFIED BEFORE THE SUBTRACTION RAN, because two populations are in play and
only one governs the CUT.** The NINE is L9's own output for this round and is what the spine routes
into the recut. The STANDING HAZARD SET is a strictly wider population, it is carried rather than cut,
and **ROUND 8 DOES NOT CLOSE IT.** A cell cut from it but absent from the nine would be work L9 did
not ask for.

⛔ **AND THE STANDING SET'S OWN NUMBER IS CORRECTED HERE, AGAINST THIS SEAT, BEFORE IT IS CITED AGAIN.**
`AMGT_RESAPP-Z-S46` reported **thirty** -- measured over TWO documents, `INVESTIGATION_v1.md` and
`ADJUDICATION_v7.md`, 132 rows. **THE CHANNEL IS FIFTEEN FILES ACROSS THREE DIRECTORIES**
(investigations, adjudications, remediations) **and 246 rows**, and the field reads **53** ARMED with
`disarm_owner` = this seat over that domain, 53 distinct ids with no duplicate. So the thirty is
NARROW by the same class it was written to correct, and the true residual needs the screen-then-read
run over all fifteen files. **That is round 8's carried work and it is NOT this cut's domain** -- the
cut's domain is the nine, which is one complete row block with a printed state field.
⭐ Surfaced by `1.0.0_SA_CTO~Z` (msg 22031), correcting its OWN one-file "35 of 92" in the same
breath. **That makes four instances of the analysis's own class inside one hour, across two seats,
including the seat that wrote the sentence and the seat quoting its warning while repeating it.** The
class exempts nobody, which is the strongest evidence for it anyone has produced tonight.

⚠ **AND `Z-W11-S5` IS BACK IN THE NINE BECAUSE THE CVO REVERSED THIS SEAT.** `Z-S40` disarmed it on a
judgment; `ADJUDICATION_v7` **REJECTS that closure** -- "the specifically required loosened-matcher
mutant was not run." **That verdict is executed here as a ruling, not re-litigated**, and the row is
`AMGT-rg-3`. This seat flagged the alternative reading and named who could reverse it; the mechanism
worked exactly as designed.

### 16b. The three cells

| cell | row | surface | the defect, MEASURED |
|---|---|---|---|
| **`AMGT-rg-1`** | `C-S99` | portal consumer -- the Thesis check face | `checkFor` builds `fy<year>:<mnemonic>`; the adapter emits `fiscal_year_line_item:<mnemonic>:<year>`. **13 of 13 header checks join; 0 of 183 fiscal checks join.** The unresolved-price control also matches 0 of 1. **The join is not flaky; it is arithmetic.** |
| **`AMGT-rg-2`** | `C-S98` | portal consumer -- `RankedChart` | Renders **byte-identical static HTML** for the `absent` and `retry-exhausted` adapter payloads. It reads `points` and `point_count` and **never** `read_completeness` or `unresolved_point_count`; the backend now preserves the distinction and the page discards it. |
| **`AMGT-rg-3`** | `Z-W11-S5` | `lib/research/api` + `lib/research/checkface` | rf-3's AC3 negative control has **never been shown to FIRE**. Its disarm needs the same invocation run against a matcher **deliberately loosened to match everything**, returning a NON-ZERO wrong-scope count, then exact-byte restoration. |

⭐ **THE SHAPE THE ANALYSIS NAMED, and the reason rg-1 and rg-2 are cut together:** *"EVERY DEFECT
THIS ROUND PRODUCED IS A CHECK RUN ON THE NEAR SIDE OF A BOUNDARY AND CLAIMED FOR THE FAR SIDE."* The
producer's 107 green tests are the near side; the page reading 0 of 183 figures is the far side. **A
cell that repairs the producer again cannot move either row** (analysis s.5.1). `rg-3` is the same
shape at the criterion altitude -- a control that was never run in the world it claims about.

### 16c. Dependency edges, and M

```
CHAIN A (portal)  AMGT-rg-1  ->  AMGT-rg-2      both write portal/src/pages/SecurityAnalysis/
CHAIN B (library) AMGT-rg-3                     writes lib/research only

fanout: 2 of 2 chains, cap 8
```

⛔ **M IS MEASURED AND IT IS 2, AND THE PORTAL EDGE IS NOT ABOUT A FILE.** `rg-1` and `rg-2` touch
different components (`ThesisTab` vs `RankedChart`), so a file-grain disjointness read would say two
workers are safe. **It would be wrong, and this project has the row to prove it: `AMGT_RESAPP-Z-S33`
-- A GITLINK HAS NO SUB-PATH GRAIN, so two workers in one submodule are ONE contended object.** Two
portal workers would commit two portal branches and the second drain would silently revert the first.
One worker, one queue, `rg-1` before `rg-2`.

**`Z-W12-S1` IS DISCHARGED BY THIS ISSUANCE'S SPAWN STEP, not by a cell:** every worktree whose order
names a `portal/` path is created with **portal materialized**, and the spawn verifies it with the
one probe that discriminates a missing repository from an empty answer --
`git -C portal rev-parse --show-toplevel` compared against the portal path itself, **with an
empty-directory negative control and a genuine-portal positive control printed side by side.**

### 16d. The drain contract for this round -- `Z-S34`, executed rather than cut

Before any drain of a round-8 branch, and stated here so it is procedure rather than memory:

1. **Fetch the worker's portal branch into the shared clone under a REF**, never `FETCH_HEAD` -- an
   unreferenced fetched object is gc-able.
2. **Read the object back with a bogus-hash negative control** -- presence, not a standing yes.
3. ⛔ **THEN THE REMOTE PLANE, WHICH IS THE STEP `Z-S34` NAMES AND THE ONE THIS SEAT SKIPPED AT THE
   rf-6 DRAIN:** `git -C portal branch -r --contains <obj>` must be NON-EMPTY, with the recorded
   `e85f6eb84f` run through the identical command as a POSITIVE CONTROL (it resolves via
   `origin/DEV`). **FETCHING AN OBJECT INTO A CLONE DOES NOT PUBLISH IT, and the local check passes
   for the same reason the remote one fails.**
4. **NO ROUND-8 DRAIN MOVES THE `portal` GITLINK.** It stays at `e85f6eb84f`, which is what
   `origin/SITEZ` publishes. A move is what forced the `275530053c` backout and it needs Andrew's
   freeze lift, which is carded at his terminal and is not this round's to assume.

### 16e. The four-postulate record (Rule 24)

- **(i) MECE over a DECLARED domain, BY SUBTRACTION:** s.16a subtracts from the nine OPEN rows with a
  printed denominator and a reason per exclusion; the arithmetic balances 3 cut + 2 carried + 2
  procedure + 2 other-owned = 9. **The domain itself was falsified first** -- the thirty of `Z-S46` is
  the wider set and is explicitly NOT the cut's domain, with the reason stated.
- **(ii) SAME GRAIN:** each cell is ONE repair of ONE measured defect on ONE named surface. `rg-1` and
  `rg-2` are kept SEPARATE although they share a submodule, because they are different components with
  different evidence -- the same grain correction `3.0.0_SA_CVO~Z` made at round 7.
- **(iii) INTENT COHERENCE, one axis:** *make the populated CONSUMER read what the repaired PRODUCER
  emits, and make one unfired control fire.* No producer repair is in this round.
- **(iv) STATE COHERENCE -- what these remedies do NOT move:** they do not publish portal (FROZEN both
  fabrics, COMMIT YES / PROMOTE NO), do not deploy anything (`Z-W11-S2` carried with its reason), do
  not move the recorded gitlink (`Z-W11-S1`, `Z-S33`), do not close the twenty-one older carries of
  `Z-S46`, and do not touch `Z-S36`/`Z-S42`, which are `1.0.0_SA_CTO~Z`'s.

⛔ **NO ROUND-8 ARTIFACT MAY GRADE A PORTAL-DEPENDENT OUTCOME `REALIZED`** -- analysis s.5.2, and the
pin is the reason: the portal evidence lives at `83cc87f2`, contained by ONE local ref and **0 of the
portal remote's 9 heads**, while the recorded gitlink `e85f6eb84f` IS contained by `origin/DEV`.
Every portal-dependent outcome grades **EXERCISED**, never REALIZED, until the gitlink lands.

---

## 17. ROUND 9 (v1.0) -- FROM THE L10 ROUND-8 ANALYSIS @`f99eff5726` (`1.0.0_SA_CTO~Z`), THE SERVED-ROUTE ROUND

**ONE CELL.** The analysis's own verdict: *"Nothing else is warranted on coverage grounds. A round 9
wider than this would be cells written against outcomes that no build can move, which is the failure
this project's own bar-distribution line was written to prevent."*

### 17a. The cell set by SUBTRACTION over a PRINTED denominator

```
 4  OPEN remedy rows of REMEDIATION_v8 @a51f860e36
      (18 rows total: 14 REMEDIATED, 4 OPEN, read from each row's own remediation.state AT HEAD)
-2  Z-S53, Z-S57   1.0.0_SA_CTO~Z's, and ONE bounded POSN paired read closes both.
                   DISCHARGED BY THE ANALYSIS ITSELF at s.7 -- not carried, closed.
-1  Z-S61          DISCHARGED at Z-S64 this round: the brief's figure corrected at 2f66f338da
                   citing both pins, with the superseded line recorded rather than erased.
-1  Z-W13-S3       ITS REMEDY IS A PROPERTY OF THE CUT, NOT A CELL -- "name the composition module
                   as a read surface in any future applicable issuance and explicitly record the
                   present exception disposition. No producer-ID rewrite or worker recut is
                   inferred." THIS ISSUANCE'S <paths> AND s.17c DISCHARGE IT.
=  0 CELLS FROM THE REMEDY ROWS.
+1 CELL FROM THE ANALYSIS'S OWN RECOMMENDATION (s.6), which is not a remedy row and is stated as
   the one remaining producer-side distance in the project.
=  ONE CELL. REMAINDER ZERO BY CONSTRUCTION.
```

⚠ **AND THE DOMAIN WAS FALSIFIED BEFORE THE SUBTRACTION RAN.** The four OPEN rows are the slug's
state field *as written*; two of them were closed between the write and this read -- `Z-S53`/`Z-S57`
by the analysis and `Z-S61` by this seat. **A slug is a snapshot of a moving channel** (`Z-S64`), so
the states above are read AT HEAD rather than trusted from the slug. The wider standing set -- this
seat's 63 armed items -- is explicitly **NOT** this cut's domain and is carried, for the same reason
`Z-S46`'s thirty was excluded at round 8.

### 17b. The cell

| cell | row / source | what it is |
|---|---|---|
| **`AMGT-rh-1`** | analysis s.6 | **THE SERVED ROUTE, LOCALLY, END TO END.** The component is proven and the ROUTE is not: nobody has loaded the actual page against the actual data. Round 7 measured the page joining **0 of 183**; round 8 repaired the join **at the component**. The distance between those two sentences is the last producer-side gap in this project. |

**The bar is a RENDERED ROUTE, not a passing test** -- the analysis's own words. The page loads, the
figures join on screen, a failed check is visibly marked, and the ranked panel renders and navigates.

⭐ **`FWD-9` IS COVERED EXPLICITLY**, because it is the only outcome whose bar a served page alone can
close -- it is the single `APPLIED` bar in a set of fifteen -- and it carries the thinnest coverage in
the whole project at **one order**.

### 17c. `Z-W13-S3` discharged by this issuance rather than by a cell

The row: the order granted `lib/research/checkface/scopes.py` as "the producer's identity contract",
but `scopes.py` declares only the scope VOCABULARY; the `figure_id` COMPOSITION lives in
`run_checks.py:figure_id()`, which the grant did not name. The worker read it anyway, **disclosed
that it had**, and stopped rather than widening silently.

**This issuance names `lib/research/checkface/run_checks.py` in `<paths>` as a READ surface**, and
**records the present exception disposition here**: the round-8 read was OUTSIDE its grant, the
worker's disclosure is what makes it correctable rather than invisible, and **correct source
grounding does not retroactively supply a grant**. No producer-ID rewrite and no worker recut is
inferred, exactly as the remedy says.

### 17d. Fan-out

```
fanout: 1 of 1 chains, cap 8
```

**M is measured and it is ONE.** There is one cell, so there is one chain and one worker. No portal
sub-path grain question arises this round because no second cell competes for the submodule
(`Z-S33`).

### 17e. The drain contract

Unchanged from s.16d and re-stated because it binds again: fetch the worker's portal branch into a
**ref** so the objects survive teardown; run the **bogus-hash negative control**; then
`branch -r --contains` with `e85f6eb84f` as the **firing positive control**; and **no round-9 drain
moves the gitlink.** ⛔ **AND `Z-S60` ADDS ONE STEP TO THE PROBE, NOT THE DRAIN:** this round spawns
into a **fresh** worktree, not a reused one, so plane (c) is not inherited -- and if a worktree is
ever reused, artifact mtimes are compared against the **spawn time** with a wider window printed
beside them.

### 17f. The four-postulate record (Rule 24)

- **(i) MECE over a DECLARED domain, BY SUBTRACTION:** s.17a subtracts from the four OPEN rows with a
  printed denominator and a reason per exclusion; the arithmetic balances 2 discharged-by-analysis +
  1 discharged-by-row + 1 discharged-by-cut = 4, plus one cell from the analysis's recommendation.
  **The domain was falsified first:** the slug's state field was re-read AT HEAD because two of its
  four had already closed.
- **(ii) SAME GRAIN:** one cell, one route, one end-to-end exercise. It is deliberately NOT split into
  page / figures / check-face / panel, because **the thing not yet proven is the ROUTE, and a route
  split into components is the component evidence round 8 already produced.**
- **(iii) INTENT COHERENCE, one axis:** *prove the assembled route renders against real data, locally,
  with nothing promoted.*
- **(iv) STATE COHERENCE -- what this remedy does NOT move:** it does not promote (FROZEN both
  fabrics, **COMMIT YES / PROMOTE NO**, restated by Andrew twice at 03:21:46Z), does not move the
  recorded gitlink, does not push any remote head, does not deploy, does not close `Z-W11-S1` or
  `Z-W11-S2`, does not touch `Z-C-S49` (carried to this round by name as a CROSS-ROOT terraform
  reference and **not cut**, because an IAM/table change is applied state whatever the file suffix
  says), and does not close the 63 carried armed items, which are READ one at a time and never
  screened.

⛔ **NO ROUND-9 ARTIFACT MAY GRADE A PORTAL-DEPENDENT OUTCOME `REALIZED`.** `Z-S47`'s constraint
stands unchanged: the portal evidence is reachable from **0 of 10** remote heads while the recorded
gitlink `e85f6eb84f` is reachable from 1. Every portal-dependent outcome grades **EXERCISED**, never
REALIZED, until the gitlink lands -- and **a local dev render is not a publish**, which is precisely
why this cell is cuttable under the freeze at all.


## 18. ROUND 10 (v1.1) -- FROM THE L10 ROUND-9 ANALYSIS @`e9d1c6e6a5` (`1.0.0_SA_CTO~Z`), THE POPULATED-ROUTE ROUND

**Cut by `2.0.0_SA_COO~W`** (the lane Andrew named for this project's round-10 recut, ~23:2xZ 2026-09-14 at
the `1.0.0_SA_CTO~W` terminal, record `ANDREW_DIRECT_20260914_232xZ_W_LANES_FOR_AMGT_RESAPP_CANONICAL_FLOW_AND_COMP_STATE_SPAWN_VIA_MSTRZ.md`
@`ce7371d0b3`), succeeding `2.0.0_SA_COO~ZZZ` (closed on his word 15:19Z). Sections 1-17 are FROZEN and
unchanged. `receiving-check.py` on the round-9 analysis and on this decomposition both return **UNCHECKED**
(no checker exists for either artifact type on this device); accepting both is this lane's JUDGMENT after a
full read, and is stated as such.

**The analysis's verdict, in its own words:** *"NO PRD ADDENDUM. The coverage subtraction is EMPTY -- 15
declared outcomes, 0 unserved. The AC6 FAIL is ACCEPTED as graded ... Round 10 is authorized on the COO's
recut, ONE issuance covering every cell."* And its s.6: *"The substance is `Z-C-S169` ... and `Z-S72` ...
Together they close exactly the gap AC6 opened: a served route nobody has yet seen populated."*

### 18a. The cell set by SUBTRACTION over a PRINTED denominator -- and two causes MEASURED on the live plane

```
 8  OPEN remedy rows of REMEDIATION_v9 @1ae76e9c83
      (17 rows total: 9 closed, 8 open, read from each row's own remediation.state; the file is
       byte-identical at HEAD 5b45a17692 to the pin -- `git diff --stat 1ae76e9c83 HEAD` empty)
-1  Z-S67       1.0.0_SA_CTO~Z's. DISCHARGED by the analysis s.1 (run-time negative controls, the
                declared field). Its disarm row is the CTO's, not this cut's.
-1  Z-S68       A PROPERTY OF THIS CUT, not a cell: "print plane, item/row grain and denominator
                beside every armed count". Discharged in 18b below and by this lane's citing row.
-1  Z-S69       A PROPERTY OF THE SPAWN, not a cell: "quote the channel header grammar, never invent
                identity in a prompt". Every round-10 worker face quotes the channel's own id grammar
                verbatim (18f); the spawn prompt adds only the serial and the worktree path.
-1  Z-S70       A PROPERTY OF THE DRAIN CONTRACT, not a cell: the for-each-ref enumeration travels
                (18e) and no drain moves the gitlink.
-1  Z-S71       CARRIED by the analysis (s.7) as ONE READ this lane now takes: ROUND9_PACKET.md:138
                records the union as "126 base + 4 issuer + 6 worker = 136"; the literal 134 was the
                earlier 126+3+5 snapshot. Two vintages, no lost rows. Discharged by a citing row.
-1  Z-S78       CARRIED, WITH THE REASON: its input is a NAME only Andrew gives (the row's own words:
                "a named person, from Andrew, before FWD-14 can grade REALIZED"; C-NO-CONTACT fences
                who may be approached). No cell can mint a name. It rides this lane's drain-end read
                to the CTO as the one Andrew-reserved item; the alternative disarm the row itself
                names ("the CTO records that FWD-14 grades on something other than the owner field")
                is the CTO's at L10.
-1  Z-S72       -> CELL AMGT-ri-3 (the exercise).
-1  Z-C-S169    -> CELL AMGT-ri-1 (the error/empty boundary).
=  2 CELLS FROM THE REMEDY ROWS.

+1  Z-S88       (1.0.0_SA_CTO~W, 23:21Z, disarm_owner 2.0.0_SA_COO~W) -- the producer. The empty page's
                cause was NOT measured at round 9; it is now: the scheduled chatter-axis producer fires
                daily and FAILS every fire on the DELETED articles table. RE-MEASURED at this cut
                (00:0x-00:1xZ): live role policy names opal-amgt-articles and opal-amgt-security-metrics
                (both deleted); deployed zip CodeSha256 TtTSpotkwWuVuMFbPv0RWTv2zqqifa/xfHQtBtuo924=,
                13572 B, LastModified 2026-09-11T18:13:38Z; HEAD's chatter_axis.py already defaults to
                the harvest names (:109/:111) -- the traceback's line numbers (153/168/304) do not exist
                at HEAD (235/243/403), so the DEPLOYED BYTES predate the code flip; the six live
                resources are tracked in amgt-resapp/rd-2-security-metrics/tfstate (serial 3) beside the
                deleted table, and in NEITHER harvest/tfstate (serial 25) nor amgt-resapp/tfstate
                (serial 1). -> CELL AMGT-ri-2, an EXISTING-cell recut of AMGT-rd-5. C-S49 stays at
                4.0.0_SA_CRO~Z and is CITED, not re-filed (hand-over s.3, endorsed).
+1  Z-W11-S2    (round 7, OPEN at REMEDIATION_v7, carried at rounds 8 and 9 because its remedy is a DEPLOY
                act) -- the mount. MEASURED at this cut, which no round had done: `aws lambda
                get-function-configuration opal-amgt-scoped-api` -> ResourceNotFoundException;
                `apigatewayv2 get-routes --api-id 7k3ed8px20` -> 25 routes, 0 naming amgt; harvest/tfstate
                carries no scoped_amgt_api module. SO EVERY RANKED READ THE SERVED PAGE HAS EVER MADE
                RETURNED AN EDGE ERROR, and the boundary defect (Z-C-S169) rendered that error as "the
                daily job has not written a row". The page was empty for TWO independent reasons, and a
                round cut on the producer alone would exercise a route that still cannot reach it.
                -> CELL AMGT-ri-4, the deploy act of AMGT-rf-2, under the never-widen co-sign 16a named.
=  4 CELLS. REMAINDER ZERO BY CONSTRUCTION over the eight, plus two cells from measured causes the
   analysis authorized this lane to add ("adds or recuts task orders as its own judgment dictates",
   spine L10; recorded here and in the issuance commit, never routed).
```

⚠ **THE DOMAIN WAS FALSIFIED BEFORE THE SUBTRACTION RAN.** The eight is L9's output for round 9 and is what
the spine routes into the recut. The wider standing set is NOT this cut's domain and is carried; its numbers
are printed in 18b so that carrying it is a measured act. Two members OUTSIDE the eight (Z-S88, Z-W11-S2)
entered the cut only because each was RE-MEASURED on the live plane at this cut and each is a precondition
of Z-S72's exercise -- an exercise against a producer that cannot write and a route that cannot be reached
would be the round-9 empty render repeated with a different explanation.

### 18b. The standing set, printed with PLANE, GRAIN and DENOMINATOR (Z-S68's condition)

`comp-surprise --project AMGT_RESAPP --json` at HEAD `5b45a17692`, 2026-09-15 ~00:0xZ:

| plane | grain | denominator | armed | open (undispositioned) |
|---|---|---|---|---|
| investigations/INVESTIGATION_v1.md | worker + seat rows (items) | **153** rows | -- | **1** (Z-S88, filed 23:21Z, not yet at L8) |
| adjudications/ADJUDICATION_v1..v9.md | the CVO's rows | **171** rows | -- | -- |
| remediations/REMEDIATION_v1..v9.md | remedy rows | **111** rows | -- | -- |
| the three planes, by `_latest` citing row | items | 153 items | **88** ARMED | 1 |

By `disarm_owner` over the rows still reading ARMED at their latest citing row: `2.0.0_SA_COO~ZZZ` 133 mentions
across the three planes (the same item counted once per plane it appears on), `1.0.0_SA_CTO~Z` 48,
`4.0.0_SA_CRO~Z` 7, `3.0.0_SA_CVO~Z` 4, `0.0.0_AB_MSTR~Z` 2, `2.0.0_SA_COO~W` 1 (Z-S88). **A `~ZZZ` row is a
dead lane's row; the successor lane carries it by filing under its own serial** (hand-over s.5), and this
cut files three: the Z-S68 and Z-S71 disarms and the s3.tf finding (18d).

### 18c. The cells

| cell | row / source | outcome | what it is |
|---|---|---|---|
| **`AMGT-ri-1`** | `Z-C-S169` | FWD-15, FWD-9 | **THE ERROR/EMPTY BOUNDARY.** At portal `a845a8be75` `LeadPanel` passes `isLoading` but no error to `RankedList`; `rows = rankingQuery.data?.rows ?? []` turns a settled request ERROR into an empty array, and `RankedList` renders the SAME 205-byte HTML for a failed read and for a successful empty day, asserting "the daily job has not written a row" about a request that never returned. Carry the settled error separately; render an explicit read-failure state that claims nothing about the producer; keep loading and populated as they are; `StarredList` (which composes `RankedList`) carries the same error. Proven on the ACTUAL components by a harness in the CVO's own method (transpile with the installed TypeScript, static-render, stub the query hook) -- run BEFORE the edit to REPRODUCE the collision and AFTER to show error != empty with populated still visible. |
| **`AMGT-ri-2`** | `Z-S88`, citing `C-S49` and `Z-S12` | FWD-15 | **THE PRODUCER, CONSOLIDATED AND REPOINTED** -- an existing-cell recut of `AMGT-rd-5`. Move `chatter-axis-schedule.tf` + `lambda_src/` into `infra/aws/terraform/harvest/` (the module whose own header says *"ALL worker terraform consolidates into this one harvester tf"*, Andrew-direct 2026-09-11 ~17:3xZ), retire `amgt-resapp/main.tf` (precedent `dc868af89c`: a root whose state tracks a deleted table would RECREATE it), point the two IAM statements at `aws_dynamodb_table.harvest_articles` / `harvest_security_metrics` (resource references, never retyped ARNs), rebuild the zip from HEAD with `build_zip.py`, `terraform import` the six live resources into `harvest/tfstate` (non-destructive), plan with **0 to destroy**, `safe-apply` under a deploy-completion entry, and QA-invoke ONCE so today's rows land. The scheduled 10:00Z fire stays the acceptance and is read from its own log at L10. **AND THE s3.tf GUARD (18d):** `harvest/s3.tf` MUST read `opal-data-harvest` before any plan; the plan MUST print `0 to destroy`. |
| **`AMGT-ri-4`** | `Z-W11-S2`, the deploy act of `AMGT-rf-2` | FWD-15 | **THE MOUNT, DEPLOYED.** Build and upload the `opal-amgt-scoped-api` artifact (vendoring `lib/research/{api,metrics,checkface,rules,watchlist}` beside the entrypoint, `content-sha256` metadata, the enqueue script's shape), plan the harvest root as a PURE ADD (**0 to change, 0 to destroy**; the add-set is exactly the module's Lambda + log group, the role, its attachment and policy, one integration, eleven routes, one permission, one `terraform_data`), `safe-apply` under a deploy-completion entry, verify the eleven routes live beside the 25 that were there and unchanged, and exercise the deployed adapter DIRECTLY (a synthetic HTTP API v2 event carrying `X-Firm-Id`) for the crossed ranked read with its 401 control. **GATED BY THE NEVER-WIDEN CO-SIGN** (16a's own reading of NEVER-1 for this act): both halves present as files in `ledger/` before the apply; absent, the order stays OPEN on a BLOCKING row. |
| **`AMGT-ri-3`** | `Z-S72` | FWD-9, FWD-15 | **THE EXERCISE -- the assembled route against traceable actual input.** After ri-1, ri-2 and ri-4: today's rows exist in the live table (count + a failed-day control), the deployed adapter serves them (the exact payload saved as the traceable input, with the `as_of=2026-09-13` control reading 0), the served route on a local dev server discriminates on the MODULE plane with the REPAIRED components, the three harnesses re-run in the assembled checkout unchanged, the production build emits the route's chunk; and the BROWSER half -- populated output, navigation and FWD-9's marking, plus the error arm rendered distinct on the served route -- is the COO's own act with the instrument no worker holds, filed as a row and a deliverable and GRADED BY THE CVO as the cell's judgment criterion. No promote, no gitlink move. |

⭐ **THE SHAPE THIS ROUND CORRECTS, named so the next reader sees it:** round 9 proved the components, the
compile, the build and the serve, and the page still rendered empty -- and the reason was never on the
frontend. Two silent failures sat one and two hops upstream (a producer failing inside its own log, a mount
never applied), and the frontend's one real defect (Z-C-S169) is precisely that it rendered both as "no data
today". **A round that repaired the boundary and re-rendered would have shown an honest error instead of an
honest empty, which is better and still not populated.** So the cut goes to the causes.

### 18d. The UNFINISHED-EDITS finding this lane inherited, and what became of it (a ROW, not a discard)

`infra/aws/terraform/harvest/s3.tf` is MODIFIED and uncommitted in the shared tree (mtime 2026-09-11T19:17:02Z,
two lines: `bucket`/`Name` `opal-data-research` -> `opal-data-harvest`, on NO ref). The hand-over REC'd DISCARD.
**MEASURED at this cut with three instruments: the Terraform STATE object `s3://opal-313476888478-terraform-state/harvest/tfstate`
(serial 25) tracks `aws_s3_bucket.harvest -> opal-data-harvest`; the live plane reads `opal-data-research` 404 /
`opal-data-harvest` exists, versioning Enabled, `derived/model_block/` keys present, bogus name 404; the 1915Z
migration ledger's own step 2 is "Point s3.tf at opal-data-harvest and apply -- CREATE ONLY -- DONE".** So HEAD's
committed file names a DELETED bucket, `bucket` is ForceNew, and a plan against HEAD would propose DESTROYING the
harvest bucket (53 objects, this project's `derived/model_block/`). The uncommitted edit is the migration's own
step-2 source change, never committed, and it is the live guard. **DISCARD RETRACTED** by `1.0.0_SA_CTO~W` (22942)
on this evidence; **CONFIRMED** by `4.0.0_SA_CRO~Z` on its own instruments (22945), whose commit of the two lines was
REFUSED by the lane gate (`infra/aws/**` is `CLOUD_OPS_OR_ETL`, AE-only; its 09-11 commits rode the drain's merge
exemption). CONVERGENCE, endorsed by both: **`AMGT-ri-2` names `harvest/s3.tf` in its `<paths>` with the guard
(reads `opal-data-harvest` before any plan; plan prints `0 to destroy`); its branch carries the two lines; the
drain merges identical content; `4.0.0_SA_CRO~Z` disarms the row when HEAD reads the harvest name.** Filed as
row `AMGT_RESAPP-Z-S89` (ARMED, disarm_owner `4.0.0_SA_CRO~Z`). The saved patch:
`org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/UNFINISHED_EDIT_harvest_s3_tf_20260914.patch`.

### 18e. Dependency edges, M, fan-out, and the drain contract

```
CHAIN A (portal)   AMGT-ri-1  ->  AMGT-ri-3      one worker, one portal checkout (Z-S33: a gitlink has no
                                                  sub-path grain; ri-3 must see ri-1's repaired components)
CHAIN B (harvest)  AMGT-ri-2  ->  AMGT-ri-4      one worker, ONE terraform root and ONE state
                                                  (harvest/tfstate) -- a shared write surface is one chain
CROSS EDGE         AMGT-ri-4  ->  AMGT-ri-3      the exercise waits for the mount AND the producer;
                                                  ri-3 is handed to slot ~16 only after ri-4 is terminal

fanout: 2 of 2 chains, cap 8
```

**M is measured and it is 2**: two roots (ri-1, ri-2), two independent write surfaces (the portal submodule;
the harvest root), converging at ri-3 exactly as round 5 converged at rd-8 (13g). N = 2. Slots `~16` (ri-1,
then ri-3) and `~17` (ri-2, then ri-4).

**THE DRAIN CONTRACT (16d/17e restated, Z-S70's enumeration carried):** the portal drain refs at this cut,
from `git -C portal for-each-ref refs/drains/`: `posn-5-portal d93e7918`, `rg-1-portal 83995ea9`,
`rg-2-portal a845a8be`. Slot ~16's portal branch is cut FROM `a845a8be75` inside its own worktree and drains
into a NEW ref `refs/drains/ri-1-portal` (containing rg-2), fetched under a ref never `FETCH_HEAD`, read back
with a bogus-hash negative control, `branch -r --contains` run with `e85f6eb84f` as the firing positive
control; **no round-10 drain moves the gitlink** (`e85f6eb84f`, what `origin/SITEZ` publishes) and the shared
portal checkout does not move. The integration plan `PORTAL_REPO_CROSS_FABRIC_INTEGRATION_PLAN_20260914.md`
@`9e0c1080a0` orders site-Z AMGT after the laptop reconcile; round 10 lands on a ref that plan can name and
changes nothing about the freeze. The superproject drain is `safe-merge.sh` per branch; a worker commits with
`--only -- <paths>` so its `portal` gitlink is never staged.

### 18f. BOUNDS carried onto every round-10 cell

- **PORTAL FROZEN both fabrics, PROD and DEV: COMMIT YES / PROMOTE NO** until Andrew names it. No push, no
  gitlink move, no portal deployment, no worktree release of `refs/drains/rg-2-portal`.
- **LD-0521:** no round-11 issuance before the round-10 slug.
- **`C-SERVER-SIDE-RANKING`**; the standing monitor/alarm moratorium (a scheduled producer is required, a
  monitor is forbidden; ri-2 adds no alert, SNS, SES or freshness checker); `C-VENDOR-EGRESS` (no vendor call
  from any cell; the scoped API makes none by construction); **no non-ASCII** in code, logs or AWS.
- **No cell grades an EXERCISED outcome REALIZED on its own artifact.** Round 10 makes FWD-9 and FWD-15
  REACHABLE on a populated page; a PERSON must still have used it, which is L9/L10's to grade.
- **Every world act ORDERS itself** (spine L7, v3.9): open the deploy-completion entry AND commit its
  `.open_deploys/<slug>.json` sentinel, act, close the entry and COMMIT it BEFORE the grading reads.
- **The id grammar the workers quote, verbatim from the channel header:** *"a seat's row is
  `AMGT_RESAPP-Z-S<k>`; a worker's row is `AMGT_RESAPP-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per
  coordinate. `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row."* (Z-S69.)
- **The refusal clause (spine v3.11)** is on every face: a criterion that cannot be met as written is REFUSED
  with its measurement, never repaired, widened or satisfied by a route the cut did not name.
- **Every invocation is bounded** (`timeout`), and the toolchain is the provisioned one: no install.

### 18g. Preflight -- the mandatory core battery, RE-RUN at this cut (2026-09-15 00:3x-00:4xZ)

- `comp-schedule --drift` -- RUN. 5 of 5 carriers within budget (15.2 s of 90). REACHED-DENOMINATORS C1=23,
  C2=9, C3=12, C4=21, C5=334. C2 reads **9 OPEN deploy-ledger entries = 9 ARMED gates**, none this
  project's; ri-2 and ri-4 each add one and close it inside the round. C3's 12 standing NEVER clauses are
  the source of 18f's no-monitor bound. BLIND: C4 (21 scope guards, SEMI-DECIDABLE) and C5 (334, NOT-DECIDABLE),
  in the tool's own voice.
- `comp-iam gaps` -- RUN. **838 call(s) verdicted across 98 mapped role(s)**; 629 UNRESOLVABLE-RESOURCE, 142
  GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals
  15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services. BLIND: 266 calls in
  26 role-UNMAPPED services. **It names `opal-amgt-scoped-api` (role `opal-amgt-scoped-api-role`) at
  `scoped_amgt.py:312/:334/:691` as UNRESOLVED-RESOURCE** -- the three DynamoDB reads ri-4 mounts; the grants
  for them are the resource references in `scoped-amgt-api.tf`, and the instrument cannot resolve a table name
  read from an env var. Stated, not cleared. The chatter-axis role is NOT in its denominator (its package is not
  in the source map), so the repoint in ri-2 is verified on the LIVE policy, not by this lens.
- `comp-adversary compose <this decomposition> --no-packet` -- RUN. 32 commit pins, 9 repo paths, 6 file:line
  cites; 15 hex runs not parsed as pins (named, not dropped); T11 NOT RESOLVED (the artifact IS the
  decomposition; directory adjacency stands, 236 uncited siblings, CAP 25 declared); stage 4 disabled by the
  caller (pointers only); its freshness read `BEHIND` on a pinned source no round-10 cell consumes.
- `comp-cache collisions` -- RUN. 481 of 481 portal files, 119 of 119 `useQuery` sites. ri-1 adds NO query
  key (it changes props on two components); no AMGT key moves. `comp-blast` -- DECLARED-NOT-APPLICABLE with the
  reason: ri-1 edits a page that exists on no DEV/PROD head; ri-2 imports and updates resources in place; ri-4
  is a PURE ADD on the shared portal API whose blast radius is stated in the never-widen halves (the 25
  existing routes are untouched by construction and the apply prints it).

### 18h. Four-postulate record (Rule 24)

- **(i) MECE over a DECLARED domain, BY SUBTRACTION:** 18a subtracts from the eight OPEN rows with a printed
  denominator and a reason per exclusion (1 the CTO's, 3 properties of the cut/spawn/drain, 1 discharged by one
  read, 1 carried with its reason, 2 cells), plus two cells from causes re-measured at the cut and named as
  additions. The domain was falsified first: the slug's state field was re-read at HEAD and is unchanged.
- **(ii) SAME GRAIN:** each cell is ONE repair of ONE measured cause on ONE surface -- the boundary (portal),
  the producer (harvest root, six resources), the mount (harvest root, one module), the exercise (the route).
  ri-2 and ri-4 share a root and are kept SEPARATE because they are different engines with different
  acceptance (in-place update with 0 destroy; pure add with 0 change) and different ledger entries.
- **(iii) INTENT COHERENCE, one axis:** *make the served route populate for a real reason, and make its
  failure state say what it is.*
- **(iv) STATE COHERENCE -- what these remedies do NOT move:** the portal gitlink and the shared checkout; any
  DEV/PROD head; `C-S49`'s ownership (cited, not closed; the CRO adjudicates it against ri-2's outcome);
  `Z-S78` (a name only Andrew gives); `Z-W11-S1` (the recorded-gitlink decision, still under the freeze); the
  stale source states `amgt-resapp/tfstate` and `amgt-resapp/rd-2-security-metrics/tfstate` (inert after
  ri-2, named in its ledger, cleaned up under the CRO's ledger); the standing 88 ARMED items, read one at a
  time and never screened.

⛔ **NO ROUND-10 ARTIFACT MAY GRADE A PORTAL-DEPENDENT OUTCOME `REALIZED`.** The portal evidence lives on
drain refs contained by 0 of the portal remote's heads while the recorded gitlink `e85f6eb84f` is contained
by `origin/DEV`. Every portal-dependent outcome grades **EXERCISED**, never REALIZED, until the gitlink lands --
and a local dev render is not a publish.

*(v1.1 cut 2026-09-15 by `2.0.0_SA_COO~W` -- the POPULATED-ROUTE round from @e9d1c6e6a5; sections 1-17
unchanged and FROZEN.)*

---

## 19. ROUND 11 (v1.2, AMENDED at v1.3 before issuance) -- THE PAGE AS ANDREW DEFINED IT: one identity, one store, one header and five tabs, and the three AC6 limbs first

**Cut by `2.0.0_SA_COO~W` 2026-09-15 ~06:5xZ; AMENDED ~07:0xZ before any issuance** on `4.0.0_SA_CRO~W`'s connection brief
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_ROUND11_CUT_20260915_W.md` @`0f9a04e81e` (eight seams
against the provisional s.19 @`a0f08622ae`, every one carried below) and on **PRD v0.7 @`164ae74e06`** (TEN contracts:
C-PAGE-LAYOUT, C-ONE-STORE, C-ONE-IDENTITY, C-RANKING-GENERATION, C-ETF-PLANE-READ, C-UNION-UNIVERSE, C-SIMILARITY-RANKER,
C-POSTURE, C-FILINGS-ANALYZER, C-EXEC-MANAGEMENT; s.9f the supersession map; s.9a-2 the measurement limits). Sources of the
cut: `1.0.0_SA_CTO~W`'s L10 round-10 analysis `ledger/ROUND_ANALYSIS.round10.md` @`8d5fe78265` s.6 and `3.0.0_SA_CVO~W`'s slug
`surprise-channel/remediations/REMEDIATION_v10.md` @`e28f0b546c`. **PIN (re-pinned at 07:0xZ): PRD v0.8 @`1170b4da69`, ADMITTED** -- ratified-text half SIGNED by `3.0.0_SA_CVO~W` (stamp @`0e6592e88c`),
brief half SIGNED by `4.0.0_SA_CRO~W` (stamp @`e1d8b2d643`); v0.8's only change from v0.7 is one paragraph moved out of the ENDPOINT,
no contract changed in substance, so every cell below stands as cut. The seam map
every cell cites was measured 2026-09-15 06:1x-06:3xZ over `C:/tmp/wk-amgt-10-1/portal` @`9aef3734` (the round-10 drain ref;
the shared `portal/` checkout at `e85f6eb84f` does NOT carry the page) and the superproject at `82fab6ad44`.

**THE BOX (s.9f, Andrew's later word of 2026-09-14 @`187f003998`, verbatim in the map): "the stable server is this box, and
the lambda api calls are also this box ... local on this device with some kind of local cron job."** Every batch this round
(the union universe, the ranker, the filings analyzer, executive management, Posture) is a LOCAL job on site-Z from the
canonical library, scheduled as a Windows task DISABLED at creation; recurring activation is Andrew's word by name. NO new
Lambda and NO new terraform resource is cut for a batch. The served read path (`opal-amgt-scoped-api`, mounted at ri-4) and the
daily ranking producer (`amgt-resapp-chatter-axis`, repointed at ri-2) stay where they are and are REDEPLOYED once (rj-10).

### 19a. THE SUBTRACTION (Rule 24; the population MINUS the excluded, denominator printed; the CRO's arithmetic finding carried)

`comp-surprise --project AMGT_RESAPP --json` at HEAD `82fab6ad44`, 2026-09-15 06:3xZ: **176 investigation items, 197
adjudication rows, 123 remediation rows across 104 files; 85 ARMED by latest citing row; 0 open items.** The remediation plane
(the slug @`e28f0b546c`): 12 rows this round, 7 closed, 5 open; six earlier clocks preserved in prior slugs (S70, S72, S78 in v9;
W11-S1 in v7; C-S49 in v5; S67 and S96 disarmed by the CTO @`008ca40b6c`).

**THE POPULATION = the 5 open v10 remediation rows (S95, C-S196, S96, W17-S4, W17-S5) + the 1 carried clock the slug advanced (S72) +
the 4 new outcomes + the 10 contracts = 20 members** (the CRO's follow-up @`865e4fc113` item 7: S72 is a carried clock, not a v10
row, and W17-S4 / W17-S5 are two rows). Each is in exactly one line below; the lines are disjoint and sum to 20.

| # | member | carried by | note |
|---|---|---|---|
| 1 | S95 the ranked-click identity (open) | **rj-1** (with rj-4's crosswalk) | -- |
| 2 | C-S196 drafting paired with evidence (open) | **rj-2** (over rj-6's typed evidence) | -- |
| 3 | S72 the exact-input exercise (a v9 clock the slug advanced) | **rj-3**, LAST | -- |
| 4 | S96 the article-store contract (open; disarmed by C-ONE-STORE; the readers' repoint is the cell) | **rj-5** + **rj-9** (the route half) + **rj-10** (the package seam) | -- |
| 5a | W17-S4 (a rerun criterion reading committed state) | the CUT's own discipline (19g) | folded, not a cell |
| 5b | W17-S5 (a state census enumerating managed addresses) | the CUT's own discipline (19g) | folded, not a cell |
| 6 | FWD-16 the header | **rj-9** | -- |
| 7 | FWD-17 executive management | **rj-8** (objects) + **rj-9** (tab) | -- |
| 8 | FWD-18 the filings analyzer + the one chart | **rj-6** (objects) + **rj-9** (chart) | -- |
| 9 | FWD-19 Posture | **rj-11** (the call) + **rj-12** (tab + header line) | -- |
| 10 | C-PAGE-LAYOUT | **rj-9** | -- |
| 11 | C-ONE-STORE | **rj-5** (reader + producer) + **rj-9** (coverage route) + **rj-10** (the deployed archives carry the reader, its schema files and `jsonschema`) | -- |
| 12 | C-ONE-IDENTITY | **rj-4** (the crosswalk `crosswalk/v1`) + **rj-1** (the route boundary) | -- |
| 13 | C-RANKING-GENERATION | **rj-5** (the writer) + **rj-9** (the reader selects the committed generation) + **rj-10** (the live rerun proves it) | -- |
| 14 | C-ETF-PLANE-READ | **rj-4** | -- |
| 15 | C-UNION-UNIVERSE | **rj-4** | -- |
| 16 | C-SIMILARITY-RANKER | **rj-7** (the set) + **rj-9** (the CSC table) | -- |
| 17 | C-POSTURE | **rj-11** + **rj-12** | -- |
| 18 | C-FILINGS-ANALYZER (v0.7: passage map, held uncited claims, typed evidence, the gate against the passage) | **rj-6** | -- |
| 19 | C-EXEC-MANAGEMENT | **rj-8** | -- |

**18 members covered by 13 cells (several shared), 2 folded into the cut; 18 + 2 = 20.** NOT IN THE POPULATION, named so nobody
looks for them here: S70 / W11-S1 (the portal freeze; nothing promotes), S78 (Andrew-reserved owner), the harvest publication
collection mechanism and cadence (reserved to Andrew @`9db2a36cdc`; rj-5 reads what the pool holds), the Bloomberg-terms
question on filings (carded, open), and the recurring activation of any batch (Andrew's word). S13 is IN this round as a bounded
measurement (**rj-13**, the CRO's eighth seam and s.9a-2's "measure, then build" row) -- one security, one declared method, a
cap, a window; no feed is built.

### 19b. PLANE, GRAIN, DENOMINATOR (the remediation-v9 condition, kept)

| plane | grain | denominator at `82fab6ad44` | armed (latest citing row) | open |
|---|---|---|---|---|
| investigations (worker + seat rows) | item | 176 | -- | 0 |
| adjudications (the CVO's rows) | row | 197 | -- | -- |
| remediations (remedy rows) | row | 123 (12 new in v10) | -- | 5 (v10) + 6 preserved clocks |
| union | item | 85 ARMED by latest citing row across planes | 85 | 0 |

Per-owner ARMED figures are mentions across planes, not items, as in s.18b; none is read at a grain it does not have.

### 19c. THE CELLS -- thirteen (ids `AMGT-rj-1` .. `AMGT-rj-13`, the grammar the L6 gate reads), five chains; rj-4 is the round's first act and every other chain starts after its drain

Worker slots: `0.9.0_WK_AMGT_RESAPP~18` (A, the page: every portal edit and every edit of `lib/research/api/scoped_amgt.py`),
`~19` (B, identity + store + the one terraform act), `~20` (C, the model-side calls: filings, then Posture), `~21` (D, the
ranker), `~22` (E, executive management, then the social measurement). Every cell names its INTERFACE (19d) where another chain
consumes it, so parallel workers converge on a pool key and a function signature, never on each other's files.

**`AMGT-rj-4` THE CROSSWALK AND THE UNION UNIVERSE** (C-ONE-IDENTITY, C-UNION-UNIVERSE, C-ETF-PLANE-READ; interfaces X-1, U-1). Chain B,
FIRST of the round. (i) `crosswalk/v1/<as_of>.json` in the pool: ONE canonical identity per economic security (`<TICKER>_<CC>_Equity`)
mapped to its Bloomberg identifier (`BA US`), display ticker, model/pack key, and EVERY publication-association key already
persisted (`BA`, `security-<16 hex>` -- measured by listing `publication-links/v1/` and the pack/model-block names), with the
source universe row and each identifier's provenance; exchange and share-class preserved; an unresolved vendor identifier stays
UNRESOLVED (never `US Equity` appended, never a suffix stripped); 89 input names, ONE disposition each; re-running the mapper
mints no second record (a fixed-point test). A library `lib/research/identity/crosswalk.py` (`resolve(any_form) -> identity |
UNRESOLVED`, `aliases(identity) -> [association keys]`) is the ONE resolver every other cell calls. (ii) `universe/v1/<as_of>.json`:
the coverage list (`universe.json`, 89) UNION the four books' current holdings from `s3://opal-data-etfs` (`gold/holding/` at the
newest `snapshots/snapshot_<date>.json` vintage; the holdings layout MEASURED first -- the snapshot itself is four ETF header
objects, 2,879 bytes), one row per name `{security_key, ticker, name, source: coverage|holding|both, books, weight_by_book,
resolution, cik, filing_identity: {source: edgar|none, cik, form_expected: 10-K|20-F|none}, snapshot_date}` -- `cik` and
`filing_identity` are the CRO's second seam, produced here from the SEC ticker-to-CIK table (cached in the deliverables) and
carried for rj-6; denominators printed. READ-ONLY on the ETF plane (the object count and newest `LastModified` before and after
are the control); the counterpart contract is NOT established (v0.7's own words), so the read is one-sided and the snapshot and
schema vintage are carried on every object.

**`AMGT-rj-1` THE ROUTE BOUNDARY AND THE RANKED CLICK** (row Z-S95; C-ONE-IDENTITY; FWD-15). Chain A, after rj-4's drain. (The ranking
row's `security_key` is emitted by `rj-5`, chain B -- the CRO's follow-up item 4: two chains never edit `chatter_axis.py`; rj-1
consumes the row shape and renders a row without a key as UNRESOLVED.) The seam:
`RankedList.tsx:138` passes `row.ticker` into a slot `useSecurityAnalysisState.ts:37-39` renames `securityKey` with no transform;
`scoped_amgt.py:843-860` takes the path segment verbatim and `read_security_overlay:630` guesses `replace("_"," ")`; ranking rows
carry `ticker` only. DELIVER: the identity resolved ONCE at the route boundary through `crosswalk.py` (X-1) and carried unchanged
through overlay, thesis, peers, model, coverage, ranking and Posture; a Bloomberg form (`BA US`) or a canonical key both resolve;
neither -> `identity_status: UNRESOLVED` with the requested string echoed, no guessing; the ranking rows carry `security_key`
(the producer's `build_rows` resolves through X-1; the deploy is rj-10's); `RankedList`/`StarredList` pass `row.security_key`; a
`null` key renders an UNRESOLVED marker and does not navigate; harness arms.

**`AMGT-rj-2` DRAFTED SENTENCES BESIDE THEIR EVIDENCE** (row C-S196; FWD-9). Chain A, after rj-1 AND after rj-6's drain (its typed evidence
is the input). The seam: `scoped_amgt.py:680` hardcodes `"drafted_sections": []`; `ThesisTab.tsx:52` hides evidence in a `title=`
tooltip. DELIVER: `read_thesis_bundle` reads `drafting/v1/<key>.json` (D-1, typed evidence records with stable ids AND passage text)
from the pool, validates every evidence id's existence, association and source version through rj-6's validator before serving,
serves `drafting_status: SERVED | ABSENT | INVALID`; `ThesisTab.tsx` renders every sentence with its machine marker AND the passage
text visibly beneath it (no `title=` carrier), the verbatim verdict as the `CheckFaceBadge`; a render check asserts the passage text
sits after its sentence and before the next; the negative controls are the pipeline's (an unknown id, an empty evidence array).

**`AMGT-rj-3` THE EXACT-INPUT EXERCISE** (row S72; FWD-15, FWD-9, FWD-10; the round's AC6 judgment). Chain A, LAST of all. ONE ranked payload
and ONE thesis bundle captured from the DEPLOYED adapter (rj-10), each carrying its `generation_id`, coverage vintage and payload
hash (C-RANKING-GENERATION: a date alone cannot tell two computations apart), sha256 printed at input and at output of the
assembled page (five tabs, header, Posture line); the persisted cache (`OPAL_PORTAL_QUERY_CACHE_v1`, `staleTime: Infinity`)
cleared per arm; error and empty controls DISTINCT; the browser half the issuer's with the same hashes; the judgment for
`3.0.0_SA_CVO~W`. No live-edge or person-session claim.

**`AMGT-rj-5` ONE STORE: THE READER, THE PRODUCER, THE GENERATION** (rows Z-S96 / Z-S101; C-ONE-STORE, C-RANKING-GENERATION; interfaces P-1,
G-1). Chain B, after rj-4. DELIVER: (i) the ONE shared adapter `lib/research/coverage/pool_reader.py` (P-1) over
`publication-links/v1/{security_key}/{publisher}/{digest}.json` and `publications/v1/{publisher}/{digest}.json`: `article_key =
publisher + ':' + article_id`, `digest = sha256(article_key)`, the body's `published` mapped to the consumer's `published_at` at the
boundary (never `fetched_at`, never `first_discovered_at`); one article counts ONCE per security however many links or aliases
carry it (the legacy association aliases learned from X-1); a missing body, a malformed record, an access denial and a partial read
are DISTINGUISHABLE states from a quiet day and from an empty feed; the field-level contract is the CRO's brief @`0e7de170e3`,
read first. (ii) `chatter_axis.py` builds its 30-day histogram per `security_key` over U-1 from P-1 and its rows carry `security_key`
through X-1 (the row-shape edit is THIS cell's); the DynamoDB articles read path and the `HARVEST_ARTICLES_TABLE` knob REMOVED. (iii) THE WRITER: a rerun publishes a COMPLETE GENERATION -- the cut names
**an immutable generation partition plus a current pointer**: rows written under `axis_date = <AXIS>#<date>#<generation_id>`,
then ONE pointer item `axis_date = <AXIS>#<date>, ticker = "_CURRENT"` carrying `generation_id`, `run_id`, `coverage_vintage`,
`payload_hash`, `row_count`, `state: COMPLETE | EMPTY | FAILED`, written AFTER the rows; a successful empty product writes an EMPTY
pointer (clears the membership from the reader's view); a failed run leaves the prior pointer and writes a FAILED marker beside it;
no mixed generation is ever readable (G-1: the reader follows the pointer AND checks the rows it reads against the pointer's
`row_count`, because a GSI read is eventually consistent -- a short read is retried, then refused, never served; the CRO's
follow-up item 3). The existing all-zero-day semantics stand: TRENDING ranks ties, BREAKOUT empties (item 5), so the EMPTY arm is
BREAKOUT on an all-zero day. The measured defect (`batch_writer(overwrite_by_pkeys)` never clearing
rows; AAA#1, BBB#1, CCC#2 after a replacement run) is the negative control the tests reproduce and the new writer passes.
(iv) the difference control (pool vs table for BA, COST, HD and a name with no links); unit tests with a local fake of the two
prefixes covering every distinguishable state. The coverage ROUTE edit is rj-9's (chain A owns `scoped_amgt.py`).

**`AMGT-rj-6` THE FILINGS ANALYZER, LOCAL** (FWD-18; C-FILINGS-ANALYZER v0.7; interfaces F-1, D-1). Chain C, after rj-4's drain (CIK and
filing identity from U-1). Card 1 @`5007337353` is the working shape (read `measure_filings_analyzer.py` first; the SEC user-agent
it sets is reused, never invented; the key through `comp-secrets get anthropic-api-key --reveal`). THE CUT NAMES TWO PASSES.
DELIVER: `lib/research/filings/` -- `fetch.py` (the latest 10-K, or 20-F for a foreign private issuer, by CIK from U-1; the
document persisted with its content hash, retrieval time and parser version; `UNRESOLVED-SOURCE` explicit), `analyze.py` (pass 1:
citations on, prose per item class; pass 2: a JSON schema over pass-1 text; EVERY cited claim RESOLVES to an exact passage through
an index-to-passage map persisted beside the rows; a claim whose tag resolves to nothing is HELD uncited -- never evidence, never a
chart input), writing `filings/v1/{security_key}/{accession}.analysis.json` (F-1) and `drafting/v1/{security_key}.json` (D-1:
TYPED evidence records `{id, passage, source: {accession, sha256, location}}` beside sentences whose `evidence[]` are those ids;
`thesis_driver` EXERCISED on a real filing). The drafting library changes are THIS cell's (chain C is `lib/research/drafting/`'s
one writer this round): the reader validates existence, association and source version for every evidence id BEFORE the verbatim
gate, and the gate runs against the PASSAGE, not the title (the measured defect: the existing gate passed an unknown id with no
quotation and refused a valid body passage, three probes ~06:2xZ). QA: at least THREE filings across TWO filers including ONE
non-US name (BA and COST as 10-K filers; SAP_GY_Equity as a 20-F filer -- the measurement limit of s.9a-2), items / cited / uncited
printed per filing; a `python -m lib.research.filings.batch --universe <U-1>` CLI over the union universe with a Windows task
definition DISABLED (`schtasks /Create ... /SC WEEKLY` with the task left disabled; activation is Andrew's). NO Lambda, NO terraform.
COST stated for Andrew: about USD 1.1 and 115 s per filing at card 1's size; a full weekly batch over ~150 names is on the order of
USD 150.

**`AMGT-rj-7` THE SIMILARITY RANKER** (FWD-8; C-SIMILARITY-RANKER; interface R-1). Chain D, after rj-4's drain. As the provisional cut, with
the identity through X-1: the loader over the six scanner universe files (`s3://opal-data-portal-v2/json/security_scanner/latest/
universes/*/universe_data.json`, asOf 2026-08-06 carried as the vintage) UNION the model-block headers; rungs sector -> size band
(0.2x-5x, `engine.py`) -> country -> industry group, log-market-cap tiebreak; the Rule 24 subtraction per rung; `peers/v1/{key}/
{as_of}.json` for every resolved name of U-1 (an `absent` object with its reason for the rest); the CSC-column map as present MINUS
absent; a Seeking Alpha comparables list measured ONCE as an input candidate if reachable without the CRO's vault, else
ABSENT-ACCESS. Local batch; no deploy.

**`AMGT-rj-8` EXECUTIVE MANAGEMENT** (FWD-17; C-EXEC-MANAGEMENT; interface M-1). Chain E, after rj-4's drain AND after rj-6's drain (the
filing rj-6 persists in the pool is its roster's source; the CRO's follow-up item 4). As the provisional cut with the identity
through X-1 and the roster from the filing rj-6's fetcher persists (the executive-officer section; role start EXERCISED on a
real filing; ex-US via the 20-F where it carries the section, else UNRESOLVED-SOURCE); Lusha enrichment through the estate's
`LushaClient` (key via `comp-secrets`; profile link + title per CONFIRMED officer; no contact field stored -- the schema forbids
`email` and `phone`); a targeted IR-domain search for the CEO via `serp_brightdata`; `management/v1/{key}/{as_of}.json` and the
pool average over U-1 with its denominator. QA one-shot on BA, COST, HD and the two names rj-11 will compare. Local; no loop
started (the production loop is the harvest estate's).

**`AMGT-rj-13` THE SOCIAL SOURCE, MEASURED** (S13; s.9a-2's "measure, then build" row; C-LISTING-NOT-CAPABILITY). Chain E, after rj-8. ONE
security, ONE declared SUPPORTED method per the CRO's social brief @`36a08d3d1a` (the CRO's follow-up item 1: NOT the old cashtag
plan -- the X inventory has no keyword-post discovery): Reddit discussion search, dataset `gd_lvz8ah06191smkebj4`, `type=discover_new`,
`discover_by=keyword`, inputs `keyword`, `date`, a bounded `num_of_posts`; the job identity persisted and retrieved through the
documented delivery flow, never resubmitted per poll; a CAP (posts and USD) and a WINDOW, under the session egress word; the observables the plan names (cost, freshness, schema, latency, relevance) printed; the record filed as
`social/v1/_measurement/<as_of>.json` and a row. NO feed is built; the header's social half renders "no source measured" until a
later round cuts one from this measurement.

**`AMGT-rj-9` THE HEADER AND THE FIVE TABS** (FWD-16; C-PAGE-LAYOUT; the rendering half of FWD-17, FWD-18, FWD-8; the route half of
C-ONE-STORE and C-RANKING-GENERATION). Chain A, after rj-2 AND after the drains of rj-5, rj-6, rj-7, rj-8. Tabs = Thesis, Exec
Management, Peers, Model, Posture; the Coverage tab retired into the header feed (P-1 items newest first; social: "no source
measured (S13)"); a one-line description (a model-block header scalar if one exists, else D-1's `company_description` first
sentence marked machine, else ABSENT); the Model tab = `fiscal_year_figures` in Adam's `Model` sheet shape; Thesis = the drafted
sections (rj-2) + ONE chart of F-1's `thesis_driver` series; Peers = the CSC table over R-1; Exec Management = M-1; EVERY adapter
route edit of the round lives here: `read_coverage_set` on P-1 (via X-1's aliases); EVERY reader of a ranking partition follows
G-1's pointer and checks `row_count` -- the rankings list, the overlay's points (`scoped_amgt.py:329-338`) and the timeseries
history (`:434-438`) alike (the CRO's follow-up item 2), never a bare date partition, never a mixed generation; `generation_id` and
`payload_hash` on every ranking response; peers on R-1, management on M-1, posture on O-1 when present; ABSENT explicit everywhere;
Print a header action. Harnesses per tab; the render check over the
assembled page.

**`AMGT-rj-10` THE DEPLOY AND THE LIVE READ** (the consumer cell; C-ONE-STORE's package seam; C-RANKING-GENERATION on the live plane). Chain B,
after rj-5 AND after the drains of rj-1, rj-9 (and rj-6/7/8, whose objects the live reads exercise). ONE terraform act in the
harvest root: rebuild the scoped API zip (the round-10 closure builder, now ALSO carrying the reader's schema files and a vendored
`jsonschema` -- the package seam, exercised in an isolated runtime before upload) and the chatter-axis zip; IAM: `s3:GetObject` /
`s3:ListBucket` on `opal-data-harvest` for the prefixes `publication-links/v1/`, `publications/v1/`, `universe/v1/`, `crosswalk/v1/`,
`filings/v1/`, `drafting/v1/`, `peers/v1/`, `management/v1/`, `posture/v1/` (read) for the two roles; the DynamoDB articles table's
grants REMOVED from both (retired as a source); NO new function, NO new schedule. The whole-root plan with the managed-address
census enumerated APART from data-source entries (W17-S5), the co-sign (COO half at the cut, CTO half requested in the issuance)
covering the served-output move (coverage, thesis, peers, management, posture and rankings now serve pool objects and committed
generations), `safe-apply` with the ledger; LIVE READS: the producer's QA invoke writes a COMPLETE generation with its pointer
(rows carry `security_key`; the pointer carries `generation_id`, `coverage_vintage`, `payload_hash`); the BREAKOUT partition on an
all-zero day carries an EMPTY pointer while TRENDING keeps its tie-ranked rows (the existing semantics; the CRO's follow-up item 5),
and a re-invoke replaces the whole generation (the changed-winner control); the deployed adapter's rankings follow the
pointer; coverage for BA from the pool; thesis with N > 0 drafted sections with passages; peers derived; management for BA. The
captured payloads (with `generation_id` and hash) are rj-3's inputs.

**`AMGT-rj-11` THE POSTURE CALL** (FWD-19; C-POSTURE). Chain C, after rj-6 AND after the drains of rj-4, rj-7, rj-8. As the provisional cut:
membership at the snapshot vintage (U-1 + the holdings read, one-sided), the comparable by R-1 restricted to the OTHER side, the
judgment through the Claude API over the two evidence packs (D-1, M-1, R-1, the model block figures for BOTH names; the ETF preset
fit scores) -> `posture/v1/{key}/{as_of}.json` (O-1) `{verdict: better|worse|hold|steer_clear|absent, comparable, basis:
[{claim, cites}], as_of, generation, marked: "machine"}`; QA on BABA_US_Equity (not held) and on ONE held name from the holdings
read, with D-1/M-1/R-1 landed for BOTH names of each pair by rj-6/7/8's QA lists (the CRO's seventh seam: the QA name lists are
aligned in 19e); a subject with no comparable -> `absent` with the reason. Local; nothing trades; no schedule.

**`AMGT-rj-12` THE POSTURE TAB AND THE HEADER LINE** (FWD-19; C-PAGE-LAYOUT). Chain A, after rj-9 AND after rj-11's drain. The tab over O-1
(verdict, the comparable as a link into its own page, each basis claim with its cited pack element beside it, the machine marker,
the snapshot date) and the header's one-line posture with the same marker; ABSENT explicit.

### 19d. THE INTERFACES (what one chain writes and another reads; the pool prefixes are the contract)

| id | writer | reader(s) | pool key / signature | shape (the fields a reader may rely on) |
|---|---|---|---|---|
| X-1 | rj-4 | every cell | `crosswalk/v1/{as_of}.json`; `lib/research/identity/crosswalk.py resolve(any_form)`, `aliases(identity)` | one record per canonical identity: `{security_key, bloomberg, display_ticker, model_key, association_keys: [...], exchange, share_class, source_row, provenance, resolution}`; UNRESOLVED records kept with their raw identifier |
| U-1 | rj-4 | rj-1, rj-5, rj-6, rj-7, rj-8, rj-11, rj-13 | `universe/v1/{as_of}.json` | `{as_of, snapshot_date, schema_version, names: [{security_key, ticker, name, source, books, weight_by_book, resolution, cik, filing_identity}], denominators}` |
| P-1 | rj-5 | rj-9, rj-10 | `lib/research/coverage/pool_reader.py coverage_items(identity, days)` | `{items: [{title, url, publisher, published_at, article_key}], store_item_count, states: {missing_body, malformed, denied, partial}, read_at}` -- one article once per security |
| G-1 | rj-5 | rj-9, rj-10, rj-3 | DynamoDB `opal-harvest-security-metrics`: rows at `<AXIS>#<date>#<generation_id>`; pointer at `<AXIS>#<date>` / `_CURRENT` | pointer `{generation_id, run_id, coverage_vintage, payload_hash, row_count, state}`; rows carry `security_key`, `ticker`, `rank`, `score`, `generation_id` |
| D-1 | rj-6 | rj-2, rj-9, rj-11 | `drafting/v1/{key}.json` | the drafting schema (typed): `evidence_records: [{id, passage, source}]`, sections x sentences `{text, generated: true, evidence: [ids], verbatim_check}`, `held_uncited: [...]`, `thesis_driver`, `dropped` |
| F-1 | rj-6 | rj-9 | `filings/v1/{key}/{accession}.analysis.json` | `{source: {url, sha256, retrieved_at, parser_version}, excerpt_sha256, passage_map, items{...}, held_uncited, thesis_driver}` |
| R-1 | rj-7 | rj-9, rj-11 | `peers/v1/{key}/{as_of}.json` | `{subject, basis, members[...], denominators, universe_vintage, csc_columns{present, absent}, sa_candidates}` |
| M-1 | rj-8 | rj-9, rj-11 | `management/v1/{key}/{as_of}.json`, `management/v1/_pool/{as_of}.json` | officers[{name, role, role_start, tenure_years, profile_url, source, confirmed}], avg_tenure_years, pool_avg_tenure_years, pool_denominator; no contact fields |
| O-1 | rj-11 | rj-12 | `posture/v1/{key}/{as_of}.json` | `{verdict, comparable, basis[{claim, cites}], as_of, generation, marked: "machine"}` |
| S-1 | rj-13 | (a later round) | `social/v1/_measurement/{as_of}.json` | the measurement record: method, cap, window, cost, freshness, schema, latency, relevance |

A reader treats an absent object as ABSENT explicit, never as an empty day. Every object carries `as_of` and the vintage of what it
read. `security_key` is the canonical form everywhere in the pool; a Bloomberg ticker is a display field, never a key.

### 19e. EDGES, FANOUT, THE DRAIN CONTRACT

Edges: rj-4 -> {rj-1, rj-5, rj-6, rj-7, rj-8} (the round's first drain gates every chain); rj-1 -> rj-2 -> rj-9 -> rj-12 -> rj-3
(chain A); rj-5 -> rj-10 (chain B); rj-6 -> rj-11 (chain C); rj-8 -> rj-13 (chain E); cross-chain: rj-6 -> rj-2; {rj-5, rj-6, rj-7,
rj-8} -> rj-9; {rj-1, rj-9} -> rj-10; {rj-7, rj-8} -> rj-11; rj-10 -> rj-3; rj-11 -> rj-12.

**M = 5 dependency-independent chains after rj-4 (A, B, C, D, E); N = 5 workers; K = 8.**
`fanout: 5 of 5 chains, cap 8, reason: one worker per chain; rj-4 is spawned alone first and the other four chains spawn at its drain; chain A holds every portal and adapter-route edit, chain C every drafting-library edit, so each shared file has one writer; cross-chain cells are handed only after the cells they consume are DRAINED`

QA name lists aligned (the CRO's seventh seam; follow-up item 6): rj-6, rj-7 and rj-8 each land objects for BA_US_Equity,
COST_US_Equity, HD_US_Equity, SAP_GY_Equity (the non-US filer) and BABA_US_Equity; the held/non-held PAIR for rj-11 is chosen by
the COO at rj-7's drain from R-1 and U-1 (a held name whose ranker comparable is one of the five, or the reverse) and named in
the spawn prompts of rj-6, rj-7 and rj-8 as "up to two more QA names" BEFORE those cells drain, so rj-11 starts with both
names' objects landed.

Drain contract: every worker in a linked worktree cut from the CURRENT branch (`git worktree add -b wk-amgt_resapp-11-<n>
C:/tmp/wk-amgt-11-<n> HEAD`, a sparse cone for chains B-E); chain A's portal checkout is cut from `refs/drains/ri-1-portal`
@`9aef3734` on `wk-amgt_resapp-11-1-portal`, fetched at its drains into `refs/drains/rj-portal` (the gitlink `e85f6eb84f` NEVER
moves); chains B-E touch no portal file. The superproject drains through `safe-merge.sh` with the channel union by row id.
Hand-over order: rj-4 alone; at its drain rj-1, rj-5, rj-6, rj-7 together and rj-8 at rj-6's drain; rj-2 after rj-1 and rj-6's drain; rj-13 after
rj-8; rj-9 after rj-2 and the drains of rj-5/6/7/8; rj-11 after rj-6 and the drains of rj-7/8; rj-10 after rj-5 and the drains
of rj-1/9; rj-12 after rj-9 and rj-11's drain; rj-3 after rj-10 and rj-12.

### 19f. BOUNDS (the round's, verbatim where they are Andrew's)

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO; no push (site-Z hold); no gitlink move (`e85f6eb84f`); the page lives on
drain refs. Egress: Andrew-direct ~05:42Z @`dfa63b6d92`, "The whole sitez fabric has free egress this session" -- a worker's egress
is its issuer's, exercised through its order; every vendor call recorded with its instrument and vintage; secrets ONLY through
`comp-secrets get <name> --reveal` (Andrew-direct ~05:4xZ @`a5c6a066de`). The box is site-Z (@`187f003998`): every batch is a local
job, its task DISABLED at creation; the publication harvest's collection mechanism and cadence stay reserved to Andrew
(@`9db2a36cdc`); no cell starts recurring collection. The ETF plane is READ-ONLY and its counterpart contract is unestablished. Nothing
trades from Posture. No monitor, alarm, SNS or SES. No non-ASCII in anything that reaches AWS. LD-0521: no round-12 issuance
before the round-11 slug and analysis. A criterion a worker cannot satisfy as written is REFUSED with a row, never repaired.

### 19g. PREFLIGHT (RUN at the cut 2026-09-15 06:4xZ; the L6 gate reads the three lines)

comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21,
C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing
NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut (every batch is a local task DISABLED at creation); BLIND on
C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED,
51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1
coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. This round's IAM delta
(rj-10): READ grants by prefix on one bucket for two roles; the DynamoDB articles grants REMOVED; no Scan, no wildcard resource.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool
mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller.
The round's adversarial surfaces: filing text and vendor responses are DATA inside a model prompt (rj-6, rj-11 state so in the
prompt; the verbatim gate against the PASSAGE bounds fabrication; held-uncited claims never render); Posture is marked machine and
read by no trade consumer; the Lusha response is scrubbed to name/title/link.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; chain A adds keys under the `amgt-lead`
namespace only and changes no existing key.
comp-blast: DECLARED-NOT-APPLICABLE for every cell but rj-10; rj-10's blast is the two functions' code and IAM and the routes'
served payloads, covered by the co-sign; the plan's 0-destroy line and the managed-address census are its criteria.
Criteria discipline from W17-S4/W17-S5: every rerun-able criterion reads COMMITTED state (`git log` beside any `git status`);
every state census enumerates managed addresses APART from data-source entries and never a literal total; every large-apply
criterion greps tokens over the saved output rather than `tail`-ing a window; every expectation is a regex-safe pattern.

### 19h. RULE 24 RECORD

(i) MECE over the declared domain: 19 members (the 5 open v10 rows + the 4 new FWD cards + the 10 contracts the CVO enumerated),
each in exactly one line of 19a, 18 covered + 1 folded = 19; the domain's own choice falsified by one unscoped read (the slug's
carries, the ENDPOINT's cards, the CONTRACTS section's bold names). (ii) Same grain: every cell is one deliverable set with its own
proof instance; the pool prefixes are one object per (key, as_of); a generation is one object per (axis, date, generation_id).
(iii) One intent per cell: identity (rj-4, rj-1), evidence (rj-2), exercise (rj-3), store (rj-5), analysis (rj-6), similarity
(rj-7), management (rj-8), social measurement (rj-13), page (rj-9), deploy (rj-10), posture (rj-11, rj-12). (iv) State coherence:
rj-10 is the ONLY cell that moves the live plane; a cell's QA one-shot writes pool objects and nothing else; the values one remedy
does not move are named in each cell (rj-1 does not deploy; rj-6 does not run the batch; rj-8 does not start the loop; rj-11 does
not schedule; rj-13 builds no feed).
---

## 20. ROUND 12 (v1.4) -- FROM THE L10 ROUND-11 ANALYSIS @`c708914c50`, ADDENDUM 1 @`1db70c8e87` AND ADDENDUM 2 @`06378dd3bd`

**Cut by `2.0.0_SA_COO~Z`**, the first round this lane holds. Continuity ruled by `1.0.0_SA_CTO~Z` (msg 23365) on
Andrew-direct ~04:5xZ, *"yeah we also need COO~Z and CVO~Z for full tier1 on this project"* (record `c05a41c0f4`).
**Rounds 1-11 are FROZEN and unchanged**; rounds 10-11 were held by `2.0.0_SA_COO~W` and that record stands.

**SIXTEEN cells, ids `AMGT-rk-1` .. `AMGT-rk-16`** (thirteen at v1.4; `AMGT-rk-14` at v1.5 s.20h; `AMGT-rk-15` and `AMGT-rk-16` at v1.6 s.20i) -- the analysis's A-M, remapped into dependency order. The letters
are the CTO's (WHAT); the ids, chains and fan-out are this seat's (HOW), per s.5's own division.

### 20a. THE SUBTRACTION (Rule 24) -- over the PRD's OUTCOMES against the SERVED PLANE

⛔ **THE DOMAIN IS THE PRD'S OUTCOMES, NOT THE PREVIOUS ROUND'S FINDINGS.** This is the standing instruction
Addendum 1 A1.1 minted for every later round of this project, and it exists because this seat got the domain wrong
first: at msg 23371 it differenced the packet's section 5 against the slug's six obligations, got 24 ids each with 15
shared, and reported the agreement as corroboration. ⛔ **IT WAS NOT.** Both are round-11 artifacts and round 11 never
looked at the DEV branch or invoked the print route, so the two instruments were blind in the same place and agreed
*because* they were blind in the same place -- Rule 22's shared-dependency blindness, which this seat named in its own
message and then did not apply to its own pair. What caught it was a SEPARATE SEAT pointed at the product
(`4.0.0_SA_CRO~Z` @`a10eece02e`). **The instrument correction is recorded rather than quietly dropped.**

**DENOMINATOR: 20 outcomes**, `FWD-1..FWD-20`, PRD **v0.9 @`44269d0515`** (FWD-20 appended at v0.9; ids permanent,
never reused). **SERVED-PLANE STATE** from `4.0.0_SA_CRO~Z`'s product-existence audit @`a10eece02e` -- an independent
seat on a different instrument (direct Lambda invoke, zip listing, `git ls-tree` on the portal, Task Scheduler, boto3
pool inventory), never this lane's own read.

**THE SUBTRACTION = 20 outcomes MINUS those a cell in `A`..`M` covers = the UNCOVERED PARTITION.** Written as a
subtraction from the printed denominator, never as a forward list of what was thought of.

⛔ **AND THE ANSWER IS NOT ZERO. THREE ITEMS SURVIVE THE SUBTRACTION, AND THIS SEAT IS SURFACING THEM, NOT CUTTING
THEM** -- adding a cell the analysis did not name would be this lane re-scoping WHAT, which is the CTO's. Each is an
OPEN CALL routed to `1.0.0_SA_CTO~Z`:

| # | uncovered | measured | instrument |
|---|---|---|---|
| U1 | **`FWD-18`'s one chart** -- *"the one chart that matters is drawn from them"* | the thesis driver chart is **ABSENT 5 of 5**; no numeric driver series exists, segments are prose. `W18-S12` occurs **ONCE** in the whole 400-line analysis -- in s.3's "what does not serve today" table -- and **ZERO times** in the cell text of s.5 A-H or either addendum | count over the analysis text, cell-section scoped and then unscoped |
| U2 | **`FWD-6`'s compare surface** -- *"naming the earlier version that shows it"* | the version STORE exists (bucket versioning Enabled, timestamped `derived/model_block/<key>/<stamp>/`); the **compare-two-versions surface is ABSENT**, 0 hits for version / earlier / compare in the page components. `FWD-6` occurs **ZERO** times in the analysis | CRO audit s.1 row S6; count over the analysis |
| U3 | **the slug's obligation-2 residue** | `W18-S13` / `W21-S6` (CSC values and horizons), `W21-S5` (currency and vintage comparability), `W20-S10` (fit inputs) are named in the round-11 slug's obligation 2 and in **no** cell's text. `W20-S9` is `1.0.0_SA_CTO~Z`'s own row | the same count, run over each id |

⚠ **U1 AND U2 ARE THE SAME CLASS ADDENDUM 1 ALREADY CAUGHT ONE LEVEL DOWN** -- an outcome whose *record* is healthy and
whose *surface* was never built. They are offered in exactly that spirit and with no claim that the cell set is
otherwise incomplete: `FWD-3`, `FWD-10` and `FWD-11` also occur zero times in the analysis, and each is correctly
covered anyway -- provenance and the check face ride the page cell, and the social source is `G`'s classify-only
mandate by ruling. **Absence from the analysis text is not by itself a gap; U1-U3 are named because their SURFACE is
absent on the served plane as well.**

⭐ **AND ONE AXIS SITS ABOVE ALL THIRTEEN CELLS**, found by `1.0.0_SA_CTO~Z` from `4.0.0_SA_CRO~Z`'s projection and
recorded here because it governs how this round's bars are written: **cells A-M repair the PLANE, never the
POPULATION.** 10 of 19 outcomes stay ABSENT for a non-pilot covered name after every cell lands. **No count bar in
this round may be cut as though the population were the coverage list.** The two cards that would move it (the
model-block pull over the 33 keyed names; the filings batch) are **RESERVED at Andrew** and are not cells.

### 20b. PLANE, GRAIN, DENOMINATOR -- the three that decide whether a criterion can fail

1. **EVERY BAR READS THE DEPLOYED PLANE, NEVER HEAD.** Round 11 passed 83 of 83 explicit criteria while the product's
   central page served zero model figures; the one JUDGMENT criterion is what caught it. A capture from source is not
   evidence about what a person opens.
2. **THE HONEST DENOMINATORS, READ AT THE CUT AND NOT ASSUMED** (Addendum 1 R5, and `W19-S8` is the round-11 row filed
   for exactly this): the article pool is **7 bodies over 3 names**; `derived/model_block/` holds **3 covered keys of
   89 coverage / 256 universe** plus NVDA, which is not covered (`4.0.0_SA_CRO~Z`'s own correction against its first
   figure of 4); filings and drafting are **5 pilot names**; `peers/v1` is 33 objects with **10** carrying members;
   `posture/v1` is **2** keys. ⛔ **A cell that writes a count bar re-reads its store AT THE CUT and PRINTS the
   denominator beside the number** -- a bar of "80% of covered names" against a 3-key store is a refused criterion.
3. **GRAIN:** a criterion names the exact route, the exact capture filename, and the exact key. `W20-S1`'s defect was a
   grain mismatch between a pre-census and a post-census; `F` is the cell that repairs the class at the issuer.

### 20c. THE CELLS -- thirteen, ids `AMGT-rk-1` .. `AMGT-rk-13`

⛔ **THE FULL ID IS WRITTEN IN EVERY HEADING AND IN EVERY TASK ORDER.** The L6 gate resolves cell ids by REGEX over
this file's text (`CELL_ID_RE`, `to-pipeline-gate.py:262`), so a bare `rk-1` in the decomposition against `AMGT-rk-1`
in the order is a refusal. Validated at the cut with controls: `AMGT-rk-1`, `AMGT-rk-9`, `AMGT-rk-12` and
`AMGT-rk-13` all fullmatch; `rk-1`, `AMGT-rk1`, `amgt-rk-1`, `AMGT-RK-1` and `AMGT-rkkkkk-1` are all refused.

| id | letter | what it must cover | closes | chained after |
|---|---|---|---|---|
| **`AMGT-rk-1`** | **I** | **FIRST.** Merge the page into portal **DEV** and read a render. 48 SecurityAnalysis files and the `/security-analysis` route exist only at `refs/drains/rj-portal` `b616b759`; DEV `be8cf218` carries 0 of 48. COMMIT-class, freeze reads COMMIT YES / PROMOTE NO. ⛔ **The DEV PUSH is RESERVED (LD-0367/0368) and no cell takes it** -- the cell commits LOCALLY and states push state LOCAL. `merge-tree` measures conflicts, not TypeScript: DEV is 212 commits past the merge-base, so the cell runs `tsc -b` on the merged tree | G1 | root |
| **`AMGT-rk-2`** | **A** | Redeploy the adapter from HEAD and grant the adapter role `derived/model_block/` READ under a **FRESH never-widen co-sign** (CTO half + COO half, each naming blast radius and per-key rollback, each COUNTING THE WRITERS of every named property). Assert from a **deployed-plane capture**: nonzero model figures, `packs` present, `comparable_name` present, classed ABSENT reasons elsewhere. **JUDGMENT CRITERION, as corrected by Addendum 2 C3:** it names the page (`BA_US_Equity`) and prints the `derived/model_block/` key count at the cut beside the verdict -- a judgment criterion still carries a printed denominator | W19-S13, Z-S107; moves FWD-8, FWD-19 | root |
| **`AMGT-rk-3`** | **B** | Build the Price generation writer. Every Price list today is ABSENT **by absence, not by measurement** -- the producer has never written a generation | W18-S11 (ARMED), Z-S105 | root |
| **`AMGT-rk-4`** | **C** | Resolve holdings **without converting unknown to false** (167 of 170 unresolved because the plane carries a bare ticker and the contract rightly forbids guessing `US`). The Positioning chain already resolves **164 of 164** by CUSIP/FIGI/SEDOL/Bloomberg security -- **that chain is the input, never a bare-ticker join.** Repair company-FIGI deduplication and the 23 empty peer subjects | W19-S6, W20-S13, W21-S3 (ARMED), W21-S4 | root |
| **`AMGT-rk-5`** | **D** | Tab scores: a Bloomberg **quarterly** pull for Robustness's six inputs on the 8-point TTM window at `FUND_PER=Q`; Peers V with subject cap and member guards; Divergence D on the ruled CFPS/EPS dispersion proxy. **Every ABSENT CLASSED before it counts.** ⛔ `integrations/bloomberg/READ_HERE.md` is read FIRST; `BEST_*` defaults to the next QUARTER and a bare identifier resolves to the WRONG security, so `BEST_FPERIOD_OVERRIDE` is set and `NAME` is checked before any measure is read | FWD-17, FWD-20's reporting side | `AMGT-rk-4` |
| **`AMGT-rk-6`** | **J** | Package the print pack **server-side** so `FWD-5` serves. Today the route returns **500**: the deployed archive (747,396 B, 183 entries) carries no matplotlib, no pypdf, no numpy, `render_pack.py` imports matplotlib at module level and reads a worker-local deliverables folder plus a OneDrive template path. Ruled NOT a browser act -- the displacement test is that a person forwards the output AS PRODUCED | G3, FWD-5 | `AMGT-rk-2` |
| **`AMGT-rk-7`** | **K** | Wire the on-demand pull: the adapter declares the queue carrier (today `/refresh` answers **501**) and the page calls the enqueue route it never calls today. ⛔ **CORRECTED BY ADDENDUM 2 C1 -- THE CONSUMER STAYS ON THE BOX AND NO LAMBDA CONSUMER IS BUILT:** `pull_consumer.py` calls the Bloomberg DAPI at `127.0.0.1:8194`, so a Lambda would drain the queue and fail every message at `bloomberg_health`. FWD-2 has already worked end to end once (`packs/NVDA_US_Equity/status.json` LANDED). Cadence is a card, not a cell. ⛔ No alarm, monitor or freshness machinery rides along | G4, FWD-2 | `AMGT-rk-2` |
| **`AMGT-rk-8`** | **E** | Both the mechanical and the browser exercise take the **same five routes** captured from the deployed adapter (`/overlay`, `/peers`, rankings, thesis, posture). Round 11 captured two, so the header description, the feed and the whole Peers panel were outside what could be exercised at all. ⭐ Chained after `AMGT-rk-1` because round 11's browser half exercised a LOCAL vite serve -- only after the DEV integration do the front-end and the deployed adapter meet on the plane a person would use | W18-S20, W18-S5 | `AMGT-rk-1`, `AMGT-rk-2` |
| **`AMGT-rk-9`** | **F** | **Criteria repair AT THE ISSUER.** Every test criterion asserts a **nonzero collected denominator**; upstream exit status is read; pre/post censuses use an identical grain; capture filenames are exact; staged and cold timeout bounds are stated. ⭐ **A criterion that cannot fail is not a criterion** -- round 11 shipped two (a suite over an empty collection, a verbatim gate over input carrying no quotation marks) | W18-S1, W20-S1 | root |
| **`AMGT-rk-10`** | **G** | **NOT a build cell.** Classify the social source -- source absence versus failed primitive -- and report: 48 records, 0 admitted, a 713-second job, cost unmeasurable with that key. ⛔ **Recurring collection stays RESERVED to Andrew by name (@`9db2a36cdc`) and nothing here enables it** | W22-S3/S6/S7/S8 | root |
| **`AMGT-rk-11`** | **H** | **Record the preserved breaches, do NOT replay them:** BA's 4-versus-2 Lusha credits, ten off-order legacy writes after a blocked deploy, the late per-act rollback receipt, two Posture writes under a one-write bound. Future cells carry cumulative budget checks and fail-closed sequencing. ⛔ **Do NOT replay world acts or restore unknown prior contents to improve a receipt** | W22-S2, W19-S16, W19-S19, W20-S14 | root |
| **`AMGT-rk-12`** | **L** | Served route + page surface for `FWD-7`, `FWD-12`, `FWD-14` -- each today a Python module a person runs by hand, 0 of 11 mounted routes, 0 page components. ⛔ **CORRECTED BY ADDENDUM 2 C2:** `ledger.py`'s CLASSES carries `stage: None` for 6 of 6, so a re-run control over it records SKIPPED every time. The control **REFUSES WITH A NAMED REASON** where activation is reserved, or ships READ-ONLY with the re-run stated as round 13 **in the issuance data**. ⛔ **Never a button that does nothing** | FWD-7, FWD-12, FWD-14 | `AMGT-rk-1`, `AMGT-rk-2` |
| **`AMGT-rk-13`** | **M** | Re-run the **similarity ranker** over the names `AMGT-rk-4` newly resolves. Without it `C` yields a better crosswalk feeding the same ten populated peer sets | FWD-8's population | `AMGT-rk-4` |

### 20d. INTERFACES -- what one chain writes and another reads

- `AMGT-rk-2` publishes the **deployed adapter vintage**; `AMGT-rk-6`, `AMGT-rk-7`, `AMGT-rk-8` and `AMGT-rk-12` all
  read a capture from THAT deployment. A cell that captures before `AMGT-rk-2` lands is capturing the old bytes --
  which is precisely `Z-S107`, the defect round 11 shipped.
- `AMGT-rk-4` publishes the **resolved identity set**; `AMGT-rk-5` and `AMGT-rk-13` read it. The pool prefixes are the
  contract: `crosswalk/v1/`, `universe/v1/`, `peers/v1/`.
- `AMGT-rk-1` publishes the **portal DEV branch state**; `AMGT-rk-8` and `AMGT-rk-12` render against it.
- `AMGT-rk-9` publishes the **criteria shape** the drain grades every other cell against; it is a root so that its
  output exists before the first proof instance is graded.

### 20e. EDGES, FAN-OUT, AND THE DRAIN CONTRACT

**FAN-OUT, STATED AS DATA (it goes into the L6 issuance commit verbatim):**

```
fanout:
  cap: 8                      # the default; not raised
  waves: 3
  wave_1_roots: [AMGT-rk-1, AMGT-rk-2, AMGT-rk-3, AMGT-rk-4, AMGT-rk-9, AMGT-rk-10, AMGT-rk-11]   # 7
  wave_2:       [AMGT-rk-5, AMGT-rk-6, AMGT-rk-7, AMGT-rk-12, AMGT-rk-13]                          # 5
  wave_3:       [AMGT-rk-8]                                                                        # 1
  max_open_width: 7           # 7 <= 8, so NOTHING is deferred for width
  deferred_for_width: []      # empty, and stated rather than omitted
```

⭐ **THE WHOLE ROUND FITS INSIDE THE DEFAULT CAP.** Addendum 1 R4 said that if fan-out could not carry `L`, `L` moves
to round 13 **stated as data rather than taken by omission**. Measured here: max open width is **7 against a cap of
8**, so `AMGT-rk-12` is carried in round 12 and `deferred_for_width` is **empty**. The empty list is written down
precisely so a later reader can tell "nothing was deferred" from "nobody looked".

**WORKER SLOTS.** Branches are `wk-amgt_resapp-12-<n>`, directories `/c/tmp/wk-amgt-12-<n>`. ⛔ **THE DIRECTORY NAME
AND THE BRANCH NAME DIFFER AND ALWAYS HAVE** -- `git branch --list 'wk-amgt-*'` returns ZERO and reads exactly like
"no branches exist". Measured at the cut: 0 `wk-amgt_resapp-12-*` branches and 0 `/c/tmp/wk-amgt-12-*` directories,
so round 12's names are free. The 13 round-11 worktrees stay in place -- removal is on Andrew's word
(ROUND11_PACKET.md s.6).

**DRAIN CONTRACT.** Every order drains with its proof instance graded at HEAD; a JUDGMENT criterion is graded at L9
and never self-graded; a compound criterion is refused at the cut, one clause per criterion with its invocation and
its expectation. **At least one judgment criterion per chain**, because round 11's single judgment clause is the only
thing that caught a page serving nothing behind 83 passing mechanical criteria.

### 20f. BOUNDS -- the round's, verbatim where they are Andrew's

- **PORTAL: COMMIT YES / PROMOTE NO.** *"No portal promote necessary"* (~04:3xZ) removes the PROD promote from the
  goal's definition of done. ⛔ It does **not** license a promote, does **not** lift the freeze, and says nothing
  about committing portal code. The portal DEV **push** is RESERVED under LD-0367/0368 and is a card at Andrew.
- **COLLECTION STAYS OFF.** Three Windows tasks DISABLED over a seven-body pool is the **measured consequence of a
  RESERVED decision, not a defect to fix**. The harvest mechanism and cadence are Andrew's by name (@`9db2a36cdc`).
- **THE TWO CARDS ARE ANDREW'S AND ARE NOT CELLS:** the model-block pull over the 33 keyed names, and the filings
  batch (~USD 1.1 per filing). ⛔ **Vendor use is never authorized by availability.** Without them the finished
  product is FIVE NAMES, and the completion report must say so rather than let the register imply otherwise.
- **NO ALARM, MONITOR, SNS/SES-SEND, NOTIFICATION OR FRESHNESS CHECKER** -- standing moratorium. A wired queue is not
  a monitor.
- **THE ETF PLANE IS READ-ONLY.** Secrets through `comp-secrets` only. **Lusha: the one authorized enrich stays
  UNUSED** under the documented contract (the endpoint returns emails and phones when `reveal` is omitted and carries
  no dates), and contact data is never stored.
- **MID-ROUND THE SPEC AND THIS DECOMPOSITION ARE FROZEN.** The only off-spec act is a surprise ROW appended to
  `surprise-channel/investigations/INVESTIGATION_v{N}.md`, and the worker keeps working.
- **PUSH:** LOCAL on SITEZ for every act in this round; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.

### 20g. BATTERY DISPOSITION -- mandatory core ALL THREE RUN, plus the COO minimum, denominators printed

| lens | verdict | denominator measured at this cut |
|---|---|---|
| `comp-schedule` | **RUN** | 5 of 5 carriers scanned in 16.25 s of a 90 s budget; **0 gates ARMED** for this scope. C1 sentinel 23, C2 deploy-ledger 7 open, C3 moratoria **12 standing NEVER clauses**, C4 scope-guard 21 (SEMI-DECIDABLE, listed never counted), C5 project-blocking 334 (NOT-DECIDABLE, a reading list). The 12 moratoria are what s.20f binds onto cells |
| `comp-iam` | **RUN** | 214 roles, 190 services, 1114 operations, **321 permission gaps**; 3 trees / 478 `.tf`; 407 policy blocks attached, **27 NOT ATTACHED**, 13 standalone. ⛔ **AND THE INSTRUMENT IS BLIND WHERE `AMGT-rk-2` NEEDS IT:** `comp-iam service opal-amgt-scoped-api` returns **3 operations, all `UNRESOLVED-RESOURCE`** (DynamoDB `Table()` via an untraced helper) and **no S3 row at all**. Its own banner says the list is a FLOOR and never a deletion warrant. **So the never-widen co-sign for `derived/model_block/` reads the Terraform directly and does not rest on this tool's silence**, and the DESIRED plane is not the APPLIED one |
| `comp-adversary` | **RUN** | declaration carried in the L5 commit message |
| `comp-routes` (COO minimum) | **RUN** | 7 origins, 29 behaviors, 14 rewrites, 22 API GW routes, 163 frontend endpoints (66 with URLs), **24 component bindings**, 66 resolved routes; 50 of 66 edge-auth, 24 of 66 API-GW auth. ⭐ **AN INDEPENDENT CORROBORATION OF G1 ON A DIFFERENT INSTRUMENT:** this tool parses `portal/src` at the working tree, which is DEV -- and **none of the 24 component bindings is a SecurityAnalysis component.** `4.0.0_SA_CRO~Z` reached the same conclusion by `git ls-tree` and `merge-tree` on the portal repo. Two instruments, two seats, one answer: the page is not on the branch a person is served from |
| `comp-cache` (COO minimum) | **RUN** | 646 of 646 portal source files scanned, 120 of 120 `useQuery` call sites captured, 0 unparseable; **17 shared keys, 0 with a TYPE MISMATCH** (the bug class). No round-12 cell inherits a cache-key collision |
| `comp-blast` | **DNA** | no served-output MOVE in this round's cells; `AMGT-rk-2`'s deploy is covered by the never-widen co-sign, which is the narrower and correct instrument |

⚠ **THE BATTERY'S OWN LIMIT, STATED:** `comp-iam` and `comp-routes` are **DESIRED-plane** (parsed Terraform and
committed source). Neither can tell a declared grant or behavior from a deployed one. Every bar in this round that
asserts a grant or a route is therefore graded on a **live read or an invoke**, never on a battery figure.
### 20h. AMENDMENT v1.4 -> v1.5 -- CELL `AMGT-rk-14` (the FIT), from ADDENDUM 3 @`e2ff09a835`

**Amended BEFORE issuance, so nothing is frozen and no order is re-cut.** `1.0.0_SA_CTO~Z`'s self-drive
tick 2 sent cell **N** deliberately early *because* this seat was mid-L5; that is the round-N analysis
reaching the decomposition before the cut rather than after it, which is the whole point of the loop.

| id | letter | what it must cover | closes | chained after |
|---|---|---|---|---|
| **`AMGT-rk-14`** | **N** | **THE FIT, BOTH ENDS IN ONE CELL.** The presets carry counts and weights instead of factor-code lists (DIVZ names 7 of 13, PFOE 0 of 16, so **22 of 29 preset slots have no code to read**), and R-1's rows carry **no scanner factor values at all** because the ranker's loader keeps the 284-code set and DROPS THE NUMBERS BY DESIGN. Ruled: (1) the presets name EVERY code they score under, 13 of 13 DIVZ and 16 of 16 PFOE, **printed denominator beside each**; (2) the loader RETAINS values for exactly those codes on the R-1 rows -- bounded by the presets, never by the scanner's width; (3) ABSENT carries a CLASSED reason where a named code has no value; (4) the criterion asserts a **NONZERO FACTOR COUNT ON A REAL NAME**. ⛔ **NOT retiring the fit** -- it is part of the surface Andrew approved (PRD s.3b), so retirement is an ENDPOINT change and a card at Andrew, never a quiet drop | W20-S9, W20-S10 | `AMGT-rk-4`, `AMGT-rk-13` |

⭐ **WHY IT IS ONE CELL AND NOT TWO, CARRIED HERE BECAUSE IT IS A CUTTING RULE AND NOT A DETAIL:** the fit
needs **a code to read AND a value to read for it**, and repairing either end alone moves nothing while
grading as progress. Name the 22 codes against rows carrying no values and the score is still ABSENT;
retain values for codes the preset never names and the score is still ABSENT. **A cell that fixes one end
and passes its criterion is the failure mode here** -- which is `AMGT-rk-9`'s criteria-that-cannot-fail
class, applied BEFORE the cut instead of found after it.

**FAN-OUT, RESTATED WITH `AMGT-rk-14` (this supersedes the block in s.20e):**

```
fanout:
  cap: 8                      # the default; still not raised
  waves: 3
  wave_1_roots: [AMGT-rk-1, AMGT-rk-2, AMGT-rk-3, AMGT-rk-4, AMGT-rk-9, AMGT-rk-10, AMGT-rk-11]   # 7
  wave_2:       [AMGT-rk-5, AMGT-rk-6, AMGT-rk-7, AMGT-rk-12, AMGT-rk-13]                          # 5
  wave_3:       [AMGT-rk-8, AMGT-rk-14]                                                            # 2
  max_open_width: 7           # UNCHANGED -- rk-14 lands in wave 3, which was the narrowest
  deferred_for_width: []      # still empty, and still stated
```

⚠ **THE FOURTEENTH CELL COST NOTHING IN WIDTH.** `AMGT-rk-14` chains after `AMGT-rk-4` and `AMGT-rk-13`,
so it falls into wave 3 beside `AMGT-rk-8` -- the narrowest wave. Max open width stays **7 of 8** and
`deferred_for_width` stays empty. Recorded because "we added a cell and the fan-out did not move" is the
kind of claim that should carry its arithmetic.

**WHAT THIS AMENDMENT DOES TO s.20a's UNCOVERED PARTITION -- it CLOSES part of U3 and leaves the rest:**

| was | now |
|---|---|
| **U3** `W20-S9` / `W20-S10` (the fit inputs) | **COVERED by `AMGT-rk-14`.** ⭐ Two seats reached this independently on DIFFERENT instruments -- this seat by counting row ids over the analysis text and finding `W20-S10` in no cell, `1.0.0_SA_CTO~Z` by reading the slug's obligation 2 against the cell set on a self-drive tick. That is corroboration in Rule 22's sense, and it is worth contrasting with msg 23371's pair, which was NOT |
| **U3** `W18-S13` / `W21-S6` (CSC values and horizons), `W21-S5` (currency and vintage comparability) | **STILL UNCOVERED.** Named in the slug's obligation 2, in no cell's text |
| **U1** `FWD-18`'s one chart (`W18-S12`) | **STILL UNCOVERED** |
| **U2** `FWD-6`'s compare surface | **STILL UNCOVERED** |

**ROUND 12 IS FOURTEEN CELLS: `AMGT-rk-1` .. `AMGT-rk-14`.** Every other clause of s.20 stands unchanged,
including the bounds in s.20f and the battery in s.20g -- the battery was run against the cut and adding a
cell that reads existing pool prefixes moves none of its denominators.
### 20i. AMENDMENT v1.5 -> v1.6 -- CELLS `AMGT-rk-15` and `AMGT-rk-16`, and `AMGT-rk-14` EXTENDED, from ADDENDUM 4 @`4055200e2f`

**Amended BEFORE issuance again, so nothing is frozen and no order is re-cut.** These are the three open
calls s.20a raised (U1, U2, the U3 remainder), ruled by `1.0.0_SA_CTO~Z`. **Two became cells; one was
folded into an existing cell rather than given its own**, and the folding argument is the interesting half.

| id | letter | what it must cover | closes | chained after |
|---|---|---|---|---|
| **`AMGT-rk-15`** | **O** | **`FWD-18`'s ONE CHART.** The ACCEPT promises "one chart, chosen for that company, of the thing it lives or dies on". Measured: the driver chart is ABSENT 5 of 5 and `thesis_driver` is a **NAMED SERIES WITH NO NUMERIC POINTS**. Ruled: the filings analyzer emits the driver as a **numeric series with its points and their units**, not only a name; the Thesis tab draws that one chart; ABSENT-explicit with a classed reason where the filing carries no series. ⛔ **THE CRITERION ASSERTS A NONZERO POINT COUNT ON A REAL NAME, never the presence of the field** -- a named series with no points is the same shape as a control that cannot act: it satisfies "the field is populated" and renders nothing | W18-S12, FWD-18 | `AMGT-rk-1`, `AMGT-rk-2` |
| **`AMGT-rk-16`** | **P** | **`FWD-6`'s COMPARE SURFACE.** The outcome promises an analyst can say what changed, **NAMING the earlier version**. Measured: the STORE EXISTS (versioning Enabled, four timestamped stamps for BA) and the SURFACE IS ABSENT (0 hits for version / earlier / compare in the page components). Ruled: the page gets a compare-two-versions surface reading the store that already serves -- current beside earlier, what moved, the earlier version NAMED | FWD-6 | `AMGT-rk-1`, `AMGT-rk-2` |

**`AMGT-rk-14` (N) IS EXTENDED, NOT SPLIT.** It now also carries the CSC columns carrying values **with
their horizon labelled** (trailing vs NTM, never a fiscal-year label over an NTM figure) and the size band
**comparable across currencies and vintages** with the FX basis and vintage named, or ABSENT with that
reason. ⛔ **ITS CRITERION PRINTS FOUR DENOMINATORS PER NAME** -- codes named, values present, horizons
labelled, FX basis stated -- **and is not a boolean.**

⭐ **WHY THE U3 REMAINDER FOLDED INSTEAD OF BECOMING ITS OWN CELL, kept because it is a CUTTING RULE:**
`W18-S13` / `W21-S6` / `W21-S5` are **the same rows, the same loader and the same property** as the fit --
a value that is present AND comparable. Giving them their own cell would repeat, one layer up, the exact
both-ends error `AMGT-rk-14` was created to prevent: **a cell could retain values that are not comparable
and still pass its criterion.** The fold is the same argument as the cell, applied to the cell's own scope.

⚠ **AND `AMGT-rk-16` IS THE ONE TO NOTICE:** the hard half -- immutable versioned history -- is already
built and serving; only the reading surface is missing. **That is exactly why it went unnoticed, because
every PRODUCER census says this outcome is fine.** An outcome can be complete at the producer and absent
at the person.

**FAN-OUT, RESTATED WITH ALL SIXTEEN (this supersedes s.20e and s.20h):**

```
fanout:
  cap: 8                      # the default; still not raised
  waves: 3
  wave_1_roots: [AMGT-rk-1, AMGT-rk-2, AMGT-rk-3, AMGT-rk-4, AMGT-rk-9, AMGT-rk-10, AMGT-rk-11]   # 7
  wave_2:       [AMGT-rk-5, AMGT-rk-6, AMGT-rk-7, AMGT-rk-12, AMGT-rk-13]                          # 5
  wave_3:       [AMGT-rk-8, AMGT-rk-14, AMGT-rk-15, AMGT-rk-16]                                    # 4
  max_open_width: 7           # UNCHANGED across three amendments -- wave 1 is still the widest
  deferred_for_width: []      # EMPTY. Nothing moves to round 13.
```

⛔ **NEITHER NEW CELL IS DEFERRED, AND THAT IS A MEASUREMENT RATHER THAN A PREFERENCE.** Addendum 1 R4 and
Addendum 4 s.6 both require that a cell which does not fit the cap move to round 13 **as data stated in the
issuance, never by omission**. Measured: `AMGT-rk-15` and `AMGT-rk-16` both chain after `AMGT-rk-1` and
`AMGT-rk-2`, so they land in **wave 3**, which was the narrowest wave at 1. Wave 3 goes 1 -> 4 and
**max_open_width stays 7 of 8** because wave 1 is and remains the binding wave. `deferred_for_width` stays
EMPTY, written down rather than omitted, so a later reader can tell "nothing was deferred" from "nobody
looked".

**CHAINING NOTE, BECAUSE IT DEPARTS FROM THE ANALYSIS'S WORD AND THE DEPARTURE IS THIS SEAT'S TO MAKE.**
Addendum 4 calls `AMGT-rk-16` "independent". Chaining is the COO's (s.5's own division, restated at
Addendum 4 s.6), and this seat chains it after `AMGT-rk-1` and `AMGT-rk-2` because **a page surface needs a
page to sit on and a deployed adapter to read through**: the compare surface is a page component, and until
`AMGT-rk-1` puts the page on DEV there is no branch to add a component to, and until `AMGT-rk-2` redeploys
there is no served route for it to read. Cutting it as a root would produce a cell that can be BUILT but
not EXERCISED, and this round's bars are exercised on the deployed plane. The same reasoning places
`AMGT-rk-15`. **It costs nothing: neither is deferred and the width does not move.**

**ROUND 12 IS SIXTEEN CELLS: `AMGT-rk-1` .. `AMGT-rk-16`.** s.20a's uncovered partition is now EMPTY --
U1 -> `AMGT-rk-15`, U2 -> `AMGT-rk-16`, U3 -> `AMGT-rk-14` (the fit half at v1.5, the remainder here.)
Every other clause of s.20 stands, including the bounds in s.20f and the battery in s.20g.

### 20j. AMENDMENT v1.6 -> v1.7 -- CELLS `AMGT-rk-17` and `AMGT-rk-18`, from ANDREW-DIRECT 2026-09-16 ~19:2xZ

⛔ **THIS ONE IS DIFFERENT FROM 20h AND 20i AND THE DIFFERENCE IS STATED RATHER THAN GLOSSED.** Both earlier
amendments say *"amended BEFORE issuance, so nothing is frozen and no order is re-cut."* **THIS AMENDMENT IS
AFTER ISSUANCE.** Round 12 is at L7 with ten of sixteen orders terminal and three workers live. The
mid-round freeze on the decomposition is real and it binds a SEAT'S OWN JUDGMENT; it is moved here by the
only two things above it: **Andrew's own word, and the adjudicator's routing of that word.**

**THE AUTHORITY, VERBATIM AND ENTIRE.** Andrew, 2026-09-16 ~19:2xZ at the `1.0.0_SA_CTO~Z` terminal, first
*"Give me the reserved calls"*, then, after the four cards were presented: **"Yes on all four, execute
them."** Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_192xZ_YES_ON_ALL_FOUR_RESERVED_CARDS_EXECUTE.md`
@`0d780cf6f8`. `1.0.0_SA_CTO~Z`, as adjudicator (msg 23473), routed the two COO items and ruled that both
**enter as PRODUCER ORDERS by ONE issuer amendment to round 12 now, or as round 13's first cells -- the
issuer's call, stated in the amendment.**

**THE ISSUER'S CALL, AND ITS REASON: ROUND 12, NOW.** Round 13 was rejected on a MECHANISM, not a
preference. **LD-0521: a round N+1 issuance cut before round N's slug DEADLOCKS round N's L10 until N+1
fully drains**, because the refuser counts open orders PER PROJECT and never per round. Cutting these as
round 13 cells today would therefore stall the round-12 L10 behind two Bloomberg-gated producer runs. The
opposite reason points the same way: the three partitions these runs resolve -- `S120` (the names with no
landed block), `S125` (the today-dated Price list) and the filings population -- are **named in the
round-12 L8 packet**, so resolving them inside round 12 is what lets L9 and L10 grade the outcomes against
a populated store instead of carrying three HELD halves forward.

| id | letter | what it must cover | closes | chained after |
|---|---|---|---|---|
| **`AMGT-rk-17`** | **Q** | **THE TWO BUDGETED PULLS.** ONE run of the model-block pull over the **33 KEYED COVERAGE NAMES** and ONE run of the price-axis pull, both on the budgeted two-phase Bloomberg sign-in, box-side. Measured pre-state: `derived/model_block/` **4 keys** of which only **3 are in the 33**, `raw/bloomberg/` **4 keys**, and `TRENDING_PRICE` **one axis date, 2026-09-10**. ⛔ **ITS BAR IS LANDED-AGAINST-ATTEMPTED WITH THE REFUSAL LIST PRINTED** -- 33 attempted and 20 landed with no list of the 13 is the one result this cell exists to make impossible | `S120`, `S125` | nothing -- it is a ROOT |
| **`AMGT-rk-18`** | **R** | **THE FILINGS AND DRAFTING BATCH** over the same 33, at approximately USD 36. Measured pre-state: `filings/v1/` **5 names, 10 objects**; `drafting/v1/` **5 names**. ⛔ **THE EGRESS IS BOUNDED AND MEASURED, NOT ASSERTED:** the analyzer calls Anthropic and the fetcher calls SEC EDGAR (censused: anthropic 14, edgar 12, sec.gov 2 across 11 modules), and **every other vendor token reads 0** -- a RECORD, not a gate: Andrew authorized egress as needed on 2026-09-16, so a further vendor the run needs is allowed and NAMED | the filings population | nothing -- it is a ROOT |

⛔ **NEITHER CELL TOUCHES A SURFACE AN OPEN ORDER HOLDS, AND THAT WAS CHECKED RATHER THAN ASSUMED.**
`AMGT-rk-17` writes only `raw/bloomberg/`, `derived/model_block/` and the price axis table; `AMGT-rk-18`
writes only `filings/v1/` and `drafting/v1/`. Chain A holds the portal, chain B the adapter and every live
AWS act on the Lambda, chain C the identity set and `peers/v1/`. **The one overlap is a REPO path, not a
world one:** `lib/research/filings/` is also `AMGT-rk-15`'s surface, and `AMGT-rk-15` is CUT BUT UNSPAWNED,
so the file has one writer at a time and the order says so in its own bounds.

⭐ **AND ONE THING IS DELIBERATELY NOT IN EITHER CELL.** The `BA_US_Equity` pilot re-run (`S127`) regenerates
BA's filings document **under `AMGT-rk-15`'s producer change**, so running it from `AMGT-rk-18` would spend
the vendor call and produce the OLD shape. It stays with chain A and is added to `AMGT-rk-15` by issuer
amendment before that order spawns. **A cell that can run something at the wrong time is told not to, in
its own text, rather than being trusted to notice.**

**FAN-OUT, RESTATED WITH ALL EIGHTEEN (this supersedes s.20i):**

```
fanout:
  cap: 8                      # the default; still not raised
  waves: 4
  wave_1_roots: [AMGT-rk-1, AMGT-rk-2, AMGT-rk-3, AMGT-rk-4, AMGT-rk-9, AMGT-rk-10, AMGT-rk-11]   # 7
  wave_2:       [AMGT-rk-5, AMGT-rk-6, AMGT-rk-7, AMGT-rk-12, AMGT-rk-13]                          # 5
  wave_3:       [AMGT-rk-8, AMGT-rk-14, AMGT-rk-15, AMGT-rk-16]                                    # 4
  wave_4_roots: [AMGT-rk-17, AMGT-rk-18]                                                           # 2, ANDREW-DIRECT
  max_open_width: 7           # UNCHANGED across four amendments -- wave 1 is still the widest
  deferred_for_width: []      # EMPTY. Nothing moves to round 13.
```

⛔ **THE TWO NEW CELLS ARE ROOTS AND THEY DO NOT WIDEN THE ROUND PAST ITS CAP, WHICH IS A MEASUREMENT.**
They depend on no cell, so they could have gone in wave 1; they are wave 4 only because Andrew's word
arrived at 19:2xZ. **Concurrent width at the moment they are issued: three live workers (`~23` on
`AMGT-rk-12`, `~24` on `AMGT-rk-6`, `~25` on `AMGT-rk-14`) plus these two is FIVE, against a cap of 8.**
Nothing is deferred and nothing is dropped.

**ROUND 12 IS EIGHTEEN CELLS: `AMGT-rk-1` .. `AMGT-rk-18`.** Every other clause of s.20 stands, including
the bounds in s.20f and the battery in s.20g -- and s.20f's COLLECTION-STAYS-OFF clause binds these two
cells hardest, because they are the only cells of the round that call a vendor at all: **Andrew's word
authorizes the RUNS and says nothing about their recurrence, so a cadence for either pull remains
RESERVED and neither order arms a schedule.**

## 21. ROUND 13 -- FROM THE L10 ROUND-12 ANALYSIS @`9419550eb1` (`1.0.0_SA_CTO~Z`), ADDENDUM 1 @`509f3f7335` AND ADDENDUM 2 @`9419550eb1`

**Cut by `2.0.0_SA_COO~Z`.** Round 12 is FROZEN at 18 of 18 terminal, ACCEPTED (s.1 of the analysis). LD-0521
authorizes this issuance from the analysis alone; LD-0522 leaves the push with `0.0.0_AB_MSTR~Z`, none
requested. Recon for every cell's exact code surface was read fresh at this cut (branch `SITEZ`, HEAD
`090beb09a5` at the read, no drift onto any surface this round grants -- the two commits between
`9419550eb1` and `090beb09a5` are `1.0.0_SA_CTO~Z`'s own `org/XXX.md` housekeeping, disjoint from every
path below).

**TWELVE obligations, R13-A..R13-L. This seat's HOW: fourteen cell ids (`AMGT-rk-19`..`AMGT-rk-30`, two
obligations -- R13-A and R13-L -- realized as a three-order battery under one id each, per the CTO's own
producer/adapter/page/criteria framing), TWO obligations decomposed no further and deferred (R13-I, R13-K,
s.21f), and TEN obligations issued as FIFTEEN task orders this round (self-corrected at this same cut: a
first count read sixteen by double-counting; the true sum is A=3, B=1, C=1, D=1, E=1, F=2, G=1, H=1, J=1,
L=3 = 15), across six active chains plus one held (chain D).

### 21a. THE MAPPING -- CTO letter -> COO id(s), and why an id sometimes carries more than one order

| letter | id(s) | why |
|---|---|---|
| R13-A | `AMGT-rk-19` (3 orders: producer, adapter, page) | s.3.1/A2.3's own four-part shape (producer / passage-map / adapter+page / criteria); producer is `lib/research/filings/`, adapter is `scoped_amgt.py` (chain B), page is the portal (chain A) -- three surfaces, one obligation, per RULING 1 the same discipline round 12 arrived at ONE CRITERION AT A TIME (moved-criterion map) is applied here FROM THE CUT instead |
| R13-B | `AMGT-rk-20` | one obligation, one order; its live-AWS-act still sequences on chain B per s.4's own discipline line, even though its file is not `scoped_amgt.py` |
| R13-C | `AMGT-rk-21` | one obligation, pool writes only, standalone chain |
| R13-D | `AMGT-rk-22` | one obligation; CUT, its worker NOT SPAWNED -- gated on CARD 5 |
| R13-E | `AMGT-rk-23` | one obligation, two files (`render_pack.py` uncontended; one `scoped_amgt.py` line contended) -- the whole order sits on chain B because `scoped_amgt.py` is chain B's surface WHOLE-FILE, not per-function (round 12's own ruling, rows `S124`/`S127`) |
| R13-F | `AMGT-rk-24` (2 orders: batch/producer, adapter) | the no-CIK reason has a producer half (`lib/research/filings/batch.py`, uncontended) and an adapter half (`scoped_amgt.py`'s `read_thesis_bundle`, chain B) |
| R13-G | `AMGT-rk-25` | one obligation, one order, chain B (same function region as R13-F's adapter half) |
| R13-H | `AMGT-rk-26` | one obligation; CUT, held at the tail of chain A -- runs only after R13-A and R13-D both deploy |
| R13-I | `AMGT-rk-27` | **DEFERRED to round 14** (s.21f) |
| R13-J | `AMGT-rk-28` | one obligation, one order, standalone chain (`.tools/criteria_quality_checker.py`, uncontended by any other cell) |
| R13-K | `AMGT-rk-29` | **DEFERRED to round 14** (s.21f) |
| R13-L | `AMGT-rk-30` (3 orders: producer, adapter, page) | same three-surface shape as R13-A: producer is `lib/research/scores/` (uncontended, new runner), adapter is `scoped_amgt.py` tail (chain B), page is the portal Model tab (chain A) |

⛔ **THE FULL ID IS WRITTEN IN EVERY HEADING AND EVERY TASK ORDER** (round 12's own banked lesson, s.20c) --
validated: `AMGT-rk-19` .. `AMGT-rk-30` all fullmatch `CELL_ID_RE`; none collides with round 12's `AMGT-rk-1`
.. `AMGT-rk-18` (a fresh, disjoint number range, never reused).

### 21b. THE SURFACE CENSUS -- what each order may touch, read fresh at the cut (no assumption carried from the analysis)

| surface | contended by | resolution |
|---|---|---|
| `lib/research/api/scoped_amgt.py` (whole file, per round-12 ruling `S124`/`S127`) | rk-19-adapter, rk-23, rk-24-adapter, rk-25, rk-30-adapter | **chain B, sequential queue of 6**, one worktree, one worker |
| live AWS acts (Lambda redeploy, DynamoDB/S3 writes that move served output) | rk-19-adapter, rk-20, rk-23, rk-24-adapter, rk-25, rk-30-adapter | same chain B queue (s.4's express sequencing rule: "each deploy follows the one before it") |
| `lib/research/filings/` (whole dir, round-12 ruling on the same dir) | rk-19-producer (`analyze.py`), rk-24-producer (`batch.py`) | **chain "Filings-producer", sequential queue of 2** |
| `lib/research/identity/` | rk-21 only | standalone chain |
| `lib/research/scores/` + a new runner | rk-30-producer only | standalone chain |
| `.tools/criteria_quality_checker.py` | rk-28 only | standalone chain |
| `portal/src/pages/SecurityAnalysis/` | rk-19-page, rk-30-page, rk-26 (held) | **chain A, queue fed in dependency order**, not file order |
| `lib/research/management/`, `lib/research/posture/`, a new batch driver | rk-22 only | its own chain; CUT, not spawned |

**No two chains write the same surface concurrently. Verified, not assumed**, against the fresh reads of
`render_pack.py`, `read_thesis_bundle()` (`scoped_amgt.py:1897-1949`), `batch.py`, `analyze.py`,
`price_axis_pull.py`/`generation.py`/`backfill_legacy_generation.py`, `classify.py`/`robustness.py`/`peers_v.py`
/`divergence.py`, `enrich.py`/`judge.py`/`packs.py`, and `criteria_quality_checker.py` at HEAD `090beb09a5`.

### 21c. THE CELLS, ONE POSTULATE RECORD PER OBLIGATION (Rule 24: MECE / SAME GRAIN / INTENT COHERENCE / STATE COHERENCE)

**`AMGT-rk-19` (R13-A, FWD-18) -- MECE:** three disjoint surfaces (producer text-verification / adapter second
join / page label), none overlapping a sibling cell's grant. **GRAIN:** every criterion asserts a real served
VALUE against its source (s.3.6's new instance), never a token count. **INTENT:** one axis -- a filing-sourced
number is verifiable or it is held, never displayed unverified. **STATE:** does not move `thesis_driver_chart`'s
existing exact-mnemonic branch; only ADDS a second branch that fires on its miss.
- *Producer* (`lib/research/filings/analyze.py`): re-key the verification domain from `passage_map` (which
  never segmented tables) to `excerpt.text`/`excerpt_sha256` per A2.3 item 1 -- a point is kept only when its
  value occurs as a whole number (thousands-normalised) inside the table-or-paragraph block carrying its
  matching period label, recording a character span and the excerpt hash; an unlocated point moves to
  `held_uncited`. A2.3 item 2: the analyzer additionally segments TABLE blocks into `passage_map` so a
  verified point also carries a `passage_id`. **NO NEW VENDOR CALL:** this is a pure re-verification pass over
  the ALREADY-STORED `source.json`/`analysis.json` objects (Python text matching, no LLM re-invoke) -- it
  both fixes the code for future analyzer runs AND is re-applied once to BA's existing analysis object to
  correct it in place.
- *Adapter* (`scoped_amgt.py`, `thesis_driver_chart()` around `:1953-2013`, called from `read_thesis_bundle()`
  `:1897-1949`): the exact-mnemonic join keeps precedence, unedited. A second branch runs ONLY on its miss:
  serve the verified filing points with `source: "filing"` and each `passage_id`, needing at least 2 verified
  points, else ABSENT with emitted/verified counts printed.
- *Page* (`portal/src/pages/SecurityAnalysis/`, the thesis driver chart component): label a filing-sourced
  series "from the filing, not the model" and link each point to its passage.
- *Criteria (A2.3 item 4):* (a) a planted negative -- a point whose value occurs in no block of the excerpt --
  MUST be held; (b) a planted wrong-period point -- a real value under another year -- MUST be held; (c) BA
  reads **SERVED with 3 verified points**, each with span and passage (Addendum 2 reverses the original
  ABSENT expectation).

**`AMGT-rk-20` (R13-B, FWD-15) -- MECE:** producer-only; the reader contract is explicitly NOT touched (s.3.2:
"the reader does not loosen"). **GRAIN:** the criterion reads the page's own Price call
(`read_rankings()`, `scoped_amgt.py:535`), never store existence. **INTENT:** one axis, completeness. **STATE:**
moves the served `as_of_date` from 2026-09-10 to 2026-09-15; does not touch any other rankings date.
- `integrations/bloomberg/research/price_axis_pull.py` routes its writes through
  `lib.research.price.generation.compute_price_axis()` (replacing `build_movement_rows()` + the direct
  `put_item` loop at `:167-231`/`:337-346`), mirroring `lib/research/metrics/chatter_axis.py`'s own working
  chain (`build_generation` `:656`, `default_write_generation` `:704`, wired at `:1006-1010`) -- **NOT**
  `model_block_pull.py`, which does not use this mechanism at all (a correction of an earlier assumption made
  and caught fresh at this cut, not carried forward wrong).
- The landed 2026-09-15 rows are REPUBLISHED, not re-pulled: a NEW function (not the existing lossy
  recompute path in `backfill_legacy_generation.py`, which would demote already-good `BREAKOUT_PRICE#` rows
  below `min_breakout_observations`) reads the bare `TRENDING_PRICE#2026-09-15`/`BREAKOUT_PRICE#2026-09-15`
  partitions verbatim, attaches `security_key`/`identity_status` via `build_identity_index()`, hand-builds a
  generation dict matching `build_generation()`'s shape, and calls `default_write_generation()` directly. No
  vendor call.
- This republish moves the Lead Panel's served date -- served output, **never-widen co-sign**.

**`AMGT-rk-21` (R13-C, FWD-1/FWD-13) -- MECE:** pool writes only, no adapter or portal touch. **GRAIN:** every
residue name is CLASSED (what is missing), never converted to a silent false. **INTENT:** one axis, identity
resolution reusing the chain that feeds the consumer. **STATE:** the held-holdings partition is measured FRESH
on the CURRENT resolution (158/161), never cited from the stale 47.
- Reuses `lib/research/identity/positioning_chain.py`'s `resolve_one()`/`build_positioning_identities()`
  (CUSIP check-digit -> FIGI-shaped -> SEDOL+domicile -> BBG-characteristics-confirmed, in that order, never a
  guessed ticker+"US" append) and `crosswalk.py`'s `_record_for()`/`_parse_bloomberg()` against the 56 unkeyed
  `crosswalk/v1/<date>.json` records.
- **First criterion:** re-run `build_universe.py:832-835`'s own denominator line fresh and print it (never cite
  158/161 from this document).
- **Core act:** cross-reference the 56 against already-resolved holding identities by name/root (an
  already-held-data check per Rule "build ladder" step 2, before anything is classed as needing a vendor
  lookup); every record that still needs a genuine Bloomberg lookup is classed CARD-BOUND residue, named, not
  silently dropped.

**`AMGT-rk-22` (R13-D, FWD-17/FWD-19) -- CUT, WORKER NOT SPAWNED, gated on CARD 5.**
- Producers: `lib/research/management/enrich.py::build_document()` (`:417`), `lib/research/posture/judge.py::run()`
  (`:362`, calls Anthropic) + `lib/research/posture/packs.py::build_pack()` (`:85`). Neither has a CLI batch
  driver today (unlike `model_block_pull.py`/`price_axis_pull.py`) -- one is net-new work inside this order.
  **Served today: management 5 names (BABA, BA, COST, HD, SAP_GY), posture 2 names (BABA, BA)** -- measured
  live at the cut, matching the obligation text exactly.
- A3.1 item 3's source-lacks/pull-missed classification is a NEW binary layer over existing free-text reasons
  that already exist (`enrich.py:424-427`'s `domain_for()`; `judge.py:337`'s `_absent_document()` and its call
  sites `:372-384`) -- not built from nothing.
- **This cell may be cut and its task order committed. Its worker MUST NOT be spawned until Andrew answers
  CARD 5** (s.21e).

**`AMGT-rk-23` (R13-E, FWD-5) -- MECE:** a census, not a single fix -- every artifact name built from a raw
security key. **GRAIN:** each site is named by file:line, not inferred. **INTENT:** one axis, path-safety.
**STATE:** does not touch S3 keys (which already tolerate `/`), only local filesystem joins.
- `lib/research/print/render_pack.py:243-244` (`pdf_path`/`txt_path`, from `security_key()` at `:147-148`,
  which only replaces spaces) and `scoped_amgt.py:1403` (`AMGT_DRAFTING_ROOT` offline/test reader) are the two
  sites CENSUSED at this cut. No existing path-safe-encode helper (`lib/opal_naming.py`'s `address()`/`name()`
  mint S3/resource addresses, not sanitize an existing key) -- a one-line encode at both sites (e.g.
  `sec_key.replace("/", "-")`), no new module (YAGNI).
- **Criterion:** print serves a valid PDF for **33 of 33** keyed names, printed with the denominator at the
  cut, including a planted case using `BP/_LN_Equity` or `NG/_LN_Equity` literally.

**`AMGT-rk-24` (R13-F, FWD-18) -- MECE:** producer half (`batch.py`, the promised object never written) and
adapter half (`scoped_amgt.py`, the reason never surfaced) are genuinely disjoint files -- two orders, same id.
**GRAIN:** the criterion reads the SERVED thesis route's `drafting_reason` for an unfiled name, never the log
line (S139's own corrected reading, S146). **INTENT:** one axis, that a classed absence is visible where a
person reads it. **STATE:** does not change `fetch.build_source_object()`'s classification logic, which is
already correct -- only makes its result durable (written) and visible (served).
- *Producer* (`lib/research/filings/batch.py`, `main()`): today `plan()` computes `unresolved` (`:80-111`)
  correctly, but `main()` (`:159-202`) only ever iterates `planned["fetchable"]`, NEVER `planned["unresolved"]`
  -- so the log's own promised
  `"UNRESOLVED-SOURCE: %d name(s), each an explicit object at .../UNRESOLVED-SOURCE.source.json"` line is a
  promise the same run never keeps. Fix: iterate `planned["unresolved"]` and write each one's object via
  `fetch`'s existing `unresolved_source_object()` shape + `crosswalk.write_pool()` (reusing `run_one()`'s
  existing write pattern for the resolved branch, `:130-152`).
- *Adapter* (`scoped_amgt.py`, `read_thesis_bundle()`'s drafting merge around `:1938`): read the security's
  `filings/v1/<key>/` object and merge its `status`/`reason` through when `UNRESOLVED-SOURCE`, replacing the
  generic `NoSuchKey` drafting_reason with the store's own no-CIK reason.
- **Criterion:** all 21 previously-unfiled names now carry a written `UNRESOLVED-SOURCE.source.json` object
  AND the thesis route's `drafting_reason` for each reads the no-CIK text, not `NoSuchKey` -- printed with the
  21-name denominator.

**`AMGT-rk-25` (R13-G, FWD-3) -- MECE:** one field, one function, no producer change (the value already exists
upstream). **GRAIN:** the served body, not the drafting object alone. **INTENT:** one axis, provenance date.
**STATE:** adds one key; moves nothing else in the bundle.
- `analyze.py:697` already sets `filing_date` on the analysis object, and `drafting_build.py:229` already
  forwards it into the drafting object (`"filing_date": analysis["filing_date"]`). `read_thesis_bundle()`
  (`scoped_amgt.py:1897-1949`) never re-exposes it as `as_of_date` on the outer bundle (confirmed absent from
  the dict literal `:1918-1934` and every subsequent `bundle.update()`/assignment). Fix: one line, either
  inside `_drafting_block()` (`read_drafted_sections()` at `:1581` delegates to it) or immediately after the
  `bundle.update(read_drafted_sections(...))` call at `:1938` -- `bundle["as_of_date"] = <the same filing_date
  already read>`. No new read, no new producer call.
- **Criterion:** the served thesis bundle for a name carrying a filing (BA) has `as_of_date` equal to that
  filing's `filing_date`, printed against a planted negative (a name with NO filing must NOT carry a stale or
  invented date).

**`AMGT-rk-26` (R13-H, judgment grades) -- CUT, HELD at chain A's tail, runs only after `AMGT-rk-19`'s page AND
`AMGT-rk-22` both deploy.**
- No dedicated capture tool exists. Extends `.tools/frontend-dev.py`'s Playwright harness (already screenshots
  via `system-Edge`/pinned chromium, writes `results.json` + `.png`) with a network-log capture
  (`page.on("response")` or a CDP `Network.enable` listener -- neither existing tool captures this today).
- Captures the five tabs -- **`ThesisTab`, `ModelTab`, `PeersTab`, `PostureTab`, `ExecManagementTab`**
  (`portal/src/pages/SecurityAnalysis/tabs/`) -- plus the header, for `BA_US_Equity` and one other keyed
  non-pilot name, from a DEV build pointed at the deployed adapter.
- Two JUDGMENT criteria (`rk-2` AC6 / `rk-8` AC4's closure class), graded by the CVO at L9, never self-graded.

**`AMGT-rk-27` (R13-I, FWD-12) -- DEFERRED TO ROUND 14, named here, not omitted.** "Ledger stages bound where
they exist, or a visible refusal with a named reason (A2.2 C2: 0 of 6 bound today)." Not decomposed further
this round; s.4's own sequential-deploy list names it alongside A/B/E/F/G, and Addendum 1's correction is what
licenses moving it (never R13-L) when the cap binds.

**`AMGT-rk-28` (R13-J, S121) -- MECE:** one file, uncontended by any other cell. **GRAIN:** the new shape
mirrors an EXISTING sealed-mutant pattern exactly, not a new style. **INTENT:** one axis, the data-vacuity
class. **STATE:** adds a shape, moves none of the existing five.
- `.tools/criteria_quality_checker.py` (358 ln, built by `AMGT-rk-9`): `evaluate()` (`:195-208`) currently
  refuses five shapes (`shape1_zero_collected` `:128`, `shape2_rc_swallowed` `:139`, `shape3_grain_mismatch`
  `:151`, `shape4_inexact_capture` `:179`, `shape5_no_timeout` `:187`), each sealed in `_self_test()`
  (`:228-320`) with a planted-mutant/clean-control pair.
- Add `shape6_data_vacuity(c)` following `shape1`'s exact pattern (`:128-136`): detects an invocation counting
  a field-name token whose `expect`/`invocation` never asserts anything about the counted items' VALUES (the
  exact class of `rk-15` AC3's bug, s.3.6's instance). Wire it into `evaluate()`'s per-criterion loop (`:200`).
  Add one sealed mutant + clean control to `_self_test()` mirroring `rk-15` AC3 VERBATIM as the planted mutant.

**`AMGT-rk-29` (R13-K, FWD-20) -- DEFERRED TO ROUND 14, named here, not omitted.** "The house forecast
producer: seeded from filings and history, the degeneracy gate at the producer." `divergence.py`'s
`check_degeneracy()` (`:94`) is the gate this producer must pass before `AMGT-rk-30`'s Divergence D score can
ever read non-ABSENT -- so R13-K's absence this round is why R13-L's D stays ABSENT on 33 of 33 by design, not
by omission.

**`AMGT-rk-30` (R13-L, addendum 1) -- MECE:** three disjoint surfaces, same shape as `AMGT-rk-19`. **GRAIN:**
Robustness and Peers V assert a real MEASURED value against `classify.py`'s record shape; Divergence D asserts
ABSENT with its reason, never a placeholder. **INTENT:** one axis -- rk-5's built scores reach a served surface.
**STATE:** adds one bundle key and one portal render block; moves nothing already served.
- *Producer* (`lib/research/scores/`, new runner -- none of the three modules is wired into any pipeline
  today, confirmed by an empty runner-script census): a QA/ad-hoc run over the 33 keyed names writes each
  name's Robustness (ANNUAL variant only -- `score_robustness_annual_variant()` `:385`, model-block inputs
  only, no vendor call; the QUARTERLY variant needs a live Bloomberg pull and STAYS A CARD, never this cell's
  act), Peers V (`score_peers_v()` `:211`, over `rk-14`'s repaired peer rows), and Divergence D (ABSENT for
  every name, reason "house forecast does not serve", via `classify.py`'s `absent()` `:39`) to the pool through
  `classify.py`'s record shape (`measured()` `:32`, `absent()` `:39`, `is_measured()` `:50`).
- *Adapter* (`scoped_amgt.py`, `read_thesis_bundle()`, immediately after the existing `bundle["posture"] =
  read_posture(...)` line near `:1939-1940`): add `bundle["scores"] = read_scores(resolved_key,
  identity=identity)`, `read_scores()` written to mirror `read_management()`'s exact shape (`:2184-2251`:
  resolve identity -> `read_pool_object(SCORES_PREFIX, key)` -> `POOL_ABSENT`/`POOL_SERVED`).
- *Page* (`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`): a new render block for the three score
  fields, each value or its ABSENT reason -- **a score that renders nothing because its field is missing is
  not met.**
- **Criteria:** served count of MEASURED Robustness and Peers V over 33, printed with ABSENT reason codes
  beside it; D reads ABSENT on 33 of 33 with its reason; one planted negative per score (an input with a
  missing value MUST class ABSENT, never 0).

### 21d. CHAINS AND QUEUES

⛔ **REVISED AT THE CUT, before issuance, on Andrew's own throughput question.** The original cut put chain
FP's two orders on one sequential worker and chain B's `AMGT-rk-30` adapter half LAST in its queue. Neither
was required: FP's two orders touch DISJOINT FILES (`analyze.py` vs `batch.py` -- the whole-directory
single-writer rule was inherited from round 12, where a THIRD order, `AMGT-rk-15`, also touched that
directory; no third order touches it this round), and `AMGT-rk-30`'s adapter half depends on NOTHING in
chain B's queue except chain SP's producer, so queuing it last forced chain A's second page to wait for all
six of chain B's steps instead of two. **Chain B's own internal sequencing (six deploys, one at a time) is
UNCHANGED and stays sequential -- that is a Terraform-state-safety and rollback-hash-anchoring constraint
from s.4's own ruling, not a throughput choice, and is not loosened for speed.**

```
Chain B        (adapter + every live AWS act; ONE worktree, ONE worker, SEQUENTIAL, 6 orders, REORDERED):
               AMGT-rk-19 (adapter) -> AMGT-rk-30 (adapter) -> AMGT-rk-20 -> AMGT-rk-23 -> AMGT-rk-24 (adapter) -> AMGT-rk-25
Chain FP-A     (lib/research/filings/analyze.py only, standalone, 1 order):
               AMGT-rk-19 (producer)
Chain FP-B     (lib/research/filings/batch.py only, standalone, 1 order):
               AMGT-rk-24 (producer)
Chain ID       (lib/research/identity/, standalone, 1 order):
               AMGT-rk-21
Chain SP       (lib/research/scores/ + new runner, standalone, 1 order):
               AMGT-rk-30 (producer)
Chain CK       (.tools/criteria_quality_checker.py, standalone, 1 order):
               AMGT-rk-28
Chain A        (portal; ONE worktree, ONE worker, fed in DEPENDENCY order, not file order):
               AMGT-rk-19 (page) [after Chain B's rk-19-adapter lands -- Chain B's step 1]
               -> AMGT-rk-30 (page) [after Chain B's rk-30-adapter AND Chain SP land -- Chain B's step 2, not step 6]
               -> AMGT-rk-26 [HELD -- after Chain A's own rk-19-page AND AMGT-rk-22 (CARD 5) both deploy]
Chain D        (management/posture producers; CUT, NOT SPAWNED -- gated on CARD 5):
               AMGT-rk-22
```

**Seven chains now (was six), still one worker each; N of M stays comfortably under the cap of 8** (7 spawned
now -- B, FP-A, FP-B, ID, SP, CK, A -- plus chain D cut-and-held).

**Cross-chain dependency notes (textual, per round-12's own precedent -- "spawn only after X has drained"),
never a mechanical gate between chains:**
- Chain A's `AMGT-rk-19` page order is fed to the worker only once Chain B's `AMGT-rk-19` adapter order (step
  1) has drained and its deploy is confirmed live.
- Chain A's `AMGT-rk-30` page order is fed only once BOTH Chain B's `AMGT-rk-30` adapter order (step 2, moved
  up from step 6) AND Chain SP's producer order have drained -- an ordinary short cross-chain wait if Chain SP
  is not yet done, not a blocking condition to file a row over.
- `AMGT-rk-26` is never fed. It is re-evaluated only after Andrew answers CARD 5 and `AMGT-rk-22` is spawned
  and drains.

### 21e. CARD 5, THE COST LINE (owed before Andrew answers, s.5 of the analysis)

Management is capped at the 12 names carrying a filing; posture can reach the 33 keyed. Today: management 5,
posture 2 -- so the ask is roughly 7 more management names and 31 more posture names, measured live at the
cut (s.21c `AMGT-rk-22`). **Per-name cost, from this round's own receipts (no other data exists yet for
either producer specifically, so this is the best available proxy, stated as such):** `AMGT-rk-18`'s 11-name
filings/drafting batch cost USD 6.2791 (USD 0.571/name); `AMGT-rk-15`'s single BA re-run cost USD 0.6588.
**Neither receipt is FROM the management or posture producer itself** (no run of either has happened yet at
any Bloomberg/LLM cost) -- the true per-name figure for `enrich.py`/`judge.py` specifically will only be
measured on CARD 5's own first batch, and this seat says so rather than presenting a filings-pipeline number
as a management/posture one. **REC: YES**, per the CTO's own s.5 recommendation, with the caveat above stated
on the card, not smoothed over.

### 21f. FAN-OUT

```
fanout:
  cap: 8                        # unchanged, not raised
  chains_total: 8               # B, FP-A, FP-B, ID, SP, CK, A, D (FP split into FP-A/FP-B at the cut, for throughput)
  chains_spawned_now: 7         # B, FP-A, FP-B, ID, SP, CK, A -- D withheld
  waves: not applicable this round -- seven chains start together, no wave gate
  deferred_to_round_14: [AMGT-rk-27, AMGT-rk-29]   # R13-I, R13-K, per Addendum 1's correction (R13-L never defers)
  held_pending_card_5: [AMGT-rk-22]                # R13-D -- cut, not spawned
  held_pending_upstream_deploy: [AMGT-rk-26]       # R13-H -- cut, tail of chain A, fed only after rk-19-page and rk-22 both land
  reason: "twelve obligations named by the CTO; ten decomposed and issued this round (A,B,C,D,E,F,G,H,J,L);
           two deferred to round 14 by explicit CTO license (I,K); D cut but held on Andrew's word (CARD 5);
           H cut but held on its own upstream dependency. Nothing moved by silent omission -- every one of
           the twelve is named in s.21a's table with its disposition."
```

**No cell is left for a later round by this seat's own choice** -- I and K move only because the CTO's own
ADDENDUM 1 licenses exactly that pair, by name, under the cap. Everything else this seat can issue, it issues.

## 22. ROUND 14 -- FROM THE L10 ROUND-13 ANALYSIS @`9c8e04cd9a` (`1.0.0_SA_CTO~Z`), PRD v0.13 @`1699960261` (the six cards answered @`4de34f0d95`; SA terms cleared by Andrew @`1699960261`)

**Cut by `2.0.0_SA_COO~Z`.** Round 13 is FROZEN at 97 of 97 terminal, ACCEPTED (analysis s.1). LD-0521 authorizes this
issuance from the analysis alone, cut only after BOTH v0.13 L4-R halves read SIGNED (LIMB 6). LD-0522 leaves the push with
`0.0.0_AB_MSTR~Z`, none requested. Andrew's frame (~16:3xZ): round 14 is organized by the STAGES OF INSTANTIATING A NEW
SECURITY, not by panel (PRD s.10). Andrew's bar (~16:3xZ): every cell is proven on the three validation names -- Caterpillar,
CSL, Keyence -- or a dry run; NO fleet run, NO re-run of the 33 before end-to-end validation (`C-VALIDATION-NAMES`). Andrew's
capacity word (~18:2xZ): this device is dedicated; the fan-out cap is raised from the default 8 to a MEASURED 16 (s.22f).

**THE COUNT, stated rather than smoothed:** the analysis says "27 cells in 7 chains, 20 independent". Its table carries
THIRTY-ONE cell rows -- it counts the three sequenced sub-queues (`M2->M3->M4`, `E5->E6`, `P2->P3`) as ONE cell each. This
seat's HOW cuts ONE ORDER PER ROW (one obligation, one order, a sub-queue sequenced on one worker slot), (the one cell the six-card answers briefly added -- reading Seeking Alpha's terms -- was WITHDRAWN at v0.13:
Andrew cleared the terms himself, *"I have already clarified SA ToS, we are good"*). **Thirty-one orders, ids `AMGT-rk-31`..`AMGT-rk-61`,
twenty-seven worker slots `~35`..`~61`**, a fresh disjoint number range (round 13 ended at `rk-30`; `rk-27` and `rk-29`
remain DEFERRED as named in s.21 -- neither is a round-14 cell, and neither is omitted silently: `rk-27` (ledger stages)
and `rk-29` (the house forecast producer behind Divergence D) wait on the Refresh-queue definition and the Posture brief
respectively, both named by the analysis as NOT cells this round).

### 22a. THE MAPPING -- CTO cell -> COO id and slot

| CTO cell | id | slot | chain | serves | co-sign |
|---|---|---|---|---|---|
| R14-I1 | `AMGT-rk-31` | ~35 | I (identity) | FWD-2, V1, `C-INSTANTIATION-ENTRY` | pool writes |
| R14-I2 | `AMGT-rk-32` | ~36 | I -> after H1 (shares `build_universe.py`) | FWD-18, V2/D1 | no |
| R14-H1 | `AMGT-rk-33` | ~37 | H (production home) | W32-S4, M1, V7/D24, `C-PRODUCTION-HOME` | no |
| R14-M1 | `AMGT-rk-34` | ~38 | M -> after H1 (the unit map's new home) | FWD-10, M1 | yes |
| R14-M2 | `AMGT-rk-35` | ~39 | M queue 1 of 3 | FWD-1, FWD-16, M2 | yes |
| R14-M3 | `AMGT-rk-36` | ~39 | M queue 2 of 3 | M3, `C-MODEL-FORECASTS` (SA fallback lifted by name), Base case | yes |
| R14-M4 | `AMGT-rk-37` | ~39 | M queue 3 of 3 | M4, M5, L8, `C-DESCRIPTION-LINE` | yes |
| R14-F1 | `AMGT-rk-38` | ~40 | F (filings) | FWD-18, T1, T8, T10, T15; international order RATIFIED | pool writes |
| R14-F2 | `AMGT-rk-39` | ~41 | F | FWD-18, V3, E10 | no |
| R14-F3 | `AMGT-rk-40` | ~42 | F | FWD-18, T13, V4, `C-FILINGS-TRANSLATION` | no |
| R14-F4 | `AMGT-rk-41` | ~43 | F | FWD-9, FWD-18, V6/D18, `C-VERBATIM-GATE` = HOLD | yes |
| R14-F5 | `AMGT-rk-42` | ~44 | F | FWD-18, T4-T7 | no |
| R14-E1 | `AMGT-rk-43` | ~45 | E (management) | FWD-17, E1, E4, E11, W32-S2 | yes |
| R14-E2 | `AMGT-rk-44` | ~46 | E | FWD-17, W32-S3, E6-E8 | no |
| R14-E3 | `AMGT-rk-45` | ~47 | E | FWD-17, E5' | yes |
| R14-E4 | `AMGT-rk-46` | ~48 | E | FWD-17, V5, E2, E3 | pool writes |
| R14-E5 | `AMGT-rk-47` | ~49 | E queue 1 of 2 | FWD-17, card 1 (Bloomberg officers fallback) | yes |
| R14-E6 | `AMGT-rk-48` | ~49 | E queue 2 of 2 | FWD-17, the CEO search | yes |
| R14-E7 | `AMGT-rk-49` | ~50 | E -> gated on F1 (`rk-38`) | FWD-17, card 2; Lusha AUTHORIZED in validation | no |
| R14-P1 | `AMGT-rk-50` | ~51 | P (peers) | FWD-8, P1-P7, `C-PEER-SET-SA` (SA production use AUTHORIZED by name) | pool writes |
| R14-P2 | `AMGT-rk-51` | ~52 | P queue 1 of 2 -> after P1 | FWD-8, S162 (1), `C-PEERS-V-FLOORS` | yes |
| R14-P3 | `AMGT-rk-52` | ~52 | P queue 2 of 2 (portal) | FWD-8 | yes |
| R14-L1 | `AMGT-rk-53` | ~53 | L (lists) | FWD-15, L2, L5, V8/D25, `C-SERVER-SIDE-RANKING` | yes |
| R14-L2 | `AMGT-rk-54` | ~54 | L (a MEASURE cell) | FWD-4, FWD-11, FWD-16, L3, L4 | no |
| R14-T1 | `AMGT-rk-55` | ~55 | T (tools) | S154 | no |
| R14-T2 | `AMGT-rk-56` | ~56 | T | S153 | no |
| R14-T3 | `AMGT-rk-57` | ~57 | T | S169 | no |
| R14-T4 | `AMGT-rk-58` | ~58 | T | W34-S2 | no |
| R14-T5 | `AMGT-rk-59` | ~59 | T (infra, `CLOUD_OPS_OR_ETL`) | W34-S1 | no |
| R14-T6 | `AMGT-rk-60` | ~60 | T | W31-S1 | no |
| R14-T7 | `AMGT-rk-61` | ~61 | T -> adapter single-writer queue | W27-S10, FWD-13 | yes |

⛔ **THE FULL ID IS WRITTEN IN EVERY HEADING AND EVERY TASK ORDER** (s.20c/s.21a's banked lesson) -- validated: every id
fullmatches `CELL_ID_RE` (`.tools/to-pipeline-gate.py:262`), none collides with `rk-1`..`rk-30`.

**Not cells, and why (the analysis's own list, adopted):** Lead Panel cards A+B are ONE direct Andrew-authorized act
(`C-PRICE-DAILY-LEG`, `C-PRICE-BREAKOUT-FLOOR`), B first, executed by this seat outside the round under a never-widen
pair; the Refresh queue needs its L4 definition first; ESEF/tier-2 and tier-3 filings wait on Andrew's international order
-- now RATIFIED (card 3), so `rk-38` builds the full battery and no separate cell is owed; card 6 (retire headless capture
estate-wide) is `0.0.0_AB_MSTR~Z`'s to place. **Carried as DATA, not a cell:** the 11 `drafting/v1` objects derived from
pre-driver-point analyses (analysis s.3.8) -- re-opened only after `rk-42` (F5) lands and the analyzer is validated.

### 22b. SURFACE CENSUS -- from the drafters' `<CELL>.census.json` (31 of 31 cells; aggregated by the issuer, every path opened by its drafter)

| cell | CTO | co-sign | depends_on | files_written | pool prefixes written | vendor calls | live AWS acts |
|---|---|---|---|---|---|---|---|
| `AMGT-rk-31` | R14-I1 | yes | none | 10: lib/research/identity/add_security.py; lib/research/identity/crosswalk.py; lib/research/identity/crosswalk.schema.json (+7) | s3://opal-data-harvest/crosswalk/v1/<as_of>.json; s3://opal-data-harvest/raw/bloomberg/<KEY>/<stamp>/identity.json | Bloomberg DAPI reference_data on '<id> Equity' -- ONE call per registered id; ceiling 9 at the cut | 1: S3 put_object + head_object on the two prefixes above; list_objects_v2/get_object reads on crosswalk/v1/ and raw/bloomberg/ for the criteria. No Lambda, no Terraform, no IAM. |
| `AMGT-rk-32` | R14-I2 | no | AMGT-rk-33 | 5: lib/research/identity/build_universe.py; lib/research/identity/tests/test_union_universe.py; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~36/ (+2) | s3://opal-data-assets/sec/global/bronze/company_tickers/date=<today UTC>/company_tickers.json | ONE GET of https://www.sec.gov/files/company_tickers.json per UTC day | 1: S3 put_object + head_object on the one object above; list/head/get reads on the bronze prefix and universe/v1/ for the criteria. No Lambda, no Terraform, no IAM. |
| `AMGT-rk-33` | R14-H1 | no | none | 11: integrations/bloomberg/research/model_block_pull.py; integrations/bloomberg/research/field_map.json; lib/research/identity/build_universe.py (+8) | s3://opal-data-assets/sec/global/bronze/company_tickers/date=2026-09-15/sec_ticker_cik_cache.json; s3://opal-data-harvest/raw/bloomberg/<KEY>/<stamp>/pull_log.json; the peer candidate universe: NO pool write expected -- the builder refuses | none | 1: S3 put_object + head_object + get_object on opal-data-assets at the builder address |
| `AMGT-rk-34` | R14-M1 | yes | AMGT-rk-33 | 8: integrations/bloomberg/research/build_unit_map.py; integrations/bloomberg/research/model_block_pull.py; <rk-33's unit-map home under integrations/bloomberg/research/> (+5) | s3://opal-data-harvest/derived/model_block/<key>/<new stamp>/model_block.json for each of the 33 crosswalk-keyed names | none | 1: S3 put_object under derived/model_block/ for 33 keys via model_block_pull.py derive |
| `AMGT-rk-35` | R14-M2 | yes | AMGT-rk-34; AMGT-rk-33 | 7: integrations/bloomberg/research/model_block_pull.py; <rk-33's unit-map home under integrations/bloomberg/research/>; org/critical_paths/change_management/<stamp>_amgt-rk35-rolling-window-validation-names-20260918_deploy_completion.md (+4) | s3://opal-data-harvest/raw/bloomberg/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>/{refdata,histdata}.json; s3://opal-data-harvest/derived/model_block/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>/model_block.json | Bloomberg DAPI via integrations/bloomberg/mcp/blp_client.py: one ReferenceDataRequest + one HistoricalDataRequest for each of CAT US Equity, CSL AU Equity, 6861 JP Equity | 1: S3 put_object for the six raw objects and three derived objects above; the input ledger's record_run for three landings. NO Lambda deploy, NO Terraform, NO IAM. |
| `AMGT-rk-36` | R14-M3 | yes | AMGT-rk-35; AMGT-rk-34 | 12: integrations/bloomberg/research/model_block_pull.py; integrations/bloomberg/research/sa_forecast_fallback.py; integrations/bloomberg/research/build_unit_map.py (+9) | s3://opal-data-harvest/raw/bloomberg/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>/{refdata,histdata,bestdata}.json; s3://opal-data-harvest/raw/seekingalpha/{same keys}/<stamp>/{symbol,metrics}.json; s3://opal-data-harvest/derived/model_block/{same keys}/<stamp>/model_block.json (+1) | Bloomberg DAPI: per validation name one ReferenceDataRequest + one HistoricalDataRequest + three ReferenceDataRequests with BEST_FPERIOD_OVERRIDE in {1FY,2FY,3FY}; Seeking Alpha via the parked session in integrations/seekingalpha/rest_fetch.py: GET /api/v3/symbols/{candidate} and GET /api/v3/metrics?filter[fields]=...&filter[slugs]=... on the validation names that have a Bloomberg gap and an entity-tested symbol | 1: S3 put_object for the raw/derived objects above; the Lambda artifact upload; ONE targeted safe-apply of module.scoped_amgt_api.aws_lambda_function.this |
| `AMGT-rk-37` | R14-M4 | yes | AMGT-rk-36; AMGT-rk-35; AMGT-rk-34 | 11: integrations/bloomberg/research/model_block_pull.py; integrations/bloomberg/research/build_unit_map.py; lib/research/api/scoped_amgt.py (+8) | s3://opal-data-harvest/raw/bloomberg/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>/{refdata,histdata,bestdata}.json; s3://opal-data-harvest/derived/model_block/{same keys}/<stamp>/model_block.json; s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip | Bloomberg DAPI: one candidate-probe ReferenceDataRequest on CAT US Equity | 1: S3 put_object for the raw/derived objects above; the Lambda artifact upload; ONE targeted safe-apply of module.scoped_amgt_api.aws_lambda_function.this with the pre-act CodeSha256 and VersionId recorded. NO IAM, NO new resource. |
| `AMGT-rk-38` | R14-F1 | no | AMGT-rk-39 | 7: lib/research/filings/battery.py; lib/research/filings/fetch.py; lib/research/filings/__init__.py (+4) | filings/v1/CAT_US_Equity/; filings/v1/CSL_AU_Equity/; filings/v1/6861_JP_Equity/ | ONE Bloomberg ReferenceDataRequest for CAT US Equity, CSL AU Equity, 6861 JP Equity; EDGAR (+1) | 1: S3 put + read-back of the three validation names' source objects under filings/v1/ |
| `AMGT-rk-39` | R14-F2 | no | none | 8: lib/research/filings/document.py; lib/research/filings/fetch.py; lib/research/filings/__init__.py (+5) | none | two HTTP GETs of the CSL and Keyence PDFs from the issuers' own sites | 0: none |
| `AMGT-rk-40` | R14-F3 | no | AMGT-rk-39 | 12: lib/research/filings/passages.py; lib/research/filings/analyze.py; lib/research/filings/drafting_build.py (+9) | none | Anthropic API on the Keyence document: one two-pass analysis; the Keyence PDF GET performed by rk-39's CLI; NO other egress, NO pool write | 0: none |
| `AMGT-rk-41` | R14-F4 | yes | AMGT-rk-42 | 10: lib/research/drafting/pipeline.py; lib/research/drafting/schema.json; lib/research/drafting/tests/test_drafting.py (+7) | drafting/v1/<key>.json for the MEASURED crosswalk keys that carry an analysis object | one EDGAR fetch; NO model call in the rebuild | 2: S3 put + read-back of the rebuilt drafting/v1 objects through the one writer (+1) |
| `AMGT-rk-42` | R14-F5 | no | none | 9: lib/research/filings/analyze.py; lib/research/filings/batch.py; lib/research/filings/run_batch.cmd (+6) | none | NONE. No model call | 1: READ-ONLY: list universe/v1/ |
| `AMGT-rk-43` | R14-E1 | yes | none | 7: lib/research/api/scoped_amgt.py; portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx; portal/src/pages/SecurityAnalysis/types.ts (+4) | none | none | 3: build-and-upload-scoped-amgt.sh -> s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip (+2) |
| `AMGT-rk-44` | R14-E2 | no | none | 5: lib/research/management/batch.py; lib/research/management/run_batch.cmd; lib/research/management/tests/test_management.py (+2) | none | none | 1: s3 list/get under filings/v1/ and crosswalk/v1/ |
| `AMGT-rk-45` | R14-E3 | yes | AMGT-rk-43 | 8: lib/research/management/enrich.py; lib/research/management/pool.schema.json; lib/research/management/tests/test_management.py (+5) | management/v1/_pool/ | none | 3: s3 put_object management/v1/_pool/<today>.json via crosswalk.write_pool (+2) |
| `AMGT-rk-46` | R14-E4 | no | none | 6: lib/research/management/roster.py; lib/research/management/management.schema.json; lib/research/management/tests/fixtures/*.json (+3) | none | none | 1: s3 list/get under filings/v1/<key>/ for six keyed names |
| `AMGT-rk-47` | R14-E5 | yes | none | 8: lib/research/management/bloomberg_fallback.py; lib/research/management/enrich.py; lib/research/management/management.schema.json (+5) | s3://opal-data-harvest/management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json; s3://opal-data-harvest/raw/bloomberg/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>/exec_officers.json | Bloomberg DAPI ReferenceDataRequest [NAME, COMPANY_EXEC_OFFICERS] on CAT US Equity, CSL AU Equity, 6861 JP Equity | 3: S3 put via crosswalk.write_pool on the 3 management keys (+2) |
| `AMGT-rk-48` | R14-E6 | yes | AMGT-rk-47 | 8: data/find/dualbiz/scripts/serp.py; lib/research/management/ceo_search.py; lib/research/management/enrich.py (+5) | s3://opal-data-harvest/management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json | Bright Data SERP; Anthropic (+1) | 2: S3 put via crosswalk.write_pool on the 3 management keys (+1) |
| `AMGT-rk-49` | R14-E7 | no | AMGT-rk-38; AMGT-rk-47; AMGT-rk-48 | 6: lib/research/management/enrich.py; lib/research/management/management.schema.json; lib/research/management/domains.json (+3) | s3://opal-data-harvest/management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json | Lusha v3 contacts/prospecting; NONE else: --enrich-only makes no Bloomberg, Bright Data, Anthropic or Seeking Alpha call by construction; AC1 and AC2 call nothing | 2: S3 put via crosswalk.write_pool on the 3 management keys (+1) |
| `AMGT-rk-50` | R14-P1 | no | none | 6: lib/research/peers/sa_peers.py; lib/research/peers/engine.py; lib/research/peers/tests/test_peers.py (+3) | s3://opal-data-assets/seeking-alpha/global/bronze/peers/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/; s3://opal-data-assets/bloomberg/global/bronze/peers-growth/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/; s3://opal-data-harvest/peers/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json | Seeking Alpha: per validation name, 1 search GET + 4 Peers GETs through the EXISTING rest_fetch.py parked session and residential proxy -- authorized BY NAME for C-PEER-SET-SA; Bloomberg DAPI: one reference_data call per validation name over subject + 5 peers, fields NAME / GEO_GROW_OPER_INC / FREE_CASH_FLOW_5_YEAR_GROWTH -- inside the validation Andrew set as the bar; health() first, never a sign-in | 1: S3 PUT of raw bytes and three R-1 pool objects under the box's existing credentials; no Lambda, no Terraform, no IAM, no schedule |
| `AMGT-rk-51` | R14-P2 | yes | AMGT-rk-50 | 9: lib/research/scores/peers_v.py; lib/research/scores/peers_fields_pull.py; lib/research/scores/run_scores.py (+6) | s3://opal-data-assets/bloomberg/global/bronze/peers-v-fields/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>.json; s3://opal-data-harvest/scores/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json | Bloomberg DAPI: at most three reference_data calls; Seeking Alpha: NONE from this order | 1: S3 PUT of raw refdata and three scores/v1 objects under the box's existing credentials; no Lambda, no Terraform, no IAM, no schedule |
| `AMGT-rk-52` | R14-P3 | yes | AMGT-rk-50; AMGT-rk-51 | 8: portal/src/pages/SecurityAnalysis/types.ts; portal/src/pages/SecurityAnalysis/cscTable.ts; portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx (+5) | none | none | 1: NONE -- one S3 GET of peers/v1/CAT_US_Equity/<newest>.json to build the fixture |
| `AMGT-rk-53` | R14-L1 | yes | AMGT-rk-60 | 11: lib/research/metrics/generation_writer.py; lib/research/metrics/chatter_axis.py; lib/research/price/generation.py (+8) | none | NONE. The price writer is exercised offline on a synthetic series; no Bloomberg, no model call. | 1: READ-ONLY: the --dry-run at AC5 reads the pool |
| `AMGT-rk-54` | R14-L2 | no | none | 4: org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~54/PUBLICATION_LINKS_COVERAGE_MEASURE_20260918.md; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~54/PUBLICATION_LINKS_COVERAGE_MEASURE_20260918.json; org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md (+1) | none | NONE. No harvester, no publisher client, no Seeking Alpha / FT / WSJ / Bloomberg / Barrons call; C-VENDOR-WORD-HARVESTERS is not exercised. | 1: READ-ONLY: paginated list_objects_v2 over publication-links/v1/ and publications/v1/ |
| `AMGT-rk-55` | R14-T1 | no | none | 5: .tools/to-pipeline-gate.py; .tools/tests/test_gate_x_round_issuer.py; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~55/ (+2) | none | NONE. | 0: none |
| `AMGT-rk-56` | R14-T2 | no | none | 5: .tools/to-pipeline-gate.py; .tools/tests/test_gate_xi_status_element.py; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~56/ (+2) | none | NONE. | 0: none |
| `AMGT-rk-57` | R14-T3 | no | none | 5: .tools/surprise-row-gate.py; .tools/tests/test_acceptance_sweep.py; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~57/ (+2) | none | NONE. | 0: none |
| `AMGT-rk-58` | R14-T4 | no | none | 6: .tools/direct-act-order.py; .tools/tests/test_direct_act_order.py; .claude/skills/dispatch/SKILL.md (+3) | none | none | 0: none |
| `AMGT-rk-59` | R14-T5 | no | none | 3: infra/aws/terraform/harvest/chatter-axis-schedule.tf; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~59/AMGT_RESAPP.TO-AMGT-rk-59.plan-tolerates-absent-zip.proof_of_spec.json; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-59.plan-tolerates-absent-zip.md | none | none named; build_zip.py's pip download of the pinned jsonschema wheels into the gitignored .build/ | 4: terraform init in infra/aws/terraform/harvest (+3) |
| `AMGT-rk-60` | R14-T6 | no | none | 5: .tools/wk-provision.sh; .claude/skills/dispatch/SKILL.md; org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~60/AMGT_RESAPP.TO-AMGT-rk-60.portal-worktree-provisioning.proof_of_spec.json (+2) | none | none | 0: none |
| `AMGT-rk-61` | R14-T7 | yes | AMGT-rk-53; AMGT-rk-59 | 6: lib/research/api/scoped_amgt.py; lib/research/api/tests/test_slash_safe_security_route.py; org/critical_paths/change_management/<ts>_amgt-rk61-router-slash-indifferent_deploy_completion.md (+3) | none | none | 4: s3 PutObject of the Lambda artifact research/opal-amgt-scoped-api.zip in opal-313476888478-lambda-artifacts (+3) |

**Files written by MORE THAN ONE cell (the contention set, 23 files):**

- `.claude/skills/dispatch/SKILL.md` <- `AMGT-rk-58`, `AMGT-rk-60`
- `.tools/to-pipeline-gate.py` <- `AMGT-rk-55`, `AMGT-rk-56`
- `<rk-33's unit-map home under integrations/bloomberg/research/>` <- `AMGT-rk-34`, `AMGT-rk-35`
- `integrations/bloomberg/research/build_unit_map.py` <- `AMGT-rk-34`, `AMGT-rk-36`, `AMGT-rk-37`
- `integrations/bloomberg/research/model_block_pull.py` <- `AMGT-rk-33`, `AMGT-rk-34`, `AMGT-rk-35`, `AMGT-rk-36`, `AMGT-rk-37`
- `lib/research/api/scoped_amgt.py` <- `AMGT-rk-36`, `AMGT-rk-37`, `AMGT-rk-43`, `AMGT-rk-45`, `AMGT-rk-53`, `AMGT-rk-61`
- `lib/research/drafting/tests/test_drafting.py` <- `AMGT-rk-40`, `AMGT-rk-41`
- `lib/research/filings/__init__.py` <- `AMGT-rk-38`, `AMGT-rk-39`, `AMGT-rk-40`, `AMGT-rk-42`
- `lib/research/filings/analyze.py` <- `AMGT-rk-40`, `AMGT-rk-42`
- `lib/research/filings/drafting_build.py` <- `AMGT-rk-40`, `AMGT-rk-41`
- `lib/research/filings/fetch.py` <- `AMGT-rk-38`, `AMGT-rk-39`
- `lib/research/filings/tests/test_filings.py` <- `AMGT-rk-39`, `AMGT-rk-40`, `AMGT-rk-41`, `AMGT-rk-42`
- `lib/research/identity/build_universe.py` <- `AMGT-rk-32`, `AMGT-rk-33`
- `lib/research/identity/tests/test_union_universe.py` <- `AMGT-rk-32`, `AMGT-rk-33`
- `lib/research/management/enrich.py` <- `AMGT-rk-45`, `AMGT-rk-47`, `AMGT-rk-48`, `AMGT-rk-49`
- `lib/research/management/management.schema.json` <- `AMGT-rk-46`, `AMGT-rk-47`, `AMGT-rk-48`, `AMGT-rk-49`
- `lib/research/management/tests/test_management.py` <- `AMGT-rk-44`, `AMGT-rk-45`, `AMGT-rk-46`
- `lib/research/peers/tests/test_peers.py` <- `AMGT-rk-33`, `AMGT-rk-50`
- `org/critical_paths/.open_deploys/` <- `AMGT-rk-41`, `AMGT-rk-43`, `AMGT-rk-45`, `AMGT-rk-51`
- `org/critical_paths/change_management/<entry> and org/critical_paths/.open_deploys/<entry>` <- `AMGT-rk-47`, `AMGT-rk-48`
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/` <- `AMGT-rk-35`, `AMGT-rk-36`, `AMGT-rk-37`
- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` <- `AMGT-rk-31`, `AMGT-rk-32`, `AMGT-rk-33`, `AMGT-rk-34`, `AMGT-rk-35`, `AMGT-rk-36`, `AMGT-rk-37`, `AMGT-rk-38`, `AMGT-rk-39`, `AMGT-rk-40`, `AMGT-rk-41`, `AMGT-rk-42`, `AMGT-rk-50`, `AMGT-rk-51`, `AMGT-rk-52`, `AMGT-rk-53`, `AMGT-rk-54`, `AMGT-rk-55`, `AMGT-rk-56`, `AMGT-rk-57`
- `portal/src/pages/SecurityAnalysis/types.ts` <- `AMGT-rk-43`, `AMGT-rk-52`, `AMGT-rk-53`

**Surface notes (verbatim from each census):**

- **`AMGT-rk-31`:** Read at HEAD 075227f4c0. The crosswalk has ONE input today, the coverage list in worker ~4's folder (crosswalk.py:71-74); build_crosswalk() :391-436 is pure and its fixed point is tested (:192-199), so the registration input must be an INPUT FILE (registrations.json beside the producer), never a clock, and a coverage record's bytes must not change (AC6 enforces). The schema is closed at every level (additionalProperties false at :6, :63, :91), so the identity block requires a schema edit -- specified as OPTIONAL additions so 2026-09-15.json still validates. The raw client's reference_data (:135-145) returns __error__ per security (:143) -- the planted negative (AC3) rides on that. The yellow-key rule is PRD :878-880 and the alias index already carries '<id> Equity' (:462). 'SEC id' vs 'CIK': in the validation they are one identifier (CAT :97 'SEC ID 18230' == CIK); the order carries cik (int) and sec_id (EDGAR's 10-digit form, fetch.py:187) from CENTRAL_INDEX_KEY_NUMBER and lets the worker add a distinct SEC field to the SAME call if the field dictionary has one. The four folders' Bloomberg ids are NOT known at the cut; the order makes the tool read each folder's own ONE PAGER via discover_bloomberg_ticker() (:191-238) and register UNRESOLVED-with-reason when it carries none -- never guessed from the folder name; AC1 re-measures the unregistered set (corpus folders MINUS crosswalk folders, denominator printed). Contention: none with rk-32/rk-33 (disjoint files). The coverage list's own worker-folder home (D2) is a C-PRODUCTION-HOME instance the PRD does NOT name and this order does NOT move (named as a wall). Rule 30: the raw landing family raw/bloomberg/<key>/<stamp>/ is an EXISTING pipeline family (crosswalk.py:137-139 measured it), so the builder does not bind here; crosswalk/v1/ likewise. The change-management entry uses .tools/deploy_ledger.py (open/close-leg/close) with legs git/verify/verify.
- **`AMGT-rk-32`:** Read at HEAD 075227f4c0. Battery step 1 IS filing_identity_for() (build_universe.py:491-539): the miss at :505-507 prints the DELIVERY's row_denominator (10,422, sec_ticker_cik_cache.json:12) while the join at :503 runs over a 33-root projection (:15-20) -- the D1 defect the validation measured on Caterpillar (:96-97). The name guard (:509-517) is the thing the cell says to KEEP; the validation's CSL -> Carlisle refusal (:108) is the standing negative control and BA -> 12927/10-K the positive control. form_expected comes from the cache's submissions block (:518-520, 15 CIKs at :188-192) and stays that way: measuring forms from EDGAR is R14-F1's, so this order makes no data.sec.gov call and says so on the note. DIVISION WITH rk-33 (same file): rk-33 = the HOME (builder address, the projection moved, load_sec_cache reading the pool, SEC_CACHE_DEFAULT gone); rk-32 = the READ (the live table landed byte-for-byte at that home, the loader returning the full table with the denominator AS READ, the miss naming the object). The ONE shell-only invocation (AC2) is the CLI itself; every other criterion is python -c over the module. The fixture control in AC5 (a 3-row table reporting 3) is what discriminates a typed denominator from a measured one. --dry-run of the union (:854-860) must not fetch: the order says a missing landed table refuses loudly rather than fetching or falling back. The whole-union --dry-run is NOT a criterion here (it reads the ETF plane and the positioning chain, :805-830, and may not terminate under 120 s); AC6 isolates step 1's read instead. No contention with rk-31; sequential after rk-33; none with chain F (fetch.py/batch.py untouched).
- **`AMGT-rk-33`:** CONFIG PATH FOR rk-34: integrations/bloomberg/research/field_map.json (beside model_block_pull.py; _FIELD_MAP_PATH becomes Path(__file__).resolve().parent / 'field_map.json'). Read at HEAD 075227f4c0. THE BUILDER WILL REFUSE BOTH POOL ADDRESSES AT THE CUT, and the order says so line by line rather than letting the worker discover it: key() :1548-1549 refuses source 'sec' (no systems.json VENDOR row -- a row the worker ADDS, the precedent being the bloomberg/msci rows with inferred D8 ownership), after which tiers.json:27 homes a COMPOSITE bronze in opal-data-assets and the SEC document lands there; address() :1562-1565 via _home_bucket :256-260 refuses a COMPOSITE gold for source 'amgt' because amgt has no scopes.json row, and a scope row is Andrew's per-scope call (02_DOCTRINE.md:589-591; the row's bucket would be opal-data-amgt per validate :342-343, and opal-data-harvest -- the project's pool -- is registered nowhere, 05_IDENTITY_SPINE.md:77). So the peer-universe POOL MOVE is expected to land as a ROW, not a move (the order carries the negative arm if the registry moves first), while its DRY-RUN half (D24, universe.py:578-580) lands regardless. THE RESIDUE NAMED: the SEC object moved is the 2026-09-15 delivery's projection (33 of 10,422 rows) placed at BRONZE -- an R9 purity question the order names in the object's provenance and the report; rk-32 lands the full delivery beside it and only the projection's submissions block stays read. SAME FILE, SAME CLASS additions beyond the PRD's three: the pull-log write (model_block_pull.py:464-467, :482-483) is rehomed (the COO may cut it); the model-block half of the candidate universe (universe.py:68-72, :417) and the coverage list's home (build_universe.py:79-81, crosswalk.py:71-74, D2) are NOT edited -- AC6 censuses the class with its denominator and one row carries it for the CTO's next L4. LANES: infra/logic/registry/** is PLATFORM_LOGIC_DOCS and the two regenerated naming-module test files are under infra/aws/** (CLOUD_OPS_OR_ETL); the worker's grant is the <paths> block (Rule 27: a worker's write surface is exactly its <paths>); the order's negative arm is a row if the commit gate refuses either. CONTENTION: build_universe.py is shared with rk-32 (sequential, this first); universe.py is chain P's package but engine.py is NOT touched (the read-only contract lands in universe.py alone); model_block_pull.py is chain M's file for SECURITIES/HIST_END/fields (rk-34/M2-M4 -- those lines are named as walls). No vendor call, no producer run, no sec.gov GET (rk-32's).
- **`AMGT-rk-34`:** Read at HEAD ced1f5f84d (draft time; the four cited code files carry no working-tree change; scoped_amgt.py last touched e2d89be7da). The unit map's home is rk-33's (chain H) and cannot be seen from here, so the order's second act is a DISCOVERY RULE: the path model_block_pull.py opens at the worktree's HEAD, refused with a row if still under org/missions/. The served figures move through the POOL alone -- the adapter takes the lexicographically-last stamp per key (scoped_amgt.py:1013-1017) -- so the order is written to need NO Lambda redeploy: it keeps the two placeholder literals 'SEE field_map.json' / 'not yet built' that run_checks.py:54, provenance/validate.py:23 and provenance/render_print.py:83 key on (none on this order's surface), and an entry present-but-UNRESOLVED is written with a text that still carries them. That avoids the round-wide hazard that every Lambda redeploy is built from ONE worktree's bytes (build-and-upload-scoped-amgt.sh) and reverts whatever another worktree deployed. CONTENTIONS SEEN: (1) build_field_map.py:29 hard-codes bucket opal-data-research while the producer (:44) and pool_reader.py:72 read opal-data-harvest -- the new builder uses the producer's bucket; (2) cmd_pull writes pull_log.json into ~1's folder (model_block_pull.py:464-467), a C-PRODUCTION-HOME instance the PRD list omits -- assigned to rk-35 (which runs pull), row if not; (3) the F2/G-24 3-security cap (:509-510) binds derive too -- the order runs 11 batches rather than lifting a budget cap; (4) rk-34 (slot ~38) and rk-35/36/37 (slot ~39) all edit model_block_pull.py -- the drafts make rk-35 depend on rk-34 (its derive for the validation names must go through rk-34's builder), so chain M is effectively rk-33 -> rk-34 -> rk-35 -> rk-36 -> rk-37 and the COO's fan-out should spawn ~39 after ~38 drains; (5) the validation names have NO raw landed in the pool (validation @b527b93214 ran SERVED-LOCAL), so this cell's C-VALIDATION-NAMES proof is the dry run (AC4) and rk-35 exercises the builder on the new names at its derive; (6) the PRD moved three times while drafting (v0.11 @9c8e04cd9a -> v0.12 @4de34f0d95 -> v0.13 @1699960261, the last answering 3.0.0_SA_CVO~Z's annotation refusal @075227f4c0); every citation here is re-pinned at 1699960261, and LIMB 6 still refuses a newly-added order against a half not SIGNED at the current bytes -- the COO's gate to clear before this file is added; (7) 348 -> 0 is stated as 'NOT-YET-BUILT refusals 0' with an honest residue allowed and listed (an UNRESOLVED-ON unit where a magnitude cannot discriminate, e.g. a zero dividend every year), because C-UNIT-MAP-MEASURED forbids inferring a unit to clear a refusal.
- **`AMGT-rk-35`:** Read at HEAD 8a788d2eaf at the last re-pin (the producer carries no working-tree change). The window rule is written as a PRODUCER rule -- request [HIST_START, pull date], derive emits only CLOSED groups (a merged fiscal-year group carrying a reported SALES_REV_TURN or IS_EPS), records excluded groups under unresolved with a reason so count-in equals count-out, and writes history_window on the block -- so the adapter needs no change (read_model serves fiscal_years from the block, scoped_amgt.py:2529) and this order deploys no Lambda. The discriminator is D4 itself: CSL (June FYE) and Keyence (March FYE) must show FY2026 with a statement figure, CAT (December FYE) must not serve 2026 as closed. CONTENTIONS: (1) the three validation names are NOT in the crosswalk, so the pool writes are UNSERVED until R14-I1 -- the co-sign pair's blast radius is 'nothing served moves; three unserved keys land', and AC4 is the negative control that no covered name was pulled or re-derived (baseline recorded AFTER rk-34's re-derive drains, hence depends_on rk-34); (2) same file as rk-34/36/37 -- this order is first in slot ~39's queue and sequenced after slot ~38; (3) cmd_pull writes pull_log.json into worker ~1's folder (:464-467), a C-PRODUCTION-HOME instance the PRD's list omits -- fixed here (--pull-log optional, no worker-folder default) and rowed; (4) the derive for a NEW security builds its unit entries through rk-34's build_unit_map.py -- if that module is absent at spawn the order STOPs with a row rather than building units a second way; (5) D5's ledger half (:246 writes around the S3 client it was given) is explicitly NOT this cell's fix -- row if touched; (6) each order in the ~39 queue re-pulls the three names (rk-36 adds the BEST_ requests, rk-37 adds fields), so the three names are pulled up to three times across the queue -- all inside the validation bar, none on the 33.
- **`AMGT-rk-36`:** Read at HEAD 8a788d2eaf at the last re-pin. The COO's two corrections are applied: PRD v0.13 @1699960261 cited everywhere (re-pinned by line at that vintage), the SA fallback is BUILT AND EXERCISED on the three validation names with no scheduled-read hold language, and the Base case is placed in rk-37 (C-MODEL-WINDOW-AND-ROWS (5) is a 'rows' clause and needs this order's BEST_EPS FY1 cell first). CONTENTIONS: (1) THE LAMBDA IS BUILT FROM ONE WORKTREE'S BYTES (build-and-upload-scoped-amgt.sh) -- every round-14 cell that redeploys opal-amgt-scoped-api from a different worktree reverts the others (chain E's E1/E3, T7's handler, P3, L1, F4 are all candidates); the order carries a mandatory stale-bytes check against SITEZ (STOP + row if lib/research/api, lib/research/checkface or the Lambda source moved on the shared branch since the worktree's base) and the COO should consider routing ALL scoped-api redeploys through one slot as round 13's chain B did; (2) the SA estimates endpoint is UNMEASURED beyond pe_nongaap_fy1/_fy2/_fy3 (Peers brief :90); rest_fetch.py measures five endpoints, none of them metrics -- the order has the worker MEASURE candidate SA field names on Caterpillar and record NOT-MAPPABLE honestly rather than typing names; (3) the SA symbol for CSL Ltd and Keyence is not derivable from the Bloomberg root (CSL on SA is Carlisle -- the ROG class; 6861 is numeric), so the honest expected state for those two is UNRESOLVED-with-reason unless R14-P1 lands an sa_symbol on the crosswalk record (read, never required); the fill logic is then proven by the planted-gap fixture (AC4); (4) the page's CONSENSUS label and forecast columns (modelSheet.ts) are NOT in this cell -- portal frozen, no portal checkout -- and are named for the COO as a portal cell; the adapter carries estimate_basis consensus on every cell; (5) the scope contract test parses the producer's source for scope literals, so scopes.py and model_block_pull.py must move in one commit; (6) forecast figures enter the check face, so the five BEST_ mnemonics need unit-map families (added to rk-34's builder); (7) the 33 covered names are NOT re-pulled, so after the deploy their served forecast_figures read [] with a reason -- stated as the honest state and asserted by AC5, never as a defect.
- **`AMGT-rk-37`:** Read at HEAD 8a788d2eaf at the last re-pin. The COO's correction places the Base case HERE (C-MODEL-WINDOW-AND-ROWS (5) is a rows clause and consumes rk-36's BEST_EPS FY1 cell): the PRODUCER computes cases.base at derive with every input carrying its source and window, the adapter serves it, and upside/downside are served ABSENT with the exact ruling reason regardless of block content (planted negative in AC2). The describes-the-business test's wording is the cut's by the PRD's own words, so the draft STATES it (three sub-rules, the PRD's and validation's three measured negatives as planted fails, one positive) rather than leaving it to the worker. CONTENTIONS: (1) the five row mnemonics are NOT verifiable from the repo -- FREE_CASH_FLOW_YIELD is the only candidate the estate already pulls (peers_v.py:74-76 per the intake); the order makes the worker PROBE candidates on CAT through blp_client's __field_errors__ channel and record refusals, and a row with no served field stays ABSENT honestly (the CRO's field-map doc :94 wanted FCF yield/margin DERIVED, which the PRD now forbids on the page -- the producer does not derive them either); (2) this deploy's blast radius is WIDER than rk-36's: the 12 drafted names' served description flips from a segment sentence to ABSENT-naming-probes (the v0.12 measured 0 of 12), and the cases reason text changes for all 33 -- the pair must name it and the worker records the 12 names' status pre/post; (3) same stale-bytes hazard as rk-36 (Lambda built from one worktree); (4) modelSheet.ts's five null rows and the cases render are portal (frozen) -- the new fields reach the page through the subtraction group until a portal cell maps them; named for the COO; (5) the header route's exact rawPath for the description is taken from the worker's own pre-deploy 13-route census (the description travels on the header payload, scoped_amgt.py:1895-1899) -- the AC4 invocation names '/header' and tells the worker to correct it from the census if the route differs; (6) the trailing-median P/E has NO invented floor on n (n is printed) -- if the CVO wants a floor that is an L4 question, not a seat's choice.
- **`AMGT-rk-38`:** Read at HEAD (lib/research/filings last moved @db6c40083f 2026-09-17). fetch.py is EDGAR-only: build_source_object :377-448 takes (security_key, cik, form_expected), the form patterns :103-152 know 10-K and 20-F only, unresolved_source_object :359-374 carries one reason and no attempt log, latest_filing :177-215 drops reportDate/website/investorWebsite that the same submissions JSON carries, pool_key :451-452 keys by accession only. blp_client.reference_data :135-145 omits a field on a field-level error (a missing CENTRAL_INDEX_KEY_NUMBER is measured by absence). The crosswalk record :257-336 carries no cik/LEI/legal name today (R14-I1 lands them), so the battery takes an injected keys record. CONTENTION: fetch.py is edited by BOTH AMGT-rk-39 (the cutter, SECTION_PATTERNS :103-152, extract_sections :329-350, officer_section :411/:440-447, PARSER_VERSION) and this cell (build_source_object :377-448, unresolved_source_object :359-374, latest_filing :177-215, pool_key :451-452, PARSER_VERSION) -- disjoint regions except PARSER_VERSION; the COO sequences rk-39 BEFORE rk-38 because rk-38 consumes document.py. No other round-14 F cell touches battery.py or test_battery.py. The registered scheduled task and build_universe.py are not touched. PRD v0.13 @1699960261 is the working-tree PRD (git diff --quiet rc 0, ancestor of HEAD); v0.12's constraint line numbers differ by +10/+11 and were NOT reused.
- **`AMGT-rk-39`:** Read at HEAD (lib/research/filings last moved @db6c40083f). The cutter is fetch.py SECTION_PATTERNS :103-152 with the bare 20-F riskfactors fallback at :128 and the unbounded fallback at :316-322 (D9, measured: 70,000 chars of a patient story cut from CSL under 20-F rules; the exact printed line is quoted in the order). extract_sections :329-350 returns text '' with full_chars 0 for a missed key and its docstring :333-334 calls that visible; build_source_object :411 and :440-447 persists officer_section text '' extracted False as a success (E10; ASML/PBR are the served instances, not re-fetched). passages.py :146/:174 make any line under 60 chars a heading, so raw PDF lines give 9.3%/1.8% coverage; the validation's PyMuPDF block reflow gave 91.6%/92.4%. pymupdf 1.28.2 and pypdf 6.16.2 are installed (probed on this device); no language library is (langdetect/fasttext missing), so detect_language is a script-share rule. CONTENTION: fetch.py is shared with AMGT-rk-38 (build_source_object :377-448, unresolved_source_object :359-374, latest_filing :177-215, pool_key :451-452) -- disjoint regions except PARSER_VERSION; this cell should land FIRST because rk-38 and rk-40 consume document.py. No other F cell touches document.py or test_document.py. ESEF is deliberately NOT a declared family (no validation name exercises it).
- **`AMGT-rk-40`:** Read at HEAD (lib/research/filings last moved @db6c40083f). passages.py:67-79 to_ascii folds evidence text and build_passage_map :182 stores the folded text (6.8% of Japanese kept, 7 of 28 passages empty); analyze.py folds again at :401, :427, :552, :814, :957 and records it at :951-956. crosswalk.serialise :439-441 is ensure_ascii=True, so the pool bytes stay ASCII without folding the text. pass_1 :285-293 sends one plain-text document (whole-document citations on Japanese, D16); the validation's design A sent a content document with one block per passage and got 1 block per citation, 72 of 72. drafting_build.py:93 splits on spaces (0 of 68 runs on Japanese); verbatim.py:42-50 has no NFC and collapses to single spaces. CONTENTION: analyze.py is shared with AMGT-rk-42 (main :1101-1231, the writer :1210-1230, DEFAULT_UNIVERSE_PATH :1095-1097, ANALYZER_VERSION :60 and its fingerprint) -- disjoint regions except the version constant, reconciled per 1.4; drafting_build.py is shared with AMGT-rk-41 (this cell :70-128 and :197-206; rk-41 the HOLD/split in :188-247 and pipeline.py); verbatim.py is this cell's only (rk-41 does not edit it). Suggested lane order on these files: rk-42 -> rk-41 -> rk-40 (rk-40 last, because it is the largest change to analyze.py and the only live model spend).
- **`AMGT-rk-41`:** Read at HEAD. The hole is verbatim.py:53-62 (an empty span is vacuously True) reaching pipeline.py:143 (PASS appended) and drafting_build.py:243 (verbatim_pass counted without a split); the docstring :44-46 and schema.json:108 both describe the vacuous PASS as intended. The adapter re-runs the gate at scoped_amgt.py:1496-1500 and would still accept a zero-span sentence -- named OUT OF SCOPE in the order (chain B's file, a Lambda change) with a read-side planted negative (AC4) instead. The record contradicts the earlier drafting instruction (LABEL interim): the six-cards record and PRD v0.12/v0.13 :912-913 rule HOLD, and the COO's correction confirmed it -- the order implements HOLD with no switch. Analysis s.3.8 defers rebuilding the 11 stale drafting objects for CONTENT; this order rebuilds the served set only to APPLY THE GATE (no model call, the rk-19 re-apply precedent) and says so, so the COO can strike AC6/AC7 if s.3.8 is read as barring even that. CONTENTION: drafting_build.py shared with AMGT-rk-40 (disjoint regions); pipeline.py and schema.json are this cell's only; verbatim.py NOT edited here. The CAT source object is fetched by the EXISTING fetch.py --cik path (works before or after rk-38/rk-39 land).
- **`AMGT-rk-42`:** Read at HEAD (lib/research/filings last moved @db6c40083f). ANALYZER_VERSION :60 has never moved although the contract did at rk-19 (:776-834); the intake measured six pool analyses, stale and current alike, at 1.0.0 -- a skip rule on that field would lock the stale ten in, hence version-then-skip. The registered task's launcher is split at the space (measured live by this pass; batch.py:125-126 builds /TR with one quote pair, which schtasks strips). run_batch.cmd:9 pins 2026-09-15; analyze.py:1095-1097 DEFAULT_UNIVERSE_PATH reads a WORKER folder with a typed date -- a fourth C-PRODUCTION-HOME instance beyond the three the analysis names, found here. Two writers of drafting/v1 confirmed by a repo-wide .py census (batch.py:150, analyze.py:1215; packs.py:107 and scoped_amgt.py:1336 read). CONTENTION: analyze.py shared with AMGT-rk-40 (this cell: version constants, main :1101-1231, the writer, DEFAULT_UNIVERSE_PATH; rk-40: :277-990) -- disjoint except the version constant; batch.py and run_batch.cmd are this cell's only; AMGT-rk-41 CALLS write_outputs. Suggested lane order on analyze.py/drafting_build.py: rk-42 -> rk-41 -> rk-40. comp-schedule is a REAL declaration (an existing disabled task is re-registered, never enabled).
- **`AMGT-rk-43`:** Read at HEAD 4f44431d34 (workspace) and 625a0888 (portal, = origin/DEV per the analysis). scoped_amgt.py:2305-2371 flips SERVED at :2346-2348 on any parsed object, never reading the officer count -- the five zero-officer objects (ASML, HAL, INTU, KMB, PBR; live read 2026-09-18) therefore serve SERVED; ceo_profile_reading at :2275-2302 derives its state from a regex over the basis SENTENCE (:2272, :2290-2296), so the 7 objects the producer never searched (query null, absence_class left at the default NOTHING_FOUND, enrich.py:414-425) read NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY and the page prints a hard-coded false sentence (ExecManagementTab.tsx:87). CONTENTION: this order holds lib/research/api/scoped_amgt.py WHOLE-FILE -- a single-writer surface shared with chain E's AMGT-rk-45 (the one-line pool read at :2343), with R14-E5 (roster_source served), R14-P3 (peers shape), R14-L1 (empty_reason) and R14-T7 (handler slash-indifference); the COO sequences every one of those after this order or folds the one-liners into this deploy. BOTH the adapter and the page are touched, deliberately: the analysis row names the CEO line, the empty-roster render and the zero-officer status, which are two files on two repos; the page half is a DEV-durability commit only (nothing serves DEV, intake L10) and needs a worktree with portal/ checked out (R14-T6). The state enumeration is by subtraction over the M-1 ceo_profile object's fields (status/url/query/absence_class/basis); the fifth PRD page state SEARCHED-NOTHING-KEPT is unreachable before R14-E6 and is said so in the order rather than invented. AC5 is a judgment criterion because mandatory MFA blocks every headless authenticated capture (analysis s.3.5; rk-26 withdrawal).
- **`AMGT-rk-44`:** Read at HEAD 4f44431d34. batch.py:83-85 splits every filings/v1 key on '/' and takes parts[2], requiring parts[3] to end .source.json, so a slash name's key (5 parts) is never counted -- BP/_LN_Equity and NG/_LN_Equity can never be built; the same walk counts UNRESOLVED-SOURCE.source.json placeholders (rk-24's, filings/batch.py:198) as filings: measured live 190 keys = 178 placeholders + 12 accessions, so the census would say 188 buildable. task_definition() :119-120 wraps the launcher in one pair of quotes that schtasks consumes as the delimiter, leaving the path split at 'Opal Bloomberg' (Execute C:\Users\Opal, measured); run_batch.cmd:12 pins universe/v1/2026-09-15.json while 2026-09-16 exists. NO CONTENTION inside chain E: batch.py, run_batch.cmd and the tests file are touched by no sibling (rk-45 edits enrich.py, rk-46 edits roster.py; rk-46 ALSO adds tests to tests/test_management.py -- an append-only shared file inside the same chain, so the two workers' additions land at different class positions and the COO drains them in sequence). The preflight comp-schedule line is a REAL declaration: an existing DISABLED task's action is corrected with schtasks /Change /TR, never enabled; the COO should read that line before gating, because the brief's NEVER list names 'any schedule' and this order touches one deliberately and says so. Reconciliation of the two batch drivers (batch.py vs integrations/.../management_posture_batch.py) is a stated residue, not this order's act.
- **`AMGT-rk-45`:** Read at HEAD 4f44431d34. enrich.py:594 keeps only keys ending /<as_of>.json, so each run pools itself; :569-579 reads universe/v1/<as_of>.json at the same date (null names_in_union on 18 Sep, no 18 Sep vintage); :605-606 averages STORED tenure_years measured at each object's own as_of. scoped_amgt.py:2343 binds the served pool to the name's as_of, so the page serves TWO pools (15 Sep names get the 15 Sep pool; NU/VLO get the empty 18 Sep pool) -- one pool on the SERVED plane needs the adapter line, which is why this order carries it and why it is sequenced. Writers of management/v1/_pool/: enrich.main :689-690, batch.main :190-191, management_posture_batch.py :194-195 -- N=3, all through compute_pool(), so the fix moves all three together (the never-widen half must print N=3). CONTENTION: enrich.py is ALSO R14-E5's and R14-E6's file (roster_source; the CEO search rewrite at :404-455) -- the CTO marked E3 independent and E5->E6 chained; the regions are disjoint (compute_pool :582-616, read_universe :569-579, main :633-702 vs build_document :490-550 and ceo_public_profile :404-455) but it is the same file, and the COO sequences the drains. tests/test_management.py is shared with rk-44 and rk-46 (append-only within chain E; different classes). Zero-officer objects are excluded from names_with_roster by this order's rule, consistent with rk-43's served rule; BABA/NU/VLO count as rosters with 0 tenures (their role starts are rk-46's parser gap).
- **`AMGT-rk-46`:** Read at HEAD 4f44431d34. roster.py:97-99 and :118-119 accept any capitalised run as a name -- measured in PRODUCTION today on VLO (management/v1/VLO_US_Equity/2026-09-18.json carries an officer named 'Senior Vice', the wrapped 'Harminder S. / "Homer" Bhullar' row), the same class the validation measured on CSL (D20); :121 needs '<year> <age>$' so VLO's bare trailing age stays inside the role (five roles end in the age); :193-201 asciify the whole section before parsing, erasing Kanji names (D22; the pool bytes would stay ASCII anyway via crosswalk.serialise ensure_ascii=True :439-441); no shape reads CAT's 'Name (age) Role (year)' (D21) or KMB's 'NAME , NN, was elected ROLE in YEAR' (194 lines, 0 candidates); HAL and INTU's Item 10 point elsewhere (Part I pp.7-8 / the Proxy) and read 'no declared shape' rather than naming the pointer -- CAT's Item 10 has the same shape (D10), so the new section_refers_to field is the roster's handoff to the filings cutter (R14-F2). :496 sorted(keys)[-1] would pick a placeholder over a real accession. NO CONTENTION on roster.py or the schema; tests/test_management.py is appended by rk-44 and rk-45 too (append-only shared file, classes at the end); enrich.py is read only (its absence classification :165-195 will class an incorporated-by-reference section as pull-missed, correctly). Fixtures come from the validation subagent's scratch folder, which survives on this device at draft time; the order STOPS rather than fetches if it is gone. AC2 uses build_roster in-process (roster.py --dry-run reads the pool the same way) so six names print in one bounded invocation.
- **`AMGT-rk-47`:** Read at HEAD da7b0b1804; git diff --stat 1699960261..HEAD is EMPTY for the PRD, the round-13 analysis, lib/research/management/ and serp.py, and the PRD/analysis carried no diff 9c8e04cd9a..4f44431d34 either, so every line cited is current. The PRD moved v0.11 -> v0.12 (@4de34f0d95) -> v0.13 (@1699960261) while drafting; C-EXEC-MANAGEMENT sits at :722-757 at v0.13 (it was :723-760 at v0.12), C-VALIDATION-NAMES :1652-1657, C-PRODUCTION-HOME :1643 -- all re-measured on the v0.13 bytes. CONTENTION 1: the adapter read_management (scoped_amgt.py:2346-2369) copies NAMED fields, so roster_source and the fallback label do not reach the page until the R14-E1 cell (analysis :131) or a chain-B order serves them; this order keeps the adapter and portal as walls and makes the OBJECT carry the label, which is the CTO row's scope ('roster_source on every object'); the COO should tell the E1 cell's worker the field names (roster_source, fallback.label). CONTENTION 2: enrich.main --write-pool also recomputes and rewrites management/v1/_pool/<as_of>.json (enrich.py:689-699), which would move the pool comparison served on every 18-Sep object and collide with the R14-E3 pool cell (analysis :133); the order adds --skip-pool and every live write uses it, and AC3 prints the pool object's ETag before and after as the control. CONTENTION 3: three cells edit enrich.py::build_document (rk-47, rk-48 on slot ~49 in sequence; rk-49 on slot ~50 gated on rk-38) -- rk-49's hunks (domain_for :138-146 and the Lusha block :497-505) are disjoint from rk-47's (:494-496) and rk-48's (:532-536), but the COO should drain rk-49 after rk-48. DESIGN NOTE: the fallback keeps roster_status UNRESOLVED-SOURCE and roster_reason on the object (PRD :727) and marks the roster by roster_source, so compute_pool's existing filter on roster_status == RESOLVED (enrich.py:599) excludes fallback rosters from the tenure pool without an edit -- coherent with PRD :752 ('EVERY current FILING roster'). The three validation names are NOT in the crosswalk (validation report :37-53), so the adapter cannot serve them until R14-I1 lands; the pool writes are still on a served prefix, hence co-sign per the CTO table. Slot ~49 and ~50 are unused (deliverables folder lists ~1..~34). Bloomberg sign-in is a human act with a 2-attempt budget (READ_HERE.md:41-48); the order makes health() the first read and a BLOCKING row the fallback. No lane row for integrations/bloomberg/research/ or lib/research/management/ was found in .owned-paths.yaml by grep (Rule 27: the worker's write surface is its <paths>).
- **`AMGT-rk-48`:** Read at HEAD da7b0b1804 (serp.py and the management package unchanged 1699960261..HEAD by git diff --stat). VENDOR-WORD GAP, FOR THE COO TO SETTLE AT THE CUT: the CTO's row runs the SERP on the validation names and Andrew's ~17:2xZ word adopted the design, but PRD v0.13 :751 says Bright Data calls 'run only under Andrew's per-use word', :1656 names ONLY Lusha and Seeking Alpha as authorized inside the validation, and the 17xxZ record's own narrow reading (:44-45) says whether the running validation calls Bright Data 'is NOT answered by this'; the ~18:4xZ grant covered 10 requests for the CRO's exploration only (:52-56). The order therefore lands the primitive fix and the agent OFFLINE (AC1-AC3, mutant pair, namesake anchor, verbatim control) unconditionally, and makes the live search (AC4-AC6) conditional on the spawn prompt stating the per-use word is on file, refusing with a row otherwise -- the COO can convert that to unconditional by naming the record in the spawn prompt. LANE NOTE: data/find/dualbiz/scripts/serp.py is FIND_DUALBIZ's file (design :321-322); its two other callers (serp.py:47, casec.py:80) keep list[str]; the worker's <paths> grants the edit and the return type is frozen. COMPATIBILITY: read_management (scoped_amgt.py:2367-2368) reads ceo_public_profile by name and derives ceo_profile_reading from its basis string, and the R14-E1 cell (analysis :131) rewrites that reading on absence_class -- so this order KEEPS ceo_public_profile as a projection of the new ceo_profile block (status/absence_class/basis derived) rather than renaming the field mid-round; serving ceo_profile itself is chain B's act. OPEN L4 (PRD :757, whether a Bloomberg-fallback CEO is searched): the block records name_source from rk-47's roster_source; on the validation names the roster is expected BLOOMBERG_FALLBACK (no filing in the pool per the validation report :37-53 unless rk-38 lands first), and the order searches whichever CEO the roster carries and prints name_source so the L4 decides on a measured field. KEYENCE: _CEO_RE (roster.py:154) may match no Japanese title ('President and Representative Director'), giving NOT_SEARCHED/NO_CEO_ON_ROSTER -- one of the five states; the order forbids widening _CEO_RE and asks for a row. TIMEOUT: one CEO per live criterion (AC4 CAT; AC5 CSL+Keyence) with max_pages 3 keeps each under timeout 120; if a fetch-heavy CEO overruns, the worker refuses that criterion with its measurement rather than raising the caps. The change-management entry is NEW (never re-use rk-47's); the never-widen pair names the same three keys and the same three writers. Secret names verified in source: find-insure/bright-data/api-key (serp.py:206-208), zone default serp_opal (:239-241), anthropic-api-key (analyze.py:229, judge.py:131).
- **`AMGT-rk-49`:** Read at HEAD da7b0b1804 (management package unchanged 1699960261..HEAD). The COO's two corrections are applied: PRD cited as v0.13 @1699960261 throughout, and the Lusha call runs LIVE inside the cell on the three validation names (the earlier 'held until card 4' framing is gone; the SIX_CARDS record :19 scopes 'full egress' to the validation and NOT to the 33, and the order says so). GATE: depends_on AMGT-rk-38 -- the verified-site field on the filings source object does not exist at HEAD (fetch.py:425-448 builds no such field), so its NAME is unknown to this drafter; the order has the worker read rk-38's order and instance at spawn, name the field on the first line of its report, and STOP with a BLOCKING row if rk-38 is not complete. No placeholder token is used. ORGANIC NEGATIVE ARM: the battery's verified site is step 4 (the company site), and CAT resolves at step 1 (EDGAR) per the validation report :86-96, so unless rk-38 records a site for every name CAT reads NOT ATTEMPTED with that reason while CSL (investors.csl.com) and Keyence (the IR library) carry one -- the order treats that as the rule working and files it as a row for the L4 (a US name resolved at EDGAR never gets a Lusha domain under this rule; widening is not this cell's). DOMAIN RULE: no eTLD+1 guess (stdlib has no public-suffix list); one leading label from a declared allow-list (www, ir, investors, investor, corporate) is stripped and the rule is printed on the object (investors.csl.com -> csl.com; www.keyence.co.jp -> keyence.co.jp). RE-BILL AVOIDANCE: a full build_document re-run would re-pull Bloomberg and re-bill rk-48's SERP and model calls, so the order adds --enrich-only (load the newest object, run only the Lusha step, write back under the same as_of). CONTENTION: enrich.py is edited by rk-47, rk-48 (slot ~49) and this cell (slot ~50); the hunks are disjoint (domain_for :138-146 and :497-505 here vs :494-496 and :532-536 there) but the order tells the worker to STOP if roster_source or --skip-pool is absent from its worktree's enrich.py, i.e. drain this after rk-48. CO-SIGN: the CTO table marks E7 'gated on R14-F1', not 'yes', so co_sign_required is false here, but the order rewrites the same three served-prefix keys as rk-47/rk-48; the order makes the live write wait for the spawn prompt to say whether chain E's existing pair covers it or a fresh pair is on file -- the COO decides. domains.json stays on disk because batch.plan (batch.py:97, the R14-E2 cell's surface) reads it for a dry-run census; only its use as a Lusha input is retired. Slot ~50 is unused.
- **`AMGT-rk-50`:** Read at HEAD 4de34f0d95 for code (byte-identical at 1699960261, which touched only the PRD and one record). The load-bearing measurement: lib/opal_naming.py address('seeking-alpha','amgt','bronze','peers','CAT_US_Equity') REFUSES today with exactly 'scope 'amgt' resolves to no scopes.json row' (_long_scope :1530-1539) because amgt is a PRODUCT SYSTEM (systems.json:47) with no scopes.json row; with the row added the builder yields s3://opal-data-assets/seeking-alpha/global/bronze/peers/CAT_US_Equity (PRODUCT bronze home = shared opal-data-assets, tiers.json). Rule 30 makes the row the mechanism, so the order grants infra/logic/registry/scopes.json in <paths> (worker_grant, .owned-paths.yaml:44-47: a worker is admitted to exactly the <paths> its order names, never a lane; the lane on infra/logic/** is PLATFORM_LOGIC_DOCS :1928-1930). CONTENTION the COO should weigh: (1) the registry row makes the DEC-5 generated views (generated_locals.tf etc., lib/opal_naming.py:68-76, :97-108) lag the registry; the order forbids the worker from regenerating them (naming-gate REFUSES a hand edit to a generated file) and has it file a surprise row for the PLATFORM_LOGIC_DOCS lane; (2) the no-registry alternative the builder ACCEPTS today is scope 'global' (GLOBAL/COMPOSITE, bronze home also opal-data-assets): address('seeking-alpha','global','bronze','peers','CAT_US_Equity') = s3://opal-data-assets/seeking-alpha/global/bronze/peers/CAT_US_Equity -- semantically a misfile of a product's data under the composite scope, so the order does not take it; if the COO withholds the registry path, swap 'amgt' for 'global' in steps 0-1 and AC2/AC3/AC6 and drop scopes.json from <paths>. Other facts: engine.py:72 BASES refuses 'sa' today (the _make guard :619-621); rest_fetch.land_raw :211-218 writes a hand-typed key into config store_bucket opal-data-harvest, so the order lands raw with its own put at the builder address and never calls land_raw; scoped_amgt.read_peer_set :1276-1278 serves the object whole so the adapter is untouched; the SA search endpoint the CRO used (sa_symbol_resolve_pass.py:55-56) is /api/v3/searches, reachable through _do_get. The naming limb of safe-commit runs in WARN mode (naming-gate docstring; org/mcp/naming-gate.enforce absent at the cut -- re-check at spawn). Bloomberg growth fields and the 11 SA metric fields are the CRO's measured list (brief :82-96). The validation names' keys follow crosswalk.py:334 minting (CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity); none is in the crosswalk until R14-I1, so the objects record identity UNRESOLVED honestly. The COO's earlier note said card 3 was OPEN; the files at HEAD say card 3 answered YES (analysis :166-172), C-SA-VENDOR-WORD lifted by name (PRD :1108) and terms CLEARED (PRD :1109, v0.13) -- the order follows the files. ISSUER AMENDMENT at the cut: the scopes.json row is withdrawn (Andrew ~21:1xZ, msg 23774: no amgt scope row; opal-data-harvest registered as the pool home); raw lands under the COMPOSITE global scope, which address() builds today.
- **`AMGT-rk-51`:** Read at HEAD 4de34f0d95 for code (byte-identical at 1699960261). The defect is exact: peers_v.score_peers_v() :270-275 returns its suppression sentence under the key 'reason' and never sets 'absent_reason', and the measured return :276-277 sets neither 'value' nor 'absent_reason'; run_scores._peers_v_record() :177-185 stores that dict verbatim, so read_scores() (scoped_amgt.py:2424-2430, 'verbatim') serves peers_v with absent_reason MISSING on 33 of 33 while robustness (run_scores.py:133-157) and divergence emit real reasons -- the asymmetry the analysis names. classify.py:32-47 is the shape to return. The floors move at :62-64 and the asserts :69-70 cite the old ruling; test_score_modules.py:331-337 builds 5 peers to prove suppression and will pass for the wrong reason at floor 5 -- the order moves it to 4 peers and adds the 5-peer control. run_scores.run() :216-232 has no per-name scoping and iterates the 33 -- the order adds --security-key and BOUNDS forbid a bare run; AC5 proves no covered name's scores object was written today (denominator = the newest crosswalk's keyed count, re-measured). The fields pull is a NEW module in lib/research/scores/ that imports sa_peers.entity_test from rk-50's module for the name-agreement check (the same trap one hop out); its raw address uses the same scope rk-50 landed under (amgt after the registry row; 'global' if the COO took the fallback) -- the order tells the worker to read rk-50's AC2 output rather than assume. CONTENTION: run_scores.py and peers_v.py have no other writer this round (chain P only); the change-management and .open_deploys folders are append-only shared surfaces (Rule 14b: do not isolate there). The R-1 objects for CSL/Keyence may honestly be absent from rk-50; the order makes the ABSENT record with a named reason the PASS of the honesty clause and AC6 grades exactly that.
- **`AMGT-rk-52`:** Read at portal DEV @625a0888 (the submodule's HEAD at the cut; rk-26's withdrawal note :135-136 records it typechecks and production-builds clean). The page today: PeerBasis :390 has no 'sa'; cscTable.ts:30-32 carries exactly one member field (market_cap_musd) and its summary rows :137-150 carry n but no source; PeersTab.tsx cellText :39-44 has no source label and no not-meaningful state, and the badge :59-66 knows analyst/derived only. The adapter (scoped_amgt.read_peer_set :1276-1278) serves the R-1 object WHOLE, so rk-50's new fields (basis sa, members[].cells, csc_columns.sa_shape) reach the page with NO adapter change -- scoped_amgt.py is deliberately OFF this order's <paths>; if the worker finds the adapter drops a field, the order says REFUSE with a row (single-writer surface the COO sequences), never edit. PostureTab.tsx :339/:347 is a second consumer of usePeerSet and must keep compiling (AC1 is the whole project build). INSTRUMENT: no browser capture (MFA, analysis s.3.5, rk-26 withdrawn); the proof copies tabs.harness.cjs :1-57 (real components transpiled with the installed typescript, react-dom/server render, captured adapter bytes as fixtures, CHECKS-OK/CHECKS-WRONG-WAY verdict :483-501) into a PeersTab-only harness with two PLANTED mutations (a not-meaningful cell must render n/m never 0.00; a fallback cell must carry its SA:<field> label) and a derived-basis regression arm on tabsFixture.BA_US_Equity.json. COMMIT MECHANICS are the contention to watch: the portal is a separate git repo on branch DEV; safe-commit.sh is the workspace's tool and the order tells the worker to try it from the portal root first and fall back to git -C portal commit --author with the refusal recorded; the workspace 'portal' gitlink is NOT bumped by the worker (lane ANY, DT/MSTR act). The fixture depends on rk-50's CAT object existing with basis sa; CSL/Keyence fixtures are added only if their sets landed. The worker-provisioned worktree must have portal/ checked out (R14-T6) -- the order's first act checks it.
- **`AMGT-rk-53`:** Read at HEAD 81e59d3818. The previous drafter's line numbers for compute_chatter_axis (:812-857) and the chatter carrier (:656-771) were STALE against HEAD (fda8d96c0a): compute_chatter_axis is :779-882 with its product loop at :812-848; the carrier spans :142-155 and :541-776. All other cited lines re-derived and confirmed. The previous draft had the WORKER deploy both Lambdas (AC7 a boto3 invoke of the deployed function, a DEPLOY block, change_management paths, a universe_snapshot.json path that does not exist in the tree) -- all replaced per the issuer rule: AC7 is now an in-process handler() invocation on the worktree bytes against the live table (read-only), the deploy is the COO's consolidated act, and the change-management paths are dropped from <paths>. Two things a naive read misses: (1) the existing arm test_chatter_axis.py:355-407 ASSERTS the defect (10 zero-signal rows ranked) and must be rewritten, stated in AC1; (2) both Lambda builds already carry a new lib/research/metrics module without a build edit (build_zip.py packages the import closure; the scoped-amgt build seeds lib/research/metrics whole), so the COO's deploy needs no Terraform change. CONTENTION: scoped_amgt.py is also edited by rk-61 (disjoint regions); chatter_axis.py is not touched by any other round-14 cell; the price writer is not touched by the COO's card-B direct act (MIN_ABSOLUTE_JUMP lives in movement_gate.py, read-only here). Portal: the nested repo is on DEV @625a0888; a linked worktree carries an EMPTY portal gitlink (W31-S1), so the page half depends on rk-60 or the main-tree mode.
- **`AMGT-rk-54`:** Read at HEAD 81e59d3818. THE MECHANISM ANSWERS HALF THE QUESTION BEFORE ANY MEASUREMENT and the order says so without pre-judging the counts: the harvester associates an article with a security BY THE JOB it ran for (worker.py:57,102,116 -> catalog.py:74), never by content, and a job runs only for config.json's five pilots unless --all-securities, whose universe() gives every non-pilot a security-<sha16> key (__main__.py:12-36,66). So 'association' can only fail for a name whose crosswalk record lacks the harvester's key form, and 'ingestion' fails for every name no job ever ran for. The runtime ledger (progress.sqlite3, device-local, gitignored, present on this box at 282,624 bytes / 2026-09-15) is the ONE instrument that separates NEVER-JOBBED from JOBBED-NOTHING-STORED, so AC3 reads it by ABSOLUTE main-tree path (a worktree read is ABSENT by construction, stated in BOUNDS). Found while drafting, recorded for a row not a fix: config.json universe_source points at a WORKER deliverables folder (0.9.0_WK_AMGT_RESAPP~3/universe.json) -- a fourth C-PRODUCTION-HOME instance beyond the three the analysis names; and the chatter Lambda's build_zip.py:91 bakes its universe snapshot from deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json (same class, off this cell). CONTENTION: none -- this cell edits no code and no other round-14 cell writes under deliverables/~54/. The COO should settle whether AC4's `python -m lib.opal_data_harvest universe` (which imports the package and calls a legacy() reader) is acceptable as a read on this device, or whether the config values alone suffice; the order treats a non-zero rc as UNMEASURED, never as a failure.
- **`AMGT-rk-55`:** Read at HEAD 81e59d3818. The gate has NO limb that reads <round> (0 matches in 2834 lines) and its issuer limb GATE (iv) grades the committing SERIAL, which is exactly why S154's two continuations of 2.0.0_SA_COO~Z both passed. The record face already carries the key (94 of 97 orders at HEAD carry a <round> element; the 3 without are legacy and are NOT back-filled). The limb is keyed to the ROUND at HEAD and grades NEWLY-ADDED only, so a worker's status flip and a COO re-cut of an existing order (both MODIFY) are never refused; the ONLY escape is the existing audited '# pipeline-override: <reason>' (:2412-2434), and the order adds no second token. CONSEQUENCE THE COO MUST OWN: from the moment this lands, every round's issuance is ONE commit -- a second commit adding orders into round 14 is refused; the 27-cell round-14 issuance must therefore be staged and committed as one act (Rule 27 already says ONE ISSUANCE). CONTENTION: rk-56 edits the same file and the same self-test list; sequence the two (either order) and the second rebases on HEAD's bytes. AC4 stages a probe file in the worker's own worktree index and resets it -- it never commits; the gate's other limbs (cell_refs on a copied rk-19 face, LIMB 6) may also refuse the probe, which the criterion records and does not count.
- **`AMGT-rk-56`:** Read at HEAD 81e59d3818. check_file() has no limb that reads the record face's status; the only status limb (check_complete_flip :2524-2560) fires on a DONE word, so an order born WITHOUT the element meets nothing -- S153's 15 of 15. Three readers downstream already learned the same lesson separately (to-check.py FIX C masks code spans; owned-paths-validate.py anchors the line after Z-S15; surprise-row-gate reads '<no status tag>' as OPEN), so the new limb is born line-anchored and a prose mention is inert by construction. TAXONOMY NOTE for the COO: two terminal vocabularies exist -- DONE_WORDS (4 words, to-pipeline-gate.py:2507) and TERMINAL_TO_WORDS (8 words, surprise-row-gate.py:152); the born-terminal arm reads their UNION and says so in its docstring rather than minting a third list; unifying the two is a separate act. The 3 untagged orders at HEAD are terminal-by-proof (S169's bucket) and are NOT back-filled (prospective only, the gate's own doctrine); if the COO wants them tagged that is a hand MODIFY. CONTENTION: rk-55 edits the same file/regions; the order names the sequencing check (git log on the file) and asks the worker to state in its report whether rk-55 was at HEAD. AC4's python probe writes the stripped copy with newline='\n' and the invocation resets the index and removes the file; it never commits.
- **`AMGT-rk-57`:** Read at HEAD 81e59d3818. The census (:1125-1165) reads terminality exactly as the spine says (VALID instance = terminal; :436, :487-488) and _proof_verdict reads the checker's rc ONLY (:1049-1050) -- so the ruling is implemented as a SECOND read beside the first, never as a change to the first. DESIGN CALL MADE HERE AND STATED FOR THE COO: the acceptance read is a NOTE at slug time plus a CLI read, NOT a refusal -- the same file was corrected at 7f82f66f93 to 'a gate refuses an act only when that act can remedy its condition' (:991) and a slug cannot remedy a FAIL (the CVO grades at L9, the COO recuts at L10); making a FAIL refuse the slug would also be an agent-made approval gate. The CTO's words are 'gains an acceptance read ... denominator printed', which the note satisfies; if the COO and CTO want a refusal, that is a widening for them to card. EXPECTED DISAGREEMENT WITH THE HAND SWEEP, stated in BOUNDS: the CTO counted 26/3/0 over 15 orders; the tool will class rk-26's criteria UNVERIFIABLE (withdrawn, no instance) and rk-30 page-half AC2 FAIL, so the tool's line will not equal 26/3/0 and the order says record the difference. CONTENTION: surprise-row-gate.py is edited by no other round-14 cell in this drafter's set (rk-55/56 edit to-pipeline-gate.py); the worker's own surprise-row commit is graded by the worktree's edited gate, so the order requires a dry run and --self-test before committing.
- **`AMGT-rk-58`:** Read at HEAD 2553fe61ff (PRD at HEAD identical to the v0.13 pin 1699960261: git diff --stat empty). The row's RESIDUE is already cleared: the scores/v1/ Terraform entry the worker could not commit landed at 3c2a6e47ca under the COO's own lane and sits at scoped-amgt-api.tf:161, so this cell is the MECHANISM only. The mechanism chosen is the MINTER (option 1 of the CTO's either/or), not a second grant source inside owned-paths-validate.py: ADHC_OWNPTH.005 (Andrew-direct 2026-09-04, record @9ef9a40aae) makes the ORDER the one grant and the gate reads task-order files at HEAD only (:176-206); reading a signed pair inside the lane gate would widen a mechanical gate against that ratified single-source rule. The pair's role is preserved as a BOUND: the minter refuses any --path neither half names verbatim. The minter never leaves an order the L6 gate would refuse: it imports to-pipeline-gate.py's check_file (importable, :2402) and deletes its own output on any violation. AC2's fixture must sit under task-orders/ because check_file resolves the project from the path (TREE_TO_RE :59); it is a hidden dotfile written and removed inside one invocation and is granted in <paths> only so the write is not a wall -- the order forbids committing it. Contention: .tools/** and .claude/** are lane ANY; the worker is admitted by this order's <paths>. No sibling round-14 cell names .tools/direct-act-order.py or SKILL.md (rk-60 edits SKILL.md Step 4 :173-177, a DIFFERENT paragraph of the same file -- the COO sequences the two SKILL.md commits or lets safe-merge resolve the non-overlapping hunks). The COO must write the round-14 decomposition s.22 entry for AMGT-rk-58 before the cut (the gate's <owned_cells> limb grades the token against the decomposition).
- **`AMGT-rk-59`:** Read at HEAD 2553fe61ff. chatter-axis-schedule.tf:124 reads source_code_hash = filebase64sha256(local.chatter_axis_zip) with the zip gitignored (.gitignore:95) and built only by lambda_src/build_zip.py; a fresh linked worktree has no .build/, and Terraform evaluates that expression for every plan in the root regardless of -target (row W34-S1 :8689, :8697). The CTO's s.3.7 either/or is taken on its first arm: ONE expression, fileexists() ? filebase64sha256() : null, identical value when the zip is present, null (no error, attribute left to the provider) when absent; the function itself still cannot be applied without the zip because filename is read at apply, so the fail-closed moves to the resource that needs it. The second arm (running build_zip.py in provisioning) is not taken and rk-60 does not take it either. The order names NO apply: a config change whose value is unchanged when the zip is present is applied by nothing; AC4 builds the zip as the positive control and records the targeted plan on the function -- any diff there is the PRE-EXISTING build/live delta (sources moved since the 2026-09-15 deploy, and rk-53 moves chatter_axis.py again this round), which belongs to the COO's consolidated chatter redeploy under rk-53's pair. change_management/ and .open_deploys/ are granted per the brief but the order forbids opening an entry. The provider's handling of a null source_code_hash (Optional; state value kept vs. a change block) is what AC3 RECORDS rather than asserts -- the bar is the absence of the evaluation error and the confinement of any function diff to source_code_hash. Lane read before naming any apply: infra/aws/** -> CLOUD_OPS_OR_ETL (.owned-paths.yaml:1906); the worker is admitted by this order's <paths>. Contention: no other round-14 cell names chatter-axis-schedule.tf; rk-61 needs a plan in this same root and hits W34-S1 unless rk-59 has landed or rk-61's worker builds the zip -- the COO settles the sequencing (rk-61's draft carries both branches). terraform init's touch of .terraform.lock.hcl, if tracked, is not in <paths> and must not be committed -- the worker reports it if it appears in git status.
- **`AMGT-rk-60`:** Read at HEAD 2553fe61ff. portal/ is a NESTED git repository, not a submodule (.gitmodules 0 bytes), so `git submodule update --init` can never populate it; the superproject gitlink (2453a7b4) is 6 commits behind the nested repository's DEV HEAD (625a0888), which carries round 13's page work -- so provisioning at the gitlink commit (the row's disarm shape (b) as worded) would hand a page worker a stale tree; the CTO's row says 'the issuance says which', and the order makes the ref an argument (--portal-ref, default the nested HEAD) printed with the gitlink gap, and tells /dispatch to carry it as portal_ref: in the issuance's fanout data. The nested repository already carries linked worktrees at this exact shape (wk-amgt_resapp-11-1-portal) and one `prunable` entry -- the shape is precedent and the prunable entry is the failure the remove verb retires. node_modules is LINKED to the main tree's (a junction when cmd.exe is on PATH, a symlink otherwise -- the one device-purpose branch, guarded by capability) so no install runs; install mode exists but is not exercised. The worker proves the portal verb INTO ITS OWN WORKTREE (the empty gitlink directory the row measured) and removes it in AC5 so the COO's drain finds a clean worktree. Contention: rk-58 edits a DIFFERENT paragraph of the same SKILL.md (:208-224 vs Step 4 :173-177) -- the COO sequences the two commits or lets the non-overlapping hunks merge. The alternative disarm shape (a), a .gitmodules entry, is not taken (the repository is managed as a nested repo by design and a submodule conversion is not this cell's to rule). rk-59's alternative arm (build_zip.py in provisioning) is deliberately NOT folded in. The COO must settle at the cut whether page cells this round (rk-53's page half among them) are spawned through this script (then rk-53's page half depends on rk-60) or in the main tree.
- **`AMGT-rk-61`:** Read at HEAD 2553fe61ff (scoped_amgt.py last moved @e2d89be7da). The router's positional match is at :3315 (len(rest) == 3) with unquote at :3322; a literal slash yields four segments and falls to the :3396 refusal -- exactly what W27-S10 measured by direct lambda.invoke. The fix is the row's own first shape (join rest[1:-1]). TWO FACTS THE COO MUST HOLD AT THE CUT: (1) the gateway's route keys (scoped-amgt-api.tf:286-308) are single-segment {security_key} with NO {proxy+}, so a literal slash never reaches the Lambda THROUGH the gateway (the gateway 404s first) while the %2F form arrives on rawPath still encoded (payload 2.0) and already works -- the handler change removes the question for direct invokes, tests and any decoded arrival, and the served-plane discriminator for the literal form is the DIRECT invoke, as the row measured; the route table and gateway are deliberately NOT changed (a {proxy+} route is a wider blast radius no half signed). (2) The sibling draft rk-53 is internally inconsistent about who deploys the scoped API: its s.2 (:141-144) says rk-61's redeploy carries rk-53's adapter bytes, its s.4 (:179-185) says the COO redeploys both Lambdas once after rk-53 and rk-61 drain. This order follows the COO's issuer rule (a): rk-61 redeploys opal-amgt-scoped-api and its blast radius NAMES rk-53's rankings-response change (empty_reason) so the pair covers it; the COO settles the sibling text. depends_on: AMGT-rk-53 (the single-writer queue -- this order is cut from HEAD after rk-53 drains; AC3's census and the git log -3 check enforce it) and AMGT-rk-59 (the harvest root's plan precondition; the procedure carries the fallback of running build_zip.py when rk-59 has not landed, never a placeholder zip). The chain-T pair files NEVER_WIDEN_ROUND14_CHAIN_T_{COO,CTO}_HALVES.md do NOT exist at HEAD -- both are owed before spawn and AC1 refuses without them. The 13-route census uses BA_US_Equity (the round-13 precedent name, MEASURED in the crosswalk); the validation names are NOT keyed in the crosswalk and appear only in the in-process boundary test (their canonical-form strings; resolution not asserted). print is excluded from the live slash-pair census for render time and covered in-process. Contention: rk-53 edits disjoint regions of scoped_amgt.py before this order; the four remaining adapter cells (rk-53's sibling text names six in total) follow this one in the queue.

### 22c. POSTULATE RECORDS (Rule 24: MECE / GRAIN / INTENT / STATE) -- one per cell, 31 of 31, drafted per cell and adopted by the issuer

**`AMGT-rk-31` (R14-I1, FWD-2/V1; `C-INSTANTIATION-ENTRY`) -- MECE:** one entry step, one module
(`lib/research/identity/add_security.py`) plus the crosswalk builder it feeds; disjoint from `AMGT-rk-32`
(`build_universe.py`, step 1's read) and `AMGT-rk-33` (`build_universe.py`, `peers/universe.py`,
`model_block_pull.py`); no downstream stage is run and `universe/v1` is not touched (the "universe row" is its
own stage, PRD v0.13 :1623). **GRAIN:** every criterion reads the POOL object every reader resolves through
(`crosswalk.py:513-530`, the newest key) or the tool's own dry-run bytes, never a log line; the never-widen is
graded record-by-record against `crosswalk/v1/2026-09-15.json` (89 records, 33 MEASURED). **INTENT:** one axis
-- a security's identity lands in the pool from ONE Bloomberg call, or it is UNRESOLVED with the vendor's own
reason and no key is minted. **STATE:** moves the pool's newest crosswalk key (33 -> 33 + registrations that
resolved) and adds ONE optional `identity` block to registration records only; does NOT move a coverage record's
bytes, the coverage list's home (`crosswalk.py:71-74`, D2 -- a wall), `universe/v1`, any producer, the schedule
of the chatter Lambda, or the crosswalk's fixed point.
- *The one call* (`integrations/bloomberg/mcp/blp_client.py:135-145`, loaded by path as
  `model_block_pull.py:147-156` does): `reference_data(["<ROOT> <CC> Equity"], [NAME, EXCH_CODE,
  LEGAL_ENTITY_IDENTIFIER, CENTRAL_INDEX_KEY_NUMBER])` -- the yellow key appended AT THE CALL (PRD :878-880);
  `__error__` (:143) is the UNRESOLVED branch and the planted negative (AC3, "ZZZZQQ US").
- *Raw before derived* (PRD :899): the response lands at `raw/bloomberg/<KEY>/<stamp>/identity.json`
  put-if-absent (`model_block_pull.py:184-198`, the existing family :242-245) BEFORE the record derives; a dry
  run lands nothing and the criteria count objects before/after (AC2, AC3).
- *The registration is config beside the producer* (`C-PRODUCTION-HOME` :1643-1650):
  `lib/research/identity/registrations.json`, read by `build_crosswalk()` (:391-436) as a second input after the
  coverage list; `registered_at` is an input, so the fixed point (`test_crosswalk.py:192-199`) holds (AC7).
- *The record shape is `_record_for()`'s* (:257-384) plus one optional `identity` object; the schema's closed
  levels (`crosswalk.schema.json:6`, :63, :91) gain OPTIONAL properties only, so 2026-09-15.json still
  validates; `harvester_key()` (:178-198) gives a foldered registration the same association key a coverage row
  gets, and a folderless one carries pack-key and model-key only, with the reason in provenance.
- *The four folders:* `--folder` reads that ONE folder's ONE PAGER through
  `build_universe.discover_bloomberg_ticker()` (:191-238) with the template-placeholder rule (:109, :241-290);
  no ticker -> UNRESOLVED with reason, no call; AC1 re-measures the unregistered set as corpus folders MINUS
  crosswalk folders with both denominators printed (4 named by the analysis; the printed set governs AC5).
- *Co-sign class POOL WRITES:* the newest-key rule makes the write reachable by every served route, so the
  order opens a `.tools/deploy_ledger.py` entry before `--write-pool`, proves DELTA=0 on the 89 base records
  (AC6), and never modifies 2026-09-15.json (`write_pool()` :609-657 writes only the named `<as_of>` key,
  ETag-conditional :628); the never-widen pair, if the issuance owes one, gates AC4-AC6 only.
- *Ceiling:* 9 Bloomberg calls at the cut (3 validation + 4 folders + AC2 + AC3), idempotent re-registration
  makes no second call; no fleet run, no re-run of the 33.

**`AMGT-rk-32` (R14-I2, FWD-18 / V2-D1) -- MECE:** one function's READ (`build_universe.filing_identity_for()`
:491-539 and the loader that feeds it :478-484) in one file, sequenced AFTER `AMGT-rk-33` (which owns the same
file's HOME: the builder address, the moved projection, `SEC_CACHE_DEFAULT`'s removal) and disjoint from chain F
(`fetch.py`/`batch.py`, which READ the CIK this function writes, :377-388) and from `AMGT-rk-31`
(`crosswalk.py`); the EDGAR submissions measurement (`form_expected`) is F1's and is explicitly not moved.
**GRAIN:** every criterion reads the document the function actually receives (`load_sec_cache()`'s return, its
`row_denominator` and `object`) and the note it emits, on the three validation names by direct call; the
denominator claim is discriminated by a 3-row fixture (AC5), never by re-reading the same number. **INTENT:** one
axis -- step 1 joins against the LIVE table and, on a miss, reports the table it read. **STATE:** moves the loader's
`rows` from a 33-root projection to the full delivery (10,4xx rows) and the miss note's numbers to measured ones;
lands one dated bronze object per UTC day; does NOT move the name guard (:509-517), the US join (:527), the
`submissions` source (rk-33's carried block, :518-520), `universe/v1` (no `--write-pool`), or any served object.
- *Raw before derived* (PRD v0.13 :899): `fetch_sec_ticker_table()` GETs `company_tickers.json` ONCE with the
  instrument at `sec_ticker_cik_cache.json:3` and lands the bytes byte-for-byte at
  `sec_table_address(date_utc, "company_tickers.json")` (rk-33's builder plumbing; `crosswalk.write_pool()`
  discipline :609-657) under `--refresh-sec-table`; put-if-absent makes it ONE GET per UTC day (AC2, run twice);
  `--dry-run` (:854-860) never fetches and refuses loudly on an absent landing.
- *The loader returns the full table* in the SAME shape (`rows`, `ticker_to_cik_table`, `submissions`) plus
  `object`, so the fixture arms (`test_union_universe.py:30`, :163-195) pass unchanged; `row_denominator` is
  `len(rows)` AS READ, and AC3 prints rows_read == rows_in_document.
- *The guard stays, the miss becomes true:* CAT resolves (18230, validation :97), CSL is REFUSED COLLISION as
  Carlisle (790051, :108) by the unchanged guard, Keyence misses honestly with the note "(N rows, retrieved ...)
  carries no ticker '6861'" naming the object (:121); the D1 sentence "(10422 rows) carries no ticker 'CAT'"
  (:96) can no longer be emitted from a 33-row read.
- *A read is a read* (AC6): object counts under the bronze prefix and `universe/v1/` are equal around a load
  plus two lookups; the landing is an explicit mode, never a side effect.
- *Egress ceiling named:* one public SEC GET per day; no `data.sec.gov` (F1), no Bloomberg; the order carries
  the arm that waits on a per-use word if the COO asks for one, with AC3-AC7 still runnable on rk-33's object.

**`AMGT-rk-33` (R14-H1, S-W32-S4 / M1 / V7-D24; `C-PRODUCTION-HOME`) -- MECE:** three named instances in three
files, each moved by its OWN rule (config -> beside the producer; cached data -> the builder's pool address; a
read never writes), disjoint from `AMGT-rk-32` (which edits `filing_identity_for()`'s READ in the same file,
sequenced AFTER this order), from `AMGT-rk-31` (`crosswalk.py`), from chain M (`SECURITIES`, `HIST_END`, the
field lists in `model_block_pull.py`) and from chain P (`engine.py`, untouched: the read-only contract lands in
`universe.py` alone); the class's OTHER instances (the model-block half at `universe.py:68-72`/:417, the coverage
list's home at `build_universe.py:79-81` and `crosswalk.py:71-74`) are CENSUSED with a denominator (AC6), not
edited. **GRAIN:** every criterion reads bytes at the new home against bytes at the old (sha256 both sides), the
builder's OWN output or refusal text (never a typed address), and a planted stale cache's mtime/sha before and
after a load; a literal census reads file:line, never a count alone. **INTENT:** one axis -- production code
reads no worker folder, and where the canon cannot yet place a dataset the refusal is RECORDED and ROUTED, never
answered by hand. **STATE:** moves `_FIELD_MAP_PATH` (worker ~1 -> `integrations/bloomberg/research/field_map.json`,
THE path `AMGT-rk-34` writes), the SEC document (worker ~19 -> `s3://opal-data-assets/sec/global/bronze/
company_tickers/date=2026-09-15/`), `load_sec_cache()`'s source, and `load_candidate_universe()`'s write
behaviour; adds ONE `systems.json` VENDOR row (`sec`) and re-marks two GENERATED files; does NOT move the
candidate universe's bytes (the builder refuses; a row), `filing_identity_for()`'s semantics (rk-32), the model
block pull's securities or dates (chain M), the peers engine, or any served object.
- *The builder is run FIRST and its answer recorded* (AC1, twice): `key()` refuses `sec` (opal_naming.py:1548-1549)
  until the VENDOR row exists -- the row the worker adds, validated by `python lib/opal_naming.py validate`
  (`10_ONBOARDING_CHECKLIST.md:90`) -- then `tiers.json:27` homes a COMPOSITE bronze in `opal-data-assets`;
  `address()` refuses `amgt` gold (:1562-1565 via `_home_bucket` :256-260) because `amgt` has no `scopes.json`
  row, and a scope row is Andrew's per-scope call (`02_DOCTRINE.md:589-591`; `opal-data-harvest` is registered
  nowhere, `05_IDENTITY_SPINE.md:77`) -- so that dataset lands as a ROW carrying the refusal verbatim, with the
  negative arm (an address in an existing bucket) written into the criterion.
- *The unit map is config* (PRD :1643-1650; `:855`): a byte-for-byte MOVE (36 fields, 3 securities), the reader
  `model_block_pull.py:286-288` repointed beside the producer; `AMGT-rk-34` rebuilds it for every name at that
  same path. The pull-log write (:464-467, :482-483) -- same file, same class -- goes to the existing raw landing
  family put-if-absent (:184-198), and the input ledger (:246) already records every pull.
- *The SEC document is a MOVE, not a rebuild:* landed with `crosswalk.write_pool()`'s discipline (:609-657, a
  bucket argument) at `sec_table_address("2026-09-15", "sec_ticker_cik_cache.json")`, dated by its own
  `retrieved_at` (:8); the loader reads the newest partition and refuses loudly on absence (no fallback to `~19`);
  the residue is NAMED -- the object is the delivery's 33-of-10,422 projection at bronze (R9), retired by rk-32's
  landing of the full delivery beside it, after which only `submissions` (:188-192) is read.
- *A read never writes* (D24; `universe.py:558-582`, :578-580 retired; `fetch_factor_metadata` :169-179 likewise):
  the planted negative is a copy of the cache with `preset_value_codes` removed under `AMGT_PEER_UNIVERSE_CACHE`
  -- before the fix its sha moves, after it does not (AC4, both recorded); the one writer is `main --refresh`
  (:661-689) with read-back; `engine.py:1453`/:1249 become read-only by contract without an edit.
- *Interface for rk-32, names exact:* `sec_table_address(partition_date, object_name)`, `sec_table_prefix()`,
  `load_sec_cache(path=None)` returning the existing shape plus `ticker_to_cik_table.object`;
  `SEC_CACHE_DEFAULT` removed; `AMGT_SEC_CACHE_PATH` and `--sec-cache-path` kept for tests.
- *Cost and non-application:* no vendor call, no sec.gov GET (rk-32's), no producer run; the two GENERATED
  naming-module files are regenerated (marks only, `TARGET_REGISTRY_KEYS` :97-108) and a diff beyond the mark
  line STOPs with a row; a commit-gate refusal on the registry path (lane PLATFORM_LOGIC_DOCS) is a row, never a
  forced commit.

**`AMGT-rk-34` (R14-M1, FWD-10) -- MECE:** two disjoint surfaces -- a production builder plus the producer's map READER
(`integrations/bloomberg/research/`), and the pool's `derived/model_block/` prefix -- neither overlapping a sibling's
grant: rk-33 owns the map's HOME (this cell discovers it and builds into it), rk-35/36/37 own the same producer file
but are sequenced behind this cell, and nothing under `lib/` moves (the two placeholder literals the check face,
validator and print renderer key on are preserved, so no Lambda-packaged byte changes and no redeploy is needed).
**GRAIN:** every criterion asserts the SERVED figure set -- the newest pool block per key graded by the SAME
`check_block` the Lambda runs (AC1, pool plane over 33) and the deployed adapter's own `/thesis` answer (AC3, three
covered names including a slash key) -- never a file count or a self-report; the population is the crosswalk's
MEASURED records read at run time, denominator printed. **INTENT:** one axis -- a figure carries a MEASURED unit or
it is REFUSED with its reason; a unit is never inferred to clear a refusal, and a name with no entry still refuses.
**STATE:** moves the served units of the 33 keyed names (a NEW stamp per key, the pre-act stamp list recorded as the
rollback target); does NOT move the Lambda's bytes, the crosswalk, the raw landings, `derived/model_block_fye/`, the
history window (rk-35) or any forecast (rk-36); does NOT pull anything.
- *Root cause and mechanism:* `_FIELD_MAP_PATH` (`model_block_pull.py:286-288`) reads `deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json`
  (3 pilots); `_resolved_unit` (`:302-318`) falls back to the pointer text at `:318`; `run_checks.py:54-55` maps that
  text to `NOT-YET-BUILT` and `figure.py:104-105` REFUSES it -- 348 refusals over 4 fields, measured (Model brief s.1.1).
- *Builder:* `build_unit_map.py` beside the producer, carrying `build_field_map.py`'s classification method (`:135-207`,
  `:233-309`) with the producer's bucket (`:44`, not `build_field_map.py:29`'s `opal-data-research`), a run-time
  population (`--securities` or `--population crosswalk`), per-entry `raw_stamp`/`derived_by`/`unit_status`, additive
  merge, an explicit `UNRESOLVED: no raw landed` terminal state, and a `--dry-run` that writes nothing.
- *Reader:* `_field_map`/`_resolved_unit`/`_resolved_sign`/`_currency_caveat` read rk-33's home; a present-but-UNRESOLVED
  entry returns a text that keeps the literals `SEE field_map.json` and `not yet built`, so `run_checks.py:54`,
  `provenance/validate.py:23` and `provenance/render_print.py:83` keep refusing and marking with zero change.
- *Act:* eleven `derive` invocations of at most three names (the `:509-510` cap is not lifted) over raw already landed
  (`stage_derive` reads S3 back at `:374-376`); each mints a new stamp (`:452-454`), which the adapter serves next
  (`scoped_amgt.py:1013-1017`). One writer of `derived/model_block/` (`:453-454`; `derive_fye_fixed.py:119` is a
  separate store) and four readers, censused at spawn for the never-widen pair; change-management entry opened first.
- *Criteria:* AC1 pool-plane census pre/post (348 -> 0 NOT-YET-BUILT over 33 of 33, residue listed by reason); AC2 the
  home outside `org/missions/`, 33 of 33 securities with a per-security entry for every producer mnemonic, and the
  planted no-entry name still mapping to NOT-YET-BUILT; AC3 the deployed adapter on BA, HD and `BP%2F_LN_Equity` with
  0 NOT-YET-BUILT and the Lambda's CodeSha256 unchanged; AC4 the three validation names on a dry run that prints a
  terminal state per name and changes no byte anywhere.

**`AMGT-rk-35` (R14-M2, FWD-1/FWD-16) -- MECE:** one surface, the producer's PULL WINDOW and DERIVE CLOSURE RULE
(`integrations/bloomberg/research/model_block_pull.py`), sequenced first in slot `~39`'s queue and after slot `~38`'s
`AMGT-rk-34` (whose builder it exercises); the adapter is untouched (`read_model` already serves `fiscal_years` from
the block, `scoped_amgt.py:2529`), the crosswalk is untouched, and the 33 covered names are neither pulled nor
re-derived. **GRAIN:** every criterion reads the LANDED block in the pool for the three validation names (never the
pull's in-memory result, C-RAW-BEFORE-DERIVED) and asserts the fiscal-year SET and a FY2026 statement VALUE, with a
count-in-equals-count-out check over `unresolved`; the dry run is graded by S3 object counts and `git status` before
versus after. **INTENT:** one axis -- the history ends at the issuer's latest CLOSED fiscal year, never a typed date,
and a group Bloomberg returns before the filing is excluded WITH its reason. **STATE:** lands three UNSERVED keys
(CAT, CSL, Keyence -- absent from the crosswalk) and their unit-map entries; moves nothing served (AC4 is the negative
control), no Lambda, no schedule, no forecast (rk-36), no new field (rk-37).
- *Defect at source:* `HIST_END = "2025-12-31"` (`:101`) requested at `:227-229`; every group emitted as a fiscal year
  (`:413-437`, `:443-444`); validation D4 (@`b527b93214` :183-184) measured FY2026 missing on CSL (June FYE) and
  Keyence (March FYE). Companion defects: `SECURITIES` as the default population (`:53`, `:507`, D5) and the pull log
  written into worker `~1`'s folder (`:464-467`, a C-PRODUCTION-HOME instance).
- *Rule:* request `[HIST_START, <pull date UTC>]`; a merged group is CLOSED when it carries a reported `SALES_REV_TURN`
  or `IS_EPS`; only closed groups become `fiscal_years`; excluded groups go to `unresolved` with the not-closed
  reason; the block carries `history_window{start, end_requested, latest_closed_fiscal_year, rule}`.
- *Population and dry run:* `--securities` required (no hand list, no crosswalk sweep added), the `:509-510` cap kept;
  `--dry-run` on both stages prints every request and key and writes nothing (S3, ledger, pull log, map).
- *Units at instantiation:* the derive builds a new security's map entries through `build_unit_map.py` (rk-34) when
  absent, never overwriting a MEASURED entry, so the validation blocks carry no NOT-YET-BUILT refusal (AC3).
- *Criteria:* AC1 the dry run (end_date = today, no 2025-12-31, zero writes, the `~1` literal gone from the source);
  AC2 the landed window on the three names (CSL/Keyence show FY2026 with a statement figure; CAT ends 2025 with any
  2026 group under `unresolved`); AC3 the check face on the three blocks with 0 NOT-YET-BUILT; AC4 33 of 33 covered
  names with the served stamp and newest raw key unchanged against the spawn-time baseline.

**`AMGT-rk-36` (R14-M3, FWD-1/FWD-16) -- MECE:** three disjoint surfaces, none overlapping a sibling's grant -- the
PRODUCER (`model_block_pull.py` forecast pull + derive, the new `sa_forecast_fallback.py`, the builder's `BEST_`
families), the SCOPE CONTRACT (`scopes.py` + its test, which parse each other), and the ADAPTER (`read_model` in
`scoped_amgt.py`, one Lambda redeploy) -- sequenced second in slot `~39`'s queue; the page (CONSENSUS label, forecast
columns) is explicitly NOT here and is named for a portal cell; the Base case is rk-37's. **GRAIN:** every criterion
asserts a real VALUE on the landed artifact or the deployed plane -- the raw `bestdata.json` with its recorded
overrides and the day-gaps between period end dates (AC1, the quarter-trap discriminator), the derived cells' fields
and the 15-cell accounting (AC2), the fallback's per-name terminal state with its landed raw and the entity test's
ROG control (AC3), five planted fixtures offline (AC4), and the deployed `/thesis` answer for BA plus a hollow key
(AC5) -- never a route existing or a self-report. **INTENT:** one axis -- a forecast cell carries its fiscal year
(from Bloomberg's own period end date), its source and its consensus basis, or it is ABSENT with the reason the
fallback recorded; a fill from an untested identity is never a value. **STATE:** lands forecasts for the three
UNSERVED validation names; moves the `/thesis` SHAPE for the 33 (four new `model.forecast_*` keys, empty with a reason)
and NO value for them; does not touch history figures, units already measured, the crosswalk, or any schedule; the
Lambda's role, layers, memory, timeout and environment are unchanged.
- *Pull:* three `reference_data([sec], FORECAST_FIELDS + ["BEST_PERIOD_END_DATE"], overrides={"BEST_FPERIOD_OVERRIDE": fp})`
  (`blp_client.py:135-163`), landed untouched as `bestdata.json` in the pull's stamp beside `refdata.json` /
  `histdata.json` (`model_block_pull.py:242-245`); the trap (brief s.7) is that the same fields without the override
  return the next quarter.
- *Derive:* one `forecast`-scope figure per (period, field) with `fiscal_period`, `override`, `period_end_date`,
  `fiscal_year` (the end date's year), `source`, `estimate_basis: consensus`; a period with no end date yields no
  figure; three end dates fewer than 300 days apart refuse the whole set; every empty cell is an `unresolved` record
  with a `fallback_status`.
- *Fallback (LIFTED BY NAME, PRD :1108; TERMS CLEARED, :1109):* candidates (crosswalk `sa_symbol` if R14-P1 landed
  one, else the Bloomberg root; a numeric root is no candidate) -> `GET /api/v3/symbols/{cand}` and a folded-name
  entity test against the block's `NAME` (ROG/Roche refuses) -> `GET /api/v3/metrics` (Peers brief :67; measured
  fields `pe_nongaap_fy1..3` :90, the rest measured on CAT and recorded or `NOT-MAPPABLE`) landed via `land_raw`
  (`rest_fetch.py:211-218`) -> fill only gaps with `meaningful` true, `source: SA_FALLBACK`, `sa_field`; `REHARVEST`
  stops the fallback and files a row. GET only, parked session only, never a sign-in.
- *Adapter and deploy:* `read_model` serves `forecast_figures` / `forecast_periods` / `forecast_source_counts` /
  `forecast_reason`; `check_face` includes forecasts. The redeploy is co-signed with the pre-act CodeSha256 and
  artifact VersionId as rollback, a 13-route census pre/post, and a MANDATORY stale-bytes check against `SITEZ`
  before the build (a worktree behind the shared branch reverts another cell's deploy -- STOP and row, never merge).
- *Criteria:* AC1 raw landing with explicit overrides and annual spacing; AC2 derived cells well-formed, 15 accounted,
  `unknown_scopes()` empty; AC3 the fallback's honest terminal state per name with landed raw and the ROG control;
  AC4 pytest over the five planted fixtures plus the scope contract; AC5 the deployed plane for BA (keys present,
  figures unmoved, reason named) and the hollow key (no fabricated forecast).

**`AMGT-rk-37` (R14-M4, FWD-1/FWD-16; C-MODEL-WINDOW-AND-ROWS (2) and (5); C-DESCRIPTION-LINE) -- MECE:** two
disjoint surfaces -- the PRODUCER (`model_block_pull.py`: two header fields, the adopted row fields, `cases.base` at
derive; the builder's families) and the ADAPTER (`scoped_amgt.py`: the description reader with the test, `_model_cases`)
with its tests and one Lambda redeploy -- last in slot `~39`'s queue; the page's five `mnemonic: null` rows and the
cases render are portal (frozen) and explicitly NOT here. **GRAIN:** every criterion asserts a real VALUE -- the raw
shape and the derived header text on the three validation names with the probe's refusal messages (AC1), planted
sentences and a planted upside number offline (AC2), an INDEPENDENT recomputation of the Base case from the block's own
figures against the served value (AC3), and the deployed plane for the PRD's two measured negatives plus a hollow key
(AC4). **INTENT:** one axis -- a row is a pulled Bloomberg field or it stays ABSENT; a description is Bloomberg's field,
else a sentence that PASSES a stated test, else ABSENT naming every probe; the Base case is the ruled formula with each
input's source and window, and no seat chooses a spread. **STATE:** moves the served `description` for the 12 drafted
names (their segment sentences fail the test -> ABSENT naming probes) and the `model.cases` shape and reason for all
33; does NOT move any figure, unit, history window or forecast of the 33 (not re-derived); lands the three validation
names unserved; the Lambda's configuration is unchanged.
- *Rows:* candidates probed on CAT in ONE `reference_data` call (`blp_client.py:135-228`; refusals under
  `__field_errors__` `:201-221`); an adopted mnemonic joins `HIST_FIELDS` (`:78-98`) with basis text and a builder
  family; a row with no served field stays ABSENT and is reported with every refusal; nothing is derived from other
  rows (Model brief s.7; `modelSheet.ts:13-14`). The only pre-measured candidate is `FREE_CASH_FLOW_YIELD`
  (`peers_v.py:74-76` per the intake).
- *Description:* `CIE_DES` / `CIE_DES_BULK` in `HEADER_FIELDS` (`:57-73`), the bulk shape measured on CAT's raw before
  the reader is built (PRD :1190-1191), joined text persisted as the header value; `DESCRIPTION_HEADER_MNEMONICS`
  (`scoped_amgt.py:2261`) in the PRD's order; `read_description` (`:2538-2605`) gains the describes-the-business test
  (three sub-rules: no amount/year token; a business-descriptor phrase; no measure phrase), `describes_business_test`
  and `probes` on the served object; the three measured negatives (Boeing, Home Depot, CAT) are planted fails.
- *Base case:* `cases.base` on the block at derive = `BEST_EPS` FY1 (rk-36's cell, source carried) x the median of the
  block's closed-year `PE_RATIO` values (window and `n` carried, no floor invented); `px_last` carried as context, no
  return derived; `_model_cases` (`:2500-2508`) serves the block's base and ALWAYS serves upside/downside ABSENT with
  the exact ruling reason (a planted upside number is never passed through).
- *Deploy:* co-signed with the pre-act CodeSha256 and artifact VersionId as rollback, the 13-route census pre/post,
  the 12 drafted names' description status pre/post as the measured blast radius, and the mandatory stale-bytes check
  against `SITEZ` before the build.
- *Criteria:* AC1 fields measured on the three names (description scalar present, raw shape printed, adopted rows
  with values, refused rows with messages); AC2 pytest over the planted sentences and the planted upside; AC3 in-process
  reads by key with the Base case recomputed on a second instrument and the exact ABSENT reasons; AC4 the deployed
  plane on BA, HD and a hollow key (no segment sentence served, no case number served, check face unmoved).

**`AMGT-rk-38` (R14-F1, FWD-18; T1, T8, T10, T15) -- MECE:** one new module (`battery.py`) plus the source-object
contract in `fetch.py` (`build_source_object` `:377-448`, `unresolved_source_object` `:359-374`, `latest_filing`
`:177-215`, `pool_key` `:451-452`); the cutter, the family detector and the language detector are `AMGT-rk-39`'s
(`document.py`), the live step 1 inside `build_universe.py:503-508` is chain I's (R14-I2), the batch and the analyzer are
`AMGT-rk-42`'s and `AMGT-rk-40`'s -- no region is shared with a sibling except `PARSER_VERSION`, which the later of
rk-39/rk-38 bumps. **GRAIN:** every criterion reads a battery RUN's recorded attempts on a real validation name or a
planted control, never a code census; AC7 reads the POOL object the downstream cell (`AMGT-rk-49`) will read. **INTENT:**
one axis -- a document is served only after it passed the entity, currency and family tests at the step that found it,
and every step tried is on the object. **STATE:** does not move the EDGAR-by-CIK path (`--cik --form` keeps working),
does not move the crosswalk, the universe row, `batch.py` or `analyze.py`; adds `battery`, `family`, `language`,
`entity_evidence`, `verified_site` to the source object and bumps `PARSER_VERSION` to 2.0.0 because that contract moved.
- *The ratified order* (PRD v0.13 @1699960261 `:668-673`): US (1) EDGAR (2) EDGAR by Bloomberg CIK (3) the IR page;
  international (1) EDGAR by ticker (2) EDGAR by Bloomberg CIK (3) ESEF/UKSEF by LEI (4) the company's site (5) the
  national regulator, one adapter per jurisdiction built only for a name step 4 fails; terminal UNRESOLVED-SOURCE with
  every attempt. Step 5 is DECLARED with an empty adapter registry and records `no adapter for jurisdiction <cc>`.
- *Step 1 is LIVE* (`:682-683`): the SEC ticker table's row count printed, the name guard on every listing; measured
  in the validation, CAT resolves and CSL (Carlisle) is refused on the live table where the estate cache missed both.
- *The acceptance test* (`:674-681`): (a) full legal name on the cover after a declared normalisation, LEI equality when
  the document carries one, a legal-form contradiction or subsidiary token FAILS; (b) period end within 18 months
  (EDGAR `reportDate`; PDF `document.period_end`); (c) `document.detect_family` + `document.cut` return a declared family
  with an item cut OK, else FAIL (c) with reason -- never a section (D9).
- *Step 4's seeds are entity-tied*: Bloomberg's `COMPANY_WEB_ADDRESS` (a hint -- a subsidiary or branch for 3 of 22,
  and NOT the report host for CSL), plus EDGAR's `website`/`investorWebsite` for any CIK a prior step tied to the entity;
  the crawl is bounded and printed (40 pages, depth 3, 25 MB per candidate) and `search_fn` stays an unwired seam --
  no search primitive is authorized (E14 measured the SERP primitive returning `[]` on failure).
- *`verified_site` is the contract AMGT-rk-49 reads*: a host tied to the winning document or to EDGAR's own record
  for the winning CIK, never Bloomberg's raw address; null carries `verified_site_reason`.
- *Discrimination*: AC5 (no keys, no seeds) terminates with one attempt per declared step; AC6 flips CAT's live outcome
  by changing ONLY the legal name (Roche Holdings, Inc.) -- the same 10-K found at steps 1 and 2 fails (a) twice.
- *Pool writes*: `filings/v1/<validation key>/` through `crosswalk.write_pool` (`:609-657`, put + read-back), three
  keys the pool crosswalk does not carry, so no served output moves; no never-widen pair is drafted.

**`AMGT-rk-39` (R14-F2, FWD-18; V3, E10) -- MECE:** one new module (`document.py`: reflow, family, language, period
end, the family-keyed cutter) and the cutter's call sites in `fetch.py` (`SECTION_PATTERNS` `:103-152` moved out,
`extract_sections` `:329-350`, the officer-section write `:411`/`:440-447`, the no-item message `:397-407`); the battery
that CONSUMES test (c) is `AMGT-rk-38`'s, the Unicode passages and translation that consume `detect_language` are
`AMGT-rk-40`'s, the roster that parses the officer section by family is chain E's -- no region is shared except
`PARSER_VERSION`. **GRAIN:** every criterion reads a CUT's status and character count on the two real step-4 documents
(CSL, Keyence -- by URL and content hash) or on a planted fixture, never a pattern census; AC4 runs the SAME text under
two families so the D9 wrong object and its remedy are one measurement. **INTENT:** one axis -- a section is served only
when a qualified heading of a KNOWN family bounded it, and every miss says why. **STATE:** does not move the 10-K rules
(TheSectionDiscriminator's assertions stand), the pool, the batch, the analyzer or the passage map; changes the 20-F risk
patterns by removing ONE bare fallback; adds `status`/`reason` per cut key and a FAILED officer-section shape; bumps
`PARSER_VERSION` to 1.1.0.
- *Reflow* (D12): PyMuPDF `page.get_text("blocks")` joined CJK-aware with hyphen repair -- the validation's own method,
  which moved passage coverage 9.3% -> 91.6% (CSL) and 1.8% -> 92.4% (Keyence); AC2/AC3 re-measure both shares on the
  same `passages.build_passage_map` metric with the denominator printed.
- *Family before cut* (PRD `:676-681`, D9): `FAMILIES = (10-K, 20-F, ANNUAL-REPORT, YUHO)`; UNKNOWN fails (c) and is
  never cut; ESEF is not declared because no validation name exercises a held ESEF filing.
- *D9 removed*: the bare `r"riskfactors"` at `fetch.py:128` goes; with `:316-322`'s unbounded fallback it cut 70,000
  characters of a patient story from CSL's report under 20-F rules. AC4 shows chars 0 / FAILED under 20-F and an OK
  risk section under ANNUAL-REPORT on the identical text.
- *E10 -- an empty cut is a FAILED cut*: `officer_section.status FAILED` with the patterns tried and why each was
  disqualified, replacing `text: ""`, `extracted: False` (`:440-447`); ASML/PBR are the served instances and are NOT
  re-fetched (no re-run of the 33) -- the fixture mirrors them.
- *Language recorded, not tested* (`C-FILINGS-TRANSLATION` `:707-708`): a script-share detector with its shares on the
  object, so a wrong detection is visible; no language library exists on the device and none is installed.
- *Dry by construction*: the CLI writes only under `.scratch/`; no pool write exists on it (`C-PRODUCTION-HOME`
  `:1646-1647`). Non-ASCII headings are `\u` escapes verified against the document at the run.

**`AMGT-rk-40` (R14-F3, FWD-18; T13, V4) -- MECE:** the three preconditions of `C-FILINGS-TRANSLATION` and the
stage itself, each in its own place -- (i) Unicode passages in `passages.py` (`to_ascii` `:67-79` and its five
`analyze.py` call sites removed), (ii) pre-cut citation blocks in `analyze.py` `pass_1` `:277-302` / `resolve_pass_1`
`:375-437`, (iii) the character rule in `drafting_build.py:85-128` and `verbatim.py:42-50`, and the stage in a new
`translate.py`; the family cut and language detector are `AMGT-rk-39`'s, the HOLD and the split counts are
`AMGT-rk-41`'s, the writer and `main()` are `AMGT-rk-42`'s. **GRAIN:** every criterion reads a MEASURED count on the
real Keyence Yuho (passages kept, blocks per citation, runs inside the cited passage, controls refused, translations
that relocate), never a code census; the negative arm is an English document that makes NO translation call. **INTENT:**
one axis -- every cited span re-locates verbatim in the ORIGINAL filing, and the English shown beside it is labelled a
translation. **STATE:** does not move the two-pass shape, the typed row set, the pool path, the hold rule or the pool's
ASCII bytes (`crosswalk.serialise` `:439-441` is `ensure_ascii=True` and stays the one escape point); moves the
`PROMPT_VERSION` (`rj6-two-pass/2`, invalidating plain-text pass-1 caches) and the analyzer version with its contract.
- *Design A, not B* (PRD `:704-706`): the original is analyzed; translating the passages first is refused because a
  mistranslation would then be invisible to the gate. Measured on Keyence: 70 of 71 findings with a 12+ character run
  inside their one cited passage; neighbour and one-character-mutation controls refused 70/70 and 68/68; 0 of 71
  translations relocate; USD 0.32 for the name.
- *(i)*: `build_passage_map` stores NFC text with a `non_ascii_chars` count; today 6.8% of Japanese survives and 7 of
  28 passages are empty (D13, D15).
- *(ii)*: one content-block document per analysis, one block per passage, for EVERY language (one path);
  `content_block_location` maps to passage ids and the cited text is still checked inside that passage (D16).
- *(iii)*: thresholds STATED, as `C-VERBATIM-GATE` `:916-917` requires -- 8 tokens for spaced scripts, 12 characters for
  unspaced (whitespace removed on both sides); `_QUOTED_RE` also reads corner brackets.
- *The contract for translated text* (PRD `:712-716`): `translated: true`, source language, translator model and
  prompt version, time, the original sentence and its passage ids beside it; English records `skipped: english` with no
  call; the gate runs on the original text against the original passage.
- *Cost and bar*: one live analysis and one translation on Keyence, cap USD 3.00; no pool write; no run on the 33.

**`AMGT-rk-41` (R14-F4, FWD-9/FWD-18; V6/D18; card 5 ANSWERED HOLD) -- MECE:** the gate's classing in
`lib/research/drafting/pipeline.py:122-144` (served-on-span / held-no-span / refused), the split denominators and the
rebuild CLI in `drafting_build.py:188-248`, the schema fields, and the served-plane act over `drafting/v1/`; the run
finder and Unicode spans are `AMGT-rk-40`'s (`drafting_build.py:70-128`, `verbatim.py`), the ONE writer is
`AMGT-rk-42`'s (`analyze.write_outputs`, called here, not edited), the adapter's own validator
(`scoped_amgt.py:1483-1514`) is chain B's and is named OUT of this cell. **GRAIN:** every criterion reads a
DOCUMENT's split or a SERVED bundle's sentences (the adapter's offline root, then the deployed Lambda), never a token
count; AC4 plants an unanchored sentence into a served copy so AC3's zero is a measurement. **INTENT:** one axis -- a
drafted sentence reaches a reader only on a verbatim span from the passage it cites; everything else is held and
counted. **STATE:** does not move `verbatim.normalise` or the REFUSE path; does not move the analyzer, the pool
`filings/v1/` objects, the crosswalk or the Lambda; moves the served `drafting/v1/` objects of the keys that carry an
analysis (12 at the cut) -- a never-widen pair and a change-management entry precede that act.
- *The rule* (PRD v0.13 @1699960261 `C-VERBATIM-GATE` `:910-918`): every pass count prints its split; a sentence with
  no span is HELD, never served (Andrew-direct ~19:4xZ *"Agreed, yes."*); it binds both writers; the neighbour-passage
  and one-character-mutation controls must refuse. No LABEL interim, no switch.
- *The hole* (D18): `verbatim.is_verbatim("")` is True (`:59-61`), `check_against_sources([])` is PASS (`:65-79`),
  `_gate_sentences` appends it (`:143`), `build_drafting_document` counts `verbatim_pass` unsplit (`:243`); CAT 17 of
  39 and CSL 16 of 40 pass with no span; 179 of 389 over the served 12.
- *The remedy stays in the library*: HELD-NO-SPAN is classed after validation and before serving, recorded with its
  reason on the document (`held_no_span`), and the split is a denominator block a reader can reject on.
- *The served act*: a deterministic gate re-apply over STORED analyses (no model call; the `AMGT-rk-19` producer-half
  precedent) over the crosswalk's MEASURED keys, never a store listing; pre-act sha256 per key from `head_object`,
  bytes saved, rollback = `write_pool` of those bytes; readers named (`scoped_amgt.py:1594`, `:2574-2592`,
  `posture/packs.py:107`); writers counted (N = 2 today, N = 1 after `AMGT-rk-42`).
- *s.3.8 placed*: the 11 stale objects are rebuilt for the GATE only, gaining no content; the COO strikes AC6/AC7 if
  s.3.8 is read as barring even that.
- *Discrimination*: AC4 (planted unanchored sentence -> rc 1) and AC7's before/after pair on the deployed adapter.

**`AMGT-rk-42` (R14-F5, FWD-18; T4-T7, E8, D27) -- MECE:** five defects of ONE object -- the batch's readiness --
each in its own region: the version and its fingerprint (`analyze.py:59-61`), the writer (`:1210-1230` ->
`write_outputs`), the default universe (`:1095-1097`, a worker folder with a typed date), the plan (`batch.py:82-116`
dedupe by CIK, D27 partitions), the launcher (`:119-130`, `run_batch.cmd:9`, and the LIVE disabled task); the passes and
the resolver are `AMGT-rk-40`'s, the gate is `AMGT-rk-41`'s (it CALLS the writer), the management task with the
identical registration defect is chain E's. **GRAIN:** every criterion reads a MEASURED state -- the fingerprint of the
fixture's shape, the literal-writer census with its file denominator, the dry run's denominators under invalid
credentials, the pool's vintage listing and version census, the task XML read back on both sides of the act -- never a
paraphrase of the code. **INTENT:** one axis -- when the batch is finally enabled on Andrew's word it does the right
thing on its first fire: skips nothing stale, fetches each issuer once, writes through one path, reads the newest
universe, and launches at all. **STATE:** does not move any pool object, any analysis, the drafting gate or the
passes; does not enable the task; moves `ANALYZER_VERSION` to 2.0.0 (the contract moved at rk-19 and the version did
not), the DISABLED task's registered command, and `run_batch.cmd`.
- *Order of operations* (PRD v0.13 @1699960261 `:689-690`): the version moves WITH the contract (a fingerprint test
  fails whenever the shape moves and the constants do not), THEN skip-on-unchanged (`--plan-only` prints
  SKIP-UNCHANGED / WOULD-RUN with reasons); AC6 shows 0 of the stored analyses carry the new version, so the skip
  locks nothing in.
- *One writer* (`C-VERBATIM-GATE` `:917-918` counts two): `write_outputs()` is the only function naming
  `drafting/v1/`; AC2 censuses the literal across every `.py` in the package with the denominator printed.
- *Newest vintage* (`C-PRODUCTION-HOME` `:1643-1650`): `universe/v1/<date>.json` is date-keyed
  (`build_universe.py:448`, `:861-862`); `newest` lists and orders; the typed `2026-09-15` and the worker-folder
  default are removed.
- *Dedupe by CIK*: one fetch and one analysis per issuer, outputs for every key sharing the CIK (ASML twice on the 16
  Sep universe).
- *The launcher* (T5/E8): the live task reads `Command C:\Users\Opal` -- measured by `schtasks /Query /XML` on
  2026-09-18; the fix re-registers from the exported XML with the quoted path and `Enabled false` preserved, read back
  on both sides; the management task is left to chain E.
- *Never run*: no `--write-pool`, no model call, no enable; the proof is tests, a dry run under invalid AWS
  credentials (a write would fail loudly), a read-only plan on the validation names, and read-only pool censuses.

**`AMGT-rk-43` (R14-E1, FWD-17; intake E1/E4/E11; W32-S2 folded) -- MECE:** two disjoint surfaces -- the adapter's
`read_management()` + `ceo_profile_reading()` (`scoped_amgt.py:2275-2371`) and the page's three render sites
(`ExecManagementTab.tsx:43-51`, `:70-93`, `:95-103` + `types.ts:680-715`); no producer file, no pool prefix, no schema
file is touched, so it overlaps none of chain E's siblings (rk-44 batch.py, rk-45 enrich.py compute_pool, rk-46
roster.py) except the ONE adapter file, which the COO sequences. The CEO readings are enumerated BY SUBTRACTION over the
M-1 `ceo_public_profile` object's own fields (`status`/`url`/`query`/`absence_class`/`basis`): CONFIRMED, NOT_SEARCHED,
SEARCHED_NOTHING_FOUND, SEARCHED_LINKS_UNREADABLE, SEARCH_FAILED, and UNREADABLE_OBJECT as the printed remainder -- a
sixth value so no object falls silently into a wrong one; the PRD's fifth page state (NOTHING KEPT) is named as
unreachable before R14-E6, not omitted. **GRAIN:** every criterion asserts a served VALUE (`management_status`,
`absent_because`, `ceo_profile_reading.reading`, the served `reason` text) against the object's own fields, on fixture
objects through the adapter's real `_LocalPoolClient` (AC2) and on the LIVE deployed plane (AC4); the page criterion
counts the six literal state tokens plus one PLANTED-ABSENT stale sentence, never a bare "changed". **INTENT:** one axis
-- a reason the page shows is the object's own reason, and a status means content (a roster with zero officers is
ABSENT with its reason, PRD v0.13 @`1699960261` `:731-732`). **STATE:** moves the served `management` block for the 12 objects (5
SERVED -> ABSENT/ZERO_OFFICERS, 7 CEO lines re-read); moves NOTHING for the 21 names with no object beyond the new
`absent_because: NO_OBJECT` field; does not move `roster_source` (R14-E5), the pool read at `:2343` (R14-E3), any officer
value, any other route, or any pool object -- no producer runs.
- *Adapter reading:* `ceo_profile_reading()` (`scoped_amgt.py:2275-2302`) stops parsing the basis sentence
  (`_SERP_URL_COUNT_RE` at `:2272` survives only to fill the informational `urls_returned`); `query is None` is the
  never-searched signal (`enrich.py:414-427` sets `query` only immediately before the SERP call), `absence_class`
  splits the searched arms, and the fixed producer prefix `"the SERP primitive raised"` (`enrich.py:432`) is the one
  string test kept -- the producer leaves the default NOTHING_FOUND in place on that path, so the field alone misreads it.
- *Adapter status:* `read_management()` (`:2305-2371`) classes `roster_status != RESOLVED or officers == []` as
  `management_status ABSENT`, `absent_because ZERO_OFFICERS`, `reason = roster_reason`, keeping the object's
  `roster_status`/`roster_reason`/`absence_reason_class`/`absence_reason_evidence`/`source_*` and `management_read` on
  the block; the no-object arm (`:2335-2342`) gains `absent_because NO_OBJECT`.
- *Page:* `CeoProfile` renders one line per reading with the object's `reason` (the hard-coded `:87` sentence is deleted
  and its count is a planted 0); `ManagementBody`'s non-SERVED branch prints `absent_because` + the roster fields and no
  table; `OfficerRow` reads `enrichment` (MATCHED / ABSENT / NOT-ATTEMPTED) and a SKIPPED `lusha_enrichment` prints its
  reason under the table (W32-S2: the seven un-enriched names read "no match" today).
- *Deploy:* served output moves -> CTO+COO never-widen pair naming the blast radius (the `/thesis` route's `management`
  key for 33 names; 12 objects render differently), writer count of the served property = 1 (this adapter), rollback =
  the live pre-act `source_code_hash`; ledger entry opened before the artifact upload (`.tools/deploy_ledger.py`, rk-19's
  precedent). The page commit is DEV-durability only.
- *Criteria:* AC1 the pre-act live count bar with its denominator; AC2 four fixture objects, three PLANTED (zero-officer
  SERVED today; raise-path NOTHING_FOUND today; never-searched CANNOT_SAY today) + one positive control; AC3 tsc -b plus
  the six tokens and the planted-absent sentence; AC4 the live plane after the redeploy on ASML (zero-officer), NU
  (never searched) and SAP (positive control) -- reads of already-served names, no re-run; AC5 judgment at L9 from a
  headed session (MFA, s.3.5).

**`AMGT-rk-44` (R14-E2, FWD-17; W32-S3; intake E6/E7/E8) -- MECE:** one producer package, three files
(`lib/research/management/batch.py`, `run_batch.cmd`, `tests/test_management.py`), no adapter, no portal, no pool
write, no schedule armed -- the one box act is correcting the ACTION of an existing DISABLED task, declared in the
preflight. The census partitions the population BY SUBTRACTION in one pass: population (the crosswalk's MEASURED
records, newest vintage) = real-filing + placeholder-only + no-object + unresolved-accession, the fourth printed so the
remainder is never silent; `would_build` is the first partition and nothing else. **GRAIN:** every criterion reads a
printed partition count with its denominator or a read-back of the box's own task action (`Get-ScheduledTask`
`Execute`/`Arguments`/`State`, the instrument that discriminates a split path from a wrapped console line), never an
rc. **INTENT:** one axis -- the batch can only ever build what carries a REAL filing, and it names every member of the
population it does not build. **STATE:** moves nothing served and nothing in the pool; moves the registered task's
action string only, with its enabled state read as Disabled before and after; does not move `enrich.py`'s pool
denominator read (`read_universe`, rk-45's), `roster.py`'s latest-accession pick (rk-46's), or the second driver
`management_posture_batch.py` (a stated residue).
- *Population* (`batch.py:66-73`, `:95`, `run_batch.cmd:12`): `crosswalk.load_crosswalk()` (`crosswalk.py:496-530`)
  resolves `crosswalk/v1/<latest>` from the pool and honours a local override; `--universe` retired, `--crosswalk`
  the QA override; the dry run prints the vintage it resolved (PRD v0.13 @`1699960261` s.10 `:1617-1618`).
- *Census* (`batch.py:76-86`): per-name prefix listing under `filings/v1/<key>/` (S3 resolves a slash inside the
  key), the class read from the key NAME (accession vs `UNRESOLVED-SOURCE.source.json`, `filings/batch.py:198`) and
  then from the latest accession object's `status`; no `.split("/")` survives (AC4 counts 0); a name cut from a full
  key is `key[len(prefix):].rsplit("/", 1)[0]`.
- *Content beside status* (`batch.py:193-195`): BATCH DONE prints RESOLVED-with-officers beside RESOLVED beside built
  (PRD v0.13 `:731-732`).
- *Launcher* (`batch.py:113-124`): `/TR "\"<launcher>\""` with escaped inner quotes, plus `change_action` and
  `read_back` strings; applied with `schtasks /Change /TR` so the enabled state is never touched; read back by
  `Get-ScheduledTask` (AC3, before and after). `run_batch.cmd` carries no typed date (AC4).
- *Planted cases* (AC1): the three validation names and the two slash names as literal keys on `_StubS3`
  (`tests/test_management.py:255-273`): CAT placeholder-only, CSL no-object, 6861 real, BP real (slash), NG
  placeholder (slash); 5 == 2 + 2 + 1 + 0. AC2 is the live dry run over the pool (a read): 33 = 12 + 21 + 0 + 0 at the
  cut, BP and NG named in the placeholder-only list where today they appear nowhere.

**`AMGT-rk-45` (R14-E3, FWD-17; intake E5/E5') -- MECE:** one computing function (`enrich.py:582-616`) that ALL THREE
`_pool` writers call (`enrich.main :689-690`, `batch.main :190-191`, `management_posture_batch.py :194-195` -- N = 3,
printed in the never-widen half), its universe read (`:569-579`), a `--pool-only` entry on `main()`, one schema field,
and ONE adapter line (`scoped_amgt.py:2343`) sequenced behind rk-43; no roster, no per-name object, no page. The pool's
membership is defined BY SUBTRACTION over the `management/v1/` listing: every key MINUS `_pool` MINUS every non-newest
object per name MINUS every newest object that is not RESOLVED-with-at-least-one-officer; the meta line prints each
subtraction's count (`objects_listed`, `names_seen`, `newest_per_name`, `names_with_roster`). **GRAIN:** every criterion
reads a pool VALUE with its denominator -- the live pre-act pool objects and the newest-per-name table (AC2), the dry
POOL line (AC3), the written object read back by sha256 (AC4), and the served `pool_read.object_key` +
`pool_denominator` on the deployed plane for a 15 Sep name and an 18 Sep name (AC5) -- never an rc and never a
"changed". **INTENT:** one axis -- there is ONE pool, over every current filing roster, at one date, and the page serves
that one (PRD v0.13 @`1699960261` `:752-753`; the docstring at `:583-588` already said so). **STATE:** moves ONE pool key
(`_pool/<today>.json`, overwritten from today's null object; rollback = the snapshotted pre-act bytes) and the pool line
of every served management block; moves no per-name object, no officer, no roster, no `_pool/2026-09-15.json` (an
object dated 15 Sep keeps 15 Sep's bytes -- the ADAPTER stops binding a name to its own date), nothing in `roster.py`
or `batch.py`.
- *Membership* (`enrich.py:589-594`): one listing; `name = key[len(prefix):].rsplit("/", 1)[0]` (a slash name is one
  name, W32-S3); newest per name by the ISO file segment; `_pool` dropped; RESOLVED and `officers >= 1` (PRD v0.13
  `:731-732`).
- *Tenure at the pool's date* (`:605-606` -> `roster.tenure_years(role_start, as_of)`, `roster.py:245-258`): the pool
  never averages figures measured at three different dates.
- *Denominator source* (`:569-579`): the NEWEST `universe/v1/` vintage when none matches the pool's `as_of`, named in
  the label and on the object as `universe_vintage` (`pool.schema.json` admits the one field); null only when no
  universe object exists at all.
- *The write* (`main :633-702`, `--pool-only [--write-pool]`): a DERIVED object over what already landed -- no
  `build_document`, no Lusha, no SERP, no re-run; AC3 dry, AC4 the one co-signed put with read-back
  (`crosswalk.write_pool :609-644`).
- *The served plane* (`scoped_amgt.py:2343`): `read_pool_object(MANAGEMENT_PREFIX, MANAGEMENT_POOL_NAME)` with no
  `as_of` = the newest pool (`:1155-1157`); AC5 plants `HOLLOW_NONEXISTENT_KEY_Equity` as the negative control (no
  object -> no pool line invented).
- *Planted tests* (AC1): same name at two dates (newest wins, once); zero-officer RESOLVED object (excluded); slash name
  (one name); two `_pool` objects (excluded); a stored `tenure_years` that disagrees with the recomputation (the
  recomputation wins); a universe at two vintages with none at the pool's date (newest read and named).

**`AMGT-rk-46` (R14-E4, FWD-17; V5 = D20/D21/D22; intake E2/E3) -- MECE:** one parser file (`roster.py`), its schema
(`management.schema.json`) and its tests + committed fixtures; no `enrich.py` (the absence classification stays
rk-22's rule, rk-45/E5/E6's file), no `batch.py`, no adapter, no page, no pool write. The parser's OUTCOMES are
enumerated by subtraction over every officer section it can be handed: RESOLVED by one of SIX declared shapes
(narrative-entry incl. the KMB variant, table-age, table-year, table-name-position-age, table-paren, table-yuho) MINUS
sections whose every row is a title (UNRESOLVED, "title, not a person") MINUS sections that point elsewhere
(UNRESOLVED, "INCORPORATES BY REFERENCE" + `section_refers_to`) MINUS empty sections (UNRESOLVED, unchanged) MINUS the
remainder ("no declared shape", still printed with its line and candidate counts). **GRAIN:** every criterion reads a
parsed VALUE -- an officer's `name`/`name_ascii`/`role`/`age`/`role_start`, a document's `parse_strategy`/
`section_refers_to`/`roster_reason` -- on committed fixtures reduced from the three validation names (AC1, AC3, AC4)
and on DRY in-process reads of six keyed names' persisted filings (AC2, before and after), never a token count.
**INTENT:** one axis -- a roster row is a PERSON read from the filing's own words, in the filing's own script, and a
section the parser cannot read says WHY and WHERE (PRD v0.13 @`1699960261` `:723`, `:733-734`). **STATE:** moves no
served object and no pool object (the rebuild of HAL/INTU/KMB/VLO is the post-validation run's, stated); ASML/PBR's
empty-cut outcome is the unchanged control (R14-F2's stage); the tenure rule, the pool, and `absence_reason_class`
(`enrich.py:165-195`) do not move.
- *D20* (`roster.py:97-99`, `:118-119`, `:178-190`): a name needs one token outside the title vocabulary and never ends
  in one; a wrapped name line pair is joined (VLO's `Harminder S.` / `"Homer" Bhullar`); an all-title section is
  UNRESOLVED so R14-E5's fallback applies. PLANTED: VLO's live "Senior Vice" officer; CSL's six.
- *Age column* (`:121`, `:291-295`): a role line ending in a bare 20-99 with no year is `age`, shape
  table-name-position-age. PLANTED: "R. Lane Riggs Chairman of the Board, Chief Executive Officer and President 60".
- *D21* (`:17-26`): table-paren, `NAME (NN) ROLE (YYYY)`, `role_start` YYYY as filing-since-column, from the CAT
  fixture (the validation's `s07b` re-cut, 17 usable lines, 0 candidates today).
- *KMB* (`:114-117`): the ` , NN, was elected ROLE in YEAR` / `has served as ROLE since DATE` entry regex; AC2's bar is
  >= 10 officers with age and role_start (0 today, 194 lines).
- *Incorporated by reference* (`:461-465`): HAL ("included under Part I on pages 7 and 8"), INTU (the Proxy), CAT's
  Item 10 (D10) -> `section_refers_to` carries the pointer sentence for the filings cutter; `roster_reason` names it.
- *D22* (`:157-171`, `:193-201`): fold punctuation and width only; `name` keeps the filing's characters, `name_ascii`
  carries the fold, logs print the fold or a `<non-ascii name, N chars>` marker; bytes stay ASCII through
  `crosswalk.serialise` (`crosswalk.py:439-441`, AC4 measures 0 non-ASCII bytes); table-yuho read from the Keyence
  fixture, bar 12 of 12 (the validation's scratch parse). Fixtures are `ensure_ascii=True` JSON under
  `tests/fixtures/`, beside the producer (`C-PRODUCTION-HOME` `:1643-1650`) -- the tests never read the scratch folder.
- *Reader* (`:496`): an accession key beats a placeholder key; PLANTED on `_StubS3` with both present.

**`AMGT-rk-47` (R14-E5, FWD-17) -- MECE:** one surface, the management PRODUCER (`lib/research/management/` plus one
census line in `management_posture_batch.py::cmd_report`), disjoint from the adapter (chain B) and the page (the
R14-E1 cell) that will label it, from the pool computation (the R14-E3 cell; this order's `--skip-pool` keeps
`_pool/` untouched) and from the roster parser (R14-E4; `build_roster` is not edited, its result is kept whole).
**GRAIN:** every criterion reads a VALUE on an object -- `roster_source`, the officer rows, the filing's own
`roster_reason` beside them, the Bloomberg `status` -- never a status count; the one count (AC4) prints its own
denominator and its split. **INTENT:** one axis -- when the filing gives no roster, Bloomberg fills the TABLE, labelled,
and never hides why the filing failed. **STATE:** does not move `roster_status` / `roster_reason` /
`absence_reason_class` (they class the FILING's absence exactly as before); does not move `avg_tenure_years` (null on a
fallback roster) or the pool (`compute_pool`'s `roster_status == RESOLVED` filter at `enrich.py:599` excludes fallback
rosters unchanged); does not run the batch (`filed_names` `:110-113` stays its ceiling); moves ONLY three new
`management/v1/<key>/<as_of>.json` objects and three raw landings.
- *Pull* (`lib/research/management/bloomberg_fallback.py`, new): one `ReferenceDataRequest` `[NAME, COMPANY_EXEC_OFFICERS]`
  through `integrations/bloomberg/mcp/blp_client.py::reference_data` (`:135`), loaded by path as
  `model_block_pull.py::_load_blp_client` (`:147-155`) does; the raw response landed at
  `raw/bloomberg/<key>/<stamp>/exec_officers.json` under the existing convention (`model_block_pull.py:5-11`,
  put-if-absent `:184-198`); entries split on the first two-space comma (brief `:204-207`), names verbatim after the
  package fold (`roster.py:157-171`); FAILED (field error, transport, unparseable) never EMPTY (zero entries).
- *Object* (`enrich.py::build_document` `:494-496`): the fallback fires only when `roster_status != RESOLVED`;
  `roster_source` FILING | BLOOMBERG_FALLBACK | null on every object (PRD `:727` @`1699960261`); fallback officers carry
  `source: "bloomberg"`, `role_start` null, `role_start_basis: "absent"`, `tenure_years` null, `enrichment
  NOT-ATTEMPTED`; a `fallback` block with the label text, status, counts, the raw key and the reason; the filing's
  `roster_status`/`roster_reason` stay on the object (PRD `:727`). Schema: `roster_source` REQUIRED, `officer.source`
  enum, `fallback` closed with the contact `not` clauses (`management.schema.json`).
- *Census* (`management_posture_batch.py::cmd_report` `:132-140`): one added line `MANAGEMENT CONTENT: FILING a
  BLOOMBERG_FALLBACK b zero-officer c of N` (PRD `:731-732`); nothing the batch RUNS changes.
- *Criteria:* (a) the planted RESOLVED filing leaves the fallback UNCALLED (counter 0); (b) the planted EMPTY and
  FAILED responses stay distinct; (c) the live pull on the three validation names (AC2 dry, AC3 written with
  `--skip-pool`, the pool object's ETag identical before and after); (d) the census split sums to its denominator.
- *Co-sign:* pool writes on a served prefix -- a never-widen pair naming exactly the three keys (pre-act ABSENT,
  printed) and three raw stamps, the three writers of `management/v1/` counted (`write_document`; the batch, not run;
  `batch.py`, disabled), rollback `delete_object` per key; the ledger entry opened before AC3.

**`AMGT-rk-48` (R14-E6, FWD-17) -- MECE:** two surfaces and no more -- the SERP primitive (`data/find/dualbiz/scripts/serp.py`,
one added classifier and one added records function; the existing `serp_brightdata` keeps its `list[str]` contract for
its two FIND_DUALBIZ callers) and the management producer (`ceo_search.py` new, the `enrich.py` call site, the schema,
the tests); disjoint from the adapter and the page (chain B and the R14-E1 cell, which serve and render the block),
from Lusha (`AMGT-rk-49`), and from the roster (`AMGT-rk-47`, whose `roster_source` this cell only READS into
`name_source`). Sequenced after `AMGT-rk-47` on one slot because both edit `build_document`. **GRAIN:** every
criterion asserts a VALUE -- a classified status on a measured byte shape, a re-located character range on a quote, a
refused mutant, `facts_verified` equal to `facts_proposed` minus `facts_dropped_unverified` -- never a url count read
off a prose `basis`; the vacuous case (zero facts) is printed as vacuous, never as a pass. **INTENT:** one axis -- a
result about the CEO is kept only when it is this person, at this company, in this role, and a fact is shown only as
the source's own words that re-locate verbatim; a failed search is never an empty one. **STATE:** does not move the
roster or `roster_source`; does not rename `ceo_public_profile` (kept as a PROJECTION so `read_management`
`scoped_amgt.py:2367-2368` and the R14-E1 reading keep working); does not change `serp_brightdata`'s return type;
does not run the batch; moves the three validation objects' `ceo_profile` and projected `ceo_public_profile` blocks
and nothing else on the served prefix.
- *Primitive FIRST* (`serp.py:245-286` beside; design s.3.1 `:285-320`): `classify_serp_attempt(http_status, headers,
  body)` -> FAILED (transport | HTTP >= 400 | `x-brd-status-code != 200` | `x-brd-error` | 0-byte | non-JSON, with
  `failure.kind`) / EMPTY (`organic == []` or `spelling.original_empty`) / OK; `serp_brightdata_records(...)` with
  `records[{rank, link, link_form, host, title, snippet, ...}]`, retry only captcha/5xx; `serp_brightdata` becomes the
  wrapper and prints `WARN:` on FAILED. Proven by the measured shapes (design s.1.5 `:112-119`) and a MUTANT classifier
  (captcha -> EMPTY) that the test REFUSES.
- *Agent* (`lib/research/management/ceo_search.py`; design s.3.2-3.4): query `"<name>" <company short> CEO` (the role
  term fixes the common-name case, 0 of 9 -> 9 of 9 measured); NOT_SEARCHED / SEARCH_FAILED / NOTHING_FOUND /
  UNREADABLE / CURATED with `reason_code`; triage call A (no memory); the deterministic anchor (surname and company
  token within 500 characters; 18/18 and 4/4 measured); extraction call B over surname windows; verification by
  `passages.Locator` (`:82-135`); `official_bio` only on the verified company domain; LinkedIn link-only; contact scrub
  everywhere; `name_source` FILING | BLOOMBERG_FALLBACK recorded for the L4's open point (PRD `:757` @`1699960261`).
- *Block and schema* (design s.3.3 `:388-407`): `ceo_profile` REQUIRED and closed; six fact topics, no `other`;
  `ceo_public_profile` derived (url / status / absence_class / basis) and its stale `:155-158` text corrected.
- *Criteria:* AC1-AC3 offline (the four shapes, the old-vs-new pair, the refused mutant, the namesake anchor, the
  verbatim mutants, the planted contact string; the classifier re-exercised through `enrich._serp_module()`; the schema
  enums); AC4-AC6 live on the three validation names only, one CEO per criterion under timeout 120, caps printed
  (9 SERP requests, 3 pages per name, US$2.00 model), read back through `get_object` + `validate()`.
- *Co-sign:* a REWRITE of the three keys `AMGT-rk-47` wrote -- a fresh never-widen pair naming them, pre-act
  `document-sha256` and `VersionId` printed, rollback by re-put of the pre-act version; a NEW ledger entry before AC4.
- *Placed, not resolved:* the per-use word for the validation run's Bright Data calls (PRD `:751`, `:1656`; the 17xxZ
  record `:44-45`) -- AC4-AC6 run only if the spawn prompt states it is on file, else refused with a row.

**`AMGT-rk-49` (R14-E7, FWD-17) -- MECE:** one surface, the enrichment step inside the management producer
(`enrich.py::domain_for` and the Lusha block, `management.schema.json::lusha_meta`, one `basis` line in `domains.json`,
a new test file), disjoint from the roster source (`AMGT-rk-47`), the CEO search (`AMGT-rk-48`), the battery that
lands the verified site (`AMGT-rk-38`, the gate), the batch census that still reads `domains.json` for a dry-run count
(the R14-E2 cell, `batch.py:97`), the adapter and the page. **GRAIN:** every criterion asserts a VALUE on the object --
`domain_source`, the derived domain and the rule that made it, `credits_used` as MEASURED `creditsCharged`
(`lusha_client.py:263-273`), per-officer `enrichment` consistent with the block's status -- never a hand-list
membership or a status count; the credit cost is printed as the denominator of every live call. **INTENT:** one axis
-- Lusha enriches a roster ONLY through the domain the battery verified as the right entity, and a name with no
verified domain is NOT ATTEMPTED with that reason, never guessed (PRD `:737-738` @`1699960261`). **STATE:** does not
move the roster, `roster_source`, `roster_status`, the `ceo_profile` block or the pool; does not re-pull Bloomberg or
re-bill the SERP (`--enrich-only` runs the Lusha step alone on the newest existing object); does not delete
`domains.json` (retired as a Lusha input, kept for the batch's census); keeps `CREDIT_BOUND_PER_NAME = 2` (the module's
design bound, not the card's ceiling); moves only the `lusha_enrichment` block and the officers' `profile_url` /
`lusha_title` / `enrichment` fields on the three validation objects.
- *Domain* (`enrich.py:138-146` re-sourced): `(company_domain, ir_domain, reason, basis)` from the filings source
  object's verified-site field as `AMGT-rk-38` names it (the object `build_document` already holds, `:493`; built at
  `fetch.py:425-448`); `company_domain` = the verified host minus ONE leading label from the declared allow-list
  (`www, ir, investors, investor, corporate`), never an eTLD+1 guess, the rule printed; no verified site (absent field,
  null, UNRESOLVED or absent object) => `(None, None, <reason naming the field and battery step 4>, domain_source null)`;
  Bloomberg's raw web address ignored by construction (brief `:92`, `:164-165`; PRD `:737`).
- *Block* (`enrich.py:497-505`; schema `:161-179`): `domain_source` (`battery-verified-site` | null), `verified_site`,
  `domain_rule`; SKIPPED keeps `absence_reason_class: pull-missed` (the battery not having verified a site is a pull
  gap, never a fact about the company); officers `NOT-ATTEMPTED` on SKIPPED (`:528-530`), `MATCHED | ABSENT` on CALLED;
  Bloomberg-fallback officers enrichable, the row's `source` naming which roster source confirmed them (PRD `:735-736`).
- *Entry* (`enrich.main`): `--enrich-only` loads the newest management object and the filings source, runs only the
  Lusha step, validates, writes back under the same `as_of` with `--write-pool --skip-pool`; `--dry-run` decides,
  prints, constructs no client, writes nothing (`C-PRODUCTION-HOME`, PRD `:1647`).
- *Criteria:* AC1 offline with the five planted negatives -- the hand-list name (`BA_US_Equity`) with no verified
  site stays SKIPPED, the planted `bloomberg_web_address` never becomes a domain, no site => client constructed 0
  times, no officers => SKIPPED with reason, a stubbed CALLED path records `credits_used 2` and scrubs a planted
  `email`; AC2 the dry run on the three validation names (client constructed 0 times, denominator 3 of 3); AC3 the
  ONE billable act, live Lusha on the names that carry a verified domain and officers, total credits printed; AC4 the
  read-back through `get_object` + `validate()` with the hand-list-fed count 0 as the discriminator.
- *Gate and organic negative:* fed only after `AMGT-rk-38` is terminal; at this cut CAT resolves at battery step 1
  (EDGAR, validation report `:86-96`) and so is expected NOT ATTEMPTED while CSL (`investors.csl.com`) and Keyence (the
  IR library) carry a step-4 site -- recorded as the rule working and as a row for the L4 (a US name never reaching
  step 4 has no enrichment under this rule), never widened here.
- *Served output:* the same three keys as `AMGT-rk-47`/`AMGT-rk-48`; the analysis marks the cell gated, not co-sign;
  the live write waits for the spawn prompt to say whether chain E's pair covers the rewrite or a fresh one is on file.

**`AMGT-rk-50` (R14-P1, FWD-8; Peers brief P1-P7) -- MECE:** one producer surface (`lib/research/peers/` plus one
registry row), disjoint from `AMGT-rk-51`'s `lib/research/scores/` and `AMGT-rk-52`'s `portal/`; the population is
exactly the three validation names MINUS none, printed as `3 of 3` terminal states, never the 33 (`C-VALIDATION-NAMES`,
PRD v0.13 @1699960261 `:1652-1658`). **GRAIN:** every criterion reads a real object -- the builder's own refusal text
and built address (AC2), the object counts before/after a dry run (AC3), the landed R-1 object's cells (AC6) -- never a
producer's self-report; the cell denominator is the 17 declared CSC columns times 6 rows = 102, printed. **INTENT:**
one axis -- the RIGHT company's peers, from Seeking Alpha, with every cell carrying its source; identity is tested
before the first peer call and again on every Bloomberg join (the same trap, one hop out). **STATE:** adds `sa` to
`engine.BASES` and supersedes the stale `sa_candidates()` note; moves NOTHING in the ranker's four rungs (FWD-19's
comparable still runs `engine.peers()`), touches no adapter (`read_peer_set` serves the object whole), and writes
three NEW pool keys only -- no existing `peers/v1` object is rewritten.
- *Identity first:* `sa_peers.entity_test()` is the CRO's measured rule ported verbatim (`org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py:92-135`
  -- accent-fold, `<b>`-strip, distinctive tokens, containment or jaccard >= 0.5), with the ROG-for-Roche control and the
  America Movil / Liberty Latin America false positive (`:112-125`) sealed as offline `unittest` cases (AC1) and the
  ROG control also printed live by every CLI invocation (AC3).
- *The four GETs through the existing module:* `rest_fetch.load_config` `:84-86`, `build_session` `:98-143`, `_do_get`
  `:153-204`, `detectors.classify` `:39-48`; `REHARVEST` raises `ReHarvestNeeded` `:70-71` and stops (rc 3, `:463-468`);
  the proxy refuses POST (`:30`) so every call is a GET; the search endpoint is the CRO's (`sa_symbol_resolve_pass.py:55-56`).
- *Raw before derivation at a builder address (Rule 30):* `lib/opal_naming.py address()` `:1558-1571`; measured refusal
  `scope 'amgt' resolves to no scopes.json row` -> one PRODUCT row in `infra/logic/registry/scopes.json` mirroring the
  `etfs` row (validate rules `:340-343`, `:358-359`), never `rest_fetch.land_raw()`'s hand-typed key (`:211-218`).
- *R-1 with a source on every cell:* `csc.CSC_COLUMNS` `:61-79` is the denominator; `Preferred` + `Minority` both map to
  SA's `other_cap_struct` (16 rendered columns cover 17 of 17 declared, stated in those words); `source` in
  {`SA`, `BBG`, `SA_FALLBACK:<field>`} or `None` with SA's reason (`meaningful: false` is never zero-filled); written by
  the ONE pool writer `engine.write_pool_object()` `:1138-1163` so `run_scores._latest_peer_set()` `:118-130` reads it.
- *The Bloomberg growth fill, name-checked:* one `blp_client.reference_data()` `:135-145` per subject over subject + 5
  peers as `<T> US Equity` with `NAME`; a NAME that fails `entity_test` against SA's company refuses that ticker's two
  BBG cells (fallback or ABSENT, `name_agreement: false`); `health()` `:125` first, never a sign-in.
- *A dry run writes nothing:* `plan` performs zero requests and zero puts, proven by object counts under all three
  prefixes read before and after (AC3), per `C-PRODUCTION-HOME` `:1646-1647`.

**`AMGT-rk-51` (R14-P2, FWD-8; slug row S162 parts (1) and (3)) -- MECE:** one producer package (`lib/research/scores/`)
plus its own test file, disjoint from `AMGT-rk-50`'s `lib/research/peers/` (imported, never edited) and `AMGT-rk-52`'s
`portal/`; the scored population is the three validation names MINUS none, and AC5 prints the complement -- `0 of 33`
covered names rewritten today -- so the fleet re-run Andrew barred is measured absent, not assumed. **GRAIN:** Peers V
asserts a real `classify.py` record (`state` / `value` / `absent_reason`) read back from the served store, never the
producer's return value; the planted negative (2 peers) and the floor pair (4 suppress / 5 compute) are graded on the
same function offline before any live call. **INTENT:** one axis -- the measure runs AS WRITTEN on its OWN Bloomberg
`FIELDS` over the set SA chose (SA says WHO, the fields say WHAT; PRD v0.13 @1699960261 `:648-650`), and every ABSENT
carries a sentence. **STATE:** moves the three floor constants and the record's key names; moves NOTHING in the six
measure functions (`peers_v.py:92-171`), the winsorization (`:189-208`) or the ranker; the `V`/`K`/`M`/`measures` keys
stay so every caller still reads them; writes three NEW `scores/v1` keys and rewrites none of the 33.
- *The one-field fix, at its lines:* `score_peers_v()` `:270-275` returns `"reason"`, never `absent_reason`; `:276-277`
  returns no `value`; `classify.absent()` `:39-47` / `measured()` `:32-36` are the shape `run_scores._peers_v_record()`
  `:177-185` stores verbatim and `read_scores()` serves verbatim (`scoped_amgt.py:2424-2430`).
- *The floors:* `MIN_PEERS_FOR_V` 8 -> 5, `MIN_PEERS_PER_MEASURE` 6 -> 5, `MIN_MEASURES_FOR_V` 3 (`:62-64`); the asserts
  `:69-70` re-cited to `C-PEERS-V-FLOORS` (`:643-650`) and never loosened below 5 / 5 / 3; the 5-peer suppression test
  (`test_score_modules.py:331-337`) moves to 4 peers so it cannot pass for the wrong reason.
- *The fields pull (new `peers_fields_pull.py`):* one `blp_client.reference_data()` `:135-145` per subject over
  `<sa_slug> US Equity` x 6 with `FIELDS` + `NAME` (`peers_v.py:74-85`) and the two overrides; raw landed at
  `address("bloomberg", <scope>, "bronze", "peers-v-fields", key, object=<stamp>.json)` BEFORE derivation (Rule 30);
  every row passes `sa_peers.entity_test(sa_company, NAME)` or is `ABSENT_PULL` with both names and excluded.
- *Scoping the runner:* `run_scores.main()` `:241-257` gains `--security-key` (repeatable); `run()` `:216-232` scores only
  those keys and never lists the crosswalk when given; a bare run stays as it was and is forbidden by BOUNDS.
- *Served output:* the three new `scores/v1` keys are the blast radius; ONE writer (`run_scores.py`), rollback = delete
  the three keys (pre-act state ABSENT, recorded by AC5's before-read); change-management entry before the first put.

**`AMGT-rk-52` (R14-P3, FWD-8; Peers brief item 6, rows P2/P3/P6) -- MECE:** one surface, `portal/src/pages/SecurityAnalysis/`
(three source files, one new harness, one captured fixture), disjoint from `AMGT-rk-50`'s producer and `AMGT-rk-51`'s
scores package; the adapter is excluded by construction because `read_peer_set()` serves the object whole
(`scoped_amgt.py:1276-1278`) and is the single-writer surface the COO sequences. **GRAIN:** every criterion reads the
component's OWN static markup over captured adapter bytes -- the fixture is the pool object `rk-50` landed, hashed --
and every count is read off the fixture (rendered columns, declared columns, cells, summary rows), never typed; the
two planted mutations (a not-meaningful cell, a fallback-sourced cell) are graded in the same render. **INTENT:** one
axis -- a value on the Peers page carries its claim: its source label, or `n/m` with SA's reason, and a summary row
never hides a mixed source (PRD v0.13 @1699960261 `:626-630`). **STATE:** adds a basis, a cell type and a render path
for `basis: "sa"`; moves NOTHING for the `derived` basis (the `MEMBER_FIELD_FOR_CODE` path stays and the five-name
`tabs.harness.cjs` is the regression arm); commits to DEV, which serves nothing, so the served plane does not move
until the PROD promote Andrew has deferred.
- *Types:* `types.ts:390` `PeerBasis` gains `'sa'`; `PeerCell {value, source, meaningful, reason, derivation, ...}`;
  `cells` on `PeerMember` (`:407-420`) and `PeerSubject` (`:452-458`); `sa_shape` on `CscColumnsMap` (`:442-450`).
- *Table:* `cscTable.ts` `buildCscTable()` `:86-161` -- a column is `PRESENT_CARRIED` when any row's `cells[column]`
  exists; `Preferred` + `Minority` render once as `Preferred + Minority` while `declared` still counts both (16 rendered
  covering 17 of 17 declared, in those words); summary rows (`:137-150`) gain a per-column source mix and exclude
  not-meaningful and absent cells from `n`.
- *Page:* `PeersTab.tsx` -- a `Seeking Alpha` badge beside `:59-66`'s two; `cellText()` `:39-44` becomes value + a
  `data-cell-source` label, or `n/m` with `title={reason}` for `meaningful: false` (never `0.00`); summary cells
  `:104-118` print `value (n=k; SA a / BBG b / SA_FALLBACK c)`; the band-valued `Panel variant="mixed"` keeps the white
  idiom legal here (portal `CLAUDE.md`).
- *Instrument:* `peersTab.harness.cjs` copies `tabs.harness.cjs` `:1-57`, `:127-132`, `:483-501` (installed `typescript`
  transpile, `react-dom/server`, stubbed hooks, `CHECKS-OK N of N` / exit code 1) over
  `peersFixture.CAT_US_Equity.json` captured from `peers/v1/CAT_US_Equity/<newest>.json` with its sha256, plus the two
  mutations and the `tabsFixture.BA_US_Equity.json` derived-basis regression; no browser, no HTTP, no file written.
- *Never `npx tsc`, never bare `tsc --noEmit`:* AC1 is `./node_modules/.bin/tsc -b --noEmit` with its rc read from
  `PIPESTATUS[0]` (the decoy and the empty-file-set traps, both banked).
- *Co-sign:* owed at the PROD promote, not at this DEV commit; stated in the order and carried by the COO.

**`AMGT-rk-53` (R14-L1, FWD-15; L2, L5, V8/D25) -- MECE:** four surfaces of ONE contract -- the pointer -- each in
its own region: the carrier (`chatter_axis.py:142-155,541-776` and its copy `price/generation.py:93-104,276-481`
collapse into ONE `generation_writer.py`), the CHATTER signal test (the product loop `chatter_axis.py:812-848`, where
`window_totals` `:807` becomes a filter instead of row detail), the PRICE `empty_reason` (`generation.py:489-594`,
whose exclusions already exist at `:516-530` and `movement_gate.py:412,452`), and the read side
(`scoped_amgt.py:404-417`, `:484-487`; `RankedList.tsx:179-186`; `types.ts:176-194`). The movement formulas and
`MIN_ABSOLUTE_JUMP` are `movement_gate.py`'s and the COO's card-B act; the `/security` router is `AMGT-rk-61`'s;
the deploy is the COO's. **GRAIN:** every criterion reads a MEASURED object at the level claimed -- a function
identity (`is`, 7 of 7 names), a hash discrimination (3 of 3 distinct), a `def` count per writer file (0 of the
former 1), a dry run's own SIGNAL lines (2 of 2 products, zero-signal rows 0), an in-process `handler()` response
against the live table -- never a paraphrase of the code and never a deployed-plane claim. **INTENT:** one axis --
a served list never contains a member the producer had no signal for, and an empty list says why, in the same
words on the pointer, the response and the page. **STATE:** does not move the live table, any prior generation,
`TOP_N`, `WINDOW_DAYS`, the score scale, the movement reasons, or either deployed function; moves both writers'
bytes, the adapter's two ranking functions, the page's EMPTY branch and its type, and REWRITES the test arm that
asserted the defect (`test_chatter_axis.py:355-407`).
- *One builder* (`C-SERVER-SIDE-RANKING` `:1157-1160`): the carrier moves whole into `lib/research/metrics/
  generation_writer.py`; both writers re-export, so `scoped_amgt.py:116`'s alias keeps resolving; AC3 proves the
  same function object from all three modules and 0 remaining `def build_pointer(` per writer.
- *Signal, per subject* (`:1152-1153`): CHATTER drops `window_totals[key] == 0` into `excluded` as
  `NO_SIGNAL_IN_WINDOW` before `normalize_scores` (`:815`); PRICE keeps the gate's own `INSUFFICIENT_OBSERVATIONS`
  / `NO_OBSERVATIONS` / `INSUFFICIENT_INTERIOR_SERIES_FOR_TRAILING_BASELINE` tests and only gains the reason on
  the pointer.
- *`empty_reason` is part of the pointer contract and of `payload_hash`*: `{reason, count, denominator}`; a
  `STATE_EMPTY` pointer refuses without it and a `STATE_COMPLETE` one refuses with it (AC1 arm c); the hash
  discriminates two reasons on the same empty row set (AC3).
- *Carried to the panel*: `generation_fields()` adds the field, `_ranking_reason()` appends it, AC4 serves it
  THROUGH `handler()` with a real event on a patched table; the page renders it in place of the fixed sentence.
- *Never a fleet run, never a deploy* (`C-VALIDATION-NAMES` `:1652-1658`; the issuer rule): AC5 is the producer's own
  `--dry-run` (rows_written=0 pointers_written=0), AC7 is `handler()` in-process against the LIVE table, read-only,
  printing the pre-act baseline (10 of 10 zero-signal rows at the cut) the COO's consolidated deploy will move.
- *Both zips already carry the new module*: `build_zip.py:186` packages the import closure and
  `build-and-upload-scoped-amgt.sh:139` seeds `lib/research/metrics/` whole -- the COO's deploy needs no build edit.

**`AMGT-rk-54` (R14-L2, FWD-4, FWD-11, FWD-16; Lead Panel L3, L4) -- MECE:** one question -- why the store covers 3
names -- split by SUBTRACTION over the crosswalk's 33 MEASURED records into four classes that partition the
population: `COVERED` (links under a crosswalk alias), `STORED-NOT-KEYED` (stored under a form the crosswalk does
not hold -- association), `JOBBED-NOTHING-STORED` (a job ran, nothing landed -- ingestion), `NEVER-JOBBED` (the
mechanism never ran for the name -- ingestion); five instruments, each on its own plane: the pool's association
layer (S3 listing), the read side's alias resolution (`crosswalk.py:588-595`, `pool_reader.py:267-330`), the
harvester's own ingestion ledger (`worker.py:21`, `progress.sqlite3`), the harvester's universe and switches
(`__main__.py:12-36`, `config.json`), and the record that joins them. The fix is the CTO's L4 (analysis s.7
`:225`); the harvest lane's mechanism and cadence are Andrew's (`C-ONE-STORE` `:546-547`). **GRAIN:** every count
is read from the object it claims -- the pool listing paginated whole with its object total, the crosswalk record's
own `association_keys`, the ledger's own tables with their row counts, the config's own values read back -- never
the intake's figures (3 names, 188 of 191, five no-key names), which are re-measured and printed beside what is
read. **INTENT:** one axis -- for each keyed name, the CTO can say whether an article was never fetched or was
fetched under a key the readers cannot see, with the code line that produces each. **STATE:** moves NOTHING -- no
pool object, no code, no config, no crosswalk, no harvester run, no vendor call; writes one record under the
worker's folder and surprise rows.
- *Association is by the job, never by content* (`worker.py:57,102,116` -> `catalog.py:74`): the link key carries
  the JOB's `security['key']`; the readers key on the crosswalk's `association_keys` (`pool_reader.py:209-231`); the
  two agree only where the crosswalk holds the harvester's form (`BA`, `COST`, `HD` for pilots; `security-<sha16>`
  otherwise, `crosswalk.py:178-198`).
- *Which names a job can ever run for* (`__main__.py:66`, `config.json`): five pilots by default, `jobs_per_run 1`,
  schedule and uploads OFF -- AC4 prints the universe's own split (pilot-keyed vs hash-keyed) and the switches
  verbatim.
- *The ingestion ledger is device-local* (`config.json` `runtime_root`, gitignored): AC3 opens the MAIN tree's file
  read-only by absolute path, printing size and mtime beside every count; ABSENT is printed, never inferred, and
  makes the ingestion axis UNMEASURED rather than a guess.
- *The population is the crosswalk's MEASURED records* (section 10 `:1617-1618`; analysis s.1): 33 rows, classes
  summing to 33 (AC5), CAT / CSL / Keyence classed by name.
- *A finding is a row, not a remedy*: `config.json` `universe_source` reads a worker's deliverables folder --
  `C-PRODUCTION-HOME`'s class (`:1643-1650`) -- and is filed as `AMGT_RESAPP-Z-W54-S<k>`, not edited.

**`AMGT-rk-55` (R14-T1; process; row S154) -- MECE:** one predicate on one key -- a NEWLY-ADDED tree order's
`<round>N</round>` against the rounds the project's orders at HEAD already carry -- in one limb of one gate
(`to-pipeline-gate.py` `main()` `:2712-2826` beside the coverage carrier), with its pure function, its read-only
census (`--rounds <CODE>`), its self-test arms (`:665-930`) and one real-index battery; WHO commits stays GATE
(iv)'s (`:225-239`), a MODIFY stays ungraded by construction (`_newly_added` `:1757-1782`), a merge stays exempt
(`:2718-2750`), and the escape stays the one audited override (`:2412-2434`); the `<status>` element is
`AMGT-rk-56`'s limb in the same function. **GRAIN:** the census reads HEAD blobs (`git ls-files` + `git show
HEAD:`), never the worktree, and the element line-anchored (the `PLACEHOLDERS_TAG_RE` `:165` discipline), so a
prose mention of `<round>` in a worker face is inert; the battery runs the gate's own CLI on real order bytes in a
scratch repo and the live control (AC4) stages a real round-13 order under a new name in the worker's own index.
**INTENT:** one axis -- a round has ONE issuance, and a second file into it is refused whoever commits it, which
is the case a serial-keyed limb could not see (S154: two continuations of `2.0.0_SA_COO~Z`). **STATE:** moves the
gate file and adds one battery; moves NO order at HEAD (the 3 unrounded legacy orders are not back-filled), no
law text, no spine text, no hook wiring; changes the COO's practice in one way, stated in the report: every
round is issued in ONE commit.
- *Keyed to the round, never the serial* (analysis s.3.1 `:67-70`): `head_rounds[N]` non-empty -> REFUSED naming
  the round, the count and the existing files; the battery's RED arm commits and stages under the SAME author.
- *The key must exist*: a newly-added tree order without a line-anchored `<round>` is refused naming the missing
  key (94 of 97 orders at HEAD already carry it; the 3 without are legacy, ungraded).
- *A re-cut into the first issuance is a MODIFY* (the CTO's remedy for a collision): never graded by this limb;
  the battery's GREEN arm stages the committed order as MODIFIED and reads no refusal.
- *The escape is the one that exists*: `# pipeline-override: <reason>`, audited to
  `org/to-pipeline-override-audit.log`; no second token is minted.
- *The read the COO runs before a cut*: `--rounds AMGT_RESAPP` prints rounds -> counts, unrounded, and the
  denominator `97 order(s) at HEAD` (the cut's figure; AC3 re-measures).

**`AMGT-rk-56` (R14-T2; process; row S153) -- MECE:** one predicate on one element -- a NEWLY-ADDED tree order
carries a LINE-ANCHORED `<status>WORD</status>` whose word is not terminal -- in one limb of one gate
(`to-pipeline-gate.py` `check_file()` `:2402-2505`, beside GATE (viii)), with its pure function, its read-only census
(`--status-census <CODE>`), its self-test arms (`:665`, list `:695`) and one real-index battery; the FLIP stays
`check_complete_flip`'s (`:2524-2560`, its own unanchored regex and its own scope), the readers downstream stay as
they are (`to-check.py:113-122`, `surprise-row-gate.py:1125-1165`, `owned-paths-validate.py:125-140`), a MODIFY is
never graded (`_newly_added` `:1757-1782`), and the `<round>` key is `AMGT-rk-55`'s sibling limb. **GRAIN:** the
element is read on its own line, so the backticked instruction every worker face carries (*"flip `<status>` to
`complete`"*) cannot open a match -- the class Z-S15 and to-check FIX C each paid for once; the battery runs the
gate's own CLI on real order bytes in a scratch repo, and the live control (AC4) stages a real order with its
status line stripped in the worker's own index. **INTENT:** one axis -- an order is born with the field its
worker will flip and every status reader keys on, so `??` and `<no status tag>` can only ever describe a legacy
order. **STATE:** moves the gate file and adds one battery; moves NO order at HEAD (the 3 untagged, terminal-by-
proof orders are not back-filled), no reader, no law text; a worker adding the element at close to a legacy order
stays admitted.
- *Refused on absence, naming the row* (S153 `one_line`): 15 of 15 round-13 orders born untagged, twice; the
  refusal text says what to write (`<status>pending</status>` in the record face).
- *Refused when born terminal*: the word is read against the UNION of `DONE_WORDS` (`:2507`) and the sibling
  gate's `TERMINAL_TO_WORDS` (`surprise-row-gate.py:152`), stated in the docstring, no third list minted.
- *A prose mention is inert*: the anchored regex (the `PLACEHOLDERS_TAG_RE` `:165` discipline) is proven by a
  self-test arm and a battery arm whose face carries only the backticked instruction.
- *Prospective only*: NEWLY-ADDED tree orders; a MODIFY that ADDS the element (S153's `world_is`: workers "invent
  the line at close") is admitted, proven by a battery arm.
- *The read the COO runs*: `--status-census AMGT_RESAPP` prints with / without (named) / word distribution over
  `97 order(s) at HEAD` (94 / 3 at the cut; AC3 re-measures).

**`AMGT-rk-57` (R14-T3; process; row S169) -- MECE:** one new READ beside one existing read, in one gate -- the
open-order census (`surprise-row-gate.py:1125-1165`, terminality by the spine's rule `:436`, `:487-488`, untouched)
and the acceptance sweep (per criterion of every order of the round, PASS / FAIL / UNVERIFIABLE by SUBTRACTION:
PASS and FAIL are the two verdict words the schema allows a mechanical row, `PROOF_OF_SPEC.schema.json:233-241`;
everything else -- the four other statuses, a judgment row `:255`, a missing row, a missing, unreadable or
ambiguous instance -- is UNVERIFIABLE with its reason); a slug-time NOTE and a CLI read carry it; the refusal
conditions of the L10 precondition (`:1256-1294`) do not move, `proof-of-spec-check.py`'s frames do not move, and
the CVO's L9 grade stays the CVO's. **GRAIN:** the sweep reads the instance's OWN acceptance rows by criterion id
against the order's OWN `<criterion>` tags, at the same ref the census reads (HEAD, or the merged index), located
by `_proof_terminal`'s own lookup (`:1056-1113`) -- the property S169 named as unread ("read the frames, not the
label"), read; the battery grades REAL bytes at HEAD (the rk-30 page-half instance, AC1 PASS / AC2 FAIL). **INTENT:**
one axis -- a round's close shows, in one output, both what is terminal and what passed, so a close over a FAIL is
visible to the seat closing it. **STATE:** moves the gate file (new functions, one note site, one CLI limb, arms)
and adds one battery; moves NO instance, NO order, NO terminality rule, NO refusal condition; changes no seat's
authority (the COO disarms S169, the CVO grades, the CTO recuts).
- *Not a refusal, by the file's own rule* (`:991`, corrected @7f82f66f93): a slug cannot remedy a FAIL, so the sweep
  is disclosed beside the census note (`:1943-1946`), never appended to the violations; the self-test proves the
  sweep contributes zero violations.
- *Three classes, denominator printed* (analysis s.3.3 `:81-85`): `PASS a / FAIL b / UNVERIFIABLE c of d criteria
  over e order(s)`, the round read from the slug's own `round` (`_round_num` `:927`), unrounded orders bucketed and
  counted, never dropped.
- *The negative control is at HEAD*: `deliverables/0.9.0_WK_AMGT_RESAPP~31/...rk-30.page-scores-render.proof_of_spec.json`
  reads AC2 FAIL while the census counts the order terminal; AC2's battery prints both reads side by side.
- *The hand sweep and the tool may differ, and the difference is recorded*: 26 / 3 / 0 over 15 orders by hand
  (s.1 `:28-33`); the tool classes rk-26's criteria UNVERIFIABLE (no instance) and adds rk-30 page AC2 -- AC3
  prints what the tool reads.
- *The read every close runs*: `--acceptance AMGT_RESAPP --round 13`, rc 0 always; the hand sweep the ruling
  required "until the tool lands", mechanized.

**`AMGT-rk-58` (R14-T4; row W34-S2; process) -- MECE:** ONE new grant path for ONE act class -- the co-signed
DIRECT act -- delivered as a MINTER (`.tools/direct-act-order.py`) plus its test and one sentence in `/dispatch`
Step 4; the gate that decides admission (`owned-paths-validate.py:114-122`, `:176-206`) and the L6 gate
(`to-pipeline-gate.py`) are READ and CALLED, never edited, so the estate keeps exactly ONE grant source (the order)
and ONE issuance gate; the round-13 residue the row measured is already landed at `3c2a6e47ca`
(`scoped-amgt-api.tf:161`) and is outside this cell. **GRAIN:** every criterion measures an OBJECT at the level
claimed -- the self-test's own `RESULT: 0 arm(s) failed of N`; a dry-run mint against the REAL committed round-13
scores-prefix pair printing two 64-hex HEAD hashes (`PAIR:` line, 1 of 1) and a rendered order counted for one
`<invocation>` and one `<expect>`; the L6 gate's own `check_file` verdict on those bytes at a tree path (0 of 1
fixture); a refused mint's rc 2 with the named path and an UNCHANGED directory count; pytest's `N passed`; a byte
count of non-ASCII per new file -- never a reading of the tool's prose. **INTENT:** one axis -- a worker spawned off
a signed pair holds a grant the mechanical gate can read, bounded to what the pair signed, or it is not spawned.
**STATE:** moves nothing at HEAD but three files (two new, one sentence appended); does not move
`.owned-paths.yaml`, either gate, any ledger half, any task order, the live estate or any pool prefix; the AC2
fixture is transient by construction (written and deleted in one `try/finally`).
- *The order is the grant, and the pair bounds it* (`owned-paths-validate.py:114-122` @4e3142cfb3; row
  `W34-S2` `:8721`): the minter emits a NON-TERMINAL tree order `issued_to 0.9.0_WK_<CODE>~<slot>` whose `<paths>`
  = the validated `--path` entries plus the five standing entries, and REFUSES (rc 2) any entry NEITHER half names
  verbatim (`REFUSED: path not named by either half: <entry>`, AC3's planted negative).
- *Reads the pair at HEAD, never the worktree*, exactly as the lane gate reads orders (`:191-197`): `git show
  HEAD:<half>`; both halves must carry a heading containing `--section`; their sha256 over HEAD bytes is printed
  (`PAIR:` line) so the minted order cites the vintage it was cut from.
- *Never emits what the gate refuses*: on write, the minter imports `to-pipeline-gate.py` via
  `importlib.util.spec_from_file_location` (the gate's own pattern, `:2185-2190`) and calls `check_file(root, rel)`
  (`:2402`); a violation deletes the file and exits 3 with the text. AC2 proves the same on a dry-run render handed
  to `check_file` at `task-orders/.fixture-AMGT-rk-58.direct-act.md`, removed in `finally`.
- *The issuer's inputs are the issuer's*: the three preflight lines (`RUN -- (` with a digit, or
  `DECLARED-NOT-APPLICABLE <reason>` -- the gate's `:65-67`, `:77-83`) and the `<proof_of_spec>` block come from
  files the COO wrote after running the batteries; the minter validates their grammar (one `<invocation>` and one
  `<expect>` per criterion, `cell_refs` = `--cell`) and never invents a criterion.
- *Issuer identity is checked*: `OPAL_AGENT_SERIAL` must start with `2.0.0_SA_COO` (base or lane, the L6 owner),
  and the `--cell` token must occur in the decomposition text, mirroring the gate's `<owned_cells>` limb (`:246-331`).
- *Dry run writes nothing* (`C-VALIDATION-NAMES` `:1652-1658`): `--dry-run` prints the render between
  `---BEGIN ORDER---` / `---END ORDER---` and touches no file; AC3 measures the task-orders directory count before
  and after a REFUSED non-dry mint and requires equality.

**`AMGT-rk-59` (R14-T5; row W34-S1; s.3.7; infra) -- MECE:** ONE expression on ONE resource in ONE root --
`aws_lambda_function.chatter_axis_producer.source_code_hash` at `chatter-axis-schedule.tf:124` -- plus the comment
block that documents its precondition (`:33-44`); the schedule (`:172-184`), the role and policy (`:58-116`),
`build_zip.py`, `scoped-amgt-api.tf`, the state and the live function are outside it, and the ruling's second arm
(a build step committed into provisioning) is NOT taken here and NOT taken by `AMGT-rk-60`. **GRAIN:** every
criterion measures the object the row measured -- a Terraform EVALUATION in this worktree's own harvest root: the
count of the `filebase64sha256` evaluation error on HEAD's bytes (1 of 1, the planted negative) against the edited
bytes (0 of 0) under the same targeted plan with the zip absent; the untargeted plan's rc and summary; `terraform
console`'s value against Python's own base64(sha256(zip)) with the zip present (equality, the positive control);
the diff's hunk ranges against the two permitted line ranges; the schedule's two literal strings counted once in
HEAD and once in the edit -- never a reading of the comment, never a claim about the provider from memory.
**INTENT:** one axis -- an unrelated resource's missing local artifact never blocks a plan in a shared root; the
resource that needs the artifact still fails closed at its own apply. **STATE:** moves one tracked file; does not
move the live function, the schedule, the state, any pool prefix, the zip's contents or the build script; names NO
apply, and any function diff the built zip reveals is RECORDED as the pre-existing build/live delta and left to the
COO's consolidated chatter redeploy under `AMGT-rk-53`'s pair.
- *The expression* (`:124`): `fileexists(local.chatter_axis_zip) ? filebase64sha256(local.chatter_axis_zip) : null`
  -- present zip: byte-identical value (AC4 `hash_equal True`); absent zip: `null`, no evaluation error (AC2, AC3),
  `filename` (`:123`) still read at apply so the function cannot be applied without it.
- *The planted negative is the row's own failure*: AC2 writes HEAD's bytes back for ONE targeted plan on
  `aws_iam_role.chatter_axis_scheduler` (`:146-156`, unrelated to the function) and requires the exact error text
  (`:8689`), then restores the edit and requires rc 0 -- the discriminator could differ if the claim were false.
- *Read-only Terraform by construction*: `-input=false -lock=false -refresh=false` on every plan (no state lock
  against a peer, no refresh write), `validate`, `console`, `fmt -check`; `.tools/safe-apply.sh:52-66` gates apply
  only and is never invoked; `aws lambda update-function-code` never.
- *The schedule is untouched* (PRD s.10 `:1633`, `:1660-1661`: the chatter schedule and every cadence stay
  Andrew's): AC5 counts `cron(0 10 * * ? *)` and `state = "ENABLED"` once in HEAD and once in the edit; comp-schedule
  RUN with its 5 of 5 carriers is the preflight's evidence that this file's schedule gate did not move.
- *Lane read before any apply was named* (`.owned-paths.yaml:1906-1907`, CLOUD_OPS_OR_ETL; ADHC_OWNPTH.005
  `owned-paths-validate.py:114-122`): the worker commits the one `.tf` on this order's grant; `change_management/`
  and `.open_deploys/` are granted and unused because no apply exists to ledger.
- *Diff confinement* (AC5): `git diff -U0` hunks' old-side ranges sit inside `:33-44` or start at `:124`; one file
  changed of one expected; 0 non-ASCII bytes, 0 CRLF.

**`AMGT-rk-60` (R14-T6; row W31-S1; process) -- MECE:** ONE provisioning script with three verbs and a self-test,
and ONE skill step naming it; the nested portal repository's branches, the superproject gitlink, `.gitmodules`
(stays empty -- the row's shape (a) is not taken), `worker.md`, every task order and `build_zip.py` (`AMGT-rk-59`'s
alternative arm) are outside it; the `npx` decoy (row W31-S2) is `0.4.0_DT_ClientPlatform`'s and is bypassed here
by resolving `tsc` by path, never fixed. **GRAIN:** every criterion measures the provisioned OBJECT, not the
script's prose: the self-test's own `RESULT: 0 arm(s) failed of N`; in this worker's OWN worktree, the entry count of
`portal/` before (0 of 0) and the existence of the two exact paths row W31-S1 found absent; the nested checkout's
`rev-parse HEAD` against the main tree's portal HEAD (equal) and its `status --short` (0 lines); `tsc --version` by
path from inside the provisioned portal against the main tree's (same version); the nested repository's worktree
listing before and after `remove` (1 of 1 then 0 of 0, prunable count unchanged); byte counts on the two edited
files. **INTENT:** one axis -- a portal cell's worktree is buildable at the ref the issuance names, and its teardown
leaves no `prunable` residue. **STATE:** at HEAD moves two files (one new script, one skill step); at runtime
creates and then REMOVES one nested worktree and one directory link inside this worker's own worktree; does not
move the nested repository's `DEV`, any existing nested worktree, the main tree's `node_modules`, the gitlink, or
anything under `portal/` for commit.
- *The shape is precedent, the gap is the ref* (`git -C portal worktree list`: `wk-amgt_resapp-11-1-portal` exists;
  gitlink `2453a7b4` is 6 behind DEV `625a0888`): `portal <worktree> [--portal-ref <ref>]` adds a linked worktree of
  the nested repository INTO the empty gitlink directory (`git worktree add` accepts an empty directory), on branch
  `wk-<CODE>-<n>-portal`, at the ref the issuance names (default: the nested HEAD), and prints `PORTAL_REF:` and
  `GITLINK: ... behind_ref=N` so the choice is on the record -- *"the issuance says which"* (analysis `:146`).
- *No install* (`CLAUDE.md`: never an install; bun via PATH, never a baked path): `link` mode joins the main tree's
  `node_modules` by a directory link (junction when `cmd.exe` is on PATH, symlink otherwise -- capability-guarded, the
  one device-purpose branch); AC3 proves `./node_modules/.bin/tsc --version` resolves BY PATH (the decoy-proof
  resolution `AMGT-rk-53` AC6 uses).
- *Refusals are the negatives*: an unresolvable `--portal-ref` (rc 2, nothing created), a non-empty `portal/` (rc 2,
  never overwrite), a main tree without `portal/.git` (rc 2); each is a self-test arm with its denominator.
- *Teardown is part of the mechanism*: `remove` takes the nested worktree down FIRST (`worktree remove --force` +
  `prune`), then the superproject worktree, so the nested repository never gains a `prunable` entry (the `C:/tmp/
  wk-amgt-10-1/portal` entry at the cut is that failure, measured); AC5 runs `--portal-only` on this worker's own
  worktree and requires the empty gitlink directory back and the main tree's `node_modules` intact.
- *The skill step carries the ref* (`SKILL.md:173-177`): `provision <CODE> <n> --path <path> [--portal-ref <ref>]`,
  `<ref>` = the issuance commit's `fanout:` `portal_ref:` value; the drain uses `remove`; the existing `git worktree
  add -b wk-<CODE>-<n> <path> HEAD` line stays as what the script runs (AC4 counts it 1 of 1).
- *Dry run by construction* (`C-VALIDATION-NAMES` `:1652-1658`): the self-test works in `.scratch/`, AC2-AC5 work in
  this worker's own worktree, nothing is committed under `portal/`, nothing is pushed, no cloud act exists.

**`AMGT-rk-61` (R14-T7; row W27-S10; s.3.4; FWD-13; co-sign YES) -- MECE:** ONE router arm in ONE function
(`handler()`'s `/security/{key}/{leaf}` match, `scoped_amgt.py:3315-3324`), ONE offline test file, and ONE ledgered
redeploy of ONE Lambda under ONE pair section; the route table (`:3444-3474`), the gateway route set
(`scoped-amgt-api.tf:286-308`), the eight leaf readers, `resolve_identity()` (`:1712`), the role and its policies,
the pool and every other function are outside it; `AMGT-rk-53`'s adapter regions (`generation_fields`,
`_ranking_reason`) are disjoint and ride this artifact as NAMED blast radius, not as this cell's edit. **GRAIN:**
every criterion measures the object the row measured at the level the row measured it: in-process `handler()` on the
worktree bytes with the boundary patched to CAPTURE the string it receives (32 of 32 slash invocations, 24 of 24
validation-name invocations, 3 of 3 negatives at 404); the live function's `CodeSha256`, the artifact's `VersionId`
and the role's policy hash read BEFORE the act and again AFTER; a DIRECT `lambda.invoke` census of the 13 GET routes
and of 6 encoded/literal pairs before and after, the literal form's router refusal counted (6 of 6 before, 0 of 0
after) -- never a gateway capture (MFA-blocked, s.3.5) and never a claim about what the gateway forwards.
**INTENT:** one axis -- whichever way a slash arrives in `security_key`, the route boundary receives ONE string and
the page is about ONE company (FWD-13). **STATE:** moves the function's code (`CodeSha256`, `CodeSize`,
`LastModified`) and the `/security` arm's behaviour on direct invocation for slash-bearing keys, plus the rankings
responses' `empty_reason` field (rk-53's bytes); does NOT move the role, env, layers, timeout 29, memory 512, the
route set, the gateway, any pool object, any table, or any other function -- and AC5/AC6 print each of those as
unchanged.
- *The arm* (`:3315-3324`): `len(rest) >= 3`, `leaf = rest[-1]`, `requested = unquote("/".join(rest[1:-1]))` --
  `BP%2F_LN_Equity` and `BP/_LN_Equity` both become `BP/_LN_Equity` at `resolve_identity()`; an unknown or missing
  leaf still falls to the `:3396` refusal (AC2 arm c, 3 of 3).
- *The gateway is left alone, deliberately* (`scoped-amgt-api.tf:286-308`, single-segment `{security_key}`, no
  `{proxy+}`; `test_scoped_amgt_mount.py` diffs the table both ways): through the gateway only the `%2F` form can
  arrive, and it already works (analysis `:37-39`, 33 of 33 with `%2F`); the ruling *"remove the question"* is
  delivered on the handler, where the row measured the defect, without widening the route surface.
- *The pair is read before the first live act* (AC1: both halves, sha256, an `AMGT-rk-61` heading 1 of 1 each, a
  rollback named) and the rollback target is THIS act's pre-act `CodeSha256` + artifact `VersionId` (AC4, written
  to `.scratch/rk61_pre.json`); either half absent = read-only criteria only, BLOCKING row, STOP.
- *Single writer, enforced twice*: `git log -3` confirms rk-53's commit is in the worktree's history before the
  file is touched; AC3's census over the four adapter paths on `SITEZ` since the worktree's base must print
  nothing (0 of 0) beside a positive control that prints one line.
- *The deploy is a ledgered procedure, not a criterion*: `deploy_ledger.py open` BEFORE the upload (C2 gains a
  seventh entry, closed on AC6), `build-and-upload-scoped-amgt.sh` (the artifact bucket, never a pool bucket --
  Andrew ~21:45Z on `opal-data-assets`), the rk-59 plan precondition or `build_zip.py` (never a placeholder), a
  targeted plan reading `0 to add, 1 to change, 0 to destroy` on the one resource, `HALT_ACK=1 safe-apply.sh -target`,
  then AC5's `CodeSha256 == uploaded sha` and 0-diff replan, then the entry COMMITTED (round-13 COO half item 7).
- *Never-widen on the served plane* (AC6): 13 of 13 GET routes with unchanged statusCodes (`LOST [] GAINED []`), 6
  of 6 slash pairs equal with 0 router refusals, the role policy sha unchanged, and the breakout rankings response
  carrying `empty_reason` (rk-53's bytes served); any miss is the rollback branch, executed in-session and ledgered
  (NEVER-2).


### 22d. CHAINS, QUEUES AND THE ORDER OF SPAWNS -- from the censuses' `depends_on` edges (22b), not from the letters

**M, the number of dependency-independent chains, is MEASURED from the edge set (20 edges over 31 cells, printed by the
aggregator at the cut), by subtraction from the 31, never by recall:**

| chain | cells (edges) | first spawn | why it is one chain |
|---|---|---|---|
| C1 identity-entry | `rk-31` | wave 1 | no edge in or out (its only coupling is REACHABILITY: its crosswalk makes other chains' validation objects served) |
| C2 production-home -> universe -> model block | `rk-33` -> {`rk-32`, `rk-34`}; `rk-34` -> `rk-35` -> `rk-36` -> `rk-37` | `rk-33` | `rk-32`/`rk-34` share `build_universe.py` and the unit-map home with `rk-33`; `rk-34`..`rk-37` all edit `model_block_pull.py` (M drafter: the whole M queue is sequential on slot ~39 after `rk-34` on ~38) |
| C3 filings + the management cells that read them | `rk-39` -> `rk-38`; `rk-39` -> `rk-40`; `rk-42` -> `rk-41`; {`rk-38`, `rk-47`, `rk-48`} -> `rk-49`; `rk-47` -> `rk-48` | `rk-39`, `rk-42`, `rk-47` | `rk-49` (E7) reads `rk-38`'s `verified_site`, so chains F and E5-E7 are ONE chain by edge; F's shared-file queues: `fetch.py` `rk-39` -> `rk-38`; `analyze.py`/`drafting_build.py` `rk-42` -> `rk-41` -> `rk-40` (F drafter) |
| C4 management adapter -> one pool | `rk-43` -> `rk-45` | `rk-43` | `rk-45`'s one adapter line is behind `rk-43`'s adapter change; `enrich.py`'s pool-write region is shared with `rk-47`, so the ISSUER sequences `rk-47` after `rk-45` DRAINS (a resource rule, not an edge -- C3's `rk-47` therefore waits on C4 in practice) |
| C5 management batch census | `rk-44` | wave 1 | reads only |
| C6 roster parser shapes | `rk-46` | wave 1 | reads only |
| C7 peers | `rk-50` -> `rk-51` -> `rk-52` | `rk-50` | `rk-51` reads `rk-50`'s R-1 object; `rk-52`'s fixture is `rk-50`'s object under `rk-51`'s fields |
| C8 lists: no rank without signal | `rk-53` | ADAPTER QUEUE | edits `scoped_amgt.py`: held to the single-writer queue below |
| C9 lists: a MEASURE cell | `rk-54` | wave 1 | reads only |
| C10-C15 tools | `rk-55`, `rk-56`, `rk-57`, `rk-58`, `rk-59`, `rk-60` | wave 1 | six chains of one; disjoint surfaces per the L+T censuses; `rk-59` is the one infra cell (`CLOUD_OPS_OR_ETL`, a real `comp-iam` declaration) |
| C16 tools: the adapter's own row | `rk-61` | ADAPTER QUEUE | edits `scoped_amgt.py` |

**M = 16.** Cross-chain RESOURCE rules (not edges; they decide spawn ORDER, never coverage):

1. **ADAPTER SINGLE-WRITER QUEUE.** Six cells edit `lib/research/api/scoped_amgt.py` and/or redeploy
   `opal-amgt-scoped-api`: `rk-43`, `rk-45`, `rk-53`, `rk-61`, `rk-36`, `rk-37`. AT MOST ONE is live at a time; the
   next is cut from HEAD only after the previous DRAINS. Order: `rk-43` -> `rk-45` -> `rk-53` -> `rk-61` -> `rk-36` ->
   `rk-37` (the M pair comes last by its own edges anyway). Every adapter order carries the issuer's rule: before
   `build-and-upload`, `git log <merge-base>..SITEZ -- lib/research/api ...` prints NOTHING or the worker STOPS, and the
   rollback target is the pre-act hash THAT worker reads. Why not one consolidated COO deploy at the end (the issuer's
   first design): every drafted served-plane criterion is written against the LIVE plane after that cell's own
   redeploy, and rewriting six cells' live criteria into in-process invokes at the cut is a larger correctness risk
   than serializing six deploys; the M queue was serial already, so the queue costs two extra serial steps
   (`rk-53`, `rk-61`) and nothing else. ONE EXCEPTION, as drafted: `rk-53` runs NO deploy (its served claims are proven
   in-process on `handler()`); its adapter bytes reach the served plane in `rk-61`'s redeploy (cut from HEAD after `rk-53`
   drains), and its `amgt-resapp-chatter-axis` bytes in ONE COO redeploy after `rk-53` drains, scoped in the chain L
   halves. `rk-53`'s page edit needs `portal/` populated by the issuer at spawn (rule 6), so it does not wait on `rk-60`.
2. **`enrich.py` queue:** `rk-45` -> `rk-47` -> `rk-48` -> `rk-49` (the pool-write region `:689-699` is touched by
   `rk-45` and `rk-47`; `rk-48` and `rk-49` are told to STOP if `roster_source`/`--skip-pool` are absent from their
   worktree, i.e. cut after `rk-48` / `rk-47` drain).
3. **`model_block_pull.py` queue:** `rk-33` -> `rk-34` -> `rk-35` -> `rk-36` -> `rk-37` (one edit surface, five cells).
4. **`build_universe.py`:** `rk-33` -> `rk-32`.
5. **F queues:** `rk-39` -> `rk-38`; `rk-42` -> `rk-41` -> `rk-40` (and `rk-40` after `rk-39` for the Keyence source
   object and `detect_language`).
6. **Portal cells** (`rk-52`; `rk-43`'s page edit): the worktree gets `portal/` populated by
   `git -C portal worktree add --detach <wt>/portal <ref>` + `bun install` (an existing lockfile; the one permitted
   install), `./node_modules/.bin/tsc -b` never `npx tsc`; no push, no promote (LD-0367/0368; PROD HELD).
7. **Never-widen pairs BEFORE spawn.** Co-signed cells (`rk-31`; `rk-34`..`rk-37`; `rk-41`; `rk-43`, `rk-45`, `rk-47`,
   `rk-48`; `rk-51`, `rk-52` at promote; `rk-53`; `rk-61`): the COO halves are the seven
   `ledger/NEVER_WIDEN_ROUND14_CHAIN_<I|M|F|E|P|L|T>_COO_HALVES.md` files (I, M, F, E, P in the L5 commit; L, T with the
   issuance), one section per cell, each naming blast radius, writer census N, both outcome branches and the per-key
   rollback from a pre-act state the worker measures FRESH; the CTO halves are the `_CTO_HALVES.md` twins, asked of
   `1.0.0_SA_CTO~Z` the same tick. A worker whose cell's section is missing from either file runs its read-only and
   dry-run criteria, files a BLOCKING row and STOPS. No co-signed cell is spawned before BOTH files carry its section.
8. **The Bright Data word for `rk-48` AC4-AC6** is not on file for the running validation (PRD v0.13 :751; the ~17:2xZ
   record :44-45); the spawn prompt states it only if Andrew gives it; else AC4-AC6 refuse with a row and AC1-AC3 land.

9. **THE REGISTRY GATE (Andrew ~21:1xZ via CTO msg 23778: `opal-data-harvest` is THE home for ALL AMGT_RESAPP data, bronze
   included, structured to the canon).** Four faces land bytes at a builder address (`rk-32`, `rk-33`, `rk-50`, `rk-51`).
   Each carries the same amendment: the live arm fires iff `lib/opal_naming.py address()` prints an `opal-data-harvest` bucket
   for the key under the scope token `harvest` (CTO L4 ruling @2560e04f46: `<vendor>/harvest/bronze/...`, `amgt/harvest/<tier>/...`;
   no `global` route, no `amgt` scope row); until `0.0.0_AB_MSTR~Z`'s two registry rows (home + R20 departure) land here by merge, the builder prints
   `opal-data-assets` and the arm is DEAD -- no write, REFUSED-BY-REGISTRY on the live criteria, one row. Consequence for the
   spawn order: `rk-33` spawns in wave 1 regardless (its dry-run half and refusal row are the cell); `rk-32` and chain P
   (`rk-50` -> `rk-51` -> `rk-52`) spawn ONLY after the issuer re-runs the builder probe and reads `opal-data-harvest` -- a
   gate held by another seat, verified real (the CTO's acceptance line in msg 23778), never a wait this seat chose. The
   existing `raw/<vendor>/<key>/<stamp>/` family in `opal-data-harvest` (chains I, M, E) is already in Andrew's bucket and
   is not re-cut here; its canon-form re-homing is the R19 conformance work the L10 addendum will name.

10. **`.tools/to-pipeline-gate.py` queue:** `rk-55` -> `rk-56` (same function region and self-test list; the L+T drafter).
    And `rk-55`'s own limb, once drained, REFUSES a second newly-added order into a round that already has orders at HEAD
    -- which is exactly why round 14 is ONE issuance commit and any later order in this round is an audited
    `# pipeline-override:`, never a second cut.

11. **Chain T edges from the drafter's censuses:** `rk-61` depends on `rk-53` (adapter queue) AND `rk-59` (the harvest-root
    plan hits W34-S1 until `rk-59`'s `fileexists()` lands; the order carries a `build_zip.py` fallback) -- `rk-59` is wave 1,
    so the edge costs nothing. `rk-58` and `rk-60` both edit `.claude/skills/dispatch/SKILL.md` in disjoint paragraphs
    (`:208-224` vs `:173-177`); their drains merge textually, second drain rebases on HEAD. `rk-60`'s provisioning script is
    NOT a dependency of this round's page cells: the issuer populates `portal/` by hand at spawn (rule 6); the script serves
    the next round. `rk-58` builds option 1 (a MINTED order from a committed pair); a gate that reads a signed pair is not
    built this round.

**Free-RAM rule:** re-read before each wave; below ~12 GB free the wave is cut on a sparse cone (Site Z memory).

### 22e. THE CARDS -- all six ANSWERED before this cut (@`4de34f0d95`, SA terms @`1699960261`), so no cell is held on a person

1 SA production use: YES by name for `C-PEER-SET-SA` and the `SA_FALLBACK` cells of `C-MODEL-FORECASTS` (`rk-50`, `rk-36`);
the terms are cleared by Andrew's own word, so a scheduled read waits on nothing in this round (no cell; any schedule stays Andrew's). 2 Lusha inside the validation: YES, no credit ceiling, scoped to the three
names (`rk-49`). 3 International battery order: RATIFIED (`rk-38`). 4 Unanchored drafted sentences: HOLD (`rk-41`).
5 Model cases: BASE = consensus EPS x trailing-median P/E; Upside/Downside ABSENT "methodology to be discussed with Andrew"
(`rk-36`/`rk-37`). 6 Headless capture: retired estate-wide -- MSTR's, outside this round; within it, NO order's criterion
needs a headless authenticated session (analysis s.3.5): a page cell tests the adapter directly and carries a JUDGMENT
criterion for the rendered page, graded by a human at L9.

### 22f. FAN-OUT

```
fanout:
  cap: 16                          # wave 1 spawns 13 of 16 chains (two held by the registry gate, two by the adapter queue, rk-56 by the gate-file queue); RAISED from the default 8 on Andrew's capacity word (~18:2xZ); measured 18:3xZ:
                                   # 20 cores at 14% load, 63.5 GB RAM / 31 GB free, 180 GB disk; 1.3 GB and ~40 s per
                                   # full worker worktree; the ceiling is the serialized DRAIN (one safe-merge at a time,
                                   # each independently re-verified by this seat), not CPU
  orders_total: 31                 # rk-31..rk-61
  slots_total: 27                  # ~35..~61; three sub-queues share a slot (M2/M3/M4 on ~39, E5/E6 on ~49, P2/P3 on ~52)
  chains_total: 16                 # MEASURED from the censuses' depends_on edge set (22d), not the eight letters: C1 rk-31; C2 I/H/M; C3 F+E5-7; C4 rk-43/45; C5 rk-44; C6 rk-46; C7 P; C8 rk-53; C9 rk-54; C10-C15 rk-55..60; C16 rk-61
  wave_1: [rk-31, rk-33, rk-39, rk-42, rk-43, rk-44, rk-46, rk-54, rk-55, rk-57, rk-58, rk-59, rk-60]  # 13 slots; rk-56 queues behind rk-55 (22d rule 10); every chain with no unmet dependency EXCEPT rk-50 (chain P) and rk-32, HELD on the registry gate (22d rule 9), and rk-53/rk-61, HELD on the adapter queue (22d rule 1)
  wave_2: [rk-32 + rk-50 when the builder prints opal-data-harvest; rk-56 after rk-55 drains; rk-34 after rk-33; rk-38 after rk-39; rk-41 after rk-42; rk-45 after rk-43 drains; rk-53 then rk-61 in the adapter queue; rk-35 -> rk-36 -> rk-37 after rk-34; rk-40 after rk-41 and rk-39; rk-47 -> rk-48 after rk-45; rk-49 after rk-38 and rk-48; rk-51 -> rk-52 after rk-50]
  ram_rule: free RAM re-read before each wave; below ~12 GB free the wave is cut on a sparse cone
  portal_rule: portal cells (rk-52, and any census-reported page edit) get portal/ populated by
               `git -C portal worktree add --detach <wt>/portal <ref>` + bun install (rk-60's own remedy, applied by hand this round)
  no_fleet_run: true               # Andrew, verbatim: "I dont care about rerunning until the process is completely validated end to end"
  carried_as_data: [W27-S3 residue: 11 drafting/v1 objects, re-opened after rk-42; two further C-PRODUCTION-HOME instances found at the cut (lib/opal_data_harvest/config.json universe_source -> deliverables/~3/universe.json; infra/aws/terraform/harvest/lambda_src/build_zip.py:91 -> deliverables/~4/universe.json) -- rows for rk-54/rk-33 to file, not orders]
  deferred_named: [AMGT-rk-27 (ledger stages; Refresh-queue L4 definition first), AMGT-rk-29 (house forecast; Posture brief first)]
```

## 23. ROUND 15 -- FROM THE L10 ROUND-14 ANALYSIS @`93cb6416e4` (`1.0.0_SA_CTO~Z`), msg 23907

**Cut by `2.0.0_SA_COO~Z`, post-reboot relaunch, per LD-0521 order (cut only after the round-14 analysis is on file).**
Round 14 does NOT close this round: `rk-32` + chain P still hold the count open on the bucket/tenancy word (analysis
s.1), and TERMINALITY cannot stamp while they stand. Round 15 is therefore **deliberately narrow** -- the analysis's
own s.3: three cells, **independent of every open word and of each other, no chain, no deploy, no served output
moved** ("None writes served output; no never-widen pair is needed unless the cutting decomposition finds
otherwise" -- this decomposition finds no need for one).

**THE THREE CELLS, each closing a named row:**
- **R15-T1** closes `AMGT_RESAPP-Z-W58-S2` (analysis s.2.1): GATE (x)'s missing-`<round>` branch refuses the exact
  shape `AMGT-rk-58`'s own direct-act minter emits by design. RULED: a narrow exemption for an order that
  EXPLICITLY declares itself round-less (a line-anchored `<direct_act>true</direct_act>` element), never a general
  weakening of one-issuer-per-round; a bare omission is refused exactly as today.
- **R15-M1** closes the UNASSIGNED half of `AMGT_RESAPP-Z-W39-S5` / `Z-S181` (disarmed, GRADUATED, owner named by the
  analysis s.2.2): `rk-61`'s carried repair of the two orphaned assertions in
  `lib/research/api/tests/test_generation_and_pool_routes.py` that still check the RETIRED two-value sentence-parsed
  contract (`NOT_CONFIRMED_NOTHING_FOUND`) instead of the six-value field-only contract `AMGT-rk-43` introduced
  (`ceo_profile_reading`, `lib/research/api/scoped_amgt.py:2377-2459`). Confirmed reproducing at this cut:
  `python -m pytest lib/research/api/tests/test_generation_and_pool_routes.py -q` -> 2 failed, 22 passed, both
  asserting `'NOT_SEARCHED' == 'NOT_CONFIRMED_NOTHING_FOUND'`.
- **R15-T2** closes `AMGT_RESAPP-Z-W39-S2` (analysis s.2.3): `integrations/bloomberg/research/pull_consumer.py`
  calls `mbp.stage_pull(blp, s3, ticker, pull_log)` -- 4 positional args against `stage_pull`'s 3-parameter signature
  (`model_block_pull.py:371`, `def stage_pull(blp, s3, security: str) -> dict`) -- inside a `try/except` that marks
  FAILED and unconditionally deletes the SQS message. EXPOSURE class (Rule 22's negative mirror), never fired:
  the served `packs/` prefix carries exactly one `status.json`, written before the defective call site was
  committed. The unused local `pull_log` dict (line 98) is dead beyond that stray argument.

### 23a. THE MAPPING -- CTO cell -> COO id and slot

| CTO cell | id | slot | chain | serves | co-sign |
|---|---|---|---|---|---|
| R15-T1 | `AMGT-rk-62` | ~62 | none (independent) | W58-S2, unblocks `rk-58`'s minter | no |
| R15-M1 | `AMGT-rk-63` | ~63 | none (independent) | W39-S5 / Z-S181's carried repair | no |
| R15-T2 | `AMGT-rk-64` | ~64 | none (independent) | W39-S2, EXPOSURE closed before first real traffic | no |

**Thirty-one to thirty-four:** round 14 minted `rk-31`..`rk-61`; round 15 continues the same disjoint id range,
`AMGT-rk-62`..`AMGT-rk-64`, worker slots `~62`..`~64`. No chain: the analysis names all three "independent of
every open word and of each other" (s.3), and this seat's own census below confirms disjoint file sets.

### 23b. SURFACE CENSUS

| cell | CTO | co-sign | depends_on | files_written | pool prefixes written | vendor calls | live AWS acts |
|---|---|---|---|---|---|---|---|
| `AMGT-rk-62` | R15-T1 | no | none | 3: .tools/to-pipeline-gate.py; .tools/direct-act-order.py; .tools/tests/test_gate_x_round_issuer.py | none | none | 0: none |
| `AMGT-rk-63` | R15-M1 | no | none | 1: lib/research/api/tests/test_generation_and_pool_routes.py | none | none | 0: none |
| `AMGT-rk-64` | R15-T2 | no | none | 2: integrations/bloomberg/research/pull_consumer.py; integrations/bloomberg/research/tests/test_pull_consumer_arity.py | none (the live proof writes ONE synthetic status.json under `packs/ZZZTEST_US_Equity/` and deletes it in the same act -- no residue) | none | 1: one real SQS SendMessage/ReceiveMessage/DeleteMessage round trip on `opal-research-pull-requests` (a synthetic, non-production ticker), plus one S3 put_object/delete_object pair on the same synthetic key. No Lambda, no Terraform, no IAM, no Bloomberg call (the worker MONKEYPATCHES `mbp._load_blp_client`/`stage_pull`/`stage_derive` in its own process; nothing it does reaches the real Bloomberg terminal) |

**Files written by more than one cell:** none -- all three cells are disjoint, matching the analysis's "independent
... of each other".

**Not cells, and why:** `rk-32`/chain P, `rk-48`'s live arm, `rk-49`'s second in-place rewrite and `rk-49`'s drain
all wait on their own named Andrew word (analysis s.3, "Not cut, and why"); this seat re-opens each under its own
pair section when its word lands -- unchanged by this round.

### 23c. FAN-OUT

```
fanout:
  cap: 8                            # default; 3 of 3 independent cells fit one wave
  orders_total: 3                   # rk-62..rk-64
  slots_total: 3                    # ~62..~64
  chains_total: 3                   # each cell is its own chain -- no shared file, no depends_on edge
  wave_1: [rk-62, rk-63, rk-64]      # all three spawn together; nothing holds any of them
  wave_2: []
  no_fleet_run: true
  carried_as_data: []
  deferred_named: []                # rk-32/chain P, rk-48's live arm, rk-49's rewrite and drain -- held on their own named Andrew word, not deferred by this seat's choice
```
