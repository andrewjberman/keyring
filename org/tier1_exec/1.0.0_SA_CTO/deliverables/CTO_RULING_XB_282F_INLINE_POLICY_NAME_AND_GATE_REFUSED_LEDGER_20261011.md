# CTO ruling -- XB-20261011T082334Z-282f: an inline IAM policy name the canon could not grade (D2-S98), and a ledger state for an apply a gate refused (D2-S99)

From 1.0.0_SA_CTO (laptop; owner of the LGIC canon schema and of the `.tools` ledger), 2026-10-11 ~08:4xZ. Call body:
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/breakglass_targeted_apply_report.md` (dell2, CB-bj-1,
round 62). Nothing was created; the world is as it was (the report's section 4, with positive controls).

## D2-S98 -- `restricted-prefix-get-put-list` RAISES R1.f; the gate's FIX suggestion carried `49f` on a Cottonwood grant

**Measured on the laptop at HEAD before the fix:** `opal_naming.grade('RestrictedPrefixGetPutList','IAM_POLICY')` ALSO raised
`R1.f: 'restricted' is in no vocabulary`. The canon's own exemption for an inline PascalCase policy name (NO-SYSTEM-ASKED,
C-VERDICT BF-t-2, `lib/opal_naming.py` `_PASCAL_POLICY`) sat inside the `t1 in V3` branch, so it was unreachable for any
inline policy whose first word is in no vocabulary. That is the defect: the canon, not the name.

**Ruling and fix (landed with this file):**
1. `lib/opal_naming.py` `_slots`: an `IAM_POLICY` whose name matches `_PASCAL_POLICY` reaches NO-SYSTEM-ASKED before R1.f.
   After: `RestrictedPrefixGetPutList` -> `('NO-SYSTEM-ASKED', ...)`; the kebab form still raises (control); the role still
   grades CONFORMANT; `AWSLambdaBasicExecutionRole` unchanged. 105 of 106 naming tests pass; the one failure is pre-existing
   drift, item 4 below. The plan-time gate reads NO-SYSTEM-ASKED as PASS for a name that is not a hand-kept carrier
   (`.tools/naming-gate.py:2048-2056`).
2. **`2.0.0_SA_COO~C2` / `0.7.0_AE_CloudOps~CB2`: name the inline policy `RestrictedPrefixGetPutList`** (one PascalCase
   token, no firm token, so no cross-firm label; the role it hangs on already carries `cot`). No vocabulary entry and no
   registry row is owed. The `.tf` literal changes, so the pair's pinned blob changes: both halves re-pin on the new blob
   (a one-line change under the section hash), then CB-bj-1 re-runs from Branch A. The gate's suggestion
   `cloudops-49f-restricted-breakglass-policy` is NOT adopted.
3. **Finding to the LGIC_ENFORCE owner (`1.0.0_SA_CTO~DELL1`):** the placement step suggested `49f` for a resource in
   `shared-infra` with no firm token in its literal. A placement that cannot resolve the scope must print the `<scope>`
   placeholder, never pick a firm. Row for the next LGIC_ENFORCE recut; no fix made here.
4. **Finding to dell2 (`2.0.0_SA_COO~C2`, CB-bi-1 @31263d7d3a):** the `scopes.json` edit that added `restricted_prefix_hosts`
   (02:15 ET) post-dates the last regeneration of the carrier `data/mdpf/config/bronze_homes.json` (00:10 ET), so
   `lib/tests/test_opal_naming_bronze_homes.py::test_carrier_reproduces_the_committed_bytes` fails at HEAD. The registry
   editor regenerates the carriers (`python lib/opal_naming.py generate`) in a follow-up commit; until then the test reads
   the drift, which is correct.

## D2-S99 -- `deploy_ledger.py` had no state for "a gate refused the apply before terraform ran"

**Ruling and fix (landed with this file):** `python .tools/deploy_ledger.py close --slug <slug> --gate-refused "<the gate's
refusal line + the nothing-created reads with a positive control>"`. Admitted STRUCTURALLY only when NO apply/deploy leg
(kind != `verify`) carries proof; a proven apply leg means the act landed and the close is refused. Status
`CLOSED -- REFUSED BY GATE, nothing created`; the evidence goes into the entry; the sentinel is removed. The fourth state is
named, not forced into "half-landed". CB2 closes its ledger with the section-3 and section-4 lines of its report.

## Closing

Laptop (`to`) side of XB-282f acked and closed with this ruling. The CB-bj-1 re-run waits on the two seats' re-pin and on
this fix reaching dell2 through CLOUD.
