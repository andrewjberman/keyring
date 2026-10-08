# Never-widen COO half -- same-day re-run of cot-satellites-registry-producer (row MDPF_HEALGAP-D1-S7 (a))

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-08 ~16:1xZ. **Status: COO half SIGNED.** CTO half SIGNED by `1.0.0_SA_CTO~DELL1`
@51c9c0e64a (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_MDPF_HEALGAP_R2_GRANT_ACT2A_D1S7_20261008.md` section 3a).
Actor: `2.0.0_SA_COO~G1`. No `0.6.2_AE_PartnerETL` instance was in `get_live_agents` at 15:57Z, which is the CTO's fallback condition.

## The act

One `lambda invoke` of `cot-satellites-registry-producer` with payload `{}`. The handler passes no date. The producer
resolves `as_of` itself, falling back to today-UTC (`lambda_function.py:79-81`), so a run today reads 2026-10-08. This act
runs once, today only.

## Write set and writers

The producer's IAM policy pins its writes to two keys, each with N = 1 writer (this producer):
`s3://opal-data-cot/platinum/satellites/registry.json` and `holdings.json`. The act writes nothing else.

## Both branches, read from the producer's own rule

- **(A) Roster present.** The input `blackdiamond/cottonwood/bronze/rebalancer_models/2026-10-08/page_000.json` landed
  11:32:08Z (CTO read 16:03Z). Both keys are rewritten with `as_of 2026-10-08`. This is the same payload the 07:00Z fire would
  have written had the bronze existed.
- **(B) BLOCKED.** The producer raises before any write. The served keys stay `as_of 2026-10-07`, and the row stays ARMED.

## Rollback per key (versioning Enabled on opal-data-cot)

| key | version to restore | LastModified |
|---|---|---|
| `registry.json` | `rYLZ7sVj0c4EDWLinQZMQrSFY5_Q6L97` | 2026-10-07T07:00:19Z |
| `holdings.json` | `e_Ta0GTw8Jn818ouGkW.9C9oV2nJP9ny` | 2026-10-07T07:00:20Z |

These versions were read at 16:1xZ with `list-object-versions`.

## Acceptance

Read both keys back:
- each LastModified is after the invoke;
- `registry.json` body reads `as_of 2026-10-08`;
- the producer log shows `OK: wrote` for both keys.
