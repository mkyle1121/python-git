# -*- mode: python -*-

block_cipher = None


a = Analysis(['chat_Client_GUI_Video.py'],
             pathex=['C:\\Users\\Mike Kyle\\PycharmProjects\\All_Python\\zz_my_python_stuff\\Chat Client'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='chat_Client_GUI_Video',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
