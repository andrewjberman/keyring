# 3.0.0_SA_CVO -- session 2026-09-15 ~07:20Z to ~08:40Z -- MDPF_TAXSMA: CERTIFIED run confirmed; L4-R ratified-text half REFUSED at v0.1, SIGNED at v0.2

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Continues:** `session_0400-0720Z_mdpf_taxsma_certified_pass_and_intake.md` (@a7180be272).

**Watchers:** no crons. Both Monitors were re-armed from the main root at each 30-minute expiry and confirmed with
TaskOutput. Now: inbox `bhkml3epy`, surprise intake `b8046g4n8`.

## DONE (every act committed; LOCAL -- ls-remote ~07:03Z, origin/CLOUD = 6a5b276f8b)

### MDPF_TAXSMA -- the CERTIFIED run, confirmed by this seat's own read

1.0.0_SA_CTO~A marked the run CERTIFIED @717f49f6ea. This seat's read at HEAD confirmed:
- run.json reads CERTIFIED;
- the run-home certification.json is byte-equal to this seat's placed copy (e54cb35c...);
- the certified rectangle is still the dry state (4a90496a...);
- no commit touches the certificate after the placement @b79ced9360.

### MDPF_TAXSMA PRD -- L4-R, the ratified-text half

| version | verdict | review | stamp | why |
|---|---|---|---|---|
| v0.1 @48befbfcbf | REFUSE R1 | @e53b06bd38 | @8699f4ba7c | the display row carried Andrew's SUPERSEDED whole-dollar rounding (@fe76e3e036); his ~02:5xZ word @39aae459ed is the nearest $10,000, with "$0" under $5,000 |
| v0.2 @8ab2dc2bc6 | SIGN | @20504bde03 | @214982df0b | R1 closed; N1 (known values only) and N2 (96960's durable pin) taken |

**v0.1 checks, all holding except R1:**
- ENDPOINT against the approved ENDPOINT_PROPOSAL.md @8e8afed454: DONE WHEN, ACCEPT and SOURCE match 8 of 8, and the
  headings are equal once markdown is stripped.
- Every CONTRACTS pin resolved at its commit.
- The reuse targets exist:
  - b00 and `net_mv_plus_cash`;
  - ms_ingest.py;
  - the publisher;
  - the 13:30 floor at `scheduled-floor.tf:133`;
  - the 13:50 publisher at `mdpf_portal_publisher.tf:228`.

**The first refusal stamp failed to commit.** A foreign `index.lock` was held by 4.0.0_SA_CRO's concurrent commit, and
the stamp left its signoff file uncommitted in the worktree.
- That is the S14 shape, measured on this seat.
- The HEAD-reading status correctly read MISSING throughout.
- A retry, after Win32_Process showed the lock clear, committed it clean.

**The fix was carried to the author.** 1.0.0_SA_CTO~A's v0.2 notice named only 4.0.0_SA_CRO's brief refusal 96983, so
this seat sent R1 directly (96985). That seat carried it into v0.2.

**v0.2, measured by this seat's section diff:**
- ENDPOINT is byte-identical.
- CONTRACTS changed exactly 3 lines: the data-contract version, 96960's pin, and the display row.
- The data contract's JSON diff, v0.1.0 -> v0.2.0, touched 4 paths: the ATTESTED-only membership rule via
  CONFIRM_EFFECTIVE_MEMBERSHIP, and SOURCE_PROVEN dropped. It agrees with the Workbook row.
- The brief half (4.0.0_SA_CRO) reads STALE after v0.2, so the PRD stays WITHHELD until that seat re-signs.

### Intake

- **LGIC_NAMING-S17 (round 3).** LIMB 6 refuses a tree issuance committed from a LINKED WORKTREE, even though the PRD's
  halves are signed at HEAD.
  - The cause is inferred to be 1.0.0_SA_CTO's S14 fix @3e8cf9e288, which reads the signoff dir at HEAD, under a
    linked worktree's hook environment. The code was not read.
  - At round 3's L9, REMEDIATION_v2 row S14 stays OPEN until the fix holds in linked worktrees.
- **LGIC_NAMING-W1-S7 and S18.** Round 3's result files overwrite round 2's records at the same paths. Round 2's records
  remain in history (@eaafb46486). This is a question for this seat and 2.0.0_SA_COO~G at round 3's L9.
- **IRPT_FNTEND-S67 and round-8 worker rows.**
  - S67 is F49-AC10 timing out at bun's 5000 ms. W3-S40 is ARMED to 0.9.0_WK_IRPT_FNTEND~1, and W1-S74 is ARMED to
    2.0.0_SA_COO~F.
  - None is ARMED to this seat. All are round-8 rows, compiled at its drain.
- **LGIC_ENFORCE.** S15 disarms W1-S14. Every ARMED row has a disarm or disposition except W1-S17, whose S13 fix is
  unexercised.

## OPEN

- **Grading at drain-end:**
  - LGIC_ENFORCE round 1: S9's duplicate ids, W7-S1 and W7-S4, W8-S3, S5 against RULING DM.
  - IRPT_FNTEND round 8: S66's admin-plus-internal gate, S67 with W3-S33.
  - LGIC_NAMING round 3: S17 against S14's remediation, W1-S7 and S18.
- **Backfill (b):** the next project, as its gap between rounds admits it.
- **MDPF_TAXSMA:** nothing further owed by this seat unless ENDPOINT or CONTRACTS change again.
