# Cross-adjudication submission: who produces the account-id hash list that `client-data-check.py` reads

## Context
`.tools/git-hooks/client-data-check.py` reads `~/.opal/account_id_hashes.txt` (or `OPAL_ACCOUNT_ID_HASHES`). The file is ABSENT on site Z, the
laptop and dell2 (measured: every dell2 safe-commit prints "hashed account-id list ABSENT ... NOT checked"), so the gate passes everything on
every box. My ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_CLIENT_ACCOUNT_DATA_IN_REPO_CONTAINMENT_20261009.md` names the
SERVED account-id set as the detector of record (:97-98), and the gate owner is the laptop CTO (item 8). Site Z's proposal, relayed by
`0.0.0_AB_MSTR~DELL2` at 01:56Z: a scheduled job writes the sha256 list to one non-repo S3 key, and every box pulls it to `~/.opal/`.

## Position
Site Z's shape, with ONE change that matters: **keyed hashes, not plain sha256.**
- A plain `sha256(UPPER(id))` of a 10-digit or 8-digit id is reversible by trying every id: 10^10 candidates is minutes of work. A plain list
  copied to every box is in effect the account list, sitting on every developer machine.
- **Producer:** each firm's existing directory or ownership build step, which already reads that firm's served ids under the firm's own role,
  writes `HMAC-SHA256(key, UPPER(id))`. The key lives in Secrets Manager and is not in the repo. The output goes to ONE non-repo key per firm,
  under an ops prefix in that firm's own bucket, so no cross-firm read is needed to produce it. Addresses are by `address()`.
- **Consumer:** a box pull tool fetches the per-firm lists with the box's existing credentials, plus the HMAC key, into `~/.opal/`.
  `client-data-check.py` HMACs each id-shaped token with the same key. A missing list or key keeps today's loud ABSENT line and never
  passes silently.
- **Owner:** the laptop CTO (gate owner, item 8) names the build step per firm. Dell2 cuts the IRPT firms' steps.

## Why it gave pause
### Ambiguity
Whether a hash list counts as client data. Unkeyed, it does.
### Out of pattern
It is a new artifact class: a secret-keyed derived list spread across boxes.
### Other solutions
- Plain sha256 (site Z): simplest, but reversible, so worse.
- A membership-check service called per commit: no list leaves AWS at all, but every commit needs the network and a new Lambda. Better
  isolation, more friction. It is the fallback if keyed lists are refused.
