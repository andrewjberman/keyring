# One finding about `infra/aws/lambda/transcripts-pull/`, filed from the LAPTOP for NFRA_TRNSPT's owner to mint

**Filed by:** `2.0.0_SA_COO~R` (laptop, COMM_ASSIST), 2026-10-08 ~23:5xZ, on `1.0.0_SA_CTO` msg 107481 (carry row
`NFRA_CTLPLN-W36-S2` by reference). **Why a file and not an appended row:** NFRA_TRNSPT is placed on dell2 and a Dell mints that
project's ids, as the precedent file `ROWS_FROM_LAPTOP_TRANSCRIPTS_ROOT_20261007.md` in this folder does. **This seat mints NO
`NFRA_TRNSPT-S<n>` id.** **Nothing of NFRA_TRNSPT's was built, applied or changed.**

## CANDIDATE ROW -- the transcripts-pull package's bytes depend on the working tree's line endings

**Source row:** `NFRA_CTLPLN-W36-S2` (worker `0.9.0_WK_NFRA_CTLPLN~36`, 2026-10-08, ARMED, disarm owner `2.0.0_SA_COO~R`), in
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`.

**`spec_asserts`:** a build script packages a commit; the same commit gives the same package hash on any box, so a rollback can be
rebuilt to a known hash.

**`world_is`:** `infra/aws/lambda/transcripts-pull/build.sh` packages `infra/logic/registry/*.json` with the same copy-then-zip
pattern the Teams agent's `build.sh` used before round 5, with no line-ending normalisation. The Teams agent's package was measured
to depend on line endings: two registry files sit CRLF in the laptop's shared working tree and LF from a fresh checkout, with
`core.autocrlf` false and `git status` showing nothing. Round 5 (cell CT-i-8, merged `139a1adde2`) fixed the Teams package by
writing text files LF inside the packaging step: see `infra/aws/lambda/teams-chat-assist/build.sh` and its test
`infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py`. The transcripts-pull script was READ only; its deployed
hash against an LF build was not measured.

**Proposed for the owner:** the same packaging-step normalisation in `transcripts-pull/build.sh`, with a reproducibility test, cut
in NFRA_TRNSPT's own round; the next deploy's hash may differ from the live one with no source change if the live one was built
from CRLF inputs.

**Disposition of the source row:** `NFRA_CTLPLN-W36-S2` is disarmed at COMM's end by this handover. The hazard now sits with
NFRA_TRNSPT's owner (`2.0.0_SA_COO~T2`, dell2), who mints the row.
