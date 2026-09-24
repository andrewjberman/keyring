/** Offline event/state review. React scheduling, DOM and browser persistence are NOT tested. */
import { afterAll, expect, test } from 'bun:test'
import { createHash } from 'node:crypto'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const root = process.env.IRPT_PORTAL_REVIEW_ROOT
if (!root) throw new Error('IRPT_PORTAL_REVIEW_ROOT must name an exact archived portal commit')
const load = (path: string) => import(pathToFileURL(resolve(root, path)).href)
const React = await load('node_modules/react/index.js')
const { renderToStaticMarkup } = await load('node_modules/react-dom/server.js')
const { ProspectComposer } = await load('src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx')
const { LiveClient } = await load('src/api/endpoints/investor-reporting.ts')
const fixture = JSON.parse(readFileSync(resolve(root,
  'src/pages/InvestorReporting/__tests__/mvp-upload/tests/producer-upload.json'), 'utf8'))
const accepted = fixture.normalized.response.data
globalThis.fetch = (() => { throw new Error('Network forbidden by review') }) as typeof fetch
const flush = () => new Promise<void>((done) => setImmediate(done))
const bytes = new TextEncoder().encode('Ticker,Market Value,Currency\nAAPL,9007199254740993.01,USD\n')
const csv = (name = 'portfolio.csv', content = bytes) => ({
  name, size: content.length, arrayBuffer: async () => content.buffer.slice(content.byteOffset, content.byteOffset + content.byteLength),
})
type Element = { type: unknown; props: Record<string, any> }
function nodes(value: any): Element[] {
  if (Array.isArray(value)) return value.flatMap(nodes)
  return value && typeof value === 'object' && value.props
    ? [value, ...nodes(value.props.children)] : []
}
function text(value: any): string {
  if (Array.isArray(value)) return value.map(text).join('')
  if (value && typeof value === 'object') return text(value.props?.children)
  return value == null || typeof value === 'boolean' ? '' : String(value)
}
function harness(api: any) {
  const slots: any[] = []; let cursor = 0; let tree: any
  const internals = React.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE
  function render() {
    cursor = 0
    const old = internals.H
    internals.H = {
      useState(initial: any) {
        const i = cursor++
        if (!(i in slots)) slots[i] = typeof initial === 'function' ? initial() : initial
        return [slots[i], (next: any) => { slots[i] = typeof next === 'function' ? next(slots[i]) : next }]
      },
      useRef(initial: any) {
        const i = cursor++
        if (!(i in slots)) slots[i] = { current: initial }
        return slots[i]
      },
    }
    try { tree = ProspectComposer({ api }) } finally { internals.H = old }
    return tree
  }
  function find(type: string, predicate: (node: Element) => boolean) {
    render()
    const found = nodes(tree).find((node) => node.type === type && predicate(node))
    if (!found) throw new Error('Missing element ' + type)
    return found
  }
  return {
    render,
    html: () => renderToStaticMarkup(render()),
    button: (label: string) => find('button', (node) => text(node).includes(label)),
    input: (type: string) => find('input', (node) => node.props.type === type),
    title: () => find('input', (node) => node.props.maxLength === 200),
    async file(selected: any) { this.input('file').props.onChange({ target: { files: [selected] } }); await flush() },
    async click(label: string) {
      const node = this.button(label)
      expect(node.props.disabled).toBeFalsy()
      node.props.onClick(); await flush()
    },
  }
}
const checks: { name: string; outcome: string }[] = []
function control(name: string, run: () => Promise<void>) {
  test(name, async () => {
    try { await run(); checks.push({ name, outcome: 'PASS' }) }
    catch (error) { checks.push({ name, outcome: 'FAIL' }); throw error }
  })
}

control('ambiguous upload retries exactly and same-tick repeated click sends once', async () => {
  const calls: any[] = []
  let reject: (error: Error) => void = () => {}
  const ui = harness({ uploadAnalysisInput: (body: any) => {
    calls.push(body); return new Promise((_resolve, fail) => { reject = fail })
  } })
  await ui.file(csv())
  const click = ui.button('Review portfolio').props.onClick
  click(); click(); await flush()
  expect(calls).toHaveLength(1)
  expect(ui.input('file').props.onChange).toBeFunction()
  expect(ui.html()).toContain('<fieldset disabled=""')
  reject(new Error('ambiguous')); await flush()
  const first = JSON.stringify(calls[0])
  await ui.click('Retry same upload')
  expect(calls).toHaveLength(2)
  expect(JSON.stringify(calls[1])).toBe(first)
  expect(atob(calls[1].csv_base64)).toContain('9007199254740993.01')
  reject(new Error('ambiguous')); await flush()
})

control('refresh clears old result, keeps parent and freezes ambiguous refresh retry', async () => {
  const calls: any[] = []
  const ui = harness({ uploadAnalysisInput: async (body: any) => {
    calls.push(body); if (calls.length === 1) return structuredClone(accepted)
    throw new Error('ambiguous refresh')
  } })
  await ui.file(csv()); await ui.click('Review portfolio')
  expect(ui.html()).toContain('prospect-review')
  await ui.click('Refresh source data')
  expect(ui.html()).not.toContain('prospect-review')
  expect(ui.html()).not.toContain('Generate Overview')
  expect(calls[1].supersedes_input_id).toBe(accepted.input_id)
  expect(calls[1].upload_token).not.toBe(calls[0].upload_token)
  await ui.click('Retry same upload')
  expect(calls[2]).toEqual(calls[1])
})

control('analysis retry freezes exact input-only body; deliberate title edit creates new request', async () => {
  const calls: any[][] = []
  const ui = harness({ uploadAnalysisInput: async () => structuredClone(accepted),
    submitAnalysisRequest: async (...args: any[]) => { calls.push(args); throw new Error('ambiguous') } })
  await ui.file(csv()); await ui.click('Review portfolio'); await ui.click('Generate Overview')
  await ui.click('Retry same analysis request')
  expect(calls).toHaveLength(2)
  expect(calls[1]).toEqual(calls[0])
  expect(calls[0]).toHaveLength(1)
  expect(calls[0][0]).toMatchObject({ input_id: accepted.input_id, client_id: null,
    account_ids: [], snapshot_id: null, variant: 'overview', comparison_keys: [], report_title: null })
  ui.title().props.onChange({ target: { value: 'Revised title' } })
  await ui.click('Generate Overview')
  expect(calls[2][0].request_id).not.toBe(calls[0][0].request_id)
  expect(calls[2][0].report_title).toBe('Revised title')
})

control('successful analysis shows acceptance and disables a second submit', async () => {
  let submits = 0
  const ui = harness({ uploadAnalysisInput: async () => structuredClone(accepted),
    submitAnalysisRequest: async (body: any) => {
      submits++; return { requestId: body.request_id, stage: 'RECEIVED' }
    } })
  await ui.file(csv()); await ui.click('Review portfolio'); await ui.click('Generate Overview')
  expect(submits).toBe(1)
  expect(ui.button('Request accepted').props.disabled).toBe(true)
  expect(ui.html()).toContain('RECEIVED')
  expect(ui.html()).toContain('after generation and verification')
})

control('correction hides generate; deliberate option correction issues distinct upload', async () => {
  const calls: any[] = []
  const ui = harness({ uploadAnalysisInput: async (body: any) => {
    calls.push(body); return structuredClone(fixture.correction.response.data)
  } })
  await ui.file(csv()); await ui.click('Review portfolio')
  expect(ui.html()).toContain('CURRENCY_CONFIRMATION_REQUIRED')
  expect(ui.html()).not.toContain('Generate Overview')
  ui.input('checkbox').props.onChange({ target: { checked: true } })
  await ui.click('Review portfolio')
  expect(calls[1].declared_currency).toBe('USD')
  expect(calls[1].upload_token).not.toBe(calls[0].upload_token)
})

control('last file selection wins even when an earlier file read completes later', async () => {
  let complete: (value: ArrayBuffer) => void = () => {}
  const calls: any[] = []
  const ui = harness({ uploadAnalysisInput: async (body: any) => { calls.push(body); return accepted } })
  await ui.file({ name: 'old.csv', size: 20, arrayBuffer: () => new Promise((done) => { complete = done }) })
  await ui.file(csv('new.csv'))
  complete(new TextEncoder().encode('old bytes').buffer); await flush()
  await ui.click('Review portfolio')
  expect(calls[0].filename).toBe('new.csv')
  expect(atob(calls[0].csv_base64)).toContain('9007199254740993.01')
})

control('exact source amount strings render without number conversion; row cap is explicit', async () => {
  // Presentation fixture only: no claim that altered data has passed envelope/hash validation.
  const response = structuredClone(accepted)
  response.portfolio.holdings.total_dollars = '9007199254740993.01'
  response.portfolio.rows = Array.from({ length: 101 }, (_, i) => ({
    original: { identifier: 'ROW' + i, source_value_verbatim: '9007199254740993.01', quantity: { units: 'USD' } },
    analysis_dollars: '9007199254740993.01',
  }))
  const ui = harness({ uploadAnalysisInput: async () => response })
  await ui.file(csv()); await ui.click('Review portfolio')
  const html = ui.html()
  expect(html).toContain('9007199254740993.01')
  expect(html).not.toContain('9007199254740994')
  expect(html).toContain('101 source rows retained. Showing 100.')
  expect(html).toContain('ROW99')
  expect(html).not.toContain('ROW100')
})

control('live upload with NO-HANDLER performs zero transport and exposes retry state', async () => {
  let calls = 0
  const api = new LiveClient({ transport: { request: async () => { calls++; throw new Error('Unexpected transport') } } })
  const ui = harness(api)
  await ui.file(csv()); await ui.click('Review portfolio')
  expect(calls).toBe(0)
  expect(ui.html()).toContain('role="alert"')
  expect(ui.button('Retry same upload')).toBeDefined()
  await ui.click('Retry same upload')
  expect(calls).toBe(0)
})

control('remount demonstrably loses in-memory attempt; persistence is not claimed', async () => {
  const calls: any[] = []
  const api = { uploadAnalysisInput: async (body: any) => { calls.push(body); throw new Error('ambiguous') } }
  const first = harness(api)
  await first.file(csv()); await first.click('Review portfolio')
  const remounted = harness(api)
  expect(remounted.button('Review portfolio').props.disabled).toBe(true)
  await remounted.file(csv()); await remounted.click('Review portfolio')
  expect(calls[1].upload_token).not.toBe(calls[0].upload_token)
})

afterAll(() => {
  if (!process.env.IRPT_PORTAL_REVIEW_OUTPUT) return
  const paths = ['src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx',
    'src/pages/InvestorReporting/tabs/analysis/prospect.ts',
    'src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx']
  writeFileSync(process.env.IRPT_PORTAL_REVIEW_OUTPUT, JSON.stringify({
    pin: '2ddf111467348c4c81ae28e0c0b8aa80e1239152',
    method: 'Actual component functions and handlers with manual React hook storage and static DOM markup. No browser scheduler, runtime transport, reload persistence or live API proof.',
    source_sha256: Object.fromEntries(paths.map((path) => [path, createHash('sha256').update(readFileSync(resolve(root, path))).digest('hex')])),
    checks,
  }, null, 2) + '\n')
})
