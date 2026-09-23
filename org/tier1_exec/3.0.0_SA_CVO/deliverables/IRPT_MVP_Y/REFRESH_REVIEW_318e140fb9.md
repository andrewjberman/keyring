# Independent refresh-lineage consumer review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `318e140fb9b7417ea28d2de5057c6c85a9ebfd57`.

The bounded consumer controls pass: supplied **17 tests PASS**, zero failures,
errors or skips; **9/9 independent refresh controls PASS**. Original Y-U01
security/price replay controls still preserve the accepted input and its value.
No new defect found in these controls. No integrated criterion grade changes.

## Evidence and reproduction

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin 318e140fb9 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_318e140fb9.json
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_refresh_lineage.py --source-evidence org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_318e140fb9.json --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/REFRESH_LINEAGE_318e140fb9.json
```

The unchanged upload probe materializes the exact candidate, records source
hashes and reruns the supplied suite plus the original replay controls. The
independent refresh probe verifies all 283 snapshot file hashes before import,
then runs actual M guarded entry, Y upload/normalization and P repository code
with the supplied conditional/version/Decimal-aware storage doubles. The
candidate's complete uploads.py and test_uploads.py were read.

## Observations

| Independent control | Result |
|---|---|
| Fresh deliberate-action token plus supersedes_input_id through actual guarded upload Entry | New input is40 from the revised price; original remains20; upload record and frozen document retain the exact parent input/hash/artifact receipt |
| Recompose service; replay original and refresh with parser/security/price callbacks that raise if called | Both complete results unchanged; zero additional blob puts; no dependency callbacks |
| Second deliberate refresh | Three retrievable revisions preserve20,40,60 and the third binds the exact second receipt |
| Parent content hash changed after publication | LINEAGE_BINDING refusal; zero additional blob puts |
| Parent artifact version changed after publication | LINEAGE_BINDING refusal; zero additional blob puts |
| Parent owner changed after publication | INPUT_UNAVAILABLE refusal; zero additional blob puts |
| Parent input index removed after publication | INPUT_UNAVAILABLE refusal; zero additional blob puts |
| Current access revoked immediately after actual local parent-artifact read | ProspectOwnershipRefused; zero additional blob puts |
| Restore the unmodified parent and access | Original refreshed document returns unchanged |

The first run's reporter incorrectly required the exact PermissionError class
name, although ProspectOwnershipRefused is a PermissionError subclass and the
access was correctly refused. The reporter was corrected to use isinstance;
all scenarios were rerun unchanged. This was a probe defect, not a candidate
access failure. The evidence retains the actual subclass and refusal message.

The unchanged prior controls additionally preserve the same accepted input
under security-revision drift and same-date price drift (20 remains20); explicit
notional correction remains a distinct preserved100-to200 revision. Supplied
suite counts and independent controls are separate denominators. Producer's
reported11 subtests are not added to the17 unittest test-method total here.

## Limits and remaining integration

Same-process service recomposition and controlled doubles do not prove actual
process loss, simultaneous server transactions, crash recovery or deployed AWS
expression evaluation. The independent negatives check immediate parent access
and receipt binding; expiry, earliest/transitive dependency retention and
lifecycle disposal still require integration with P. Browser token reuse,
deliberate-action affordances and wire behavior remain P/CVO~P obligations.
The guarded analysis acceptance in the supplied suite remains a Mock.

No source implementation changed and no vendor/cloud/render/provisioning call
was made by this reviewer. This is a bounded consumer review, not full Y1/Y2,
S3/S4/S7, released report, READY or E2E acceptance. All fourteen integrated
criteria remain NOT_EVALUATED. Commit state LOCAL.

-- 3.0.0_SA_CVO~Y
