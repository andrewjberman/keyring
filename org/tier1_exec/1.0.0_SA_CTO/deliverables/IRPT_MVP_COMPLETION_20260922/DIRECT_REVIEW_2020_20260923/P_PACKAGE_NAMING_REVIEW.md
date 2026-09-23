# P-PACK-01: canonical destination dependency omitted

CTO direct review, 2026-09-23 21:42 UTC. Candidate source08f9738226, evidence de6216d795, exact local v3 zip SHA2569cc2d2d9aeaf57b935c914f760515cded4efd3e1c4f523af6f05910725d02bc6,58members. Bounded package FAIL; source fidelity/mapping reviews and empty-bucket plan73c40b05ad remain accepted.

Extracted that exact zip to a new scratch directory outside all repositories, used a fresh Python process with only its packaged lib on sys.path, and called:

```python
from opal_naming import preview_reporting_destination
preview_reporting_destination('cottonwood', 'PERFORMANCE',
    'RPT-' + 'a'*32, 'b'*64, policy_revision='irpt-x10-v1')
```

Observed FileNotFoundError for packaged org/standards/NAMING_SCHEMA.json via preview_reporting_destination -> _reporting_destination -> key -> _schema -> load_schema. No state flip, S3 call, data write or vendor use. Preview exercises the same address builder used by an active writer without changing pending policy.

Discriminating control: copied ONLY org/standards/NAMING_SCHEMA.json from exact08f9738226 into the scratch package. SHA2562c8834a98f7453fd1843eebe9baa45630aeb31cca708c114646678fdce480f33. Same fresh-process command exits0 and resolves opal-data-irpt/irpt/cottonwood/platinum/performance_reports/RPT-.../<digest>.json, writable:false, same pending-policy hashcb9c4e6e9541fefc315f57844490309ad15c9735593fe3a165b067a3087dc220. This local control is not a repaired shipped artifact.

Owner P: include that exact canonical schema in review build and canonical source-map/package closure; rebuild, publish new digest/manifest, rerun this one destination probe against final extracted bytes. No duplicate schema or handwritten address. Existing cold-import success did not exercise destination construction. Full guarded Lambda factory, Linux dependency execution, combined package/layer size, consumer grants, policy enforcement and authenticated retained-report screen remain open and are not closed by this fix. Do not delay the separately accepted empty-bucket apply on this packaging repair.
