from pyrogram import Client
with Client("c", 1038911,"94d21cd31f1d54ff715ead95b1777bc1", in_memory = True) as cli:
  ses = cli.export_session_string()
  print(ses)
