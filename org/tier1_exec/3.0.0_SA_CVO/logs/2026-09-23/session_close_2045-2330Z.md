# 3.0.0_SA_CVO~Z -- session close 2045-2330Z, AMGT: L4-R cycle, cutover acceptance, incident reach

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), DIAGNOSE, TRACE

**Window:** 2026-09-23 ~20:45Z (respawn) -> ~23:30Z. **21 commits.** Prior log:
`session_close_1815-0700Z.md`.

## SUMMARY

Respawned onto three named bottlenecks and cleared all three, then took the incident's second
remedy half, which was named as owed mid-session.

- **GATE 1 (AMGT_HARVST L4-R ratified-text half): CLOSED.** Five amendments, three refusals, three
  signatures. PRD now `ADMITTED`, both halves current at `fa4257b65ca7` @`3659741074`.
- **GATE 2 (served-output cutover): CLOSED.** Review issued PASS-with-C1-blocking; after the lane
  deployed correctly, **C4 executed and PASSED on the deployed bytes**. C1, C2, C5 discharged.
- **GATE 3 (closer CONTRACT v1.0):** s.3 departure **upheld** with two residuals; **all pinned
  candidates graded** (H `1b6cd9d4e0`, reader delta `4dc4b667f3`, B08 `4599b05795`).
- **INCIDENT SECOND HALF:** realised reach **measured and final** at five served responses, one
  security, one client IP -- over the **full measurable history**, not just the named window.

## WHAT WAS FOUND (the substance)

**R5 -- the finding that mattered.** The ratified text approved relabelling **1,595 of 1,596 rows**
`DENIED -> NO_COVERAGE` while asserting it "needs no writer change" and "no investigation is
required." `pool_reader._GOLD_DAY_STATE_MAP` carries no `NO_COVERAGE` key and `:707` skips unknowns
via `.get()`. Exercised with a positive control: **`complete` flips False -> True on the same row,
only the label changed.** A genuinely uncovered window would have been reported to every caller as a
clean read. Now bound as a **condition** of the migration.

**H-a -- found while grading a different candidate.** The fix the PRD then ratified named the
**counter** and was silent on the **score**, so a conforming implementation would still have dropped
those 1,595 days out of `counts` entirely. R5 served a silent clean read; H-a served a silent gap.
Both closed permanently once the reader was made label-blind.

**C1 -- the cutover finding.** Neither never-widen half named the deploy mechanism.
`opal-amgt-scoped-api` is Terraform-managed and `modules/yang-lambda` derives `source_code_hash`
from the **S3 object**, so the artifact of record is the S3 key. Changing the function without it
would have left the next unrelated `terraform apply` silently restoring the defective package.

**Incident reach.** 521 AMGT requests in the rk-41 window, 423 refused 401. Of 21 served thesis
responses only **BA_US_Equity** was in the drafting corpus: **4 responses + 1 overlay, one client
IP.** Widened to the full log history (09-03 -> cutover, 2,222 more files): **adds zero.**
**"179 sentences served" is the defect's CAPACITY, not its realised reach** -- ratified as R-11.

## COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "deployed CodeSha256/RevisionId of opal-amgt-scoped-api" | PARTIAL | Returned 3 tied graph-plane candidates; the question needed the LIVE plane, so routed to the AWS API instead. Correct behaviour, wrong plane for the need. |
| `comp-routes trace` | `/api/scoped/amgt/security/BA_US_Equity/thesis` | PASS | Resolved CloudFront behavior -> APIGateway-portal origin + `auth-validator-edge` viewer-request. DESIRED plane, disclosed as such by the tool. |
| comp rail (`comp-tool-hud`) | raw `aws apigatewayv2 get-apis` | **GATE FIRED, CORRECTLY** | Denied and routed to `comp-routes`. The rail was right: `comp-routes` gave the serving path plus the CF custom-error masking a raw call would not surface. |
| `prd_signoff_lib` | `half_hashes` / `top_sections` direct | PASS | Used every round to measure half hashes and section routing independently of the author's claims. |
| `.tools/prd-signoff.py` | `status` / `refuse` / `sign` | PASS | 3 refusals + 3 signatures stamped; `status` is the one read of what is owed. |
| `.tools/surprise-row-gate.py` | via `safe-commit` | **REFUSED ME TWICE, CORRECTLY** | See "What failed" below. |
| `owned-paths-validate.py` | `resolve_lane` / `check_agent`, driven directly | PASS | Settled the s.3 departure on measurement rather than inference. |

**What worked.** Driving library internals directly (`prd_signoff_lib`, `owned-paths-validate`,
`pool_reader`) rather than reading code and reasoning about it. Every material finding this session
came from **exercising** an object, not from reading it. The C4 acceptance and the R5/H-a findings
are all direct-invoke results.

**What failed (mine, not the tools').**
1. **I invented two enum values.** `hazard_standing='DISARMED'` and `disposition='REMEDIATED'`,
   neither in the ratified enum, plus the CVO as `disarm_owner` which R-19 bars. **The gate caught
   all six violations and was right on every one.** I hold a banked lesson saying to read the
   disposition enum before typing one and did not apply it.
2. **`git log --since` read my UTC bound as LOCAL time.** `%cI` prints `-04:00` here, so
   `--since="20:45"` returned **0 commits** for a window containing 21. The zero was the tell.
3. **A `json.dumps` fix re-serialised a whole 561-row file** (123 insertions / 99 deletions) when
   one row was added. Verified semantically identical before reporting; disclosed rather than left
   to be found.
4. **First CloudFront parse read 0 rows across 664 files** -- those logs carry a bare
   space-separated header, not `#Fields:`. Only the positive control (19,114 rows) made the later
   zeros trustworthy.

**Gap found.** No instrument in this estate can attribute a request on `/api/scoped/amgt/*` to a
**firm**: the firm header is injected by `auth-validator-edge` **downstream** of the CloudFront
access log, API Gateway access logging is not declared, and the Lambda log carries no route and no
firm on a successful request. Route and client IP are reconstructable; firm is not. Filed as
`AMGT_RESAPP-Z-S238`, ratified as **R-11a**.

## MCP TRAFFIC

~30 messages handled, all acked. Significant: GATE 1 refusals/signatures (6 sends), the s.3
departure ruling, the cutover review + C1 blocker, C4 acceptance, the incident reach measurement and
its window addendum, and 3 surprise-row notifications. **One send REFUSED by the L8 correspondence
guard** (direct to `2.0.0_SA_COO~Z`) -- correct, and I flagged the owed relay rather than letting the
gap read as delivery.

## FILES MODIFIED

See commit messages: `59d833bd88`, `60dde3b252`, `f0d533e084`, `6f8958909a`, `031fee04bc`,
`da1a8c583b`, `94a817c8a8`, `2191738f38`, `27549bd865`, `4cb1b6b009`, `c9d862dd9c`, `65132a45c7`,
`39cd826599`, `8e5612576b`, `3e33937f78`, `73259627c4`. All under
`org/tier1_exec/3.0.0_SA_CVO/deliverables/` plus the AMGT_RESAPP surprise channel.

⚠ **One commit (`39cd826599`) carried a FOREIGN ROW** (`AMGT_RESAPP-Z-S237`, by
`0.1.0_DE_MarketIntelligence`) under the audited `surprise-row-override`. It sat uncommitted in the
shared tree and was blocking every later append. Carried at its author's exact bytes, nothing
edited, disclosed to `1.0.0_SA_CTO~Z` in the same turn, and **ratified** by that seat.

## BLOCKERS

**None owned by this seat.** Nothing offered to it is ungraded and no discriminator it can run is
outstanding.

**Held elsewhere, evidence-cited:**
- **The remediation ACT** on the 4+1 responses is **Andrew's by class** (outward-facing) and is
  correctly held for his return, not escalated mid-break. It turns on who the client was, which no
  instrument here can determine.
- **`E0` / the live product thread** remains **UNGRADED** for want of a captured authenticated
  trace. C4 is a **backend** acceptance by direct invoke, not a browser trace, so under CONTRACT
  s.2 `H1`-`H4` and `C1`-`C3` stand `NOT_EVALUATED`.

## CURRENT STATE (for a reader with zero prior context)

- **`AMGT_HARVST` PRD** `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`: **ADMITTED**.
  ratified-text SIGNED @ `fa4257b65ca7` (pin `3659741074`), brief SIGNED by `4.0.0_SA_CRO~Z` @
  `12aa73e8bb31` -- **byte-unchanged across all five amendments**, so the CRO signature was never
  re-opened. Clauses 1-6 of `C-HV-DAILY-STATUS` are ratified in **TEXT only**;
  `pool_reader.py` at HEAD still carries the two-key map, which is correct under clause 4's ordering
  since `publication_gold.py:579` still writes `"DENIED"`.
- **`opal-amgt-scoped-api`**: live `CodeSha256`
  `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`, CodeSize 807,904, deployed 22:02:35Z via
  `safe-apply`. S3 artifact of record `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
  ETag `cb90ed8636c79c9dbc29120923349bc5`, VersionId `ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe`, uploaded
  21:58:26Z -- **before** the apply, which is what shuts the incidental revert path.
- **Served state, measured live:** 12/12 securities HTTP 200, **210 served / 179 held / 389 total /
  ZERO spanless served**. Per-security figures match `REPAIR_REPLAY.json` exactly on all four
  securities it pins.
- **Incident:** guard built, deployed, exercised; reach measured and final. **NOT CLOSED** -- the
  remediation act is outstanding and is Andrew's.
- **Surprise channel** `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md`:
  562 rows. Mine: **S238** (attribution blindness, ARMED), **S239** (500s historical, INERT/GRADUATED),
  **S240** (no stranded portal commit, INERT/GRADUATED).

## NEXT STEPS

1. **[Andrew]** The remediation act on 4 `BA_US_Equity` thesis responses + 1 overlay, one client IP,
   2026-09-22 19:15Z - 2026-09-23 20:44Z. Carded at `1.0.0_SA_CTO~Z` as R-11b. The set is **final**,
   not provisional -- the widened census closed that.
2. **[2.0.0_SA_COO~Y]** Clauses 1-6 are ratified text and the reader delta `4dc4b667f3` is graded
   PASS, but neither is merged or deployed. Clause 5 (score preserved) and clause 6 (relabel
   invariance) are the two a later tidy-up would most easily undo.
3. **[2.0.0_SA_COO~Z]** `E0` needs a **captured** authenticated trace; an operator sentence is not
   one of the contract's three instruments. This seat holds no captured trace and publishes none.
4. **[3.0.0_SA_CVO~Z, successor]** Nothing owed. If the incident's remediation act lands, grade it;
   if `E0` produces a captured trace, `H1`-`H4` and `C1`-`C3` become gradable for the first time.
