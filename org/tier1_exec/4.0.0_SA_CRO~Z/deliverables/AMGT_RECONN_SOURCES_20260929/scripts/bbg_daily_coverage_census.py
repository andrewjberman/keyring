import collections,datetime,json,pathlib,sys,time,gc
import pythoncom,win32com.client,win32process,pywintypes
sys.path.insert(0,str(pathlib.Path.cwd()))
from lib.trading_calendar import trading_days_between,calendar_source
sys.stdout.reconfigure(encoding='utf-8')
OUT=pathlib.Path('.runtime/amgt-reconn-daily-census-20260929').resolve();OUT.mkdir(exist_ok=True)
dates=trading_days_between('2024-12-31','2026-09-28')
tickers=['WCMG','GQGU','TSEL','BASG','ETFT','PCLG']
universe='['+','.join(repr(t+' US Equity') for t in tickers)+']'
todo=[d for d in dates if not (OUT/(str(d)+'.json')).exists()]
excel=None;book=None;sheets=[];pid=None
meta={'started':datetime.datetime.now().astimezone().isoformat(),'calendar':calendar_source(),'date_count':len(dates),'tickers':tickers}
def com(call):
 end=time.monotonic()+30
 while True:
  try:return call()
  except pywintypes.com_error as e:
   if e.hresult not in [-2147418111,-2147417846] or time.monotonic()>end:raise
   pythoncom.PumpWaitingMessages();time.sleep(.2)
try:
 excel=win32com.client.DispatchEx('Excel.Application');excel.Visible=False;excel.DisplayAlerts=False
 pid=win32process.GetWindowThreadProcessId(excel.Hwnd)[1];meta['pid']=pid
 (OUT/'run.json').write_text(json.dumps(meta,indent=2))
 with (OUT/'runs.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(meta)+'\n')
 excel.Workbooks.Open('C:/blp/API/Office Tools/BloombergUI.xla')
 excel.RegisterXLL('C:/blp/API/Office Tools/blpxladdin.xll');excel.RegisterXLL('C:/blp/API/Office Tools/brtdwrap.xll')
 book=excel.Workbooks.Add()
 for i in range(20):
  sh=book.Worksheets.Add();sh.Name=f'probe{i:02}';sheets.append(sh)
 print('START',len(dates),'trading dates;',len(todo),'not yet captured',flush=True)
 for offset in range(0,len(todo),20):
  batch=todo[offset:offset+20]
  for sh,d in zip(sheets,batch):
   com(lambda:sh.Cells.ClearContents())
   query=f'get(id()) for(holdings({universe},dates={d}))'
   formula='=BQL.Query("'+query.replace('"','""')+'","showallcols=true")'
   com(lambda:setattr(sh.Range('A1'),'Formula',formula))
  com(lambda:excel.Calculate());started=time.monotonic();status={}
  while time.monotonic()-started<35:
   end=time.monotonic()+1
   while time.monotonic()<end:pythoncom.PumpWaitingMessages();time.sleep(.03)
   com(lambda:excel.Calculate())
   status={str(d):com(lambda:sh.Range('A1').Text) for sh,d in zip(sheets,batch)}
   if time.monotonic()-started>=3 and not any('Requesting' in v or 'Getting' in v for v in status.values()):break
  counts=collections.Counter()
  for sh,d in zip(sheets,batch):
   anchor=com(lambda:sh.Range('A1').Text)
   vals=com(lambda:sh.Range('A1:P500').Value)
   rows=[list(row) for row in vals if any(v is not None for v in row)]
   rows=[row[:max(i+1 for i,v in enumerate(row) if v is not None)] for row in rows]
   if com(lambda:sh.UsedRange.Rows.Count)>500:raise RuntimeError('Range cap exceeded')
   result={'requested_date':str(d),'at':datetime.datetime.now().astimezone().isoformat(),'query':f'get(id()) for(holdings({universe},dates={d}))','anchor':anchor,'rows':rows}
   if anchor=='ID':
    h=rows[0];rr=[dict(zip(h,r)) for r in rows[1:]]
    if not all(str(r.get('DATES'))[:10]==str(d) for r in rr):raise RuntimeError('Requested-date provenance mismatch')
    counts.update(r['ORIG_IDS'].split()[0] for r in rr)
   (OUT/(str(d)+'.json')).write_text(json.dumps(result,default=str),encoding='utf-8')
  print('BATCH',min(offset+len(batch),len(todo)),'/',len(todo),str(batch[0]),str(batch[-1]),'rows',dict(counts),'errors',sum(v!='ID' for v in status.values()),flush=True)
 meta['completed']=datetime.datetime.now().astimezone().isoformat()
 (OUT/'run.json').write_text(json.dumps(meta,indent=2))
finally:
 if book is not None:book.Close(SaveChanges=False)
 if excel is not None:excel.Quit()
 sheets.clear();sh=None;book=None;excel=None;gc.collect()
