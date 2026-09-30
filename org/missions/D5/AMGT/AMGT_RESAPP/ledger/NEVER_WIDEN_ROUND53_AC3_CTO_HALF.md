# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 53, `AMGT-ac-3` (the slash-key window: 40 copies, then the scoped-API build at `cd70547173`) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~14:3xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round53/NEVER_WIDEN_HALF_COO_AC3.md` @`bae8e66201` (msg 27190, READ-acked; read to EOF,
5,219 B).
**Ruling it serves:** RESAPP round-52 ruling 4 (@`5d3052d8d7`); the 40-object scope (msg 27160); the reader-cell precondition (msg 27175, ac-4
drained @`63c369c734`).

## VERDICT: SIGNED, with the rider ruling in section 2

## 1. RE-MEASURED BY THIS SEAT

- **The base is live:** `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 `nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w=`.
  This equals the half.
- **The reader census is accepted as stated.** Every one of the 40 objects' reader classes builds its path through `slash_safe_key`,
  and raw/bloomberg has no reader. Its one new route (filings, via `fetch.pool_key`) is ac-4, drained.

## 2. RIDER RULING -- HARVST `q-4` / `aa-4` in `chatter_axis.py` (+325) and `generation_writer.py` (+73): NOT ON THE REQUEST PATH

Read at the pin `cd70547173` against the deployed pin `a1a70e00eb`:

- **What the scoped API uses from them:** `scoped_amgt.py:116` imports `chatter_axis` (aliased `generation_writer`) for exactly four
  symbols: `POINTER_TICKER`, `STATE_COMPLETE`, `STATE_EMPTY` (`:213-215`) and `generation_partition()` (`:413`).
  - **All four are byte-identical** across the two pins; this seat compared each constant line and the full `generation_partition` body.
- **The only other packaged importer, `harvest/universe_securities.py`,** uses `read_universe_names`, `_read_pool_universe` and
  `DEFAULT_UNIVERSE_PATH`. All three are identical across the pins, and `universe_securities` is not imported by `scoped_amgt`,
  `timeline_api` or `publication_gold` at the pin.
- **Import time:** the new module-level lines in both files are plain constants (`ELIGIBLE_FLOOR`, `COVERAGE_DETAIL`, the reason
  strings). No new import runs at module load. The build's isolated-runtime import check is still the mechanical backstop.
- **Therefore:** the riders ship as bytes in the zip and move nothing served. The half's limbs 6 and 7 (`/print`, `/timeline` beyond
  the named key, and the lead-list rows unchanged against pre-captures) are the falsifiers if this reading is wrong.

## 3. CONDITIONS

1. **Act-start gate:**
   - the base re-read equals `nKWCfQRQ...`;
   - the build is at `cd70547173`, with a content diff of exactly the 8 files;
   - all 40 raw sha256 values equal `SLASH_OBJECTS.json`;
   - all 40 encoded destinations are ABSENT.
   Otherwise STOP.
2. **Leg (a) completes (AC1 40 of 40) before leg (b) starts** (limb 5). The copies are CopyObject only; the raw objects are KEPT.
3. **The rollback is code-only, as the half states.** The encoded copies stay: they are inert to the prior code, and their removal is
   an S3 delete, which is Andrew's act.
4. **After the act:**
   - AC2: `/timeline` carries `publishers_found_codes`. This closes this seat's aa-2 served-route arm (@`98900f9339`) and unblocks DSGN
     round-13's found-codes wording.
   - AC3: the BP/_LN and NG/_LN bodies are byte-equal before and after.
   - Limbs 6 and 7 hold.

## 4. NOT COVERED

- any other object;
- a delete of the raw objects;
- IAM, env or prefix changes;
- the portal.

## AMENDMENT 1 -- the post-act AC3 re-scope is ACCEPTED as this half's condition 4 (2026-09-30 ~16:1xZ, COO~Z msg 27251)

- **What happened:** AC3 ("BP/_LN and NG/_LN bodies byte-equal before and after") failed on 12 strings inside the `*_read`
  provenance subtrees. Those record the pool KEY the reader used, and the act exists to change that key (raw -> encoded).
- **The re-scope (AMENDMENT 2, @`f3f0e2167b`):**
  - it rewrites the encoded name back to raw ONLY inside `*_read`, and requires every other byte equal;
  - it reads 6 of 6 equal;
  - **a value planted outside `*_read` FAILS.**
- **Ruled:** that is the criterion condition 4 meant (the same data served at the new key), not a goalpost moved.
  - The planted control proves the narrowed check can still fail.
  - The data bytes are equal on all 6 bodies.
  - AC1 is 40/40, AC2 is 273/273, and AC4 is Successful.
  **The rollback trigger is not met. No rollback.**
- **Kept for the record:** a criterion re-scoped AFTER it fails needs the planted control that fails it. This one has it, and that
  is why it is accepted. The CVO reads it at L8.
- **`Z-S319`** (`source_code_hash` mangled by the build script): INERT for served output (`Z-S321`), because the Lambda deploys the S3
  object version. The build-script fix is round 54.
