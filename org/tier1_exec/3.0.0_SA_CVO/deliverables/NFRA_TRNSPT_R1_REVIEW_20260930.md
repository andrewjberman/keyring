# NFRA_TRNSPT -- round 1: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Packet:** `2.0.0_SA_COO~T` 103386, `R1_DRAIN_END_PACKET_20260930.md` @2b7372f583. **Orders:** 12 of 12 terminal; the
row gate's own census reads 0 open of 12. **Watermark:** 2026-09-30T20:15Z. **Carriers:** `ADJUDICATION_v1.md`
(C-S1..C-S5) and `REMEDIATION_v1.md` (9 rows), co-committed.

## L9 -- TR1-t4-AC3: PASS

FWD-5 ACCEPT: an analyst gets what was said about one company without opening a file. Graded on the real silver
parquet, run by this seat at CLOUD HEAD:

```
python data/transcripts/scripts/teams/read_meeting.py --series monday_meeting --date 2026-09-28 --grep Goldman
MEETING monday_meeting 2026-09-28 turns=290 speakers=7 transcripts=1
(2 turns follow, at 13:03:17Z and 13:39:24Z, each with its speaker and full text)
```

The turns' text is not reproduced here: the meeting content stays inside the two readers C-READERS names, and this
file is pushed. Read by this seat on the terminal: both turns state a position on the named firm in plain words, so
two turns of 290, each with its time and speaker, answer "what was said about Goldman" in one command, with no file
opened. The limit: the match is a literal token, so a later turn that says "they" about the same firm is not returned.
That is a recall limit for round 2's enrichment, not a failure of this criterion.

## What this seat ran or read at CLOUD HEAD (20:0xZ to 20:2xZ)

| read | result | bears on |
|---|---|---|
| `thread_trace.py --series monday_meeting --transcript MM-20260928-0858 --date 2026-09-28 --negative-date 2026-09-27` | `THREAD-TRACE hops=3 no_person=true negative_arm=NOT-HELD`, rc 0 | FWD-1 reproduces; hops 1-2 (the scheduled pull) are not exercised, as the packet states |
| `pytest data/transcripts/scripts/tests` in one process | 23 failed, 95 passed | S6-S8 graduated (the packet's 22 / 30 was an earlier tree) |
| `lib/opal_naming.py validate` | OK, 51 system rows, 13 scopes, 40 warnings | S4, W4-S11, W4-S12 closed |
| `generate --out <scratch>` over all targets | 13 written; 12 identical to the committed file; 1 differs in its mark line | S3 graduated, narrowed to one portal target |
| `missions-tree-index.py check` | 0 violations | W1-S1, W2-S1, W3-S1, W4-S4 closed |
| row gate `_open_tos_census('NFRA_TRNSPT')` | 0 open of 12 | L8 precondition |

## Rows: 30, all compiled

| rows | disposition |
|---|---|
| S1, S5 | dismissed (C-S1): CTO 103271 placed the gateway tools on site Z |
| W1-S1, W2-S1, W3-S1, W4-S4 | dismissed (C-S2): index drift fixed |
| W4-S1, W4-S2, W4-S3, W4-S5 | dismissed (C-S3): the applied rulings |
| W4-S11, W4-S12, S4 | dismissed (C-S4): the registry validates and regenerates |
| W1-S2..S5, W3-S2, W4-S6, W4-S7, W4-S9 | dismissed (C-S5): legal resolutions recorded |
| S2, S3 | graduated to 1.0.0_SA_CTO: the site Z relay for read_email's fields; one stale portal target |
| S6, S7, S8 | graduated to 2.0.0_SA_COO~T: the batched repair cell |
| S9, S10 | graduated to 2.0.0_SA_COO~T: the two thread-breaking items, first |
| W4-S8, W4-S10 | graduated to 2.0.0_SA_COO~T: the wipe's stated limits; the slicer's composition read |

## What you should have asked but did not

- **Q1. FWD-7 has run on no real row.** The one real input broke at the envelope (S9), so silver, gold, the wipe and
  the slicer are proven on synthetic input only. The planted-token wipe gate passing 8 of 8 says the wipe removes
  what was planted. It does not say what a real Manav message leaves behind (W4-S8 names two classes it will miss).
  Round 2 should land the recorded sample and read its silver before any reader beyond the two named ones.
- **Q2. The combined suite is the round's real test, and it is red.** Every file passes alone and 23 fail together.
  That is the shape of a deployed Lambda that imports both packages (S7), not a test artifact. The repair cell
  should prove the import in the deployed layout (CTO 103374), not only a green run.

## Not verified by this seat

The 12 proof-of-spec instances individually (the census admits them by status word), the Terraform plan's `9 to add`,
and the replay directory outside the repo (client data, not read).

-- 3.0.0_SA_CVO
