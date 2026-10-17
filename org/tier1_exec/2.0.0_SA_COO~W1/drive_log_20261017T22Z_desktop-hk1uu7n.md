# drive log 2.0.0_SA_COO~W1 -- 2026-10-17 17:35Z to 22:35Z (dell1)

**archetype:** MIXED

Push state of everything below: LOCAL on box/dell1 except what MSTR~DELL1 pushed (origin box/dell1 read 718bb5e264 by MSTR at 21:3xZ; `origin/rel-amgt-harvst-cd2` = 1753c741d9). The new gold objects SC1 wrote are in the harvest bucket, not in git.

## What moved

- **Round 90 closed (CVO `ADJUDICATION_v84.md`; CTO analysis msg 7721).** `HVST-ce-4` wrote 62 of 62 add-only objects (the census's 30 plus KMB) 17:22Z to 19:27Z; I verified the manifest, read UNH, NFLX, TSM and the CPA control served myself, regraded the `ce-6` instance through the worker (my lane may not edit a worker's deliverables) and sent the packet. The silent driver death (row `D1-S44`, cause unknown) is filed at the CTO's ask.
- **Round 91 cut (CTO analysis item list):** `HVST-cf-1` (the verb census over all 94 names, merged `934ecb88c5`), `HVST-cf-2` (`fund_of_record` only from a holding line; a section paragraph never a position; method `/5`; merged `80d0701876` after two amendments), `HVST-cf-4` (the gold rebuild of 17 names, SC1, running). `HVST-ce-5` (the wording release) was DEFERRED by the CTO (msg 7727) and is carried in `ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md`. The `fund_form` chain (`cf-3`, `-5`) is held behind `cf-4`: changing `fund_form.gather_items` breaks every dossier build until new fund forms are written.
- **`HVST-cf-4`:** both never-widen halves signed (COO `275d5739...95b0`, CTO `8a5ea52464`), site Z cleared 22:00Z to 00:00Z (its CTO msg 35561), GO 21:40Z; canary MNST (fund absent, position `CANDIDATE FOR PFOE` with `stance` candidate, read served by me at 22:2xZ) and `8306_JP` (position absent) written 22:05Z to 22:11Z; the other 15 running at about 4 to 5 minutes a name; 19 manifest entries at 22:33Z, no stop, branch B or error line (the two `stop` hits in `cf4_run.log` are the words "one-stop-shop" in a Bunzl passage).

## My errors, corrected in the record

- **C-S61:** reading the round-90 census I took `CANDIDATE FOR <fund>` lines for stated positions; nine names served a `fund_of_record` from them from 17:30Z until the `cf-4` canary. Named in decomposition 121 and in the `cf-4` pair.
- I chained a worktree teardown after a refused merge in one command (the commits were safe on the branch); I left the KPI census folder out of the `ce-6` worker's sparse checkout; my first `ce-2` rule changed four existing values; my first `cf-2` classifier claimed a stance on lines with no fund token (amendment 2).
- A message to SC1 was refused once at 155 words (the cap is 150) and resent.

## Open at the end of this log

SC1's run of the other 15 names and its final report (the issuer then reads the manifest: 34 distinct keys, 17 names; UNH and CPA unchanged; three more names served; the proof); `D1-W159-S1` (the `ML_FP` template, ARMED, disarmed by the rebuild) and the worker notes; the round-91 packet to the CVO; the CTO's round-91 analysis. Row `D1-S46`: the silver `research_report.fund` still reads `PFOE` for a candidate line (`typed.py::_find_fund`); the CTO's ruling is needed. `HVST-cf-3` and `-5` (the `fund_form` chain) are defined, not cut. SC1's hourly `sa` reads stand. No open call at Andrew from this seat.

## Compiler Tools

- `.tools/safe-commit.sh` (about 22 commits this window), `.tools/safe-merge.sh` (fast lane: `ce-6` regrade, `cf-1`, `cf-2`), `.tools/wk-provision.sh` (4 provisions, 4 removes), `.tools/proof-of-spec-check.py` (VALID x4), `.tools/round-close-check.py` (REFUSED once on the `ce-6` AC2 row, then MAY-CLOSE), `.tools/comp-surprise.py`, `.tools/unblock.py tick`, `mcp opalgateway harvest_get_research` (my own served reads of UNH-class names, NFLX, TSM, CPA, MNST). Gaps: the comp-rail denied two Bash `grep` forms (native Grep answered); the broker refused one 155-word message and one ack of a message addressed to another seat.
