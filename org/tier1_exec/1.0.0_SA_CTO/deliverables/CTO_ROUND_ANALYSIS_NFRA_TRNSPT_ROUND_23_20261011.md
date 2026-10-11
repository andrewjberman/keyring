# CTO ROUND-23 ANALYSIS -- NFRA_TRNSPT -- answering the round-22 L10 slug (2026-10-11 ~06:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/remediations/REMEDIATION_v10.md`
@7ac9a6d1ff (3.0.0_SA_CVO msg 4298), on the close record `deliverables/2.0.0_SA_COO~T2/R22_CLOSE.md` @733aec56af.
**PRD:** `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md`. **No PRD addendum now;** section 3 names the one case that
would need one.

## 1. Where the project stands

Round 22 found that the scheduled Teams pull had failed on every fire since 2026-10-09T16:00Z, fixed it, deployed it and ran it
clean once by hand. The round-21 PASS that had missed this is withdrawn. Tonight three acts landed on the transcripts root:
the pull fix, the pull's memory at 1024 MB, and the commentary function created and then re-applied onto the pull's bytes.

| outcome | state | why |
|---|---|---|
| FWD-1 | APPLIED, ACCEPT owed | Andrew's Monday read; unchanged |
| FWD-2 | 0 of 4 types EXERCISED on the fixed code | the scheduled trigger has not fired on it; Monday 2026-10-12 13:00Z is the first unaided fire. `research_meeting`'s listing is refused |
| FWD-3 | NOT MET as written, for four meetings | section 3 |
| FWD-8 | UNGRADED | the ADMITTED read is parked with Andrew (row D2-S24); the REFUSED half is measured |
| FWD-5, FWD-6, FWD-9 | as carried in `R21_CLOSE.md` | not touched this round |

## 2. Measured by this seat (05:51Z, `get-function-configuration`, one call per function)

`teams-global-transcripts-pull-lambda` and `outlook-global-commentary-draft-lambda` both read CodeSha256 `AI4UQD0ME+ABza1X...`;
`outlook-global-transcripts-pull-lambda` reads `VGIq85Xxm5KVLCnv...`, last modified 2026-10-07. The three fix commits
fd74f984ac, 5ae3b3ddd9 and 7bca11ddee are ancestors of `origin/CLOUD` (positive control: yes). So row D2-S22's second disarm
read is met and its first reads 2 of 3. **The row stays ARMED.**

## 3. Rulings on the rows

| row | ruling |
|---|---|
| **D2-S22** (BLOCKING, ARMED; owner this seat) | Disarms when the mail pull is re-applied onto the root's one zip, section 4 item 1. It is first in the round and is NOT held for Monday's fire: the two functions share nothing at run time, and an armed row with a known fix does not wait on an unrelated event. Until it disarms, every apply on this root is targeted and hashes its tree's zip against the pull's live digest before the plan. |
| **D2-S16** (BLOCKING, INERT) | Closes on Monday's scheduled fire, read from `run.json` per-series counts with the REPORT line beside it. The driven invoke of round 22 is the deliberate arm; Monday is the unaided one. The REPORT line's Max Memory Used on a run that lands a transcript is the first measured peak. |
| **D2-S15** (BLOCKING, INERT; owner this seat) | **The four Monday meetings are NOT yet accepted as lost.** The gateway's meeting route refuses their content; that is one route. A Teams meeting's transcript is also a file in the organizer's OneDrive or the meeting's SharePoint site. One read-only cell looks there for the four dates (2026-04-10, 04-13, 05-04, 06-01), section 4 item 3. Found: they land by the content-only path with their source stated, and FWD-3 stands as written. Not found: this seat writes a PRD addendum that names the four as lost to every route read, and FWD-3's second ACCEPT clause ("no meeting that could be fetched on 29 September is later found missing") is then Andrew's to accept with that exception or not. The round-22 census counted 34 fetchable at that cutoff and 5 missing, so the clause is not met today. **Standing fact, to FWD-4's statement of what is missing and why:** a meeting not landed within about 120 days is lost to the meeting route. |
| FWD-2's wording, `research_meeting` | **Unchanged.** The outcome is that the latest Research Meeting is in the database without anyone fetching it; which Microsoft surface it is read from is mechanism. When Andrew's folder link arrives (open call `-01c5`), the source for that one series becomes the SharePoint folder, as a CONTRACTS addendum, and the scheduled pull reads it. Until then FWD-2 can reach 3 of 4. |
| **D2-S17** (OBSERVATION, INERT; owner this seat) | **A committed `readers.auto.tfvars`, holding exactly the applied value.** The value is READ from applied state (the role's live trust policy), never typed; the commit cites `CTO_RULING_NFRA_TRNSPT_FWD5_WIPED_SILVER_READER_HOLDERS_20261009.md`. The variable keeps NO default in the `.tf`, so a tree without the file still refuses to plan. Who reads the tier is then in git, changed only by a commit under a pair that carries Andrew's C-READERS word. Proof: a plan of the reader resources shows 0 changes; DELTA=0 needs no pair. Section 4 item 2. |
| **D2-S20** (OBSERVATION, INERT) | `readers.tf`'s header states the applied state, in the commit of item 2, which touches that root. |
| **D2-S24**, FWD-8 | Stays parked with Andrew. Added from the issuer's read: `Opal_Terminal`'s one Active access key, minted 2026-07-10, reads LastUsedDate NONE. Carried to Andrew as a fact. No seat deactivates or rotates it. |

## 4. ENRICHMENT LIST for round 23 (ONE issuance, in this order)

1. **The mail pull onto the root's one zip** (D2-S22). A code-only, targeted re-apply of `aws_lambda_function.mail_pull` onto
   the pull's live package, fetched, not rebuilt; its own never-widen pair in the shape of the commentary re-apply
   (`2287c83ba4`): the member diff, the mail handler's import closure against the changed set, the key producers equal, a
   rollback to the kept `VGIq85Xx` zip, and ONE driven invoke of the mail pull graded against its last scheduled run.
2. **`readers.auto.tfvars` from applied state, and the header** (D2-S17, D2-S20). LOCAL, with a plan showing 0 changes.
3. **The four Monday meetings, another route** (D2-S15). Read-only: the organizer's OneDrive and the meeting's SharePoint
   site, through the gateway's file tools, for the four dates. Output: found or not, per date, with the path and the tool
   that answered. No landing in this cell.
4. **`read_refused` in the handler's totals and log line; `test_eod_voice.py` collects.** LOCAL. The two tests that pin the
   totals are edited in the same cell that changes them.
5. **Monday's fire, read** (D2-S16). The issuer's read after 2026-10-12 13:00Z; not a cell that waits, a read that is owed.

Items 2, 3 and 4 are independent and start now. Item 1's packet comes to this seat. Each build order carries at most three
mechanical criteria.

## 5. Acts and inputs only Andrew can give (none gates items 1 to 4)

- **The Research Team Meeting SharePoint folder's link, or its site name and path** (open call `-01c5`). Citation: a share to
  his own account.
- **The ADMITTED read as `Opal_Terminal`** on the machine that holds its key, and which machine that is (row D2-S24).
  Citation: a credential on a device no seat runs.
- **His Monday read through the FWD-5 reader role,** which closes FWD-1's ACCEPT and FWD-5 together.
- **A past meeting he names** for FWD-3's first ACCEPT clause.

## 6. What this analysis did not measure

It rests on the slug, the close record and the issuer's readback as filed. This seat measured the three functions' digests
and the three commits' ancestry (section 2) and nothing else of round 22. That a transcript file exists in the organizer's
OneDrive for any of the four dates is not known; item 3 is the read.

-- 1.0.0_SA_CTO~DELL2
