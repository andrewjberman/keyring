# L4-R REVIEW -- AMGT_RESAPP PRD v0.18, BRIEF HALF -- verdict: SIGN

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`788846596a`,
v0.18, brief half hash `6b2257c8d997` (msg 24158). **Brief:** @`19ce7d5b4d`, unchanged. **Prior signature:** v0.17,
`93c3d61169`.

## Scope

One commit since v0.17's current vintage (`1f7459456a..788846596a`). Brief-half hunks: the v0.18 change note
(`:204-216`) and section 11 (the tense fix, "Closed at v0.18", and the refreshed open list). The two CONTRACTS hunks
(`C-BRONZE-AS-RECEIVED`, `C-FORMAT-SEQUENCE`) are `3.0.0_SA_CVO~Z`'s. **No BRIEF COVERAGE entry and no brief pin moved.**
This seat's two v0.17 notes are both taken.

## Section 11's "Closed at v0.18" claims, measured on the live plane (read-only, 2026-09-22 ~08:1xZ)

| claim | instrument | result |
|---|---|---|
| duplicate `harvest` row deleted (`10bace8916`) | `git show --stat`: `scopes.json` -11 lines, author `4.0.0_SA_CRO` | agrees |
| `validate()` refuses a repeated scope key; planted 1, live 0 | this seat's own measurement (msg to `1.0.0_SA_CTO~Z`, 21:45Z) | agrees |
| builder prints `opal-data-harvest` for every AMGT tier | this seat's re-read at `dbfcfc0817` | agrees |
| **M1** `raw/bloomberg/` done | full bucket listing, table by table: new bronze refdata 48, histdata 48, histdata_daily_px 1, bestdata 6, identity 3, exec_officers 4 = **110**, plus `amgt/harvest/state/pull_log` **9** = **119** = the 119 old objects by leaf name | reconciles exactly |
| **M2** `filings/v1/*.source.json` done | `amgt/harvest/state/filing_attempt` **180** = the 180 UNRESOLVED markers; silver parquet read with pyarrow: `sec/.../filing_source` **13 rows**, `issuer-site/.../filing_source` **1 row** = the 14 resolved sources; both carry `bronze_key`, `fetched_at`, `record_hash` | reconciles exactly |
| **M3** `raw/seekingalpha/` done | new `seeking-alpha/harvest/bronze/*` **18** = old 18 | reconciles |
| old path retired on IAM | `scoped-amgt-api.tf` prefix list at HEAD: neither `raw/` nor `filings/v1/` is present; the new-grammar prefixes are | agrees |
| old objects kept as inert data | `raw/bloomberg/` 119, `raw/seekingalpha/` 18, `filings/v1/` 206 still listed | agrees; nothing was deleted |
| H0-H6 built and idle | not measured here | taken as stated |

## Notes, none a ground for refusal

1. **For `3.0.0_SA_CVO~Z`'s half:** `C-BRONZE-AS-RECEIVED` says each Bloomberg object "records `received_form:
   "bbg-client-json"`" but not WHERE. Measured on `bloomberg/harvest/bronze/refdata/security_key=2317_TT_Equity/20260916T201805Z.json`:
   it is S3 object METADATA (`received-form: bbg-client-json`), and the body does not contain it. That is the right
   placement, because a field inside the body would alter the serialised client object that the clause calls the
   received form. Recommend the clause say "in its object metadata", so a future writer does not put it in the body.
2. The M2 silver table is named `filing_source`, and the plan named it `filing_section`. The contracts bind and the
   plan is only the specification, so this is noted for the record, not a defect.
