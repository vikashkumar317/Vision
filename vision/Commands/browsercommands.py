from pynput.keyboard import Key,Controller

#command list for browsing
browsercommandset = [['write'],['open','new','window'],['open','new','incognito','window'],
['open','new','tab'],['reopen','last','closed','tab'],['jump','to','next','open','tab'],
['jump','to','previous','open','tab'],['minimize','current','window'],['close','current','window'],
['close','current','tab'],['quit','chrome'],['stop','loading','page'],['print','current','page'],
['save','current','page'],['reload','current','page'],['everything','on','page','bigger'],
['everything','on','page','smaller'],['everything','on','page','of','default','size'],
['delete','previous','word'],['go','to','top','of','page'],['go','to','end','of','page'],
['open','chrome','menu'],['open','find','bar'],['jump','to','next','match','of','find','bar','search'],
['jump','to','previous','match','of','find','bar','search'],['clear','browsing','data','option'],['go'],['start','mousehover'],
['stop','mousehover'],['likho'],['chrome','band','karo'],['mousehover','shuru','karo'],
['mousehover','band','karo'],['khojo'],['naya','window','kholo'],
['naya','incognito','window','kholo'],['naya','tab','kholo'],
['antim','band','tab','phir','kholo'],['agle','tab','par','jao'],
['pichhle','tab','par','jao'],['window','chhota','kare'],
['window','band','kare'],['tab','band','kare'],
['load','karna','band','karo'],['print','karo'],['save','karo'],
['reload','karo'],['page','bada','karo'],['page','chhota','karo'],
['page','default','karo'],['pichhla','shabad','hataye'],['upar','jao'],['niche','jao'],
['chrome','menu','khole'],['find','bar','khole'],['browsing','data','hatao'],
['agle','match','pas','jao'],['pichhle','match','pas','jao']]

browsercommandsdict = {'open new window' : [Key.ctrl,'n'] ,
'naya window kholo' : [Key.ctrl,'n'] ,
'open new incognito window' : [Key.ctrl,Key.shift,'n'] ,
'naya incognito window kholo' : [Key.ctrl,Key.shift,'n'] ,
'open new tab' : [Key.ctrl,'t'] ,'naya tab kholo' : [Key.ctrl,'t'] ,
'reopen last closed tab' : [Key.ctrl,Key.shift,'t'] ,
'antim band tab phir se kholo' : [Key.ctrl,Key.shift,'t'] ,
 'jump to next open tab' : [Key.ctrl,Key.tab] ,
 'agle tab par jao' : [Key.ctrl,Key.tab] ,
'jump to previous open tab' : [Key.ctrl,Key.shift,Key.tab] ,
'pichhle tab par jao' : [Key.ctrl,Key.shift,Key.tab] ,
'minimize current window' : [Key.alt,Key.space,'n'] ,
'window chhota kare' : [Key.alt,Key.space,'n'] ,
'close current window' : [Key.alt,Key.f4] ,
'window band kare' : [Key.alt,Key.f4] ,
'close current tab' : [Key.ctrl,'w'] ,
'tab band kare' : [Key.ctrl,'w'] ,
'quit chrome' : [Key.ctrl,Key.shift,'q'],
'chrome band karo' : [Key.ctrl,Key.shift,'q'],
'stop loading page' : [Key.esc],
'load karna band karo' : [Key.esc],
'print current page' : [Key.ctrl,'p'] ,
'print karo' : [Key.ctrl,'p'] ,
'save current page' : [Key.ctrl,'s'] ,
'save karo' : [Key.ctrl,'s'] ,
'reload current page' : [Key.ctrl,'r'] ,
'reload karo' : [Key.ctrl,'r'] ,
'everything on page bigger' : [Key.ctrl,'+'] ,
'page bada karo' : [Key.ctrl,'+'] ,
'everything on page smaller' : [Key.ctrl,'-'] ,
'page chhota karo' : [Key.ctrl,'-'] ,
'everything on page of default size' : [Key.ctrl,'0'] ,
'page default karo' : [Key.ctrl,'0'] ,
'delete previous word' : [Key.ctrl,Key.backspace] ,
'pichhla shabad hataye' : [Key.ctrl,Key.backspace] ,
'go to top of page' : [Key.home] ,
'upar jao' : [Key.home] ,
'go to end of page' : [Key.end] ,
'niche jao' : [Key.end] ,
'open chrome menu' : [Key.alt,'e'] ,
'chrome menu khole' : [Key.alt,'e'] ,
'open find bar' : [Key.ctrl,'f'] ,
'find bar khole' : [Key.ctrl,'f'] ,
'jump to next match of find bar search' : [Key.ctrl,'g'] ,
'agle match pas jao' : [Key.ctrl,'g'] ,
'jump to previous match of find bar search' : [Key.ctrl,Key.shift,'g'],
'pichhle match pas jao' : [Key.ctrl,Key.shift,'g'],
'clear browsing data option' : [Key.ctrl,Key.shift,Key.delete],
'browsing data hatao' : [Key.ctrl,Key.shift,Key.delete],
'go':[Key.enter],'khojo':[Key.enter]
}
