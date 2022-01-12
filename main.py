from sys import argv
from pathlib import Path
from mega import Mega
import zipfile
read_buffer_size = 1024
chunk_size = 1024 * 100000
mega = Mega()
email = 'bhaskar.reddy6666666@gmail.com'
password = 'Townhall8@'
#m = mega.login(email, password)


def downloadmega():
     m = mega.login(email, password)
     try:
         x = m.find('ooo.zip')
         m.download(x, 'movie', 'x.zip')
     except:
         pass

     zipextract()


def zipextract():
    with zipfile.ZipFile('movie/x.zip', 'r') as zip_ref:
        zip_ref.extractall('xyz')

    _join('xyz/oo')



def _chunk_file(file, extension):
    current_chunk_size = 0
    current_chunk = 1
    done_reading = False
    while not done_reading:
        with open(f'{current_chunk}{extension}.zip', 'ab')as chunk:
            while True:
                bfr = file.read(read_buffer_size)
                if not bfr:
                    done_reading = True
                    break

                chunk.write(bfr)
                current_chunk_size += len(bfr)
                if current_chunk_size + read_buffer_size > chunk_size:
                    current_chunk += 1
                    current_chunk_size = 0
                    break



def _join(y):
    q = Path.cwd()
    p = q / y
    chunks = list(p.rglob('*.zip'))
    chunks.sort()
    extension = chunks[0].suffixes[0]
    with open(f'join{extension}','ab') as file:
        for chunk in chunks:
            with open(chunk, 'rb')as piece:
                while True:
                    bfr = piece.read(read_buffer_size)
                    if not bfr:
                        break
                    file.write(bfr)



def main():
    downloadmega()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
