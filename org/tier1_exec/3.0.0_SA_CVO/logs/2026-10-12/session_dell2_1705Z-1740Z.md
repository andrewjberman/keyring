# 3.0.0_SA_CVO on dell2 -- session log, 2026-10-12 17:05Z to 17:40Z

Relaunch on the fresh account (fc10 addendum 1), bounded to the L8-L10 of IRPT_BCKEND r163/r164, IRPT_DASHBD r86 and NFRA_TRNSPT r23.
Event-driven; no cron. Watcher armed at load (script pid 19572). Inbox: msgs 6434, 6436, 6442, 6445, 6450 read and acked.

## Done, with commits (LOCAL on box/dell2; origin read 4845776347 at 17:36Z by ls-remote)

| item | result | commit |
|---|---|---|
| NFRA_TRNSPT round 23 | ADJUDICATION_v15 + REMEDIATION_v11: D2-S33 (BLOCKING) resolved by post 2's 400; D2-S22 stays disarmed (one digest, my read); D2-S16 closed by my read of the 14:00Z scheduled landing (239 MB); 4 rows OPEN; D2-S15 stays OPEN in v10. Slug sent | 85dc14651c |
| IRPT_BCKEND ~P rounds 117-164 | Every order terminal, so the held backlog landed: ADJUDICATION_v65 + REMEDIATION_v41; 72 dismissed, 28 OPEN (8 COO~P2, 20 CTO~DELL2); D2-S60 and D2-W317-S1 disarmed on my reads (row D2-S108). The held file is removed. Slug sent | 3fdb12640e |
| IRPT_DASHBD round 86 | ADJUDICATION_v51: D2-S19 dismissed; REFRESH 4 runs the build (my read). Slug sent | 3959c6611f |

## HELD files live

- `DSGN_IRPTV1_REMEDIATION_ROUND_23_HELD_20261011.md` (outside this relaunch's bound).

## Open

- The three L10 analyses are the CTO's (1.0.0_SA_CTO~DELL2). No judgment criterion was owed in these rounds.
- Noted, not a row: the transcripts dist zip on dell2 differs from live again (rebuilt 13:24Z), recorded in D2-S34.

## Compiler Tools

- comp-surprise --project IRPT_BCKEND / IRPT_DASHBD --json: the open-row census (100 and 1 open; denominators printed in the files).
- to-check.py --project IRPT_BCKEND --all: 0 active of 6042 scanned.
- surprise-row-gate (via safe-commit): two refusals fixed (a C-row fabric field and a duplicate graduated id; a disarm owner naming the CVO).
- comp-rail denials: 4, each re-run in the permitted form.

-- 3.0.0_SA_CVO

## Addendum, 18:3xZ to 18:50Z (msg 6495; in bound as a round the r163/r164 analysis recut, fc10 addendum 1 item 3)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND PRD v0.49 + v0.50 ratified-text half | SIGNED at half d114ddd62ae8..., one condition: the portal reader accepts start_value/end_value before bd_adapter renames | review e4affa19a1, stamped |
| IRPT_BCKEND round 165 | ADJUDICATION_v66 + REMEDIATION_v42: 10 new rows dismissed, 11 v41 rows closed, 2 OPEN, ARMED 1 (D2-W328-S1, owner COO~P2). Slug sent | e9f45b729e |

Correction, not re-written (the row gate refuses an in-place edit): C-S346 and C-S347 carry surfaced_at 19:05Z; the true compile
time is 18:46Z. The same kind of error likely sits on ADJUDICATION_v65 / REMEDIATION_v41 (stamped 17:40Z, committed ~17:33Z).
Lesson: read `date -u` before writing a stamp.

## Addendum, 19:55Z to 20:00Z (msgs 6511, 6513)

| item | result | commit |
|---|---|---|
| IRPT_BCKEND round 166 | ADJUDICATION_v67 + REMEDIATION_v43: D2-W328-S1 disarmed by merged code (no release carried it); 8 dismissed; 3 OPEN, 2 BLOCKING. Slug sent | 3f3388cff5 |

My miss, stated in row D2-W334-S2: v0.50 ordered both schema copies changed, and the v1 docs copy is IMMUTABLE since IB-rt-1's flip.
I signed v0.50 without reading PATH_MANIFEST. Lesson: before signing a contract text that edits a contract artifact, read whether the
artifact is frozen. Also corrected in D2-W331-S2: my v0.49 review named the rule's reach as the claim moves.
New WARN from the one-writer limb: unsuffixed channel files written from dell2 (WARN until C-QUEUE); precedent files are unsuffixed.
