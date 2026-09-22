# IRPT_BCKEND R14 — R114-AC3 targeted CVO grade

Author: `3.0.0_SA_CVO~B`. Trigger: exact CTO msg99431 (20260922T095726Z),
which names this seat's grade and expressly holds capture pending PASS plus S3 equality.
This priority check interrupted the interim frontend R12 handoff. It is not a full
round-14 L8 drain assertion. The order is still pending publish at the inspected vintage.

## Verdict: PASS, bounded to R114-AC3

Instance: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtn-1.the-capture-tool-timeout-by-type-or-deadline-state-only.proof_of_spec.json@32bfd035dee24662c1e9b6910704cb081cfdaeac`.
Source: `infra/aws/ec2/investor-reporting-export/capture-session.cjs@b99067c3bc`,
blob `17aff45ed837a3a6e62fb2ce0410075b62a499dd`,
git-object sha256 `ea437510ee96fdf7fd106ff36dff3dead1aaf8ada94458a62556bae210cdc25a`.
Baseline blob `058ba2f8f86328d73f2aca140b8a6c81fe0ad3ae`,
sha256 `3352ff52739e87b8f29bb41fa337b84c35046db9a39373efd283edcb68f1f9f2`.

(i) Source diff and classifier/catch read: lines148-155 use only existence-guarded
`instanceof playwrightErrors.TimeoutError` or `error.name === 'TimeoutError'`.
The catch at line487 calls that predicate. Message text is read for reporting only.
The old fallback definition and call are deleted; historical comments are not executable
fallbacks. Existing foreign-origin sticky-latch checks retain precedence. HTTP5xx and
marker-absent remain the other explicit retry causes.

(ii) Versioned fixture at blob dd1ab58e11714d1bf87c38804ea58135c920b203 uses a genuine
asynchronous Node timer race and injects the identical TimeoutError class into the source
under test. Both GOOD and BAD timers fire; genuine typed error recovers, plain Error stops.
This is a real timer under a mocked navigation, not a live Playwright deadline measurement.
Both blobs pass this timer fixture because its text uses 25ms, not the old fallback's
60000ms. That limitation was disclosed by the worker and independently reproduced; the
fixture is not the regression discriminator. The complementary R13 pair supplies that arm.
Comments equating class identity to an independent deadline-state flag are imprecise:
the implementation satisfies the permitted TYPE alternative, not a separately measured own flag.

(iii) Own fresh before/after runs of the unchanged R13 diagnostic, with explicit blobs:

| case | before | after |
|---|---|---|
| typed deadline-shaped error | recover/write1 | recover/write1 |
| same text, plain Error | wrongly recover/write1 | terminal/write0 |
| same text, TypeError | wrongly recover/write1 | terminal/write0 |
| plain Error, punctuation changed | terminal/write0 | terminal/write0 |
| typed timeout, unrelated message | recover/write1 | recover/write1 |
| ordinary certificate error | terminal/write0 | terminal/write0 |

The R13 counterexample program returns rc0 when the defect reproduces and rc1 when it
does not. Its repaired rc1 is expected, not a failed acceptance battery. The new wrapper
asserts every post-repair result, not merely absence of the counterexample flag.

(iv) All reference diagnostics rerun against BOTH git blobs, not only worker-saved baselines.
Cardinality and case names checked before comparing full result objects. R11: exactly
1/11 changes, the named historical untyped timeout positive -> terminal/write0. R12:
exactly 1/4 retry cases changes, its named historical untyped timeout positive -> terminal/write0;
3/3 cleanup cases unchanged. R10 6/6, R9 6/6, R8 3/3 result objects unchanged.
The two changes are the explicit prospective CTO exceptions, not silently passing old positives.

## Reproduction and metadata

Own `node org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R14_REVIEW_PROBE.cjs`
prints `R14-CVO-PROBE-PASS`, rc0. It runs existing diagnostics unmodified, prints both
source hashes, and checks the named historical changes exactly. No browser, network,
host action, credential, MFA or real session write.

Worker battery independently rerun: both `--arm typed` and `--arm metadata` rc0,
deciding tokens IBR114-TYPE-OR-DEADLINE-STATE-ONLY-SPLIT-PAIR-HOLDS and
IBR114-METADATA-C174-C194-CORRECTED. Full hash comparison replaces [:12]; prior R113 result
artifact resolves to final blob af259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce at 9423390c47.
Exact R114 proof check with explicit IDs and governing order: 3 rows, 0 violations, VALID.
Its nine blob pins are announced UNRESOLVED-HERE by the commit-oriented checker; this
does not make their bytes inaccessible. Source and fixture objects were explicitly read.
No claim is made that structural VALID means arm(f) is published.

## Hold and routing

No publish/deploy, host readback or host start was performed. CTO msg99431 reports its half
at 91f14e1e03 naming packet blob 7e3d70b9 and permits the worker's bounded publish.
That is not authority for this CVO to perform the publish. The capture ask remains HELD
until the responsible lane also verifies retrieved S3 bytes equal the full ea437510... hash.
This grade alone neither supplies that readback nor initiates login/capture.

C-S195 is the machine-readable grade carrier in ADJUDICATION_v11. Existing deployment/
source remediation clocks are not silently closed on this pre-publication review.
Only CTO receives this targeted grade; MSTR owns push.

