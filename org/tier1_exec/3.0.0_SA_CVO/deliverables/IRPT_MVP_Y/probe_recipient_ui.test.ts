/** Actual composer events with manual hooks and offline transport, not a browser. */
import { afterAll, expect, test } from 'bun:test'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'
const root = process.env.IRPT_PORTAL_REVIEW_ROOT!
const load = (path: string) => import(pathToFileURL(resolve(root, path)).href)
const React = await load('node_modules/react/index.js')
const { renderToStaticMarkup } = await load('node_modules/react-dom/server.js')
const { GenerateComposer } = await load('src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx')
const { ProspectComposer } = await load('src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx')
const { ProspectJobStatus } = await load('src/pages/InvestorReporting/tabs/analysis/ProspectJobStatus.tsx')
const { LiveClient } = await load('src/api/endpoints/investor-reporting.ts')
const { validRecipientDisplay, readSubmissionRequest } = await load('src/pages/InvestorReporting/contracts/submission-request.ts')
const { validRecipient } = await load('src/pages/InvestorReporting/tabs/analysis/recipient.ts')
const upload = JSON.parse(readFileSync(resolve(root, 'src/pages/InvestorReporting/__tests__/mvp-upload/tests/producer-upload.json'), 'utf8')).normalized.response.data
const results: any[] = [], observations: any[] = []
const tick = () => new Promise<void>((done) => setImmediate(done))
function nodes(tree: any): any[] { return Array.isArray(tree) ? tree.flatMap(nodes) : tree?.props ? [tree, ...nodes(tree.props.children)] : [] }
function text(tree: any): string { return typeof tree === 'string' || typeof tree === 'number' ? String(tree) : Array.isArray(tree) ? tree.map(text).join('') : tree?.props ? text(tree.props.children) : '' }
function deferred() { let resolve!: (value: any) => void; const promise = new Promise((done) => { resolve = done }); return { resolve, promise } }
function issued(id: string) { return { requestId: id, revision: '1', stage: 'RECEIVED' } }
function harness(Component: any, props: any) {
  let cursor = 0, tree: any
  const slots: any[] = [], internals = React.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE
  function render() {
    cursor = 0
    const prior = internals.H
    internals.H = {
      useState(initial: any) { const i = cursor++; if (!(i in slots)) slots[i] = initial; return [slots[i], (v: any) => { slots[i] = typeof v === 'function' ? v(slots[i]) : v }] },
      useRef(initial: any) { const i = cursor++; if (!(i in slots)) slots[i] = { current: initial }; return slots[i] },
      useMemo(fn: any) { cursor++; return fn() },
    }
    try { tree = Component(props) } finally { internals.H = prior }
    return tree
  }
  return {
    render,
    all() { return nodes(render()) },
    recipient() { return nodes(render()).find((n) => n.type === 'input' && n.props.required) },
    label(value: string) { const n = this.recipient(); if (!n || n.props.disabled) throw new Error('recipient unavailable'); n.props.onChange({ target: { value } }); render() },
    button(name: string) { return nodes(render()).find((n) => n.type === 'button' && text(n) === name) },
    click(name: string) { const b = this.button(name); if (!b || b.props.disabled) throw new Error('button unavailable: ' + name); b.props.onClick(); render() },
    async settle() { for (let i = 0; i < 4; i++) { await tick(); render() } },
    html() { return renderToStaticMarkup(render()) },
    jobText() { return text(nodes(render()).find((n) => n.props['data-slot'] === 'job-state')) },
  }
}
function custody(submit: any) {
  return harness(GenerateComposer, {
    scope: { resolvedScope: { clientId: 'C-one' }, scope: { clientId: 'C-one' }, permittedAccountIds: ['A-one'] },
    scopeRef: { firmId: '49financial', clientId: 'C-one' },
    snapshot: { sourceSetRevision: 'SNAP-one', businessAsOf: '2026-09-22', coverage: { remainderAmount: 0 } },
    snapshotEnvelope: { state: 'READY' }, submitter: { submitAnalysisRequest: submit },
  })
}
async function prospect(submit: any) {
  const ui = harness(ProspectComposer, { api: { submitAnalysisRequest: submit, uploadAnalysisInput: async () => structuredClone(upload) } })
  const file = ui.all().find((n) => n.type === 'input' && n.props.type === 'file')
  file.props.onChange({ target: { files: [{ name: 'holdings.csv', size: 29,
    arrayBuffer: async () => new TextEncoder().encode('Ticker,Dollars\nAAPL,100\n').buffer }] } })
  await ui.settle(); ui.click('Review portfolio'); await ui.settle()
  return ui
}
function control(name: string, run: () => Promise<void> | void) {
  test(name, async () => {
    const fetch = globalThis.fetch
    globalThis.fetch = (() => { throw new Error('NETWORK_FORBIDDEN') }) as any
    try { await run(); results.push({ name, outcome: 'PASS' }) }
    catch (e) { results.push({ name, outcome: 'FAIL', error: String(e) }); throw e }
    finally { globalThis.fetch = fetch }
  })
}
control('both composers require an explicit empty initial recipient', async () => {
  const c = custody(async () => issued('unused')), p = await prospect(async () => issued('unused'))
  for (const ui of [c, p]) { expect(ui.recipient().props.value).toBe(''); expect(ui.recipient().props.required).toBe(true) }
  expect(c.button('Generate').props.disabled).toBe(true)
  expect(p.button('Generate Overview').props.disabled).toBe(true)
})
control('custody exact retry and recipient edit bind distinct actual bodies', async () => {
  const calls: any[] = []
  const ui = custody(async (body: any) => { calls.push(structuredClone(body)); throw new Error('ambiguous offline response') })
  ui.label('  Recipient <one>  '); ui.click('Generate'); await ui.settle()
  ui.click('Generate'); await ui.settle()
  expect(calls[0]).toEqual(calls[1]); expect(calls[0].prepared_for).toBe('  Recipient <one>  ')
  ui.label('Recipient two'); ui.click('Generate'); await ui.settle()
  expect(calls[2].request_id).not.toBe(calls[0].request_id)
  expect(calls[2].prepared_for).toBe('Recipient two')
  expect(calls[2].report_title).toBe(null); expect(calls[2].account_ids).toEqual(['A-one'])
})
control('prospect exact retry is cleared by recipient edit', async () => {
  const calls: any[] = []
  const ui = await prospect(async (body: any, scope: any) => { calls.push({ body: structuredClone(body), scope }); throw new Error('ambiguous') })
  ui.label('  Recipient <one>  '); ui.click('Generate Overview'); await ui.settle()
  ui.click('Retry same analysis request'); await ui.settle()
  expect(calls[0]).toEqual(calls[1]); expect(calls[0].scope).toBe(undefined)
  ui.label('Recipient two'); expect(ui.button('Generate Overview')).toBeTruthy()
  ui.click('Generate Overview'); await ui.settle()
  expect(calls[2].body.request_id).not.toBe(calls[0].body.request_id)
  expect(calls[2].body.prepared_for).toBe('Recipient two')
  expect(calls[2].body.account_ids).toEqual([]); expect(calls[2].body.input_id).toBe(upload.input_id)
})
control('prospect recipient edit clears previously issued child status', async () => {
  const ui = await prospect(async () => issued('REQ-' + 'a'.repeat(24)))
  ui.label('Recipient one'); ui.click('Generate Overview'); await ui.settle()
  expect(ui.all().some((n) => n.type === ProspectJobStatus)).toBe(true)
  ui.label('Recipient two')
  expect(ui.all().some((n) => n.type === ProspectJobStatus)).toBe(false)
  expect(ui.button('Generate Overview').props.disabled).toBe(false)
})
control('busy prospect prevents recipient editing while a request is pending', async () => {
  const wait = deferred(), ui = await prospect(() => wait.promise)
  ui.label('Recipient one'); ui.click('Generate Overview')
  expect(ui.recipient().props.disabled).toBe(true)
  wait.resolve(issued('REQ-' + 'b'.repeat(24))); await ui.settle()
  expect(ui.recipient().props.disabled).toBe(false)
})
control('custody late response for previous recipient cannot replace newer request status', async () => {
  const a = deferred(), b = deferred(), calls: any[] = []
  const ui = custody((body: any) => { calls.push(structuredClone(body)); return calls.length === 1 ? a.promise : b.promise })
  ui.label('Recipient A'); ui.click('Generate')
  ui.label('Recipient B'); ui.click('Generate')
  expect(calls).toHaveLength(2)
  b.resolve(issued('REQ-' + 'b'.repeat(24))); await ui.settle()
  expect(ui.jobText()).toContain(calls[1].request_id)
  a.resolve(issued('REQ-' + 'a'.repeat(24))); await ui.settle()
  observations.push({ name: 'custody_out_of_order_recipient', calls, current_label: ui.recipient().props.value, final_job_text: ui.jobText() })
  expect(ui.recipient().props.value).toBe('Recipient B')
  expect(ui.jobText()).toContain(calls[1].request_id)
  expect(ui.jobText()).not.toContain(calls[0].request_id)
})
control('both actual input markups escape hostile text without altering state', async () => {
  const label = '"><script>alert(1)</script>&', c = custody(async () => issued('unused')), p = await prospect(async () => issued('unused'))
  for (const ui of [c, p]) {
    ui.label(label); expect(ui.recipient().props.value).toBe(label)
    const html = ui.html(); expect(html).not.toContain('<script>'); expect(html).toContain('&lt;script&gt;')
  }
})
control('component guard and shared guard agree on complete prohibited character sweep', () => {
  const points = [...Array(32).keys(), ...Array.from({ length: 33 }, (_, i) => i + 127), ...Array.from({ length: 2048 }, (_, i) => i + 0xd800)]
  for (const code of points) {
    const value = 'Recipient' + String.fromCharCode(code)
    if (validRecipient(value) || validRecipientDisplay(value)) throw new Error('accepted forbidden codepoint ' + code)
  }
  for (const guard of [validRecipient, validRecipientDisplay]) {
    expect(guard('😀'.repeat(200))).toBe(true); expect(guard('😀'.repeat(201))).toBe(false)
    expect(guard(' \u2003 ')).toBe(false)
  }
  observations.push({ name: 'prohibited_sweep', controls: 65, surrogates: 2048, validators: 2 })
})
control('actual LiveClient rejects invalid body before transport and sends exact recipient', async () => {
  const calls: any[] = []
  const client = new LiveClient({ transport: { async request(url: any, init: any) {
    calls.push({ url, body: JSON.parse(init.body) }); throw new Error('offline sentinel')
  } }, telemetrySink: () => undefined })
  const body = { request_id: 'review', client_id: null, account_ids: [], snapshot_id: null,
    input_id: upload.input_id, variant: 'overview', comparison_keys: [], report_title: null, prepared_for: '  hostile <text> 😀  ' }
  for (const invalid of [{ ...body, prepared_for: '' }, { ...body, prepared_for: 'x'.repeat(201) }, { ...body, principal_id: 'forged' }]) {
    expect(() => client.submitAnalysisRequest(invalid)).toThrow()
  }
  expect(calls).toHaveLength(0)
  const cloned = readSubmissionRequest(body); body.comparison_keys.push('mutated' as never)
  expect(cloned.comparison_keys).toEqual([])
  await client.submitAnalysisRequest(cloned).catch(() => undefined)
  expect(calls).toHaveLength(1); expect(calls[0].body).toEqual(cloned)
})
afterAll(() => writeFileSync(process.env.IRPT_RECIPIENT_UI_OUTPUT!, JSON.stringify({
  pin: JSON.parse(readFileSync(resolve(root, 'review-source-hashes.json'), 'utf8')).pin,
  results, observations, limitations: ['Manual hooks and React static markup, not a real browser', 'Offline transport sentinel; no backend acceptance/worker/vendor/render/export grade'],
}, null, 2) + '\n'))
