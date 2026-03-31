# DS Gold Cleanup -- AE Assessment and Next Steps

**Date:** 2026-03-24
**From:** 0.6.0_AE_PartnerETL
**Re:** DS .004 local repo cleanup of gold scripts

---

## Assessment

DS cleaned the local repo correctly. archive/ deleted (31 files), run_all.sh removed,
README rewritten, run_gold_layer.sh and deploy script updated. No conflicts with AE's
S3 audit. The two workstreams are complementary: DS owns local repo, AE owns S3.

DS correctly identified the critical gap: `aws s3 sync` without `--delete` means local
deletions never propagate to S3. This is exactly how 5 parallel S3 prefixes accumulated
over 6 weeks.

---

## DS Next Steps

### 1. Add --delete to deploy script's S3 sync (CRITICAL)

The deploy script (`deploy-to-ec2.sh` or equivalent) must use `--delete` on the
`aws s3 sync` that pushes gold scripts to `code/gold/`. Without it, every file
rename or deletion locally leaves a ghost on S3.

**Safety guard required:** The sync MUST exclude data artifacts so a code sync
doesn't nuke parquet files or other outputs that live under the same bucket:

```bash
aws s3 sync data/black_diamond/scripts/gold/ s3://opal-data-bd/code/gold/ \
  --delete \
  --exclude "*.parquet" \
  --exclude "*.pyc" \
  --exclude "__pycache__/*"
```

This is the one change that prevents the problem from recurring.

### 2. Commit local cleanup as a single commit

All local changes (archive deletion, README rewrites, run_gold_layer.sh fix, deploy
script fix) should be one commit. Suggested message:

```
cleanup(gold): delete archive/, rewrite docs, fix deploy paths (ADVI_PRICES-004)
```

### 3. Do NOT touch S3

S3 cleanup (Phase A from AE audit) is AE scope. AE will run the `aws s3 rm` commands
after the current gold rerun completes.

### 4. Do NOT rewrite historical logs or archive/ references

DS already correctly identified these as records. Leave them.

---

## AE Will Handle

- `aws s3 rm s3://opal-data-bd/code/gold/archive/ --recursive`
- `aws s3 rm s3://opal-data-bd/scripts/gold_layer/ --recursive`
- `aws s3 rm s3://opal-data-bd/scripts/gold/ --recursive`
- Root-level stray scripts
- Dead runner scripts
- Phase B: move scheduler script from `scripts/` to `code/silver/` (with Lambda update)
- Phase C: establish `code/` prefix convention, deprecate `scripts/`
