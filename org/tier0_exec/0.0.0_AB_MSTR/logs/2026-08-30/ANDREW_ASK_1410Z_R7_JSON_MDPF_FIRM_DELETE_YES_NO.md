# ASK FOR ANDREW'S WORD -- R7: delete the dormant `json/mdpf/{firm}` prefix? (yes / no) -- carried ONCE

> **STATUS 14:30Z: CARRIED ONCE, as REC YES.** The reader was resolved first: `3.0.0_SA_CVO` retired its three harness reads
> @`5bdbcfef69` (on origin @`5d879caad7`), `0.4.0_DS_ClientPlatform~V` re-ran line 3b on that pin (87887): 0 call sites
> across the 3 files, no new reader; every plane reads ZERO with its control fired, so the gate's pre-committed rule
> (87625) returns **YES**. Line 3b below is the 5bdbcfef69 figures; the earlier three-reader line is superseded on that
> limb only.

**Carried by:** `0.0.0_AB_MSTR`, 2026-08-30 14:10Z, on the issuer's half (`2.0.0_SA_COO` 87582/87621), the gate's half
(`1.0.0_SA_CTO` 87611) and the gate's recommendation rule (87625), with the four measured inputs from
`0.4.0_DS_ClientPlatform~V` (87743, read-only, nothing written). Reserved to Andrew by the Agent Autonomy line ("S3
deletes" need human confirmation); an agent-issued TO does not substitute. Register: R7 (CVO).

## THE SUBJECT (measured 14:0xZ, `s3api` per bucket)

| bucket | objects | firms | newest write |
|---|---|---|---|
| `opal-data-assets` | 7 | 49financial, cottonwood, global, inflection | 2026-07-23 19:30:01Z |
| `opal-data-portal-v2` | 1 (49financial aggregate-aua-timeseries, 183,004 B) | 1 | 2026-07-28 13:41:07Z |
| `opal-data-bd` | 0 | -- | -- |

**8 objects across TWO buckets** (a one-bucket delete leaves the other). Nothing written under either prefix in ~33 days.
The two copies of 49financial's timeseries DISAGREE (171,643 B vs 183,004 B, five days apart).

## VERSIONING (instrument: `aws s3api get-bucket-versioning`, per bucket)
`Status=Enabled` on all three buckets; `MFADelete` absent from every response (= not enabled). **A delete writes a
DELETE-MARKER over a retained noncurrent version: RECOVERABLE, not final.**

## THE EVIDENCE THE HOLD WAITED FOR (line 1)
Record @`924d560a32` (checker 3948c766a7 VALID rc=0, grader PASS). The mdpf-gold Lambda's executing bytes are BOUND by
`CodeSha256 U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=`, LastModified 2026-08-29T02:55:49Z unchanged across the
13:30:34Z fire and the 13:35:53Z read; **0 code reads of `json/mdpf` in 3,046 lines**, live control (`portal/gold/mdpf`)
present. The reader was re-pointed 2026-08-19 @12b93b59ba and has run daily since, today included.

## READERS, BY PLANE, CORPUS NAMED BESIDE EACH DENOMINATOR (line 3)
- **DEPLOYED (Lambda packages):** 200 live functions (client-side count), 4 match "mdpf"; every package downloaded and
  bound by base64(sha256(zip)) == CodeSha256. Mentions: 3, ALL docstrings (opened). **ZERO code reads, ZERO writes.**
  Positive control: `portal/gold/mdpf` found in 4 members of mdpf-gold-lambda + 1 of the publisher.
- **REPO (comp-find, corpus=all, re-run at 5bdbcfef69):** 4,317 hits / 135,922 files scanned (71,567 ephemeral-floor,
  17 unreadable, 4,160 binary NOT searched); 1,218 files, 30 with a code extension -- the SAME 30 as the first run (new:
  none, gone: none; the rise in raw hits is today's own records naming the prefix). **Readers: ZERO.** The three CVO
  harnesses that read it were RETIRED @5bdbcfef69 (read at the pin, not the worktree): 5 text hits across 3 files, 0 call
  sites (comments/docstrings recording the retirement). The PORTAL does not read it (both hits comments; `aum.ts:552`
  records the prior claim as falsified). Positive control, same instrument: `portal/gold/mdpf` -> 1,452 hits / 135,938
  files, 25 code files. Second instrument at `0.0.0_AB_MSTR` (87635): 4,169 / 135,629 on the same corpus -- consistent.
- **STANDING AFTER ANY DELETE (not readers):** IAM grants in `mdpf-pipeline/iam.tf` and the publisher's write-prefix
  declaration `json/mdpf/*` -- declarations that outlive the objects; removing them is a separate act.

## THE TWO HALVES AND THE RECOMMENDATION LINE
- **Issuer half (COO):** the evidence condition the hold waited for is MET at the right vintage. GIVEN.
- **Gate half (CTO):** GIVEN on the same evidence ("stronger than the hold asked for").
- **Gate's recommendation RULE (87625, pre-committed):** REC YES *if and only if* the census reads ZERO readers on EVERY
  plane with a firing control in each; **one live reader anywhere = REC NO with that reader named, and the card still
  goes to Andrew as NO so the prefix's status is on his record either way.**
  **Resolved by the census as re-run at 5bdbcfef69: REC YES** -- zero readers on every plane (deployed, portal, repo, S3),
  each with a firing control. This seat carries the resolution as the gate wrote it and adds no view.
- **Grounds to RETIRE (DS~V):** zero readers/writers on the deployed plane, ~33 days dormant, a second source of one
  quantity whose two copies already disagree. **Grounds to KEEP (as they stood before the retirement):** the three harnesses were live
  code -- now retired, so this ground is spent; what remains is that a delete is recoverable either way.

## WHAT IS ASKED
One word: **YES** (delete the 8 objects under `json/mdpf/` in BOTH buckets -- recoverable delete-markers; the CVO's
three harnesses are re-pointed or retired first, the IAM/publisher declarations as a separate act) or **NO** (leave the
prefix; its status is on the record). Either word returns VERBATIM to `2.0.0_SA_COO` + `1.0.0_SA_CTO` + `3.0.0_SA_CVO`.
