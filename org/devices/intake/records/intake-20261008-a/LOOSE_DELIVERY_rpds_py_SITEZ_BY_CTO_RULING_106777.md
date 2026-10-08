# Batch intake-20261008-a -- the rpds-py wheel was delivered LOOSE, by CTO ruling (msg 106777; the ask was msg 106773)

Written by `2.0.0_SA_COO~C`, 2026-10-08 ~06:0xZ, on the CTO's instruction to record this beside the batch. This seat did not
carry the file; `1.0.0_SA_CTO` did, and the facts below are the CTO's as reported in msg 106777, not measured by this seat.

- **What went:** five files, by Taildrop to the target "sitez", at about 05:4xZ, rc=0 as the CTO reports:
  `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl`, its delivery text
  `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl.delivery.txt`, the two records
  `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl.fetch.json` and `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl.check.json`, and a
  `.sha256` file the CTO made.
- **From where:** the tool's own release folder, `C:\opal-intakeelease\intake-20261008-a` (measured by this seat at ~06:0xZ:
  it holds the wheel and its delivery text). Re-hashed by the CTO before sending: SHA-256 begins `0be972be84cf`, equal to the
  signed check record.
- **Why loose:** `pack` refused the batch because `click-8.3.1-py3-none-any.whl` remains in holding
  (`INTAKE-PACK REFUSED ... files remain in holding/intake-20261008-a/`). The CTO ruled that a refusal about the batch being
  incomplete says nothing about a file that is checked and released.
- **What this means on the receiving box:** there is NO pack and NO manifest for this file, so `intake_receive.py verify`
  cannot be run on it at site Z. The receiving seat's check is the `.sha256` file against the wheel, and the check record's
  eight lines read by a person. The receipt this route normally returns is therefore not owed in its usual form; site Z's
  own statement that the hash matched is the receipt.
- **State of the batch:** rpds-py `verdict=checked`, released, delivered loose. click HELD on `c6=failed`, a reading caused
  by the tool (an editable install whose source folder is gone), under repair in cell CT-e-3 AMENDMENTS 3 and 4;
  `pack --released-only` is part of that repair.
