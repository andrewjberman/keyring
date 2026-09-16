# AMGT_RESAPP -- L5 decomposition (COO) -- v1.4 (s.20 = round 12; s.18 = round 10; the header read v0.6 through v1.0 and is corrected here)

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

**THIRTEEN cells, ids `AMGT-rk-1` .. `AMGT-rk-13`** -- the analysis's A-M, remapped into dependency order. The letters
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
