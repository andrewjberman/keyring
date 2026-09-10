# AMGT_RESAPP -- L5 decomposition (COO) -- v0.2

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
