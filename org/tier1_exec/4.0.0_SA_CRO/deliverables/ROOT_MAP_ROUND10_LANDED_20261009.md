# Root map and registry, LGIC_BLANKFIX round 10 -- landed, and rulings R10-5..R10-7

**By:** `4.0.0_SA_CRO` (registry owner), 2026-10-09 ~09:5xZ. **Asked by:** dell1 `2.0.0_SA_COO~B1` msg 2192, relayed by
`0.0.0_AB_MSTR` msg 107896. Drafts at box/dell1 @dcfb18066a:
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/` (`MAP_ENTRIES_round10.json`,
`REGISTRY_ROWS_round10.json`, `HOLES_OWNED_round10.md`). Rulings R10-1..R10-4: `ROOT_MAP_ROUND10_RULINGS_20261009.md`.

## Written

- `root_map.json`: the 7 drafted entries (R10-1..R10-3, `_cite` stripped) and `advi/billing-read` (R10-5). Roots 78 -> 86.
- `key_rulings.json` +19 (142 -> 161), `name_rulings.json` +21 drafted + 1 (R10-6) (97 -> 119), `event_rules.json` +1
  (11 -> 12). No duplicate on any key.
- `key_rulings.json` row (opal-data-inf, gold/meta/pipeline-complete.json): `declared_in` added (R10-7).

Measured on the real files, laptop, after each step:

```
before        roots_total=88 mapped=78 unmapped=10 hole=0  stale_hints=0 uncounted=1
after rows    roots_total=88 mapped=86 unmapped=2  hole=5  (carded-class 4, other 1) stale_hints=0
after R10-7   roots_total=88 mapped=86 unmapped=2  hole=4  (carded-class 4, other 0) stale_hints=0 refused=0
VALIDATE: OK 54 system row(s), 14 scope row(s), 0 warning(s) over all 13 registry file(s)
```

The 2 unmapped are the two roots R10-4 retires. The 4 holes left are `1.0.0_SA_CTO`'s key-reader cases (astn-pipeline 1,
etfs-reports 1, shared-infra 2; `HOLES_OWNED_round10.md`, row `LGIC_BLANKFIX-D1-W2-S4`): their rows are already landed and
match once `bucket_of` reads the true bucket.

## Rulings

**R10-5. `advi/billing-read` (new since round 9): system `advi`, scope `49financial`, source `advi`, fills `["system"]`.**
Every name is builder output with system advi (`lambda.tf`, `iam.tf`); the lambda, role and policy carry the firm of master
08335338, which is 49financial (`locals.tf`, `scopes.json`); the one store is `advi/49financial/gold/advi_billing/`. The
artifact name carries no scope, so scope is not in fills. Measured: the root reads items=4 right=4 hole=0.

**R10-6. `restricted-prefix-get-put-list` (shared-infra, IAM_POLICY): a name ruling, not a vocabulary row.** `restricted`
is a function word, not a system token. The policy sits on the break-glass role, whose own name is builder output (system
cloudops, the firm of the commonwealth master 08335338 = 49financial, function `restricted-breakglass`). Canonical:
`cloudops-49f-restricted-breakglass-policy`, which grades CONFORMANT. Renaming it is the shared-infra applier's act.

**R10-7. `gold/meta/pipeline-complete.json` in opal-data-inf: `declared_in` names the four files that use it there.**
`inf-gold-trigger`, `inf-gold-freshness-guard`, `inf-portal-publisher` and `mdpf-daily-trigger` (whose bucket is
`INF_BUCKET`, an environment variable the reader cannot read). Naming only the mdpf file would make the other three read as
stale hints; with all four, stale_hints stays 0 and the mdpf hole closes.

## The two retired roots

The tracked files of `canonical-schwab-si2-schedule` and `opal-assets-absence` are removed in the commit after this one
(R10-4: both states hold 0 resources). Each box's untracked leftovers in those folders (stray `org/`, `.build/`, a
`.tfplan`) are a recursive delete, which waits on Andrew's word; they hold no Terraform and do not count as a root.
