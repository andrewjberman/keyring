# The comparison identity read, for P's next window (CTO 102028 (1)): 4 read-only GETs, measured write set

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~19:0xZ. Scope: FWD-4's Comparison and Multi-Comp arms (IRPT_BCKEND_PRD.md:52).
Entitlement is **not** in this act: it is Andrew's word, carded at the CTO terminal (102028 (2)). Nothing that depends
on it is built.

## The act (on P's vendor session; P's installation, P runs it)

Exactly four GETs, one per catalogue entry. There is no retry: a refused read is recorded as refused.

| # | Request | Catalogue entry (`templates.json` comparison_catalog, candidate 20260923.v1) |
|---|---|---|
| 1 | `GET /securities/securities_info?securities=P%3A1728413` | opal_long_term, "Opal Long-Term" |
| 2 | `GET /securities/securities_info?securities=P%3A1728415` | opal_short_term, "Opal Short-Term" |
| 3 | `GET /securities/securities_info?securities=P%3A1728315` | opal_intermediate_term, "Opal Intermediate-Term" |
| 4 | `GET /securities/securities_info?securities=P%3A1728420` | opal_ultra_long_term, "Opal Ultra Long-Term" |

This is the research worker's own read (`docs/research/investor_reporting_ycharts_variants_20260911/variant_worker.py`,
`security_info`). It has no body, and makes no portfolio create, report create or other vendor write.

**Write set (what the window may touch):**
- the vendor: 4 GETs, 0 writes;
- the session lease row `_opal` in irpt-jobs, as on every session acquire;
- ONE evidence file, retained where P chooses (the packet names it):
  ```json
  {"retrieved_at": "<UTC>", "reads": [{"identity": "P:1728413", "status": 200, "content_type": "application/json",
    "waf_action": null, "login_destination": false, "body": <the response JSON, verbatim>}, ...]}
  ```
- Nothing else: no queue, no job row, no report, no catalogue edit.

Rollback: none needed for the vendor; the evidence file is additive.

Stop: a WAF challenge or a login destination on any read stops the act. The read is recorded as refused, and the rest
are not sent.

## The grade (Y, offline, after the window)

`live_walk/comparison_identity.py --catalogue <templates.json> --evidence <file> --out <record>`. It applies the
research worker's rules per entry:
- exactly one returned row carries the entry's `security_id`;
- its `security_name` equals the label;
- its `detailed_security_type` is `model_portfolio`.

Proved on shaped inputs (rc 0 only at 4/4):

| Arm | Result |
|---|---|
| all four answer as catalogued | IDENTITY 4/4, rc 0 |
| name drift / wrong type / duplicate row / WAF 202 | NAME_DRIFT, TYPE_MISMATCH, NOT_UNIQUE, READ_REFUSED; 0/4, rc 1 |
| one read missing, one stray id | NO_READ, `reads_outside_catalogue ['P:9999999']`; 3/4, rc 1 |

On 4/4, Y versions the catalogue with the evidence (sha, `retrieved_at`, returned name, type and instance id per
entry). Admission becomes identity-verified with entitlement pending. The served generate still refuses every
selection until Andrew's permission word and M's reviewed policy consumer land (`maintained_sources.py`
`resolve_comparison_fields`).

## Historical context (not current evidence)

- The Sep 11 research multicomp sent `P:1728415` and `P:1728315` (payload `security_ids`), and its receipt reads
  `comparison_names_verified: true`.
- Its PDF prints "Opal Short-Term" and "Opal Intermediate-Term" as Dynamic, Initial, inception Jan. 1, 2024.
- The comparison PDF prints "Opal Long-Term" the same way.
- The raw securities_info bodies were not retained, so no current identity follows from them.
