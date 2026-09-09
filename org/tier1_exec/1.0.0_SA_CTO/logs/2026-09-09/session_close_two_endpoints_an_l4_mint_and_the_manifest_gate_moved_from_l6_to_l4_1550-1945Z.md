# Two L2 endpoints, an L4 mint -- and the surface-manifest refusal moved from the COO's task order to the CTO's PRD -- `1.0.0_SA_CTO~Z`

**archetype:** MIXED
**secondary_archetypes:** SCRIBE (spec) primary by volume; IMPLEMENT (the gate + the comp-find repair); DIAGNOSE (the blocked instrument, the VINTAGE contradiction)

**Date:** 2026-09-09
**Serial:** `1.0.0_SA_CTO~Z` (site-Z fabric; no `org/tier1_exec/1.0.0_SA_CTO~Z/` folder exists, so this
lands in the base-serial folder with the lane named in the title, per `/log` Step 0)
**Task Order:** ad-hoc -- L2/L3/L4 spine work on `NFRA_OPSEC202609`, `NFRA_REPORT`, `NFRA_IAMROLES202609`
**Window:** session start (no prior `~Z` log today; the three 2026-09-09 files in this folder are the
base seat and the `~X` lane) -> 1945Z. **14 commits.**
**Status:** COMPLETE

---

## Objective

Process Andrew's OPSEC crawler-protection addendum, take the `4.0.0_SA_CRO~Z` Global Infrastructure
Reporting brief through `/endpoint --forward` -> L3 -> L4, stand up `NFRA_IAMROLES202609`, and get
the tree clean and pushed. Mid-session two things changed the shape of the work: a shared blocked
instrument turned out to have **two** broken callers rather than one, and Andrew ruled that a
**surface manifest is mandatory at commit** with a `comp-adversary` grid beneath it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `"DENY-BY-DESIGN" --all --limit 30` | PASS | Found ruling 12 at source in one call; the relay had quoted it correctly but the SOURCE carried the disclaimer that decided the ruling. |
| comp-find | `--corpus aws --limit 2` | PASS | The repaired live-AWS plane. 757 hits / 2157 nodes, **and it prints its VINTAGE** -- which settled an intra-file contradiction. |
| comp-find | `"PRD_HEADER" --all --limit 20` | PASS | Found the existing L6 enforcer, which is what made this a MOVE rather than a new rule. |
| comp-read | on TO/PRD files `--for` | PASS | Qualifier surfacing; used through the endpoint reads. |
| comp-adversary | `compose <PRD> --out ...` | **PARTIAL** | Ran clean (rc=0, 38.5KB) and its sound limbs are genuinely useful, but the PACKET degenerated -- see Gap found. |
| comp-iam | `gaps` / `live` / `role` | PASS | The 16 undeclared roles; corroborated across two substrates. |
| comp-which | plain-English routing | PASS | Reflex before the repo searches. |
| comp-routes | `behaviors` | PASS | Consumer-walk grounding for `FWD-6`. |
| comp-system | `--gate --changed` | PASS | Fired twice; one STRUCTURAL-TWOPHASE override taken and DISCHARGED same-session at `09bb71eaa8`. |
| comp-schedule | armed-gate read | PASS | Loop-arming discipline at launch. |
| prd-manifest-gate | `--self-test` / `--census` / wired | PASS | **New this session.** 5 controls hold; census 0-of-8 refused; refusal + pass both exercised through the real `safe-commit` path. |

**What worked:** `comp-find --all` with a real `--limit` instead of a pipe. The one census that
mattered -- *which step-4 PRDs would this gate refuse* -- was answerable in a single call because the
schema already declared the discriminator (`step: 4`), so no new classifier had to be invented.

**What failed:** Two probes of my own, both returning clean-looking numbers. (1) `LC_ALL=C grep -c
'[^\x00-\x7F]'` on the commit message read **109** -- basic grep does not interpret `\x` escapes, so
the class matched literal `x`/`0`/`7`/`F`. The true count was **0**. (2) An earlier PRD-manifest
census used `grep -c` emitting two lines, so the shell test passed for all 205 files and the MISSING
list was structurally empty. Both discarded and re-run in Python. **A count that cannot be true is
the tell** -- and both of these could be true, which is why they cost a round each.

**Gap found:** `comp-adversary`'s T11 decomposition-neighborhood source resolves only for an artifact
carrying `<decomp_ref>` + `<owned_cells>`. **A step-4 PRD carries neither by construction**, so at L4
the tool can only offer filesystem adjacency -- and with all three sharp salience classes returning
zero, first-match-wins fell through to `S4 PERIPHERAL` and selected the first 12 of 962 siblings in
**directory order**. The packet is therefore 12 unrelated advisor-platform briefs. Not a bug: the
selection rule working as designed on an artifact whose neighborhood is uninformative. **The remedy
is downstream, not a code change** -- the COO's decomp DOES carry cells, so a run against that
resolves T11. Recorded in PRD section 9 so the next L4 author does not read the degenerate packet as
findings.

---

## Work Completed

### 1. `NFRA_OPSEC202609` -- the crawler-protection addendum (PRD v0.12 -> v0.14)

Established by direct read that `www.opalinvest.com` has **zero** anti-automation controls on its
form path, and that `FWD-13` (well-known attack patterns) is **structurally incapable** of serving
form spam -- a valid POST differing only in provenance. Added `FWD-19` and constraints `C-17`
(SOAK-FIRST), `C-18` (VOLUME-GRADED), `C-19` (NO-GODADDY), `C-20` (FWD-4-RECIPIENT).

**`C-19` re-cut the scope axis and that is the load-bearing result:** there is **no AWS-only route to
an edge** -- WAF cannot attach to bare EC2, and every candidate edge needs a GoDaddy DNS change
Andrew has ruled out. So `FWD-19`'s edge half is **UNBUILDABLE, not deferred**. The boundary is not
on-box-vs-edge; it is NO-GODADDY vs GODADDY.

Filed surprise row **`Z-S151`** (BLOCKING/ARMED, `disarm_owner 2.0.0_SA_COO~Z`): `FWD-4` graded
complete but is **unsatisfiable** -- 3 of 7 distinct alarm targets have ZERO confirmed subscribers
(`opal-login-abuse-alerts`, `astn-wsjft-alerts`, `etfs-reports-alerts`), positive-controlled by the 4
that do.

### 2. `NFRA_REPORT` -- L2 endpoint -> L3 register -> L4 PRD (v0.1 -> v0.3)

Endpoint cut at `2286056b79` (ELEVEN outcomes from a TEN-outcome brief; the eleventh against an OWNS
line no numbered outcome covered), confirmed against the amended brief at `62881a7369` -- **the
re-read earned its cost, because F11a falsified `FWD-2`'s acceptance line as first cut.** Andrew's
amendments folded at `0ad9ddf491`: `FWD-1` re-cut as declarative, `FWD-12` added, `C-AI` added.

Registered under D12 and PRD minted at `ff9900b0ea`. **v0.1 shipped with no SURFACE MANIFEST** --
see section 4.

### 3. The shared blocked instrument -- and there were TWO broken callers

`comp-find --corpus aws` and `org/modules/graph/comp_trigger.py` both passed `--mode inc` to
`kuzu_cli.py`, which accepts only `query|--json|--limit|--schema`. Fixed both at `9b99b49342` and
**exercised end to end, which nobody had done**. The fresh projection CORROBORATED the 16 undeclared
IAM roles. This unblocked `NFRA_REPORT` D4 and `NFRA_IAMROLES202609` D1 simultaneously -- a defect in
what the members SHARE, which no per-member check could have seen.

### 4. Andrew's directive: the surface manifest is mandatory AT COMMIT (`17c153a1cb`)

**This is a MOVE, not a new rule, and that is the whole finding.** `PRD_HEADER.schema.json` already
said the L6 TO gate "refuses a TO whose PRD lacks this block, the ENDPOINT section, or the surface
manifest", and then stated the consequence itself: *"A PRD with no header is not refused by itself --
a TO cut against it is."* **That sentence was true and it WAS the defect** -- the refusal pointed at
the COO's artifact for the CTO's omission, one step too late.

Built `.tools/prd-manifest-gate.py`, wired into `.tools/safe-commit.sh`:
- **Domain = the estate's own discriminator.** 205 tracked `*_PRD.md`; only **8** carry `step: 4`.
  An architecture doc merely NAMED `*_PRD.md` is out of domain.
- **Blast radius censused BEFORE the gate was written:** 0 of 8 refused today. Because the refused
  set is empty it ships fail-closed with **no legacy carve-out** (Andrew confirmed: *"we dont need
  legacy carve out"*) and **no audited override** (his word is "literally cannot"; flagged in-source
  as reversible in one word).
- **One detector, one primary:** it IMPORTS `to-pipeline-gate.py`'s `_top_section` +
  `MANIFEST_HEADING_RE` rather than copying them, inheriting CVO~A's hardening against two false
  passes (heading inside a fence; empty body). Two carriers of one rule drift from minute one.
- **Exercised both directions through the real path:** a throwaway manifest-less step-4 PRD was
  BLOCKED (rc=1, unstaged, 0 commits landed); the real PRD commit printed
  `[prd-manifest] OK: 1 step-4 PRD(s) carry a SURFACE MANIFEST`.

### 5. PRD v0.3 -- section 9 adversary grid, and three of my own errors caught by my consumer

`2.0.0_SA_COO~ZZ` (msg 20592) found what I had shipped:
- **(a) `S1` carried a TWO-value axis.** v0.2 abbreviated ruling 12 as "CHECKED vs BLIND"; the enum
  has **six** values and `INERT` is the one ruling 12 uses in its own worked example. A worker handed
  only that cell builds the wrong vocabulary. That lane could not fix it (section 8 is `ANY_CTO`) and
  mitigated at its own end instead.
- **(b) Section 7 and `S11` contradicted each other on VINTAGE, inside one file.** Resolved by
  **measurement**, not by preferring the newer sentence: the tool prints `VINTAGE: Built from the
  estate as of 2026-09-09 14:59:48 UTC. manifest: 86ea84674078`. Section 7 was the stale half.
- **(c) The JSON header still read `prd_version: v0.1` while the prose said v0.2.** The schema names
  that field's entire purpose -- *"the R3 monitor emits on new-or-bumped, so an un-bumped substantive
  edit is INVISIBLE to COO"*. **The manifest v0.2 added was invisible to the monitor that exists to
  announce it**, which is why both catches came through human reading.
- **(d) And the v0.2 census was SCOPED.** "Of the SIX tree-home L4-spine PRDs FIVE do" was true and
  scoped to `org/missions/**`. Unscoped on the step-4 discriminator there are **EIGHT** (adding
  `ADVI_INSURE` and `ADVI_49F` at the legacy `docs/architecture/` home), of which **seven** already
  carried one.

### 6. Ruling on `2.0.0_SA_COO~ZZ` msg 20592 -- neither `RP-s-1` resolution amends ruling 12

That lane found ruling 12's Axis-1 enum expresses neither a PERMANENT blind nor a DESIRED-not-APPLIED
row, proposed two additive resolutions, and asked whether they amend a sovereign-ratified enum.
**Both land at L5; nothing routes to Andrew.** Read at source: ruling 12 claims two axes, GREEN =
CHECKED+OK, and the forbidden pair -- an orthogonal field touches none of them. **And the record
disclaims completeness in its own words** (*"Every Axis-1 value is PROMOTED from a section already
running"*); a harvested vocabulary carries no MECE claim over a domain it never declared. Andrew's
verbatim word there was *"Both recs approved, move to Costs."*

### 7. `NFRA_IAMROLES202609` + estate hygiene

L2 endpoint cut (8 outcomes, UNCOVERED check clean), brief-create handoff written for relay to
`4.0.0_SA_CRO~Z`, ruling 20 folded at `02a6afae87`. Corrected my own claim that `comp-iam-usage` was
unbuilt -- **it IS built**, which discharged Andrew's standing ruling-18 deferral early. Also
corrected `0.0.0_AB_MSTR~Z`'s false law-staleness broadcast using blob identity across three refs
plus a positive control, and fixed `org/XXX.md` Step 1b-F (`4b4df0187c`) -- the loop-arming
subsection was the only one of ten that was bold text rather than a `###` heading, while every launch
prompt names it as the sole source of truth on loop authorization.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| The manifest gate ships with **no audited override** | Andrew's word is "literally cannot"; measured wedge risk is zero (0 of 8). Every sibling gate has one, so the departure is flagged in-source as reversible in one word. |
| Gate **imports** the L6 detector rather than copying it | Two carriers of one rule drift from minute one; the imported one is already hardened against two false passes I would otherwise have re-opened. |
| Domain = `step: 4` header, not the filename | 205 `*_PRD.md` vs 8 step-4 PRDs. Gating on the filename would demand manifests from 197 documents that are not in the spine. |
| Both `RP-s-1` resolutions land at L5 | They ADD orthogonally; every claim ruling 12 makes survives intact, and its record disclaims completeness itself. |
| The `DENY-BY-DESIGN` test is **that lane's**, not mine | It holds the website facts at a grain the PRD does not. A ruling made without them would be a guess wearing authority. |
| VINTAGE contradiction resolved by re-measuring | Both halves were my own writing; preferring the newer sentence would have been a coin flip dressed as a decision. |

---

## Files Modified

See commit messages: `5f4d4b894f`, `2286056b79`, `5d9497db65`, `62881a7369`, `68cf8271c6`,
`0ad9ddf491`, `02a6afae87`, `9b99b49342`, `09bb71eaa8`, `ff9900b0ea`, `26380c7bbe`, `1703e825d0`,
`17c153a1cb`, `2b92207ccc`. Rows needing extra context:

| File | Change | Committed |
|------|--------|-----------|
| `.tools/prd-manifest-gate.py` | **NEW.** Step-4 PRD manifest gate; `--self-test` (5 controls) + `--census` (blast radius). | Yes -- `17c153a1cb` |
| `.tools/safe-commit.sh` | Gate wired in, pathspec-keyed (NOT `IN_SCOPE` -- PRDs are `.md`). | Yes -- `17c153a1cb`, ASCII fix `2b92207ccc` |
| `org/standards/PRD_HEADER.schema.json` | Description corrected: the clause saying a PRD "is not refused by itself" is now false for the manifest limb. | Yes -- `17c153a1cb` |
| `.tools/comp-find` + `org/modules/graph/comp_trigger.py` | Dropped the stale `--mode inc` arg. `comp-find` hunk later superseded by CLOUD's R7 served-graph port in the merge; `comp_trigger` fix survived. | Yes -- `9b99b49342` |

---

## Blockers

- **AMBIGUOUS: the rule-bank version drift has no owner.** Head is v1.8; 8 SDK assertion sites sit at
  v1.2, ~20 days, identical on both fabrics. `3.0.0_SA_CVO~Z` corrected the surface to **7 files / 8
  sites** (the eighth file is `system_parity.py`, whose hits are self-excluded fixtures including a
  deliberate v1.1 negative control). Lane `0.8.0_AE_CloudComp` is **not seated**, so there is no
  agent to route it to. Carried to Andrew as an open call.

Nothing else is blocked. `NFRA_REPORT` L5 is CUT (`f060f2354e`, twelve cells `RP-s-1..12`) and L6 is
next at `2.0.0_SA_COO~ZZ`; **nothing is owed from this seat before it.**

---

## Current State

> Written for a reader with zero prior context.

**Law changed this session and it binds every PRD author.** `.tools/prd-manifest-gate.py`, called
from `.tools/safe-commit.sh`, **refuses any commit carrying a `*_PRD.md` whose `PRD_HEADER` declares
`step: 4` unless that file has a non-empty top-level `SURFACE MANIFEST` section.** No override. It
does NOT enforce the header block, the ENDPOINT section or `endpoint_outcomes` agreement at commit
time -- those three limbs still refuse only at L6 via `.tools/to-pipeline-gate.py` limb 5, unchanged.
Re-derive the blast radius on any fabric with `python .tools/prd-manifest-gate.py --census` (today:
205 tracked `*_PRD.md`, 8 step-4, **0 refused**). Second half of the same directive: the L4 author
now runs `comp-adversary compose <prd>` and lands a grid beneath the manifest --
`org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md` **section 9** is the worked example.

**`NFRA_REPORT`** (D12, site-z) is at **PRD v0.3** with twelve outcomes `FWD-1..FWD-12`, all bars
Andrew-confirmed, `status: RATIFIED`. Section 8 carries twelve engine rows `S1..S12`; section 9 the
adversary grid. `2.0.0_SA_COO~ZZ` has CUT L5 at `f060f2354e` -- twelve cells `RP-s-1..12`, round
widths 2/5/4/1 -- and goes to L6 next. **`RP-s-1` carries two expressibility gaps I ruled on this
turn** (msg 20595): both resolutions land at L5, and `DENY-BY-DESIGN` must be tested against the
Website blind before gap 1's `resolvable` field is built.

**`NFRA_OPSEC202609`** (D12) is at PRD v0.14 with 19 outcomes; `FWD-19`'s edge half is UNBUILDABLE
under `C-19` (no AWS-only route to an edge exists). Surprise row `Z-S151` is **ARMED and BLOCKING**
with `disarm_owner 2.0.0_SA_COO~Z`.

**`NFRA_IAMROLES202609`** (D12) has an L2 endpoint (8 outcomes, unconfirmed bars) and a relayable
brief-create handoff at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_NFRA_IAMROLES202609_BRIEF_CREATE_20260909.md`. It
has **no tree home** and is sequenced behind the other two per Andrew.

**Push state, MEASURED:** every commit above is **LOCAL**. `origin/SITEZ` reads `3054872f2b` by
`ls-remote` at 19:1xZ; HEAD is ahead of it. This seat does not push a shared branch (LD-0367/0368) --
`0.0.0_AB_MSTR~Z` integrates on Andrew's word.

---

## Next Steps

1. **[2.0.0_SA_COO~ZZ] L6 issuance for `NFRA_REPORT`** -- one issuance covering all twelve cells,
   fan-out from the chains in the decomp (max width 5, inside the cap of 8). Nothing is owed from
   this seat first.
2. **[2.0.0_SA_COO~ZZ] Test `DENY-BY-DESIGN` against the Website blind before building `resolvable`**
   -- rung 1 is YAGNI, and `C-19` may mean the ratified enum already carries it.
3. **[2.0.0_SA_COO~Z] Disarm or action `Z-S151`** -- `FWD-4` is graded complete and unsatisfiable.
4. **[0.0.0_AB_MSTR~Z] Push `SITEZ`** on Andrew's word; 14 commits from this seat are local.
5. **[ANDREW] The rule-bank drift needs an owner** -- 7 files / 8 sites at v1.2 against head v1.8,
   and `0.8.0_AE_CloudComp` is not seated.
6. **[ANDREW] `NFRA_IAMROLES202609` sequencing** -- its 8 bars are unconfirmed and it has no tree
   home; explicitly behind the other two by his word.
