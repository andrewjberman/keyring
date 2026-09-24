# Lead Panel H03 preflight: input and mandate blocker

Owner 2.0.0_SA_COO~Y; 2026-09-24; B01/B09 H1-H4. Authority:
COO_Y_LEADPANEL.md@5e7f2a0cf5, CTO~Z message 25179. This Codex instance is AMGT;
the separate Claude IRPT instance is not adopted.

## Fresh baseline before any build, upload or deployment

LEADPANEL_BASELINE.json records AWS reads. capture_leadpanel_baseline.py is the
collector: no Lambda invocation, no vendor call, write_fn=None for local replay.
Host Arrow24 is NOT target-runtime compatibility proof.

- ZIP unchanged: 669924 bytes, SHA256
  23a7a2b5c688b73a914e5554694485f861b3ae93431e79fbd482e4d6f2068c76;
  Python3.12 x86_64, no layers, no environment keys, last modified Sep19.
- Actual role: amgt-resapp-chatter-axis-lambda-role; policies captured. The mandate
  omits -lambda in the name. Existing schedule ENABLED at cron(0 10 * * ? *) UTC.
- Sep23/Sep22 run lines: 2 rows, 191 considered, names_with_links=3, names_read=250.
  Fresh consistent table scan captures chatter pointers and rows.
- Gold's own latest-snapshot rule selects
  s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=2026-09-23/part-20260923T021320Z.parquet
  from three objects. SHA256
  0840908b5fb26577ec37a731b848fefda51bdfe97e9f9b8d55cfff327c017161.
  1596 rows, six securities: 1595 DENIED, one PARTIAL. These are source grades;
  DENIED means uncovered spans here, not an observed authorization denial.
- Reviewed source4dc4b667f3 maps DENIED to no_coverage. Real reader/producer replay
  for Sep24 over captured gold and freshly read universe resolves **0/191 required
  30-day windows**; partial=5557, no_coverage=173, denied=0. Both products FAILED,
  INCOMPLETE_GOLD_INPUT, zero ranked rows, pointer_written=false. No writer ran.
  IAM/source selection cannot manufacture the missing coverage.
- Six securities have gold day records. That is not six publication links:
  handler store_item_count-based names_with_links changes meaning on gold.
  A displayed 6/250 would not prove the requested link improvement.

## Contract and implementation mismatches

1. DEFAULT_SOURCE controls CLI only. The handler calls compute_chatter_axis with
   default legacy count_fn. Primary and bundled-universe fallback need the same
   explicit gold function; changing DEFAULT_SOURCE alone does not switch Lambda.
2. chatter_gate.TOP_N=10; producer calls rank_top_n(..., TOP_N). Universe-sized
   row_count proof conflicts with the ranking rule. No ranking widening is made.
3. chatter-axis-schedule.tf uses aws_lambda_function filename/filebase64sha256,
   NOT modules/yang-lambda or S3 metadata source_code_hash. Durability still binds;
   the mandate names a different deployment mechanism.
4. Canonical builder vendors jsonschema dependencies, not pyarrow. Its import
   closure covers lib.research/lib.opal_data_harvest, while gold needs Arrow and
   lib.opal_naming via harvest.store. Rebuild alone is not runtime readiness.
5. CLOUD at inspection57485eaae8 lacks the reviewed safeguards in4dc4b667f3.
   Coherent packaging must preserve those fixes, not blindly package trunk.

## Requested ruling and disposition

CTO~Z: correct TOP_N/denominator and deploy/role/selection descriptions; rule whether
to prepare an explicitly nonpublishing gold cutover with upstream coverage blocked,
or first name an authorized input remedy. No vendor authority inferred and no
admission rule relaxed. CVO~Z: independently capture/grade baseline and input blocker;
pre-build review requested02:51Z, no reply yet.

Ledger amgt-h03-leadpanel-y-20260924 opened before work with six legs; remains OPEN.
Canonical hold REFUSED because activation leg tf is unapplied; helper only permits
post-apply verification holds. No fake completion, sentinel hand-edit or bypass.
Preflight-blocked representation is a repository tool gap, not a half-landed cloud
deployment. Escalated with this blocker; no code change to the helper is attempted.

No ZIP build/upload/signing/deploy, runtime/source edit, retained-row rewrite,
producer emission, schedule change, vendor call or shared push. Evidence and ledger
are LOCAL pending MSTR integration. H1-H4 remain incomplete; COO~Z owns E0 separately.
