# 1.0.0_SA_CTO — session close 2026-08-20 1350Z -> 2026-08-21 0104Z

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), TRACE, COORDINATE, VALIDATE

Window: since `morning_reform_drain_1330-1350Z.md`. 16 commits, ~40 MCP dispatches handled,
0 deploys, 6 gates closed, 1 sovereign-instruction relay absorbed.

---

## What this window was

Andrew ran a full working day through this seat. Four substantive arcs, then a night of
gate/verify traffic:

1. **The Cottonwood supervised-AUM question, end to end** (Andrew-direct, Manav matter).
   Traced the `supervised` field from a recorded HAR to its source; corrected my own trace
   twice on other seats' evidence (the silent-drop set is **10 of 30**, not 6; and
   `$455,532,550` is `activeRelationshipAggregateResult.supervisedEmv`, NOT a "named-books"
   subtotal — my label came from arithmetic coincidence).
2. **The $8.5M BD-vs-our-plane gap, SOLVED at account level.** Reconciled
   **$8,516,957.24 -> $0.00 residual**; **91 outside-custodian accounts = 100.0%** of the
   supervised gap. Method note on the record: my first join was defective (a trailing-token
   key collapsed every multi-word account number to "Alts") and manufactured a **$19.8M
   phantom cohort**. It was caught **because the reconciliation refused to close**, not by
   review — rebuilt on mask-aware normalized keys.
3. **BD insurance surface -> DATA_BDINSURANCE PRD + registry + project.** qt6 ("BI Billing")
   identified as the never-ingested gap; two token authorities distinguished (`/Auth/Token`
   for DataMining/dashboard vs `/session/token` for insurance/account-api). PRD amended
   through sec.4.4.6 as Andrew narrowed scope to backend-only, tag-as-alternative. First
   cadence measurement reframed the project: **42 accounts / $41,559,989 flat, 0 stepped
   over 9 weeks**, incl. **$25,973,104 of supervised Voya** flat across the Q2 close —
   recorded **UNDETERMINED** (legitimate cadence vs stalled feed) with a named discriminating
   test, not asserted either way.
4. **NFRA_EPISTEMY registered** (Andrew-direct), coordinated with 4.0.0_SA_CRO; sibling
   relation to ATOM_LAYER0 written into BOTH project JSONs so no containment relation gets
   minted later. `/atom-layer0` + `/atom-decomp` skills + the `workflows/atom_layer0/` package.

---

## THE FINDING OF THE WINDOW — D4c TrueShares holdings arm is a NO-OP

Andrew deferred the D4 serving question + Phase-B scope word "against tonight's fetch read."
The 22:00Z fetch fired clean and the data is live (**111 of 114 holdings rows moved `shares`**
day-over-day). **But holdings coverage is 2 of 4 funds** — `source='trueshares'` rows: **0 of
114**, today and yesterday.

**Source-confirmed on the DEPLOYED ARTIFACT** (`CodeSha256 tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI=`;
member sha256 `f306aa23...` byte-identical to HEAD; both package members grepped), with in-file
positive controls so the instrument is shown to discriminate:

| token | count | |
|---|---|---|
| `TS_HOLDINGS_ENABLED` | 1 (`:381`, own assignment) | never branched on |
| `fetch_trueshares_holdings` | 1 (`:420`, own def) | never called |
| `fetch_filepoint` (control) | 3 | wired |
| `fetch_trueshares` (control) | 2 | wired |

**Why every check passed:** the deploy ledger's L5 bar was *"deployed package
`TS_HOLDINGS_ENABLED` > 0 AND `get-function-configuration` env shows =1."* **Both limbs are
TRUE — I re-ran both.** The bar **counted PRESENCE and was read as WIRING.** The discriminating
count is not the token's but the **call count of the function the flag enables**. This is the
**inverse** of the 2026-08-12 instance already in Rule 22a; the present-but-inert form is worse
precisely because it makes a presence check pass.

**Serving impact measured, and it reframes the call:** the live served surface
(`platinum/etf_ownership_dashboard.json`) has **zero** dependency on the holdings feed —
`holding`/`shares`/`cusip`/`nav`/`net_assets` all **0** occurrences in the served document.
So Phase B is a *"should we build the look-through"* decision, **not** a *"we are broken"* one.

**Not a gate.** Andrew's 0057Z standing egress already covers the pull; what is missing is a
call site, not a permission. Routed to the D4c lanes as ordinary work carrying a **behavioral**
acceptance bar (*does the holdings parquet carry `source='trueshares'` rows?*).

---

## Gates / rulings issued this window

| Item | Ruling |
|---|---|
| **freshguard-leg4 GO-conditions** | MARKER_CAS_* **alarm leg DROPPED** — and explicitly NOT on the moratorium: the alarm is *structurally blind to IGNORED* (an always-succeeding CAS is telemetry-identical to a working one). Dropped for a reason that survives the moratorium lifting. |
| **freshguard probe mechanism** | **PARK.** Rule-1 carve-out REJECTED outright. Version-introspection option REJECTED because it is *structurally silent on IGNORED* — the verdict the probe exists for. (a) is the right mechanism but the **probe's verdict expires faster than the hold**, so it is taken at fix-time, not banked. Mechanism pre-selected so nobody re-litigates it later. |
| **Precondition_Token 0.1 arch gate** | **PASSED**, read at source. Both binding conditions discharged: rung 4 does not degrade (`StopAndSurface` on `ParamValidationError`, no lock table); m4 fires visibly, reproduced at a second seat. Concurred with base's C1 and **added the load-bearing reason** — the ABSENT sentinel welds the object to S3's idiom on a leg built class-agnostic. Mutation hooks checked: zero production call sites, and recorded as the *correct* tradeoff (a battery mutating a copy proves nothing). |
| **C3-IDENTITY rider recompile** | **Gate STANDS, no re-gate** — the object did not move; only the consumed envelope's `plane`/`substrate` did. Contributed test **14c**: the maintainer's mutant (reach inferred from plane) must be discriminated on the TrueShares specimen. |
| **NEVER#3 leg, D_04 rename** | **PRE-DISCHARGED.** Published my sign-off bar ahead of the deploy act rather than at the gate — *a sign-off whose bar is revealed only when asked for IS a hidden hold*. |

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `TS_HOLDINGS_ENABLED`, `target_state_digest`, `unreconciled_aua`, `header_metrics` | PASS | BAND separation did real work — `[DEF]` vs `[DOC]` immediately separated the def-only flag from its 11 doc mentions. DENOMINATOR line used as the frame every time. |
| `safe-commit.sh` | 2 commits this sub-window | PASS | risk-reflex CLEAN, measured (1 file vs 1,817 danger nodes). |
| `aws lambda get-function` / `get-function-configuration` | etfs-netassets-daily, opal-globgrph-incremental-updater | PASS | APPLIED-plane truth; package downloaded and read rather than inferred. |
| `s3api head-object` vs `s3 ls` | one object, both tools | PASS | **The control that caught my own error** — see Gap. |
| boto3 paginated walks | opal-data-etfs (741), trueshares/ (368), platinum/ (13) | PASS | Materialised client-side; never a `--query length()` over a page. |

**What worked:** the in-file **positive control** pattern (grepping a known-wired function beside
the suspect one) is what turned "the token appears once" from a suspicion into a finding — a bare
count of 1 proves nothing without a 2-or-3 beside it.

**What failed:** nothing tool-side. Two of MY OWN readings failed and were caught by controls.

**Gap found (mine, not the tools'):** my pre-fetch baseline recorded historical 18:00 stamps as
"prior-cadence residue, not a second producer." That was the **`aws s3 ls` local-time trap** —
proven on one object, they were 22:00Z all along. Had it survived I would have reported a phantom
cadence change on a healthy producer. **The same trap re-fired inside this very log**: my
`git log --date=format:'%H:%MZ'` rendered LOCAL time under a `Z` label. Caught before writing.
*Twice in one window, two different tools — the offset does not announce itself.*

---

## Corrections I made against myself this window

1. **The $19.8M phantom cohort** — defective join key; caught by a reconciliation that refused
   to close, not by care.
2. **Silent-drop set 6 -> 10 of 30** — I had enumerated columns I recognised from an output diff
   instead of diffing the declared list. Corrected on 0.2.0's evidence.
3. **`$455,532,550` mislabelled** as a named-books subtotal; it is `supervisedEmv`. My label came
   from arithmetic coincidence — the number matched, so I stopped looking.
4. **The `s3 ls` local-time baseline note** (above).
5. **"18 plus 5"** — CVO's count delta on the header_metrics shapes. Re-measured at set level:
   16 shared + **7** INF-only + **2** bd/cot-only. Ruling unchanged; the *characterisation* would
   have licensed a false "INF is a superset of the archetype" inference later.

---

## Current State (for a reader with zero context)

- **D4/D4c:** `etfs-netassets-daily` fires `cron(0 22 * * ? *)`, ENABLED, healthy. Silver lands
  in `opal-data-etfs/silver/{holdings,netassets}/{date}.parquet`; bronze lands in
  **`opal-data-assets`** under the monolith grammar (`BRONZE_BUCKET=opal-data-assets`,
  `BRONZE_GRAMMAR=monolith`) — **there is no `bronze/` prefix in `opal-data-etfs` at all**, so a
  census there returns a clean, confident, wrong zero. TrueShares holdings capability written
  (`fetch_trueshares_holdings`, `lambda_function.py:420`) and **unreachable**.
- **NEVER#3 / D_04 rename:** live `platinum/firm/header_metrics.json` `total` blocks measured —
  bd 18 keys, cot 18 keys (identical sets), inf 23 keys with `unreconciled_aua` PRESENT. The
  field is INF-only, outside the frozen archetype. Deploy act must state RENAME (remove old, add
  new, no dual-key window); I sign against that shape.
- **NFRA_EPISTEMY:** C3-IDENTITY closed + rider-conformant @d652c88490; C10-PRECOND complete,
  build-staging only, no activation; C2-ATTEST GO issued by COO; C4-LEASE + R1-RARITY staged.
- **Merge:** MSTR ran `/integrate` leg 1 (CLOUD <- SITEZ) 0051-0055Z, zero conflicts. My lane was
  clean throughout (staged set empty); commit act held and released on the CLOSE frame.

## Blockers

**None.** Nothing at this seat is blocked or waiting on another agent.

## Next Steps

- **[ANDREW]** Tomorrow morning: the D4 fetch read at his terminal -> the serving question + the
  Phase-B scope word he deferred ~1425Z. Both halves ready: the defect AND the fact it costs
  nothing served.
- **[ANDREW]** Two carried calls: insurance HEAVY-route advisor-demand decision; yes/no on folding
  tonight's BD insurance findings into `data/black_diamond/API/domains/insurance/` (REC: yes).
- **[0.6.2 / 0.2.0]** FRI 11:30Z Cottonwood G4/G4b acceptance belt.
- **[0.4.0_DS_ClientPlatform]** (queued, no live session) D4c wiring — the call site, under the
  existing standing egress, with the behavioral bar.
- **[2.0.0_SA_COO]** When the D_04 rename TO reaches its deploy step, my never-widen sign-off is
  a two-line mechanical check against the stated shape.
- **[1.0.0_SA_CTO]** FRI 13:30Z PB-1 proof-read before flip -> same-day PROD promote.
