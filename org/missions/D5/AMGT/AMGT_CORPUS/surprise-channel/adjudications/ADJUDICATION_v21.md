# AMGT_CORPUS ROUND 18 -- L8 COMPILE + L9 ON THE TWO JUDGMENT ITEMS

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~02:0xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND18_DRAIN_END_PACKET.md` @`8868d88625`, msg 26838. The packet was read to EOF (5,068 B).
**L7 re-measured, not adopted:** `t-2` reads `complete` on its LAST `<status>` tag, and the packet's `t-1`/`t-3` flips match its
drains. `t-4` is held on AMGT_RESAPP r51, and nothing is registered.

---

## 1. L9 -- THE TWO ITEMS

| item | verdict | grounds (this seat's reads) |
|---|---|---|
| **t-2's "byte-equal" graded as 0 shared/type change with 209 of 214 reproduced; the 5 attributed to the CLI-versus-producer header path (`Z-W2-S14`)** | **AGREED** | Re-run `t2_AC1.sh`: "t2 replay rc 0 shared_changed 0 shared_removed 0 type_changed 0 hitachi_reproduced 209 of 214 non6501_added 0". It wrote only to a temp map. This seat then **listed the 5 unreproduced additions**. They are exactly `measured_on[+"6501 JP Equity"]` under `BEST_DPS`, `BEST_EBITDA`, `BEST_EPS`, `BEST_PE_RATIO` and `CIE_DES_BULK`: the BEST_ (bestdata) fields and the description field. That is one family the CLI's header preparation omits, consistent with `Z-W2-S14`. None is an exception-shape entry, and nothing shared moved. |
| **t-3's one ABSENT reader judged not served** (`render_pack.py main()`, a CLI building `BP-_LN_Equity`) | **AGREED, with the one served path checked that the packet did not name** | The `render_pack` module IS on a served path: `scoped_amgt.py` imports `build_rich_text` (`:4495`) and `build_pack` (`:4517`) for `/print`. `render_pack.security_key()` turns `/` into `-` (`:155`), so BP/ derives `BP-_LN_Equity`, the key with 0 objects. But the served route reads the model block by the RESOLVED raw key (`read_model_block(resolved_key)`, `:4479`) and passes the block in. Inside `build_pack`, the derived `sec_key` only names the output files (`pack_<sec_key>.pdf` / `.txt`) and reads nothing. **So the served print reads BP/'s real data; only `main()`'s own read uses the empty key form.** The judgment holds. The worker's `/versions` and `/thesis` reads did not exercise `/print`; this is the code-level check, not an invocation. |

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S65` (`build_unit_map` downgrades shared fields on one ambiguous name) | **GRADUATED** | t-2's replay re-run by this seat: shared_changed 0, shared_removed 0, type_changed 0 |
| `Z-S64` (the model-block writer bypasses `slash_safe_key`) | **CARRIED** as a migration item | The served readers read the raw key (section 1). Round-17 ruling 3 keeps it as a migration. |
| `Z-W2-S13` (ARMED: an exception under a SCALAR shared field is invisible to `_resolved_unit`/`_resolved_sign`, so 6501's BEST_SALES reads the shared `MILLIONS`) | **CARRIED** -> the analysis | A served-value hazard for one name's unit, and a reader cell in `model_block_pull`. It is the first place a PM could read a wrong unit on Hitachi. |
| `Z-W1-S18` (ARMED: `price_axis_pull.py:97-100` puts the MAIN workspace on `sys.path` at import) | **CARRIED** -> the analysis | **A grading hazard:** a multi-file pytest in a worktree grades the MAIN tree's bytes, so a worker's red can read green. Single-file AC scripts are unaffected. |
| `Z-W2-S14`, `Z-W3-S9`, `Z-S67` | **CARRIED**, INERT | as the packet |
| `Z-S63`, `Z-S66` (ARMED) | **CARRIED** | t-4 waits on AMGT_RESAPP r51 cell 1 |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | |

## 3. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3 cut. t-4 was held on a named external block. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W2-S13` and `Z-W1-S18` CARRIED with owners; the rest as before. **MET**
3. **Every judgment item graded:** 2 of 2 AGREED. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S21",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T02:05:00Z",
    "one_line": "L9 round 18: t-2 replay re-run (0 shared/type change, 209 of 214) and its 5 unreproduced additions listed -- all measured_on appends on BEST_DPS/EBITDA/EPS/PE_RATIO and CIE_DES_BULK, the header-path family; t-3's not-served call holds -- /print imports render_pack but reads the block by the raw key and uses the derived BP-_LN key only to name output files; Z-S65 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "t2_AC1.sh re-run: 't2 replay rc 0 shared_changed 0 shared_removed 0 type_changed 0 hitachi_reproduced 209 of 214 non6501_added 0'; the 5 missing: /fields[mnemonic=BEST_DPS|BEST_EBITDA|BEST_EPS|BEST_PE_RATIO|CIE_DES_BULK]/measured_on[+'6501 JP Equity'].",
        "lib/research/api/scoped_amgt.py:4479 read_model_block(resolved_key); :4495 from lib.research.print.render_pack import build_rich_text; :4517 import build_pack.",
        "lib/research/print/render_pack.py:155 security_key -> replace('/', '-'); build_pack uses sec_key only for pack_<sec_key>.pdf/.txt output names.",
        "TO-CRPS-t-2 reads 'complete' on its LAST <status> tag."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S65"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @8868d88625 asserts t-1..t-3 VALID and merged, t-2's replay 0 shared/type change with 209 of 214, t-3's one ABSENT reader not served, and t-4 blocked on AMGT_RESAPP.",
    "world_is": "True as read. Both judgment items hold on this seat's own reads, and the one served path through render_pack the packet did not name (/print) is shown to read the raw key.",
    "notes": "FOR THE ROUND-18 ANALYSIS: Z-W2-S13 is a served-unit hazard on Hitachi's BEST_SALES; Z-W1-S18 can make a worktree's multi-file pytest grade the main tree's bytes."
  }
]
```
