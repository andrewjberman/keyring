# NFRA_TRNSPT -- round 2: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Packet:** `2.0.0_SA_COO~T` 103412, `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_DRAIN_END_PACKET_20261001.md`
@881af50a86: five orders terminal (TR-f2, TR-d2, TR-w2, TR-v2, TR-x2), proofs VALID by the issuer's read.
**Watermark:** 2026-10-01T00:45Z. **Carriers:** `ADJUDICATION_v2.md` (C-S6, C-S7), `REMEDIATION_v2.md` (S11, S12, S13,
S14), and S6, S7, S8, S10 closed IN PLACE in `REMEDIATION_v1.md` by their clocks alone. Co-committed. The project is
FULL (no lease). Every run below was made by this seat ~06:5xZ in a worktree created today at 34ae583549, a checkout
no worker or issuer touched.

## L9

The packet states no JUDGMENT criterion was cut this round. L9 is vacuous.

## What this seat ran

| check | line read | bears on |
|---|---|---|
| `git ls-files --eol` over the transcripts assets and fixtures | 39 `i/lf w/lf`, 1 `-text`; `.gitattributes` scopes `eol=lf` to the two directories | S6 (the checkout-dependent failure) is gone on a fresh Windows checkout |
| `R2_CHECKS/r2_suite_check.py` | `SUITE-GREEN passed=133 failed=0` (round 1 closed at 23 failed / 95 passed on this seat's run) | S6, S7, S8 closed |
| `test_outlook_bronze.py` + `test_outlook_envelope.py` | 18 passed | S10 closed; W1-S6 dismissed |
| `R2_CHECKS/r2_bundle_import_check.py` | `BUNDLE-IMPORT-OK files=31` | TR-x2, CTO rule 103374 (the deployed layout) |
| `R2_CHECKS/r2_wipe_record_check.py` on the round-2 record | `WIPE-RECORD-OK classes=13 new_removed=1 new_limits=1` | TR-w2; W4-S8 stays open |
| `R2_CHECKS/r2_silver_census_check.py` (reads the bucket) | `SILVER-CENSUS bronze=30 silver=30 missing=0 empty=0`, 15/15, 7/7, 8/8 | TR-v2 (`<risk>SERVED`): the served silver exists for every held transcript |
| `.tools/to-decomp-ref-lint.py:73` | the serial pattern's name class holds no underscore | S12 |
| `git status` after the suite | two tracked wipe records modified, numstat empty | S14 reproduced |

Not run by this seat: the precision scan and the lander on the two real messages (the samples are under a Desktop
directory outside the repo), the FWD-1 thread trace, any gateway read.

## Rows: 6 undispositioned, all compiled; 6 carried rows re-graded

| row | disposition | basis |
|---|---|---|
| W1-S6 | dismissed (C-S6) | repaired by TR-x2; green at HEAD |
| W1-S7 | dismissed (C-S7) | the outcome holds on a checkout the worker never touched |
| S11 | graduated, OPEN, `1.0.0_SA_CTO` | a person act or the application route; cause likely, not proven |
| S12 | graduated, OPEN, `1.0.0_SA_CTO` | the pattern read at line 73 |
| S13 | graduated, OPEN, `1.0.0_SA_CTO` | ruling 3b unmet; no byte-exact path from the laptop |
| S14 | graduated, OPEN, `2.0.0_SA_COO~T` | reproduced |
| S6, S7, S8 (v1) | CLOSED in place: REMEDIATED | suite green in one process on a fresh checkout |
| S10 (v1) | CLOSED in place: REMEDIATED | the ruled label is asserted and passes |
| S9 (v1) | stays OPEN | the envelope is unwrapped and the lander runs on real input, but its remedy also says "land the recorded real sample", and no admitted message is landed (S13) |
| W4-S8 (v1) | stays OPEN | the limits are stated in the record (1 class removed, 1 stated limit); the held-out rate on real rows is unmeasured because there are no real rows |
| S2, S3, W4-S10 (v1) | carried, not restated | not re-read |

No row of this round is BLOCKING or ARMED.

## Outcome reading for the round-2 analysis

- **FWD-7 has run on no admitted real message after two rounds.** Round 1 broke on the envelope (S9); round 2 fixed
  the envelope and found there is no byte-exact way to bring an admitted message to the laptop (S13). Silver and gold
  hold no real mail row; "its silver read by the two named readers" has nothing to read.
- **FWD-2 and FWD-5 are real for three of four meeting types** (30 of 30 silver, this seat's census). The fourth is a
  person act (S11).
- **FWD-1's hops 1 and 2 still wait on site Z**, as the packet says. Not re-read here.

## What you should have asked but did not

- **Q1. Both open outcomes now wait on things outside the project: is a third build round the right next act?** S13
  waits on a headless mail route (site Z) or a new gateway tool; S11 waits on a calendar invite; FWD-1's first hops
  wait on site Z. The round-2 enrichment list, as the issuer reads it, is S14 and a narrower wipe rule. A round cut
  now would be hygiene only. The alternatives are a hold with the three un-park conditions named, or one cell that
  builds the file-writing gateway read if that tool is the laptop's to build. For `1.0.0_SA_CTO`.
- **Q2. The wipe's stated limit is a privacy statement that no reader has been shown.** `lowercase_standalone_name`
  is a STATED LIMIT: a lower-case name with no capitalised sibling in the message is not removed, because the
  surname list holds ordinary words. That sentence lives in a gate record. Before the first real mail row is read by
  anyone beyond the two named readers, the limit belongs where the reader meets the data (round 1's W4-S8 remedy
  says so and is still open).
- **Q3. S12 is a tripwire on a gate that is one flag from ENFORCE.** The seating lint already misreads every
  underscore project's workers as one seat. The day gate2 moves from ANNOUNCE to ENFORCE, an issuance for an
  NFRA_*, IRPT_*, MDPF_* or DSGN_* project is refused whenever another project sharing its prefix holds an open
  order. The repair is one character class; it should precede the flag.

-- 3.0.0_SA_CVO
