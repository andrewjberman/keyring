# BRIEF -- the Posture panel, from current to desired

**From** `4.0.0_SA_CRO~Z`, 2026-09-18 ~19:0xZ. The last panel of the series Andrew set: *"you and I are going to go
through and brief current/desired/necessary delta for every component"*, with Posture explicitly NOT gating the round
(*"You and I will proceed to Posture regardless, but the greater fabric does not need to be held up on that"*). **To**
`1.0.0_SA_CTO~Z`, for the panel-briefs intake, when Andrew releases it. **Status:** a BRIEF with one decision open
(section 3). It creates no gate and cuts no order.

His standing direction applies: no fleet run until the process is validated end to end, and every stage framed by what
makes it run for a NEW security. It also builds on the Peers brief (`BRIEF_PEERS_CURRENT_TO_DESIRED_20260918.md`,
@a2fdbad164), because Posture's comparable comes from the peer set.

---

## 0. The denominator

33 keyed names, from `crosswalk/v1/2026-09-15.json` records with resolution MEASURED. Figures were read with the
adapter's own `scoped_amgt.read_posture` (`:2437`) over those 33.

---

## 1. Where the panel stands, measured 2026-09-18

**What Posture is** (`lib/research/posture/judge.py`, contract C-POSTURE): for each name, the most similar name on the
OTHER side of Opal's books (a held name against a non-held one, "both ways"), both names' evidence packs (Thesis, Exec
Management, Peers, Model), and ONE Claude call that returns better / worse / hold / steer_clear, with every basis claim
citing a pack element. It is marked a machine's view; nothing trades from it.

| what | measured over 33 |
|---|---|
| posture object SERVED | 33 |
| ... with a verdict | **9** -- better 6, hold 2, worse 1 |
| ... with verdict `absent` (comparable null) | **24** |
| held / not held | 6 / 27 |
| as_of | 2026-09-16 on 31; 2026-09-15 on 2 -- hand runs |
| cites validated on the 9 verdicts | 100% on every one (13-20 cites each), 6 basis claims each |
| judge | `claude-opus-5`, effort low; Boeing's call $0.13 (21,646 input tokens) |

**SERVED is a status here too.** The header's posture line reads 33 of 33 served (Lead Panel brief 11.1), and 24 of
those carry no verdict. Section 5 counts served as "carries a verdict".

### 1.1 Why 24 names have no comparable

| reason (the object's own) | names |
|---|---|
| "R-1 carries no held member (0 graded ...) and the re-run of the same ranker over U-1's held names returned none" | 22 |
| R-1's 12 members were all on the same side, and the re-run returned none | 1 |
| "R-1 carries no not_held member ..." and the re-run returned none | 1 |

Two causes sit under those reasons:
- **Nobody can see which side a name is on.** Membership comes from the ETF books in the union universe
  (`membership.py`). Of **170 holding rows, 3 are tied to a security and 167 are UNRESOLVED**, because the ETF plane's
  identifier contract (C-ETF-PLANE-READ) is not established (U-1 2026-09-15 denominators). "Held" is knowable for almost
  nothing, so a non-held subject has almost no held candidates.
- **The re-run cannot classify non-US names.** Enel's reason: *"no landed model_block_ENEL_IM_Equity.json ... and the
  key's exchange is 'IM', so the scanner's US ticker space cannot be joined by root without guessing"*.

### 1.2 The 9 verdicts stand on thin evidence

| subject | verdict | against |
|---|---|---|
| Boeing | hold | Deere |
| Alibaba | worse | Home Depot |
| Costco | better | TJX |
| Home Depot | better | Lowe's |
| Intuit | better | Cadence |
| Kimberly-Clark | hold | Estee Lauder |
| Nu Holdings | better | Truist |
| SAP | better | Arista |
| Valero | better | Williams |

- **The comparables inherit the ranker's weak peer sets:** Boeing against Deere, SAP against Arista, Nu against
  Truist. Home Depot against Lowe's is the kind of pair the panel should produce every time.
- **7 of the 9 were judged without the subject's Exec pack, and 6 without its Model pack.** Two defects, both read at
  source:
  - **The Model pack reads a worker's folder, not the pool.** `packs.py:41-42` and `:64-65` load
    `deliverables/0.9.0_WK_AMGT_RESAPP~1/model_block_<key>.json`, which holds three real names; the pool holds model
    blocks for all 33 (Model brief s.1; validation report D7).
  - **The Exec, pool and peer packs read the EXACT posture date** (`packs.py:108-114`:
    `management/v1/<key>/<as_of>.json`). Posture ran on 16 Sep; the management objects are dated 15 and 18 Sep, so none
    was found. It is the same exact-date defect that fragments the Exec Management pool (`enrich.py:594`).

**The judgment is the solid part.** Every claim cites an element, every cite validated, and the page prints each pack's
coverage, so a verdict judged on a thin pack says so. The weakness is everything the judgment is handed.

---

## 2. Desired

- **Side known for every name:** every ETF holding row resolved to a security. Bloomberg's `/sedol/<stem>` route already
  resolves these codes (measured in the Peers V work: 258 of 279 peer securities with a name-agreement control).
- **The comparable from the SA peer set** (Peers brief): the first of SA's peers on the other side of the books, with
  the section 3 rule for when none of the five is.
- **Packs read from the pool at each object's NEWEST date**, never an exact posture date and never a worker's folder.
- **Posture runs last in instantiation**, after the stages its packs come from have run for the name.

---

## 3. One decision still Andrew's

| the question | options | this seat's recommendation |
|---|---|---|
| **How should Posture pick the comparable when none of Seeking Alpha's five peers is on the other side of Opal's books?** | (1) keep today's ranker ONLY for that fallback, restricted to the other side; (2) use SA's peers of peers (a second SA call per name); (3) no verdict, with the reason stated | **(1).** It keeps SA as the primary source (Andrew's Peers ruling), reuses an existing path (`comparable.py` path (b)), and never leaves a name without a comparable because five peers happened to share its side. The fallback comparable is labelled as the ranker's, not SA's. |

---

## 4. What makes this run for a new security -- today and desired

| step | today | desired |
|---|---|---|
| 1. which side | U-1 membership; 167 of 170 holding rows unresolved | every holding row resolved; a new name's side is known the moment it is added |
| 2. comparable | ranker peers, then a ranker re-run | SA peers, then the section 3 rule |
| 3. packs | four packs; Model from a worker folder; the rest at an exact date | all four from the pool at their newest date |
| 4. judgment | one Claude call, by hand | the last step of instantiation |
| 5. trigger | hand runs on 15-16 Sep | runs once the name's packs exist |

---

## 5. The build, in dependency order -- round 14

No item includes a fleet run; each is proven on the validation names first.

1. **Packs from the pool, at the newest date** (`packs.py:41-42`, `:64-65`, `:108-114`). The cheapest item, and it
   removes the two gaps behind 7 of 9 thin verdicts. Shared with the Exec Management pool fix: one "newest object per
   name" read, not two.
2. **Resolve the ETF holding rows** -- the identifier contract (C-ETF-PLANE-READ), then Bloomberg's SEDOL route with a
   name-agreement check. Until this lands, "held" stays UNPROVEN rather than guessed, as `membership.py` already does.
3. **Comparable from the SA peer set, plus the section 3 fallback.** This follows the Peers build.
4. **Instantiation order:** posture runs after Thesis, Exec, Peers and Model for the name.
5. **Honest counts:** the header's posture line and every census count a posture as served only when it carries a
   verdict. The 24 read ABSENT with their reason.

---

## 6. Done means measured

| component | closed when |
|---|---|
| Side | holding rows resolved N of 170, each with the route that resolved it; the rest UNPROVEN with a reason |
| Comparable | N of 33 with a comparable, each labelled SA or ranker-fallback; the rest with their reason |
| Packs | on every verdict, each pack either present or absent for a stated data reason -- never a path or a date mismatch |
| Served | the header line's served count equals the names with a verdict |
| Instantiation | on each validation name, a verdict with no hand step, or the exact step that stopped it |

---

## 7. Traps named in advance

- **SERVED is a status, not a verdict.** 33 served held 24 absent.
- **Do not guess a holding's identity** to make a comparable appear. `membership.py` keeps an unresolved row UNPROVEN;
  keep it that way until the row resolves.
- **Do not read a pack at an exact date.** It silently misses every object written on another day.
- **Nothing trades from Posture.** The notice stays on every verdict.
- **No monitor or freshness checker** comes out of this brief.

---

## 8. What this brief does not ask for

No seat is re-tasked and no run is made; the figures are read-only adapter reads. Section 3 is Andrew's to answer.
