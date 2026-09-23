# CVO C4 POST-DEPLOY ACCEPTANCE -- `opal-amgt-scoped-api` no-span HOLD repair

**`3.0.0_SA_CVO~Z`, 2026-09-23 ~22:1xZ.** Executed and graded by this seat on the **DEPLOYED BYTES**.
Closes the battery owed by `AMGT_SCOPED_API_CUTOVER_REVIEW_20260923_Z.md`@`031fee04bc`.

## VERDICT: **C4 PASSES. C1, C2 AND C5 DISCHARGE. THE SERVED-OUTPUT INCIDENT IS REPAIRED ON THE DEPLOYED PLANE.**

**179 sentences that were being served in violation of `C-VERBATIM-GATE` v0.12 are now HELD**, measured
live against the deployed function, not replayed.

| condition | verdict |
|---|---|
| **C1** deploy mechanism -- S3 key then `safe-apply` | **DISCHARGED** |
| **C2** artifact durability | **DISCHARGED** |
| **C3** pre-deploy remeasure (`CodeSha256` + `RevisionId`) | **SATISFIED** |
| **C4.1** deployed hash + S3 key holds candidate bytes | **PASS** |
| **C4.2** all twelve served GETs, 210 / 0 spanless | **PASS** |
| **C4.3** missing-firm 401 + negative control | **PASS** |
| **C4.4** both overlay controls | **PASS** on the fail-closed property; positive description path **NOT_EVALUATED** |
| **C5** change-management ledger | **DISCHARGED** |

## 1. C1 AND C4.1 -- THE DEPLOY TOOK THE ROUTE THIS REVIEW REQUIRED

Measured by this seat on the live planes, not taken from the deploy receipt:

| object | measured | required by C1 |
|---|---|---|
| Live `CodeSha256` | `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` | the signed candidate -- **MATCH** |
| Live `CodeSize` | 807,904 | `candidate.zip` bytes -- **MATCH** |
| S3 `research/opal-amgt-scoped-api.zip` ETag | `cb90ed8636c79c9dbc29120923349bc5` | **the exact MD5 this review named** -- **MATCH** |
| S3 `ContentLength` | 807,904 | **MATCH** |
| S3 `LastModified` | **21:58:26Z** | upload FIRST |
| Function `LastModified` | **22:02:35Z** | apply SECOND |

⭐ **The ordering is the part that mattered and it is correct**: the artifact of record was updated
**before** the function, so Terraform's `source_code_hash` and the running code agree. **The incidental
revert path C1 was written to close -- an unrelated `terraform apply` silently restoring the defective
package -- is now shut**, because the S3 object no longer holds the defective bytes. Reported route was
`safe-apply`, exit 0, `0 added, 1 changed, 0 destroyed`; the measured end state is consistent with it.

**C2 discharges in the same act.** The artifact now exists durably in S3 at `VersionId`
`ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe`, so the single-copy-in-a-temp-directory exposure is closed exactly
as the addendum predicted it would be -- *"the artifact of record and the durable copy are the same
object."*

## 2. C4.2 -- ALL TWELVE SERVED GETS. **210 / 179 / 389 / ZERO SPANLESS**

**Instrument:** direct `lambda invoke` against `opal-amgt-scoped-api` with a synthetic API Gateway v2
event, one call per security, route `GET /api/scoped/amgt/security/{security_key}/thesis`, firm header
present. **This exercises the deployed package and the real S3 data plane.** Served sentences counted by
walking `drafted_sections[].sentences[]`; a *spanless served* sentence is one reaching a caller with an
empty `quoted_spans`.

| security | status | served | `held_no_span` | spanless served |
|---|---|---|---|---|
| ASML_NA_Equity | SERVED | 2 | 8 | **0** |
| BABA_US_Equity | SERVED | 34 | 2 | **0** |
| BA_US_Equity | SERVED | 17 | 21 | **0** |
| COST_US_Equity | SERVED | 15 | 24 | **0** |
| HAL_US_Equity | SERVED | 11 | 7 | **0** |
| HD_US_Equity | SERVED | 20 | 16 | **0** |
| INTU_US_Equity | SERVED | 26 | 14 | **0** |
| KMB_US_Equity | SERVED | 18 | 21 | **0** |
| NU_US_Equity | SERVED | 8 | 19 | **0** |
| PBR_US_Equity | SERVED | 16 | 13 | **0** |
| SAP_GY_Equity | SERVED | 30 | 8 | **0** |
| VLO_US_Equity | SERVED | 13 | 26 | **0** |
| **AGGREGATE** | **12/12 HTTP 200** | **210** | **179** | **0** |

**210 + 179 = 389, reconciling exactly to the historical census.** ⭐ **And the four securities for
which `REPAIR_REPLAY.json` carries per-case figures -- ASML 2/8, BABA 34/2, BA 17/21, COST 15/24 --
MATCH THE LIVE RESPONSE EXACTLY.** That is the discriminator: **the offline replay and the deployed
function agree per-security, not merely in aggregate**, so the totals are not two different
distributions summing to the same number.

⛔ **THE WHOLE POINT, STATED PLAINLY: `spanless served` is ZERO on every one of the twelve.** The
incident was 179 no-span sentences reaching the served surface. They are now held at read, and the
count of those held is exactly 179.

## 3. C4.3 -- MISSING-FIRM 401, WITH A DISCRIMINATING NEGATIVE CONTROL

| probe | result |
|---|---|
| thesis route, **`x-firm-id` ABSENT** | **HTTP 401** -- *"missing edge-injected X-Firm-Id: request did not pass auth-validator-edge"* |
| **`x-firm-id` present**, bogus route under the same prefix | **HTTP 404** -- *"no /api/scoped/amgt route for ..."* |

⭐ **The control discriminates, and it is stronger than the API-Gateway-layer version.** At the edge,
the CTO measured a nonexistent path returning the *identical* 401, which shows only that auth fires
before path resolution. **At the Lambda, a bogus route with the header present returns 404, not 401 --
so the 401 is demonstrably about the missing header and not a blanket refusal of everything.** The
firm gate fails closed exactly as `_firm_id` documents.

## 4. C4.4 -- BOTH OVERLAY CONTROLS

| probe | `description` |
|---|---|
| `BA_US_Equity` overlay | `status=ABSENT`, `text=null`, `source=null`, `marked=null` |
| `ASML_NA_Equity` overlay | `status=ABSENT`, `text=null`, `source=null`, `marked=null` |
| `NOSUCH_XX_Equity` (negative control) | `status=ABSENT`, `reason="identity UNRESOLVED -- no description was read"` |

**PASS on the property the control exists to test:** the overlay description fallback -- the second
production consumer crossing the repaired reader -- **serves no prose at all**, so no unverified text
reaches it. The negative control carries a **different `reason`** from the real securities, which
discriminates an unresolved identity from a resolved one with nothing to serve.

⚠ **LIMIT, STATED RATHER THAN GLOSSED: the POSITIVE description path is NOT_EVALUATED on the live
plane.** No live security currently has a description to serve, so this seat has exercised
"serves nothing unverified" and **not** "serves correctly when there is something". ⛔ **And this seat
holds NO pre-deploy baseline for the overlay description**, since the previous package is gone -- so
`ABSENT` is **not** claimed here as unchanged-by-the-repair. It is consistent with the CTO half's own
s.6, which states the raw-D1 evidence-input posture is a separate upstream follow-up and is **not**
claimed repaired.

## 5. C5 -- THE LEDGER

`org/critical_paths/change_management/20260923T215256Z_amgt_exact_nospan_C1_cutover.md`:

- **Opened 21:52:56Z** -- *"before any cloud write"* -- which precedes the S3 upload (21:58:26Z) and
  the apply (22:02:35Z). **The NEVER-2 ordering is satisfied.**
- **CLOSED 22:03:28Z** at HEAD, executor named, opening commit `b0f33e7821` cited.
- ⭐ **It correctly scopes itself:** *"C4 runtime acceptance remains pending separately."* **The
  ledger did not claim the acceptance this document supplies**, which is the distinction that keeps a
  deploy receipt from reading as a grade.
- Read across **41 live worktrees** per NEVER-2's union rule rather than from the shared tree alone.

## 6. WHAT THIS ACCEPTANCE DOES **NOT** COVER

- **`E0` and the live product thread remain UNGRADED.** This is a **backend acceptance on the deployed
  package**, reached by direct invoke. It is **not** an authenticated browser trace, and under
  CONTRACT v1.0 s.2 *offline and backend closures grade nothing until `B00`/`E0` passes*. **`H1`-`H4`
  and `C1`-`C3` stand NOT_EVALUATED.**
- **The API Gateway edge is not exercised here.** The firm gate was tested at the Lambda boundary; the
  CUSTOM authorizer in front of it was not.
- **Raw-D1 posture, machine-empty print prose, portal rendering of the new counters, and human viewing
  of the served sentences remain UNMEASURED**, exactly as both halves of the pair state.
- **The `no_coverage` reader work is unrelated to this package** and did not enter this ZIP, as the
  executor states and as the unchanged `CodeSha256` confirms.
- This seat re-ran **neither** lane's test suite; the grade rests on the live invokes above, which are
  a different instrument.

## 7. ONE OBSERVATION WORTH KEEPING

⭐ **THE PER-SECURITY MATCH IS WHAT MAKES THIS AN ACCEPTANCE RATHER THAN A COINCIDENCE.** An aggregate
of 210 could be produced by many different distributions; four independently-pinned per-security pairs
reproducing exactly on the live plane could not. **When a replay and a deployment agree in total, ask
whether they agree row by row** -- the aggregate is the weaker claim and it is the one usually
reported. COST: the per-case figures were already in the replay JSON. NON-APPLICATION: evidence that
carries no per-member breakdown, where the aggregate is all there is.
