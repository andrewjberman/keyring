# WP-3 LEDGER — ENGINE CHOICE BY ONE CRITERION

**WP3-1-AC4** · criterion cell `WP3-ajtr-1..4` · decomp vintage `540503df0a` · design read at
`d0398b977d` (§6, the engine is deliberately OPEN and the round-3 attackers were barred from
attacking the choice — it is a build decision, made here for the first time).

---

## 1. THE CRITERION — ONE SENTENCE

> **The ledger store lives on the device that owns the work, and no write to it is ferried across
> a fabric boundary.**

That is CLAUDE.md Rule 26 (`docs/doctrine/CLAUDE_ANNEX.md:465` — *"THE APPLY RUNS ON THE DEVICE
THAT OWNS THE WORK. NEVER FERRY AN APPLY ACROSS FABRICS"*) read as a property of the STORE rather
than of an apply: the seat that mints a record holds the context that record's admission needs, and
a ferry is precisely the step that separates the two.

**This is the only criterion.** Nothing below selects on performance, familiarity, query ergonomics
or scale. If a reader finds a second selection criterion in this file, the file is defective — see
§4.

## 2. WHAT THE CRITERION YIELDS

Design §6 offers three candidates. The criterion is applied to each, and it is applied to all three
before any is preferred:

| candidate | store locality | ferried write? | criterion |
|---|---|---|---|
| Iceberg table under Nessie | catalog + objects are REMOTE and shared across fabrics | **yes** — every write crosses a fabric boundary to a shared catalog | **REJECTED** |
| JSONL log + index | a local file on the owning device | no | **admitted** |
| SQLite / DuckDB file | a local file on the owning device | no | **admitted** |

Two candidates survive locality. They are separated **not by a second criterion** but by the
design's own stated REQUIREMENT — §6: *"`commit_seq` is a requirement ON the engine (a monotone
batch counter), not a choice of engine."* A requirement is a filter every candidate must pass, not
a preference between them:

- **JSONL log + index** — append order gives a monotone counter only while there is exactly one
  writer. Two processes on one device appending concurrently interleave, so `commit_seq` needs an
  EXTERNAL lock. That is a second mechanism outside the engine, which means the engine does not
  provide the counter — it fails the requirement on its own terms.
- **SQLite file** — a transaction gives a monotone counter inside the engine (a `batch` row per
  admitted batch; its integer primary key is the `commit_seq`), and writer serialisation is the
  engine's, not a bolt-on.

**CHOICE: a single-file SQLite store, local to the owning device.**
DuckDB is the near miss and is named so the rejection is legible: same locality, same single file,
but its concurrent-write story is weaker than SQLite's for a store whose whole job is admitting
batches one at a time. Locality does not separate them; the `commit_seq` requirement does.

## 3. HOW THE ENGINE PROVIDES `commit_seq`

One `batches` row per admitted batch, `commit_seq INTEGER PRIMARY KEY AUTOINCREMENT`, written in
the same transaction that admits the batch's records. Monotone by the engine's own key allocation;
gap-free is NOT claimed and is not required (design §2e: `commit_seq` is a total order ACROSS
batches and shared WITHIN one). A rejected batch consumes no `commit_seq` because it never opens a
transaction that commits.

## 4. FAILURE MODE — WHAT A FALSE ANSWER LOOKS LIKE

Stated so a reader can refute this file rather than agree with it:

- **Two criteria.** If the choice needs locality *and* a second selection property to land, the
  criterion did not yield the choice — the author did, and the second property is where the real
  decision hid. A requirement stated by the design (`commit_seq`) is not a second criterion; a
  preference introduced here would be.
- **A choice that cites none.** An engine named with no criterion applied to the rejected
  candidates — the shape where the answer arrives first and the reasoning is written to fit it.
  §2 applies the criterion to all three, including the one chosen.
- **A criterion that admits everything.** If Rule-26 locality had admitted all three candidates, it
  would have selected nothing and this file would be decoration. It rejects Iceberg-under-Nessie on
  a stated property, so it discriminates.
- **The concrete refutation:** show that an Iceberg-under-Nessie store does NOT ferry a write across
  a fabric boundary, or that a JSONL log provides a monotone `commit_seq` under concurrent writers
  without an external lock. Either refutes §2 and the choice must be re-derived.

## 5. SPEC ANCHOR

`WP3_LEDGER_DESIGN.md` §6 @ `d0398b977d` (engine open; `commit_seq` a requirement on the engine)
and §2e (commit_seq total across batches, shared within one). CLAUDE.md Rule 26 @
`docs/doctrine/CLAUDE_ANNEX.md:465`.

**This file authorises no ledger code.** WP3-1 is battery-first; the runner reads this file to know
which store to open in wave 2.
