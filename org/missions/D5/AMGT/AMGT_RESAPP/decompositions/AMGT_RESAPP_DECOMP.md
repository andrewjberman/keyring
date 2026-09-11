# AMGT_RESAPP -- L5 decomposition (COO) -- v0.6

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
| `AMGT-rd-8` | S16 | FWD-15 | **THE SURFACE ITSELF.** The `.tsx`: a persistent **Lead Panel** (universe discovery -- Trending/Breakout x Price/Chatter, List/Chart, Security overlay, Starred) above **three tabs: Thesis / Peers / Coverage**. **Print is a header export action**, not a tab. **The Model tab is CUT and its figures REHOMED** into Thesis and the Security overlay. Reads pre-computed rows from `opal-amgt-security-metrics`; never re-derives a ranking at render time. | OPEN | `rd-5`, `rd-6`, `rd-7` |

### 13c. Rule 24 record for what v0.6 ADDS (the eight round-5 cells)

- **(i) MECE over the DECLARED domain, BY SUBTRACTION from a printed denominator -- not by recall.** The
  domain is the SIX named constraints of PRD s.3b plus the S16 manifest row. Subtracting what each cell
  covers: `C-AMGT-ARTICLES-STORE` -> `rd-1`; `C-SERVER-SIDE-RANKING` -> `rd-2` (the store) + `rd-5` (its
  writer); `C-PRICE-RANKING-BOXSIDE` -> `rd-6`; `C-HARVESTER-COMPUTE` -> `rd-3` (box + role) + `rd-4` (the
  four harvesters); `C-STARRED-PER-FIRM` -> `rd-7`; the approved page shape + S16 -> `rd-8`. **REMAINDER
  ZERO.** `C-VENDOR-WORD-HARVESTERS` is the sixth constraint and is deliberately NOT a cell -- it is a
  time-scoped BOUND on `rd-4`, carried in 13d. A constraint that is a bound rather than a cell is named
  here so the subtraction balances visibly rather than by silence.
- **(ii) SAME GRAIN:** each cell is one engine with one home. The two stores are separate cells because
  they are separate tables with separate consumers, not one "make the tables" cell.
- **(iii) INTENT COHERENCE:** one axis per cell. Storage (`rd-1`, `rd-2`), compute host (`rd-3`),
  acquisition (`rd-4`), ranking production (`rd-5`, `rd-6`), marker state (`rd-7`), presentation (`rd-8`).
  No cell mixes another's concern; notably the BOX is separated from the HARVESTERS that run on it, because
  a box that exists and a harvester that runs are different proofs.
- **(iv) STATE COHERENCE -- what these do NOT move:** they build the surface, so for the first time an
  `EXERCISED` bar becomes REACHABLE -- but **REACHABLE IS NOT REALIZED.** No cell may grade its own FWD
  REALIZED on the strength of its own artifact; fourteen of fifteen outcomes need a PERSON to have used the
  thing, which is L9's to grade and never L7's. They do NOT close `FWD-9` (APPLIED, the drafting face) and
  do NOT touch rounds 1-4's landed correctness work.

### 13d. BOUNDS carried onto the round-5 cells

- **`C-VENDOR-WORD-HARVESTERS` IS TIME-SCOPED AND ITS CLOCK IS THE BOX.** Andrew gave the per-use word for
  Seeking Alpha, FT, Bloomberg and WSJ for THIS project's harvesters, **effective when the harvester box is
  stood up and ready to run -- NOT before.** So `rd-4` may not egress to any of the four until `rd-3` has
  landed. It is NOT a blanket grant: `C-VENDOR-EGRESS` still binds every other vendor and every other use,
  and "availability is not authorization" is unchanged.
- **NO MONITOR, NO ALARM, NO FRESHNESS-CHECKER** (standing moratorium; `comp-schedule` carrier C3 counts 12
  standing NEVER clauses). `rd-5` and `rd-6` are SCHEDULED PRODUCERS, which is not only permitted but
  required ("production pipelines MUST be scheduled"); a producer that computes a ranking is not a monitor.
  STOP: neither cell may add an alert, an SNS topic, an SES send or a freshness checker on top of its output.
- **`opal-data-research` IS AN EXISTING DECLARED RESOURCE AND IS NOT RE-CREATED** (rows `Z-S5` -> `Z-S8`).
  Measured at this cut: versioning **Enabled**, SSE AES256 (SSE-C blocked), **no lifecycle** (accumulation is
  not silently truncated), **no bucket policy** (IAM-only), us-east-1, and list access PROVEN by a successful
  `list-objects-v2` -- existence and access measured separately. Created by this project's own `AMGT-s-6`
  @`20260910T2059Z` via `safe-apply`. A round-5 cell touching it INTEGRATES; it must not re-create,
  re-declare or re-configure it.
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
- **ROUND 5 (v5, THE SURFACE ROUND, 8 cells, 2 chains):** roots `AMGT-rd-1` and `AMGT-rd-2` spawn at
  issuance (TABLES FIRST).
  **CHAIN A (3 cells, slot ~1):** `rd-1` -> `rd-3` -> `rd-4`.
  **CHAIN B (5 cells, slot ~2):** `rd-2` -> {`rd-5`, `rd-6`, `rd-7`} -> `rd-8`, the three middles
  serialized in that slot's queue and `rd-8` handed last because it converges all three.
  **`fanout: 2 of 2 chains, cap 8.`** N = M = 2: asking for more workers than there are independent
  chains buys nothing and serializes anyway.
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
