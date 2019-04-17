from StringIO import StringIO
import re

class Buffer:
    def load_buffer(self):
        arq = open('aici.c', 'r')
        text = arq.read()
        text = self.strip_comments(text).splitlines()


        buffer = []
        cont = 1

        # The buffer size can be changed by changing cont
        for line in text:
            buffer.append(line)
            # text = arq.readline()
            cont += 1

            if cont == 10 or line == '':
                # Return a full buffer
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reset the buffer
                buffer = []

        arq.close()

    def strip_comments(self, text):
        return re.sub('/\\*+[^*]*\\*+(?:[^/*][^*]*\\*+)*/', '', text, flags=re.S)

