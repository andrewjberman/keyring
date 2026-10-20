# Review: IRPT_ANLREQ PRD v0.27 @cd00de4ecb, brief half (4.0.0_SA_CRO~TCKT, 2026-10-20 ~17:3xZ)

The diff `62631269b7..cd00de4ecb` on the PRD is 24 insertions and 2 deletions. It changes the version line and the
C-AUDIT-RECORD row, and adds addendum v0.27. The ENDPOINT is byte-unchanged.

## Against Andrew's words and this seat's records

| Term | Andrew (record @f2581e90b9, memo @9de85135f0) | v0.27 row |
|---|---|---|
| What | "formalize a structured JSON for that audit reporting and for that audit logging" | One audit JSON per request with a published JSON Schema (AnalysisAudit.v1) that a consumer rejects a malformed record against |
| Where | "an analysis-report folder in each firm's bucket ... using lgic naming standards" | In each firm's bucket, at a builder-made address; the table is `analysis_audit` |
| Retention | not stated | 2,555 days from filing, no unreferenced expiry; the row says Andrew's word changes it |

## The one place the wording moved, and why it is sound

His folder name "analysis-report" becomes table `analysis_audit`. The builder already uses `analysis_reports` for the
analysis table (`opal_naming.py:2605`), and LGIC names come from the builder (rule 30). His operative terms all hold:
each firm's bucket, LGIC-named, a structured record. The name change is reported to him in this seat's next update. It
is not a refusal.

Writing the record at attach time (the packager) is the one hop holding all four linkages (ticket, form as filed,
filer, package and commentary pointers). That matches the item this seat routed (@15cfc42950).

Verdict: SIGN.
