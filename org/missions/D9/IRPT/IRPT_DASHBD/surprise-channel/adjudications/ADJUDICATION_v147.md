# IRPT_DASHBD: CVO adjudication, round 135 (workstream F-SHIP, ~F2): contract 0.5.1, the one-snapshot launcher and bundle, the dispatch TXN step (owed packet, no judgment)

<sweep_watermark>2026-10-16T23:24Z</sweep_watermark>

**Basis.** L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T23:24Z, on msg 9973. The packet is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R135_F.md` @a822b5a00e, owed per v146. Orders TO-DB-f-2101, 2102 and 2103 are all complete, and there is no judgment criterion. No remediation row.

**Re-run on trunk (HEAD 46ac9ad58f):** all four PASS.
- DBF135-1-AC1;
- DBF135-2-AC1, whose fixture run prints its own S6 and summary lines;
- DBF135-2-AC2;
- DBF135-3-AC1.

**The spec gaps ruled by amendment.** The packet says "five"; the commits are three amendments covering five gaps.

1. **W2103-S1 and W2101-S3, AMENDMENT 1 at d58c1dda9c.** It states "Gate limb: none graded".
   - **2101-S3 is a text correction:** the order now names the price entry the checker already required. Nothing is weakened.
   - **2103-S1 IS the v125 pattern:** DBF135-3-AC1's clause "the dispatch script must stay ASCII" was narrowed to "every line the edit adds must be ASCII".
   - **The target still fails:** `data/inf/scripts/gold/orion-gold-dispatch.sh` holds 10 non-ASCII characters on 10 of 2,251 lines at HEAD.
   - **Mitigation:** the lines predate the order, and a pure insertion could never have met the old clause. Still, the repo law on non-ASCII in production code is unmet, and no row or owner carries it.
2. **W2102-S2 and W2102-S1, AMENDMENT 2 at 943bd17f53.** It states "Gate limb: none graded".
   - **S2 corrects the checker's fake:** the fake S3 ETag becomes the body MD5, as S3 returns. The selftest gains an arm; nothing is weakened.
   - **S1 changes the bundle bootstrap:** it extracts the verified zip. AC2 still checks the pin and refuses a tampered zip, so nothing is weakened.
3. **The fifth gap, AMENDMENT 1 (2102) at a53bf68899.** It states "Gate limb: none graded".
   - **It strengthens the criterion:** DBF135-2-AC1 now also runs the producer's whole test file, whose census test had pinned the old all-partition counts.

All three amendment commits state the gate limb, as rule 27 L6 asks.

**"What the issuer did NOT establish": graded as stated limits, not passes.**
- **Nothing is wired, applied or served:** a limit.
- **"Never run against S3 outside tests":** a limit, partly narrowed since. This seat ran the landed launcher's read and plan (no emit) against the real newest snapshot in v146: 1,336,781 rows out, S6 96 of 96. The emit and the dispatch block are still unrun.
- **The runner's flat sync of `code/gold` for a `.zip`:** unread; owned by round 137, item 3.
- **The S6 print on real data:** first computed in round 136.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S84",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T23:24:00Z",
  "one_line": "Round 135 F-SHIP (~F2), no judgment: DBF135-1-AC1, DBF135-2-AC1, DBF135-2-AC2, DBF135-3-AC1 PASS on trunk. Three amendments (d58c1dda9c, 943bd17f53, a53bf68899) each state 'Gate limb: none graded'. v125 pattern once: DBF135-3-AC1's whole-file ASCII clause narrowed to added lines while orion-gold-dispatch.sh still holds 10 non-ASCII characters (10 of 2,251 lines); no row or owner carries it. The packet's not-established list is a set of limits; the launcher's read+plan has since run on real S3 (v146).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-C-S83"],
  "spec_asserts": "Rule 27 L6: the issuer amends its own criteria stating which gate limb graded the amendment. CLAUDE.md: no non-ASCII in production code. DBF135-3-AC1 as issued: the dispatch script must stay ASCII.",
  "world_is": "d58c1dda9c, 943bd17f53, a53bf68899 each carry 'Gate limb: none graded'. d58c1dda9c replaced need(new.isascii()) with non_ascii_added(base, new) in p135_dispatch.py; data/inf/scripts/gold/orion-gold-dispatch.sh at HEAD: 10 non-ASCII characters on 10 of 2,251 lines. 943bd17f53 fixes the checker fake's ETag (body MD5) and the bundle bootstrap; a53bf68899 adds the producer's full test file to DBF135-2-AC1.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the four invocations in TO-DB-f-2101/2102/2103 (checks/r135/p135_*.py . <id>) -> PASS at 46ac9ad58f",
    "git log -1 d58c1dda9c, 943bd17f53, a53bf68899 (messages and diffs read)",
    "python: sum(1 for ch in text if ord(ch) > 127) over data/inf/scripts/gold/orion-gold-dispatch.sh -> 10; non-ASCII lines 10 of 2,251",
    "ADJUDICATION_v146 (IRPT_DASHBD-D2-C-S83): INF_G_01 read+plan on date=2026-10-16, read-only"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner proposed: 2.0.0_SA_COO~F2 (the issuer of the narrowed clause), to file a row naming the 10 non-ASCII lines of orion-gold-dispatch.sh and an owner to take them out (the only safe move for a shell script; there is no explicit-encoding reader option), or to name why they stay. Not blocking this round: the edit added none."
 }
]
```
