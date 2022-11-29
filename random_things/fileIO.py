# -------------open-------------
# parameter encoding is use to determinate a formatting


def open_archive(arg='r'):
    a = arg
    read_test = open('test', a, encoding='utf8')
    return read_test


# -------------read-------------
"""read_test = open_archive('r')"""

# unique variable
'''print(read_test.read())'''

# method readline(s)
'''print(read_test.readline(), end='')'''  # the parameter inside readline('here'),
# say a number from characters than you want show on the line
'''print(read_test.readline())'''  # more of one read line, makes the others lines be read
'''print(read_test.readline())'''  # if pass the number lines return nothing

'''print(read_test.readlines()[1])'''  # this will return a list with a lines in the file
# or too list(read_test()), [] does return a specific line(slicing(fatiamento))
# in this case: [0:2] all, [1] line2 [0] line 1
"""print(read_test.readlines())  # return a empty list"""

# line to line
'''for i in read_test:
    print(i, end='')'''

# -------------write-------------
# create a file if not exist and if exist delete all rewrite all file
"""delete_writing = open_archive('w')
delete_writing.write("daledal")"""

# concatenate a new line on file, give an append in list of the readlines
# Abra o arquivo (leitura)
'''arquivo = open_archive('r')'''
'''conteudo = arquivo.readlines()'''

# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
'''conteudo.append('\nnew line')'''

# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
'''arquivo = open_archive('w')'''
'''arquivo.writelines(conteudo)'''
'''arquivo.close()'''

# concatenate a new line on file, with parameter a
# create a file if not exist
'''concatenate = open_archive('a')'''
'''concatenate.write('\n        ,  new line')'''

# overwriting a file
'''overwriting = open_archive('w')'''
'''overwriting.write('overwriting a doc')'''

# -------------x-------------
# create if not exist a file and opening a write mode(if the file exist call a error)
"""create_write = open_archive('x')
create_write.write("hello there")"""

# -------------bytes-------------
# read in bytes(see this another day)

# -------------tests-------------
'''tests = open_archive('r')'''
'''tests.readline()'''
'''print(tests.tell())'''  # return a position of the character on file, in this case the next character is 46
# so return th 46 | this is good to know how many characters have a line, text etc...

'''tests.seek(162)'''  # set a position of the character to start read, write
'''print(tests.readline())'''

'''tests.flush()'''  # Python file method flush() flushes the internal buffer, like stdio's fflush.
# This may be a no-op on some file-like objects.
# Python automatically flushes the files when closing them. But you may want to flush the data before closing any file.

"""
# ao abrir um arquivo como escrita para leitura ele é apagado e da erro
test = open_archive('r')
print(test.readline())"""

# the 'r+' makes a read commands and write commands work, but if have a command from read it has total priority by the
# write command(makes write command don't work)
# 'r+' makes than write command write in the start text file, replacing the first characters in the first line
# different of just 'r' with write command this don't present error
'''test = open_archive('r+')
test.write("5")'''

# delete all file with command read, and delete and write with command write
# different of just 'w' with read command this don't present error
"""test = open_archive('w+')
test.read("5")"""

# write on the end file, don't deleted anything
# different of just 'a' with read command this don't present error
"""test = open_archive('a+')
test.write("test 1\n")"""


# -------------close-------------
# if don't close the file the modifies will be applied
# close the file
"""arquivo = open_archive('r')
conteudo_arquivo = arquivo.read()
print(conteudo_arquivo)
print('Arquivo fechado? {}'.format(arquivo.closed))
if not arquivo.closed:
    arquivo.close()
print('Arquivo fechado? {}'.format(arquivo.closed))"""

# close file with with
"""with open_archive('r') as arquivo:
    print('Arquivo fechado? {}'.format(arquivo.closed))
    print(arquivo.read())
print("Leitura do arquivo finalizada.")
print('Arquivo fechado? {}'.format(arquivo.closed))
"""
